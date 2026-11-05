# GATE CS 2027 — Full-Length Mock Test 097

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

A notice must express that a visitor may enter only when accompanied by a guide, while making no promise that accompaniment alone guarantees entry. Which sentence states precisely this necessary condition?

A. Every visitor accompanied by a guide may enter.
B. A visitor may enter if and only if accompanied by a guide.
C. A visitor may enter only if accompanied by a guide.
D. A visitor may enter unless accompanied by a guide.

### Q2. [1 Mark] [NAT]

A uniform mixture of two grains has average cost50 currency units per kilogram. Five kilograms are removed and replaced by five kilograms of grain costing40 per kilogram. The resulting average is45 per kilogram. What was the mixture's original mass?

**Answer format:** Exact number of kilograms.

### Q3. [1 Mark] [MSQ]

Some A are B. Every B is C. No C is D. Which conclusions necessarily follow?

A. Every A is C.  
B. Some A are not D.  
C. Some D are A.  
D. No B is D.

### Q4. [1 Mark] [NAT]

A point is rotated180 degrees about(1,0), then180 degrees about(0,2). Starting at(3,4), what is the squared distance between its initial and final positions?

**Answer format:** Integer.

### Q5. [1 Mark] [MCQ]

“A train service reduced the average delay but increased the maximum delay.” Which statement follows from these two statistics alone?

A. Every passenger experienced a shorter delay.
B. At least one statistic improved while the worst observed delay became larger.
C. The statistics are mathematically inconsistent.
D. The median delay necessarily increased.

### Q6. [2 Marks] [NAT]

A workshop must produce exactly 20 items using two methods. Method A takes two hours and costs 3 units per item; method B takes one hour and costs 5 units per item. The total processing-time budget is 28 hours, with no overlap of work. What is the minimum total cost?

**Answer format:** Integer cost units.

### Q7. [2 Marks] [NAT]

A service centre completed 18 of 20 jobs on Monday and 12 of 20 on Tuesday. On Wednesday it completes every job it receives. What is the minimum number of Wednesday jobs needed to make the combined three-day completion rate at least 80%?

**Answer format:** Integer.

### Q8. [2 Marks] [NAT]

A rectangular sheet occupies 0≤x≤8 and 0≤y≤6. Fold its right half onto the left along x=4, then fold its top half onto the bottom along y=3. In the folded rectangle, cut out the entire small rectangle 3<x≤4, 1<y<2 through all layers. What is the total perimeter of all resulting internal holes after the sheet is unfolded? The cut reaches the folded edge x=4, but does not touch y=3 or the original sheet's outer boundary.

**Answer format:** Exact integer, in the same length units.

### Q9. [2 Marks] [MCQ]

Arrange the following sentences into a coherent chronological account. Treat the explicitly stated causal and time relations as binding.

P. Based on the successful repeat trial, the final report recommended a full rollout.
Q. Both gauges were calibrated before the first trial began.
R. During that first trial, the two readings diverged as temperature rose.
S. Replacing one gauge eliminated this divergence in a repeat trial.
T. After receiving the final report, the committee accepted its recommendation.

Which sequence is correct?

A. Q-R-P-S-T  
B. R-Q-S-P-T  
C. Q-R-S-P-T  
D. Q-S-R-T-P

### Q10. [2 Marks] [NAT]

Two rectangular sheets occupy [0,4]×[0,2] and [2,6]×[1,3] in a coordinate plane. Their overlap is glued and becomes internal to the combined flat shape. What is the perimeter of their union?

**Answer format:** Integer length units.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MSQ]

A recognizer for a language may loop on some nonmembers. Which statements are correct?

A. If it accepts an input, that input is a member.
B. If it has not halted after a fixed finite number of steps, the input must be a nonmember.
C. A decider must halt on every input.
D. Every recognizer is automatically a decider.

### Q12. [1 Mark] [NAT]

An epsilon-NFA has states 0,1,2,3, initial state 0, and these transitions; unlisted transitions have empty target sets.
```text
0 --a--> 0,1
1 --epsilon--> 2
2 --b--> 3
3 --epsilon--> 1
```
After consuming the entire input aab, take epsilon closure. How many states are in the resulting active-state set?

**Answer format:** Numeric value; integer.

### Q13. [1 Mark] [MSQ]

On a nonempty domain, P and Q are unary predicates. Which implications are valid for every interpretation?

