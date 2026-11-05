# GATE CS 2027 — Full-Length Mock Test 069

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

### Q1. [1 Mark] [MCQ]

Four events are A, data collection; B, instrument calibration; C, result certification; D, publication. The only constraints are A before C, B before C and C before D. Which lists exactly the possible chronological orders?

A. ABCD only
B. ABCD and BACD
C. ACBD and BCAD
D. All 24 permutations

### Q2. [1 Mark] [NAT]

Two inlet pipes, working alone, fill an empty tank in 6 hours and 9 hours. With both inlets and a leak open, an initially empty tank fills in 4 hours. All rates are constant. How many hours would the leak alone take to empty a full tank?

**Answer format:** Integer hours.

### Q3. [1 Mark] [MCQ]

“The proposed change is reversible: the previous configuration can be restored.” Which meaning of reversible applies?

A. Impossible to undo.
B. Capable of being undone.
C. Required to happen twice.
D. Unrelated to the previous configuration.

### Q4. [1 Mark] [NAT]

Find the positive real x satisfying 3^(x+1)=27×9^(x−2).

**Answer format:** Integer.

### Q5. [1 Mark] [MSQ]

For a statement P(n) about integers n≥2, a proof establishes P(2) and P(k) implies P(k+2) for every integer k≥2. Which conclusions follow?

A. P(n) holds for every even integer n≥2.
B. These facts alone prove P(3).
C. Adding a proof of P(3) would establish P(n) for every integer n≥2.
D. The step from k to k+2 supplies the missing odd base case automatically.

### Q6. [2 Marks] [NAT]

A solid cube is assembled from 27 unit cubes in a 3×3×3 arrangement. Remove the central unit cube of each of its six faces, leaving all other unit cubes in place. Count every face of a remaining unit cube that is adjacent to empty space, including space within the resulting openings. What is the total exposed area in square units?

**Answer format:** Integer.

### Q7. [2 Marks] [NAT]

A sequence obeys a(n+2)=u·a(n+1)+v·a(n) for fixed real constants u,v. Its first four terms are2,3,8,19. What is the fifth term?

**Answer format:** Exact number.

### Q8. [2 Marks] [NAT]

A rectangular garden is 40 m by 30 m. A path of uniform width runs just inside all four boundaries, leaving a rectangular planted region. If the path occupies 264 m², find its width, which is less than 15 m.

**Answer format:** Integer metres.

### Q9. [2 Marks] [MCQ]

Choose the revision that is grammatically correct and preserves both intended meanings: Mira did not leave earlier, so she missed the train; Mira, not the meeting, reached the office late.

Original: “If Mira had left earlier, she will catch the train. Having reached the office late, the meeting had already begun.”

A. If Mira left earlier, she will catch the train. Having reached the office late, the meeting began.  
B. If Mira had left earlier, she would have caught the train. When Mira reached the office late, the meeting had already begun.  
C. If Mira had left earlier, she would catch the train. Having reached the office late, the meeting had begun.  
D. If Mira would have left earlier, she caught the train. When the meeting reached the office late, Mira had begun.

### Q10. [2 Marks] [NAT]

A contractor buys60 units from supplier A at50 rupees each and40 units from B at75 rupees each. In the next order, both suppliers raise their prices by20%, but the contractor still buys100 units and spends exactly the original total amount. How many units must now be bought from A?

**Answer format:** Integer.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MSQ]

Functions f:A→B and g:B→A satisfy g composed with f=identity on A. No finiteness assumption is made. Which statements necessarily hold?

A. f is injective.
B. f is surjective onto B.
C. g is surjective onto A.
D. f composed with g=identity on B.

### Q12. [1 Mark] [NAT]

A real4×4 matrix P satisfies P²=P and trace(P)=3. What is the dimension of the null space of I−P?

**Answer format:** Integer.

### Q13. [1 Mark] [MCQ]

Consider `p=a*b; a=read_input(); q=a*b;`. Scalars do not alias, but read_input may return any value. Why is replacing the final a*b by p generally invalid?

A. Multiplication is never eligible for common-subexpression elimination.
B. Operand a may have changed since p was computed.
C. b must have changed.
D. p must be uninitialized.

### Q14. [1 Mark] [NAT]

