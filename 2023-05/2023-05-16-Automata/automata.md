## Question 1 

Apparently, $\forall\ w=\underbrace{(a\Sigma^*b)^*}_{\in A^*}=a(\Sigma^*ba\Sigma^*\cdots \Sigma^*)b{\color{purple}\text{ or }\lambda}\in A\cup \{\lambda\}$, hence $A^*\sub A\cup \{\lambda\}$.

Also $A\sub A^*,\{\lambda\}\sub A^*$ corresponding $1$ or $0$ reptations of $a\Sigma^*b$ respectively. Therefore $A^*=A\cup \{\lambda\}$

## Question 2

==$L(M_1)\cap L(M_2)\sub L(M_1\times M_2)$==

For any $w=a_1a_2\ldots a_n\in L(M_1)\cap L(M_2)$ of length $n$, since $w\in L(M_1),L(M_2)$,  it is accepted by $M_1$ and $M_2$, hence 
$$
\delta_1^n(s_1,w)=\delta_1(\delta_1(\delta_1(\cdots),a_{n-1}),a_n)=\iota_1\\
\delta_2^n(s_2,w)=\delta_2(\delta_2(\delta_2(\cdots),a_{n-1}),a_n)=\iota_2\\
$$
Hence in $M_1\times M_2$, $\delta=\delta_1\times \delta_2$
$$
\delta^n((s_1,s_2),w)=\delta(\delta(\delta(\ldots),a_{n-1}),a_{n})=(\iota_1,\iota_2)
$$
i.e. $w$ can be accepted by $M_1\times M_2$. $L(M_1)\cap L(M_2)\sub L(M_1\times M_2)$.

==$L(M_1\times M_2)\sub L(M_1)\cap L(M_2)$==

Since $M_1$ decides $L(M_1)$, $M_2$ decides $L(M_2)$, 

- for $w\not\in L(M_1)$, $\delta_1^n(s_1,w)\neq \iota_1$ for $n=|w|$.
- for $w\not\in L(M_2)$, $\delta_2^n(s_2,w)\neq \iota_2$ for $n=|w|$.

Thus for $w\not\in L(M_1)\cap L(M_2)$, either $w\not\in L(M_1)$ or $w\not\in L(M_2)$. i.e. either $\delta_1^n(s_1,w)=a_i\neq \iota_1$ or $\delta_2^n(s_2,w)=a_j\neq \iota_2$. Therefore $\delta^n((s_1,s_2),w)=(a_i,a_j)\neq (\iota_1,\iota_2)$, hence $w$ is not accepted by $L(M_1\times M_2)$. $L(M_1\times M_2)\sub L(M_1)\cap L(M_2)$

Thus we can conclude that $L(M_1\times M_2)= L(M_1)\cap L(M_2)$, $M_1\times M_2$ decides the language $L(M_1)\cap L(M_2)$.

## Question 3

==Method 1:==

Suppose there's a DFA $M$ for $L$. Consider a subset of $L=\{s\mid s\text{ contains same count of $a$ and $b$}\}$, $S=\{a^nb^n\mid n\geqslant 0\}$. If for any $s\neq t$, $a^s,b^t$ put $M$ in the same state, then $\forall z\in\{a,b\}^*$, $a^s,b^t$ put $M$ in the same state.

But $M$ accepts $a^sb^s,a^tb^t$ but not $a^sb^t,a^tb^s$, hence for any $s\neq t$ $a^s,b^t$ must put $M$ in distinct states. Therefore, to handle $S_n=\{a^nb^n\mid0\leqslant n\leqslant N\}$, $M$ need at least $N$ states. Therefore to accept $S$ and $L$, $M$ needs infinity states. This contradicts the definition of DFA. 

Therefore $L$ can not be accepted by any DFA.

==Method 2:==

A language can be accepted by a DFA if and only if it is regular. By Pumping Lemma, for $L=\{s\mid s\text{ contains same count of $a$ and $b$}\}$, also, we consider the subset of it $S=\{a^nb^n\mid n\geqslant 0\}$.

Consider $xyz=a^nb^n\in L,|xy|\leqslant n$, hence $y$ can only contain $a$'s, $y\neq\lambda$, hence $y$ must contains at least one $a$. let $y=a$, then $xy^2z\not\in L$. By the Pumping Lemma, $L$ could not be regular, hence there's no DFA accepts it.

