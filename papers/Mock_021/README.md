# GATE CS 2027 — Full-Length Mock Test 021

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

Q1–Q5 and Q11–Q35 carry one mark each; all others carry two marks. Each MCQ has exactly one correct option. Incorrect MCQs lose one-third of their assigned marks. MSQs require all correct options, with no partial credit or negative marking. NATs have no negative marking. Unattempted questions score zero. GA carries15 marks, Engineering Mathematics13 and core CS72. Numerical answers are exact unless rounding is specified.

## Section A — General Aptitude

### Q1. [1 Mark] [MCQ]

Arrange these sentences into a coherent account. “This discrepancy” refers to the difference between the two measurements, and “the repair” refers to replacing the defective sensor.

P: A replacement sensor brought the readings into agreement.  
Q: Two instruments measuring the same temperature initially gave different readings.  
R: After the repair, both instruments remained stable during a second trial.  
S: This discrepancy led the technician to identify a defective sensor.

A. Q,S,P,R
B. S,Q,R,P
C. Q,P,R,S
D. P,R,Q,S

### Q2. [1 Mark] [NAT]

A bag contains two red and two blue balls. Two balls are drawn without replacement. The first ball's colour is not revealed. A truthful observer reports only that at least one of the drawn balls is red. What is the probability that both are red? Round to four decimal places.

**Answer format:** Decimal rounded to four places.

### Q3. [1 Mark] [MCQ]

“The committee's endorsement was qualified: it supported the proposal only if its cost was independently audited.” In this sentence, “qualified” most nearly means:

A. Awarded a professional certificate.
B. Expressed subject to a reservation or condition.
C. Withdrawn without explanation.
D. Unconditionally enthusiastic.

### Q4. [1 Mark] [NAT]

For positive numbers x and y, log2(x)+log2(y)=7 and log2(x/y)=3. What is x?

**Answer format:** Exact number.

### Q5. [1 Mark] [MCQ]

For a two-digit number with nonzero unequal digits, operation R reverses the digits and operation S replaces each digit d by 9−d. Which statement holds whenever the intermediate results are interpreted as two-digit strings, allowing a leading zero?

A. R followed by S always equals S followed by R.
B. Applying R twice always produces S's result.
C. Applying S twice always swaps the digits.
D. R followed by S always leaves the original string unchanged.

### Q6. [2 Marks] [NAT]

A solid cube of side3 is assembled from27 unit cubes. The central unit cube of each of the six faces and the unit cube at the centre of the large cube are removed. All remaining unit cubes stay in place. What is the total area of the remaining solid's exposed surfaces, including surfaces inside the resulting passages?

**Answer format:** Integer square units.

### Q7. [2 Marks] [NAT]

A sequence obeys a(n+2)=u·a(n+1)+v·a(n) for fixed real constants u,v. Its first four terms are2,3,8,19. What is the fifth term?

**Answer format:** Exact number.

### Q8. [2 Marks] [NAT]

Two axis-aligned squares each have side4. One occupies [0,4]×[0,4]. The other occupies [t,t+4]×[t,t+4], where0≤t≤4. Their union has area28. What is t?

**Answer format:** Exact number.

### Q9. [2 Marks] [MCQ]

Choose the sentence that clearly states that the engineer inspected the bridge, found cracks, and then recommended closure, without assigning an action to an inappropriate subject.

A. Having inspected the bridge, cracks prompted the engineer to recommend closure.
B. Having inspected the bridge and found cracks, the engineer recommended closure.
C. Having been inspected by the engineer, closure was recommended by cracks.
D. The bridge inspected the engineer, who recommended closure after finding cracks.

### Q10. [2 Marks] [NAT]

A contractor buys60 units from supplier A at50 rupees each and40 units from B at75 rupees each. In the next order, both suppliers raise their prices by20%, but the contractor still buys100 units and spends exactly the original total amount. How many units must now be bought from A?

**Answer format:** Integer.

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

A scalar five-stage pipeline issues one instruction each cycle when unobstructed. A taken branch incurs two lost issue cycles; an untaken branch incurs none. An execution contains100 instructions, including20 branches, of which12 are taken. Ignore pipeline filling and draining and assume no other stalls. How many issue cycles are needed?

**Answer format:** Integer.

### Q12. [1 Mark] [MCQ]

Initially head points to node A in the singly linked list A→B→C→NULL. Consider these assignments, evaluated in order:

```text
p = head.next
head.next = p.next
p.next = head
head = p
```

