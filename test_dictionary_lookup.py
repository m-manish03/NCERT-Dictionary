import glob
import json
import os
import sys
import textwrap
from collections import OrderedDict


class Color:
    ENABLED = (
        hasattr(sys.stdout, "isatty")
        and sys.stdout.isatty()
        and os.environ.get("TERM") != "dumb"
        and "--no-color" not in sys.argv
    )

    RESET = "\033[0m" if ENABLED else ""
    BOLD = "\033[1m" if ENABLED else ""
    CHAPTER = "\033[1;36m" if ENABLED else ""
    CONCEPT = "\033[1;33m" if ENABLED else ""
    LABEL = "\033[1;32m" if ENABLED else ""
    DEFINITION = "\033[0;37m" if ENABLED else ""
    BULLET = "\033[0;35m" if ENABLED else ""
    BADGE = "\033[1;34m" if ENABLED else ""
    WARNING = "\033[0;33m" if ENABLED else ""
    PROMPT = "\033[1;37m" if ENABLED else ""
    SEPARATOR = "\033[0;90m" if ENABLED else ""


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

SEPARATOR_LINE = "─" * 42

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
    file_paths = sorted(glob.glob("data-json/Class*.json"))
    for path in file_paths:
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
    return records, file_paths


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


def available_metadata(records):
    classes = sorted({record["class_num"] for record in records})
    subject_order = {"Science": 0, "Mathematics": 1}
    subjects = sorted(
        {record["subject"] for record in records},
        key=lambda subject: (subject_order.get(subject, 99), subject),
    )
    return classes, subjects


def validate_class_selection(raw_value, available_classes):
    value = raw_value.strip().lower()
    if value == "all":
        return "all"

    if value.isdigit():
        class_num = int(value)
        if class_num in available_classes:
            return class_num

    return None


def filter_records_by_class(records, class_selection):
    if class_selection == "all":
        return records
    return [record for record in records if record["class_num"] == class_selection]


def search(records, query, class_selection):
    filtered_records = filter_records_by_class(records, class_selection)
    term = normalize_query(query)
    if not term:
        return []

    term_lower = term.lower()

    concept_matches = [
        record
        for record in filtered_records
        if term_lower in record["concept_title"].lower()
    ]
    if concept_matches:
        return sorted(concept_matches, key=sort_key)

    chapter_matches = [
        record
        for record in filtered_records
        if term_lower in record["chapter_title"].lower()
    ]
    return sorted(chapter_matches, key=sort_key)


def group_by_chapter(records):
    grouped = OrderedDict()
    for record in records:
        grouped.setdefault(chapter_key(record), []).append(record)
    return grouped


def wrap_visible_text(text, first_prefix, continuation_prefix, width=80):
    available_first = max(1, width - len(first_prefix))
    available_next = max(1, width - len(continuation_prefix))
    wrapped = textwrap.wrap(
        str(text),
        width=available_first,
        break_long_words=False,
        break_on_hyphens=False,
    )

    if not wrapped:
        wrapped = [""]

    lines = [first_prefix + wrapped[0]]
    for line in wrapped[1:]:
        extra = textwrap.wrap(
            line,
            width=available_next,
            break_long_words=False,
            break_on_hyphens=False,
        )
        if extra:
            lines.extend(continuation_prefix + item for item in extra)
        else:
            lines.append(continuation_prefix)
    return lines


def print_labeled_text(label, text):
    first_prefix = f"    {label}: "
    continuation_prefix = " " * len(first_prefix)
    wrapped_lines = wrap_visible_text(text, first_prefix, continuation_prefix)
    first_text = wrapped_lines[0][len(first_prefix) :]
    print(
        f"    {Color.LABEL}{label}:{Color.RESET} "
        f"{Color.DEFINITION}{first_text}{Color.RESET}"
    )
    for line in wrapped_lines[1:]:
        continuation_text = line[len(continuation_prefix) :]
        print(f"{continuation_prefix}{Color.DEFINITION}{continuation_text}{Color.RESET}")


def print_bullet_item(item):
    first_prefix = "      • "
    continuation_prefix = " " * len(first_prefix)
    wrapped_lines = wrap_visible_text(item, first_prefix, continuation_prefix)
    first_text = wrapped_lines[0][len(first_prefix) :]
    print(f"      {Color.BULLET}• {first_text}{Color.RESET}")
    for line in wrapped_lines[1:]:
        continuation_text = line[len(continuation_prefix) :]
        print(f"{continuation_prefix}{Color.BULLET}{continuation_text}{Color.RESET}")


