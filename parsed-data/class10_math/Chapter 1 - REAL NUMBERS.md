# 1.1 Introduction

In Class IX, you began your exploration of the world of real numbers and encountered irrational numbers. We continue our discussion on real numbers in this chapter. We begin with very important properties of positive integers in Sections 1.2, namely the Euclid's division algorithm and the Fundamental Theorem of Arithmetic.

Euclid's division algorithm, as the name suggests, has to do with divisibility of integers. Stated simply, it says any positive integer $a$ can be divided by another positive integer $^ { b }$ in such a way that it leaves a remainder $r$ that is smaller than $^ { b }$ Many of you probably recognise this as the usual long division process. Although this result is quite easy to state and understand, it has many applications related to the divisibility properties of integers. We touch upon a few of them, and use it mainly to compute the HCF of two positive integers.

The Fundamental Theorem of Arithmetic, on the other hand, has to do something with multiplication of positive integers. You already know that every composite number can be expressed as a product of primes in a unique way—this important fact is the Fundamental Theorem of Arithmetic. Again, while it is a result that is easy to state and understand, it has some very deep and significant applications in the field of mathematics. We use the Fundamental Theorem of Arithmetic for two main applications. First, we use it to prove the irrationality of many of the numbers you studied in Class IX, such as ${ \sqrt { 2 } } , { \sqrt { 3 } }$ and $\sqrt { 5 }$ Second, we apply this theorem to explore when exactly the decimal expansion of a rational number, say q ≠ , is terii nd whe t is nnterminating repeating. We do so by looking at the prime factorisation of the denominator $q$ of $\frac { p } { q }$ You will see that the prime factorisation of $q$ will completely reveal the nature of the decimal expansion of $\frac { p } { q }$ .

So let us begin our exploration.

# 1.2 The Fundamental Theorem of Arithmetic

In your earlier classes, you have seen that any natural number can be written as a product of its prime factors. For instance, $2 = 2$ . $4 = 2 \times 2$ . $2 5 3 = 1 1 \times 2 3$ ,and so on. Now, let us try and look at natural numbers from the other direction. That is, can any natural number be obtained by multiplying prime numbers? Let us see.

Take any collection of prime numbers, say 2, 3, 7, 11 and 23. If we multiply some or all of these numbers, allowing them to repeat as many times as we wish, we can produce a large collection of positive integers (In fact, infinitely many). Let us list a few :

$$
\begin{array} { l l } { { 7 \times 1 1 \times 2 3 = 1 7 7 1 } } & { { \qquad 3 \times 7 \times 1 1 \times 2 3 = 5 3 1 3 } } \\ { { 2 \times 3 \times 7 \times 1 1 \times 2 3 = 1 0 6 2 6 } } & { { \qquad 2 ^ { 3 } \times 3 \times 7 ^ { 3 } = 8 2 3 2 } } \\ { { 2 ^ { 2 } \times 3 \times 7 \times 1 1 \times 2 3 = 2 1 2 5 2 } } & { { } } \end{array}
$$

and so on.

Now, let us suppose your collection of primes includes all the possible primes. What is your guess about the size of this collection? Does it contain only a finite number of integers, or infinitely many? Infact, there are infinitely many primes. So, if we combine all these primes in all possible ways, we will get an infinite

collection of numbers, all the primes and all possible products of primes. The question is - can we produce all the composite numbers this way? What do you think? Do you think that there may be a composite number which is not the product of powers of primes? Before we answer this, let us factorise positive integers, that is, do the opposite of what we have done so far.

We are going to use the factor tree with which you are all familiar. Let us take some large number, say, 32760, and factorise it as shown.

So we have factorised 32760 as $2 \times 2 \times 2 \times 3 \times 3 \times 5 \times 7 \times 1 3$ as a product of primes, i.e., $3 2 7 6 0 = 2 ^ { 3 } \times 3 ^ { 2 } \times 5 \times 7 \times 1 3$ as a product of powers of primes. Let us try another number, say, 123456789. This can be written as $3 ^ { 2 } \times 3 8 0 3 \times 3 6 0 7 .$ Of course, you have to check that 3803 and 3607 are primes! (Try it out for several other natural numbers yourself.) This leads us to a conjecture that every composite number can be written as the product of powers of primes. In fact, this statement is true, and is called the Fundamental Theorem of Arithmetic because of its basic crucial importance to the study of integers. Let us now formally state this theorem.

