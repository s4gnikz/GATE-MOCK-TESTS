# GATE CS 2027 — Full-Length Mock Test 076

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

A sequence has a1=2, a2=6 and a(n+2)=2a(n+1)−a(n)+2 for n≥1. Find a6.

**Answer format:** Integer.

### Q2. [1 Mark] [NAT]

A right triangle has perpendicular sides 6 cm and 8 cm. What is the altitude from its right-angle vertex to its hypotenuse?

**Answer format:** Exact finite decimal centimetres.

### Q3. [1 Mark] [MCQ]

Which sentence states that every report was read by at least one reviewer, without asserting that a single reviewer read all reports?

A. One reviewer read every report.
B. Every report was read by some reviewer.
C. Every reviewer read every report.
D. No reviewer read a report.

### Q4. [1 Mark] [NAT]

A price is first increased by p percent and then reduced by p percent, where 0<p<100. The final price is 96% of the original. What is p?

**Answer format:** Exact integer.

### Q5. [1 Mark] [MSQ]

Exactly one of K,L,M is a coordinator. K is a coordinator only if L is available. L is unavailable. If M is a coordinator, N is available. Which conclusions necessarily follow?

A. K is not the coordinator.
B. L is the coordinator.
C. Either L or M is the coordinator.
D. N is available.

### Q6. [2 Marks] [MCQ]

Let R rotate a point 90° counterclockwise about the origin and F reflect it in the line y=x. Starting at (2,1), what pair gives the resulting points for “R then F” and “F then R,” respectively?

A. ((−2,1),(2,−1))  
B. ((−1,2),(1,−2))  
C. ((2,−1),(−2,1))  
D. ((2,−1),(2,−1))

### Q7. [2 Marks] [MCQ]

“A new policy reduced average processing time, but the study did not measure the number of incorrect decisions.” Which claim is justified by the study as described?

A. Processing became faster on average, while the effect on decision accuracy remains unmeasured.
B. Decision accuracy necessarily improved.
C. Every decision became faster and more accurate.
D. Incorrect decisions necessarily increased.

### Q8. [2 Marks] [MSQ]

The distinct letters A,B,C,D,E are arranged in a row, each exactly once. Let X be the set of arrangements where A and B are adjacent in either order, and Y the set where B and C are adjacent in either order. Which statements are correct?

A. X contains48 arrangements.
B. The intersection of X and Y contains24 arrangements.
C. Exactly72 arrangements belong to at least one of X and Y.
D. Exactly36 arrangements belong to neither X nor Y.

### Q9. [2 Marks] [MCQ]

Two teams produce identical items. The table lists working hours and completed items in two months. Overall productivity means total completed items divided by total working hours.

| Team | Month 1 hours | Month 1 items | Month 2 hours | Month 2 items |
|---|---:|---:|---:|---:|
| A | 40 | 400 | 60 | 660 |
| B | 60 | 900 | 40 | 640 |

What is the percentage change in overall productivity from Month 1 to Month 2?

A. 0%  
B. 8% increase  
C. 10% increase  
D. 12% increase

### Q10. [2 Marks] [MCQ]

Six unit squares form a cube net. Their centres on a square grid are A=(0,0), B=(1,0), C=(2,0), D=(3,0), E=(1,1), and F=(1,-1). Squares sharing a full edge are hinged, and the net is folded into a cube with labels on the outside. Which pair of faces is opposite, and which triple can meet at one cube vertex?

A. A and C are opposite; A,B,E can meet.
B. B and C are opposite; A,C,E can meet.
C. E and F are opposite; A,B,C can meet.
D. A and D are opposite; B,E,F can meet.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

Insert 8,3,10,1,6,4,7 into an initially empty ordinary binary search tree, with no rebalancing. Delete key 3 by replacing it with its inorder successor and then removing that successor's old node. What is the key of the left child of node 6 after deletion?

**Answer format:** Enter -1 if the child is absent; otherwise enter its key.

### Q12. [1 Mark] [MCQ]

Which word belongs to (ab|ba)* but not to (ab)*?

A. abab
B. baab
C. aabb
D. aaa

### Q13. [1 Mark] [NAT]

A TCP sender's next unsent byte has sequence number5000. It receives a cumulative ACK with acknowledgment number4200 and advertised window600 bytes. Assume no sequence-number wraparound and that the congestion window imposes no tighter restriction. How many new bytes may it send immediately, without retransmitting already sent bytes?