Which list is reachable from head afterward?

A. A→C→B→NULL
B. B→A→C→NULL
C. B→C→A→NULL
D. A→B→C→NULL

### Q13. [1 Mark] [NAT]

For the grammar S→AB, A→aA | ε, B→aB | ε, how many distinct parse trees generate the terminal string aaa?

**Answer format:** Integer.

### Q14. [1 Mark] [MSQ]

On {1,2,3}, equivalence relation R has classes {1,2},{3}; equivalence relation S has classes {1},{2,3}. Which statements are correct?

A. R∪S is transitive.
B. R∩S is the identity relation.
C. The smallest equivalence relation containing R∪S has one class.
D. R∪S contains the ordered pair(1,3).

### Q15. [1 Mark] [MCQ]

Let R be a finite unary relation over an infinite domain. A tuple-calculus query asks for all x satisfying NOT R(x), with no further restriction on x. Which statement is correct?

A. The result is always finite because R is finite.
B. The result can be infinite and depends on values outside the active domain.
C. Negation is forbidden in every safe tuple-calculus query.
D. The result always equals R.

### Q16. [1 Mark] [NAT]

An instruction at byte address100 has length4 bytes and a signed PC-relative displacement−6. The architecture defines the target as the address of the next instruction plus twice the displacement. What is the target byte address?

**Answer format:** Integer.

### Q17. [1 Mark] [MCQ]

A change-making algorithm repeatedly takes the largest coin not exceeding the remaining amount. Coin denominations are1,4,6 with unlimited supplies. For amount8, which statement is correct?

A. Greedy uses two coins and is optimal.
B. Greedy uses three coins, while the optimum uses two.
C. Greedy uses four coins, while the optimum uses three.
D. No exact representation of8 exists.

### Q18. [1 Mark] [NAT]

Table T has column x with rows1,1,2,NULL. What is the number of rows returned by this query under SQL bag semantics?

```sql
SELECT x FROM T
UNION ALL
SELECT x FROM T WHERE x <> 1;
```

**Answer format:** Integer.

### Q19. [1 Mark] [NAT]

A real4×4 matrix P satisfies P²=P and trace(P)=3. What is the dimension of the null space of I−P?

**Answer format:** Integer.

### Q20. [1 Mark] [MSQ]

Two processes share a memory segment containing a counter initialized to0. Each performs one ordinary non-atomic read-increment-write operation. Which statements are correct without synchronization?

A. A final value of1 is possible.
B. A final value of2 is possible.
C. Shared memory automatically makes each read-increment-write atomic.
D. A final value of3 is possible from these two operations alone.

### Q21. [1 Mark] [NAT]

A real polynomial f has five distinct real roots. What is the minimum number of distinct real roots that its second derivative f'' must have?

**Answer format:** Integer.

### Q22. [1 Mark] [NAT]

A synchronous two-bit state machine has next-state equations Q1'=Q0 and Q0'=NOT Q1. Starting at00, how many clock edges occur before the state first returns to00?

**Answer format:** Integer.

### Q23. [1 Mark] [NAT]

A component is selected uniformly from two factories. Factory A produces10% defective components and factory B produces30% defective components. A selected component is found defective by a perfect inspection. What is the conditional probability that it came from B?

**Answer format:** Exact decimal.

### Q24. [1 Mark] [MCQ]

A stack initially empty receives items1,2,3,4 in that order. Pops may be interleaved with pushes. Which proposed output sequence is impossible?

A. 2,1,4,3
B. 3,2,1,4
C. 3,1,2,4
D. 4,3,2,1

### Q25. [1 Mark] [MSQ]

For0/1 knapsack, an implementation uses one array dp[c], initially zero. For each item of positive weight w and value v, it updates dp[c]=max(dp[c],dp[c−w]+v). Which statements are correct?

A. Scanning c downward from capacity to w prevents reuse of the current item.
B. Scanning upward can allow the same item to be used repeatedly.
C. Either direction always computes the0/1 optimum.
D. With a single item of weight2 and value3 and capacity4, an upward scan gives dp[4]=6.

### Q26. [1 Mark] [NAT]

A three-address-code representation allows each arithmetic instruction to contain exactly one binary operation and one assignment. Loads and copies are not needed; the operands a,b,c,d are already available. No algebraic reassociation is allowed. What is the minimum number of arithmetic instructions required to compute (a+b)*(c−d)+(a+b), reusing repeated subexpressions?

**Answer format:** Integer.

