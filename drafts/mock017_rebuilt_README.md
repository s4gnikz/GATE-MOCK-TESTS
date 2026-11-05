# GATE CS 2027 — Full-Length Mock Test 017

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

Q1–Q5 and Q11–Q35 carry one mark each; other questions carry two marks each. MCQs have one correct option and lose one-third of their marks for an incorrect answer. MSQs require every correct option, with no partial credit or negative marking. NATs have no negative marking. Unattempted questions score zero. General Aptitude contributes 15 marks, mathematics 13 and core CS 72. NAT answers are exact unless a rounding format is specified.

## Section A — General Aptitude

### Q1. [1 Mark] [MCQ]

Choose the grammatically correct completion in formal English: “Neither the two applicants nor their supervisor ___ available when the committee ___ its decision yesterday.”

A. were; announce
B. was; announced
C. were; announcing
D. was; announce

### Q2. [1 Mark] [NAT]

Two funds initially contain amounts in the ratio 3:5. Twenty percent of the second fund is transferred to the first. What is the new ratio of the first amount to the second, expressed as a numerical quotient?

**Answer format:** Integer.

### Q3. [1 Mark] [MSQ]

A, B and C finish a race at distinct times. Exactly two of these statements are true: “A finishes before B”; “B finishes before C”; “C finishes before A.” B does not finish last. Which competitors could finish first?

A. A
B. B
C. C
D. None of the three

### Q4. [1 Mark] [MCQ]

Unit cubes form four vertical stacks on a 2×2 footprint, with height rows (1,3) and (2,1). Orthogonal projections onto the horizontal plane and the two vertical coordinate planes count overlapping projected squares only once. What is the sum of the areas of these three projections, in square units?

A. 7
B. 11
C. 12
D. 14

### Q5. [1 Mark] [MCQ]

A report states: “Giving buses priority reduced average passenger delay on the studied corridor, although average car travel time increased. The study did not measure adjacent roads.” Which conclusion is supported?

A. Every traveller's journey became faster.
B. Adjacent roads necessarily became less congested.
C. The reported average passenger benefit can coexist with an increase in average car travel time.
D. Bus priority always reduces delay on every corridor.

### Q6. [2 Marks] [NAT]

Four married couples sit around a circular table. All eight people are distinct; arrangements differing only by rotation are identical, but reflections are distinct. How many arrangements have no spouses adjacent?

**Answer format:** Integer.

### Q7. [2 Marks] [NAT]

Last year, centre A passed 90 of 100 candidates and centre B passed 1 of 10. This year, A passed 19 of 20 and B passed 16 of 80. By how many percentage points did the combined pass percentage fall, despite both centres improving individually? Round to two decimal places.

**Answer format:** Number to 2 decimal places.

### Q8. [2 Marks] [NAT]

A square sheet occupies −4≤x≤4, −4≤y≤4. Fold the lower half over the upper half along y=0, then the left half over the right along x=0. Finally fold the part with x>y across y=x onto x≤y. Punch a small hole centred at (1,3) through all layers, away from all creases. How many distinct hole centres appear after fully unfolding?

**Answer format:** Integer.

### Q9. [2 Marks] [MCQ]

Four events Q,R,S,P occurred at distinct times. Four log entries assert Q before R, R before S, S before P, and P before Q, respectively. Exactly one of these four entries is wrong. An independent reliable record establishes R before P. Which ordering must be true?

A. Q before R.
B. Q before P.
C. S before P.
D. P before R.

### Q10. [2 Marks] [NAT]

An urn contains two red and two blue balls. Balls are drawn uniformly without replacement until the first red ball appears. Given that the procedure stopped within the first two draws, what is the probability that it stopped on the first draw?

**Answer format:** Exact finite decimal.

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

A control ROM is addressed by a two-bit operation code, a three-bit microstep index and two condition bits. Every address combination has a word containing 20 control bits and a seven-bit next address. How many bits does the ROM contain, including unused address combinations?

**Answer format:** Integer.

### Q12. [1 Mark] [MSQ]

For grammar S→aA | aB, A→b, B→c, which statements are true?

A. The two S alternatives conflict in an LL(1) predictive table.
B. The generated language is inherently ambiguous.
C. Replacing the grammar by S→aX, X→b | c gives an LL(1) grammar for the same language.
D. No deterministic parser can recognize the generated language.

### Q13. [1 Mark] [MSQ]