**Answer format:** Exact integer.

### Q14. [1 Mark] [NAT]

A continuous random variable X has density f(x)=c x(1−x) for 0<x<1 and zero elsewhere, with c chosen to normalize the density. Find E[X²].

**Answer format:** Exact finite decimal.

### Q15. [1 Mark] [MCQ]

A five-stage in-order pipeline has stages IF,ID,EX,MEM,WB, each one cycle. There is no forwarding and no automatic stalling. Register writes occur in the first half of a cycle and ID reads in the second half, so ID may read a value written in WB during the same cycle. The instructions below use ordinary integer registers; R0 is always available. What is the minimum total number of NOP instructions that must be inserted without reordering to guarantee correct results for arbitrary initial register values?
```text
ADD R1,R0,R0
ADD R2,R1,R0
ADD R3,R2,R0
```

A. 2  
B. 3  
C. 4  
D. 6

### Q16. [1 Mark] [NAT]

On the power set of {1,2,3,4}, define X~Y exactly when |X| and |Y| have the same remainder modulo 3. How many equivalence classes does this relation have?

**Answer format:** Integer.

### Q17. [1 Mark] [MCQ]

A two-input gate outputs 1 exactly when its inputs differ. Its output is fed to a second identical gate together with a third input c. Which description of the final output is correct?

A. It is 1 exactly when one input, but not all three, is 1.
B. It is 1 exactly when an odd number of the three inputs are 1.
C. It is 1 exactly when at least two inputs are 1.
D. It is 1 exactly when all inputs agree.

### Q18. [1 Mark] [MCQ]

Resource type A has two instances and B one. P holds one A and requests B; Q holds B and requests one A. The other A instance is free. A process releases its resources after receiving its requested resource and finishing. Which statement is correct?

A. The cycle in the resource graph necessarily implies deadlock.
B. Q can receive the free A and finish, allowing P to proceed.
C. No process can receive any resource.
D. P must be aborted for any progress.

### Q19. [1 Mark] [NAT]

A scalar constant-propagation analysis sees three incoming paths to a join. Two set x=4; the third is provably unreachable and would set x=9. If unreachable paths are excluded, what constant value can be assigned to x at the join?

**Answer format:** Integer.

### Q20. [1 Mark] [NAT]

Table T has column x with rows1,1,2,NULL. What is the number of rows returned by this query under SQL bag semantics?

```sql
SELECT x FROM T
UNION ALL
SELECT x FROM T WHERE x <> 1;
```

**Answer format:** Integer.

### Q21. [1 Mark] [MCQ]

A variable is live if its current value may be read along a subsequent control-flow path before being overwritten. In the code below, x, y, z and flag are ordinary variables, and there are no implicit uses after return. Which set contains exactly the variables live at P, immediately before y = z?

```text
L: x = y
   if flag goto K
P: y = z
   goto L
K: return x
```

A. {z, flag}  
B. {x, z, flag}  
C. {y, z, flag}  
D. {x, y, z, flag}

### Q22. [1 Mark] [NAT]

A parent row P has two child rows C1,C2. C1 has two grandchild rows and C2 has one. Both foreign-key levels use ON DELETE CASCADE; no other rows reference any of these rows. How many rows in total are deleted when P is deleted, including P itself?

**Answer format:** Integer.

### Q23. [1 Mark] [MCQ]

A datagram socket has two queued datagrams, with payloads ABCDE and FG in that order. A receive buffer has space for three bytes. In this specified model, a receive returns at most one datagram and discards any excess bytes of a truncated datagram. After one receive returns ABC, what payload does the next receive return?

A. FG
B. DE
C. DEF
D. DEFG

### Q24. [1 Mark] [NAT]

A normalized binary floating-point format has five significant bits including the leading 1. What is the spacing between adjacent representable numbers in [8,16), assuming the exponent range includes this interval?

**Answer format:** Exact finite decimal.

### Q25. [1 Mark] [NAT]

A divide-and-conquer procedure on 16 elements repeatedly splits each nontrivial problem into equal halves until size one. How many leaves are in its recursion tree?

**Answer format:** Integer.

### Q26. [1 Mark] [MSQ]

A recursive depth-first search on a directed graph colors undiscovered vertices white, vertices on its active recursion stack gray, and finished vertices black. A currently explored edge is u→v. Which statements hold?

