## Problem 1

#### Description

Given positive integer $N$ e are asked to find a rational number, $p/q,p,q\in\mathbb{N}$ such that $p+q\leqslant N$ and is the one most closer to the so-called Catalan Constant  $\displaystyle G=\sum_{i=0}^{+\infty}\dfrac{(-1)^k}{(2k+1)^2}$.

From the definition of Catalan Constant $\displaystyle G=\sum_{i=0}^{+\infty}\dfrac{(-1)^k}{(2k+1)^2}$, we can construct two arrays approaching $G$:

$$\displaystyle L_k=\sum_{i=0}^k \left[\dfrac{1}{(4i+1)^2}-\dfrac{1}{(4i+3)^2}\right]=\sum_{i=0}^k \left[\dfrac{16i+8}{(4i+1)^2(4i+3)^2}\right]=\sum_{i=0}^kl_i$$

$$\displaystyle U_k=1-\sum_{i=1}^k \left[\dfrac{1}{(4i-1)^2}-\dfrac{1}{(4i+1)^2}\right]=1-\sum_{i=0}^k \left[\dfrac{16i}{(4i-1)^2(4i+1)^2}\right]=1-\sum_{i=0}^ku_i$$

note that $\forall k\in\mathbb{N^+}$, $l_k>0,u_k>0$, hence $L_k$ is a strictly monotonously increasing array and $U_k$ is a strictly monotonously decreasing array, as $k\rightarrow +\infty$. Hence the sum must converges to a positive real number.

In the assignment, an approximation of $G$ is given as 0.915965594177219.

#### Method

Naturally, we may at first think about going through all possible integer pairs $(p,q)$, and remain the best one. But there are 

$\sum_{i=1}^n(N-i)=O(N^2)$ possible pairs to enumerate. This is not a satisfactory algorithm.

However, note that from the given approximation, we can deduce a lower bound and an upper bound of $G$, denoted as $u,l$ respectively. i.e.

$G\in[0.915965594177218,0.915965594177220]=[l,u]$

and if our rational number $p/q$ is better enough, there must be that $ql\leqslant p$and $qu\geqslant p$. This ensures such $p$ is the best choice among all $k/q,k\in\mathbb{N}^{\geqslant 1,\leqslant q}$. Thus, we can iterate all possible $q\leqslant N$, and choose this best $p$ in every turn, and among these $p$‘s, choose the best again, the the problem is solved. 

Note that $qu,ql$ is close to each other, so our algorithm is simplified to a large extent. And since the give approximation of $G$ has 15 significant digits, it is enough for all input $N$ less than $10^{15}$, which is large enough.

#### Codes and results

the following codes show what we have done.

```
function [p, q] = Appcat(N)
    catconst = 0.915965594177219;
    
   lowerbound = 0.915965594177218;
   upperbound = 0.915965594177220;

    p = 1;
    q = 1;
    for i = 1 : N
        low = floor(lowerbound * i); % lower bound of the numerator ql
        high = ceil(upperbound * i); % upper bound of the numerator qu
        for j = low : high
            if abs(p / q - catconst) > abs(j / i - catconst) && i + j <= N 
            	% verify if this pair of q, p is better, if better, update p, q
                p = j;
                q = i;
            end
        end
    end
end
```

for $N=2022$, the results are output as below:

![image-20221026002316287](Report.assets/image-20221026002316287.png)

which is saying that the best valid rational number for $N=2022$ is $\dfrac{109}{119}$, the relative error is about $(109/119 - 0.915965594177219) / 0.915965594177219\approx 8.65\times 10^{-7}$

this is good enough although  the denominator is small.

## Problem 2

#### Problem

This is taxicab number problem. Given a positive integer $N$, we’re going to find a minimum integer $M$ that exceeds $N$ and can be written as the sum of two cubes in at least 2 ways. That is, exist two pairs of positive integer $(a,b)$, $(c,d)$, such that $a\neq c,a\neq d$, and $a^3+b^3=c^3+d^3=M$.

#### Method

Without loss of generality, we can let $a\leqslant b$ and $c\leqslant d$, since $(a,b),(b,a)$ are treated as the same pair.

and under this assumption, we can deduce that $a,c$ won’t exceed $\sqrt[3]{M/2}$, otherwise $a^3+b^3>M/2+M/2=M$

hence we can iterate from $a=1$ to $a=\lfloor\sqrt[3]{M/2}\rfloor$, and to see if $M-a^3$ is a cube. This will be better than iterate $b$ again within a loop.

Also, we need a $2\times 2$ matrix to store $a,b,c,d$ and update them after such $M$ is found.

#### Codes and Results

The following is the details of my implementation.

