## Question 1

We're going to prove the optimality using staying ahead method. Let $f(i)$ the number of ships to ship the first $i$ boxes. The algorithm can be restated as 

1. Let $W$ be the ordered tuple $(w_1,w_2,\cdots,w_n)$ and $S=\varnothing$ be the set of partition of $W$, each element for a set of packages to carry. $T$ be the maximum capability.
2. Take as many packages as possible from $W$ that will not exceed $T$ and add this subset to $S$ from the leftmost element of $W$ and remove them from $W$
3. If $W$ is empty, terminate the algorithm. Otherwise, go to step 2.

Since the size of $W$ is decreasing for each turn if $\forall\ w_i, w_i\leqslant T$, hence the algorithm will finally be terminated and we will collect a disjoint set of partitions of $W$, i.e. $S$.

Suppose $S$ is not optimal, denote the optimal solution as $O$. We are going to prove $f_S(n)\leqslant f_O(n)$ by introduction.

- for $m=1$, the first package must be loaded, hence $f_S(1)=f_O(1)$.

- suppose for $m<k$, $f_S(m)\leqslant f_O(m)$

- then for $m=k$:

  if $f_S(k)>f_O(k)\ \ (*)$, since $f_S(k-1)\leqslant f_O(k-1)$ by the assumption, $(*)$ will indicate that $w_k$ cannot be loaded to the $f_S(k-1)$-th ship in our algorithm due to overweight, but can be loaded into the $f_O(k-1)$-th ship in the optimal solution. And there must be $f_S(k-1)=f_O(k-1)$.

  Since the packages are loaded in order, this indicates that $\exists w_h,h<k$, $w_h$ is loaded onto the  $f_S(k-1)$-th ship in our solution but loaded onto the  $(f_O(k-1)-1)$-th ship in the optimal solution.

  hence we can deduce that $f_S(h)>f_O(h)$, which contradicts to our assumption.

Therefore we proved that $f_S(i)\leqslant f_O(i)$ holds for all $1\leqslant i\leqslant n$. Since $O$ is optimal, we have $f_S(n)=f_O(n)$.

To minimize $f(n)$, the conclusion above apparently shows the optimality of our algorithm and solution $S$.

## Question 2