A. (∀x P(x)) OR (∀x Q(x)) implies ∀x(P(x) OR Q(x)).
B. ∀x(P(x) OR Q(x)) implies (∀x P(x)) OR (∀x Q(x)).
C. ∃x(P(x) AND Q(x)) implies (∃x P(x)) AND (∃x Q(x)).
D. (∃x P(x)) AND (∃x Q(x)) implies ∃x(P(x) AND Q(x)).

### Q14. [1 Mark] [NAT]

An unlimited supply of coins of denominations 1 and 3 is used to make amount 5. If order matters, how many sequences of coins have total value 5?

**Answer format:** Integer.

### Q15. [1 Mark] [MSQ]

Initially, on-call flags A and B are both 1. Transaction T1 reads B and, if B=1, writes A=0. Transaction T2 reads A and, if A=1, writes B=0. Both read the same initial snapshot. A system rejects concurrent transactions only when they write a common item. Which statements hold?

A. Both transactions can commit under this rule.
B. Every serial execution leaves A=B=0.
C. The committed outcome can violate the invariant A+B≥1.
D. Testing only for overlapping write sets fails to prevent this anomaly.

### Q16. [1 Mark] [NAT]

A sliding-window minimum algorithm maintains a deque of indices. Before inserting each new index i, it removes expired indices from the front, then removes indices from the back while their values are at least the new value, then appends i. The window length is3. Starting empty, process values[4,2,3,1] from left to right. How many removals from the back occur in total?

**Answer format:** Integer.

### Q17. [1 Mark] [NAT]

A binary search repeatedly compares the target with a midpoint key, returning on equality and otherwise searching the appropriate remaining half. Midpoint is floor((low+high)/2). On the sorted keys 1 through 15, how many key comparisons find target 14?

**Answer format:** Integer.

### Q18. [1 Mark] [NAT]

A rooted ordered tree has root R with children A,B,C in that order. A has children D,E, B has none and C has child F. In the left-child/right-sibling binary representation, how many right-sibling pointers are non-null?

**Answer format:** Integer.

### Q19. [1 Mark] [MSQ]

Two threads use a mutex to protect a counter. The counter is initialized once before either starts. Each thread locks, reads, increments, writes and unlocks exactly once. Which statements are correct under ordinary correct mutex semantics?

A. The two increment regions cannot overlap.
B. The final value is the initial value plus2.
C. The mutex by itself specifies which thread increments first.
D. Removing the lock but retaining the unlock preserves the synchronization guarantee.

### Q20. [1 Mark] [MSQ]

A prime-implicant chart has columns 1,2,3 and rows P covering {1,2}, Q covering {2,3}, R covering {1,3}. All columns must be covered. Which statements are true?

A. P is essential because it covers two columns.
B. No prime implicant is essential.
C. Two rows suffice to cover all columns.
D. The absence of an essential prime implicant means no cover exists.

### Q21. [1 Mark] [MCQ]

The three-input majority function is F=xy+xz+yz. A two-to-one multiplexer selects D0 when x=0 and D1 when x=1. Which pair (D0,D1) realizes F?

A. (y OR z, y AND z)
B. (y AND z, y OR z)
C. (y XOR z, y AND z)
D. (NOT y, z)

### Q22. [1 Mark] [MSQ]

In a basic block, p and q are pointers to valid int objects and may alias. Consider `t=*p; *q=7; u=*p;`. There is no concurrency or volatile access. Which statements are correct?

A. Replacing the final load by u=t is valid whenever p and q are proved to point to different objects.
B. The replacement is valid for all possible aliases and initial values.
C. If p=q and the initial pointed-to value is 3, the original block ends with t=3,u=7.
D. A store through q cannot affect a subsequent load through p because the pointer names differ.

### Q23. [1 Mark] [NAT]

A router has routes192.0.2.0/24→A,192.0.2.128/25→B and192.0.2.160/27→C, using longest-prefix match. How many addresses in192.0.2.0/24 are forwarded to B?

**Answer format:** Integer address count; include all addresses in the ranges.

### Q24. [1 Mark] [MSQ]

At entry to a block, x and y have defined values. The block is:

```text
x = y + 1
z = x + y
return z
```

No other use follows. Which statements are correct under standard liveness analysis?

A. The incoming value of x is live at block entry.
B. The incoming value of y is live at block entry.
C. Immediately after the first assignment, both x and y are live.
D. Immediately after the second assignment, y is live.

### Q25. [1 Mark] [MSQ]

A producer sends messages through an operating-system queue and a consumer receives them. Which statements distinguish message passing from directly accessing an ordinary shared variable?