## Question 4

Since $S$ is finite, we can plug finite independent state into NFA and use union (or) structure to combine them:

<img src="automata.assets/image-20230516080458232.png" alt="image-20230516080458232" style="zoom: 50%;" /> 

In the diagram, $M_1,M_2,\cdots$ are the states for $S$ with merged accepting state (it's also ok not to merge and create new transition to $q_2$), `q2->q1` for the closure.

For example, $S=aa+baab+ba+bbb$, $aa$ is like

<img src="automata.assets/image-20230516080808280.png" alt="image-20230516080808280" style="zoom:50%;" />

$baab$ is like

<img src="automata.assets/image-20230516080915372.png" alt="image-20230516080915372" style="zoom:50%;" />

$ba$ is like

<img src="automata.assets/image-20230516080943974.png" alt="image-20230516080943974" style="zoom:50%;" />

$bbb$ is like

<img src="automata.assets/image-20230516081024718.png" alt="image-20230516081024718" style="zoom:50%;" />

Hence $S^*$ is like 

<img src="automata.assets/image-20230516081349948.png" alt="image-20230516081349948" style="zoom:50%;" />

$e$ for $\varepsilon/\lambda$.

## Question 5

1. The NFA is 

   <img src="automata.assets/image-20230516084339881.png" alt="image-20230516084339881" style="zoom:50%;" />

   which defines $\{ab\}$. Apply the rule we get

   <img src="automata.assets/image-20230516084429159.png" alt="image-20230516084429159" style="zoom:50%;" />

   The language becomes $\{\lambda,a,b,ab\}$.

2. If the original NFA decides $L$, then the modified NFA defines $L'=\{s\in w\mid w\in L\}$, where $s\in w$ means $s=\lambda$ or $s$ is a substring of $w$.

## Question 6

(1)

- If there is a path from the starting state $s$ to the final states $\Iota$, then following the path, we can find a string accepted by the NFA. $L(N)\neq \varnothing$
- If $L(N)\neq\varnothing$, suppose there's no path from the starting from the starting state to the final state. Thus $\forall\ w\in L(N),n\in \N$, the transition function $\delta^n(s,w)\not\in \Iota$. $w$ is not accepted by the machine. Contradictory.

Thus $L(N)\neq\varnothing $ if and only if there's no path from the starting state to the final states.

(2)

==IF== If there's a path from $s$ to $\iota$, for any $R$ as a regex expression and not a single letter, then it can be decomposed into $LT$ or $L+T$ or $L^*$, by the description, 

- If decomposed into $LT$, we can find a DFA such that the final state of $L$, say $\zeta$ is the start state of $T$, hence there is path from $s$ to $\zeta$ and from $\zeta$ to $\iota$. Then run our algorithm on $L$ and $T$.
- If decomposed into $L+T$, we can find an NFA such that the start and final state of $L,T$ are the same. hence there's a path along $L$ **or** along $R$. Then run our algorithm on L and $T$.
- If decomposed into $L^*$, return `false` by the description.
- If $R$ is a letter, return `false`

Running the algorithm recursively, we can conclude that that it must return `false` on the assumption above.

==ONLY IF== If the algorithm returns `false`, then the NFA can decide nested expressions composed by the 4 occasions above. Thus there must be a path from $s$ to $\iota$.

## Question 7 

We can design a non-final dead state $d$ representing the state that $L$ is exceeding $R$ in count by at least $4$. Other states:

- $q_0$: Initial and final state. Exceeds by 0.  Move to $q_1$ if $L$ eaten, move to $d$ if $R$ eaten (parathesis not paired).
- $q_1$: Exceeds by 1. Move to $q_2$ if $L$ eaten, move to $q_0$ if $L$ eaten.
- $q_2$: Exceeds by 2. Move to $q_3$ if $L$ eaten, move to $q_1$ if $R$ eaten.
- $q_3$: Exceeds by 3. Move to $d$ if $L$ eaten (exceeds over 4), move to $q_2$ if $R$ eaten.
- $d$: Exceeds by at least 4 or the parathesis are not paired. Move to $d$ for all inputs.

<img src="automata.assets/image-20230516203645917.png" alt="image-20230516203645917" style="zoom:50%;" />

Try to minimize:

- $S=\{d,q_1,q_2,q_3\}, T=\{q_0\}$
- $q_1$ eats $R$ and move to $T$, $q_2,q_3,d$ eats $R$ and stay in $S$​, hence we'd divide $S=\{q_1\}\cup\{q_2,q_3,d\}$
- $q_2$ eats $R$ and move to $\{q_1\}$, $q_3,d$ eats $R$ and stay in $\{q_2,q_3,d\}$,  hence we'd divide $S=\{q_1\}\cup\{q_2\}\cup\{q_3,d\}$
- $q_3$ eats $R$ and move to $\{q_2\}$, eats $L$ and stay in $\{q_3,d\}$, 
- Thus we should divide $S=\{q_0\}\cup\{q_1\}\cup\{q_2\}\cup \{q_3\}$

Now we get exactly the same DFA as the previous one. Hence this DFA is already minimized.

Regex: `((LR)*L(LR)*L(LR)*L(LR)*R(LR)*R(LR)*R(LR)*)|((LR)*L(LR)*L(LR)*R(LR)*R(LR)*)|((LR)*L(LR)*R(LR)*)|(LR)*`

## Question 8

==Basic Idea:== follow the following procedure:

1. we scan the length to reach the blank right after $w$ and write a new character to flag end
2. move head back to the far left
3. for each character in the string, move the head to the far end and write down it and convert all a, b to x, y, then go back to the nearest x, y
4. loop 3 until c met.
5. go back and transform x, y back to a, b
6. go right and cancel c to blank

==Description of steps in detailed states:==

1. First convert all a’s, b’s into a’s, b’s and go right then the right most blank into $c$ and go left 
2. Then convert all a’s, b’s into a’s, b’s and go left
3. If b convert it into $x$ and go right convert all a’s, b’s into a’s, b’s and go right then, convert $c$ into $c$ and go right then convert all a’s, b’s into a’s, b's and go right then convert blank into $1$ and go left then convert all a’s, b’s into a’s, b’s and go left then convert $c$ into $c$ and go left then convert all a’s, b’s into a’s, b’s and go left then convert all x into x and go right and then repeat all the process from step-2 till end 
4. If a then convert it into y and go right then convert all a’s, b’s into a’s, b’s and go right then convert c into c and go right then convert all a’s, b’s into a’s, b’s and go right then convert blank into a and go left then convert all a’s, b’s into a’s, b’s and go left then convert c into c and go left then convert all a’s, b’s into a’s, b’s and go left then convert all y into y and go right and then repeat all the process from step-2 till end 
5. Otherwise if c found convert it into c and go left then convert all x into b and y into a and go left then convert blank into blank, c into blank and go right and **stop the machine.** 

![image-20230516072443652](automata.assets/image-20230516072443652.png)

[Turing machine visualization](https://turingmachine.io/) code:

```yaml
input: 'abba'
blank: ' '
start state: start
table:
  start:
    ['a','b']: R
    ' '  : {write: 'c', L: q1}
  q1:
    ['a','b']: L
    ' ': {R: q2}
  q2:
    'a': {write: 'y', R: q3}
    'c': {L: q11}
    'b': {write: 'x', R: q7}
  q3: 
    ['a','b']: R
    'c': {R: q4}
  q4: 
    ['a','b']: R
    ' ': {write: 'a', L: q5}
  q5:
    ['a','b']: L
    'c': {L: q6}
  q6:
    ['a','b']: L
    'y': {R: q2}
  q7:
    ['a','b']: R
    'c': {R: q8}
  q8:
    ['a','b']: R
    ' ': {write: 'b', L: q9}
  q9:
    ['a','b']: L
    'c': {L: q10}
  q10:
    ['a','b']: L
    'x': {R: q2}
  q11:
    'x': {write: 'b', L: q11}
    'y': {write: 'a', L: q11}
    ' ': {R: q12}
  q12:
    ['a','b']: R
    'c': {write: ' ', R: q13}
  q13:
    ['a','b']: R
    ' ': {R: done}
  done:
```

