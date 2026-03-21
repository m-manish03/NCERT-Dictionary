1

# A SQUARE AND A CUBE

Queen Ratnamanjuri had a will written that described her fortune of ratnas (precious stones) and also included a puzzle. Her son Khoisnam and their 99 relatives were invited to the reading of her will. She wanted to leave all of her ratnas to her son, but she knew that if she did so, all their relatives would pester Khoisnam forever. She hoped that she had taught him everything he needed to know about solving puzzles. She left the following note in her will-

"I have created a puzzle. If all 100 of you answer it at the same time, you will share the ratnas equally. However, if you are the first one to solve the problem, you will get to keep the entire inheritance to yourself. Good luck."

The minister took Khoisnam and his 99 relatives to a secret room in the mansion containing 100 lockers.

The minister explained— "Each person is assigned a number from 1 to 100.

Person 1 opens every locker.   
• Person 2 toggles every 2nd locker i.e., closes it if it isopen, opens it if it is closed).   
Person 3 toggles every 3rd locker (3rd, 6th, 9th, ... and so on).   
Person 4 toggles every 4th locker (4th, 8th, 12th, .. and so on).

This continues until all 100 get their turn.

In the end, only some lockers remain open. The open lockers reveal the code to the fortune in the safe."

? Before the process begins, Khoisnam realises that he already knows which lockers will be open at the end. How did he figure out the answer?

Hint: Find out how many times each locker is toggled.

If a locker is toggled an odd number of times, it will be open. Otherwise, it will be closed. The number of times a locker is toggled is the same as the number of factors of the locker number. For example, for locker #6, Person 1 opens it, Person 2 closes it, Person 3 opens it and Person 6 closes it. The numbers 1, 2, 3, and 6 are factors of 6. If the number of factors is even, the locker will be toggled by an even number of people and it will eventually be closed.

Note that each factor of a number has a 'partner factor' so that the product of the pair of factors yields the given number. Here, 1 and 6 form a pair of partner factors of 6, and 2 and 3 form another pair.

6:   
$1 \times 6$   
$2 \times 3$   
Factors are 1, 2, 3 and 6.

Does every number have an even number of factors?

1:   
$1 \times 1$   
The only factor is 1. 4:   
$1 \times 4$   
$2 \times 2$   
Factors are 1, 2 and 4. 9:   
$1 \times 9$   
$3 \times 3$   
Factors are 1, 3 and 9.

We see in some cases, like $2 \times 2$ , that the numbers in the pair are the same.

$\textcircled{7}$ Can you use this insight to find more numbers with an odd number of factors?

For instance, 36 has a factor pair $6 \times 6$ where both numbers are 6. Does this number have an odd number of factors? If every factor of 36 other than 6 has a different factor as its partner, then we can be sure that 36 has an odd number of factors. Check if this is true.

Hence all the following numbers have an odd number of factors —

$$
1 \times 1 , 2 \times 2 , 3 \times 3 , 4 \times 4 , . . .
$$

A number that can be expressed as the product of a number with itself is called a square number, or simply a square. The only numbers that have an odd number of factors are the squares, because they each have one factor which, when multiplied by itself, equals the number. Therefore, every locker whose number is a square will remain open.

$\frac { 3 } { 2 }$ Write the locker numbers that remain open.

Khoisnam immediately collects word clues from these 10 lockers and reads, “The passcode consists of the first five locker numbers that were touched exactly twice."

Which are these five lockers?

The lockers that are toggled twice are the prime numbers, since each prime number has 1 and the number itself as factors. So, the code is 2-3-5-7-11.

# 1.1 Square Numbers

Why are the numbers, 1, 4, 9, 16, .., called squares? We know that the number of unit squares in a square (the area of a square) is the product of its sides. The table below gives the areas of squares with different sides. —

<table><tr><td rowspan=1 colspan=1>Sidelength(in units)</td><td rowspan=1 colspan=1>Area(in sq units)</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1 × 1 = 1 sq. unit</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2 × 2 = 4 sq. units</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3 × 3 = 9 sq. units</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4 × 4 = 16 sq. units</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>5 × 5 = 25 sq. units</td></tr><tr><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>10 × 10 = 100 sq. units</td></tr></table>

<table><tr><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1>P</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

We use the following notation for squares.

$$
\begin{array} { c } { { 1 \times 1 = \overline { { { 1 } } } ^ { 2 } = 1 } } \\ { { 2 \times 2 = 2 ^ { 2 } = 4 } } \\ { { 3 \times 3 = 3 ^ { 2 } = 9 , } } \\ { { 4 \times 4 = 4 ^ { 2 } = 1 6 } } \\ { { 5 \times 5 = 5 ^ { 2 } = 2 5 . } } \\ { { \vdots } } \end{array}
$$