A. Communication uses send/receive operations on messages.
B. A messaging interface can transfer data between distinct address spaces.
C. Message passing necessarily makes every application free of race conditions.
D. All message passing must use busy waiting.

### Q26. [1 Mark] [NAT]

During merge-based inversion counting, the sorted left half is[2,5,7] and the sorted right half is[1,5,6]. An inversion is a pair of positions i<j with value[i]>value[j], strictly. How many cross-half inversions are counted at this merge?

**Answer format:** Integer.

### Q27. [1 Mark] [NAT]

The coefficient rows of a linear system in three unknowns are (1,1,1), (1,2,3), (2,3,4), and the corresponding right-hand sides are 1,t,3. For what value of t does the system have infinitely many solutions?

**Answer format:** Integer.

### Q28. [1 Mark] [NAT]

A ticket lock stores next-ticket and currently-served ticket numbers modulo eight. Every new contender obtains the next ticket and advances that counter atomically, then enters when its ticket equals the currently-served value. The owner has not yet released the lock and no previously issued ticket has completed. What is the smallest total number of outstanding contenders, including the current owner, that can give another contender the owner's ticket through counter wraparound?

**Answer format:** Integer.

### Q29. [1 Mark] [NAT]

A byte-addressed 16-bit address bus interfaces an 8 KiB memory chip. Chip inputs A0 through A12 connect to the corresponding bus lines. The chip is selected exactly when A15=1 and A14=0; A13 is not decoded. How many distinct CPU byte addresses access the same physical byte of this chip?

**Answer format:** Exact integer.

### Q30. [1 Mark] [NAT]

A memory system has a 2 ns cache lookup time and a 5% miss rate. A miss adds 60 ns after the cache lookup, with no overlap. What is the average memory access time?

**Answer format:** Integer nanoseconds.

### Q31. [1 Mark] [MCQ]

For every real x, define f(x)=|x-1|+|x+1| and g(x)=f(f(x)-3). At exactly which points is g not differentiable?

A. x=-1 and x=1 only  
B. x=-2,-1,1,2  
C. x=-2 and x=2 only  
D. At no real point

### Q32. [1 Mark] [NAT]

A NAT can allocate public ports4000 through4007 inclusive on each of two public IPv4 addresses. Each simultaneous mapping consumes a distinct(public address,public port) pair, and no reuse is allowed. How many simultaneous mappings can it support?

**Answer format:** Integer.

### Q33. [1 Mark] [NAT]

X takes values 0 and 1, and Y=1−X. If E[X+2Y]=1.7, what is Var(X+2Y)?

**Answer format:** Decimal rounded to two places.

### Q34. [1 Mark] [NAT]

R(A,B)={(1,a),(1,b),(2,a),(3,a),(3,b),(3,c)}. Count A values satisfying: there exist distinct y,z with R(A,y) and R(A,z), and for every w, R(A,w) implies w=y or w=z.

**Answer format:** Integer.

### Q35. [1 Mark] [MSQ]

Functions f:A→B and g:B→C have injective composition g∘f. Which statements necessarily follow?

A. f is injective.
B. g is injective on all of B.
C. g is injective when restricted to f(A).
D. f is surjective onto B.

### Q36. [2 Marks] [MSQ]

A directed weighted graph contains s→a (1), a→b (−2), b→a (1), b→c (4), and s→t (5), with no other edges. Which statements are correct?

A. There is no finite minimum weight among s-to-c walks.
B. The shortest s-to-t path has weight 5.
C. The negative cycle makes every vertex's distance from s equal to minus infinity.
D. c can reach a negative cycle.

### Q37. [2 Marks] [NAT]

A TCP sender's next new data byte has sequence number 5001. Its latest cumulative acknowledgement is ACK=1001, meaning that byte 1001 is next expected. The advertised receive window is 6000 bytes and the congestion window is 8000 bytes.

The sender transmits the maximum permitted amount of new data. It then receives ACK=3001 with an advertised receive window of 3500 bytes and an updated congestion window of 10000 bytes, and again transmits the maximum permitted new data. Finally, it receives ACK=5501 with an advertised receive window of 5000 bytes and an updated congestion window of 4500 bytes, and again sends as much new data as permitted.

There are no other transmissions, acknowledgements or window changes. Each advertised receive window starts at its ACK number. Ignore sequence-number wraparound and segment-size restrictions. Data already sent may lie beyond the right edge of a newly reduced receive window; it remains outstanding. How many new data bytes are transmitted in total across these three sending opportunities?

