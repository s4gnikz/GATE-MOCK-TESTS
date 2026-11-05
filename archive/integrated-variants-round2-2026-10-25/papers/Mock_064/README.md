# GATE CS 2027 — Full-Length Mock Test 064

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard (target)

## General Instructions

- Attempt the paper within 180 minutes.
- Q1–Q5 and Q11–Q35 carry one mark each; Q6–Q10 and Q36–Q65 carry two marks each.
- General Aptitude contributes 15 marks, Engineering Mathematics 13 marks, and core Computer Science 72 marks.
- MCQ: choose exactly one option. Incorrect one-mark MCQs lose 1/3 mark; incorrect two-mark MCQs lose 2/3 mark.
- MSQ: select all and only the correct options. There is no partial credit and no negative marking.
- NAT: enter the numerical answer at the stated precision. There is no negative marking.
- Unattempted questions receive zero. The answer key follows Question 65.

---

## Section A — General Aptitude

### Q1. [1 Mark] [NAT]

A factory produces 300 units with a 2% defect rate and another 200 units with a 5% defect rate. What percentage of the combined output is defective?

**Answer format:** Exact finite decimal percentage, without the percent sign.

### Q2. [1 Mark] [NAT]

A square sheet occupies[0,8]×[0,8]. Fold the right half left across x=4 and then the top half down across y=4. A point-sized hole is punched at(4,2), on one fold line but not the other. How many distinct point holes appear after unfolding? Ignore the hole's radius and count distinct coordinates only.

**Answer format:** Integer.

### Q3. [1 Mark] [MCQ]

Arrange these sentences into the most coherent chronological paragraph, using the references “that inspection” and “second inspection” consistently.

P. This second inspection found no leak.  
Q. The crew replaced the cracked valve and inspected the pipe again.  
R. A pressure drop first prompted an inspection.  
S. That inspection identified a crack in the valve.

A. R,Q,S,P  
B. S,R,Q,P  
C. R,S,Q,P  
D. Q,P,R,S

### Q4. [1 Mark] [NAT]

A bag contains two red and two blue balls. Two balls are drawn without replacement. The first ball's colour is not revealed. A truthful observer reports only that at least one of the drawn balls is red. What is the probability that both are red? Round to four decimal places.

**Answer format:** Decimal rounded to four places.

### Q5. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“The panel gave the proposal a qualified endorsement: it supported the idea, provided that the budget and access arrangements were revised.” What does “qualified” mean here?

A. Issued by a person holding a professional certificate.  
B. Limited by stated conditions.  
C. Completely withdrawn.  
D. Expressed without reservation.

### Q6. [2 Marks] [NAT]

A population starts at 800, increases by 25% in the first year, decreases by 20% in the second, and increases by 10% in the third. What constant annual percentage growth rate over the same three years gives the same final population? Round to two decimal places.

**Answer format:** Number to 2 decimal places, without the percent sign.

### Q7. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A conjecture states: “For every positive integer n, n²+n+41 is prime.” Which single calculation is sufficient to refute the conjecture?

A. It equals43 at n=1.  
B. It equals47 at n=2.  
C. It equals41² at n=40.  
D. It is odd at n=3.

### Q8. [2 Marks] [NAT]

Unit cubes are stacked in four columns on a2×2 base. A column may have height0,1,or2. The maximum heights seen in the two rows are respectively2 and1; the maximum heights seen in the two columns are respectively2 and1. Rows and columns have fixed labels. How many different height arrays satisfy these four maxima?

**Answer format:** Integer.

### Q9. [2 Marks] [NAT]

Let a1=1 and a(n+1)=a(n)+n². Find a5.

**Answer format:** Integer.

### Q10. [2 Marks] [NAT]

A cylindrical tank has radius 3 m and initially contains water to height 4 m. A solid sphere of radius 1.5 m is lowered completely below the water without touching the tank walls, and no water spills. By how many metres does the water level rise? Treat π symbolically.

**Answer format:** Exact finite decimal.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

A connected undirected graph has four vertices and every edge has weight 7. How much does any minimum spanning tree weigh?

**Answer format:** Integer.

### Q12. [1 Mark] [MSQ]

Events A,B have P(A)=0.8 and P(B)=0.7. Which additional specifications are individually consistent with these two probabilities?

A. P(A∩B)=0.4
B. P(A∩B)=0.6
C. P(A|B)=0.5
D. P(A∪B)=1