In general, for any number $n$ , we write $n \times n = n ^ { 2 }$ , which is read as $\mathfrak { n }$ squared'.

Can we have a square of sidelength ${ \frac { 3 } { 5 } } \operatorname { o r } 2 . 5$ units?

Yes, ther re qu n $( \frac { 3 } { 5 } ) ^ { 2 } = ( \frac { 3 } { 5 } ) \times ( \frac { 3 } { 5 } ) = ( \frac { 9 } { 2 5 } )$ and $\left( 2 . 5 \right) ^ { 2 } = \left( 2 . 5 \right) \times \left( 2 . 5 \right) = 6 . 2 5$ .

The squares of natural numbers are called perfect squares. For example, 1, 4, 9, 16, 25, . are all perfect squares.

# Patterns and Properties of Perfect Squares

Find the squares of the first 30 natural numbers and fill in the table below.

<table><tr><td rowspan=1 colspan=1>1² = 1</td><td rowspan=1 colspan=1>11²= 121</td><td rowspan=1 colspan=1>21² = 441</td></tr><tr><td rowspan=1 colspan=1>2² = 4</td><td rowspan=1 colspan=1>12² =</td><td rowspan=1 colspan=1>22²=</td></tr><tr><td rowspan=1 colspan=1>3² = 9</td><td rowspan=1 colspan=1>13² =</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>4² = 16</td><td rowspan=1 colspan=1>14² =</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>5²= 25</td><td rowspan=1 colspan=1>15² =</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>6² =</td><td rowspan=1 colspan=1>16²=</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>7² =</td><td rowspan=1 colspan=1>17² =</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>8² =</td><td rowspan=1 colspan=1>18² =</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>9²2 =</td><td rowspan=1 colspan=1>192 =</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>10² =</td><td rowspan=1 colspan=1>202 =</td><td rowspan=1 colspan=1></td></tr></table>

$3$ What patterns do you notice? Share your observations and make conjectures.

Study the squares in the table above. What are the digits in the units places of these numbers? All these numbers end with 0, 1, 4, 5, 6 or 9. None of them end with 2, 3, 7 or 8.

If a number ends in 0, 1, 4, 5, 6 or 9, is it always a square?

The numbers 16 and 36 are both squares with 6 in the units place. However, 26, whose units digit is also 6, is not a square. Therefore, we cannot determine if a number is a square just by looking at the digit in the units place. But, the units digit can tell us when a number is not a square. If a number ends with 2, 3, 7, or 8, then we can definitely say that it is not a square.

$\textcircled{7}$ Write 5 numbers such that you can determine by looking at their units digit that they are not squares.

The squares, $1 ^ { 2 } , 9 ^ { 2 } , 1 1 ^ { 2 } , 1 9 ^ { 2 } , 2 1 ^ { 2 }$ ,and $2 9 ^ { 2 }$ , all have 1 in their units place. Write the next two squares. Notice that if a number has 1 or 9 in the units place, then its square ends in 1.

$\textcircled{7}$ Let us consider square numbers ending in $6 \colon 1 6 = 4 ^ { 2 }$ , $3 6 = 6 ^ { 2 }$ $1 9 6 = 1 4 ^ { 2 }$ , $2 5 6 = 1 6 ^ { 2 }$ , $5 7 6 = 2 4 ^ { 2 }$ ,and $6 7 6 = 2 6 ^ { 2 }$ .

Which of the following numbers have the digit 6 in the units place?

(i) 382 (ii) 34² (iii) 462 (iv) $5 6 ^ { 2 }$ (v) 74² (vi) 82²2 ? Find more such patterns by observing the numbers and their squares from the table you filled earlier.

Consider the following numbers and their squares.

102 = 100 We have 202 = 400 But we have one zero. 40² = 800 two zeroes. 1002 = 10000   
We have 200² = 40000 But we have   
two zeroes. 700²2 = 49000 four zeroes. 9002 =81000

? If a number contains 3 zeros at the end, how many zeros will its square have at the end?

$\frac { 3 } { 2 }$ What do you notice about the number of zeros at the end of a number and the number of zeros at the end of its square? Will this always happen? Can we say that squares can only have an even number of zeros at the end?

What can you say about the parity of a number and its square?

# Perfect Squares and Odd Numbers

Let us explore the differences between consecutive squares. What do you notice?

$$
4 - 1 = 3 \qquad 9 - 4 = 5 \qquad 1 6 - 9 = 7 \qquad 2 5 - 1 6 = 9
$$

ee if this pattern continues for the next few square numbers.