A synchronous modulo-5 counter uses three flip-flops. Legal states 000,001,010,011,100 advance cyclically in that order; each illegal state goes to 000 on the next edge. From initial state 111, what unsigned state value appears after seven clock edges?

**Answer format:** Exact integer.

### Q15. [1 Mark] [NAT]

A differentiable function f on[0,2] has f(0)=1 and f(2)=7, and f'(x)≤3 everywhere on(0,2). What is f(1)?

**Answer format:** Exact integer.

### Q16. [1 Mark] [MSQ]

Two virtual pages of one process intentionally map to the same physical frame. Both mappings are writable and there is no copy-on-write mechanism. Which statements are correct?

A. A write through one mapping can be read through the other at the corresponding offset.
B. The virtual page numbers must be equal.
C. The mappings can have different virtual addresses while sharing storage.
D. Each write necessarily allocates a fresh physical frame.

### Q17. [1 Mark] [NAT]

A recovery system redoes committed updates and undoes uncommitted updates using durable before-and-after log records. Initially x=5,y=7. T1 logs x:5→8 and commits, but its updated data page has not been flushed. T2 logs y:7→9 and its data page is flushed, but T2 has not committed when a crash occurs. All mentioned log records and T1's commit record are durable. What is x+y after recovery?

**Answer format:** Integer.

### Q18. [1 Mark] [NAT]

In the additive group of integers modulo12, how many distinct elements can be obtained as 4m+6n modulo12 with nonnegative integers m,n?

**Answer format:** Integer.

### Q19. [1 Mark] [MSQ]

An undirected triangle has edges AB of weight1, BC of weight2 and AC of weight3. Each weight w is replaced by w−2. Which statements are correct?

A. The set of minimum spanning trees is unchanged.
B. The set of shortest simple A–C paths is unchanged.
C. The minimum spanning-tree weight decreases by4.
D. Subtracting the same constant always preserves comparisons between paths having different numbers of edges.

### Q20. [1 Mark] [NAT]

Evaluate the limit as x→0 of (eˣ−1−x)/x².

**Answer format:** Exact finite decimal.

### Q21. [1 Mark] [NAT]

For grammar S→S | a, how many distinct finite parse trees generate a and contain at most three applications of S→S?

**Answer format:** Integer.

### Q22. [1 Mark] [MSQ]

A recursive depth-first search on a directed graph colors undiscovered vertices white, vertices on its active recursion stack gray, and finished vertices black. A currently explored edge is u→v. Which statements hold?

A. If v is gray, the graph contains a directed cycle.
B. If v is black, u→v necessarily belongs to a directed cycle.
C. If no edge to a gray vertex is encountered during a full DFS forest, the graph is acyclic.
D. If v is white, v must be an ancestor of u in the current DFS tree.

### Q23. [1 Mark] [NAT]

Assume conventional C semantics and representable integer values. What is the final value of a[1]?

```c
int a[3] = {1,2,3};
int *p = a;
int x = *p++;
*p += x;
```

**Answer format:** Integer.

### Q24. [1 Mark] [NAT]

An unsigned fixed-point format has three integer bits and two fractional bits, with no padding. What is its largest representable value?

**Answer format:** Exact decimal.

### Q25. [1 Mark] [MSQ]

Consider the following code. The return is the only program exit and has no implicit use of other variables.

```text
x = 1;
y = x + 2;
x = 4;
return y;
```

Which statements about backward liveness hold?

A. x is live immediately after x=1.
B. The value assigned by x=4 is live immediately after that assignment.
C. y is live immediately before x=4.
D. y is live immediately before y=x+2.

### Q26. [1 Mark] [NAT]

A two-bit synchronous counter uses transitions00→01→10→00 and11→00. What is the maximum number of clock edges needed to enter the repeating three-state cycle from an arbitrary initial state?

**Answer format:** Integer; entering at time0 requires zero edges.

### Q27. [1 Mark] [NAT]

An inode has one direct pointer and one pointer to a single-indirect block. Blocks contain 1024 bytes and pointers contain 4 bytes. A previously empty file is extended by writing one byte at byte offset 3072, with offsets starting at zero. The file system supports holes and allocates only necessary data and indirect blocks. Excluding the inode, how many blocks are newly allocated?

**Answer format:** Exact integer.

### Q28. [1 Mark] [NAT]

