## Exercise 1

The following functions are all positive and increasing.

$$
\begin{aligned}
&\lim_{n\to +\infty}\dfrac{f_2(n)}{f_3(n)}=\lim_{n\to +\infty}\dfrac{7n-2}{100\sqrt n+2n^{1/4}-100}=\lim_{n\to +\infty}\dfrac{7\sqrt{n}-\dfrac{2}{\sqrt n}}{100+2n^{-1/4}-100n^{-1/2}}=+\infty\\
&\lim_{n\to +\infty}\dfrac{f_{7}(n)}{f_2(n)}=\lim_{n\to +\infty}\dfrac{n\log n}{7n-2}=\lim_{n\to +\infty}\dfrac{\log n}{7-2/n}=\lim_{n\to+\infty}\dfrac{\log n}{7}=+\infty\\
&\lim_{n\to +\infty}\dfrac{f_6(n)}{f_4(n)}=\lim_{n\to +\infty}\dfrac{3^n}{2^{\log^2 n}}\geqslant \lim_{n\to +\infty}\dfrac{2^n}{2^{\log^2 n}}=\lim_{n\to +\infty} 2^{n-\log^2 n}=+\infty\implies \lim_{n\to +\infty}\dfrac{f_6(n)}{f_4(n)}=+\infty\\
&\lim_{n\to +\infty}\dfrac{f_4(n)}{f_1(n)}=\lim_{n\to +\infty}\dfrac{2^{\log^2 n}}{n^{\sqrt{\log n}}}=\lim_{n\to +\infty}\dfrac{n^{\frac{\log n}{\log_2 e}}}{n^{\sqrt {\log n}}}=\lim_{n\to +\infty}n^{\frac{\log n}{\log_2 e}-\sqrt{\log n}}=+\infty\\
&\lim_{n\to +\infty}\dfrac{f_1(n)}{f_5(n)}=\lim_{n\to +\infty}\dfrac{n^{\sqrt{\log n}}}{2^{2\log n}+n^{1.1}}=\lim_{n\to +\infty}\dfrac{n^{\sqrt{\log n}}}{n^{\frac{1}{\log_4 e}}+n^{1.1}}=\lim_{n\to+\infty}n^{\sqrt{\log n}-\frac{1}{\log_4 e}}=+\infty\\
&\lim_{n\to+\infty}\dfrac{f_5(n)}{f_7(n)}=\lim_{n\to+\infty}\dfrac{n^{\frac{1}{\log_4 e}}+n^{1.1}}{n\log n}=\lim_{n\to+\infty}\dfrac{n^{0.1}}{\log n}=+\infty
\end{aligned}
$$

From the calculations above, we have
$$
f_6(n)=\Omega (f_4(n)),f_4(n)=\Omega(f_1(n)),f_1(n)=\Omega (f_5(n)),f_5(n)=\Omega(f_7(n)),f_7(n)=\Omega(f_2(n)),f_2(n)=\Omega(f_3(n))
$$
Hence the required rearrangement is 
$$
f_3(n),f_2(n),f_7(n),f_5(n),f_1(n),f_4(n),f_6(n)
$$

## Exercise 2

Since $f(n)=O(g(n))$, we know that $\displaystyle \lim_{n\to+\infty}\dfrac{f(n)}{g(n)}=C<+\infty$, $C$ may be $0$ or some other positive constant. Thus

1. The statement is false. Counterexample, suppose $f(n)=2,g(n)=1+\dfrac{1}{n}$, then
   $$
   \lim_{n\to+\infty}\dfrac{f(n)}{g(n)}=\lim_{n\to+\infty}\dfrac{2}{1+1/n}=2<+\infty
   $$
   but
   $$
   \lim_{n\to+\infty}\dfrac{\log_2f(n)}{\log_2g(n)}=\lim_{n\to+\infty}\dfrac{1}{\log_2(1+1/n)}=+\infty\implies \log_2f(n)=\Omega(\log_2(g(n)))
   $$

2. The statement is false. Counterexample, suppose $f(n)=2n,g(n)=n$, then $f(n)=O(2n)=O(n)=O(g(n))$ holds, but $2^{f(n)}=2^{2n}=4^n,2^{g(n)}=2^n$, thus
   $$
   \lim_{n\to+\infty}\dfrac{2^{f(n)}}{2^{g(n)}}=\lim_{n\to+\infty}\dfrac{4^n}{2^n}=\lim_{n\to+\infty}2^n=+\infty\implies 2^{f(n)}=\Omega (2^{g(n)})
   $$