**Answer format:** Numeric value; integer.

### Q38. [2 Marks] [MSQ]

Let A=[[2,1],[0,2]]. Which statements are correct?

A. A has two linearly independent eigenvectors over the real numbers.
B. A⁵ has diagonal entries32 and32.
C. A⁵−32I has rank1.
D. A⁵=32I.

### Q39. [2 Marks] [MSQ]

In a connected undirected weighted graph, an edge e is the unique heaviest edge of a cycle. Which statements are correct?

A. e belongs to every MST.
B. e belongs to no MST.
C. Deleting e leaves the graph connected.
D. The conclusion in B remains valid with “unique heaviest” replaced by merely “one of the heaviest”.

### Q40. [2 Marks] [MSQ]

Consider exact integer arithmetic and the following code. The condition may be either true or false; no operations have hidden side effects.

```text
p = a+b
if condition:
    a = a+1
    t = a+b
else:
    t = p
z = a+b
```

Which statements hold for arbitrary initial a,b?

A. The final right-hand side can always be replaced by p.
B. The final right-hand side can always be replaced by t.
C. On both incoming paths, t equals the current a+b at the join.
D. The final right-hand side can always be replaced by p+1.

### Q41. [2 Marks] [MSQ]

A Banker's-algorithm system has two resource types. Current available resources are (1,1). Allocation and remaining need are:

| Process | Allocation | Remaining need |
|---|---|---|
| P0 | (1,0) | (1,2) |
| P1 | (0,1) | (2,0) |
| P2 | (1,1) | (1,1) |

Consider each request independently from the displayed state. Which statements are correct?

A. The current state has exactly two safe process-completion orders.  
B. Granting P0's request (1,0) would make the state unsafe.  
C. Granting P1's request (1,0) leaves a safe state.  
D. Granting P2's request (1,0) leaves a safe state.

### Q42. [2 Marks] [NAT]

For grammar S→SS | a, how many distinct parse trees generate the word aaaa? Left and right children are ordered; different orders of expanding nodes in the same tree do not create different trees.

**Answer format:** Integer.

### Q43. [2 Marks] [NAT]

Insert the distinct keys8,4,12,2,6,10,14,5,7 into an initially empty binary search tree, without balancing. Delete key8 by copying its inorder predecessor into its node and then deleting the predecessor's original node. What is the sum of the keys compared with the target during a successful ordinary BST search for5 in the resulting tree, including5 itself?

**Answer format:** Integer.

### Q44. [2 Marks] [MSQ]

Let L be recognized by a Turing machine that may loop on nonmembers. A second machine enumerates all strings, simulates the recognizer on them by dovetailing, and prints a string when its simulation accepts. Which statements are correct?

A. Every member of L is eventually printed.
B. The enumerator must halt when L is finite.
C. If L is empty, the enumerator may run forever without printing anything.
D. Waiting for a fixed input to appear in this enumeration decides membership in L for every recognizable L.

### Q45. [2 Marks] [NAT]

On the interval[−2,2], how many distinct x values attain the global maximum of |x³−3x|?

**Answer format:** Integer.

### Q46. [2 Marks] [NAT]

Use set relational algebra. Relation E(X,Y) contains(a,b),(a,c),(b,c),(c,c). Form pairs(X,Z) for which some Y satisfies E(X,Y) and E(Y,Z), project away Y, then subtract E after renaming its second attribute to Z. How many tuples remain?

**Answer format:** Exact integer.

### Q47. [2 Marks] [MSQ]

A directed graph has edges s→a of weight 2, s→b of weight 5, b→a of weight −4, a→t of weight 3 and b→t of weight 1. A standard Dijkstra implementation finalizes vertices in increasing tentative-distance order, breaks the a/b/t ties by choosing t before b, never reopens a finalized vertex, and stops when t is finalized. Which statements are true?

A. The true shortest s-to-t distance is 5.
B. The true shortest s-to-t distance is 4.
C. This graph contains a negative directed cycle.
D. The specified implementation returns 5.

### Q48. [2 Marks] [NAT]

An urn initially contains one red and one blue ball. Draw a ball uniformly, replace it, and add one extra ball of the same color. Then draw a second ball uniformly from the three balls now present. Given that the second ball is red, what is the probability that the first was blue?

**Answer format:** Decimal rounded to four places.

### Q49. [2 Marks] [NAT]

An eight-input Boolean function is the parity of all eight inputs. Only two-input XOR gates are available. Every gate has unit delay and unlimited fanout; wire delay is zero. Among circuits with the minimum possible number of XOR gates, what is the minimum worst-case input-to-output delay?