A memory system must contain1024 words of16 bits each. Available chips each contain256 words of8 bits. How many chips are required, assuming ordinary depth and width expansion without redundancy?

**Answer format:** Integer.

### Q29. [1 Mark] [MSQ]

Which statements about socket receive results are correct? Calls request a positive number of bytes and encounter no errors unless explicitly stated.

A. On a connected TCP stream, returning zero after buffered input is exhausted indicates an orderly end of incoming data.
B. Each successful TCP receive must return exactly one complete application message.
C. Receiving a zero-length UDP datagram can return zero without implying that the sender has closed a connection.
D. TCP preserves the sender's write-call boundaries as receive-call boundaries.

### Q30. [1 Mark] [NAT]

A schedule has operations r1(x),r2(x),w1(x),w2(x), followed by commits. How many directed edges are in its precedence graph, counting each ordered pair of distinct transactions at most once?

**Answer format:** Integer.

### Q31. [1 Mark] [MCQ]

A distance-vector router X has links of costs 2 and 5 to neighbors Y and Z. Before processing updates, their advertised distances to D are 4 and 1, respectively. Only Y then advertises distance 9. Using the latest advertisement from each neighbor and no other route to D, what should X advertise?

A. 4
B. 6
C. 11
D. 14

### Q32. [1 Mark] [MSQ]

A recognizer for a language may loop on some nonmembers. Which statements are correct?

A. If it accepts an input, that input is a member.
B. If it has not halted after a fixed finite number of steps, the input must be a nonmember.
C. A decider must halt on every input.
D. Every recognizer is automatically a decider.

### Q33. [1 Mark] [NAT]

A circular singly linked list has a sentinel H and three data nodes A,B,C, with links H→A→B→C→H. Execute `B.next = B.next.next`, without freeing any node. How many data nodes remain reachable by following next from H before returning to H?

**Answer format:** Integer.

### Q34. [1 Mark] [MSQ]

A programming language specifies that every evaluation of a volatile memory read is observable, even if the returned values happen to be equal. For two successive expressions x=read_volatile(p) and y=read_volatile(p), which statements are correct?

A. Equal returned values alone justify replacing the second read by y=x.
B. Such replacement removes an observable operation.
C. Ordinary expression-value equality is insufficient for this optimization.
D. Volatile reads are guaranteed never to return equal values.

### Q35. [1 Mark] [NAT]

A two-level memory system checks a cache in 2 ns. On a miss, it then accesses main memory in 50 ns; the cache check and memory access do not overlap. A measured average access time is 7 ns. What is the cache hit probability?

**Answer format:** Exact decimal.

### Q36. [2 Marks] [NAT]

A two-way cache has two sets, initially empty, with LRU replacement. The memory-block reference sequence is 0,2,4,0,2,4. Compare mapping I, set index equal to block-address bit 0, with mapping II, set index equal to bit 0 XOR bit 1. Block bits are numbered from zero at the least significant end. How many fewer misses occur with mapping II?

**Answer format:** Integer.

### Q37. [2 Marks] [NAT]

A one-based min-heap array is[1,10,2,11,12,3,4]. Delete the node at index4 by replacing it with the last entry and removing the last slot. Restore the heap using the necessary upward or downward exchanges. What value ends at index2?

**Answer format:** Integer.

### Q38. [2 Marks] [NAT]

A divide-and-conquer algorithm splits a problem of size16 into two equal children until singleton leaves. Each internal node allocates a temporary buffer equal to its subproblem size, frees it before returning, and retains its own buffer while processing its two children sequentially. Leaf nodes allocate no buffer. What is the maximum simultaneous buffer allocation, in units?

**Answer format:** Integer.

### Q39. [2 Marks] [NAT]

A 2 GHz processor executes 10⁹ instructions with average CPI 1.2. A compiler transformation reduces instruction count by 20% but increases average CPI to 1.4. What is the execution-time reduction in milliseconds at the same clock frequency?

**Answer format:** Integer.

### Q40. [2 Marks] [MSQ]

A bounded-buffer implementation starts empty with semaphores empty=N, full=0, mutex=1, where N>0. The producer executes wait(empty),wait(mutex),insert,signal(mutex),signal(full). The consumer incorrectly executes wait(mutex),wait(full),remove,signal(empty),signal(mutex). Which statements are correct?

