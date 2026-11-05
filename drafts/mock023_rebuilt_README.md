# GATE CS 2027 — Full-Length Mock Test 023

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

Q1–Q5 and Q11–Q35 carry one mark each; the others carry two. Each MCQ has one correct option; an incorrect MCQ loses one-third of its marks. MSQs require all correct options and award no partial credit. MSQs and NATs have no negative marking. Unattempted questions score zero. General Aptitude contributes15 marks, Engineering Mathematics13 and core CS72. Numerical answers are exact unless rounding is requested.

## Section A — General Aptitude

### Q1. [1 Mark] [MCQ]

A machine maps every integer n to an integer f(n). Tests establish f(1)=2, f(2)=4 and f(3)=6; no other restriction on f is given. Which claim is justified?

A. f(4) must equal8.
B. f is necessarily linear.
C. The observations are consistent with f(n)=2n but do not uniquely establish it.
D. No function can satisfy all three observations.

### Q2. [1 Mark] [NAT]

Some unit cubes occupy cells of a2×2×2 grid. Looking along each of the three coordinate axes, all four cells in the corresponding2×2 projection must appear occupied. What is the minimum possible number of unit cubes?

**Answer format:** Integer.

### Q3. [1 Mark] [NAT]

A sequence starts with a1=1 and satisfies a(n+1)−a(n)=2n+1 for n≥1. For how many n in {1,...,10} is a(n+1)−a(n) greater than a(n)?

**Answer format:** Integer.

### Q4. [1 Mark] [NAT]

The diagonals of a trapezium intersect at O. The two triangles having the parallel sides as bases and O as their opposite vertex have areas9 and16. What is the area of the entire trapezium?

**Answer format:** Exact number.

### Q5. [1 Mark] [MCQ]

Which sentence states that every report was read by at least one reviewer, without asserting that a single reviewer read all reports?

A. One reviewer read every report.
B. Every report was read by some reviewer.
C. Every reviewer read every report.
D. No reviewer read a report.

### Q6. [2 Marks] [NAT]

An examination awards4 marks for a correct response, subtracts1 for a wrong response and awards0 for an omitted question. A candidate attempted75% of40 questions and scored75 marks. How many attempted responses were wrong?

**Answer format:** Integer.

### Q7. [2 Marks] [MCQ]

Exactly two of A,B,C attend a meeting. A says “B attends”; B says “C does not attend”; C says “A does not attend.” Exactly one of these statements is true, regardless of whether its speaker attends. Who does not attend?

A. A
B. B
C. C
D. No assignment satisfies the conditions.

### Q8. [2 Marks] [MSQ]

A rigid planar transformation is built by composing rotations and reflections in lines. Translations are allowed. Which statements are correct?

A. One reflection followed by any rotation reverses the clockwise order of three noncollinear labelled points.
B. Two reflections necessarily return every point to its original position.
C. A composition of two reflections preserves distances and orientation.
D. A translation can change the area of a triangle.

### Q9. [2 Marks] [MCQ]

A researcher writes: “No failure was observed in a hundred trials. This excludes failure in those trials but does not establish that failure is impossible.” Which additional claim conflicts with that qualification?

A. The observed failure count was zero.
B. The tested system may still fail in an untested situation.
C. Future observations could require revising the assessment.
D. A future failure is logically impossible solely because of these trials.

### Q10. [2 Marks] [NAT]

How many distinct arrangements of the multiset of letters A,A,B,B,C contain no adjacent A's?

**Answer format:** Integer.

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

Two1000-bit packets traverse a store-and-forward router. The incoming link transmits1000 bits/ms; the outgoing link transmits500 bits/ms. Both packets are ready at the source at time0, propagation is negligible, and the router starts forwarding a packet only after receiving it completely. At what time, in milliseconds, does the last bit of the second packet leave the router?

**Answer format:** Exact number.

### Q12. [1 Mark] [NAT]

Tables R(x) and S(x) contain rows R={1,1,2,NULL} and S={1,NULL}. Under SQL's usual NULL semantics, how many rows does this query return?

```sql
SELECT r.x FROM R r
WHERE NOT EXISTS (SELECT 1 FROM S s WHERE s.x = r.x);
```