### Q13. [1 Mark] [NAT]

An Ethernet learning switch has hosts A,B,C on distinct ports1,2,3. Its forwarding table is initially empty. It learns a source address before deciding how to forward that frame. In order, it receives unicast frames A→B, B→A, and C→A. There is no aging or other traffic. How many frame copies in total are transmitted by the switch over its output ports?

**Answer format:** Exact integer.

### Q14. [1 Mark] [NAT]

Find the limit as x tends to zero of (sin x−x)/x³. Angles are in radians. Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q15. [1 Mark] [MSQ]

For the following straight-line code, which variables are live immediately after the second statement? Use ordinary syntactic liveness on this code as written, before dead-code elimination; there are no implicit uses at return.

```text
x = a+b
y = x*c
x = d
return y
```

A. x
B. d
C. c
D. y

### Q16. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For Boolean variables x,y, which expressions equal x XOR y for all inputs?

**Candidates**

**I.** x′y + xy′

**II.** (x+y)(x′+y′)

**III.** xy + x′y′

**IV.** x+y

A. III and IV  
B. I and III  
C. I and II  
D. I and IV

### Q17. [1 Mark] [MCQ]

Which grammar is the direct left-factored equivalent of S→ab | ac | a, with ε denoting the empty string?

A. S→aX; X→b | c | ε
B. S→Xa; X→b | c | ε
C. S→aX; X→bX | cX | ε
D. S→a; X→b | c

### Q18. [1 Mark] [NAT]

A directed graph on vertices 0–3 is stored in CSR form with row pointers [0,2,2,5,6] and column indices [1,3,0,2,3,1]. Outgoing neighbours of vertex i occupy indices row[i] through row[i+1]−1. What is the minimum number of directed edges that must be added to make the graph strongly connected?

**Answer format:** Integer.

### Q19. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For L={a^n b^n : n≥0}, choose z=a^p b^p in a pumping-lemma argument, where p≥1. Which statement correctly addresses every decomposition z=uvw with |uv|≤p and |v|≥1?

A. v contains only a's, so removing v produces a string outside L.  
B. v contains equal numbers of a's and b's, so repeating v stays in L.  
C. Some suitable decomposition must be chosen by the person proving nonregularity.  
D. The lemma allows v to be empty if u is nonempty.

### Q20. [1 Mark] [NAT]

A horizontal microinstruction has five independent one-bit control signals and an eight-bit next-address field. A redesigned encoding replaces the five control bits by a three-bit code selecting one of six permitted control combinations, retaining the next-address field unchanged. How many bits per microinstruction are saved?

**Answer format:** Integer.

### Q21. [1 Mark] [MCQ]

All variables below are distinct scalar integers, with exact arithmetic and no side effects. Which expression can replace the right-hand side of the last assignment while preserving the program's result for every initial state?

```text
t = a + b
a = a + 1
u = a + b
```

A. t
B. t + 1
C. t − 1
D. b + 1

### Q22. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

SQL table T(x) has two rows, both x=NULL. Compare Q1=SELECT COUNT(*) FROM (SELECT DISTINCT x FROM T) AS U and Q2=SELECT COUNT(DISTINCT x) FROM T. What pair of scalar results (Q1,Q2) is returned?

A. (0,0)  
B. (2,0)  
C. (1,1)  
D. (1,0)

### Q23. [1 Mark] [NAT]

A binary search repeatedly compares the target with a midpoint key, returning on equality and otherwise searching the appropriate remaining half. Midpoint is floor((low+high)/2). On the sorted keys 1 through 15, how many key comparisons find target 14?

**Answer format:** Integer.

### Q24. [1 Mark] [NAT]

Four routers S,A,B,C have undirected links SA,SB,AC,BC,AB. S originates one new link-state advertisement and sends it on every incident link. Each other router, on its first receipt, forwards one copy on every incident link except the one on which that first copy arrived; later duplicates are discarded without forwarding. Links are reliable, and acknowledgement traffic is ignored. How many advertisement transmissions occur in total, counting each direction separately?

**Answer format:** Integer.

### Q25. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A source-reachable directed graph has nonnegative edge weights, some equal to zero. Which statements about Dijkstra's algorithm are correct?

**Candidates**

**I.** Zero-weight edges are permitted by its correctness argument.

**II.** Every source-reachable vertex must have a unique shortest path.

**III.** Different vertices can have the same final distance from the source.