Shared integers x,y start at zero. Thread A performs `x=1; rA=y;` and thread B performs `y=1; rB=x;`. Every displayed read/write is atomic, each thread's order is preserved, and all operations are sequentially consistent. Which final pairs (rA,rB) are possible?

A. (0,1)
B. (0,0)
C. (1,0)
D. (1,1)

### Q14. [1 Mark] [NAT]

R(x,y) contains (1,a),(1,b),(2,a),(3,c), and S contains a,b. Over these domains, how many x values satisfy `(∃y R(x,y)) AND (∀z (R(x,z) → S(z)))`?

**Answer format:** Integer.

### Q15. [1 Mark] [MCQ]

Router A reaches destination D through neighbour B at total cost 5; A also has a direct link to D of cost 8. A currently selects B as next hop. With poisoned reverse, what distance to D does A advertise to B for this selected route?

A. 5
B. 8
C. Infinity
D. The cost of A's link to B only

### Q16. [1 Mark] [MCQ]

A syntax-directed translation emits each operand when recognized and emits a binary operator after translating both operands. Multiplication binds more tightly than addition. What does it emit for a+b*c?

A. ab+c*
B. +a*bc
C. abc*+
D. abc+*

### Q17. [1 Mark] [MCQ]

A byte-addressed 4 KiB window maps to a 2 KiB memory chip. Address bits A10–A0 reach the chip; A11 is ignored and the chip is selected throughout the window 0x000–0xFFF. Which other address accesses the same stored byte as 0x134?

A. 0x135
B. 0x234
C. 0x534
D. 0x934

### Q18. [1 Mark] [MCQ]

On domain {0,1}, let R(x,y) mean x=y. Which pair gives the truth values of ∀x∃y R(x,y) and ∃y∀x R(x,y), in that order?

A. False, false
B. True, false
C. False, true
D. True, true

### Q19. [1 Mark] [NAT]

The coefficient rows of a linear system in three unknowns are (1,1,1), (1,2,3), (2,3,4), and the corresponding right-hand sides are 1,t,3. For what value of t does the system have infinitely many solutions?

**Answer format:** Integer.

### Q20. [1 Mark] [MSQ]

Records have fields name and department. The desired ascending order uses name as primary key and department as secondary key. Which methods guarantee that order for arbitrary input?

A. Stable sort by name, followed by stable sort by department.
B. Stable sort by department, followed by stable sort by name.
C. Sort by department, followed by an arbitrary unstable sort comparing only names.
D. Sort directly with a lexicographic comparator on (name,department).

### Q21. [1 Mark] [MSQ]

An IPv4 fragment has a 20-byte header and MF=1. Which total-length values can meet the eight-byte payload-alignment requirement? Ignore link MTU limits for this question.

A. 532
B. 540
C. 552
D. 556

### Q22. [1 Mark] [NAT]

Eight-bit two's-complement fixed-point words have four fractional bits. Add raw words 0xC8 and 0x34 using eight-bit addition. What real value does the resulting word represent?

**Answer format:** Exact finite decimal, possibly negative.

### Q23. [1 Mark] [NAT]

A binary floating-point format has three significant bits including the leading one, sufficient exponent range, and round-to-nearest with ties-to-even. Starting from the exactly represented value 1, add the exact real number 0.125 twice, rounding after each addition. What is the exact real sum minus the final stored value?

**Answer format:** Exact finite decimal.

### Q24. [1 Mark] [MCQ]

To refute the regular-language pumping condition, which quantifier order must a proof establish? Here p is a positive pumping length, w∈L has length at least p, and a valid split means w=xyz, |xy|≤p, |y|>0; “fails” means xy^i z∉L for i≥0.

A. There exist p,w, a valid split and i that fails.
B. For every p, there exist w and a valid split for which every i fails.
C. There exists p such that every w has a failing split.
D. For every p, there exists w such that every valid split has some i that fails.

### Q25. [1 Mark] [MSQ]

For real x, define f(x)=x when x is rational and f(x)=−x when x is irrational. Which statements are true?

A. f is continuous at zero.
B. f is not differentiable at zero.
C. f is continuous at one.
D. f′(0)=0.

### Q26. [1 Mark] [NAT]

What integer is printed by this C code? All operations are within the array.

```c
int a[] = {2,4,6};
int *p = a;
int x = *p++;
int y = ++*p;
printf("%d", x + y + a[1]);
```