A. If v is gray, the graph contains a directed cycle.
B. If v is black, u→v necessarily belongs to a directed cycle.
C. If no edge to a gray vertex is encountered during a full DFS forest, the graph is acyclic.
D. If v is white, v must be an ancestor of u in the current DFS tree.

### Q27. [1 Mark] [MCQ]

Relation R(A,B,C) has exactly the functional dependencies implied by AB→C and C→B. Assuming atomic attribute values, which classification is correct?

A. R is in BCNF because every attribute belongs to a key.
B. R is in3NF but not BCNF.
C. R violates2NF because C→B has a single-attribute determinant.
D. A alone is a candidate key.

### Q28. [1 Mark] [NAT]

An instruction has a12-bit signed displacement encoded in two's complement and scaled by four bytes. What is the most negative byte displacement it can encode?

**Answer format:** Integer.

### Q29. [1 Mark] [MSQ]

A connected, undirected graph has a unique minimum spanning tree T. Every edge weight is replaced by w'(e)=3w(e)+7. Which statements necessarily hold?

A. T remains the unique minimum spanning tree.
B. Every shortest path remains a shortest path.
C. The relative weights of any two spanning trees remain ordered in the same way.
D. The weight of T increases by exactly 7.

### Q30. [1 Mark] [NAT]

An array-based binary min-heap is [2,7,4,12,9,6,5], using one-based indices. Delete the minimum by moving the last element to the root and repeatedly exchanging it with its smaller child until the heap property holds. What is the sum of the values at indices2 and3 afterward?

**Answer format:** Integer.

### Q31. [1 Mark] [MSQ]

A real 4×4 matrix M satisfies M²=I and trace(M)=0. Which statements must hold?

A. det(M)=1.  
B. rank(M−I)=2.  
C. M is diagonalizable over the real numbers.  
D. M is symmetric.

### Q32. [1 Mark] [MCQ]

A function f is continuous on[0,2] and twice differentiable on(0,2), with f(0)=0,f(1)=2,f(2)=0. Which statement must hold?

A. f''(x)<0 at every x in(0,2).
B. f''(x)<0 at some x in(0,2).
C. f''(1)=−4.
D. f'(1)=0.

### Q33. [1 Mark] [NAT]

For grammar S→S | a, how many distinct finite parse trees generate a and contain at most three applications of S→S?

**Answer format:** Integer.

### Q34. [1 Mark] [NAT]

Three jobs arrive at0. Estimated CPU bursts for A,B,C are1,2,3, while actual bursts are8,1,1. A nonpreemptive scheduler executes jobs by increasing estimate. What is its total waiting time minus the minimum total waiting time attainable with knowledge of the actual bursts? There is no switching overhead.

**Answer format:** Integer time units.

### Q35. [1 Mark] [NAT]

What is the smallest size of a nonempty finite domain D on which a binary relation R can make `∀x∃y R(x,y)` true but `∃y∀x R(x,y)` false? Both quantifiers range over D.

**Answer format:** Integer.

### Q36. [2 Marks] [NAT]

A PDA starts with one bottom-of-stack marker. On each input a it pushes two ordinary symbols; on each b it pops one ordinary symbol and rejects if only the bottom marker remains. Acceptance requires input exhaustion with only the marker left. For input aabbbb, what is the maximum stack height, counting the marker, reached during the computation?

**Answer format:** Integer.

### Q37. [2 Marks] [NAT]

A sorted file occupies100 pages, each with100 records. A sparse index has one entry per data page, with20 entries fitting per index page. The index is searched in memory after all its pages are fetched once. A query then fetches one qualifying data page. With an empty buffer and no other reads, how many page reads occur?

**Answer format:** Integer.

### Q38. [2 Marks] [NAT]

An expression parser uses grammar E→E−E | num. It resolves every shift/reduce conflict on `−` by shifting. What value does it assign to `20−5−3` using exact arithmetic?

**Answer format:** Integer.

### Q39. [2 Marks] [NAT]

A stop-and-wait sender retransmits one packet until it receives an acknowledgment. Each data transmission is independently lost with probability 0.2. Each successfully received copy triggers an acknowledgment, independently lost with probability 0.1. An unsuccessful attempt times out before the next begins; there are no delayed packets or acknowledgments. Count every receiver arrival, including duplicates. What is the expected number of duplicate arrivals before the sender stops, excluding the first received copy? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q40. [2 Marks] [NAT]