Let $T$, $S$ be 2 different minimum spanning trees of $G=(V,E)$, then there must be a vertex $v\in V$, such that the edges which take $v$ as an end point are different in $T$ and $S$, let it be $E\ni e=(v,v')$, $e\in T$ but $e\notin S$.

By the definition of spanning tree, $v'\in V(T\cap S)$, then $S\cup \{e\}$ must contain a cycle $C$. By the assumption, $e\notin S$, hence $\exist\ e'\neq e, e'\in C$, s.t. $e'\notin T$, otherwise $T$ will contain a cycle (contradictory to the definition of trees).

Consider such $e,e'\in C\subset E(G)$. By the given conditions, the weights $w(e)\neq w(e')$. WLOG, let $w(e)>w(e')$. Note that if we substitute $e$ with $e'$ in $T$, we will get another spanning tree with $w(e)-w(e')>0$ less weight than $T$. This contradicts to the definition of minimal spanning tree.

Therefore, the minimal spanning tree must be unique for such graph $G$.

## Question 3

1. We have known the MST (Minimum spanning tree) of $T$ of $G$. Then $T$ is a connected subgraph with the minimal sum of weighted edges of $G$. 

   **Ideas:**

   <u>Claim:</u> If we added the new edge $e=(v,w)$, the subgraph $T\cup\{e\}$ will contain exactly one cycle $C,e\in C$.

   Prove: By the definition of spanning tree, there will be a path connecting $v,w$, say $p=\{(v,e_1),(e_1,e_2),\cdots,(e_n,w)\}$, then $p\cup \{e\}$ will be a cycle.

   Suppose there appears more than 1 cycles, then for each cycle, it corresponds to a path connecting $v,w$, say $p_1,p_2$ is the paths of the first 2 such cycles. $p_1=\{(v,e_{11}),\cdots,(e_{1n},w)\}$, $p_2=\{(w,e_{21}),\cdots,(e_{2m},v)\}$. Then obviously, $p_1\cup p_2\subset T$ is a cycle. This contradicts to that $T$ is a spanning tree.

   Thus we proved there is and only is one cycle in $T\cup\{e\}$. □

   Note that

   - By the definition of MST, not edge in $G-T$ could make the weight of $T$ smaller
   - If we delete any edge $\notin C$ from $T$, then $T$ will be disconnected
   - Hence if the minimal spanning tree changes after we add the edge, then there must be an edge in $C$ that is swapped with $e$, which doesn't break the connectivity of $T$.

   **Algorithm:**

   So here comes our algorithm:

   1. Perform a common ancestor search on $T$ from $v,w$ respectively and maintain a stack recording all the vertices and edges we went through. 
   2. If we encountered the same ancestor $a$, terminate the search algorithm and check through all the weights of the edges in the 2 stacks below $a$.
   3. Find the minimum weight of the weights collected above, say such edge is $e_m$ with weight $k$. Then
      - If $k<w(e)$ (weight of the newly added edge), then $T$ is changed. To get the new MST, we'd swap $e$ and $e_m$.
      - If $k\geqslant w(e)$, then $T$ is not changed.

   **Data structure:**

   To find all the vertices connected to a give vertex when performing common ancestors, $T$ should be represented by vertices and its preceding vertex (dictionary). 

   To perform the search, we should maintain a stack to record all passed vertices and when a leaf vertex is reached, pop the top element and go back to the last vertex. Moreover, we should maintain a `visited` flag list to record if we have passed a specific vertex. This ensures that the algorithm will finally terminate and the search is the most efficient.

   **Runtime (find common ancestor):**

   We can see that the runtime will be the time complexity of the common ancestor search on $G$.

   Consider the worst case. By the algorithm, each vertex is visited at most once ($a$ is visited twice). The `visited` list is maintained in linear time in total (if stored as a list). Time complexity to find common ancestor of $v,w$ is $O(|V(T)|)=O(|E|)$

   **Runtime (test)**

   After finding common, we have 2 stacks whose top items are all $a$, then we transverse all the edges from $a$ to $v,w$, in 2 paths formed by the items in the 2 stacks, and compare each edge's weight with $w(e)$. This costs linear time and will not exceeds time to find common ancestor of $v,w$. (just pop instead push).

   Hence the time complexity is $O(|V(T)|)=O(|E|)$.

   **Runtime (update)**

   If we found the tree should be updated, WLOG, think the situation that the swapped edge $e'$ is on the path from $w$ to $a$, Then we need to delete $e'$, append $e$ to $T$ and run BFS from $w$ to vertices below (if $e'$ is below $w$ in $T$, otherwise go above). Thus each vertex will be visited at most once. Time complexity also $O(|V(T)|)$.

   <u>In summary, to test if $T$ is changed, the runtime is $O(|E|)$, and to update the tree, the runtime is also $O(|E| )$.</u>

   <u>We have answered</u> <u>(a), (b).</u>

   ## Question 4

   2. Consider the following machine with 5 virtual pages, 3 physical pages, and a reference string: 0,1,2,3,0,1,4,0,1,2,3,4

      Then the FIFO (First in First out) strategy gives the following movement with 9 faults

      |      | 0     | 1     | 2     | 3     | 0     | 1     | 4     | 0    | 1    | 2     | 3     | 4    |
      | ---- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ---- | ---- | ----- | ----- | ---- |
      | A    | **0** | 0     | 0     | **3** | 3     | 3     | **4** | 4    | 4    | 4     | 4     | 4    |
      | B    | -     | **1** | 1     | 1     | **0** | 0     | 0     | 0    | 0    | **2** | 2     | 2    |
      | C    | -     | -     | **2** | 2     | 2     | **1** | 1     | 1    | 1    | 1     | **3** | 3    |

      But LRU strategy gives 10 faults:

      |      | 0     | 1     | 2     | 3     | 0     | 1     | 4     | 0    | 1    | 2     | 3     | 4     |
      | ---- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ---- | ---- | ----- | ----- | ----- |
      | A    | **0** | 0     | 0     | **3** | 3     | 3     | **4** | 4    | 4    | **2** | 2     | 2     |
      | B    | -     | **1** | 1     | 1     | **0** | 0     | 0     | 0    | 0    | 0     | **3** | 3     |
      | C    | -     | -     | **2** | 2     | 2     | **1** | 1     | 1    | 1    | 1     | 1     | **4** |

      Hence there exists better strategy. LRU is not optimal.

   1. For the same example, FWF will give 16 page faults:

      |      | 0     | 1     | 2     | 3     | 0     | 1     | 4     | 0     | 1     | 2     | 3     | 4     |
      | ---- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
      | A    | **0** | 0     | 0     | **3** | 3     | 3     | **4** | 4     | 4     | **2** | 2     | 2     |
      | B    | -     | **1** | 1     | -     | **0** | 0     | -     | **0** | 0     | -     | **3** | 3     |
      | C    | -     | -     | **2** | -     | -     | **1** | -     | -     | **1** | -     | -     | **4** |

      Hence FWF is also not optimal.