**Answer format:** Integer.

### Q27. [1 Mark] [MSQ]

SQL table R has non-null values 1,2,3 in column x. Table S has values 2 and NULL in column y. Which statements are correct under standard SQL three-valued logic?

A. `SELECT x FROM R WHERE x NOT IN (SELECT y FROM S)` returns no rows.
B. `SELECT x FROM R WHERE NOT EXISTS (SELECT 1 FROM S WHERE S.y=R.x)` returns 1 and 3.
C. `SELECT COUNT(y) FROM S` returns 2.
D. The predicate `NULL=NULL` evaluates to TRUE.

### Q28. [1 Mark] [NAT]

A recursive function is mathematically defined by f(0)=0, f(1)=1 and f(n)=f(n−1)−f(n−2) for n≥2. Find f(2027).

**Answer format:** Integer, possibly negative.

### Q29. [1 Mark] [NAT]

Two independent fair dice give values X,Y. Find E[X | X+Y=7 and X>Y].

**Answer format:** Integer.

### Q30. [1 Mark] [NAT]

A relation on a four-element set is symmetric and transitive but not reflexive. What is the maximum possible number of ordered pairs in the relation?

**Answer format:** Integer.

### Q31. [1 Mark] [NAT]

A parent row P has two child rows C1,C2. C1 has two grandchild rows and C2 has one. Both foreign-key levels use ON DELETE CASCADE; no other rows reference any of these rows. How many rows in total are deleted when P is deleted, including P itself?

**Answer format:** Integer.

### Q32. [1 Mark] [MSQ]

Consider a resource-allocation graph for processes waiting for reusable resources; a resource type may have multiple instances. Which statements hold in the standard model?

A. A deadlock implies a directed cycle.
B. An acyclic graph rules out deadlock.
C. Every directed cycle proves deadlock even with multiple instances per resource type.
D. A cycle-free graph proves every process has already finished.

### Q33. [1 Mark] [MCQ]

Recognizers M and N recognize L and its complement respectively. How can they be used to decide L on input w?

A. Run M to completion before starting N.
B. Accept whenever either machine accepts.
C. Interleave their steps; accept if M accepts and reject if N accepts.
D. Reject immediately unless M accepts in its first step.

### Q34. [1 Mark] [NAT]

A row-major array A[2..4][−1..2] stores four-byte elements with A[2][−1] at address 1000. What is the byte address of A[4][1]?

**Answer format:** Integer.

### Q35. [1 Mark] [MCQ]

An open-addressed hash table uses linear probing and tombstones for deletion. During insertion of key k, the first tombstone is encountered before an occupied slot containing k. Duplicate keys are forbidden. What must a correct insertion do?

A. Immediately place a second copy of k in the tombstone.
B. Treat the tombstone as proof that k is absent.
C. Stop searching at every tombstone as if it were never occupied.
D. Continue searching beyond the tombstone to detect the existing key before deciding to insert.

### Q36. [2 Marks] [NAT]

Singly linked nodes initially form A: 1→2→3→4→null and B: 9→3→4→null, sharing the actual nodes 3 and 4. The A list is reversed in place by changing its nodes' next pointers; B's head pointer is unchanged. What is the sum of node labels encountered from B's head after the reversal?

**Answer format:** Integer.

### Q37. [2 Marks] [MSQ]

Let F(x,y,z)=xy+yz+zx using Boolean AND and OR. Define its Boolean difference with respect to x as F(0,y,z) XOR F(1,y,z). Which statements are correct?

A. The difference equals y+z.
B. The difference equals y XOR z.
C. The difference is independent of x.
D. The difference equals yz.

### Q38. [2 Marks] [NAT]

Over alphabet {a,b}, let L contain exactly the words having exactly one a and length divisible by three. How many states does the minimal complete DFA for L have, including a rejecting sink if needed?

**Answer format:** Integer.

### Q39. [2 Marks] [NAT]

For F(a,b,c,d)=(a XOR b)(c XOR d), what is the minimum total number of literal occurrences in a two-level sum-of-products expression without don't-care inputs? Count each occurrence in each product separately.

**Answer format:** Integer.

### Q40. [2 Marks] [MCQ]

What is the tight asymptotic running time of the following code? Each work() and each loop-control operation costs constant time. Arithmetic is exact and n is a positive integer.

```text
k = 1
for i = 1 to n:
    if i == k:
        for j = 1 to i:
            work()
        k = 2*k
```

