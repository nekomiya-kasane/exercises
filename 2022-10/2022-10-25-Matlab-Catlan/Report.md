# Project 1

## Problem 1

### primary observation

The Catalan Constant is defined as $\displaystyle G=\sum_{i=0}^{+\infty}\dfrac{(-1)^k}{(2k+1)^2}$, a 15 digits approximation of $G$ is given as 0.915965594177219. 

In fact, the definition formula converges too slow, so I found another much better one from [Catalan's constant fast convergent series - MathOverflow](https://mathoverflow.net/questions/424055/catalans-constant-fast-convergent-series):

$$\displaystyle G=\dfrac{1}{64}\sum_{n=1}^{+\infty}\dfrac{\displaystyle 256^n(580n^2-184n+15)}{\displaystyle n^3(2n-1)\binom{6n}{3n}\binom{6n}{4n}\binom{4n}{2n}}$$

take the leading several items, we can get a more accurate value of $G$

```
res = sym(0);
for i = 1: 9
k = sym(i);
res = res + sym(256)^k*(580*k^2-184*k+15)/(k^3*(2*k-1)*nchoosek(6*i,3*i)*nchoosek(6*i,4*i)*nchoosek(4*i,2*i)*64);
end
vpa(res, 20)
```

which gives that $G>0.91596559417721901505$

hence we know $G=0.915965594177219\sim0.915965594177220=g_1\sim g_2=I$

### problem 

Next, as described in the assignment, we are going to find a rational number $p/q$ such that $p+q\leq N$, where $N$ is given, $|p/q-G|$ is minimized and $p,q$ are positive integers.

### approaches

Note that for any denominator $q$, the best numerator lies within $[\lfloor g_1 q\rfloor, \lceil g_2 q\rceil]$

Generally, this interval won't contain more than 2 integers for any denominator $< 10^{15}$ since the length of $I$ is much narrower than such $1/q$, this ensures that our implementation be $O(n)$.

Here are the detailed steps:

- loop denominator from 1 to N
- calculate the lower and upper bound of possible numerators
- if the fraction is better (closer to $G$ and conforms with $p + q \leqslant N$), update current $p,q$
- return $p,q$

```
function [p, q] = AppCat(N)
    catconst = 0.915965594177219;
    catconst_ceil = 0.915965594177220;

    p = 1;
    q = 1;
    for i = 1 : N
        low = floor(catconst * i); 		% lower bound of denominator g1 q
        high = ceil(catconst_ceil * i); % higher bound of denominator g2 q
        if i + low > N
            break;
        end
        for j = low : high
            if abs(p / q - catconst) > abs(j / i - catconst) && i + j <= N
            	% determine whether new p / q is better than the current one, and the 
                % constraints are satisfied.
                p = j;
                q = i;
            end
        end
    end
end
```

**<u>Result:</u>**

$\texttt{Appcat(2022)}=[109,119]\Rightarrow 109/119\approx G$

**<u>Command Line Output:</u>**

![image-20221025233838157](../Schelling.assets/image-20221025233838157.png)

**<u>Additional Work:</u>**

I also drew a graph showing how $p$ and $q$ changes as $N$ increases. From the graph, we can rough guess that $p$ and $q$ are increasing linearly as $N$ increases.

Here are the codes for drawing the graph above:

```
[p, q] = Appcat(2022);
disp(p + "/" + q);
disp(p / q);

n = 8;
ps = zeros(1, n);
qs = zeros(1, n);
for i = 1 : n
    [p, q] = Appcat(10 ^ i);
    ps(i) = p;
    qs(i) = q;
end
figure;
semilogy(1 : n, ps);
hold on
semilogy(1 : n, qs);
legend("p", "q", "Location", "best");
xlabel("log N")
ylabel("p or q")
hold off
```



## Problem 2

### problem

Given $N\in\mathbb{N}$, we are going to find an integer s.t. $n\geqslant N$ and has 2 ways to be decomposed into two different pairs of cubes $N=a^3+b^3=c^3+d^3$, $a,b,c,d\in\mathbb{N^+}$. 

### approaches

WLOG, we can assume that $a< b$ and $c\leqslant d$, then we only to search $a,c$ from $1$ to $\left(\frac{N}{2}\right)^{\frac{1}{3}}$, and verify if $N-a^3$ is a cube.

By the demand of output, we also need a matrix to store valid cube pairs that have been already found.

Here are the detailed steps:

- initialize two flags indicating whether the first/second pair of cubes are already found for certain integer $n$
- loop from $1$ to $(N/2)^{1/3}$ as $a_p$, search for $b_p$ such that $b_p\geq a_p, a_p^3+b_p^3 = N$.
- if $a_p,b_p$ found and the first flag is `true`, update $a,b$, otherwise update $c,d$ to $a_p,b_p$.
- if $c,d$ are updated, terminate the loop since we have found the minimal $N$ 

```
function [a, b, c, d, M] = CubicTaxicabNum(N)
    a = 0;
    b = 0;
    k = N;
    while true
        found = [false, false];
        for i = 1 : floor((k / 2) ^ (1 / 3))
            ap = i ^ 3;
            bp = round((k - ap) ^ (1 / 3));
            if bp == 0 % to handle
                continue;
            end
            if ap + bp ^ 3 == k % verify if bp ^ 3 = N - a ^ 3 is a cube. 
            % verify if ap, bp is a valid pair of cubes
                if found(1) % the second pair
                    c = i;
                    d = bp;
                    found(2) = true;
                    break;
                end
                a = i; % update the first pair
                b = bp;
                found(1) = true;
            end
        end
        if sum(found) == 2
            M = k;
            return;
        end
        k = k + 1;
    end
end
```

**<u>Result:</u>**

$\texttt{CubicTaxicabNum(36031)}=[2,34,15,33,39312]$

i.e. $2^3+34^3=15^3+33^3=39312$

**<u>Command Line Output:</u>**

![image-20221025234725051](../Schelling.assets/image-20221025234725051.png)

## Problem 3

This problem is classified as Taxicab Number Problems, the solution is usually denoted as $T(n,m,w)$, where

- $n$ is the power of components
- $m$ is the number of items
- $w$ is the count of different ways to decompose

$T(n,m,w)$ is the minimum positive integer that have at least $w$ ways to be decomposed in to the sum of $m$ positive integer items to the power of $n$. i.e. $\displaystyle T(n,m,w)=\min\{N\in\mathbb{N}\ |\ \#\{(a_1,a_2,\cdots,a_m),a_1\leqslant a_2\leqslant \cdots\leqslant a_m\in\mathbb{N},\sum a_k^n=N\}\geqslant w\}$ 

for $m=2,n=3,T_{3,2}(w)$ is categorized at [A011541 - OEIS](http://oeis.org/A011541). We can find out that $T_{3,2}(3)=87539319$. It can be found with the following script, which is a modification of the code in Problem 2.

    function [map, M] = CubicTaxicabNum2(n)
        k = 1;
        map = zeros(n, 2); % n rows matrix to record found cube pairs 
        				   % echo row for a valid pair of cubes.
        while true
            found = zeros(1, n);
            nx = 1;
            for i = 1 : floor((k / 2) ^ (1 / 3)) % WLOG, assume a <= b in a^3 + b^3 = N, hence a <= (N/2)^(1/3)
                ap = i ^ 3;
                bp = round((k - ap) ^ (1 / 3));
                if bp == 0
                    continue;
                end
                if ap + bp ^ 3 == k
                    map(nx, 1) = i; 	
                    map(nx, 2) = bp;
    
                    found(nx) = true; 	% the nx-th pair of cubes is found and update the nx-th row of map
                    nx = nx + 1;
                    if nx > n
                        break;
                    end
                end
            end
            if sum(found) == n
                M = k;
                return;
            end
            k = k + 1;
        end
    end
I must mention that this piece of code really takes a long time, since we are not supposed to know the solution in advance, so we have to search from $1$.

**<u>Result:</u>**

$\texttt{CubicTaxicabNum2(3)}=[[167,436];[228,423];[255,414],87539319]$

i.e. $T_3=87539319=167^3+436^3=228^3+423^3=255^3+414^3$

**<u>Command Line Output:</u>**

![image-20221025235525985](../Schelling.assets/image-20221025235525985.png)