From this we observe that adding consecutive odd numbers starting from 1 gives consecutive square numbers, as shown below.

$$
\begin{array} { l l } { 1 = 1 } & { \bullet \bullet \bullet \bullet \bullet \bullet } \\ { 1 + 3 = 4 } & { \bullet \bullet \bullet \bullet \bullet \bullet } \\ { 1 + 3 + 5 = 9 } & { \bullet \bullet \bullet \bullet } \\ { 1 + 3 + 5 + 7 = 1 6 } & { \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet } \\ { 1 + 3 + 5 + 7 + 9 = 2 5 } & { \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet } \\ { 1 + 3 + 5 + 7 + 9 + 1 1 = 3 6 . } & { \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet \bullet } \end{array}
$$

Do you remember this pattern from Grade 6?

The picture below explains why each subsequent inverted L gives the next odd number:

We see that the sum of the first $n$ odd numbers is $n ^ { 2 }$ Alternatively, every square is a sum of successive odd numbers starting from 1.

In mathematics, sometimes arguments and reasoning can be presented without any words. Visual proofs can be complete by themselves.

Also, we can find out whether a number is a perfect square by successively subtracting odd numbers. Consider the number 25, successively subtract 1, 3, 5, .. until you get or cross over 0,

$$
2 5 - 1 = 2 4 \qquad 2 4 - 3 = 2 1 \qquad 2 1 - 5 = 1 6 \qquad 1 6 - 7 = 9 \qquad 9 - 9 = 0
$$

This means $2 5 = 1 + 3 + 5 + 7 + 9$ and is thus a perfect square. Since we subtracted the first five odd numbers, $2 5 = 5 ^ { 2 }$

Using the pattern above, find $3 6 ^ { 2 }$ , given that $3 5 ^ { 2 } = 1 2 2 5$ .

From the question we know that 1225 is the sum of the first 35 odd numbers. To find $3 6 ^ { 2 }$ , we need to add the 36th odd number to 1225.

How do we find the 36th odd number?

The 1st odd number is 1, 2nd odd number is 3, 3rd number is 5, .., 6th odd number is 11 and so on.

What is the $n ^ { t h }$ odd number?

The $n ^ { t h }$ odd number is $2 n { - } 1$ .

Therefore, the 36th odd number is 71.

By adding 71 to 1225, we get 1296, which is $3 6 ^ { 2 }$ .

Consider a number such as 38 that is not a square and subtract consecutive odd numbers starting from 1.

$$
\begin{array} { l l l l l } { { 3 8 - 1 = 3 7 } } & { { \ 3 7 - 3 = 3 4 } } & { { \ 3 4 - 5 = 2 9 } } & { { \ 2 9 - 7 = 2 2 } } & { { \ 2 2 - 9 = 1 3 } } \\ { { \nonumber } } & { { \ } } & { { \nonumber } } \\ { { 1 3 - 1 1 = 2 } } & { { \ 2 - 1 3 = - 1 1 } } & { { } } & { { } } \end{array}
$$

This shows that 38 cannot be expressed as a sum of consecutive odd numbers starting with 1.

Thus, we can say that a natural number is not a perfect square if it cannot be expressed as a sum of successive odd natural numbers starting from 1. We can use this result to find out whether a natural number is a perfect square.

? Find how many numbers lie between two consecutive perfect squares. Do you notice a pattern?

$\frac { 3 } { 2 }$ How many square numbers are there between 1 and 100? How many are between 101 and 200? Using the table of squares you filled earlier, enter the values below, tabulating the number of squares in each block of 100. What is the largest square less than 1000?

<table><tr><td>1-100 101-200</td><td>201-300 301-400</td><td>401-500</td></tr><tr><td>501-600 601-700</td><td>701-800 801-900</td><td>901-1000</td></tr></table>

# Perfect Squares and Triangular Numbers

Do you remember triangular numbers?

? Can you see any relation between triangular numbers and square numbers? Extend the pattern shown and draw the next term.

$$
1 + 3 = 4 = 2 ^ { 2 } \qquad 3 + 6 = 9 = 3 ^ { 2 } \qquad 6 + 1 0 = 1 6 = 4 ^ { 2 }
$$

# Square Roots

? The area of a square is 49 sq. cm. What is the length of its side? We know that $7 \times 7 = 4 9$ ,or $7 ^ { 2 } = 4 9$ .

So, the length of the side of a square with an area of 49 sq. cm is 7 cm.

We call 7 the square root of 49.

In general, if $\scriptstyle y = x ^ { 2 }$ then $\boldsymbol { x }$ is the square root of y.

? What is the square root of 64?

We know that $8 \times 8$ is 64. So, 8 is the square root of 64. What about $- 8 \times - 8 ?$ That is 64 too!