**Answer format:** Integer.

### Q13. [1 Mark] [NAT]

During merge-based inversion counting, the sorted left half is[2,5,7] and the sorted right half is[1,5,6]. An inversion is a pair of positions i<j with value[i]>value[j], strictly. How many cross-half inversions are counted at this merge?

**Answer format:** Integer.

### Q14. [1 Mark] [MSQ]

A compiler considers replacing x/x by1 for a signed integer x. Division by zero is invalid; all other values here are representable. Which statements are correct?

A. The rewrite preserves the defined result whenever x is known to be nonzero.
B. The rewrite preserves every possible runtime error when x may be zero.
C. A dominating condition that establishes x!=0, with no intervening modification, can justify the rewrite on that path.
D. Textual repetition of x alone proves the rewrite safe for every input.

### Q15. [1 Mark] [NAT]

A counting semaphore is initialized to2. Three threads each execute wait(S), then enter a region, and signal(S) only upon leaving it. All semaphore operations are atomic. Before any thread leaves the region, what is the maximum number of threads that can have entered it?

**Answer format:** Integer.

### Q16. [1 Mark] [MSQ]

The following code operates on ordinary integer variables; assignment copies a value and does not create an alias.

```text
x = 4
y = x
x = 9
z = y + x
```

Which statements are correct?

A. z is13.
B. y is9 at the end.
C. The value assigned by the first line contributes to z.
D. Changing x on line3 also changes y.
### Q17. [1 Mark] [NAT]

A differentiable function f on the real line satisfies f(0)=0 and f'(x)≥2 for every real x. What is the smallest possible value of f(3)−f(−1)?

**Answer format:** Exact number.

### Q18. [1 Mark] [NAT]

An instruction uses base-plus-scaled-index addressing: effective address=base+4×index+displacement. The index register contains−3, base contains100 and displacement is20. A32-bit word is loaded from that effective address. What is the byte address of its last byte?

**Answer format:** Integer.

### Q19. [1 Mark] [MSQ]

Given two arbitrary Turing machines M1,M2 and an input w, a simulator alternates one step of each machine on w. It accepts as soon as either simulation accepts. Which statements are correct?

A. It recognizes the union of the two recognized languages.
B. It always halts if neither machine accepts w.
C. It avoids being trapped forever in M1 before giving M2 any steps.
D. It decides the intersection of the languages.

### Q20. [1 Mark] [NAT]

A four-bit ALU performs a logical left shift by one on bit pattern1011, discarding the outgoing most significant bit and filling the low bit with0. Interpret the result as a signed two's-complement integer. What value results?

**Answer format:** Integer.

### Q21. [1 Mark] [MSQ]

An unweighted directed graph has edges s→a,s→b,a→c,b→d,d→c. A BFS begins at s and marks vertices when enqueued. Which statements are correct regardless of the order of s's adjacency list?

A. c is assigned distance2.
B. c may be assigned distance3 if b is examined first.
C. d is assigned distance2.
D. Every vertex's BFS parent is necessarily unique in every directed graph.

### Q22. [1 Mark] [NAT]

Two independent fair coins are tossed. Their colours are red and blue, so they are distinguishable. A report states that the red coin is heads. What is the conditional probability that exactly one coin is heads?

**Answer format:** Exact decimal.

### Q23. [1 Mark] [MSQ]

In the subset lattice of {a,b,c}, ordered by inclusion, which statements are correct?

A. The meet of{a,b} and{b,c} is{b}.
B. Their join is{a,b,c}.
C. They are comparable.
D. The empty set is a lower bound of every pair of elements.

### Q24. [1 Mark] [NAT]

For Boolean variables a,b,c, how many assignments satisfy (a OR b) AND ((NOT a) OR c) while making b OR c false?

**Answer format:** Integer.

### Q25. [1 Mark] [MCQ]

A queue is implemented with two stacks. Enqueue pushes onto stack I. Dequeue pops stack O if nonempty; otherwise it moves all of I to O by repeated pops and pushes, then pops O. Which statement is correct for a sequence starting with both stacks empty?

