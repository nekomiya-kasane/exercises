**Prob 2**

```fortran
1 Function oottasti(n):       # T(n)
2     if n < 2 then 	      # comparasion: 1
3     	return 0
4     for i ← 1 to n do       
5     	if a[i+5] = 0 then    # addition: 1, comparasion: 1
6     		return i
7     a[1] ← 0                
8     return oottasti(n-1)    # T(n-1)
```

From line 4 to line 6, each turn of the loop will take constant operations, and in the worst case, it is looped $n$ times.  hence the recursion can be depicted by
$$
T(n)=T(n-1)+2n+1=T(n-1)+O(n)
$$
**Prob 4**

```fortran
01 Function erithell(n)
02	  for i <- 1 to 2n do
03		for j <- 1 to n do
04			C elementary operations
05    j <- 1                             
06    for i <- 1 to n do 
07    	while j < n ^ 3 do             # 1 comparasion
08    		C elementary operations
09    		j <- j + 1                 # 1 addition
10      if i % 2 == 0 then             # 1 modulus, 1 comparasion
11        	j <- 1
12    i <- 1
13    j <- 1
14    while i < n do                   # 1 comparasion
15    	while j < n do                 # 1 comparasion
16    		j <- j + j                 # 1 addition
17    		C elementary operations 
18    	i <- i + 2                     # 1 addition
```

As required, we only count the operations containing $C$, i.e. from line 4, 8, 17

- the loop from line 2 to 4: since $i,j$ are independently looping, hence the inner block is executed $2n\times n=2n^2$ times, costs $2Cn^2$ operations in total.

- the loop from line 6 to 11: the outer loop containing $i$ runs $n$ times, in each run, due to the while block (name it as $w_1$.

  when $i$ is odd, $w_1$ loops for $n^3$ times, then $i$ will be even, but since $j$ already reaches $n^3$, $w_1$ will not be executed but after $w_1$, $j$ is reset to $1$.

  Hence when $i$ is odd, the inner block costs $Cn^3$ operations; otherwise, it costs $3$ operations. The total number of operations is 
  $$
  \sum_{i=1}^{\lfloor n/2\rfloor}Cn^3
  $$

- the loop from line 14 to 17: in line 16, we see that $j$ is doubled each turn and not reset, hence the while block $w_2$ from line 15 to 17 will only be run once, costing $C\lceil \log_2 n\rceil$ operations. Except the first turn, the inner block from line 15 to 18 will take $2$ operations each turn, hence the total number of operations is
  $$
  C\lceil \log_2 n\rceil
  $$

In summary, the time complexity of this function `erithell` about $C$ is
$$
\begin{array}{rl}
T(n)&\displaystyle=C\lceil \log_2 n\rceil+2Cn^2 +\sum_{i=1}^{\lfloor n/2\rfloor}Cn^3\\
&=C(O(\log_2n)+O(n^2)+O(n^4))\\
&=CO(n^4)
\end{array}
$$
