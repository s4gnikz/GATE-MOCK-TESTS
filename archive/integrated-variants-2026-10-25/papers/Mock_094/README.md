# GATE CS 2027 — Full-Length Mock Test 094

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

A rule says, “A consignment will be released only if it is inspected, unless it is exempt.” Which situation necessarily violates the rule?

A. An exempt consignment is released without inspection.
B. A nonexempt consignment is inspected but not released.
C. A nonexempt consignment is released without inspection.
D. An exempt consignment is inspected before release.

### Q2. [1 Mark] [NAT]

A planar figure consists of the three labelled points A=(0,0), B=(2,0), C=(0,1). It is reflected in the line y=x and then translated by(1,−1). What is the x-coordinate of the image of C minus the y-coordinate of the image of B?

**Answer format:** Integer.

### Q3. [1 Mark] [MCQ]

Read the statement: “When the library extended its hours, evening visits increased. Total daily visits stayed unchanged because morning visits fell by the same amount. The data alone do not establish whether additional people began using the library.” Which inference is supported?

A. Every new evening visitor was previously a morning visitor.
B. The number of distinct users increased.
C. The distribution of visits across the day changed.
D. Extending hours caused no benefit to any visitor.

### Q4. [1 Mark] [NAT]

Five distinct books A,B,C,D,E are placed in a row. A must appear somewhere before B, and C and D must not be adjacent. How many arrangements satisfy both conditions?

**Answer format:** Integer.

### Q5. [1 Mark] [NAT]

Of200 survey invitations,120 recipients responded. Of these respondents,75% supported a proposal. What is the smallest possible percentage of all200 invited recipients who supported the proposal, counting each person's view whether or not they responded?

**Answer format:** Percentage number, without the percent symbol.

### Q6. [2 Marks] [MSQ]

A cube net consists of unit squares on a square grid. Labelled square centres are A=(0,0), B=(1,0), C=(2,0), D=(1,1), E=(1,2), F=(1,−1). Adjacent grid squares share an edge. Fold the net into a cube. Which listed pairs of faces share an edge on the cube?

A. A and E  
B. A and C  
C. E and F  
D. B and E

### Q7. [2 Marks] [MCQ]

Arrange the following troubleshooting steps coherently: P, verify that the replacement resolves the fault; Q, isolate the faulty component using measurements; R, replace the isolated component; S, observe and record the original symptom.

A. S–Q–R–P
B. Q–P–S–R
C. R–S–P–Q
D. P–Q–R–S

### Q8. [2 Marks] [NAT]

An urn contains two red and two blue balls. Balls are drawn uniformly without replacement until the first red ball appears. Given that the procedure stopped within the first two draws, what is the probability that it stopped on the first draw?

**Answer format:** Exact finite decimal.

### Q9. [2 Marks] [MCQ]

“The panel described the evidence as suggestive rather than conclusive; its recommendation was consequently provisional.” Which revision preserves both the strength of the evidence and the status of the recommendation?

A. The evidence proved the claim, so the recommendation was final.
B. The evidence offered some support, so the recommendation remained open to revision.
C. The evidence disproved the claim, so the recommendation was withdrawn.
D. The evidence was irrelevant, so the recommendation was unanimous.

### Q10. [2 Marks] [NAT]

A population starts at 800, increases by 25% in the first year, decreases by 20% in the second, and increases by 10% in the third. What constant annual percentage growth rate over the same three years gives the same final population? Round to two decimal places.

**Answer format:** Number to 2 decimal places, without the percent sign.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MSQ]

A connected weighted undirected graph has a vertex v incident to exactly one edge e. Edge weights may be negative or equal. Which statements necessarily hold?

A. Every spanning tree contains e.
B. Every minimum spanning tree contains e.
C. e must be the minimum-weight edge in the entire graph.
D. Removing e leaves a connected graph.

### Q12. [1 Mark] [MSQ]

A pushdown automaton accepts by final state after consuming its entire input. A proposed modification erases all its stack symbols immediately whenever it first enters any final state, then continues with the original transitions. The original transitions may depend on the stack top. Which statements are correct?

A. The modification can destroy an accepting computation that must leave a final state and read further input.
B. The modification always preserves the accepted language.
C. Entering a final state before input exhaustion does not by itself accept the input.
D. Every final state in every pushdown automaton must have no outgoing transitions.

### Q13. [1 Mark] [NAT]

