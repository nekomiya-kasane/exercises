### Question 1

#### (a)

truth table:

| $r$  | $p$  | $q$  | $\neg q$ | $p\vee \neg q$ | $\color{purple} r\Rightarrow (p\vee \neg q)$ | $q\wedge r$ | $\color{orange}(q\wedge r)\Rightarrow p$ |
| ---- | ---- | ---- | -------- | -------------- | -------------------------------------------- | ----------- | ---------------------------------------- |
| T    | T    | T    | F        | T              | T                                            | T           | T                                        |
| T    | T    | F    | T        | T              | T                                            | F           | T                                        |
| T    | F    | T    | F        | F              | F                                            | T           | F                                        |
| F    | T    | T    | F        | T              | T                                            | F           | T                                        |
| T    | F    | F    | T        | T              | T                                            | F           | T                                        |
| F    | T    | F    | T        | T              | T                                            | F           | T                                        |
| F    | F    | T    | F        | F              | T                                            | F           | T                                        |
| T    | T    | T    | F        | T              | T                                            | T           | T                                        |

By the 6th and 8th columns, which are exactly the same, we can conclude that $\color{purple} r\Rightarrow (p\vee \neg q)\color{forestgreen}\equiv \color{orange}(q\wedge r)\Rightarrow p$ 

#### (b)

truth table:

| $r$  | $p$  | $q$  | $p\Rightarrow q$ | $\color{purple}(p\Rightarrow q)\Rightarrow r$ | $q\Rightarrow r$ | $\color{orange}p\Rightarrow(q\Rightarrow r)$ |
| ---- | ---- | ---- | ---------------- | --------------------------------------------- | ---------------- | -------------------------------------------- |
| T    | T    | T    | T                | T                                             | T                | T                                            |
| T    | T    | F    | F                | T                                             | T                | T                                            |
| T    | F    | T    | T                | T                                             | T                | T                                            |
| F    | T    | T    | T                | F                                             | F                | F                                            |
| T    | F    | F    | T                | T                                             | T                | T                                            |
| F    | T    | F    | F                | T                                             | T                | T                                            |
| F    | F    | T    | T                | F                                             | F                | T                                            |
| F    | F    | F    | T                | F                                             | T                | T                                            |

By the last 2 rows, of which the 6th and 8th columns are different from each other, we can conclude that $\color{purple}(p\Rightarrow q)\Rightarrow r\color{red} \not\equiv \color{orange}p\Rightarrow(q\Rightarrow r)$

### Question 2

？

### Question 3

> If $x^2=y^2+z^2$, then $xyz$ is even. 

Contrapositive of this implication:

> If $xyz$ is NOT even (i.e. is odd), then $x^2\neq y^2+z^2$

Since the contrapositive statement is true if and only if the original statement is true, vice versa.

Hence we'll prove the original statement by proving its contrapositive statement.

If $xyz$ is odd, then $x,y,z$ must be all odd. Hence $x^2,y^2,z^2$ are odd, which leads to that $y^2+z^2$ is even but $x^2$ is odd. Therefore $x^2\neq y^2+z^2$. Proved. 

So we can conclude that if $x^2=y^2+z^2$, then $xyz$ is even. 

### Question 4

Given $x$ is rational, suppose that $x^2=x+1$. WLOG, let $x=\dfrac{p}{q}$, where $p\in \mathbb{Z}$ and $q\in \mathbb{Z}-\{0\}$ are coprime. Hence $\dfrac{p^2}{q^2}=\dfrac{p}{q}+1\Leftrightarrow p^2=q(p+q)$. 

By the fundamental theorem of arithmetic, the left hand side and right hand side have exactly the same prime decompositions with exactly the same multiplicities, hence $\exist$ prime $h\neq 1$, $h\mid q$ such that $h\mid p$, then $1<h\mid \gcd (p,q)\Rightarrow \gcd(p,q) >1$. 

This contradicts to the assumption that $p,q$ are coprime. Therefore there must be $x^2\neq x+1$. Proved. 

### Question 5

There are 3 o's, 2 t's, 2 r's in total, and one u, e, p, i, c each letter. Total length 12.

all anagrams: $\dfrac{12!}{3!2!2!}=19958400$

anagrams without consecutive o's: $\displaystyle \dfrac{(12-3)!}{2!2!}\times \binom{10}{3}=10886400$

anagrams with at least 2 consecutive o's: $19958400-10886400=9072000$