Theorem 1.1 (Fundamental Theorem of Arithmetic) : Every composite number can be expressed (factorised) as a product of primes, and this factorisation is unique, apart from the order in which the prime factors occur.

An equivalent version of Theorem 1.2 was probably first recorded as Proposition 14 of Book IX in Euclid's Elements, before it came to be known as the Fundamental Theorem of Arithmetic. However, the first correct proof was given by Carl Friedrich Gauss in his Disquisitiones Arithmeticae.

Carl Friedrich Gauss is often referred to as the 'Prince of Mathematicians' and is considered one of the three greatest mathematicians of all time, along with Archimedes and Newton. He has made fundamental contributions to both mathematics and science.

  
Carl Friedrich Gauss (1777 - 1855)

The Fundamental Theorem of Arithmetic says that every composite number can be factorised as a product of primes. Actually it says more. It says that given any composite number it can be factorised as a product of prime numbers in a 'unique' way, except for the order in which the primes occur. That is, given any composite number there is one and only one way to write it as a product of primes, as long as we are not particular about the order in which the primes occur. So, for example, we regard $2 \times 3 \times 5 \times 7$ as the same as $3 \times 5 \times 7 \times 2$ ,or any other possible order in which these primes are written. This fact is also stated in the following form:

The prime factorisation of a natural number is unique, except for the order of its factors.

In general, given a composite number $x .$ we factorise it as $x = p _ { 1 } p _ { 2 } \ldots p _ { n } ;$ where $p _ { 1 }$ , $p _ { 2 } , \ldots$ $p _ { n }$ are primes and written in ascending order, i.e., $p _ { \mathrm { ~ 1 ~ } } \leq p _ { 2 }$ $\leq . . . \leq p _ { n } .$ If we combine the same primes, we will get powers of primes. For example,

$$
3 2 7 6 0 = 2 \times 2 \times 2 \times 3 \times 3 \times 5 \times 7 \times 1 3 = 2 ^ { 3 } \times 3 ^ { 2 } \times 5 \times 7 \times 1 3
$$

Once we have decided that the order will be ascending, then the way the number is factorised, is unique.

The Fundamental Theorem of Arithmetic has many applications, both within mathematics and in other fields. Let us look at some examples.

Example $\mathbf { 1 : }$ Consider the numbers $4 ^ { n }$ ,where $n$ is a natural number. Check whether there is any value of $n$ for which $4 ^ { n }$ ends with the digit zero.

Solution : If the number $4 ^ { n }$ , for any $n$ ,were to end with the digit zero, then it would be divisible by 5. That is, the prime factorisation of $4 ^ { n }$ would contain the prime 5. This is not possible because $4 ^ { n } = ( 2 ) ^ { 2 n }$ ; so the only prime in the factorisation of $4 ^ { n }$ is 2. So, the uniqueness of the Fundamental Theorem of Arithmetic guarantees that there are no other primes in the factorisation of $4 ^ { n }$ So, there is no natural number $n$ for which $4 ^ { n }$ ends with the digit zero.

You have already learnt how to find the HCF and LCM of two positive integers using the Fundamental Theorem of Arithmetic in earlier classes, without realising it! This method is also called the prime factorisation method. Let us recall this method through an example.

Example ${ \mathfrak { 2 } } :$ Find the LCM and HCF of 6 and 20 by the prime factorisation method.

Solution : We have :

You can find $\mathrm { H C F } ( 6 , 2 0 ) = 2$ and $\mathrm { L C M } ( 6 , 2 0 ) = 2 \times 2 \times 3 \times 5 = 6 0$ , as done in your earlier classes.

Note that $\mathrm { H C F } ( 6 , 2 0 ) = 2 ^ { 1 } =$ Product of the smallest power of each common prime factor in the numbers.

LCM $( 6 , 2 0 ) = 2 ^ { 2 } \times 3 ^ { 1 } \times 5 ^ { 1 } =$ Product of the greatest power of each prime factor, involved in the numbers.

From the example above, you might have noticed that $\mathrm { H C F } ( 6 , 2 0 ) \times \mathrm { L C M } ( 6 , 2 0 )$ $= 6 \times 2 0$ .In fact, we can verify that for any two positive integers $\pmb { a }$ and $\pmb { b }$ , HC $\mathbf { \mathrm { F } } \left( a , b \right) \times \mathbf { \mathrm { L C M } } \left( a , b \right) = a \times b .$ We can use this result to find the LCM of two positive integers, if we have already found the HCF of the two positive integers.