A directed graph with five vertices has eight edges and no self-loops. In an adjacency-list representation storing each directed edge once, how many edge entries are stored, excluding vertex headers?

**Answer format:** Integer.

### Q14. [1 Mark] [NAT]

A2×2 real matrix has eigenvalues3 and−1. What is trace(A²)?

**Answer format:** Exact number.

### Q15. [1 Mark] [MSQ]

In a basic block, t=a+b is computed, then a store through pointer p occurs, then u=a+b is computed. The scalar values a,b reside in memory and p may alias them. Arithmetic is exact and has no side effects. Which statements are correct?

A. Reusing t for u without alias information can be unsound.
B. Proving the store cannot change a or b permits reuse in this block.
C. Identical expression text alone guarantees equal values across the store.
D. Recomputing a+b after the store preserves the required new operand values.

### Q16. [1 Mark] [NAT]

A real polynomial f has five distinct real roots. What is the minimum number of distinct real roots that its second derivative f'' must have?

**Answer format:** Integer.

### Q17. [1 Mark] [MCQ]

A direct-mapped cache has four lines. Block b maps to line b mod 4. Which pair of distinct blocks can coexist in this cache?

A. 1 and 5
B. 2 and 6
C. 3 and 7
D. 4 and 5

### Q18. [1 Mark] [MSQ]

Two threads acquire initially free nonrecursive mutexes A and B. Thread P acquires A then B; thread Q acquires B then A. Each releases both only after acquiring both. Which statements are correct?

A. A deadlock is possible.
B. Every interleaving deadlocks.
C. Changing Q to acquire A then B eliminates deadlock in this two-thread, two-mutex program.
D. Releasing a mutex immediately after acquiring it preserves the original protection of a critical section that requires both mutexes together.

### Q19. [1 Mark] [NAT]

A fair coin and a double-headed coin are selected with equal probability. The selected coin is tossed twice and both outcomes are heads. What is the probability that a third toss of the same coin is heads?

**Answer format:** Exact finite decimal.

### Q20. [1 Mark] [NAT]

In C, assume unsigned int has exactly16 value bits and arithmetic on it is modulo65536. What value is printed?

```c
unsigned int x = 65535u;
unsigned int y = x + 2u;
printf("%u", y);
```

**Answer format:** Integer.

### Q21. [1 Mark] [NAT]

An application sends 2400 bytes using three UDP datagrams, each with 800 application bytes. Each datagram adds an 8-byte UDP header and a 20-byte IPv4 header. No fragmentation occurs. How many total IPv4 bytes are transmitted?

**Answer format:** Integer.

### Q22. [1 Mark] [MCQ]

For relation R(A,B,C), consider F={A→B, A→C, B→C}. Which is a minimal cover with singleton right-hand sides equivalent to F?

A. {A→B, B→C}
B. {A→C, B→C}
C. {A→B, A→C}
D. {A→BC}

### Q23. [1 Mark] [NAT]

Two packets of 1000 bits each are ready at time 0 and travel through three store-and-forward links in order. Their rates are 2 Mbit/s, 1 Mbit/s and 2 Mbit/s, respectively; 1 Mbit=10^6 bits. Each link transmits only one packet at a time, buffers are sufficient, and propagation and processing delays are zero. Packets retain their order. Each link begins transmitting as soon as both the packet and that link are available. At what time, in milliseconds, does the last bit of the second packet reach the destination?

**Answer format:** Numeric value; integer.

### Q24. [1 Mark] [MSQ]

Let L be a context-free language over {a,b}. Define h(a)=01 and h(b)=epsilon. Let R be a regular language over {0,1}. Which languages must be context-free?

A. h(L)
B. h(L) intersect R
C. The complement of L over {a,b}*
D. L intersect {a}*

### Q25. [1 Mark] [NAT]

A directed graph has edges s→a of weight2, s→b of weight5, b→a of weight−4 and a→t of weight2. There are no other edges. A flawed Dijkstra implementation permanently settles vertices and refuses to update a settled vertex. Starting at s, by how much does its reported distance to t exceed the true shortest-path distance?

**Answer format:** Integer.

### Q26. [1 Mark] [MSQ]

A partially ordered set has elements0,a,b,1, with0<a<1 and0<b<1; a and b are incomparable. Which statements are correct?

A. a and b have meet0 and join1.
B. The poset is a total order.
C. The poset is a lattice.
D. There is no upper bound of both a and b.

