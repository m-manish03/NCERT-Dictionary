import glob
import json
import sys
import textwrap
from collections import OrderedDict


QUESTION_PREFIXES = [
    "what is",
    "what are",
    "explain",
    "define",
    "tell me about",
    "describe",
    "how does",
    "what do you mean by",
    "give me",
    "show me",
]

BULLET = "•"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


def concept_id_key(concept_id):
    parts = str(concept_id).split(".")
    key = []
    for part in parts:
        if part.isdigit():
            key.append((0, int(part)))
        else:
            key.append((1, part.lower()))
    return tuple(key)


def sort_key(record):
    return (
        record["class_num"],
        record["chapter_number"],
        concept_id_key(record["concept_id"]),
    )


def normalize_query(query):
    normalized = query.strip()
    lowered = normalized.lower()

    for prefix in QUESTION_PREFIXES:
        if lowered.startswith(prefix):
            normalized = normalized[len(prefix) :].strip()
            break

    return normalized


def load_index():
    records = []
    for path in sorted(glob.glob("Class*.json")):
        with open(path, "r", encoding="utf-8") as handle:
            data = json.load(handle)

        for chapter in data.get("chapters", []):
            for concept in chapter.get("concepts", []):
                records.append(
                    {
                        "class_num": data["class"],
                        "subject": data["subject"],
                        "chapter_number": chapter["number"],
                        "chapter_title": chapter["title"],
                        "concept_id": concept["id"],
                        "concept_title": concept["title"],
                        "definition": concept["definition"],
                        "formulae": concept.get("formulae", []),
                        "examples": concept.get("examples", []),
                    }
                )
    return records


def record_key(record):
    return (
        record["class_num"],
        record["subject"],
        record["chapter_number"],
        record["chapter_title"],
        record["concept_id"],
    )


def chapter_key(record):
    return (
        record["class_num"],
        record["subject"],
        record["chapter_number"],
        record["chapter_title"],
    )


def search(records, query):
    term = normalize_query(query)
    if not term:
        return []

    term_lower = term.lower()

    concept_matches = [
        record
        for record in records
        if term_lower in record["concept_title"].lower()
    ]

    matched_chapters_from_concepts = {chapter_key(record) for record in concept_matches}
    chapter_title_matches = {
        chapter_key(record)
        for record in records
        if term_lower in record["chapter_title"].lower()
    }

    fallback_records = []
    for record in records:
        current_chapter = chapter_key(record)
        if (
            current_chapter in chapter_title_matches
            and current_chapter not in matched_chapters_from_concepts
        ):
            fallback_records.append(record)

    merged = OrderedDict()
    for record in sorted(concept_matches + fallback_records, key=sort_key):
        merged[record_key(record)] = record

    return list(merged.values())


def group_by_chapter(records):
    grouped = OrderedDict()
    for record in records:
        grouped.setdefault(chapter_key(record), []).append(record)
    return grouped


def format_wrapped_text(label, text):
    prefix = f"    {label}: "
    return textwrap.fill(
        str(text),
        width=80,
        initial_indent=prefix,
        subsequent_indent=" " * len(prefix),
        break_long_words=False,
        break_on_hyphens=False,
    )


def print_concept(record):
    print(f"  Concept {record['concept_id']}: {record['concept_title']}")
    print(format_wrapped_text("Definition", record["definition"]))

    if record["formulae"]:
        print("    Formulae:")
        for item in record["formulae"]:
            print(f"      {BULLET} {item}")

    if record["examples"]:
        print("    Examples:")
        for item in record["examples"]:
            wrapped = textwrap.fill(
                str(item),
                width=80,
                initial_indent=f"      {BULLET} ",
                subsequent_indent=" " * 8,
                break_long_words=False,
                break_on_hyphens=False,
            )
            print(wrapped)


def print_no_results(query):
    print(f'No concepts found for "{query}" in the loaded files (Class 7–8 only).')
    print("More classes will be available as additional files are added.")


def print_results(records, original_query):
    if not records:
        print_no_results(original_query)
        return

    grouped = group_by_chapter(records)
    groups = list(grouped.items())

    for group_index, (current_chapter, chapter_records) in enumerate(groups):
        class_num, subject, chapter_number, chapter_title = current_chapter
        print(f"Chapter {chapter_number}: {chapter_title}  [Class {class_num} {subject}]")

        for concept_index, record in enumerate(chapter_records):
            if concept_index > 0:
                print()
            print_concept(record)

        if group_index < len(groups) - 1:
            print()
            print()


def run_test_queries(records):
    tests = [
        'Test 1: "what is nutrition"',
        'Test 2: "photosynthesis"',
        'Test 3: "quadratic"',
        'Test 4: "force"',
        'Test 5: "what is buoyancy"',
    ]

    for index, label in enumerate(tests):
        query = label.split(": ", 1)[1].strip().strip('"')
        print(label)
        print_results(search(records, query), normalize_query(query))
        if index < len(tests) - 1:
            print()
            print()


def interactive_loop(records):
    while True:
        query = input("Search concept (or type 'quit'/'exit'): ").strip()
        if query.lower() in {"quit", "exit"}:
            print("Exiting dictionary lookup.")
            break

        print_results(search(records, query), normalize_query(query))
        print()


def main():
    records = load_index()
    if not records:
        print("No files matching 'Class*.json' were found in the current directory.")
        return

    print(
        f"Loaded {len(records)} concepts from {len(glob.glob('Class*.json'))} JSON files."
    )
    print()
    run_test_queries(records)
    print()
    interactive_loop(records)


if __name__ == "__main__":
    main()