A. Θ(log n)
B. Θ(n log n)
C. Θ(n)
D. Θ(n²)

### Q41. [2 Marks] [MSQ]

Consider S→aSbS | bSaS | ε. Which statements are true?

A. Every generated word has equally many a and b symbols.
B. The word abab has more than one parse tree.
C. Every prefix of every generated word has at least as many a as b symbols.
D. The generated language is regular.

### Q42. [2 Marks] [MSQ]

In four-variable cube notation, a dash means either bit. Two implicants are 0−0− and −00−. Suppose every minterm in either cube is an ON minterm and all other minterms are OFF, except 1100 and 1101, which are don't-cares. Which statements are correct?

A. The cubes cannot be combined by the ordinary one-bit-difference Quine–McCluskey combination rule because their dash positions differ.
B. Their union alone already contains all minterms of −−0−.
C. The larger cube −−0− includes an OFF minterm under the specified classification.
D. Using the two don't-cares permits −−0− as a valid implicant covering their union.

### Q43. [2 Marks] [NAT]

Inputs 1,2,3,4 enter a single stack in that order. Each input is pushed exactly once and each is popped exactly once; pops produce an output permutation. How many distinct output permutations are possible if the stack may never hold more than two items?

**Answer format:** Integer.

### Q44. [2 Marks] [NAT]

A processor can perform two arithmetic operations per ns and main memory can transfer eight bytes per ns. Each independent iteration needs eight arithmetic operations and 24 bytes of memory traffic. An optimization reduces arithmetic work to four operations per iteration without changing traffic. Assume perfect overlap of computation and transfers, no startup cost, and no other bottleneck. What is the ratio of optimized to original steady-state iteration throughput? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q45. [2 Marks] [MSQ]

Relation R(A,B,C,D) has dependencies A→B, B→A and C→D, with no additional independent dependencies. Which statements are true?

A. AC and BC are exactly its candidate keys.
B. R is already in BCNF.
C. Decomposition into AB, CD and AC is lossless and preserves all the given dependencies.
D. Decomposition into AB and CD alone is guaranteed lossless.

### Q46. [2 Marks] [NAT]

A router has routes 10.0.0.0/8 to A, 10.64.0.0/10 to B, 10.96.0.0/11 to C and 10.100.0.0/16 to D. Within 10.96.0.0/11, how many complete /16 blocks are forwarded to C under longest-prefix matching?

**Answer format:** Integer.

### Q47. [2 Marks] [NAT]

A clustered file packs ten fixed-length records per data block. A range scan starts at zero-based slot 7 of one block and returns the next 23 records, including that starting record. Finding the first record requires reading three separate index blocks; all blocks are initially uncached, index blocks are distinct from data blocks, and following data blocks incurs no extra index reads. How many distinct blocks must be read?

**Answer format:** Integer.

### Q48. [2 Marks] [MCQ]

A lexically scoped language has procedure P with local x=10. Procedures Q and S are declared directly inside P. Q has its own local x=20 and declares R inside Q. S increments its lexically nearest x and returns that x. During one activation of P, Q calls R, and R calls S twice in sequence. What is the sum of S's returned values?

A. 21
B. 23
C. 43
D. 40

### Q49. [2 Marks] [MSQ]

A NAT translates TCP connections using a single public IPv4 address and external ports. Two internal hosts use the same local source port. Which statements are correct?

A. If both connect to the same remote IP and port simultaneously, their translated source ports must differ to keep the external TCP connections distinct.
B. Changing the source IP address never affects the TCP checksum.
C. A suitable NAT policy may reuse the same external port for connections to different remote endpoints when its reverse lookup includes the remote endpoint.
D. The local source port alone always uniquely identifies the internal host for an incoming reply.

### Q50. [2 Marks] [NAT]

An unweighted tree has edges AB, AC, BD, BE, CF, FG and FH. Distance is the number of edges on the unique path. How many unordered pairs of distinct vertices have distance equal to the tree's diameter, its largest vertex-pair distance?

**Answer format:** Integer.

### Q51. [2 Marks] [MSQ]

Binary Huffman coding is applied to five symbols with weights 1,1,2,2,4. Ties may be resolved arbitrarily. Which codeword lengths can the weight-4 symbol receive in a resulting Huffman tree? The root has depth zero.

A. 1
B. 2
C. 3
D. 4

### Q52. [2 Marks] [MSQ]