def print_concept(record):
    print(
        f"  {Color.CONCEPT}Concept {record['concept_id']}: "
        f"{record['concept_title']}{Color.RESET}"
    )
    print_labeled_text("Definition", record["definition"])

    if record["formulae"]:
        print(f"    {Color.LABEL}Formulae:{Color.RESET}")
        for item in record["formulae"]:
            print_bullet_item(item)

    if record["examples"]:
        print(f"    {Color.LABEL}Examples:{Color.RESET}")
        for item in record["examples"]:
            print_bullet_item(item)


def class_scope_label(class_selection):
    if class_selection == "all":
        return "all classes"
    return f"Class {class_selection}"


def print_no_results(query, class_selection):
    print(
        f'{Color.WARNING}No concepts found for "{query}" in '
        f"{class_scope_label(class_selection)}.{Color.RESET}"
    )
    print(
        f"{Color.WARNING}More classes will be available as additional files are added."
        f"{Color.RESET}"
    )


def print_separator():
    print(f"{Color.SEPARATOR}{SEPARATOR_LINE}{Color.RESET}")


def print_results(records, original_query, class_selection):
    if not records:
        print_no_results(original_query, class_selection)
        return

    grouped = group_by_chapter(records)
    groups = list(grouped.items())

    for group_index, (current_chapter, chapter_records) in enumerate(groups):
        class_num, subject, chapter_number, chapter_title = current_chapter
        print(
            f"{Color.CHAPTER}Chapter {chapter_number}: {chapter_title}{Color.RESET}  "
            f"{Color.BADGE}[Class {class_num} {subject}]{Color.RESET}"
        )

        for concept_index, record in enumerate(chapter_records):
            if concept_index > 0:
                print()
            print_concept(record)

        if group_index < len(groups) - 1:
            print()
            print_separator()
            print()


def prompt_for_class(available_classes):
    while True:
        raw_value = input(
            f"{Color.PROMPT}Enter class ({available_classes[0]}-{available_classes[-1]}) "
            f"or 'all' for all classes: {Color.RESET}"
        )
        selection = validate_class_selection(raw_value, available_classes)
        if selection is not None:
            return selection
        print("Invalid class. Please enter 6, 7, 8, 9, 10, or 'all'.")


def prompt_for_updated_class(current_selection, available_classes):
    current_label = "all" if current_selection == "all" else str(current_selection)
    raw_value = input(
        f"{Color.PROMPT}Class (current: {current_label} — press Enter to keep, "
        f"or change): {Color.RESET}"
    ).strip()

    if raw_value == "":
        return current_selection

    selection = validate_class_selection(raw_value, available_classes)
    if selection is not None:
        return selection

    print("Invalid class. Please enter 6, 7, 8, 9, 10, or 'all'.")
    return prompt_for_updated_class(current_selection, available_classes)


def print_header(classes, subjects):
    class_text = ", ".join(str(class_num) for class_num in classes)
    subject_text = ", ".join(subjects)
    print("NCERT Concept Dictionary")
    print(f"Available: Class {class_text}  |  {subject_text}")


def run_autotests(records):
    tests = [
        ('── Autotest 1 ── "what is nutrition"  (class: all)', "what is nutrition"),
        ('── Autotest 2 ── "photosynthesis"     (class: all)', "photosynthesis"),
        ('── Autotest 3 ── "force"              (class: all)', "force"),
        ('── Autotest 4 ── "quadratic"          (class: all)', "quadratic"),
        ('── Autotest 5 ── "buoyancy"           (class: all)', "buoyancy"),
    ]

    for index, (label, query) in enumerate(tests):
        print(label)
        print_results(search(records, query, "all"), normalize_query(query), "all")
        if index < len(tests) - 1:
            print()
            print()


def interactive_loop(records, available_classes, initial_selection):
    current_selection = initial_selection

    while True:
        query = input(f"{Color.PROMPT}Search: {Color.RESET}").strip()
        if query.lower() in {"quit", "exit", "q"}:
            print("Goodbye.")
            break

        current_selection = prompt_for_updated_class(current_selection, available_classes)
        normalized_query = normalize_query(query)
        print_results(search(records, query, current_selection), normalized_query, current_selection)
        print()


def main():
    records, file_paths = load_index()
    if not records:
        print("No files matching 'data-json/Class*.json' were found.")
        return

    classes, subjects = available_metadata(records)
    print_header(classes, subjects)
    initial_selection = prompt_for_class(classes)
    print()
    run_autotests(records)
    print()
    print_separator()
    print()
    interactive_loop(records, classes, initial_selection)


if __name__ == "__main__":
    main()