**Answer format:** Integer gate delays.

### Q50. [2 Marks] [MSQ]

An application sends two messages over one TCP connection, adding no lengths, delimiters or other framing. The receiver knows neither message length. Which statements are correct?

A. TCP's ordered delivery alone identifies the boundary between the messages.
B. The same received byte string may correspond to more than one split into two messages.
C. A protocol-level length field can make boundaries recoverable.
D. One send call necessarily corresponds to one recv call.

### Q51. [2 Marks] [MSQ]

Relation R(A,B) has primary key A and a CHECK constraint `B > 0`, with B allowed to be NULL. Under ordinary SQL CHECK semantics, a row is rejected by CHECK only when the condition is FALSE. Which insertions can satisfy these constraints if A is a fresh non-NULL key each time?

A. B=3
B. B=NULL
C. B=0
D. B=−2

### Q52. [2 Marks] [MSQ]

A lexer uses maximal munch with tokens HEX=0x[0-9A-F]+ and ID=[A-Z]+. No rule requires whitespace between tokens. On the input0x1G, which statements are correct?

A. The lexer can return HEX with lexeme0x1 followed by ID with lexemeG.
B. The entire input must be one valid HEX token because it starts with0x.
C. Successful tokenization alone does not prove that the token sequence is a valid expression in the parser's grammar.
D. G is a valid hexadecimal digit under the given HEX rule.

### Q53. [2 Marks] [NAT]

A two-way cache has two sets, initially empty, with LRU replacement. The memory-block reference sequence is 0,2,4,0,2,4. Compare mapping I, set index equal to block-address bit 0, with mapping II, set index equal to bit 0 XOR bit 1. Block bits are numbered from zero at the least significant end. How many fewer misses occur with mapping II?

**Answer format:** Integer.

### Q54. [2 Marks] [NAT]

A device transfers 12,000 bytes in one second. With interrupt-driven I/O, each byte causes an interrupt costing 80 CPU cycles. With DMA, one completion interrupt occurs per 1,000-byte block at a cost of 120 CPU cycles, plus 30 setup cycles per block; ignore all other CPU work and bus stalls. How many CPU cycles are saved by DMA during that second?

**Answer format:** Integer.

### Q55. [2 Marks] [NAT]

Nonpreemptive shortest-job-first scheduling handles jobs J1,J2,J3 with arrival times 0,1,2 and CPU bursts 5,2,1. Context switching costs zero. What is their mean turnaround time? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q56. [2 Marks] [MSQ]

Let L={a^n b^n : n≥0}, and define K={w : there exists z in b* such that wz is in L}. Which statements are correct?

A. aaab belongs to K.
B. abb belongs to K.
C. K is context-free.
D. K is regular.

### Q57. [2 Marks] [NAT]

A disk head is at cylinder50. Three requests target55,30,80. Seek time is one time unit per cylinder. Their additional rotational waits after reaching the target are respectively50,0,0 time units; transfer times are equal and may be ignored. How much larger is the first-request service time selected by shortest-seek-time-first than the smallest available first-request service time?

**Answer format:** Integer time units.

### Q58. [2 Marks] [NAT]

In the subset lattice of {a,b,c}, let X={a,b} and Y={b,c}. How many subsets Z satisfy X∩Y⊆Z⊆X∪Y and are incomparable with both X and Y under inclusion?

**Answer format:** Integer.

### Q59. [2 Marks] [NAT]

For R(A,B,C), dependencies are A→B and B→C. How many of the seven nonempty subsets of{A,B,C} are superkeys?

**Answer format:** Integer.

### Q60. [2 Marks] [NAT]

An HTTP cache has a stored response with an entity tag. On revalidation the server returns a304 response with no representation body, confirming that the stored representation is usable. The representation is5000 bytes, and the304 response is200 bytes. Ignoring the request and all other overhead, how many response bytes are saved compared with a full response of5200 bytes?

**Answer format:** Integer.

### Q61. [2 Marks] [NAT]

A five-stage scalar pipeline uses IF,ID,EX,MEM,WB, one cycle per stage, and has full forwarding except that a load's result becomes available only at the end of MEM. The sequence is load r1,[a]; add r2,r1,r3; add r4,r2,r5. With separate instruction/data memories and no other stalls, how many cycles are required from the first IF through the last WB?

**Answer format:** Integer.

### Q62. [2 Marks] [NAT]