A loop visits consecutive integer indices i starting at s and loads the four-byte array element at byte address base+4*i. Arithmetic is exact, base is unchanged, and i is also used by other statements. Which strength reductions preserve the load addresses and those other uses?

A. Initialize address p=base and increment p by four each iteration for arbitrary s.
B. Initialize p=base+4*s, use p for each load, and increment p by four after each iteration while retaining i's original updates.
C. The multiplication used to form each load address can then be removed from the loop body if it has no other uses.
D. Remove every update of i merely because a running address is available.

### Q53. [2 Marks] [NAT]

A TCP sender has congestion window 10 segments, advertised receive window 12 segments and eight unacknowledged segments. It first sends as many additional segments as allowed. A subsequent cumulative ACK acknowledges five of the outstanding segments; for the next send decision, congestion window is set to eight and the new advertised receive window is six segments. There are no retransmissions or other changes. How many new segments can be sent in total across these two send decisions?

**Answer format:** Integer.

### Q54. [2 Marks] [NAT]

Let u,v be real column vectors of length four satisfying vᵀu=−1, and A=I+uvᵀ. Find det(A+2I).

**Answer format:** Integer.

### Q55. [2 Marks] [MSQ]

A function f is continuously differentiable on [0,1], with f(0)=0, f(1/2)=2 and f(1)=1. Which statements must hold?

A. f′ equals 4 somewhere in (0,1/2).
B. f′ is positive throughout (0,1).
C. f′ equals −2 somewhere in (1/2,1).
D. f′ equals zero somewhere in (0,1).

### Q56. [2 Marks] [NAT]

Round-robin scheduling uses quantum two and zero context-switch cost. Jobs P,Q,R arrive at times 0,1,2 with CPU bursts 5,3,1 respectively. Arrivals exactly at a quantum boundary join the ready queue before the just-preempted job. What is the sum of their waiting times?

**Answer format:** Integer.

### Q57. [2 Marks] [MSQ]

A nondeterministic PDA recognizes even-length palindromes over {a,b} by pushing an initial segment, guessing its midpoint using an epsilon transition, and then matching and popping the remaining symbols; it accepts only after consuming all input and returning to its bottom marker. Which statements are correct?

A. Any accepting computation on abba must guess the midpoint after two input symbols.
B. Guessing the midpoint after one input symbol can accept abba by ignoring a mismatched stack symbol.
C. The word abab is rejected on every computation.
D. An incorrect midpoint guess must make every computation on an actual palindrome reject.

### Q58. [2 Marks] [NAT]

An initially empty B+ tree has leaves holding at most three keys and internal nodes holding at most three separator keys (four children). Insert keys 1 through 12 in increasing order. An overflowing leaf with four keys splits into two leaves of two keys. An overflowing internal node with five children splits into a left node of two children and a right node of three children; one separating key is promoted. A root split creates a new root. Count all leaves and internal nodes, including the root. How many nodes exist after all insertions?

**Answer format:** Integer.

### Q59. [2 Marks] [NAT]

Four matrices A,B,C,D have dimensions 5×10, 10×2, 2×8 and 8×3. Using ordinary matrix multiplication with pqr scalar multiplications for a p×q by q×r product, what is the minimum scalar multiplication count over all parenthesizations of ABCD?

**Answer format:** Integer.

### Q60. [2 Marks] [NAT]

A two-way cache has two sets, initially empty, with LRU replacement. The memory-block reference sequence is 0,2,4,0,2,4. Compare mapping I, set index equal to block-address bit 0, with mapping II, set index equal to bit 0 XOR bit 1. Block bits are numbered from zero at the least significant end. How many fewer misses occur with mapping II?

**Answer format:** Integer.

### Q61. [2 Marks] [NAT]

CPU instructions each take one bus-available cycle. Beginning at cycle 1, a DMA device steals every fourth cycle (4,8,12,...) until it has completed 64 one-cycle transfers. The CPU must execute 100 instructions and cannot progress during stolen cycles. At the end of which cycle does its 100th instruction finish?

**Answer format:** Integer.

### Q62. [2 Marks] [NAT]

A prize is equally likely to be in boxes A,B,C. A contestant selects A. A knowledgeable host opens an unselected empty box: if the prize is in A, the host opens B with probability 1/4 and C with probability 3/4; if the prize is elsewhere, the host opens the only empty unselected box. Given that the host opens B, what is the probability that switching to C wins?

