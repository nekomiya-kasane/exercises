## Question 1

Greedy algorithm, is a way to solve problems, usually optimization problems, by taking the best choice in every decision, or, at each stage.

## Question 2

1. Consider the tasks sorted by Earliest Finish First rule, which are expressed in tuple `(Start, End, Value)`:

   $(0,1,1),(2,3,2), (1,4,9)$

   by the algorithm we used for jobs with all equal time, tasks $(0,1,1),(2,3,2)$ which be chosen, with a total of values $3$, but if we choose $(1,4,9)$, we'll get total value $9$. Therefore the rule doesn't work in weighted scheduling problem.

2. We can note a fact that no matter how we schedule the tasks, the last task will finish running on the supercomputer after $\displaystyle \sum_{i=1}^n p_i$​ time, it doesn't make sense to gap time between two tasks. Therefore we can adopt the following policy: the shorter $f_i$ is, the earlier we will execute it. 

   ```python
   def EARLY_FINISHED(tasks: list[tuple[int, int, int]]):
       # Input: time tuples array tasks(1...n) = (i, p_i, f_i)
       # Output: array s(1...n) for the order to execute tasks (indices), and a total time T
       
       sort(tasks, key=lambda x: x[2], order=Decending)
       
       T = 0
       pT = 0
   	for task in tasks:
           pT = pT + task[1]
   		T = max(pT + task[2], T)
       
   ```

   obviously the shortest time is $T(f)=\displaystyle\min_{1\leqslant j\leqslant n}\sum_{i=1}^j p_{f(i)}+f_{f(j)}$, where $f(i)$ is sorted descending arrangement of $p_i$.

3. The time complexity of the algorithm is the same as the sorting algorithm plus a maximum finding procedure ($O(n)$), for example, if we choose selection sort algorithm $(O(n^2))$, then the resultant time complexity is $(O(n)+O(n^2)=O(n^2))$. It's a polynomial time algorithm.

   Correctness prove:

   Suppose the output of this algorithm is not optimal, then $\exist\ \varphi$ an arrangement such that $T(f)>T(\varphi)$.

   Without loss of generosity, we can suppose $f(i)=i$, i.e., the $f_i$ array is already sorted.

   Next, choose $k$ s.t. $\displaystyle \sum_{i=1}^k p_i+f_k=T(f)$, let $h$ be the smallest number s.t. 
   $$
   \{1,2,\cdots,k\}\subset \{\varphi(1),\varphi(2),\cdots,\varphi(h)\}
   $$
   as $h$ is the smallest, we can find that $\varphi(h)\leqslant k$, otherwise $h-1$ is another number satisfying the statement but smaller than $h$. Naturally, since $f_i$ is already sorted, we have
   $$
   \sum_{i=1}^hp_{\varphi(i)}\geqslant \sum_{i=1}^kp_i\quad \Rightarrow\quad T(\varphi)\geqslant \sum_{i=1}^hp_{\varphi(i)}+f_{\varphi(h)}\geqslant \sum_{i=1}^kp_i+f_{k}=T(f)
   $$
   This contradicts to our assumption. Therefore the output of the algorithm is optimal.

### Question 3

1. **Greedy choice:** cover as many points as possible from the left.

   **Algorithm: ** 

   1. Sort the point in non-descending order of their locations (and place them from left to right)
   2. Find the leftmost point $x$, append an interval $[x,x+h]$ and a tower at $x+\dfrac{h}{2}$, where $h$ is the length of the interval. Delete all points covered by this interval.
   3. If there's no points left, terminate the algorithm, otherwise, repeat step 2.

   In this problem, for each interval $[x,x+h]$, we should let $h=8$.

   The points are sorted and scanned once $(O(n))$, hence the total complexity depends on the sorting algorithm we choose, if we choose selection sorting algorithm, the resultant complexity will be $O(n)+O(n^2)=O(n^2)$.

2. Let $X=\{x_1,x_2,\cdots,x_n\}$ be the given set of points, each represents the location of a house, WLOG, we can suppose that $X$ is already sorted and is non-descending. Let $I=\{I_1,I_2,\cdots, I_m\}$ be the set of intervals collected from the algorithm.

   Assume that $I$ is not optimal, then there exists another set of intervals $J=\{J_1,J_2,\cdots,J_t\}$ covering $X$ s.t. $t<m$. Obviously, we can let the intervals in $J$ be pairwise non-identical, to make $t$ as smaller as possible. Moreover, we can suppose $I,J$ are both arranged in non-descending order by left endpoints.

   For convenience, let $L(A),R(A)$ be the left and right endpoints of an interval $A$. By the definition of the algorithm, $L(A)\in X$. And we have the following observation:

   1. $\forall\ 1\leqslant i\leqslant t,\ L(I_i)\geqslant L(J_i)$.

   2. $I$ minimally covers $X$

   <u>Proof of 1.</u> by induction: 

   - For $i=1$, if $L(I_1)<L(J_1)$ then $X\ni L(I_i)=x<L(J_1)$, $J$ is not a covering of $X$, hence $L(I_1)\geqslant L(J_1)$.
   - Suppose for $i\leqslant r<t$, $L(I_i)\geqslant L(J_i)$
   - Then for $i=r+1$, then $R(I_i)\geqslant R(J_i)$, if $L(J_{i})>L(I_i)$, then the point $X\ni x=L(I_i)<L(J_i)$ is not covered by $J$, hence $L(I_i)\geqslant  L(J_i)$ must holds.

   By the principle of induction, 1. always holds.

   <u>Proof of 2.</u> Obviously, $I$ covers $X$. 

   If $I$ is not optimal, consider $J$. By 1. $\forall\ 1\leqslant i\leqslant t$, $L(I_i)\geqslant L(J_i)\Rightarrow R(I_i)\geqslant R(J_i)$. 

   But, note that $m>t$, there exists $X\ni x=L(I_{t+1})>R(I_t)\geqslant R(J_i)$ not covered by $J$. Contradictory. Therefore $I$ is already optimal.

	### Question 4