A. Each element can move from I to O at most once before removal.
B. Every dequeue performs a constant number of stack operations in the worst case.
C. Moving I to O reverses FIFO order incorrectly.
D. Every enqueue must first empty O.

### Q26. [1 Mark] [NAT]

A DFA over {0,1} stores the parity of the number of0s and the parity of the number of1s. It accepts exactly when both counts are odd. What is the minimum number of states required?

**Answer format:** Integer.

### Q27. [1 Mark] [MSQ]

A binary linear error-detecting code regards a received vector as valid exactly when its syndrome is zero. Which statements are correct?

A. Adding a nonzero codeword as an error pattern is undetected.
B. A zero syndrome proves that no bits were altered.
C. The syndrome of the received word equals the syndrome of the error when the transmitted word was valid.
D. Every nonzero error pattern has a nonzero syndrome.

### Q28. [1 Mark] [NAT]

A=LU, where L is unit lower triangular and U is upper triangular with diagonal entries2,−3,4. No row permutation is involved. What is det(A)?

**Answer format:** Integer.

### Q29. [1 Mark] [NAT]

A four-variable Boolean function is1 on exactly the minterms0000,0001,0011,0010 and0 elsewhere. How many literals occur in a minimum sum-of-products expression?

**Answer format:** Integer.

### Q30. [1 Mark] [NAT]

In a collision-detection network, the maximum one-way propagation delay is20 microseconds. A sender must still be transmitting when a worst-case collision indication returns. At10 megabits per second, what is the minimum frame length, in bits, required by this timing condition alone?

**Answer format:** Integer.

### Q31. [1 Mark] [NAT]

Let f be integrable on[0,1] and satisfy f(x)+f(1−x)=6 for every x. What is its integral over[0,1]?

**Answer format:** Exact number.

### Q32. [1 Mark] [MSQ]

A table has PRIMARY KEY(id) and a foreign key parent_id referencing id in the same table. parent_id is nullable and no further constraint is specified. Which statements are correct?

A. A row may have parent_id=NULL.
B. The foreign key alone prevents cycles of length two.
C. A row whose parent_id equals its own existing id can satisfy these constraints.
D. Every non-null parent_id must reference an existing key when the constraint is checked.

### Q33. [1 Mark] [NAT]

A rooted ordered tree has root R with children A,B,C in that order. A has children D,E, B has none and C has child F. In the left-child/right-sibling binary representation, how many right-sibling pointers are non-null?

**Answer format:** Integer.

### Q34. [1 Mark] [MCQ]

Two threads always acquire mutexes X and Y in the order X then Y, and release both after finite computation. No other resources or waits exist. Which statement is correct?

A. A cycle of these two threads each holding one of X,Y and waiting for the other is possible.
B. The common acquisition order excludes a circular wait involving these mutexes.
C. The order guarantees equal waiting times.
D. Deadlock freedom implies that neither thread can ever wait.

### Q35. [1 Mark] [NAT]

For grammar S→aSb | SS | ε, what is the minimum number of applications of S→aSb needed in any derivation of aabbab?

**Answer format:** Integer.


### Q36. [2 Marks] [NAT]

Immediately before this fragment, x and y hold arbitrary values. Immediately afterward, both are needed. A compiler gives each of the names x,y,t one fixed register throughout the fragment. Two names that are simultaneously live must use different registers; live ranges may not be split and the assignments may not be rewritten.

```text
t = x
x = y
y = t
```

What is the minimum number of registers under these rules?

**Answer format:** Integer.

### Q37. [2 Marks] [NAT]

The five observations are0,1,2,3,t, where t is a real number constrained by t≥3. What is the minimum population variance of these five observations?

**Answer format:** Exact decimal.

### Q38. [2 Marks] [NAT]

An undirected graph on A,B,C,D has edges AB(1), BC(2), CD(3), DA(4), AC(5), BD(6), with weights in parentheses. What is the minimum weight of a spanning tree whose weight is strictly greater than the minimum-spanning-tree weight?

**Answer format:** Integer.

### Q39. [2 Marks] [MSQ]

In a tabular Boolean-minimization procedure, two product cubes may be combined only if their don't-care positions are identical and they differ in exactly one remaining bit. Here '-' denotes a don't-care position. Which pairs can be combined under that rule?