```
function [a, b, c, d, M] = CubicTaxicabNum(N)
    pairs = zeros(2, 2);
    M = N;
    while true
        ind = 1;
        for i = 1 : floor(nthroot(M / 2, 3))
            a = i ^ 3;
            b = max(1, floor(nthroot(M - a, 3)));
            if a + b ^ 3 == M % check if b is a cube, if it is not, 
            				  % floor(nthroot(M - a, 3)) won't equals M - a
                pairs(ind, 1) = i;
                pairs(ind, 2) = b;
                ind = ind + 1;
                if ind == 3
                    break;
                end
            end
        end
        if ind == 3
            break;
        end
        M = M + 1;
    end
    a = pairs(1,1);
    b = pairs(1,2);
    c = pairs(2,1);
    d = pairs(2,2);
end
```

The following messages are output to command line window:

![image-20221026004450403](Report.assets/image-20221026004450403.png)

This show that $39312$ is the smallest integer that exceeds $36031$ and can be written in the sum of two cubes in at least 2 ways.

$39312=2^2+34^2=15^2+33^2$

## Problem 3

#### Description

This problem is an extension of Problem 2, and it’s a standard Taxicab Number Problem. We can express it in a more mathematic way: Taxicab Number $T(a,b,c)$ is defined as the minimum integer that satisfies the following rules:

- $T(a,b,c)$ can be written as the sum of $b$ integers to the power of $a$ in at least $c$ ways.

where ‘distinct’ means that among all items in the sum form, at least one integer is different. for example, $(1,2)$ and $(2,1)$ are the same while $(1,2)$ and $(3,4)$ are distinct.

In fact, the Taxicab Number is really hard to compute, since the digits is increasing exponentially. $T(3,2,3)$, which we are going to compute, is not discovered until 1957 ([Taxicab Number -- from Wolfram MathWorld](https://mathworld.wolfram.com/TaxicabNumber.html)). and $T(3,2,5)$ is not discovered until 1999 ([T325](https://www.google.co.jp/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjK0NfC7fv6AhWbCrcAHZVPCLwQFnoECAwQAQ&url=https%3A%2F%2Fcs.uwaterloo.ca%2Fjournals%2FJIS%2Fwilson10.html&usg=AOvVaw0aB6PtJChbYR90YxB1qfYn)).

#### Methods

For $n=1,2$, the result is predicted to be small (less than $39312$, according to the result of Problem 2), so we can reuse the login of the code in Problem 2 - just change the start integer form $N$ to $1$. (※)

But for $n=3$, things become complicated. $T(3,2,3)$ exceeds $80000000$, if we choose to use a simple loop, then we may need a whole night to run our code. So I decided to use space to exchange time. Note that $10^8$ 32-bit integers only cost about $10^8/32/1024/1024/1024\approx 2.99$GB, my computer can certainly afford this. - And if we use bitmap (2-bit version), the memory cost will reduce to $ 186$ MB. Referring to this, my computer can even handle more than 1 billion 2-bit integers.

For every integer in the array $A$ of index $i$, we define $a_i\in A$ to be the ways integer $i$ can be expressed as $2$ positive cubes.

Then we can begin our iterations: Iterator $i,j$ from $1$ to $100\times n$, if $i\times j=k$, then increase $a_k$ by $1$, when $a_k$ reaches $3$, record $k$ and find the minimum $k$. If no such situation happens, increase $n$ can extend the size of $A$, and continue the iteration.

This algorithm is much faster than (※), but unfortunately, for $n\geq4$, due to memory problem, we have to fallback to (※) Method.

#### Codes and Results

The following is the details of my implementation.

```
function [pairs, M] = Find3(N)
    res = 1;
    if N == 3
        for n = 5 : 10
            G = zeros(1, n * n * 10 ^ 7); % is the array A in the description above
            res = n * n * 10 ^ 7;
            for i = 1 : (n * 100)
                for j = i : (n * 100)
                    G(i ^ 3 + j ^ 3) = G(i ^ 3 + j ^ 3) + 1;
                    if G(i ^ 3 + j ^ 3) == 3
                        res = min(res, i ^ 3 + j ^ 3);
                    end
                end
            end 
            if res ~= n * n * 0.1 * 10 ^ 8
                break
            end
        end
    end
    M = res;

`	% fallback method, for n = 3, we will searh only one turn for all valid pairs of cubes,
	% since M is already found above.
    pairs = zeros(N, 2);
    while true
        ind = 1;
        for i = 1 : floor(nthroot(M / 2, 3))
            a = i ^ 3;
            b = max(1, floor(nthroot(M - a, 3)));
            if a + b ^ 3 == M
                pairs(ind, 1) = i;
                pairs(ind, 2) = b;
                if ind == N
                    break;
                end
                ind = ind + 1;
            end
        end
        if ind == N
            M = res;
            break;
        end
        M = M + 1;
    end
end
```

The following messages are output to command line window:

![image-20221026012103090](Report.assets/image-20221026012103090.png)

This show that $87539319$ is the smallest integer that and can be written in the sum of two cubes in at least 3 ways.

$T_3=87539319=167^3+436^3=228^3+423^3=255^3+414^3$