**IV.** A zero-weight cycle necessarily makes shortest distances undefined.

A. II and IV  
B. III and IV  
C. I and III  
D. I and II

### Q26. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Two threads always acquire mutexes X and Y in the order X then Y, and release both after finite computation. No other resources or waits exist. Which statement is correct?

A. A cycle of these two threads each holding one of X,Y and waiting for the other is possible.  
B. The common acquisition order excludes a circular wait involving these mutexes.  
C. The order guarantees equal waiting times.  
D. Deadlock freedom implies that neither thread can ever wait.

### Q27. [1 Mark] [NAT]

A memory has eight banks. Word address a maps to bank a modulo8. A program repeatedly accesses addresses3,9,15,21,... with stride6. How many distinct banks are visited before the bank sequence repeats?

**Answer format:** Integer.

### Q28. [1 Mark] [NAT]

A=LU, where L is unit lower triangular and U is upper triangular with diagonal entries2,−3,4. No row permutation is involved. What is det(A)?

**Answer format:** Integer.

### Q29. [1 Mark] [NAT]

For Boolean variables a,b,c, let f(a,b,c)=(a AND b) XOR ((NOT a) AND c). For how many assignments of(b,c) does flipping a change f, regardless of a's initial value?

**Answer format:** Integer.

### Q30. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Shared integers x,y start at zero. Thread A performs `x=1; rA=y;` and thread B performs `y=1; rB=x;`. Every displayed read/write is atomic, each thread's order is preserved, and all operations are sequentially consistent. Which final pairs (rA,rB) are possible?

A. (0,1)  
B. (0,0)  
C. (1,0)  
D. (1,1)

### Q31. [1 Mark] [MSQ]

Given an arbitrary Turing machine M over{0,1}, consider whether it accepts at least one word of length at most3. Which statements are correct?

A. Dovetailing simulations on the finitely many candidate words recognizes YES instances.
B. The finite number of candidate words alone makes this property decidable for arbitrary M.
C. Its negation is also recognizable for arbitrary M.
D. If M is promised to halt on every input, sequentially testing all candidates decides the property under that promise.

### Q32. [1 Mark] [NAT]

Table T(g,v) contains (A,2),(A,NULL),(B,5),(B,7). How many groups remain after `GROUP BY g HAVING COUNT(v)=2`?

**Answer format:** Integer.

### Q33. [1 Mark] [NAT]

Evaluate the definite integral from0 to1 of x/[x²+(1−x)²] with respect to x.

**Answer format:** Decimal rounded to four places.

### Q34. [1 Mark] [NAT]

A dataset has population mean4 and variance9. Each observation x is replaced by y=10−2x. What is E[Y²], interpreting E as the empirical population average?

**Answer format:** Exact number.

### Q35. [1 Mark] [NAT]

An NFA has states s,a,b,c, start state s, and only c accepting. Its transitions are s —ε→ a, a —ε→ b, b —0→ b, b —1→ c, and c —1→ c. There are no other transitions. How many strings of length three are accepted?

**Answer format:** Integer.

### Q36. [2 Marks] [NAT]

An IPv4 datagram has total length 2020 bytes, including a 20-byte header. It crosses a link with MTU 820 bytes. Routers use 20-byte headers for all fragments and maximize the data in each fragment subject to IPv4 alignment rules. What is the fragment-offset field of the last fragment, in its encoded eight-byte units?

**Answer format:** Integer.

### Q37. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A bounded buffer has capacity2 and is initially empty. A semaphore empty starts at2, full at0, and mutex at1. A consumer mistakenly executes wait(mutex), then wait(full), and retains mutex while blocked. A producer executes wait(empty), then wait(mutex) before inserting. Which statements are correct if the consumer runs first?

A. The consumer can block while holding mutex.  
B. The producer can then block on mutex while unable to insert the item that would release the consumer.  
C. Increasing the buffer capacity alone fixes this ordering bug for an initially empty buffer.  
D. Having the consumer wait(full) before wait(mutex) avoids this particular hold-and-wait cycle.

### Q38. [2 Marks] [NAT]

A B+ tree stores at most three keys in each leaf and at most three child pointers in each internal node. Its root initially has separator keys [20,40] and these three leaves, from left to right:

```text
[5,10,15]   [20,25,30]   [40,45,50]
```