A. 0-01 and0-11.
B. 00-1 and0-01.
C. -100 and-101.
D. 0101 and1010.

### Q40. [2 Marks] [MSQ]

Relation R(A,B,C,D) has dependency set F={AB→C, C→B, A→D, D→C}. Which statements are correct?

A. AB→C can be removed without changing the closure of F.
B. C→B can be removed without changing the closure of F.
C. A is a candidate key of R.
D. D is a candidate key of R.
### Q41. [2 Marks] [MSQ]

A binary search tree stores distinct keys. An algorithm claims that checking only “each left child is smaller than its parent and each right child is larger” is sufficient to validate the whole BST. Which statements are correct?

A. The local condition is necessary.
B. The local condition is sufficient.
C. A tree with root10, left child5 and5's right child12 is a counterexample to sufficiency.
D. Propagating ancestor-imposed lower and upper bounds can detect the counterexample.

### Q42. [2 Marks] [MCQ]

An NPDA recognizes strings ww^R over {a,b} by nondeterministically choosing a midpoint, pushing before the midpoint and matching/popping afterward. It accepts only when the input is exhausted and the stack is empty. Which statement correctly explains the midpoint choice?

A. Every midpoint guess must accept for the input to be accepted.
B. A successful branch must choose a midpoint leaving equally long push and pop portions; wrong guesses may reject.
C. The machine needs two stacks to compare the reverse.
D. Nondeterminism allows acceptance with unread symbols.

### Q43. [2 Marks] [NAT]

A microsequencer has a7-bit next-address field. A conditional microinstruction chooses between the encoded address a and address a+1 by setting the low address bit to a Boolean condition; all upper bits come from a. This works only for aligned address pairs. How many disjoint target pairs can be represented in a128-word control store?

**Answer format:** Integer.

### Q44. [2 Marks] [NAT]

A byte-addressed memory uses four banks, selected by the low two address bits. Each bank stores one byte at each local row; the remaining address bits select that row. A four-byte word beginning at byte address6 is read. How many distinct local row numbers are accessed across its four bytes?

**Answer format:** Integer.

### Q45. [2 Marks] [MSQ]

In this code, p points to a valid integer object, f may modify that object, and integer arithmetic does not overflow:

```text
u = *p + 2
call f()
v = *p + 2
```

Which statements are correct?

A. Identical text proves v may be replaced by u.
B. A proof that f cannot modify the pointed-to object can make that reuse valid.
C. If f changes the object, the two evaluations may differ.
D. A function call is never relevant to memory-expression availability.

### Q46. [2 Marks] [NAT]

Routers A,B,C form a line with link costs AB=1 and BC=1. Destination C initially has distances at A=2,B=1. Link BC fails. Before receiving B's failure update, A advertises its old distance2 to B. With ordinary distance-vector updating and no split horizon, what distance can B incorrectly adopt through A?

**Answer format:** Integer.

### Q47. [2 Marks] [MSQ]

An IPv4 receiver reassembles fragments using the tuple(source address,destination address,protocol,identification). Two fragments have the same identification value but different source addresses. Which statements are correct under this rule?

A. They belong to different reassembly contexts.
B. Equal identification values alone are sufficient to combine them.
C. The fragment offset determines placement within a context rather than replacing the context key.
D. Arrival order alone uniquely identifies which datagram each fragment belongs to.
### Q48. [2 Marks] [NAT]

A processor's execution time is40% memory-stall time and60% other time on a fixed workload. A proposed change halves only the memory-stall component but increases the other component by10%. What is the new execution time as a percentage of the original time?

**Answer format:** Exact percentage number, without the percent symbol.

### Q49. [2 Marks] [MSQ]

A routing table contains prefix203.0.113.0/24 via X and more-specific prefix203.0.113.128/25 via Y. No other route matches. Which statements are correct under longest-prefix matching?

A. Address203.0.113.200 uses Y.
B. Address203.0.113.100 uses X.
C. Installing the /24 after the /25 necessarily makes it override the /25.
D. Removing the /25 makes203.0.113.200 use X.

### Q50. [2 Marks] [MSQ]