A. If the consumer acquires mutex first, it can block on full while preventing the producer from acquiring mutex.
B. The given order is guaranteed deadlock-free because every semaphore is eventually signalled in the source code.
C. Moving the consumer's wait(full) before wait(mutex), leaving its remaining operations in order, removes this particular deadlocking acquisition order.
D. Initializing full to N correctly represents the stated initially empty buffer.

### Q41. [2 Marks] [NAT]

Partition this three-address code into maximal basic blocks using the usual leader rules. Count distinct directed edges between the resulting blocks, including both outcomes of conditional branches. There are no exceptional-control-flow edges.

```text
1: i = 0
2: if i >= n goto 9
3: if a[i] < 0 goto 7
4: s = s + a[i]
5: i = i + 1
6: goto 2
7: i = i + 2
8: goto 2
9: return s
```

**Answer format:** Integer.

### Q42. [2 Marks] [NAT]

For a matrix A, pivoted elimination gives PA=LU, where P swaps rows1 and2,

```text
L=[1 0; 2 1],    U=[1 3; 0 2].
```

Solve Ax=b for b=(7,2)ᵀ. What is x1?

**Answer format:** Exact decimal.

### Q43. [2 Marks] [NAT]

A ternary relationship R(A,B,C) has exactly the four tuples (0,0,0),(0,1,1),(1,0,1),(1,1,0). It is replaced by its three binary projections on AB, BC and AC. Under set semantics, naturally join these projections on their common attributes. How many tuples in the join were not in the original relationship?

**Answer format:** Integer.

### Q44. [2 Marks] [NAT]

For Boolean variables a,b,c, how many assignments make a XOR b XOR c differ from(a OR b OR c)?

**Answer format:** Integer.

### Q45. [2 Marks] [MSQ]

Let L={ww : w∈{a,b}*}, a non-context-free language. Define the homomorphism h by h(a)=h(b)=0. Which statements are correct?

A. h(L) consists of all even-length words over {0}.
B. h(L) is regular.
C. Non-context-freeness of L implies non-context-freeness of h(L).
D. The word 000 belongs to h(L).

### Q46. [2 Marks] [NAT]

A sender estimates round-trip time using S←(3/4)S+(1/4)R and then D←(1/2)D+(1/2)|R−S_old|, where S_old is the estimate before that sample's update. Its timeout is S+4D. Initially S=100ms and D=10ms. Two successive unambiguous samples are140ms and100ms. What timeout results after both updates?

**Answer format:** Exact milliseconds.

### Q47. [2 Marks] [NAT]

A systematic CRC encoder uses generator polynomial x³+x+1, represented by 1011. For data bits 1101, append three zeros and divide by 1011 over GF(2). Interpret the three-bit remainder as an unsigned integer. What is that integer?

**Answer format:** Integer.

### Q48. [2 Marks] [MSQ]

A proposed proof that {a^n b^n : n≥0} is not regular takes pumping length p and word a^p b^p. Which statements correctly describe the regular-language pumping lemma argument?

A. Every permitted decomposition with |xy|≤p and |y|>0 has y consisting only of a's.
B. Choosing the one convenient decomposition x=ε,y=a is sufficient by itself.
C. For every permitted decomposition, pumping y zero times produces a word outside the language.
D. The pumping length may be chosen after seeing an arbitrary decomposition of an arbitrarily short word.

### Q49. [2 Marks] [NAT]

An eight-bit unsigned multiplier retains only the low eight product bits. For a fixed odd input a=13, how many inputs b in {0,…,255} produce output 0? Count b values, not ordered pairs of inputs.

**Answer format:** Integer.

### Q50. [2 Marks] [MSQ]

For grammar S→AB, A→aA | ε, B→bBc | ε, with start symbol S and end marker $, which statements are correct?

A. The grammar is LL(1).
B. c belongs to FOLLOW(A).
C. FOLLOW(B)={c,$}.
D. The production A→ε must be selected on lookahead a in an LL(1) table.

### Q51. [2 Marks] [NAT]

A six-bit register represents six valid one-hot states. A recovery circuit maps a word containing at least one 1 to the one-hot word retaining only its highest-index 1 (indices 0 through 5). It maps the all-zero word to the state with bit 0 set. Each of the 64 possible input words is equally likely. What is the probability that the recovered state has index at least 4?

**Answer format:** Exact finite decimal.