Every separator is the smallest key in its right child subtree. Insert 35 and then 55. A leaf overflowing to four keys splits into two leaves with two keys each. An internal node overflowing to four children splits into two nodes with two children each; the boundary separator moves to its parent. Splitting the root creates a new root. Existing nodes are reused as one of the split halves. How many nodes, including the root and all leaves, exist after both insertions?

**Answer format:** Numeric value; integer.

### Q39. [2 Marks] [NAT]

A uniformly random permutation of {1,2,3,4,5} is chosen. Given that 1 is not fixed, what is the probability that the permutation has exactly one fixed point?

**Answer format:** Exact finite decimal.

### Q40. [2 Marks] [NAT]

A simple graph consists of two vertex-disjoint triangles, with one additional edge joining one vertex of the first triangle to one vertex of the second. How many proper colorings using three labeled colors does the graph have?

**Answer format:** Exact integer.

### Q41. [2 Marks] [NAT]

Table T(x) contains the multiset {1,1,2,3}. A query self-joins two aliases of T on `L.x < R.x` and returns all matching pairs without DISTINCT. How many rows does it return?

**Answer format:** Integer.

### Q42. [2 Marks] [NAT]

A processor services eight independent cache misses. Each miss takes100 cycles from issue to completion. It can issue at most one miss per cycle and have at most four outstanding misses. A slot freed by a completion can be reused in that same cycle. All misses are ready initially and are issued as early as permitted, starting in cycle0. In what cycle does the last miss complete?

**Answer format:** Integer.

### Q43. [2 Marks] [NAT]

A byte-addressed memory contains 64 KiB and is built from chips storing 8K words of four bits each. Chips are arranged so one addressed byte is transferred at once. How many chips are needed in total?

**Answer format:** Integer.

### Q44. [2 Marks] [MSQ]

Consider these C declarations inside a function. No operation shown overflows.

```c
int a[3] = {2,4,6};
int *p = a + 3;
```

Which subsequent expressions have defined behavior?

A. p - a
B. *(p - 1)
C. *p
D. p == a + 3

### Q45. [2 Marks] [MSQ]

Records have fields (department,score,id). A stable sorting routine is available. The desired order is department ascending, then score descending, preserving original order for records tied on both fields. Which procedures always achieve that order?

A. Stable sort by score descending, then stable sort by department ascending.
B. Stable sort by department ascending, then stable sort by score descending.
C. One stable sort using the lexicographic key (department,negative score).
D. First reverse the entire input, then use procedure A.

### Q46. [2 Marks] [NAT]

Binary words of length six containing exactly three ones are considered equivalent when one is a cyclic rotation of the other. Reflections are not identified. Count the equivalence classes whose words have least rotational period exactly six; words invariant under a smaller positive rotation are excluded.

**Answer format:** Integer.

### Q47. [2 Marks] [NAT]

Functions on nonnegative integers satisfy f(0)=1, g(0)=0 and, for n≥1, f(n)=f(n−1)+g(n−1), g(n)=f(n−1)−g(n−1). What is f(10)?

**Answer format:** Integer.

### Q48. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For the grammar S→SS | a, consider the string aaaaa. Parse trees are ordered, and derivations are finite. Which statements are correct?

A. It has exactly 14 parse trees.  
B. It has exactly 14 leftmost derivations.  
C. Counting leftmost and rightmost derivations produces 28 different parse trees.  
D. The language generated by the grammar is regular.

### Q49. [2 Marks] [MSQ]

A nondeterministic PDA recognizes even-length palindromes over {a,b} by pushing an initial segment, guessing its midpoint using an epsilon transition, and then matching and popping the remaining symbols; it accepts only after consuming all input and returning to its bottom marker. Which statements are correct?

A. Any accepting computation on abba must guess the midpoint after two input symbols.
B. Guessing the midpoint after one input symbol can accept abba by ignoring a mismatched stack symbol.
C. The word abab is rejected on every computation.
D. An incorrect midpoint guess must make every computation on an actual palindrome reject.

### Q50. [2 Marks] [NAT]

An open-addressed hash table has12 slots numbered0–11. For a particular key the probe sequence is (2+8i) modulo12 for i=0,1,2,... . All slots that this sequence can reach are occupied; all other slots are empty. If the secondary step is replaced by5 while the starting slot remains2, how many probes, including the initial probe, are needed to reach the first empty slot?

**Answer format:** Integer.

### Q51. [2 Marks] [MSQ]

Consider the augmented grammar with start S and productions