So, the square roots of 64 are $^ + 8$ and - 8.

Every perfect square has two integer square roots. One is positive and the other is negative. The square root of a number is denoted by $\surd$ Thus, ${ \sqrt { 6 4 } } = \pm 8$ and $\sqrt { 1 0 0 } = \pm 1 0$ . Note that $\sqrt { 8 ^ { 2 } } = \pm 8$ and ${ \sqrt { 1 0 ^ { 2 } } } = \pm 1 0$ . In general, ${ \sqrt { n ^ { 2 } } } = \pm n$ . In this chapter, we shall only consider the positive square root.

? Given a number, such as 576 or 327, how do we find out if it is a perfect square? If it is a perfect square, how can we find its square root?

We know that perfect squares end in 1, 4, 9, 6, 5, or an even number of zeros. But, it is not certain that a number that satisfies this condition is a square.

We can clearly say that 327 is not a perfect square. However, we cannot be sure that 576 is a perfect square.

1. We can list all the square numbers in sequence and find out whether 576 occurs among them. We know that $2 0 2 = 4 0 0$ , we can find squares of 21, 22, 23, .. and so on until we get 576 or a number greater than 576.

$$
2 0 ^ { 2 } = 4 0 0 \qquad 2 1 ^ { 2 } = 4 4 1 \qquad 2 2 ^ { 2 } = 4 8 4 \qquad 2 3 ^ { 2 } = 5 2 9 \qquad 2 4 ^ { 2 } = 5 7 6
$$

However, this process becomes inefficient for larger numbers.

2. Recall that every square can be expressed as a sum of consecutive odd numbers starting from 1. Consider $\sqrt { 8 1 }$ .

I $8 1 - 1 = 8 0$ $\begin{array} { c } { { 8 0 - 3 = 7 7 \quad 7 7 - 5 = 7 2 \quad 7 2 - 7 = 6 5 \quad 6 5 - 9 = 5 6 } } \\ { { \cdot \quad 4 5 - 1 3 = 3 2 \quad \quad 3 2 - 1 5 = 1 7 \quad \quad 1 7 - 1 7 = 0 } } \end{array}$

From 81, we successively subtracted consecutive odd numbers starting from 1 until we obtained 0 at the 9th step. Therefore ${ \sqrt { 8 1 } } = 9$ .

Can we find the square root of 729 using this method? Yes, but it will be time-consuming.

3.We know that a perfect square is obtained by multiplying an integer by itself. Will looking at a number's prime factorisation help in determining whether it is a perfect square?

Yes, if we can divide the prime factors of a number into two equal groups, then the product of the prime factors in either group combine to form the square root.

?Is 324 a perfect square?

$$
3 2 4 = 2 \times 2 \times 3 \times 3 \times 3 \times 3 .
$$

These can be grouped as

$$
\begin{array} { c } { { 3 2 4 = ( 2 \times 3 \times 3 ) \times ( 2 \times 3 \times 3 ) . } } \\ { { = ( 2 \times 3 \times 3 ) ^ { 2 } = 1 8 ^ { 2 } . } } \end{array}
$$

We can also write the prime factors in pairs. That is,

$$
3 2 4 = ( 2 \times 2 ) \times ( 3 \times 3 ) \times ( 3 \times 3 ) ,
$$

which shows that 324 is a perfect square. Thus,

$3 2 4 = ( 2 { \times } 3 { \times } 3 ) ^ { 2 } = 1 8 ^ { 2 } .$ Therefore, ${ \sqrt { 3 2 4 } } = 1 8$ .

$\textcircled{7}$ Is 156 a perfect square? The prime factorisation of 156 is $2 \times 2 \times 3 \times 1 3$ . We cannot pair up these factors. Therefore, 156 is not a perfect square.

$\textcircled{7}$ Find whether 1156 and 2800 are perfect squares using prime factorisation.

We can estimate the square root of larger perfect squares by looking at the closest perfect squares we are familiar with and then narrowing down the interval to search.

For example, to find $\sqrt { 1 9 3 6 }$ , we can reason as follows:

(i) 1936 is between 1600 $( 4 0 ^ { 2 } )$ and 2500 $( 5 0 ^ { 2 } )$ , so $4 0 < \sqrt { 1 9 3 6 } < 5 0 .$ .   
(ii) The last digit of 1936 is 6. So, the last digit of the square root must either be 4 or 6. It can be 44 or 46.   
(iii) If we calculate $4 5 ^ { 2 }$ , we can compare it with 1936 to halve the interval to search from 4050 to either 4045 or 4550. We can write $4 5 ^ { 2 }$ as $( 4 0 ~ + ~ 5 )$ $( 4 0 \div 5 ) = 4 0 ^ { 2 } + 2 \times 4 0 \times 5 + 5 ^ { 2 }$ $= 1 6 0 0 + 4 0 0 + 2 5 = 2 0 2 5$ .   
(iv) $2 0 2 5 > 1 9 3 6 . \mathrm { S } 0 , 4 0 < \sqrt { 1 9 3 6 } < 4 5$   
(v) From the observation in point b we can guess and then verify that $\sqrt { 1 9 3 6 }$ is 44.