A Boolean function f(a,b,c) must satisfy f(a,b,0)=a XOR b and f(a,b,1)=a OR b for every a,b. How many input assignments make f different from a OR b OR c?

**Answer format:** Integer.

### Q41. [2 Marks] [NAT]

An unsigned four-bit adder adds inputs11 and9 with carry-in0. Let S be the low four-bit unsigned result and C the carry-out bit. What is S+16C?

**Answer format:** Integer.

### Q42. [2 Marks] [MSQ]

A poset has elements a,b,c,d with a<c,b<c,c<d, and only the comparisons forced by these and reflexivity. Let J be the family of its downward-closed subsets, ordered by inclusion. Which statements are correct?

A. J has six elements, including the empty subset.
B. Join in J is set union.
C. Meet in J is set intersection.
D. J fails distributivity because a and b are incomparable.

### Q43. [2 Marks] [NAT]

Packets A, B and C are sent back-to-back in that order through two links and a store-and-forward router. Their transmission times on link 1 are respectively 3, 1 and 2 ms; on link 2 they are respectively 1, 4 and 2 ms. Each link has a propagation delay of 2 ms. The router forwards complete packets in arrival order as soon as link 2 is free. Links operate concurrently; processing time is zero. How many milliseconds after the first bit of A leaves the source does the last bit of C reach the destination?

**Answer format:** Integer milliseconds.

### Q44. [2 Marks] [MCQ]

A programming language permits arbitrarily nested comments, with tokens OPEN and CLOSE marking comment boundaries. Why is a fixed finite-state lexer, with no extra stack or counter, insufficient to recognize exactly the balanced comment sequences of unbounded depth?

A. It would need to distinguish arbitrarily many outstanding OPEN counts.
B. Every finite input requires infinitely many processing steps.
C. The two-token alphabet is infinite.
D. All non-nested comments are also nonregular by definition.

### Q45. [2 Marks] [MCQ]

Six distinct keys are in two already sorted runs of three keys each. Only comparisons between keys reveal their relative order. What is the smallest achievable worst-case number of additional comparisons needed to merge the runs into one sorted run?

A. 3  
B. 4  
C. 5  
D. 6

### Q46. [2 Marks] [MCQ]

A TCP receiver advertises zero window because its buffer is full. The network has no loss. Which statement is correct?

A. The sender should interpret this as proof that a router dropped a packet.
B. Receiver flow control currently prevents ordinary new data from exceeding that advertised allowance.
C. The receiver has permanently closed the TCP connection.
D. The sender's congestion window must become exactly zero immediately.

### Q47. [2 Marks] [MSQ]

A DNS record is cached with a positive TTL. The authoritative server changes the record before that TTL expires. Assume ordinary caching without an explicit invalidation mechanism. Which statements are correct?

A. A resolver can continue returning the cached old record until expiry.
B. Every cache is immediately informed of the authoritative change by the TTL field itself.
C. Reducing the authoritative record's TTL afterward does not retroactively shorten a previously cached expiry under this model.
D. TTL is a guarantee that the authoritative value cannot change during that interval.

### Q48. [2 Marks] [NAT]

For solving Ax=b, a factorization PA=LU is supplied. P swaps the first two rows, b=(1,2,3)ᵀ, L has rows (1,0,0),(2,1,0),(−1,3,1), and U has rows (2,1,−1),(0,3,2),(0,0,4). Find the third component of x.

**Answer format:** Exact finite decimal.

### Q49. [2 Marks] [MSQ]

An undirected simple graph with n vertices and m edges is represented either by a Boolean adjacency matrix or adjacency lists. Lists are unsorted and store each undirected edge twice. Which worst-case bounds hold?

A. The matrix uses Θ(n²) entries even for an empty graph.
B. Enumerating all neighbours of v from the matrix takes Θ(deg(v)) time for every v without extra indexing.
C. Enumerating all neighbours of v from its list takes Θ(1+deg(v)) time, including access to an empty list.
D. The lists require Θ(n+m) storage, including vertex headers.

### Q50. [2 Marks] [NAT]

A microprogram has40 microinstructions. Each has12 independent control bits and a next-address field able to address every microinstruction. A redesigned store has the same40 entries but adds a two-bit branch-condition selector to every word. What is the increase in total control-store capacity, in bits?

**Answer format:** Integer.