**Answer format:** Exact finite decimal.

### Q63. [2 Marks] [NAT]

Let D be the positive divisors of 30, ordered by divisibility. How many bijections f:D→D preserve the order in both directions, meaning x divides y if and only if f(x) divides f(y)?

**Answer format:** Integer.

### Q64. [2 Marks] [NAT]

A disk head starts at track 50 moving upward at one track per ms on tracks 0–99. It uses SCAN: it continues to physical endpoint 99 before reversing, even if no pending request lies farther upward. At time zero requests exist at tracks 60 and 20. A new request for track 70 arrives at time 30 ms, after the head has passed track 70. Service takes zero time; direction does not change for the new arrival. How many ms does the new request wait from arrival to service?

**Answer format:** Integer.

### Q65. [2 Marks] [MSQ]

In a language with exact integer arithmetic, division by zero raises an observable exception. Consider `t=1/x; t=2; print(t);`, with x unchanged and print observable. Which statements are correct?

A. The first assignment can always be removed because its stored value is dead.
B. Its stored value is dead, but its possible exception can prevent unconditional removal.
C. Both assignments can always be removed, leaving print(t) with t's old value.
D. If x is proved nonzero, the whole fragment may be replaced by print(2).

## ANSWER KEY — MOCK TEST 017

NAT answers are exact except for the stated rounded ranges.

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | B |
| 2 | NAT | 1 | 1 |
| 3 | MSQ | 1 | A, B |
| 4 | MCQ | 1 | D |
| 5 | MCQ | 1 | C |
| 6 | NAT | 2 | 1488 |
| 7 | NAT | 2 | 47.73 (range 47.725–47.735) |
| 8 | NAT | 2 | 8 |
| 9 | MCQ | 2 | C |
| 10 | NAT | 2 | 0.6 |
| 11 | NAT | 1 | 3456 |
| 12 | MSQ | 1 | A, C |
| 13 | MSQ | 1 | A, C, D |
| 14 | NAT | 1 | 2 |
| 15 | MCQ | 1 | C |
| 16 | MCQ | 1 | C |
| 17 | MCQ | 1 | D |
| 18 | MCQ | 1 | B |
| 19 | NAT | 1 | 2 |
| 20 | MSQ | 1 | B, D |
| 21 | MSQ | 1 | A, B, D |
| 22 | NAT | 1 | -0.25 |
| 23 | NAT | 1 | 0.25 |
| 24 | MCQ | 1 | D |
| 25 | MSQ | 1 | A, B |
| 26 | NAT | 1 | 12 |
| 27 | MSQ | 1 | A, B |
| 28 | NAT | 1 | -1 |
| 29 | NAT | 1 | 5 |
| 30 | NAT | 1 | 9 |
| 31 | NAT | 1 | 6 |
| 32 | MSQ | 1 | A, B |
| 33 | MCQ | 1 | C |
| 34 | NAT | 1 | 1040 |
| 35 | MCQ | 1 | D |
| 36 | NAT | 2 | 15 |
| 37 | MSQ | 2 | B, C |
| 38 | NAT | 2 | 7 |
| 39 | NAT | 2 | 16 |
| 40 | MCQ | 2 | C |
| 41 | MSQ | 2 | A, B |
| 42 | MSQ | 2 | A, D |
| 43 | NAT | 2 | 8 |
| 44 | NAT | 2 | 1.3333 (range 1.33325–1.33335) |
| 45 | MSQ | 2 | A, C |
| 46 | NAT | 2 | 31 |
| 47 | NAT | 2 | 6 |
| 48 | MCQ | 2 | B |
| 49 | MSQ | 2 | A, C |
| 50 | NAT | 2 | 4 |
| 51 | MSQ | 2 | A, B |
| 52 | MSQ | 2 | B, C |
| 53 | NAT | 2 | 3 |
| 54 | NAT | 2 | 54 |
| 55 | MSQ | 2 | A, C, D |
| 56 | NAT | 2 | 10 |
| 57 | MSQ | 2 | A, C |
| 58 | NAT | 2 | 9 |
| 59 | NAT | 2 | 178 |
| 60 | NAT | 2 | 3 |
| 61 | NAT | 2 | 133 |
| 62 | NAT | 2 | 0.8 |
| 63 | NAT | 2 | 6 |
| 64 | NAT | 2 | 48 |
| 65 | MSQ | 2 | B, D |