Consider the following situations —

Aribam and Bijou play a game. One says a number and the other replies with its square root. Aribam starts. He says 25, and Bijou quickly responds with 5. Then Bijou says 81, and Aribam answers 9. The game goes on till Aribam says 250. Bijou is not able to answer because 250 is not a perfect square. Aribam asks Bijou if he can at least provide a number that is close to the square root of 250.

For this, Bijou needs to estimate the square root of 250.   
We know that $1 0 0 < 2 5 0 < 4 0 0$ and ${ \sqrt { 1 0 0 } } = 1 0$ and $\sqrt { 4 0 0 } = 2 0$ .   
So, $1 0 < \sqrt { 2 5 0 } < 2 0$ .

But, we are still not very close to the number whose square is 250. We know that $1 5 ^ { 2 } = 2 2 5$ and $1 6 ^ { 2 } = 2 5 6$ .

Therefore, $1 5 < { \sqrt { 2 5 0 } } < 1 6 .$ Since 256 is much closer to 250 than 225, $\sqrt { 2 5 0 }$ is approximately 16. We also know it is less than 16.

Here is another problem that requires estimating square roots.

Akhil has a square piece of cloth of area $1 2 5 ~ \mathrm { c m } ^ { 2 }$ .He wants to know if he can cut out a square handkerchief of side $1 5 ~ \mathrm { c m }$ If not, he wants to know the maximum size handkerchief that can be cut out from this piece of cloth with an integer side length.

125 is not a perfect square. The nearest perfect squares are $1 1 ^ { 2 } = 1 2 1$ and $1 2 ^ { 2 } = 1 4 4$ So the largest square handkerchief with integer side length that can be cut out from this piece of cloth has side length 11 cm.

# ? Figure it Out

1. Which of the following numbers are not perfect squares?

(i) 2032 (ii) 2048 (iii) 1027 (iv) 1089

2. Which one among $6 4 ^ { 2 }$ , $1 0 8 ^ { 2 }$ ,2922, $3 6 ^ { 2 }$ has last digit 4?

3. Given $1 2 5 ^ { 2 } = 1 5 6 2 5$ what is the value of $1 2 6 ^ { 2 } ?$

(i) $1 5 6 2 5 + 1 2 6$ (ii) $1 5 6 2 5 + 2 6 ^ { 2 }$ (iii) 15625 + 253 (iv) $1 5 6 2 5 + 2 5 1$ $\mathrm { ( v ) } 1 5 6 2 5 + 5 1 ^ { 2 }$

4.Find the length of the side of a square whose area is $4 4 1 ~ \mathrm { m } ^ { 2 }$ .

5. Find the smallest square number that is divisible by each of the following numbers: 4, 9, and 10.

6. Find the smallest number by which 9408 must be multiplied so that the product is a perfect square. Find the square root of the product.

7. How many numbers lie between the squares of the following numbers?

(i) 16 and 17 (ii) 99 and 100

8. In the following pattern, fill in the missing numbers:

$$
\begin{array} { c } { { 1 ^ { 2 } + 2 ^ { 2 } + 2 ^ { 2 } = 3 ^ { 2 } } } \\ { { 2 ^ { 2 } + 3 ^ { 2 } + 6 ^ { 2 } = 7 ^ { 2 } } } \\ { { 3 ^ { 2 } + 4 ^ { 2 } + 1 2 ^ { 2 } = 1 3 ^ { 2 } } } \\ { { 4 ^ { 2 } + 5 ^ { 2 } + 2 0 ^ { 2 } = ( \phantom { - } \underline { { { \bf \sigma } } } ) ^ { 2 } } } \\ { { 9 ^ { 2 } + 1 0 ^ { 2 } + ( \phantom { - } \underline { { { \bf \sigma } } } ) ^ { 2 } = ( \phantom { - } \underline { { { \bf \sigma } } } ) ^ { 2 } } } \end{array}
$$

9. How many tiny squares are there in the following picture? Write the prime factorisation of the number of tiny squares.

W I |

# 1.2 Cubic Numbers

You know the word cube from geometry. A cube is a solid figure all of whose all sides meet at right angles and are equal. How many cubes of side 1 cm make a cube of side $2 \mathrm { c m } ?$