### Q27. [1 Mark] [MCQ]

A condition variable is associated with a mutex and predicate ready. Waiting atomically releases the mutex and later reacquires it before returning. Spurious wakeups are permitted. Which pattern correctly waits for ready?

A. Lock; if not ready, wait once; use protected data; unlock.
B. Lock; while not ready, wait; use protected data; unlock.
C. Test ready without the mutex, then lock only if true.
D. Lock; repeatedly test ready without releasing the mutex until it becomes true.

### Q28. [1 Mark] [NAT]

There are three identical reusable resources. Each of two processes may need at most two simultaneously; each holds any allocated resources until it finishes. If each currently holds one and requests one more, how many processes can finish first without preempting resources?

**Answer format:** Number of possible choices for the first finishing process.

### Q29. [1 Mark] [NAT]

A binary tree has distinct node labels. Its preorder traversal is A,B,D,E,C,F and its postorder traversal is D,E,B,F,C,A. Left and right child positions are distinguished, and a node may have only one child. How many binary trees have both of these traversals?

**Answer format:** Integer.
### Q30. [1 Mark] [MSQ]

An even-parity bit is appended to each fixed-length data word. Which statements are correct?

A. Every single-bit error in the transmitted word is detected.
B. Every two-bit error is detected.
C. Some errors affecting the parity bit and one data bit are undetected.
D. Every odd number of flipped bits is detected.

### Q31. [1 Mark] [NAT]

On the set {1,2,3,6,12}, order elements by divisibility. What is the join (least upper bound) of2 and3 in this partially ordered set?

**Answer format:** Integer.

### Q32. [1 Mark] [NAT]

Two unsigned8-bit fixed-point values have four fractional bits and raw integer encodings24 and40. Their exact product is to be represented with four fractional bits. What raw integer encoding represents that product?

**Answer format:** Integer.

### Q33. [1 Mark] [MSQ]

A deterministic pushdown automaton recognizes balanced parentheses by pushing on '(' and popping on ')', rejecting a pop from an empty stack. Acceptance requires the stack to be empty at end of input. Which statements are correct?

A. The empty string is accepted.
B. Equal total counts of '(' and ')' guarantee acceptance.
C. Every prefix of an accepted string has at least as many '(' as ')'.
D. The string '())(' is accepted.

### Q34. [1 Mark] [MCQ]

Consider ordinary integer variables with no overflow or side effects:

```text
x = a * 0
y = x + b
x = 7
return y
```

Which replacement computes the same returned value for all inputs?

A. return 7+b
B. return a+b
C. return b
D. return 0

### Q35. [1 Mark] [NAT]

In a simplified slotted contention scheme, two stations independently choose one of four slots uniformly and transmit once in that slot. A collision occurs if they choose the same slot. Given that station A chose a slot later than slot1, what is the collision probability?

**Answer format:** Exact decimal.

### Q36. [2 Marks] [MSQ]

In a finite directed network, every link has strictly positive cost and every router can reach destination d. Each router u other than d selects any outgoing neighbour v satisfying dist(u,d)=cost(u,v)+dist(v,d), using exact shortest-path distances. Different routers may break equal-cost ties independently. Which statements are correct?

A. The selected next-hop graph can contain a directed cycle because tie-breaking is independent.
B. Distance to d strictly decreases at each selected hop.
C. Every packet following these next hops eventually reaches d.
D. Allowing zero-cost links would leave the strict-decrease argument unchanged.

### Q37. [2 Marks] [MSQ]

Consider A=[[0,1],[1,1]]. An unpivoted factorization A=LU is sought with L unit lower triangular and U upper triangular. Which statements are correct?

A. Such an LU factorization exists because det(A) is nonzero.
B. Interchanging the rows allows a unit-lower/upper factorization.
C. A is invertible even though the stated unpivoted factorization is impossible.
D. The obstruction proves that the linear system Ax=b has no solution for some real b.

### Q38. [2 Marks] [MCQ]

A table has two rows with distinct primary keys1 and2 and a UNIQUE non-null code column initially containing A and B respectively. A transaction first updates row1's code to B and then row2's code to A. No other transaction runs. Which statement correctly distinguishes immediate checking from checking the UNIQUE constraint only at transaction commit?

A. Both modes must accept because the final state is unique.
B. Immediate checking rejects the first update; commit-only checking can accept the final swapped state.
C. Commit-only checking must reject because any intermediate duplicate is forbidden in that mode.
D. Both modes necessarily change the primary keys.