1. Basic Idea: This is a time-dependent shortest path problem. Let $V=\{v_1,v_2,\cdots,v_n\}$ be the $n$ stops, represented by vertices in a undirected path graph $G$. and $T=\{1,2,\cdots,n\}$ be the time series. We can try to find an arbitrary path by DFS to determine an upper bound for $n$, and fix it.

   Generate a new time-expanded graph by taking the Cartesian product, $\hat{V}=V\times T$, from the weather forecast, we can construct the edges pairwise between vertices in $\hat{V}$.

   The we can perform a normal shortest path algorithm. 

   Note the graph is acyclic, and the Bellman's Principle still holds, we can come up with an optimized BFS-like algorithm. 

   **Algorithm (Python-like pseudo code):**

   ```python
   def TIME_DEPENDENT_SHORTEST(V, W, v0, d):
       # Input: V, index-connected_vertices map, represents stops and the stops they are connected to respectively
       #        W, time-dependent weighting function W(E, t) or W(v1, v2, t)
       #        v0, starting vertex's index
       # 		 d, destination vertex index
       
       visited = [False] * len(V) # flags to indicate if a vertex has been visited 
       visited[v0] = True
       
       times = [-1] * len(V) # shortest path from v0 to each vertex
       times[v0] = 0
       
       back_nodes = [-1] * len(V) # back node of each vertex
       
       qu = PriorityQueue(key=lambda x: times[x]) # shortest time prior
       qu.push(v0)
       
       # evaluate the least arrival time to each stop
       while len(qu):
           node = visited.pop() # next node
           time = times[node] # current time
           
           for next in node.items():
               next_time = time + W(node, next, time)
               if (not visited[next]) or (next_time < times[next]):
                   # not visited or the arrival time is updated
                   times[next] = next_time
                   back_nodes[next] = node
                   if next in qu:
                       qu.remove(next) # to keep prior
                   qu.push(next)                	
   	
       # collect the shortest path
       path = [d]
       last = d
       while back_nodes[last] != -1: # not starting vertex
           last = back_nodes[last]
           path = [last] + path
           
       return (verts, times[d]) # return path and shortest time
                   
   ```

2. Example graph:

   ![Graph](https://g.gravizo.com/svg? 
   digraph G {  rankdir = LR
       1->2[label=4] 
       2->4[label="2+t"] 
       2->3[label=10] 
   	4->3[label="max{8-t/2,1}"] 
   	3->5[label=4] 
       4->5[label="2+t"] 
       5->6[label=1]
   })

   Obviously, the shortest path should be 18. Out algorithm will proceed as (start at 1, destination 6) 

   | Step | visited           | times                  | back nodes              | queue         | current time | next_time |
   | ---- | ----------------- | ---------------------- | ----------------------- | ------------- | ------------ | --------- |
   | Init | $\{T,F,F,F,F,F\}$ | $\{0,-1,-1,-1,-1,-1\}$ | $\{-1,-1,-1,-1,-1,-1\}$ | $\{1\}$       | 0            | -         |
   | 1.1  | $\{T,T,F,F,F,F\}$ | $\{0,4,-1,-1,-1,-1\}$  | $\{-1,1,-1,-1,-1,-1\}$  | $\{2\}$       | 0            | 4         |
   | 2.1  | $\{T,T,T,F,F,F\}$ | $\{0,4,14,-1,-1,-1\}$  | $\{-1,1,2,-1,-1,-1\}$   | $\{3\}$       | 4            | 10        |
   | 2.2  | $\{T,T,T,T,F,F\}$ | $\{0,4,14,10,-1,-1\}$  | $\{-1,1,2,2,-1,-1\}$    | $\{4,3\}$     | 4            | 6         |
   | 3.1  | $\{T,T,T,T,F,F\}$ | $\{0,4,13,10,-1,-1\}$  | $\{-1,1,4,2,-1,-1\}$    | $\{3\}$       | 10           | 3         |
   | 3.2  | $\{T,T,T,T,T,F\}$ | $\{0,4,13,10,22,-1 \}$ | $\{-1,1,4,2,4,-1\}$     | $\{3,5\}$     | 10           | 12        |
   | 4.1  | $\{T,T,T,T,T,F\}$ | $\{0,4,13,10,17,-1\}$  | $\{-1,1,4,2,3,-1\}$     | $\{5\}$       | 13           | 4         |
   | 5.1  | $\{T,T,T,T,T,T\}$ | $\{0,4,13,10,17,18\}$  | $\{-1,1,4,2,3,5\}$      | $\{6\}$       | 17           | 1         |
   | 6.1  | $\{T,T,T,T,T,T\}$ | $\{0,4,13,10,17,18\}$  | $\{-1,1,4,2,3,5\}$      | $\{\}$ -> end | 18           | -         |

   Find path

   | Step | Init  | 1       | 2         | 3           | 4             | 5               |
   | ---- | ----- | ------- | --------- | ----------- | ------------- | --------------- |
   | path | $[6]$ | $[5,6]$ | $[3,5,6]$ | $[4,3,5,6]$ | $[2,4,3,5,6]$ | $[1,2,4,3,5,6]$ |
   | last | $5$   | $3$     | $4$       | $2$         | $1$           | $-1$ -> end     |

   Therefore the shortest path is $[1,2,4,3,5,6]$, length $18$.