How many cubes of side 1 cm will make a cube of side $3 \mathrm { c m } ?$

Consider the numbers 1, 8, 27, ..

These numbers are called perfect cubes. Can you see why they are named so?

Each of them is obtained by multiplying a number by itself three times. We note that

$$
\begin{array} { c } { 1 = 1 \times 1 \times 1 } \\ { 8 = 2 \times 2 \times 2 } \\ { 2 7 = 3 \times 3 \times 3 } \end{array}
$$

$3$ Is 9 a cube?

We see that $2 \times 2 \times 2 = 8$ and $3 \times 3 \times 3 = 2 7 .$ This shows that 9 is not a perfect cube. Nor is any number from 10 to 26.

$\frac { 3 } { 2 }$ Can you estimate the number of unit cubes in a cube with an edge length of 4 units?

It has 64 unit cubes! If you notice carefully, each layer of this cube has $4 \times 4$ unit cubes. Each square layer has 16 unit cubes $( 4 \times 4 )$ , and there are 4 such layers, so the total number of unit cubes is $4 \times 4 \times 4 = 6 4 .$ —

Since $5 ^ { 3 } = 5 \times 5 \times 5 = 1 2 5$ ,125 is a cube.

In general, for any number $\pmb { n }$ , we write the cube $\pmb { n } \times \pmb { n } \times \pmb { n }$ as $\pmb { n } ^ { 3 }$ .

Complete the table below.

<table><tr><td rowspan=1 colspan=1>1³ = 1</td><td rowspan=1 colspan=1>11³ = 1331</td></tr><tr><td rowspan=1 colspan=1>2^3}=8</td><td rowspan=1 colspan=1>12³ =</td></tr><tr><td rowspan=1 colspan=1>33 = 27</td><td rowspan=1 colspan=1>13³=2197</td></tr><tr><td rowspan=1 colspan=1>4³ = 64</td><td rowspan=1 colspan=1>14³3 = 2744</td></tr><tr><td rowspan=1 colspan=1>5³ = 125</td><td rowspan=1 colspan=1>15³ =</td></tr><tr><td rowspan=1 colspan=1>63</td><td rowspan=1 colspan=1>16³ =</td></tr><tr><td rowspan=1 colspan=1>7³ =</td><td rowspan=1 colspan=1>17³ = 4913</td></tr><tr><td rowspan=1 colspan=1>83 =</td><td rowspan=1 colspan=1>18³ = 5832</td></tr><tr><td rowspan=1 colspan=1>93=</td><td rowspan=1 colspan=1>19³ = 6859</td></tr><tr><td rowspan=1 colspan=1>10³ =</td><td rowspan=1 colspan=1>20³ =</td></tr></table>

?

What patterns do you notice in the table above?

$\frac { 3 } { 2 }$ We know that 0, 1, 4, 5, 6, 9 are the only last digits possible for squares. What are the possible last digits of cubes?

$\frac { 3 } { 2 }$ Similar to squares, can you find the number of cubes with 1 digit, 2 digits, and 3 digits? What do you observe?

Can a cube end with exactly two zeroes (00)? Explain.

Just as we can take squares of fractions/decimals — $( \frac { 4 } { 6 } ) ^ { 2 }$ , (13.08)², and $( - 6 ) ^ { 2 }$ — we also can compute cubes of such numbers — $( \frac { 4 } { 6 } ) ^ { 3 }$ , (13.08)3, and $( - 6 ) ^ { 3 }$ .

$$
( \frac { 4 } { 6 } ) ^ { 3 } = ( \frac { 4 } { 6 } ) \times ( \frac { 4 } { 6 } ) \times ( \frac { 4 } { 6 } ) = ( \frac { 6 4 } { 2 1 6 } )
$$

$$
( 1 3 . 0 8 ) ^ { 3 } = 1 3 . 0 8 \times 1 3 . 0 8 \times 1 3 . 0 8 = 2 2 3 7 . 8 1 0 1 1 2
$$

$$
( - 6 ) ^ { 3 } = - 6 \times - 6 \times - 6 = - 2 1 6 .
$$

# Taxicab Numbers

Once when Srinivasa Ramanujan was working with G. H. Hardy at the University of Cambridge, Hardy had come to visit Ramanujan at a hospital when he was ill. Hardy had ridden in a taxicab numbered 1729 and he remarked that 1729 was 'rather a dull number,' adding that he hoped that this was not a bad sign. Ramanujan immediately replied, "No, Hardy, it is a very interesting number. It is the smallest number that can be expressed as the sum of two cubes in two different ways".