3. The statement is true. 
   $$
   \lim_{n\to+\infty }\dfrac{f(n)^2}{g(n)^2}=\left(\lim_{n\to+\infty}\dfrac{f(n)}{g(n)}\right)^2=C^2<+\infty\implies f(n)^2=O(g(n)^2)
   $$

## Exercise 3

1. My algorithm: First, we sort the array in ascending order, then

   ```
   input: array A
   output: a pair of integers in A that sum up to T. If no such integers, return None
   
   A = sort(A)
   i = 0, j = length(A) - 1
   while i < j:
   	if A[i] + A[j] == T:
   		return (A[i], A[j])
   	elif A[i] + A[j] > T:
   		j = j - 1
   	else # A[i] + A[j] < T:
   		i = i + 1
   return None
   ```
   Time complexity: The sorting procedure costs $O(n\log n)$ time (for example, use heap sort), in the while loop, each element in $A$ is visited once, the loop body is of complexity $O(1)$, hence the time cost is $O(n)$. In summary, our algorithm costs $O(n\log n)+ O(n)=O(n\log n)$ time, which is better than the given algorithm's $O(n^2)$ time complexity.

2. Algorithm: let the algorithm in $(a)$ be implemented in `Target-Sum`

   ```
   input: array A, target sum T
   output: three integers in A that sum up to T. If no such integers, return None
   
   for i from 0 to length(A) - 1:
   	result2 = Target-Sum(A[i:]) # A[i:] represents subarray from i to the end
   	if result2 is not None:
   		return (i, result2[0], result2[1])
   ```

   In the for loop, every element is visited once, and for each element, Target-Sum is executed once, on a subarray of length $n-i$, where $n$ is the length of the original array, and $i$ is the index of current element. Hence the total complexity is 
   $$
   O(n)\sum_{i=0}^{n-1}O((n-i)\log(n-i))=O(n^2\log n)
   $$
   In fact, we can find a more efficient algorithm,

   ```
   Target-Sum-3
   
   input: array A, target sum T
   output: three integers in A that sum up to T. If no such integers, return None
   
   A = sort(A)
   i = 0, j = length(A) - 1
   while (i < j):
   	# run binary from A[i + 1] to A[j - 1] (included)
   	result = binary_search(A[i + 1 : j], T - A[i] - A[j]) 
   	if result is not None:
   		return (i, j, result)
   return None
   ```

   note that `binary_search` returns the index if the input integer is found and returns None otherwise.

   We know that binary-search takes $O(\log n)$ time on a sorted array, and in the while loop, every element is visited once, the sort method costs $O(n\log n)$ time, hence the resultant time complexity is 
   $$
   O(\log n)O(n)+O(n\log n)=O(n\log n)
   $$

## Exercise 4

Algorithm

```
Target-Sum-3

input: array A
output: a good element or None

if length(A) < 2:
	return None
for i from 0 to length(A) - 1:
	if i == 0 and A[i] > A[i + 1]: # first
		return A[i]
	elif i == length(A) - 1 and A[i] > A[i - 1]: # last
		return A[i]
	elif i > 0 and i < length(A) - 1 and A[i] > A[i - 1] and A[i] > A[i + 1]:
		return A[i]
```

Every element is visited once, and the loop body takes $O(1)$ time, hence the resultant time complexity is $O(n)$.

## Exercise 5

1. for a tree of depth 1, there is only 1 node and it is a leaf, hence the number of vertices with 2 children is 0, the number of leaves is 1, the statement holds.
2. assume the statement holds for a binary tree of depth less than $n$, 
3. then for a binary tree of depth $n+1$, consider the root node, the depths of its children is at most $n$, and 
   - if it has 2 children $A,B$, the numbers of 2-children vertices of them are $v_A, v_B$ respectively, and the numbers of leaves of them are $l_A,l_B$ respectively, then by the assumption, $v_A = l_A-1,v_B=l_B-1$, the current tree has $v_A+v_B+1$ 2-children vertices and $l_A+l_B$ leaves, $v_A+v_B+1=l_A+l_B-1$, the statement holds
   - if it has 1 child $A$, the number of 2-children vertices of this child is $v_A$, and the number of leaves of it is $l_A$, then by the assumption, $v_A=l_A-1$, the current tree has $v_A$ 2-children vertices and $l_A$ leaves, $v_A=l_A-1$, the statement holds

By the principle of induction, the statement holds for all binary tree.