Example 3: Find the HCF of 96 and 404 by the prime factorisation method. Hence, find their LCM.

Solution : The prime factorisation of 96 and 404 gives :

$$
9 6 = 2 ^ { 5 } \times 3 , 4 0 4 = 2 ^ { 2 } \times 1 0 1
$$

Therefore, the HCF of these two integers is $2 ^ { 2 } = 4$ .

Also,

$$
\operatorname { L C M } ( 9 6 , 4 0 4 ) = { \frac { 9 6 \times 4 0 4 } { \operatorname { H C F } ( 9 6 , 4 0 4 ) } } = { \frac { 9 6 \times 4 0 4 } { 4 } } = 9 6 9 6
$$

Example $4 :$ Find the HCF and LCM of 6, 72 and 120, using the prime factorisation method.

Solution : We have :

$$
6 = 2 \times 3 , 7 2 = 2 ^ { 3 } \times 3 ^ { 2 } , 1 2 0 = 2 ^ { 3 } \times 3 \times 5
$$

Here, $2 ^ { 1 }$ and $3 ^ { 1 }$ are the smallest powers of the common factors 2 and 3, respectively.

So,

$$
\mathrm { H C F } \left( 6 , 7 2 , 1 2 0 \right) = 2 ^ { 1 } \times 3 ^ { 1 } = 2 \times 3 = 6
$$

23, $3 ^ { 2 }$ and $5 ^ { 1 }$ are the greatest powers of the prime factors 2, 3 and 5 respectively involved in the three numbers.

So,

$$
\operatorname { L C M } \left( 6 , 7 2 , 1 2 0 \right) = 2 ^ { 3 } \times 3 ^ { 2 } \times 5 ^ { 1 } = 3 6 0
$$

Remark : Notice, $6 \times 7 2 \times 1 2 0 \neq \mathrm { H C F }$ (6, 72, 120) × LCM (6, 72, 120). So, the product of three numbers is not equal to the product of their HCF and LCM.

# EXERCISE 1.1

1. Express each number as a product of its prime factors:

i 140 (i) 156U (ii) 3825 v) 5005 (v) 7429

2Find the LCM and HCF of the following pairs of integers and verify that ${ \mathrm { L C M } } \times { \mathrm { H C F } } =$ product of the two numbers.

i 26 and 91 510 and 92 336 and 54

Find the LCM and HCF of the following integers by applying the prime factorisation method.

(il) 12, 15 and 21 i17, 23 and 29 ii 8, 9 and 25

Given that HCF $( 3 0 6 , 6 5 7 ) = 9$ , find LCM (306, 657).

5. Check whether $6 ^ { n }$ can end with the digit 0 for any natural number $n$ .

6.Explain why $7 \times 1 1 \times 1 3 + 1 3$ and $7 \times 6 \times 5 \times 4 \times 3 \times 2 \times 1 + 5$ are composite numbers.

7There is a circular path around a sports field. Sonia takes 18 minutes to drive one round of the field, while Ravi takes 12 minutes for the same. Suppose they both start at the

same point and at the same time, and go in the same direction. After how many minutes will they meet again at the starting point?

# 1.3 Revisiting Irrational Numbers

In Class IX, you were introduced to irrational numbers and many of their properties. You studied about their existence and how the rationals and the irrationals together made up the real numbers. You even studied how to locate irrationals on the number line. However, we did not prove that they were irrationals. In this section, we will prove that ${ \sqrt { 2 } } , { \sqrt { 3 } } , { \sqrt { 5 } }$ and, in general, $\sqrt { p }$ is irrational, where $p$ is a prime. One of the theorems, we use in our proof, is the Fundamental Theorem of Arithmetic. :

Recall, a number $\mathit { \Pi } ^ { \circ } { } _ { S } \mathit { \Pi } ^ { \circ }$ is called irrational if it cannot be written in the form $\frac { p } { q } .$ where $p$ and $q$ are integers and $q \neq 0$ Some examples of irrational numbers, with which you are already familiar, are :