### Q27. [1 Mark] [MCQ]

A byte-addressed 4 KiB window maps to a 2 KiB memory chip. Address bits A10–A0 reach the chip; A11 is ignored and the chip is selected throughout the window 0x000–0xFFF. Which other address accesses the same stored byte as 0x134?

A. 0x135
B. 0x234
C. 0x534
D. 0x934

### Q28. [1 Mark] [NAT]

A has rows (2,1),(6,5). In its factorization A=LU without row swaps, L is lower triangular with unit diagonal and U is upper triangular. Find L21+U22.

**Answer format:** Integer.

### Q29. [1 Mark] [NAT]

A binary error-detecting code consists of all four-bit words having even parity. A valid transmitted word suffers exactly two distinct bit flips. How many of the six possible error-position pairs are detected by an even-parity check?

**Answer format:** Integer.

### Q30. [1 Mark] [MSQ]

A segment has byte offsets 0 through 5999. It is paged using 4096-byte pages, with both required pages present. Segment bounds are checked independently of page presence. Which statements are correct?

A. Offset 5000 is valid and uses page 1 with offset 904.  
B. Offset 7000 is valid because page 1 is present.  
C. Offset 5999 is the last valid byte.  
D. Allocating the second page automatically enlarges the segment to 8192 bytes.

### Q31. [1 Mark] [MSQ]

For a unary relation R(x), compare tuple-calculus expressions E1={t | R(t)} and E2={t | NOT R(t)}. Values of t range over an external domain containing the active domain of R. Which statements are correct?

A. E1 is unchanged if the external domain is enlarged without changing R.
B. E2 is unchanged under every such enlargement.
C. E2 can gain tuples when the external domain is enlarged.
D. E1 necessarily returns every element of the external domain.

### Q32. [1 Mark] [MCQ]

An eight-bit two's-complement negation computes the low eight bits of NOT x plus 1. For which input is the signed result equal to the signed input even though the mathematical negation is not representable?

A. 00000000
B. 01111111
C. 11111111
D. 10000000

### Q33. [1 Mark] [MCQ]

Records (key,id) occur initially as(1,A),(1,B),(2,C). They are stably sorted by ascending key and the whole resulting array is then reversed. Relative to the original input, is this a stable descending-key sort?


A. No, because A and B appear in the opposite order.
B. Yes, because reversing always preserves equal-key order.
C. No, because key2 appears before key1.
D. Yes, because the ascending sort was stable.

### Q34. [1 Mark] [NAT]

A cache miss fetches eight consecutive words. The memory returns the first requested word after 12 cycles and each subsequent word one cycle later. The CPU needs word offset 6 of the line. Compare a fill starting at offset 0 and proceeding in increasing order with critical-word-first delivery starting at offset 6. The CPU resumes as soon as its requested word arrives. How many cycles earlier can it resume with critical-word-first delivery?

**Answer format:** Integer.

### Q35. [1 Mark] [MCQ]

Let F(x,y,z)=x XOR (y AND z). Define D(x,y,z)=F(x,y,z) XOR F(x,NOT y,z). Which expression equals D for every Boolean input?

A. x  
B. y  
C. z  
D. NOT z

### Q36. [2 Marks] [NAT]

Evaluate the integral from0 to2 of |x²−1| with respect to x.

**Answer format:** Exact number.

### Q37. [2 Marks] [NAT]

The five observations are0,1,2,3,t, where t is a real number constrained by t≥3. What is the minimum population variance of these five observations?

**Answer format:** Exact decimal.

### Q38. [2 Marks] [MSQ]

A process successfully executes a new program image through an exec-like operation with the following specified semantics: its PID is retained, its old address space is replaced, and descriptors marked close-on-exec are closed while others remain open. Which observations are possible immediately afterwards?

A. The PID is unchanged although the executed code is different.
B. An unmarked file descriptor remains usable by the new program.
C. Every pointer into the old heap is guaranteed to remain valid with its old object.
D. Every inherited descriptor must have been closed.

### Q39. [2 Marks] [NAT]

A recursive procedure enumerates subsets of positions 1 through 5 with no two adjacent positions selected. At each position, it always makes a recursive call excluding that position. It also makes a call including it if the previous position was not selected. After position 5 it outputs once and returns. The initial call handles position 1 with no previous position selected. How many nonleaf calls occur, counting separate calls even when their remaining-position arguments coincide?