### Q51. [2 Marks] [MCQ]

A B+ tree has all leaves exactly two edges below the root. The root and each nonroot internal node have between two and four children. Each leaf stores between two and four data keys; internal separator copies are not data keys. Which pair gives the minimum and maximum possible data-key counts?

A. (4,16)
B. (8,64)
C. (8,32)
D. (16,64)

### Q52. [2 Marks] [MSQ]

Host H sends an IPv4 packet through two routers to host J. Each link uses Ethernet, and there is no NAT, tunneling, or fragmentation. Which statements hold for normal forwarding?

A. The source and destination Ethernet addresses can change at each routed hop.
B. The source and destination IPv4 addresses change at every routed hop.
C. The IPv4 TTL decreases at each router that forwards the packet.
D. An Ethernet destination address on the first link must be J's Ethernet address even when J is on another subnet.

### Q53. [2 Marks] [NAT]

A disk's cylinders are 0 through 199. The head is at 80 and is moving upward. Pending requests are 20,90,150. Under SCAN, the head continues to cylinder 199 before reversing, even after serving 150. Stop measuring when the final pending request is served. What total distance is travelled?

**Answer format:** Integer cylinders.

### Q54. [2 Marks] [MSQ]

Choose a,b independently and uniformly from {0,1,2,3,4}, and define h(x)=(ax+b) mod 5 on the same domain. For two distinct fixed keys x,y, which statements are true?

A. For each ordered pair (r,s) of output values, exactly one pair (a,b) gives h(x)=r,h(y)=s.
B. Every function in this family is a permutation of the domain.
C. The probability h(x)=h(y) is 1/5.
D. After conditioning on a≠0, h(x) and h(y) remain independent uniform variables.

### Q55. [2 Marks] [MCQ]

Let L consist of binary strings of length at least four whose fourth symbol from the right is 1. What is the number of states in a smallest complete DFA for L?

A. 5
B. 16
C. 17
D. 32

### Q56. [2 Marks] [NAT]

A database initially has x=100. Transaction T1 adds20 to x and commits. A later transaction T2 reads the committed value, subtracts5, and aborts. Recovery uses transaction rollback to restore T2's before-image; T1 is not undone. What is the recovered value of x?

**Answer format:** Exact integer.

### Q57. [2 Marks] [NAT]

Fixed partitions have sizes8,12,20 KiB. Processes of sizes7,10,18 KiB are assigned to them respectively. What is total internal fragmentation, in KiB?

**Answer format:** Integer.

### Q58. [2 Marks] [MCQ]

A TCP connection has congestion window 10,000 bytes and advertised receive window 7,000 bytes. Its oldest unacknowledged sequence number is 20,000 and the next unsent byte has sequence number 25,000. There is no wraparound. An ACK arrives with acknowledgment number 23,000 and advertised receive window 4,000; assume the congestion window remains unchanged and no data are sent before processing it. How many additional data bytes may be sent immediately?

A. 1,000
B. 2,000
C. 4,000
D. 5,000

### Q59. [2 Marks] [NAT]

Assume all array accesses in this C program are valid and int can represent all values shown. What value is returned?

```c
int f(void) {
    int a[4] = {3, 5, 7, 9};
    int *p = a + 1;
    int **q = &p;
    (*q)++;
    **q += a[0];
    return p[-1] + a[2] + (int)(p - a);
}
```

**Answer format:** Exact integer.

### Q60. [2 Marks] [MSQ]

For L={0^n1^n : n≥0}, choose0^p1^p in a pumping-lemma argument, where p is a proposed regular pumping length. Which statements are correct?

A. Every legal pumped part lies entirely in the0 block.
B. Pumping that nonempty part down changes the number of0s while leaving the number of1s unchanged.
C. One must know the exact pumped-part length before choosing the original string.
D. The resulting contradiction disproves regularity.

### Q61. [2 Marks] [MCQ]

In the covering stage of tabular Boolean minimization, the following is the complete prime-implicant chart. Column labels denote the six required on-set minterms; don't-care minterms, if any, need not be covered. A mark means the prime implicant covers that required minterm. Use only these prime implicants. Minimize the number of selected product terms first, then the total literal count among covers with that minimum term count.

| Prime implicant | m1 | m2 | m3 | m4 | m5 | m6 | Literals |
|---|---|---|---|---|---|---|---:|
| P1 | X | X | X | | | | 2 |
| P2 | X | | | X | X | | 3 |
| P3 | | X | | X | | X | 3 |
| P4 | | | X | | X | X | 4 |