$$
{ \sqrt { 2 } } , { \sqrt { 3 } } , { \sqrt { 1 5 } } , \pi , - { \frac { \sqrt { 2 } } { \sqrt { 3 } } } , 0 . 1 0 1 1 0 1 1 1 0 1 1 1 1 0 \ldots , \operatorname { e t o r } (
$$

Before we prove that $\sqrt { 2 }$ is irrational, we need the following theorem, whose proof is based on the Fundamental Theorem of Arithmetic.

Theorem $1 . 2 : L e t p$ be a prime number. If $p$ divides $a ^ { 2 } ,$ then $p$ divides a, where a is a positive integer.

\*Proof : Let the prime factorisation of $a$ be as follows :

$a = p _ { _ 1 } p _ { _ 2 } \ldots p _ { n } ,$ where $p _ { 1 } , p _ { 2 } , . . . , p _ { n }$ are primes, not necessarily distinct.

Therefore, $a ^ { 2 } = ( p _ { 1 } p _ { 2 } \ldots p _ { n } ) ( p _ { 1 } p _ { 2 } \ldots p _ { n } ) = p _ { 1 } ^ { 2 } p _ { 2 } ^ { 2 } \ldots p _ { n } ^ { 2 } .$

Now, we are given that $p$ divides $a ^ { 2 }$ Therefore, from the Fundamental Theorem of Arithmetic, it follows that $p$ is one of the prime factors of $a ^ { 2 }$ However, using the uniqueness part of the Fundamental Theorem of Arithmetic, we realise that the only prime factors of $a ^ { 2 }$ are $p _ { 1 } , p _ { 2 } , . . . . p _ { n }$ . $\mathrm { S o } p$ is one of $p _ { 1 } , p _ { 2 } , . . . , p _ { n } .$ .

Now, since $a = p _ { 1 } p _ { 2 } \ldots p _ { n } , p$ divides $a$

We are now ready to give a proof that $\sqrt { 2 }$ is irrational.

The proof is based on a technique called 'proof by contradiction'. (This technique is discussed in some detail in Appendix 1).

Theorem $1 . 3 : { \sqrt { 2 } }$ is irrational.

Proof : Let us assume, to the contrary, that $\sqrt { 2 }$ is rational.

So, we can find integers $r$ and $s \left( \neq 0 \right)$ such that ${ \sqrt { 2 } } \ = { \frac { r } { s } }$

Suppose $r$ and $s$ have a common factor other than 1. Then, we divide by the common factor to get ${ \sqrt { 2 } } = { \frac { a } { b } }$ where $a$ and $^ { b }$ are coprime.   
So, $b { \sqrt { 2 } } = a$ .

Squaring on both sides and rearranging, we get $2 b ^ { 2 } = a ^ { 2 }$ Therefore, 2 divides $a ^ { 2 }$ .

Now, by Theorem 1.2, it follows that 2 divides $a$ .

So, we can write $a = 2 c$ for some integer $c$ .

Substituting for $a$ ,we get $2 b ^ { 2 } = 4 c ^ { 2 }$ , that is, $b ^ { 2 } = 2 c ^ { 2 }$ .

This means that 2 divides $b ^ { 2 }$ , and so 2 divides $^ { b }$ (again using Theorem 1.2 with $p = 2$ ).

Therefore, $a$ and $^ { b }$ have at least 2 as a common factor.

But this contradicts the fact that $a$ and $^ { b }$ have no common factors other than 1.

This contradiction has arisen because of our incorrect assumption that $\sqrt { 2 }$ is rational.

So, we conclude that $\sqrt { 2 }$ is irrational.

Example $5 :$ Prove that $\sqrt { 3 }$ is irrational.

Solution : Let us assume, to the contrary, that $\sqrt { 3 }$ is rational.

That is, we can find inters $a$ and $b \left( \neq 0 \right)$ such that ${ \sqrt { 3 } } = { \frac { a } { b } } \cdotp$

Suppose $a$ and $^ { b }$ have a common factor other than 1, then we can divide by the common factor, and assume that $a$ and $^ { b }$ are coprime.

Squaring on both sides, and rearranging, we get $3 b ^ { 2 } = a ^ { 2 }$

Therefore, $a ^ { 2 }$ is divisible by 3, and by Theorem 1.2, it follows that $a$ is also divisible by 3.

So, we can write $a = 3 c$ for some integer $c$ .

Substituting for $a$ ,we get $3 b ^ { 2 } = 9 c ^ { 2 }$ , that is, $b ^ { 2 } = 3 c ^ { 2 }$ .

This means that $b ^ { 2 }$ is divisible by 3, and so $^ { b }$ is also divisible by 3 (using Theorem 1.2 with $p = 3$ ).

Therefore, $a$ and $^ { b }$ have at least 3 as a common factor.

But this contradicts the fact that $a$ and $^ { b }$ are coprime.

This contradiction has arisen because of our incorrect assumption that $\sqrt { 3 }$ is rational.   
So, we conclude that $\sqrt { 3 }$ is irrational.

In Class IX, we mentioned that :

the sum or difference of a rational and an irrational number is irrational and the product and quotient of a non-zero rational and irrational number is irrational.

We prove some particular cases here.

Example 6 : Show that $5 - { \sqrt { 3 } }$ is irrational.

Solun: Le us assue,  he contrary $5 - { \sqrt { 3 } }$ is rational.

That is, we can find coprime $a$ and $^ { b }$ $( b \neq 0 )$ such that $5 - { \sqrt { 3 } } = { \frac { a } { b } }$

Therefore, $5 - { \frac { a } { b } } = { \sqrt { 3 } }$

Rearranging this equation, we get ${ \sqrt { 3 } } = 5 - { \frac { a } { b } } = { \frac { 5 b - a } { b } } \cdotp$

Since $a$ and $^ { b }$ are integers, we get $\displaystyle { \mathfrak { s } } - { \frac { a } { b } }$ is rational, and so $\sqrt { 3 }$ is rational.

But this contradicts the fact that $\sqrt { 3 }$ is irrational.

This contradiction has arisen because of our incorrect assumption that $5 - { \sqrt { 3 } }$ is rational.

So, we conclude that $5 - { \sqrt { 3 } }$ is irrational.

Example 7 : Show that $3 \sqrt { 2 }$ is irrational.

Solution Let us assume, to the contrary, that $3 \sqrt { 2 }$ is rational.

That is, we can find coprime $a$ and $^ { b }$ $( b \neq 0 )$ such that $3 { \sqrt { 2 } } = { \frac { a } { b } }$

Rearranging, we get √2 = a.

Since 3, $a$ and $^ { b }$ are integers, $\frac { a } { 3 b }$ is rational, and so $\sqrt { 2 }$ is rational.

But this contradicts the fact that $\sqrt { 2 }$ is irrational.   
So, we conclude that $\overline { { 3 \sqrt { 2 } } }$ is irrational.

# EXERCISE 1.2

Prove that $\sqrt { 5 }$ is irrational.

Prove that $3 + 2 { \sqrt { 5 } }$ is irrational.

3.Prove that the following are irrationals :

(i) $\frac { 1 } { \sqrt { 2 } }$ () \$ sqrt5}\$ (i) 6 +√sqr2 2\$