**Answer format:** Integer.

### Q40. [2 Marks] [NAT]

An idealized half-duplex CSMA/CD link connects two stations 2400 m apart. Propagation speed is 2×10^8 m/s and the bit rate is 100 Mb/s, where 1 Mb/s = 10^6 bits/s. Detection circuitry adds 2 microseconds after the collision disturbance reaches a transmitting station. Ignore all other delays and framing overhead. A sender must still be transmitting when a worst-case collision is detected. Under the model, what is the minimum integer frame length in bytes? Treat the worst-case round-trip propagation bound as inclusive.

**Answer format:** Numeric value; integer.

### Q41. [2 Marks] [NAT]

A uniformly random permutation of {1,2,3,4,5} is chosen. Given that 1 is not fixed, what is the probability that the permutation has exactly one fixed point?

**Answer format:** Exact finite decimal.

### Q42. [2 Marks] [NAT]

A three-variable Boolean function has1-minterms {0,2,6}, don't-care minterms {4}, and0-minterms {1,3,5,7}. A is the most significant bit and C the least significant. After obtaining a minimum-literal SOP, what value does that implementation assign to minterm 4?

**Answer format:** Exact integer,0 or1.

### Q43. [2 Marks] [MCQ]

For the finite language L={ε,a,a²,…,a⁷}, what is the smallest positive pumping length p satisfying the regular-language pumping lemma? The lemma imposes its decomposition requirement only on words of length at least p.

A. 8
B. 7
C. 1
D. No pumping length exists because the language is finite.

### Q44. [2 Marks] [MSQ]

In a finite directed network, every link has strictly positive cost and every router can reach destination d. Each router u other than d selects any outgoing neighbour v satisfying dist(u,d)=cost(u,v)+dist(v,d), using exact shortest-path distances. Different routers may break equal-cost ties independently. Which statements are correct?

A. The selected next-hop graph can contain a directed cycle because tie-breaking is independent.
B. Distance to d strictly decreases at each selected hop.
C. Every packet following these next hops eventually reaches d.
D. Allowing zero-cost links would leave the strict-decrease argument unchanged.

### Q45. [2 Marks] [MCQ]

R(A,B,C) has dependencies AB→C and C→B. Which statement is correct?

A. Its only candidate key is AB and it is in BCNF.
B. Its candidate keys are AB and AC; it is in 3NF but not BCNF.
C. Every attribute is a candidate key by itself.
D. It fails 3NF because B is not prime.

### Q46. [2 Marks] [NAT]

A direct-mapped cache has two 16-byte lines, is initially empty, and uses write-back with write allocation. Arrays A and B each contain four four-byte words. A begins at byte address 0 and B at byte address 32. Execute, for i=0,1,2,3, in this order: read A[i], write B[i], read A[i]. Each miss transfers one whole block from memory; each dirty eviction writes one whole block to memory. Ignore all other traffic and do not flush the cache afterwards. How many bytes are transferred between cache and memory in total?

**Answer format:** Integer.

### Q47. [2 Marks] [NAT]

In a four-variable Boolean minimization problem, the only ON minterms are 0,1,2,3 and the only don't-care minterms are 8,9,10,11. All remaining minterms are OFF. Variables are a,b,c,d from most to least significant. What is the minimum number of literals in a single product term covering every ON minterm without covering an OFF minterm?

**Answer format:** Integer.

### Q48. [2 Marks] [MSQ]

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

### Q49. [2 Marks] [MSQ]

A Turing machine M is promised to halt on every input. A proposed procedure enumerates input strings and simulates M on each until it finds an accepted input. Which statements are correct?

A. If L(M) is nonempty, this sequential procedure eventually finds an accepted input.
B. If L(M) is empty, the procedure eventually proves emptiness just by reaching a sufficiently long rejected input.
C. Totality of M makes each individual simulation finish.
D. The promise supplies a finite maximum length beyond which no new accepted input can occur.

### Q50. [2 Marks] [NAT]

A simple graph consists of two vertex-disjoint triangles, with one additional edge joining one vertex of the first triangle to one vertex of the second. How many proper colorings using three labeled colors does the graph have?

**Answer format:** Exact integer.

### Q51. [2 Marks] [NAT]