Which set is selected by this criterion?

A. {P1,P2}  
B. {P1,P3,P4}  
C. {P1,P2,P3}  
D. {P2,P3,P4}

### Q62. [2 Marks] [NAT]

Evaluate ∫ from −1 to 2 of |x²−x| dx. Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q63. [2 Marks] [NAT]

Five observations have sum 20 and sum of squares 90. One observation equal to 6 is removed. What is the population variance of the remaining four observations, using divisor four?

**Answer format:** Exact finite decimal.

### Q64. [2 Marks] [MCQ]

Use the standard SLR(1) construction for the augmented grammar below. How many LR(0) item-set states have a shift/reduce conflict in the resulting SLR table?

```text
S' -> S
S  -> A a | b A c | d c | b d a
A  -> d
```

A. 0  
B. 2  
C. 1  
D. 3

### Q65. [2 Marks] [NAT]

A process has four virtual pages numbered 0–3, initially absent from memory, and two frames. It accesses pages 0,1,0,2,1,3,1,2 in that order. Under optimal offline page replacement, what is the minimum possible number of page faults?

**Answer format:** Integer.

---

## ANSWER KEY — MOCK TEST 076

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | NAT | 1 | 42 |
| 2 | NAT | 1 | 4.8 |
| 3 | MCQ | 1 | B |
| 4 | NAT | 1 | 20 |
| 5 | MSQ | 1 | A, C |
| 6 | MCQ | 2 | C |
| 7 | MCQ | 2 | A |
| 8 | MSQ | 2 | A, D |
| 9 | MCQ | 2 | A |
| 10 | MCQ | 2 | A |
| 11 | NAT | 1 | -1 |
| 12 | MCQ | 1 | B |
| 13 | NAT | 1 | 0 |
| 14 | NAT | 1 | 0.3 |
| 15 | MCQ | 1 | C |
| 16 | NAT | 1 | 3 |
| 17 | MCQ | 1 | B |
| 18 | MCQ | 1 | B |
| 19 | NAT | 1 | 4 |
| 20 | NAT | 1 | 5 |
| 21 | MCQ | 1 | A |
| 22 | NAT | 1 | 6 |
| 23 | MCQ | 1 | A |
| 24 | NAT | 1 | 0.5 |
| 25 | NAT | 1 | 16 |
| 26 | MSQ | 1 | A, C |
| 27 | MCQ | 1 | B |
| 28 | NAT | 1 | -8192 |
| 29 | MSQ | 1 | A, C |
| 30 | NAT | 1 | 12 |
| 31 | MSQ | 1 | A, B, C |
| 32 | MCQ | 1 | B |
| 33 | NAT | 1 | 4 |
| 34 | NAT | 1 | 14 |
| 35 | NAT | 1 | 2 |
| 36 | NAT | 2 | 5 |
| 37 | NAT | 2 | 6 |
| 38 | NAT | 2 | 18 |
| 39 | NAT | 2 | 0.1111 (range 0.11105–0.11115) |
| 40 | NAT | 2 | 2 |
| 41 | NAT | 2 | 20 |
| 42 | MSQ | 2 | A, B, C |
| 43 | NAT | 2 | 14 |
| 44 | MCQ | 2 | A |
| 45 | MCQ | 2 | C |
| 46 | MCQ | 2 | B |
| 47 | MSQ | 2 | A, C |
| 48 | NAT | 2 | 3.5 |
| 49 | MSQ | 2 | A, C, D |
| 50 | NAT | 2 | 80 |
| 51 | MCQ | 2 | B |
| 52 | MSQ | 2 | A, C |
| 53 | NAT | 2 | 298 |
| 54 | MSQ | 2 | A, C |
| 55 | MCQ | 2 | B |
| 56 | NAT | 2 | 120 |
| 57 | NAT | 2 | 5 |
| 58 | MCQ | 2 | B |
| 59 | NAT | 2 | 17 |
| 60 | MSQ | 2 | A, B, D |
| 61 | MCQ | 2 | C |
| 62 | NAT | 2 | 1.8333 (range 1.83325–1.83335) |
| 63 | NAT | 2 | 1.25 |
| 64 | MCQ | 2 | B |
| 65 | NAT | 2 | 5 |