### Q52. [2 Marks] [MSQ]

In a tabular Boolean-minimization procedure, two product cubes may be combined only if their don't-care positions are identical and they differ in exactly one remaining bit. Here '-' denotes a don't-care position. Which pairs can be combined under that rule?

A. 0-01 and0-11.
B. 00-1 and0-01.
C. -100 and-101.
D. 0101 and1010.

### Q53. [2 Marks] [MSQ]

A real 3×3 matrix A satisfies A³=0 and A²≠0. Which statements must hold?

A. rank(A)=2.
B. rank(A²)=1.
C. A has an eigenvalue equal to 1.
D. (I−A)⁻¹=I+A+A².

### Q54. [2 Marks] [NAT]

A single process runs the following pseudocode. Every fork succeeds; the child receives return value zero and the parent a positive value. Each process prints once after the loop.

```text
for i = 0,1,2:
    if fork() == 0:
        break
print(i)
```

A process completing all iterations has i=3 at print time. What is the sum of all printed integers, regardless of output order?

**Answer format:** Integer.

### Q55. [2 Marks] [MCQ]

Two internal TCP clients connect to the same external server through a translator sharing one public address. The translator assigns different public source ports. Which information is essential for routing a returning server segment to the correct internal connection?

A. Only the external server's destination port, ignoring the translated port.
B. A translation mapping that includes the public-side connection endpoint information and its corresponding internal endpoint.
C. Only the Ethernet broadcast address.
D. Only the length of the TCP payload.

### Q56. [2 Marks] [MSQ]

Under set semantics let R(A,B)={(1,x),(2,y)}, S(B) be empty, and U(A)={1,2,3}. Standard relational division R÷S uses candidate A values from π_A(R). Separately, a query selects each A in U for which no B in S lacks a matching tuple in R. Which statements are true?

A. R÷S returns {1,2}.
B. R÷S returns {1,2,3}.
C. The separately described query returns {1,2,3}.
D. Both results must be empty because S is empty.

### Q57. [2 Marks] [NAT]

A directed multigraph has adjacency-count matrix with rows (1,2,0), (0,0,3), (1,0,0). Entries count distinct parallel edges, and walks distinguish different edge choices. How many length-three walks start and end at vertex 1?

**Answer format:** Integer.

### Q58. [2 Marks] [NAT]

Two processes communicate over two initially empty FIFO channels of capacity one message each. Sending blocks when the destination channel is full; receiving blocks when it is empty. P executes send(a),send(b),receive(x), while Q executes send(c),receive(y),receive(z). P's sends go to Q and Q's send goes to P. Both run fairly, and local computation takes no time. How many messages can remain queued when both processes finish?

**Answer format:** Exact integer.

### Q59. [2 Marks] [MSQ]

Let u,v be nonzero real column vectors of length3 satisfying vᵀu=1, and let A=I−uvᵀ. Which statements are correct?

A. A is invertible.
B. The nullspace of A is precisely the span of u.
C. Ax=b is solvable exactly when vᵀb=0.
D. A²=A.

### Q60. [2 Marks] [MSQ]

Random variables X∈{1,2} and Y∈{0,1} have joint probabilities P(X=x,Y=y)=c(x+y), for a normalizing constant c. Which statements are correct?

A. c=1/8.
B. X and Y are independent.
C. P(Y=1)=5/8.
D. E[X|Y=0]=5/3.

### Q61. [2 Marks] [NAT]

A syntax-directed translation uses the grammar E→E−T | T and T→digit. The semantic rules are E→E1−T: E.val=E1.val−T.val; E→T: E.val=T.val; T→digit: T.val=the digit's value. For the input9−4−2, a second implementation incorrectly rewrites the grammar to right recursion E→T−E | T and uses ordinary subtraction of the child values. What is the correct implementation's value minus the second implementation's value?

**Answer format:** Integer, possibly negative.

### Q62. [2 Marks] [NAT]

CPU instructions each take one bus-available cycle. Beginning at cycle 1, a DMA device steals every fourth cycle (4,8,12,...) until it has completed 64 one-cycle transfers. The CPU must execute 100 instructions and cannot progress during stolen cycles. At the end of which cycle does its 100th instruction finish?

**Answer format:** Integer.

### Q63. [2 Marks] [MSQ]