A translation for binary strings uses S→S b | b, where b is a terminal0 or1. At S→b, set S.value=b and S.length=1. At S→Sleft b, set S.value=Sleft.value+b×2^(Sleft.length) and S.length=Sleft.length+1. What value is computed for terminal string10110?

**Answer format:** Exact integer.

### Q52. [2 Marks] [NAT]

A chained hash table has three buckets containing respectively 1,2,3 distinct keys. All six keys are equally likely targets of a successful search, and each chain is searched from its head. What is the expected number of key comparisons? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q53. [2 Marks] [NAT]

A16-to-1 multiplexer is built entirely from2-to-1 multiplexers arranged as a binary selection tree, without sharing data inputs between tree branches. How many2-to-1 multiplexers are required?

**Answer format:** Integer.

### Q54. [2 Marks] [MSQ]

An inode contains four direct pointers, one single-indirect pointer and one double-indirect pointer. A block is 1024 bytes and each pointer is 4 bytes. Indirect blocks contain only pointers. A nonsparse file contains exactly 263 completely full data blocks, numbered logically from 0. Allocate only the indirect blocks needed for these data blocks. The inode is already in memory. Which statements are correct?

A. Exactly three indirect blocks are allocated.  
B. With no other blocks cached, reading the data in logical block 260 requires three block reads, including the data block.  
C. Logical block 259 is reached through the double-indirect pointer.  
D. The file contains 269312 bytes of data.

### Q55. [2 Marks] [MSQ]

A contiguous row-major array A has3 rows and5 columns of four-byte elements, without padding. A transpose view B has5 rows and3 columns and maps B[i,j] to A[j,i], without copying data. Which statements are correct?

A. Increasing i by1 at fixed j advances the element address by4 bytes.
B. Increasing j by1 at fixed i advances the element address by20 bytes.
C. B is contiguous in its own row-major traversal order.
D. Writing B[2,1] changes the same stored element as A[1,2].

### Q56. [2 Marks] [NAT]

An IPv4 receiver obtains three fragments of one original datagram. Their (fragment offset,payload length,MF) triples are(0,400,1),(75,200,1),(100,120,0). Offsets are in standard IPv4 units; all payload lengths are in bytes. No other fragments have arrived. How many original payload bytes are still missing?

**Answer format:** Exact integer.

### Q57. [2 Marks] [MCQ]

A lexically scoped language has procedure P with local x=10. Procedures Q and S are declared directly inside P. Q has its own local x=20 and declares R inside Q. S increments its lexically nearest x and returns that x. During one activation of P, Q calls R, and R calls S twice in sequence. What is the sum of S's returned values?

A. 21
B. 23
C. 43
D. 40

### Q58. [2 Marks] [MCQ]

A regular file contains bytes ABCDE. Descriptor p opens it at offset zero; q=dup(p); descriptor r comes from a separate open of the same file, also at zero. With no intervening operations, execute read(p,2), read(q,1), seek(r,1 from start), read(r,2), read(p,1). All reads succeed fully. What are the byte strings from the four reads in order?

A. AB; A; BC; A
B. AB; C; BC; E
C. AB; C; DE; D
D. AB; C; BC; D

### Q59. [2 Marks] [NAT]

During a 1000-cycle interval, a DMA controller steals one memory-bus cycle in every group of five cycles. A CPU instruction stream requires the bus every cycle and otherwise could complete one instruction per cycle. Assume a stolen cycle stalls exactly one instruction opportunity, with no other stalls. How many instructions complete during the interval?

**Answer format:** Integer.

### Q60. [2 Marks] [NAT]

How many binary strings of length 6 contain exactly two occurrences of the substring 01? Occurrences are counted by their starting positions.

**Answer format:** Exact integer.

### Q61. [2 Marks] [MCQ]

For n a positive perfect square, determine the tight asymptotic number of loop iterations as n grows. Arithmetic and floor-square-root evaluation each take constant time.

```text
i = 1
while i < n:
    i = i + floor(sqrt(i))
```

A. Θ(log n)
B. Θ(n)
C. Θ(n log n)
D. Θ(sqrt(n))

### Q62. [2 Marks] [NAT]

A system has three page frames and initially no resident pages. It uses optimal replacement with knowledge of the future. For references 1,2,3,4,1,2,5,1,2,3,4,5, how many page faults occur?

**Answer format:** Integer.

### Q63. [2 Marks] [NAT]