A finite monoid M has identity e and satisfies left cancellation: ax=ay implies x=y for all a,x,y in M. Which statements follow?

A. For fixed a, the map x↦ax is a bijection on M.
B. Every a has a right inverse b with ab=e.
C. Such a b also satisfies ba=e.
D. The conclusion that every element is invertible follows by the same finite-cardinality argument for arbitrary infinite monoids.

### Q51. [2 Marks] [NAT]

A binary max-heap contains distinct keys. The heap has15 elements and is represented in a one-based array. A decrease-key operation changes the root to a value smaller than every other key, then restores heap order by repeatedly swapping with the larger child. How many swaps occur?

**Answer format:** Integer.

### Q52. [2 Marks] [MSQ]

Let h be a homomorphism that maps each symbol of a finite alphabet to a finite string, possibly ε. Which statements are correct?

A. The image under h of a regular language is regular.
B. The image under h of a context-free language is context-free.
C. A nonregular language must remain nonregular under every such h.
D. Erasing every symbol maps every nonempty language to{ε}.

### Q53. [2 Marks] [NAT]

A lexer has tokens IF for the keyword if and ID for a letter followed by zero or more letters or digits. It first uses longest match and then gives IF priority over ID only when lengths tie. Spaces separate tokens. For input “if if2 iff if”, how many ID tokens are produced?

**Answer format:** Integer.

### Q54. [2 Marks] [NAT]

A single CPU schedules P,Q,R nonpreemptively in increasing burst-time order; all arrive at time0. Bursts are2,4,6. Switching between consecutive processes costs1 time unit; there is no initial switch cost. What is the sum of their turnaround times?

**Answer format:** Integer.

### Q55. [2 Marks] [NAT]

A combinational circuit implements unsigned comparison A>B for two-bit inputs A=a1a0 and B=b1b0. Among the16 possible input pairs, for how many does the low-bit comparison a0>b0 disagree with the full comparison A>B?

**Answer format:** Integer.

### Q56. [2 Marks] [NAT]

A file contains1000 fixed-size records of80 bytes in4000-byte data blocks, with no headers and no spanning. A sparse index has one16-byte entry per data block and is stored in4000-byte index blocks. No blocks are cached. A successful lookup first reads the required index block, then the selected data block. What is the total number of block reads for that lookup?

**Answer format:** Integer.

### Q57. [2 Marks] [MSQ]

A synchronous machine has two different states that produce the same output now. Which statements are correct about state minimization?

A. Equal current outputs alone guarantee equivalence.
B. A future input sequence yielding different output sequences distinguishes the states.
C. Equivalent states must have equivalent successors for every input under the usual deterministic Moore-machine definition.
D. Different state encodings alone guarantee distinguishability by external observations.

### Q58. [2 Marks] [NAT]

A directed graph with four vertices has adjacency matrix A, where A[i,j] is the number of directed edges i→j. Its only edges are1→2,1→3,2→4,3→4,4→1, one of each. What is entry(1,1) of A³?

**Answer format:** Integer.

### Q59. [2 Marks] [NAT]

A disk head at cylinder40 uses SSTF with pending requests at10,45,70. No new requests arrive; ties favour the smaller cylinder. After all requests are served, what is its total head movement?

**Answer format:** Integer cylinders.

### Q60. [2 Marks] [NAT]

An initially empty B+ tree has a single root leaf. Each leaf holds at most three keys. Inserting a fourth key splits a leaf into two leaves of two keys each, promoting the first key of the right leaf to the parent; the key remains in the leaf. Insert1,2,3,4,5,6 in order. The internal root can hold at least three separators. How many leaf nodes exist afterward?

**Answer format:** Integer.

### Q61. [2 Marks] [MSQ]

For L={0^n1^n : n≥0}, choose0^p1^p in a pumping-lemma argument, where p is a proposed regular pumping length. Which statements are correct?

A. Every legal pumped part lies entirely in the0 block.
B. Pumping that nonempty part down changes the number of0s while leaving the number of1s unchanged.
C. One must know the exact pumped-part length before choosing the original string.
D. The resulting contradiction disproves regularity.

### Q62. [2 Marks] [NAT]