$$
\begin{array} { l } { { 1 7 2 9 = 1 ^ { 3 } + 1 2 ^ { 3 } } } \\ { { \ } } \\ { { \leq 9 ^ { 3 } + 1 0 ^ { 3 } . } } \end{array}
$$

Because of this story, 1729 has since been known as the Hardy-Ramanujan Number. And numbers that can be expressed as the sum of two cubes in two different ways are called taxicab numbers.

? The next two taxicab numbers after 1729 are 4104 and 13832. Find the two ways in which each of these can be expressed as the sum of two positive cubes.

How did Ramanujan know this? Well, he loved numbers. All through his life, he tinkered with numbers. During Ramanujan's time in Cambridge, his colleagues often marveled at his ability to see deep patterns in numbers that seemed arbitrary to others. His colleague, John Littlewood, once said, "Every positive integer was one of his [Ramanujan's] personal friends".

# Perfect Cubes and Consecutive Odd Numbers

Consecutive odd numbers have a role to play with cubes too. Look at the following pattern:

$$
1 = 1 = 1 ^ { 3 }
$$

$$
3 + 5 = 8 = 2 ^ { 3 }
$$

$$
7 + 9 + 1 1 = 2 7 = 3 ^ { 3 }
$$

$$
1 3 + 1 5 + 1 7 + 1 9 = 6 4 = 4 ^ { 3 }
$$

$$
2 1 + 2 3 + 2 5 + 2 7 + 2 9 = 1 2 5 = 5 ^ { 3 }
$$

$$
3 1 + 3 3 + 3 5 + 3 7 + 3 9 + 4 1 = 2 1 6 = 6 ^ { 3 } .
$$

Later in this series, we get the following set of consecutive numbers:

$$
9 1 + 9 3 + 9 5 + 9 7 + 9 9 + 1 0 1 + 1 0 3 + 1 0 5 + 1 0 7 + 1 0 9 .
$$

D Can you tell what this sum is without doing the calculation?

# Cube Roots

We know that $8 = 2 ^ { 3 }$ .

We call 2 the cube root of 8 and denote this by $2 = { \sqrt [ { 3 } ] { 8 } }$ .

More generally, if $y = x ^ { 3 }$ , then $\boldsymbol { \chi }$ is the cube root of y. This is denoted by $x = \sqrt [ 3 ] { y }$ . So, $\sqrt [ 3 ] { 8 } = \sqrt [ 3 ] { 2 ^ { 3 } } = 2 .$

Similarly, ${ \sqrt [ 3 ] { 2 7 } } = { \sqrt [ 3 ] { 3 ^ { 3 } } } = 3$ and $\sqrt [ 3 ] { 1 0 0 0 } = \sqrt [ 3 ] { 1 0 ^ { 3 } } = 3 .$ In general, $\sqrt [ 3 ] { n ^ { 3 } } = n$

How do we find out if a number is a cube? Taking inspiration from the case of squares, let us see if we can use prime factorisations.

? Let us check if 3375 is a perfect cube.

$$
3 3 7 5 = 3 \times 3 \times 3 \times 5 \times 5 \times 5 .
$$

Can the factors be split into three identical groups? For 3375, we can form three groups of $\left( 3 \times 5 \right)$ . So,

$$
\begin{array} { c } { 3 3 7 5 = ( 3 \times 5 ) \times ( 3 \times 5 ) \times ( 3 \times 5 ) } \\ { = ( 3 \times 5 ) ^ { 3 } = 1 5 ^ { 3 } . } \end{array}
$$

Another way is to check if the factors can be grouped into triplet(s): $3 3 7 5 = ( 3 \times 3 \times 3 ) \times ( 5 \times 5 \times 5 ) = 3 ^ { 3 } \times 5 ^ { 3 }$ . This means $\sqrt [ 3 ] { 3 3 7 5 } = 1 5$ .

?

Is 500 a perfect cube?

$5 0 0 = 2 \times 2 \times 5 \times 5 \times 5 .$ We see that the factors cannot be split into three identical groups. Therefore, 500 is not a perfect cube.

<table><tr><td rowspan=1 colspan=1>Prime Factorisation of aNumber</td><td rowspan=1 colspan=1>PrimeFactorisation of its Cube</td></tr><tr><td rowspan=1 colspan=1>4 = 2 ×2</td><td rowspan=1 colspan=1>4³ = 64 = 2 ×2×2×2×2×2=2³2³</td></tr><tr><td rowspan=1 colspan=1>6=2×3</td><td rowspan=1 colspan=1>63 =216=2×2×2×3× 3×3 = 23×33</td></tr><tr><td rowspan=1 colspan=1>15 = 3×5</td><td rowspan=1 colspan=1>15³= 3375= 3×3×3×5×5×5= 3³×5³</td></tr><tr><td rowspan=1 colspan=1>12=2×2×3</td><td rowspan=1 colspan=1>123= 1728=2×2×222×2×2×333=2323 33</td></tr></table>