### Q39. [2 Marks] [NAT]

A single CPU uses preemptive shortest-remaining-processing-time scheduling, with no switching overhead. Processes P,Q,R arrive at times0,1,3 and require CPU times7,4,1 respectively. When remaining times tie, the currently running process continues. What is the sum of their waiting times?

**Answer format:** Integer time units.

### Q40. [2 Marks] [MSQ]

The following code uses unbounded integers. The input y is arbitrary.

```text
if y > 0:
    x = 2
else:
    x = 2
if x == 2:
    z = 7
else:
    z = y
```

Which statements are correct about the values and constant-propagation opportunities?

A. z is always7.
B. y must equal2 after the first conditional.
C. A flow-sensitive constant-propagation analysis can establish x=2 at the join and remove the unreachable second else branch.
D. The two different predecessor blocks force x to be nonconstant at their join even when both assign2.
### Q41. [2 Marks] [NAT]

A recursive procedure on a sorted array of length64 splits every non-singleton interval into two equal halves. It processes both children, then compares the last element of the left half with the first element of the right half. If they are already in nondecreasing order, it skips merging entirely. Otherwise it would merge, but this never occurs on the given sorted input. How many key comparisons are performed in total, including only the stated boundary tests?

**Answer format:** Integer.

### Q42. [2 Marks] [MSQ]

Let L1={a^n b^n c^m : n,m≥0} and L2={a^m b^n c^n : n,m≥0}. Which statements are correct?

A. Both L1 and L2 are context-free.
B. Their intersection is {a^n b^n c^n : n≥0}.
C. Their intersection must be context-free because each language is context-free.
D. Their union is context-free.

### Q43. [2 Marks] [NAT]

Insert the distinct keys8,4,12,2,6,10,14,5,7 into an initially empty binary search tree, without balancing. Delete key8 by copying its inorder predecessor into its node and then deleting the predecessor's original node. What is the sum of the keys compared with the target during a successful ordinary BST search for5 in the resulting tree, including5 itself?

**Answer format:** Integer.

### Q44. [2 Marks] [NAT]

A continuously differentiable function f on[0,2] satisfies f(2)=4 and the integral of f(x) over[0,2] equals3. What is the integral of x f'(x) over[0,2]?

**Answer format:** Exact number.

### Q45. [2 Marks] [NAT]

A disk has cylinders0 through199, and the head starts at50 moving toward larger numbers. Pending requests are at60,70,20, with no future arrivals. LOOK reverses at the largest pending request; SCAN proceeds to199 before reversing. Both stop immediately after serving the last request. How much more total head movement does SCAN make than LOOK?

**Answer format:** Integer cylinders.

### Q46. [2 Marks] [MSQ]

A TLB entry is keyed by(ASID, virtual page). A process with ASID5 terminates, leaving cached translations. A new process is assigned ASID5 with a different page table; the old translations are not invalidated. Which statements are correct?

A. A stale entry can translate the new process's address to an old physical frame.
B. The ASID field by itself makes reuse safe forever.
C. Invalidating entries for the reused ASID before execution prevents this stale-entry problem.
D. Merely changing the page-table base necessarily makes all old ASID-tagged entries miss.

### Q47. [2 Marks] [NAT]

An8-bit two's-complement ALU computes the expression (x+y)−y, wrapping after each operation. For x=100 and y=60, count how many of the two operations signal signed overflow. The overflow flag is recomputed separately for each operation.

**Answer format:** Integer.

### Q48. [2 Marks] [MSQ]

Relation R(X,Y,Z) has functional dependencies XY→Z and Z→Y. It is decomposed into R1(X,Z) and R2(Z,Y), using their projected dependencies. Which statements are correct?

A. The decomposition is lossless.
B. The decomposition preserves XY→Z through the projected dependencies alone.
C. Both components are in BCNF.
D. Z is necessarily a key of the original R.

### Q49. [2 Marks] [NAT]

A binary floating-point system has precision p=4 significant bits, includes an implicit leading1 for normalized numbers, and has enough exponent range for all numbers here. It rounds to nearest, ties to even. Compute fl(fl(8+0.5)+0.5), rounding after each addition. What value results?

**Answer format:** Exact decimal or integer.

### Q50. [2 Marks] [NAT]

A Boolean function f(a,b,c) must satisfy f(a,b,0)=a XOR b and f(a,b,1)=a OR b for every a,b. How many input assignments make f different from a OR b OR c?

**Answer format:** Integer.