A simple graph contains a five-cycle a–b–c–d–e–a and two additional vertices p,q. Each of p,q is adjacent to all five cycle vertices, but p and q are not adjacent to each other. There are no other edges. What is the graph's chromatic number?

**Answer format:** Integer.
### Q63. [2 Marks] [NAT]

How many permutations of {1,2,3,4,5} place1 before2 before3, with no restriction on the relative positions of4 and5?

**Answer format:** Integer.

### Q64. [2 Marks] [NAT]

A paged process uses virtual addresses of16 bits with1024-byte pages. A valid page-table entry maps virtual page5 to physical frame12. What physical byte address corresponds to virtual byte address5500?

**Answer format:** Integer.

### Q65. [2 Marks] [MSQ]

A directed graph has no negative cycle. Potentials h(v) reweight every edge u→v by w'(u,v)=w(u,v)+h(u)−h(v). Which statements are correct?

A. All paths between fixed endpoints have their weights shifted by the same amount.
B. The ordering of path weights between fixed endpoints is preserved.
C. An arbitrary choice of h necessarily makes every edge weight nonnegative.
D. Every directed cycle retains its original total weight.

---

## ANSWER KEY — MOCK TEST 023

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | C |
| 2 | NAT | 1 | 4 |
| 3 | NAT | 1 | 2 |
| 4 | NAT | 1 | 49 |
| 5 | MCQ | 1 | B |
| 6 | NAT | 2 | 9 |
| 7 | MCQ | 2 | D |
| 8 | MSQ | 2 | A, C |
| 9 | MCQ | 2 | D |
| 10 | NAT | 2 | 18 |
| 11 | NAT | 1 | 5 |
| 12 | NAT | 1 | 2 |
| 13 | NAT | 1 | 5 |
| 14 | MSQ | 1 | A, C |
| 15 | NAT | 1 | 2 |
| 16 | MSQ | 1 | A, C |
| 17 | NAT | 1 | 8 |
| 18 | NAT | 1 | 111 |
| 19 | MSQ | 1 | A, C |
| 20 | NAT | 1 | 6 |
| 21 | MSQ | 1 | A, C |
| 22 | NAT | 1 | 0.5 |
| 23 | MSQ | 1 | A, B, D |
| 24 | NAT | 1 | 0 |
| 25 | MCQ | 1 | A |
| 26 | NAT | 1 | 4 |
| 27 | MSQ | 1 | A, C |
| 28 | NAT | 1 | -24 |
| 29 | NAT | 1 | 2 |
| 30 | NAT | 1 | 400 |
| 31 | NAT | 1 | 3 |
| 32 | MSQ | 1 | A, C, D |
| 33 | NAT | 1 | 3 |
| 34 | MCQ | 1 | B |
| 35 | NAT | 1 | 3 |
| 36 | NAT | 2 | 3 |
| 37 | NAT | 2 | 1.36 |
| 38 | NAT | 2 | 7 |
| 39 | MSQ | 2 | A, C |
| 40 | MSQ | 2 | A, C |
| 41 | MSQ | 2 | A, C, D |
| 42 | MCQ | 2 | B |
| 43 | NAT | 2 | 64 |
| 44 | NAT | 2 | 2 |
| 45 | MSQ | 2 | B, C |
| 46 | NAT | 2 | 3 |
| 47 | MSQ | 2 | A, C |
| 48 | NAT | 2 | 86 |
| 49 | MSQ | 2 | A, B, D |
| 50 | MSQ | 2 | A, B, C |
| 51 | NAT | 2 | 3 |
| 52 | MSQ | 2 | A, B, D |
| 53 | NAT | 2 | 2 |
| 54 | NAT | 2 | 23 |
| 55 | NAT | 2 | 4 |
| 56 | NAT | 2 | 2 |
| 57 | MSQ | 2 | B, C |
| 58 | NAT | 2 | 2 |
| 59 | NAT | 2 | 90 |
| 60 | NAT | 2 | 3 |
| 61 | MSQ | 2 | A, B, D |
| 62 | NAT | 2 | 4 |
| 63 | NAT | 2 | 20 |
| 64 | NAT | 2 | 12668 |
| 65 | MSQ | 2 | A, B, D |