```text
S → A a | b A c | d c | b d a
A → d
```

Consider the parser state reached after shifting the viable prefix bd. Which statements are correct?

A. The LR(0) item set contains S→bd·a and A→d·.
B. An SLR(1) table has a shift/reduce conflict on a in this state.
C. The completed A→d· item in the corresponding canonical LR(1) state has lookahead c, so it does not cause a conflict on a.
D. FOLLOW(A) contains only c.

### Q52. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Relation R(A,B,C) contains exactly (1,x,p),(1,y,q),(2,x,p),(2,y,r). Which functional dependencies hold on this relation instance?

**Candidates**

**I.** A→C

**II.** AB→C

**III.** C→A

**IV.** C→B

A. II and IV  
B. III and IV  
C. I and II  
D. I and III

### Q53. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Two processes use a shared counting semaphore initialized to 0. P executes `signal(s); signal(s);`, while Q executes `wait(s); wait(s); print();`. There are no other accesses. Which statements are correct?

**Candidates**

**I.** If both processes are eventually scheduled and semaphore operations are correct, Q can eventually print.

**II.** The two signals collapse into a single remembered event.

**III.** Q may block on its first wait depending on scheduling.

**IV.** Q must print before P executes its second signal.

A. III and IV  
B. I and III  
C. I and II  
D. I and IV

### Q54. [2 Marks] [NAT]

A C array `int a[2][3]={{1,2,3},{4,5,6}};` is followed by `int (*p)[3]=a;`. Evaluate `*(*(p+1)+2) + (*p)[1]`.

**Answer format:** Integer.

### Q55. [2 Marks] [NAT]

A compiler translates references to a contiguous three-dimensional array with index ranges −1..1, 2..5, and 0..2, all inclusive. Elements occupy four bytes. Storage is row-major, so the final index varies fastest. The base address denotes element A[−1][2][0]. What byte offset from the base does the compiler generate for A[0][4][1]?

**Answer format:** Integer.

### Q56. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

What is the asymptotic number of executions of work()?

```text
for i = 1 to n:
    j = 1
    while j <= i:
        for k = 1 to j:
            work()
        j = 2*j
```

A. Θ(n log n)  
B. Θ(n²)  
C. Θ(n² log n)  
D. Θ(log² n)

### Q57. [2 Marks] [NAT]

A synchronous three-bit shift register has next-state equations q2′=q1, q1′=q0, q0′=q2 XOR q0. Starting in state q2q1q0=001, after how many clock edges does it first return to 001?

**Answer format:** Integer.

### Q58. [2 Marks] [NAT]

Round-robin scheduling has quantum2, zero overhead, and a ready queue initially[A,B,C]. All arrive at0, with CPU bursts A=5,B=3,C=1. A process with remaining work joins the queue tail after its quantum. What is the mean turnaround time?

**Answer format:** Decimal rounded to four places.

### Q59. [2 Marks] [NAT]

For the grammar S→ABc, A→a | ε, B→AD | b, D→d | ε, with start S, how many distinct terminal symbols belong to FOLLOW(A)? The end marker is not a terminal symbol.

**Answer format:** Integer.

### Q60. [2 Marks] [NAT]

A sorted data file occupies64 blocks. A sparse primary index has one entry per data block and occupies4 blocks, with16 entries per index block. A second index level has one entry per first-level block and fits in one block. No blocks are cached. A successful point lookup follows the root, one first-level index block, then its data block. Compared with binary search directly on the64 data blocks, whose worst-case successful lookup requires7 block reads, how many block reads are saved in that worst-case comparison?

**Answer format:** Exact integer.

### Q61. [2 Marks] [MSQ]

Over alphabet {a,b,c}, define

```text
L = { a^i b^j c^k : i,j,k >= 0 and (i=j or j=k) }
R = { a^i b^j c^k : i,j,k >= 0 and j<=2 }
S = { a^n b^m c^n : n,m >= 0 }.
```

All exponents are integers, and L minus R denotes set difference. Which statements are correct?

A. L intersect R is regular.  
B. L minus R is regular.  
C. L minus R is context-free.  
D. L intersect S is context-free.

### Q62. [2 Marks] [NAT]

A device transfers 12,000 bytes in one second. With interrupt-driven I/O, each byte causes an interrupt costing 80 CPU cycles. With DMA, one completion interrupt occurs per 1,000-byte block at a cost of 120 CPU cycles, plus 30 setup cycles per block; ignore all other CPU work and bus stalls. How many CPU cycles are saved by DMA during that second?

