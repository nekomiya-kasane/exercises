## Problem 1

1. A set of constructive objects of some fixed type which admits an algorithm to determine membership in a set of formulas. A set $M$ is said to be decidable if there exists a general recursive function $f$ (algorithm) such that $M=\{x\mid f(x)=1\}$ and $\forall x\not\in M, f(x)=0$.

   For example, $\{n\in\N\mid n\equiv 1\mod 2\}$ among $\N$ is a decidable set.

2. Since $G$ is strictly increasing and computable, $\forall\ i\geqslant 1,G(i+1)>G(i)$ computable, as it maps positive integers to positive integers, $G(1)\geqslant  1$ computable, therefore $\forall i\geqslant 1$, we have $G(i+1)\geqslant G(i)+1$, followed by
   $$
   G(i)\geqslant  G(i-1)+1\geqslant G(i-2)+2\geqslant \cdots\geqslant G(1)+i-1\geqslant i
   $$

3. Since $G$ is computable, we’ll prove that the set $S=\{G(x)\mid x\in \N\}$ decidable by explicitly give an algorithm that decides whether some item $y$ belongs to $S$ or not. WLOG, we consider $S$ within $\N$. Given $x$, 

   1. Set $i=1$.
   2. If $G(i)=x$, terminate the process and return $1$. If $G(i)>x$, terminate the process and return $0$. 
   3. Otherwise, $i\leftarrow i+1$ and go to the second step.

   We claim the procedure must terminate. Since $G(x)$ is strictly increasing, hence $\forall\ s,t\in\N, s<t$, we have $G(s) <G(t)$, thus $\forall\ s>x$, we have $G(s)\geqslant s>x$. Thus step 3 can be executed at most $s-1<\infty$ times. By the description of step 2, the procedure executed by some Turing machine must terminate and returns either $0$ or $1$ for reject and accept respectively. 

   Therefore $S$ is decidable.

## Problem 2

For clarification, let $L(M)$ be the strings (language) accepted by the Turing Machine $M$, while $L$ itself denotes the set proposed by the problem.

1. A ==Turing-recognizable== language is a language for which there exists a Turing machine that can accept or recognize all the strings that belong to the language. In other words, there is a Turing machine that, when provided with a string belonging to the language as input, will eventually halt and accept the input, but for strings that do not belong to the language, it may either halt and reject, or loop indefinitely without halting.

   An ==undecidable language== is a language for which no Turing machine can be constructed that will accept or recognize all the strings in the language. In other words, there’s no algorithm executed by a Turing Machine that can determine, for any given input string, whether it belongs to the language or not.

2. $L$ is **recognizable**. For a specified Turing machine $M\in L$ that can accept at least $2$ binary strings, say the two shortest such strings are $w_1,w_2$, and $|w_1|\leqslant  |w_2|=m$, then if we iterate all binary strings from $\varepsilon$ to strings of length $m+1$ lexicographically and with non-decreasing lengths, for example $\Sigma=\{0,1\}$, $\varepsilon,0,1,00,01,10,11,\cdots$. then we must have met $w_1$ and $w_2$ before the $2^{m+1}$-th iteration (at this iteration, all strings shorter than $m+1$ including $w_1,w_2$ have been already transverse), and we have already recognized $M$ and terminated the procedure before the $2^{m+1}$-th iteration. 

   Therefore for any $M$, we can determine if $M\in L$ within finite steps if $M\in L$ really holds. $L$ is recognizable. 

3. To prove 2. formally, we’d propose explicitly an algorithm (recognizer $S$) that can determine a $M\in L$ within finite steps. $S=\ \downarrow$

   - Let $c\leftarrow 0$
   - For $k=0,1,2,\cdots$ (not bounded)
     - For every distinct binary string $w$ of length $k$ (bounded, executed at most $2^k$ times)
       - Run $M$ on $w$ for at most $k$ steps, if $M$ halts, $c\Leftarrow c+1\ (*)$ 
       - If $c=2$, terminate the procedure.

   If this algorithm terminates on a machine $M$, then it has run $M$ on 2 strings on which $M$ terminates.

   Conversely, if $M\in L$, there exist $2$ strings contained in $L(M)$, say $w_1,w_2$. Till $k=\max\{|w_1|,|w_2|\}+1$, i.e. till the $2^{(\max\{|w_1|,|w_2|\}+1+1)}$-th execution of $(*)$, we must have run $M$ on both $w_1,w_2$ within the transversal, $c\geqslant 2$, but $M$ halts on $c=2$, hence the algorithm terminates with $k\leqslant \max\{|w_1|,|w_2|\}$.

   Therefore $L$ is recognizable.

4. $L$ is undecidable. We’d prove this by Rice’s Theorem. Let $\mathbb{P}$ be the semantic property
   $$
   \mathbb{P}=\{L\sube \Sigma ^*\mid |L|\geqslant 2\}
   $$
    where $\Sigma$ is the alphabet, $|\Sigma|=2$. And since
   $$
   \begin{align}L&=\{\lang M\rang\mid |L(M)|\geqslant  2\text{ where $M$ is a Turing machine}\}\\
   &=\{\lang M\rang\mid M\text{ is a Turing machine and } L(M)\in\mathbb{P}\}=L_\mathbb{P}\end{align}
   $$
   we know $L=L_\mathbb{P}$. We proceed to show that there’s a recognizable language in $\mathbb{P}$ and another not in $\mathbb{P}$. WLOG, let $\Sigma=\{0,1\}$,

   - $\{0,1\}\in\mathbb{P}$ is recognizable since it is finite and contains only strings of length $1$.
   - $\varnothing\notin\mathbb{P}$  is recognizable trivially.

   Thus $\mathbb{P}$ is nontrivial, by Rice’s Theorem, $L=L_\mathbb{P}$ is undecidable.

## Problem 3

1. D-Wave’s computing is processed at a temperature below -273.1℃ to assure its computation is adiabatic. so that by the adiabatic theorem, it can be subjected to gradually changing external conditions and adapts itself such that it retains its initial character and correctly give the solution.

2. At -273.1 ℃.

3. The D-Wave quantum computer work using quantum annealing to search for the lowest energy state of an optimization problem especially where variables takes 0-1 values:

   - Initially all values are simultaneously 0-1
   - Read in and simultaneously, slowly turns off the quantum superposition effect
   - Get a solution

   To mitigate wrong answers, one can run multiple iterations, apply post-processing and error correction techniques, optimize problem formulation and mapping, or benefit from hardware improvements and calibration.

4. In NFA, for a given input symbol, there can be multiple possible transitions that the automata can take, and it may not always have a unique next state. This allows branching and multiple parallel computations. Conversely, DFA only takes unique transition for a given symbol each step, and the next state is also unique.

   Similarly, a probabilistic machine can also have non-determined behavior in its computation. It can have multiple possible states simultaneously and provide probabilistic outputs for certain computations. 

   Therefore it is more like an NFA than a DFA. 



 

1. ```
   
   ```