A five-stage pipeline has stage logic delays 1,2,3,4,5 ns and a 0.2 ns latch overhead per stage. Its longest stage is split into two 2.5 ns logic stages, producing six stages. Both designs issue one instruction per cycle without hazards. For a batch of twenty instructions starting with an empty pipeline, what is the ratio of old completion time to new completion time? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q64. [2 Marks] [MCQ]

The available closed intervals are [0,4], [3,8], [7,10], [0,6], [6,9], [8,10]. Starting at 0, a greedy covering algorithm repeatedly chooses, among intervals beginning at or before the current covered endpoint, an interval extending that endpoint farthest. It stops when [0,10] is covered. Which sequence does it select?

A. [0,4], [3,8], [8,10]
B. [0,6], [6,9], [8,10]
C. [0,6], [7,10]
D. [0,4], [7,10]

### Q65. [2 Marks] [NAT]

A ternary relationship T(Student,Course,Tutor) has tuples(0,0,0),(0,1,1),(1,0,1),(1,1,0). A designer replaces it by the three binary relationship projections onto(Student,Course),(Student,Tutor),(Course,Tutor). How many additional ternary tuples appear when those projections are naturally joined, beyond the four original tuples?

**Answer format:** Integer.

---

## ANSWER KEY — MOCK TEST 094

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | C |
| 2 | NAT | 1 | 1 |
| 3 | MCQ | 1 | C |
| 4 | NAT | 1 | 36 (exact) |
| 5 | NAT | 1 | 45 |
| 6 | MSQ | 2 | A, C |
| 7 | MCQ | 2 | A |
| 8 | NAT | 2 | 0.6 |
| 9 | MCQ | 2 | B |
| 10 | NAT | 2 | 3.23 (range 3.225–3.235) |
| 11 | MSQ | 1 | A, B |
| 12 | MSQ | 1 | A, C |
| 13 | NAT | 1 | 8 |
| 14 | NAT | 1 | 10 |
| 15 | MSQ | 1 | A, B, D |
| 16 | NAT | 1 | 3 |
| 17 | MCQ | 1 | D |
| 18 | MSQ | 1 | A, C |
| 19 | NAT | 1 | 0.9 |
| 20 | NAT | 1 | 1 |
| 21 | NAT | 1 | 2484 |
| 22 | MCQ | 1 | A |
| 23 | NAT | 1 | 3 (exact) |
| 24 | MSQ | 1 | A, B, D |
| 25 | NAT | 1 | 1 |
| 26 | MSQ | 1 | A, C |
| 27 | MCQ | 1 | D |
| 28 | NAT | 1 | 5 |
| 29 | NAT | 1 | 0 |
| 30 | MSQ | 1 | A, C |
| 31 | MSQ | 1 | A, C |
| 32 | MCQ | 1 | D |
| 33 | MCQ | 1 | A |
| 34 | NAT | 1 | 6 |
| 35 | MCQ | 1 | C |
| 36 | NAT | 2 | 2 |
| 37 | NAT | 2 | 1.36 |
| 38 | MSQ | 2 | A, B |
| 39 | NAT | 2 | 19 |
| 40 | NAT | 2 | 325 (exact) |
| 41 | NAT | 2 | 0.375 |
| 42 | NAT | 2 | 1 |
| 43 | MCQ | 2 | A |
| 44 | MSQ | 2 | B, C |
| 45 | MCQ | 2 | B |
| 46 | NAT | 2 | 208 (exact) |
| 47 | NAT | 2 | 1 |
| 48 | MSQ | 2 | A, B, C |
| 49 | MSQ | 2 | A, C |
| 50 | NAT | 2 | 24 |
| 51 | NAT | 2 | 13 |
| 52 | NAT | 2 | 1.6667 (range 1.66665–1.66675) |
| 53 | NAT | 2 | 15 |
| 54 | MSQ | 2 | A, B, D |
| 55 | MSQ | 2 | A, B, D |
| 56 | NAT | 2 | 200 |
| 57 | MCQ | 2 | B |
| 58 | MCQ | 2 | D |
| 59 | NAT | 2 | 800 |
| 60 | NAT | 2 | 21 |
| 61 | MCQ | 2 | D |
| 62 | NAT | 2 | 7 |
| 63 | NAT | 2 | 1.1886 (range 1.18855–1.18865) |
| 64 | MCQ | 2 | B |
| 65 | NAT | 2 | 4 |