Relations R(x),S(x) are finite but the underlying value domain is infinite. Which formulas, with x free, always return a finite set of values?

A. R(x) AND NOT S(x)
B. NOT R(x)
C. R(x) OR S(x)
D. NOT R(x) AND NOT S(x)

### Q64. [2 Marks] [NAT]

What does this conforming C program print?

```c
#include <stdio.h>
void change(int **q, int *r) {
    **q += 2;
    *q = r;
    **q += 3;
}
int main(void) {
    int a = 4, b = 7;
    int *p = &a;
    change(&p, &b);
    printf("%d\n", a + b + *p);
    return 0;
}
```

**Answer format:** Integer.

### Q65. [2 Marks] [NAT]

An initially empty five-stage IF-ID-EX-MEM-WB pipeline issues at most one instruction per cycle. Without stalls, N retired instructions take N+4 cycles. Full forwarding leaves exactly one stall cycle for an immediately dependent load-use pair. A taken branch incurs exactly two additional cycles, with no other penalties. A path retires, in order, a load, an ALU instruction using that load, a taken branch depending on that ALU result, and a target ALU instruction. ALU-to-branch forwarding avoids any additional data stall. How many cycles elapse through the final instruction's WB?

**Answer format:** Exact integer.

---

## ANSWER KEY — MOCK TEST 069

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | B |
| 2 | NAT | 1 | 36 |
| 3 | MCQ | 1 | B |
| 4 | NAT | 1 | 2 |
| 5 | MSQ | 1 | A, C |
| 6 | NAT | 2 | 78 (exact) |
| 7 | NAT | 2 | 46 |
| 8 | NAT | 2 | 2 |
| 9 | MCQ | 2 | B |
| 10 | NAT | 2 | 100 |
| 11 | MSQ | 1 | A, C |
| 12 | NAT | 1 | 3 |
| 13 | MCQ | 1 | B |
| 14 | NAT | 1 | 1 |
| 15 | NAT | 1 | 4 |
| 16 | MSQ | 1 | A, C |
| 17 | NAT | 1 | 15 |
| 18 | NAT | 1 | 6 |
| 19 | MSQ | 1 | A, C |
| 20 | NAT | 1 | 0.5 |
| 21 | NAT | 1 | 4 |
| 22 | MSQ | 1 | A, C |
| 23 | NAT | 1 | 3 |
| 24 | NAT | 1 | 7.75 |
| 25 | MSQ | 1 | A, C |
| 26 | NAT | 1 | 1 |
| 27 | NAT | 1 | 2 |
| 28 | NAT | 1 | 8 |
| 29 | MSQ | 1 | A, C |
| 30 | NAT | 1 | 2 |
| 31 | MCQ | 1 | B |
| 32 | MSQ | 1 | A, C |
| 33 | NAT | 1 | 2 |
| 34 | MSQ | 1 | B, C |
| 35 | NAT | 1 | 0.9 |
| 36 | NAT | 2 | 3 |
| 37 | NAT | 2 | 4 |
| 38 | NAT | 2 | 30 |
| 39 | NAT | 2 | 40 |
| 40 | MSQ | 2 | A, C |
| 41 | NAT | 2 | 7 |
| 42 | NAT | 2 | -2.5 |
| 43 | NAT | 2 | 4 |
| 44 | NAT | 2 | 3 |
| 45 | MSQ | 2 | A, B |
| 46 | NAT | 2 | 177.5 |
| 47 | NAT | 2 | 1 |
| 48 | MSQ | 2 | A, C |
| 49 | NAT | 2 | 1 |
| 50 | MSQ | 2 | A, C |
| 51 | NAT | 2 | 0.75 |
| 52 | MSQ | 2 | A, C |
| 53 | MSQ | 2 | A, B, D |
| 54 | NAT | 2 | 6 |
| 55 | MCQ | 2 | B |
| 56 | MSQ | 2 | A, C |
| 57 | NAT | 2 | 7 |
| 58 | NAT | 2 | 0 |
| 59 | MSQ | 2 | B, C, D |
| 60 | MSQ | 2 | A, C, D |
| 61 | NAT | 2 | -4 |
| 62 | NAT | 2 | 133 |
| 63 | MSQ | 2 | A, C |
| 64 | NAT | 2 | 26 |
| 65 | NAT | 2 | 11 |