Observe that each prime factor of a number appears three times in the prime factorisation of its cube.

? Find the cube roots of these numbers:

(i) $\sqrt [ 3 ] { 6 4 } ~ =$ (ii) \512 = (i) 72 /

# Successive Differences

We know that the differences between consecutive perfect squares gives the sequence of odd numbers. Observe the figure below where the differences are computed successively for perfect squares. After two levels, all the differences are the same.

Perfect Squares 14916253   
Level 1 3 5 9 11   
Level 2 2 2 2 2 •••

? Compute successive differences over levels for perfect cubes until all the differences at a level are the same. What do you notice?

Perfect Cubes 127 64 125 216 ...

# 1.3 A Pinch of History

The first known list of perfect squares and perfect cubes was compiled by the Babylonians as far back as 1700 BCE. These lists, found on clay tablets, were used to quickly find square roots and cube roots in problems involving land measurement, architectural design, and other areas where geometric calculations were necessary.

In ancient Sanskrit works the term varga was used both for the square figure or its area, as well as the square power, and the term ghana was used both for the solid cube as well as the product of a number with itself three times. The fourth power was called varga-varga . These terms were used in India at least from the third century BCE.

# Aryabhata (499 CE) states

"A square figure of four equal sides and the number representing its area are called varga. The product of two equal quantities is also called varga."

Thus, the term varga for square power has its origin in the graphical representation of a square figure.

Why is the word 'root' (the root of a plant) used for the mathematical operation $\surd$ (square root, cube root, etc.)?

It is because, in ancient India, the Sanskrit word mula, meaning root of a plant, basis, cause, origin, etc., was used for the mathematical operations of taking roots.

In Sanskrit, varga-mula (the basis, cause, origin of the square) was used for square-root and ghana-mula was used for cube-root. This use of mula for the mathematical concept of root was subsequently emulated in Arabic and Latin through their corresponding words for the root of a plant — jidhr and radix respectively. The term mula for root has been used in India at least from the first century BCE. Another term used was pada (foot, basis, cause, origin). Brahmagupta (628 CE) explains, The pada (root) of a krti (square) is that of which it is a square.'

# ? Figure it Out

1. Find the cube roots of 27000 and 10648.

2. What number will you multiply by 1323 to make it a cube number?

State true or false. Explain your reasoning.

(i) The cube of any odd number is even.   
(ii) There is no perfect cube that ends with 8.   
(iii) The cube of a 2-digit number may be a 3-digit number.   
(iv)The cube of a 2-digit number may have seven or more digits.   
(v) Cube numbers have an odd number of factors.

4. You are told that 1331 is a perfect cube. Can you guess without factorisation what its cube root is? Similarly, guess the cube roots of 4913, 12167, and 32768.

5Which of the following is the greatest? Explain your reasoning.

(i) $6 7 ^ { 3 } - 6 6 ^ { 3 }$ (ii) 433 - 423 (ii) 672 -662 (iv) 43² -422

# SUMMARY

A number obtained by multiplying a number by itself is called a square number. Squares of natural numbers are called perfect squares.   
All perfect squares end with 0, 1, 4, 5, 6 or 9. Squares can only have an even number of zeros at the end.   
Square root is the inverse operation of square. Every perfect square has two integral square roots. The positive square root of a number is denoted by the symbol √ . For example, ${ \sqrt { 9 } } = 3$ A number obtained by multiplying a number by itself three times is called a cube. For example 1, 8, 27, .. ,etc., are cubes. A number is a perfect square if its prime factors can be split into two identical groups.   
A number is a perfect cube if its prime factors can be split into three identical groups   
The symbol $\sqrt [ 3 ] { \phantom { + } }$ denotes cube root. For example, $\sqrt [ 3 ] { 2 7 } = 3$ .

# is PUZZLE TIME!

# Square Pairs!

Look at the following numbers:3 6 10 15 1   
They are arranged such that each pair of adjacent numbers adds up to a square.

$$
3 + 6 = 9 , 6 + 1 0 = 1 6 , 1 0 + 1 5 = 2 5 , 1 5 + 1 = 1 6 .
$$

Try arranging the numbers 1 to 17 (without repetition) in a row in a similar way — the sum of every adjacent pair of numbers should be a square.

Can you arrange them in more than one way? If not, can you explain why?

Can you do the same with numbers from 1 to 32 (again, without repetition), but this time arranging all the numbers in a circle?

NCER be rep