### Q51. [2 Marks] [MSQ]

In the code below, execution starts at line1 and exits after line6. Only z is observed on exit. Expressions have no side effects.

```text
1: x = 1
2: if flag goto 5
3: y = x + 1
4: goto 6
5: y = 4
6: z = y
```

Which statements are correct about ordinary may-liveness analysis?

A. x is live immediately after line2.
B. x is live immediately before line5.
C. y is live immediately before line6.
D. Line1 is dead because one path does not use x.

### Q52. [2 Marks] [NAT]

A binary min-heap with distinct keys has array[1,4,2,8,5,3,7], using one-based indexing. Delete the minimum by moving the last key to the root, reducing the size, then repeatedly swapping it with its smaller child while needed. Then insert key0 by bubbling it upward. What key occupies array index3 after both operations?

**Answer format:** Integer.

### Q53. [2 Marks] [NAT]

A microprogram uses a control word with three independently chosen fields. Field F selects one of eight mutually exclusive operations; field G selects one of five mutually exclusive operations; field H specifies any subset of four independent enables. An encoded implementation uses the minimum binary bits for each field. A horizontal implementation uses one bit for each of the eight F operations, one for each of the five G operations, and four H bits. For a store of128 words, how many storage bits does encoding save?

**Answer format:** Integer.

### Q54. [2 Marks] [NAT]

An IPv4 datagram has a20-byte header and2400 bytes of payload. A router fragments it for an MTU of1020 bytes using the largest legal payload in each nonfinal fragment. The final fragment is later forwarded onto a link with MTU220 bytes and is fragmented again if necessary. All headers remain20 bytes, with no options. What is the fragment-offset field of the last fragment reaching the final link? Offset fields are in8-byte units relative to the original datagram payload.

**Answer format:** Integer.

### Q55. [2 Marks] [NAT]

An organization owns192.0.2.0/24. The ranges192.0.2.0/26 and192.0.2.192/26 are reserved and cannot be included in a free-space advertisement. What is the minimum number of CIDR prefixes whose union is exactly the remaining addresses?

**Answer format:** Integer.

### Q56. [2 Marks] [NAT]

Two disjoint groups each contain the same number of observations. Their means are2 and8, and their population variances are1 and9 respectively. What is the population variance of all observations combined?

**Answer format:** Exact number.

### Q57. [2 Marks] [MSQ]

For variables a,b,c,d, f=1 exactly when a XOR b=1, independently of c,d. A conventional sum-of-products Karnaugh-map minimization uses cubes that do not cover a zero. Which statements are correct?

A. f has a two-product implementation (NOT a)b+a(NOT b).
B. One product term is sufficient because eight of the sixteen inputs produce1.
C. Each of the two displayed products covers four minterms.
D. A valid product covering both(a,b)=(0,1) and(1,0) can omit both a and b without covering zeros.

### Q58. [2 Marks] [NAT]

An undirected graph has vertices1 through5 and edges12,23,31,34,45. A signed vertex-edge incidence matrix assigns an arbitrary orientation to every edge, placing−1 at its tail and+1 at its head. What is the dimension of the null space of this matrix over the real numbers?

**Answer format:** Integer.

### Q59. [2 Marks] [NAT]

Fixed-length records of100 bytes are stored without spanning in4096-byte blocks, each with a96-byte header. A sorted file contains401 records packed as fully as possible. An in-memory directory identifies the first block needed for a range query. The query must retrieve records at sorted ranks39 through83 inclusive, with ranks starting at1. How many distinct data blocks must be read, assuming nothing is cached?

**Answer format:** Integer.

### Q60. [2 Marks] [MSQ]

Let L={a^n : n is a perfect square}, including ε. For a hypothetical regular pumping length p≥1, choose s=a^(p²). A legal pumped part has length k with1≤k≤p. Which statements are correct?

A. Pumping once more gives length p²+k, strictly between p² and(p+1)².
B. For every legal decomposition, pumping twice leaves the language.
C. The proof depends on choosing the pumped part to have exactly p symbols.
D. The pumping lemma therefore proves L regular.

### Q61. [2 Marks] [NAT]

A recursive DFS starts at s in a directed graph with edges s→a,s→b,a→c,b→c,c→d. Each adjacency list is processed in alphabetical order. A vertex is marked immediately upon its first visit. How many edges lead to vertices already marked at the moment that edge is examined?

**Answer format:** Integer.

### Q62. [2 Marks] [NAT]