**Answer format:** Integer.

### Q63. [2 Marks] [NAT]

Let an count length-n strings over {0,1,2} in which every run of consecutive2s has even length; runs of0s and1s are unrestricted. The empty string is allowed. What is a4?

**Answer format:** Exact integer.

### Q64. [2 Marks] [NAT]

An organization owns192.0.2.0/24. The ranges192.0.2.0/26 and192.0.2.192/26 are reserved and cannot be included in a free-space advertisement. What is the minimum number of CIDR prefixes whose union is exactly the remaining addresses?

**Answer format:** Integer.

### Q65. [2 Marks] [NAT]

Disk cylinders range from0 to199. The head is at50 and moves upward. Pending requests are at20,60,90. Under SCAN, service all requests encountered, continue to199 before reversing if requests remain below, and stop as soon as the last pending request is served. Under LOOK, reverse at the largest pending request instead. How many more cylinders does SCAN travel than LOOK for this batch?

**Answer format:** Exact integer.

---

## ANSWER KEY — MOCK TEST 064

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | NAT | 1 | 3.2 |
| 2 | NAT | 1 | 2 |
| 3 | MCQ | 1 | C |
| 4 | NAT | 1 | 0.2000 (accepted range 0.19995–0.20005) |
| 5 | MSQ | 1 | A, C, D |
| 6 | NAT | 2 | 3.23 (range 3.225–3.235) |
| 7 | MSQ | 2 | A, B, D |
| 8 | NAT | 2 | 5 |
| 9 | NAT | 2 | 31 |
| 10 | NAT | 2 | 0.5 |
| 11 | NAT | 1 | 21 |
| 12 | MSQ | 1 | B, D |
| 13 | NAT | 1 | 4 |
| 14 | NAT | 1 | -0.1667 (range -0.16675–-0.16665) |
| 15 | MSQ | 1 | B, D |
| 16 | MCQ | 1 | C |
| 17 | MCQ | 1 | A |
| 18 | NAT | 1 | 1 (exact) |
| 19 | MSQ | 1 | B, C, D |
| 20 | NAT | 1 | 2 |
| 21 | MCQ | 1 | B |
| 22 | MSQ | 1 | A, B, C |
| 23 | NAT | 1 | 3 |
| 24 | NAT | 1 | 7 |
| 25 | MCQ | 1 | C |
| 26 | MSQ | 1 | A, C, D |
| 27 | NAT | 1 | 4 |
| 28 | NAT | 1 | -24 |
| 29 | NAT | 1 | 2 |
| 30 | MCQ | 1 | B |
| 31 | MSQ | 1 | A, D |
| 32 | NAT | 1 | 1 |
| 33 | NAT | 1 | 0.7854 (accepted range 0.78535–0.78545) |
| 34 | NAT | 1 | 40 |
| 35 | NAT | 1 | 3 |
| 36 | NAT | 2 | 200 |
| 37 | MCQ | 2 | C |
| 38 | NAT | 2 | 8 (exact) |
| 39 | NAT | 2 | 0.375 |
| 40 | NAT | 2 | 24 |
| 41 | NAT | 2 | 5 |
| 42 | NAT | 2 | 203 |
| 43 | NAT | 2 | 16 |
| 44 | MSQ | 2 | A, B, D |
| 45 | MSQ | 2 | A, C |
| 46 | NAT | 2 | 3 |
| 47 | NAT | 2 | 32 (exact) |
| 48 | MCQ | 2 | C |
| 49 | MSQ | 2 | A, C |
| 50 | NAT | 2 | 2 |
| 51 | MSQ | 2 | A, B, C |
| 52 | MCQ | 2 | A |
| 53 | MCQ | 2 | B |
| 54 | NAT | 2 | 8 |
| 55 | NAT | 2 | 76 |
| 56 | MSQ | 2 | A, C, D |
| 57 | NAT | 2 | 7 |
| 58 | NAT | 2 | 7.3333 (accepted range 7.33325–7.33335) |
| 59 | NAT | 2 | 4 |
| 60 | NAT | 2 | 4 |
| 61 | MSQ | 2 | A, C |
| 62 | NAT | 2 | 958200 |
| 63 | NAT | 2 | 29 |
| 64 | NAT | 2 | 2 |
| 65 | NAT | 2 | 218 |