A synchronous machine has one state bit q, initially0. For input bit x, it emits y=q XOR x and then updates q=x at the clock edge. On input sequence110101, how many emitted bits are1?

**Answer format:** Exact integer.

### Q63. [2 Marks] [MSQ]

An undirected weighted graph has a cycle whose edge weights are 1,2,2,5. Other edges may exist. Which statements necessarily hold?

A. The weight-5 edge on this cycle belongs to no minimum spanning tree of a connected graph containing it.
B. Every weight-2 edge on the cycle belongs to no minimum spanning tree.
C. Removing that weight-5 edge preserves connectivity of its original connected component.
D. The minimum spanning tree is necessarily unique.

### Q64. [2 Marks] [NAT]

The exact value −1.375 is rounded to a signed fixed-point format with two fractional bits and sufficient integer range. Rounding is to nearest, ties to an even encoded integer. What real value is stored?

**Answer format:** Exact finite decimal.

### Q65. [2 Marks] [NAT]

An undirected simple graph has 64 vertices and m edges. Compare a bit-packed adjacency matrix of exactly 64² bits with an adjacency-list representation using 32 bits for each of 65 header/offset entries and 16 bits for each of the 2m neighbour entries. Ignore all other overhead. What is the smallest integer m for which the matrix occupies strictly less storage than these lists?

**Answer format:** Integer.

---

## ANSWER KEY — MOCK TEST 097

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | C |
| 2 | NAT | 1 | 10 |
| 3 | MSQ | 1 | B, D |
| 4 | NAT | 1 | 20 |
| 5 | MCQ | 1 | B |
| 6 | NAT | 2 | 84 |
| 7 | NAT | 2 | 10 |
| 8 | NAT | 2 | 12 |
| 9 | MCQ | 2 | C |
| 10 | NAT | 2 | 18 |
| 11 | MSQ | 1 | A, C |
| 12 | NAT | 1 | 3 (exact) |
| 13 | MSQ | 1 | A, C |
| 14 | NAT | 1 | 4 |
| 15 | MSQ | 1 | A, C, D |
| 16 | NAT | 1 | 3 |
| 17 | NAT | 1 | 3 |
| 18 | NAT | 1 | 3 |
| 19 | MSQ | 1 | A, B |
| 20 | MSQ | 1 | B, C |
| 21 | MCQ | 1 | B |
| 22 | MSQ | 1 | A, C |
| 23 | NAT | 1 | 96 |
| 24 | MSQ | 1 | B, C |
| 25 | MSQ | 1 | A, B |
| 26 | NAT | 1 | 5 |
| 27 | NAT | 1 | 2 |
| 28 | NAT | 1 | 9 |
| 29 | NAT | 1 | 2 |
| 30 | NAT | 1 | 5 |
| 31 | MCQ | 1 | C |
| 32 | NAT | 1 | 16 |
| 33 | NAT | 1 | 0.21 (two decimals) |
| 34 | NAT | 1 | 1 |
| 35 | MSQ | 1 | A, C |
| 36 | MSQ | 2 | A, B |
| 37 | NAT | 2 | 5000 (exact) |
| 38 | MSQ | 2 | B, C |
| 39 | MSQ | 2 | B, C |
| 40 | MSQ | 2 | B, C |
| 41 | MSQ | 2 | A, B, D |
| 42 | NAT | 2 | 5 |
| 43 | NAT | 2 | 22 |
| 44 | MSQ | 2 | A, C |
| 45 | NAT | 2 | 4 |
| 46 | NAT | 2 | 0 |
| 47 | MSQ | 2 | B, D |
| 48 | NAT | 2 | 0.3333 (accepted range 0.33325–0.33335) |
| 49 | NAT | 2 | 3 |
| 50 | MSQ | 2 | B, C |
| 51 | MSQ | 2 | A, B |
| 52 | MSQ | 2 | A, C |
| 53 | NAT | 2 | 3 |
| 54 | NAT | 2 | 958200 |
| 55 | NAT | 2 | 5.3333 (range 5.33325–5.33335) |
| 56 | MSQ | 2 | A, C |
| 57 | NAT | 2 | 35 |
| 58 | NAT | 2 | 0 |
| 59 | NAT | 2 | 4 |
| 60 | NAT | 2 | 5000 |
| 61 | NAT | 2 | 8 |
| 62 | NAT | 2 | 5 |
| 63 | MSQ | 2 | A, C |
| 64 | NAT | 2 | -1.5 |
| 65 | NAT | 2 | 64 |