Under multiplication modulo15, consider the group of invertible residues. How many group elements x satisfy x²=1 modulo15?

**Answer format:** Integer.

### Q63. [2 Marks] [NAT]

An undirected graph has triangle vertices A,B,C with all three triangle edges of weight1. Vertex D is joined to A by a weight2 edge and to B by a weight3 edge; there are no other edges. How many distinct minimum spanning trees does the graph have?

**Answer format:** Integer.

### Q64. [2 Marks] [MSQ]

In this control-flow fragment, a and b are not modified, and arithmetic has no side effects or overflow:

```text
if flag:
    t = a + b
else:
    u = a + b
v = a + b
```

Which statements are correct?

A. The expression a+b has been evaluated on every path reaching the assignment to v.
B. Replacing v=a+b with v=t is always valid even if t is undefined on the else path.
C. A compiler may compute a+b into one common temporary before the branch and use it on both paths and afterward.
D. Replacing v=a+b with v=u is always valid even if u is undefined on the then path.

### Q65. [2 Marks] [MSQ]

A total decider D exists for language L over a finite alphabet. Consider a machine that enumerates all strings in length-lexicographic order, runs D on each, and prints precisely those D accepts. Which statements are correct?

A. Every string of L is eventually printed.
B. If L is empty, the enumerator must eventually halt.
C. If L is finite, the enumerator as described can run forever after printing its last member.
D. The construction requires a known uniform bound on D's running time over all inputs.



---

## ANSWER KEY — MOCK TEST 021

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | A |
| 2 | NAT | 1 | 0.2000 (accepted range 0.19995–0.20005) |
| 3 | MCQ | 1 | B |
| 4 | NAT | 1 | 32 |
| 5 | MCQ | 1 | A |
| 6 | NAT | 2 | 72 |
| 7 | NAT | 2 | 46 |
| 8 | NAT | 2 | 2 |
| 9 | MCQ | 2 | B |
| 10 | NAT | 2 | 100 |
| 11 | NAT | 1 | 124 |
| 12 | MCQ | 1 | B |
| 13 | NAT | 1 | 4 |
| 14 | MSQ | 1 | B, C |
| 15 | MCQ | 1 | B |
| 16 | NAT | 1 | 92 |
| 17 | MCQ | 1 | B |
| 18 | NAT | 1 | 5 |
| 19 | NAT | 1 | 3 |
| 20 | MSQ | 1 | A, B |
| 21 | NAT | 1 | 3 |
| 22 | NAT | 1 | 4 |
| 23 | NAT | 1 | 0.75 |
| 24 | MCQ | 1 | C |
| 25 | MSQ | 1 | A, B, D |
| 26 | NAT | 1 | 4 |
| 27 | MCQ | 1 | B |
| 28 | NAT | 1 | 2 |
| 29 | NAT | 1 | 2 |
| 30 | MSQ | 1 | A, C, D |
| 31 | NAT | 1 | 6 |
| 32 | NAT | 1 | 60 |
| 33 | MSQ | 1 | A, C |
| 34 | MCQ | 1 | C |
| 35 | NAT | 1 | 0.25 |
| 36 | MSQ | 2 | B, C |
| 37 | MSQ | 2 | B, C |
| 38 | MCQ | 2 | B |
| 39 | NAT | 2 | 6 |
| 40 | MSQ | 2 | A, C |
| 41 | NAT | 2 | 63 |
| 42 | MSQ | 2 | A, B, D |
| 43 | NAT | 2 | 22 |
| 44 | NAT | 2 | 5 |
| 45 | NAT | 2 | 258 |
| 46 | MSQ | 2 | A, C |
| 47 | NAT | 2 | 2 |
| 48 | MSQ | 2 | A, C |
| 49 | NAT | 2 | 8 |
| 50 | NAT | 2 | 2 |
| 51 | MSQ | 2 | A, C |
| 52 | NAT | 2 | 2 |
| 53 | NAT | 2 | 896 |
| 54 | NAT | 2 | 275 |
| 55 | NAT | 2 | 2 |
| 56 | NAT | 2 | 14 |
| 57 | MSQ | 2 | A, C |
| 58 | NAT | 2 | 1 |
| 59 | NAT | 2 | 3 |
| 60 | MSQ | 2 | A, B |
| 61 | NAT | 2 | 1 |
| 62 | NAT | 2 | 4 |
| 63 | NAT | 2 | 3 |
| 64 | MSQ | 2 | A, C |
| 65 | MSQ | 2 | A, C |