# 1.4 Summary

In this chapter, you have studied the following points:

1. The Fundamental Theorem ofArithmetic :

Every composite number can be expressed (factorised) as a product of primes, and this factorisation is unique, apart from the order in which the prime factors occur.

2. If $p$ is a prime and $p$ divides $a ^ { 2 }$ ,then $p$ divides $a$ where $a$ is a positive integer.

To prove that ${ \sqrt { 2 } } , { \sqrt { 3 } }$ are irrationals.

# A Note to the Reader

You have seen that :

HCF $\left( p , q , r \right) \times \mathrm { L C M } \left( p , q , r \right) \neq p \times q \times r$ where $p , q$ $r$ are positive integers (see Example 8). However, the following results hold good for three numbers $p , q$ and $r$ :

$$
\begin{array} { r } { \mathrm { L C M } \left( p , q , r \right) = \frac { p \cdot q \cdot r \cdot \mathrm { H C F } \left( p , q , r \right) } { \mathrm { H C F } \left( p , q \right) \cdot \mathrm { H C F } \left( q , r \right) \cdot \mathrm { H C F } \left( p , r \right) } } \\ { \mathrm { H C F } \left( p , q , r \right) = \frac { p \cdot q \cdot r \cdot \mathrm { L C M } \left( p , q , r \right) } { \mathrm { L C M } \left( p , q \right) \cdot \mathrm { L C M } \left( q , r \right) \cdot \mathrm { L C M } \left( p , r \right) } } \end{array}
$$