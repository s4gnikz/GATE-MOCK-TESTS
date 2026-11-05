# GATE CS 2027 — Full-Length Mock Test 072

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

### Q1. [1 Mark] [MSQ]

Every signed form is archived. No archived form is editable. At least one editable form exists. Which conclusions necessarily follow?

A. No signed form is editable.
B. Every unsigned form is editable.
C. At least one unsigned form exists.
D. At least one signed form exists.

### Q2. [1 Mark] [NAT]

A paper strip has coordinate 0≤x≤8. Fold its part x>5 leftwards across x=5. Then fold every layer lying at x<3 rightwards across x=3. Punch through all layers at the resulting position x=4 and fully unfold. What is the mean of the original x-coordinates of all distinct punctures?

**Answer format:** Integer.

### Q3. [1 Mark] [MSQ]

Four events occur once each: filing F, inspection I, approval A, and publication P. Filing precedes both inspection and approval. Publication follows both inspection and approval. No order between inspection and approval is specified. Which conclusions necessarily follow?

A. Filing is the first of these four events.
B. Inspection immediately precedes approval.
C. Publication is the last of these four events.
D. Exactly two orders of these four events satisfy the conditions.

### Q4. [1 Mark] [NAT]

A bag contains one red and three blue balls. They are drawn without replacement until the red ball appears. What is the expected total number of draws, including the red ball?

**Answer format:** Exact decimal.

### Q5. [1 Mark] [MSQ]

Every sensor that passed calibration was installed. Some installed sensors were not tested. Which statements follow necessarily?

A. Every sensor not installed failed to pass calibration.
B. Every installed sensor passed calibration.
C. At least one installed sensor was not tested.
D. No untested sensor passed calibration.

### Q6. [2 Marks] [NAT]

A triangle has vertices A=(0,8),B=(−6,0),C=(6,0). Its orthocentre H is the intersection of its altitude lines. What is the y-coordinate of H?

**Answer format:** Exact decimal.

### Q7. [2 Marks] [MSQ]

For a finite list of integers, operation R reverses the list, and operation N negates every entry without changing the order. A student claims that applying R then N always gives the same list as applying N then R. Which statements hold?

A. Checking the claim on one list of length three proves it for lists of every length.
B. The claim holds because each final position contains the negative of the same original entry under either order.
C. Applying the combined operation twice restores every original list.
D. The claim implies that reversing a list always leaves it unchanged.

### Q8. [2 Marks] [NAT]

An urn contains three red and three blue balls. Two balls are drawn without replacement. If they have different colours, a prize of 6 units is paid; otherwise nothing is paid. What is the expected prize?

**Answer format:** Exact finite decimal.

### Q9. [2 Marks] [NAT]

A sequence starts a1=0. For each positive integer n, define a(n+1)=a(n)+n when n is odd and a(n+1)=a(n)−n when n is even. What is a101?

**Answer format:** Integer, including a minus sign if needed.

### Q10. [2 Marks] [NAT]

Two axis-aligned squares each have side4. One occupies [0,4]×[0,4]. The other occupies [t,t+4]×[t,t+4], where0≤t≤4. Their union has area28. What is t?

**Answer format:** Exact number.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

A C array `int a[3][5]` is stored in row-major order, with sizeof(int)=4 bytes. What is the byte offset of a[2][3] from the start of the array?

**Answer format:** Integer.

### Q12. [1 Mark] [NAT]

A DFA tracks the input length modulo2 and the number of a symbols modulo2 over alphabet{a,b}. It starts with both parities even. How many of the four parity-pair states are reachable?

**Answer format:** Integer.

### Q13. [1 Mark] [MSQ]

Initially x=y=1 and a database invariant requires x+y≥1. Two concurrent transactions read the same initial snapshot. T1, seeing y=1, writes x=0; T2, seeing x=1, writes y=0. A scheme rejects only concurrent writes to the same item, so both commit. Which statements are correct?

A. Their writes target different items.
B. The final state violates the invariant.
C. The execution is equivalent to a serial execution of these conditional transactions.
D. Avoiding direct write-write conflicts alone is insufficient for this invariant.

### Q14. [1 Mark] [MSQ]

T1 writes x. Before T1 commits, T2 reads that written value and then commits. T1 later aborts. Which statements are correct?

A. T2 performed a dirty read.
B. This schedule is recoverable.
C. T2 committed based on a value later rolled back.
D. The schedule is strict.

### Q15. [1 Mark] [NAT]

A grammar has start symbol S and productions S→AB, A→a, B→bB, C→c. A nonterminal is productive if it derives some finite terminal string. How many nonterminals are both reachable from S and productive?

**Answer format:** Integer.

### Q16. [1 Mark] [NAT]

A Karnaugh-map group contains eight minterms of a four-variable function and forms a valid Boolean cube. How many literals remain in its product term?

**Answer format:** Integer.

### Q17. [1 Mark] [MSQ]

An unweighted directed graph has edges s→a,s→b,a→c,b→d,d→c. A BFS begins at s and marks vertices when enqueued. Which statements are correct regardless of the order of s's adjacency list?

A. c is assigned distance2.
B. c may be assigned distance3 if b is examined first.
C. d is assigned distance2.
D. Every vertex's BFS parent is necessarily unique in every directed graph.

### Q18. [1 Mark] [NAT]

A collision-detection link transmits at 100 Mbit/s. The worst-case one-way propagation time between stations, including repeater delays, is 2.4 microseconds. Ignore all other timing constraints. What is the minimum frame size in bytes required for a sender still to be transmitting when a worst-case collision notification returns?

**Answer format:** Integer bytes; use 1 Mbit=10⁶ bits.

### Q19. [1 Mark] [NAT]

A directory contains three hard links to the same ordinary file. One link is removed. How many directory hard links to that file remain, assuming no other changes?

**Answer format:** Integer.

### Q20. [1 Mark] [NAT]

A procedure F(n) returns immediately for n≤1 and otherwise calls F(floor(n/2)) once. Including the initial invocation and the base invocation, how many calls occur for n=19?

**Answer format:** Integer.

### Q21. [1 Mark] [NAT]

A random variable X has mean 10 and variance 4. For Z=3X−2, find E[Z²].

**Answer format:** Integer.

### Q22. [1 Mark] [NAT]

A relation R on {1,2,3,4} is defined by xRy iff x and y have the same parity. How many ordered pairs belong to R composed with R?

**Answer format:** Exact integer.

### Q23. [1 Mark] [MCQ]

A lexer recognizes unsigned integer tokens, the operator '-', and identifiers. It tokenizes x--12 without treating '--' as a separate operator. The parser alone distinguishes unary and binary minus. Which token sequence is produced?

A. identifier(x), minus, integer(−12)
B. identifier(x), minus, minus, integer(12)
C. identifier(x−−12)
D. identifier(x), decrement, integer(12)

### Q24. [1 Mark] [NAT]

Two Ethernet stations collide and independently choose their backoff values uniformly from {0,1,2,3}. Conditional on their values being different, what is the probability that the smaller value is zero?

**Answer format:** Exact decimal.

### Q25. [1 Mark] [NAT]

Four identical256×8-bit RAM chips provide a1024×8-bit byte-addressable memory. Address bits A0–A7 connect to every chip's address pins. A decoder selects a chip using A8,A9. How many chips are selected during one valid byte read, and how many distinct byte addresses can be read? Enter the product of these two numbers.

**Answer format:** Integer.

### Q26. [1 Mark] [MSQ]

A connected weighted undirected graph has a vertex v incident to exactly one edge e. Edge weights may be negative or equal. Which statements necessarily hold?

A. Every spanning tree contains e.
B. Every minimum spanning tree contains e.
C. e must be the minimum-weight edge in the entire graph.
D. Removing e leaves a connected graph.

### Q27. [1 Mark] [NAT]

In a simplified slotted contention scheme, two stations independently choose one of four slots uniformly and transmit once in that slot. A collision occurs if they choose the same slot. Given that station A chose a slot later than slot1, what is the collision probability?

**Answer format:** Exact decimal.

### Q28. [1 Mark] [NAT]

In the multiplicative group of units modulo 10, what is the order of the element 3?

**Answer format:** Integer.

### Q29. [1 Mark] [MSQ]

For real x, define f(x)=x when x is rational and f(x)=−x when x is irrational. Which statements are true?

A. f is continuous at zero.
B. f is not differentiable at zero.
C. f is continuous at one.
D. f′(0)=0.

### Q30. [1 Mark] [NAT]

An eight-bit two's-complement fixed-point representation uses four fractional bits. What real number does bit pattern 11101000 represent?

**Answer format:** Exact finite decimal.

### Q31. [1 Mark] [MCQ]

A lexer recognizes the keyword `in`, identifiers matching [a-z]+, and the single-character token '.'. It uses longest match, giving the keyword priority over an identifier only when their matched lengths tie. What token-type sequence is produced on input `in.inner`?

A. keyword, '.', identifier.
B. identifier, '.', keyword, identifier.
C. keyword, '.', keyword, identifier.
D. identifier, '.', identifier.

### Q32. [1 Mark] [MSQ]

A directed graph has edges s→a of weight 2, s→b of weight 5, and b→a of weight −4. There are no other edges. Which statements are correct?

A. The shortest s-to-a path has weight 1.
B. The graph has a negative-weight cycle.
C. A Dijkstra implementation that permanently settles a before b can output a wrong distance for a.
D. Every shortest path uses the fewest possible edges.

### Q33. [1 Mark] [NAT]

Independent random variables X and Y each have variance 4. Find Var(2X−3Y+7).

**Answer format:** Integer.

### Q34. [1 Mark] [NAT]

A processor uses byte addressing and little-endian 32-bit words. Bytes at addresses 100 through 103 are hexadecimal 12,34,56,78. It loads the 32-bit word at 100, shifts that unsigned value right by 16 bits, and stores the low 16 bits at addresses 102–103 in little-endian order. What decimal value is then in byte 102?

**Answer format:** Integer.

### Q35. [1 Mark] [MSQ]

On a UNIX-like file system, path p refers to regular file F. Process R has already opened F for reading. Process W creates a different regular file G and atomically renames G over p. No process modifies F or G afterward. Assume rename succeeds and no symbolic links are involved. Which statements hold?

A. R's existing descriptor still refers to F.
B. A later successful open of p refers to G.
C. The rename necessarily changes the inode referred to by R's existing descriptor.
D. F's storage must be reclaimed before the rename can return, even while R retains its descriptor.

### Q36. [2 Marks] [NAT]

A size-7 hash table uses linear probing with h(k)=k mod 7 and wraparound. Insert 10,17,24,11 in that order into an empty table. Delete 17 by leaving a tombstone. A subsequent unsuccessful search for 31 stops at the first slot that has never been occupied, but passes tombstones. How many slots does this search inspect, including the terminating slot?

**Answer format:** Integer.

### Q37. [2 Marks] [NAT]

A direct-mapped cache has four sets and two-word blocks. A four-row matrix stores four data words per row, followed by p padding words per row. The matrix starts at word address0, and each row must begin at an even word address. What is the smallest nonnegative p making the first data words of the four rows map to four different cache sets?

**Answer format:** Integer words.

### Q38. [2 Marks] [MSQ]

A routing table contains prefix203.0.113.0/24 via X and more-specific prefix203.0.113.128/25 via Y. No other route matches. Which statements are correct under longest-prefix matching?

A. Address203.0.113.200 uses Y.
B. Address203.0.113.100 uses X.
C. Installing the /24 after the /25 necessarily makes it override the /25.
D. Removing the /25 makes203.0.113.200 use X.

### Q39. [2 Marks] [NAT]

Four matrices A,B,C,D have dimensions 5×10, 10×2, 2×8 and 8×3. Using ordinary matrix multiplication with pqr scalar multiplications for a p×q by q×r product, what is the minimum scalar multiplication count over all parenthesizations of ABCD?

**Answer format:** Integer.

### Q40. [2 Marks] [NAT]

A message of 1200 bytes traverses two store-and-forward links in series, each operating at 8000 bits/s. It is divided into k equal-payload packets, each with a 75-byte header, where k is a positive divisor of1200. Links can operate simultaneously on different packets. Ignore propagation and processing delays. What value of k minimizes the time at which the complete message arrives?

**Answer format:** Exact integer.

### Q41. [2 Marks] [NAT]

A rooted tree has the parent array for vertices1 through7 given by[0,1,1,2,2,4,3], where0 marks the root. An operation cuts the subtree rooted at2 and reattaches its root as a child of7. How much does the sum of depths of all seven vertices increase, with the root's depth defined as0?

**Answer format:** Integer.

### Q42. [2 Marks] [NAT]

Insert keys20,10,30,25,40,22,27 into an initially empty ordinary BST. Perform a single left rotation at root20: its right child30 becomes the root,20 becomes30's left child, and30's former left subtree becomes20's right subtree. How many keys have the same depth before and after the rotation, counting the root's depth as0?

**Answer format:** Integer.

### Q43. [2 Marks] [NAT]

Represent exactly the address set10.1.0.0/24 excluding10.1.0.64/26 as a union of CIDR prefixes, without including any excluded address. What is the minimum number of prefixes needed?

**Answer format:** Integer.

### Q44. [2 Marks] [MSQ]

Consider replacing x*2 by x+x in an integer intermediate representation. Which statements are correct?

A. For unbounded mathematical integers the two expressions are equal.
B. For arithmetic modulo2^w the two results are equal for every w-bit x.
C. This equivalence alone proves that replacing any signed C expression involving multiplication can ignore its language's overflow rules.
D. The replacement's profitability can depend on the target machine, even when semantic equivalence holds.

### Q45. [2 Marks] [MSQ]

A fractional knapsack has capacity5 and two available items, each of weight4 and value8. Any real fraction between0 and1 of each item may be selected. Which statements are correct?

A. Selecting weight2.5 from each item is optimal.
B. Every optimal solution must have at most one partially selected item.
C. An optimal solution with one whole item and one partially selected item exists.
D. The optimal allocation is unique.

### Q46. [2 Marks] [NAT]

How many ordered compositions of 8 use only parts 1 and 2 and never place two parts of size 2 consecutively? For example, 2,1,2 is allowed for total 5, while 1,2,2 is not.

**Answer format:** Integer.

### Q47. [2 Marks] [NAT]

Procedure P is lexically nested inside Main. Procedures Q and R are both lexically nested inside P. During execution, Main calls P, P calls Q, and Q calls R. Each activation has a static link to its immediate lexical parent's activation and a dynamic link to its caller. From R's activation, how many static links must be followed to access a local variable of Main?

**Answer format:** Integer.

### Q48. [2 Marks] [NAT]

A binary floating-point system has three significant bits, including the leading1, and sufficient exponent range. It rounds each operation to nearest, with ties to an even significand low bit. Compute the absolute difference between fl(fl(8+1)−8) and fl(8+fl(1−8)). Here fl means rounding one operation in that format.

**Answer format:** Exact number.

### Q49. [2 Marks] [NAT]

Five CPU-bound processes are permanently ready in round-robin order. A quantum lasts q positive integer milliseconds, and each intervening context switch costs one millisecond. At time zero the first process starts without an initial switch. Require useful CPU time to be at least 80% of steady-state elapsed time, and require the fifth process to begin its first quantum no later than time 20. What value of q satisfies both requirements?

**Answer format:** Integer.

### Q50. [2 Marks] [MSQ]

A Boolean cover-selection chart contains candidate rows P and Q. P covers{u,v} at cost3; Q covers{u,v,w} at cost2. The objective is minimum total cost, and selecting a row has no effect except covering its columns. Which statements are correct?

A. An optimal cover can always be chosen without P.
B. Replacing P by Q in a cover cannot uncover a column and cannot increase cost.
C. P must be retained merely because some of its columns also appear in Q.
D. The same dominance conclusion follows if Q instead costs5, solely from its greater coverage.

### Q51. [2 Marks] [NAT]

A rooted tree has root r with children a,b,c. Vertex a has two leaf children, b has one leaf child, and c is a leaf. How many different preorder sequences of vertex labels are possible if the order of children at every vertex may be chosen independently? All seven vertex labels are distinct.

**Answer format:** Exact integer.

### Q52. [2 Marks] [NAT]

On the interval[−2,2], how many distinct x values attain the global maximum of |x³−3x|?

**Answer format:** Integer.

### Q53. [2 Marks] [MSQ]

Define L={aⁱbʲ:i,j≥0 and i≠j}. Which statements are correct?

A. L is context-free.
B. L is regular.
C. The complement of L within a*b* is {aⁿbⁿ:n≥0}.
D. ε belongs to L.

### Q54. [2 Marks] [NAT]

Six employees participate in a directed Mentors relationship. Self-mentoring is forbidden. Each employee may mentor at most two others and must be mentored by at least one other employee. A pair (u,v) means u mentors v. What is the maximum possible number of distinct pairs?

**Answer format:** Integer.

### Q55. [2 Marks] [NAT]

An initially free64-KiB region is managed by a binary buddy allocator. Each request is rounded up to the smallest power-of-two KiB block that fits it. Splitting always allocates the lowest-address available suitable descendant; free buddies coalesce immediately. Requests A=9KiB, B=9KiB, C=17KiB are allocated in that order. A is then freed. What is the size, in KiB, of the largest request that can now be satisfied without freeing B or C?

**Answer format:** Integer.

### Q56. [2 Marks] [NAT]

A combinational circuit implements unsigned comparison A>B for two-bit inputs A=a1a0 and B=b1b0. Among the16 possible input pairs, for how many does the low-bit comparison a0>b0 disagree with the full comparison A>B?

**Answer format:** Integer.

### Q57. [2 Marks] [NAT]

One process executes the following pseudocode. Every fork succeeds and duplicates the current process; no process exits early.

```text
fork()
if fork() returns 0:
    fork()
```

Including the original process, how many processes exist after all forks complete?

**Answer format:** Integer.

### Q58. [2 Marks] [MSQ]

Let L={a^n : n is a perfect square}, including ε. For a hypothetical regular pumping length p≥1, choose s=a^(p²). A legal pumped part has length k with1≤k≤p. Which statements are correct?

A. Pumping once more gives length p²+k, strictly between p² and(p+1)².
B. For every legal decomposition, pumping twice leaves the language.
C. The proof depends on choosing the pumped part to have exactly p symbols.
D. The pumping lemma therefore proves L regular.

### Q59. [2 Marks] [MSQ]

Let L={ww : w in {a,b}*}. Which statements are correct?

A. Every word in L has even length.
B. Every even-length palindrome belongs to L.
C. L contains words that are not palindromes.
D. L is closed under reversal.

### Q60. [2 Marks] [NAT]

An ideal single-issue pipeline executes100 instructions in104 cycles, including filling and draining. Of these instructions,20 are conditional branches. A prediction scheme mispredicts exactly25% of those branches; every misprediction introduces3 extra cycles. No other stalls occur. What is the resulting CPI, using total execution cycles divided by100?

**Answer format:** Exact decimal.

### Q61. [2 Marks] [NAT]

A fair coin chooses one of two bags. Bag A contains two red and one blue ball; bag B contains one red and two blue balls. Two draws are made without replacement from the chosen bag. Given that the second draw is red, what is the probability that the first draw was blue? Round to four decimal places.

**Answer format:** Decimal rounded to four places.

### Q62. [2 Marks] [MSQ]

Let L1={a^n b^n c^m : n,m≥0} and L2={a^m b^n c^n : n,m≥0}. Which statements are correct?

A. Both L1 and L2 are context-free.
B. Their intersection is {a^n b^n c^n : n≥0}.
C. Their intersection must be context-free because each language is context-free.
D. Their union is context-free.

### Q63. [2 Marks] [NAT]

Under set semantics, R(A,B)={(1,x),(1,y),(2,x),(3,x),(3,y)} and S(B)={x,y}. How many tuples are in relational division R÷S?

**Answer format:** Integer.

### Q64. [2 Marks] [MSQ]

In an expression language, evaluating an operand may have side effects; && and || evaluate left to right and short-circuit. Values are Boolean. Which rewrites preserve both returned value and operand side effects in every execution?

A. false && f() → false
B. f() && false → false
C. true || f() → true
D. f() || true → true

### Q65. [2 Marks] [MSQ]

A poset has elements a,b,c,d with a<c,b<c,c<d, and only the comparisons forced by these and reflexivity. Let J be the family of its downward-closed subsets, ordered by inclusion. Which statements are correct?

A. J has six elements, including the empty subset.
B. Join in J is set union.
C. Meet in J is set intersection.
D. J fails distributivity because a and b are incomparable.

---

## ANSWER KEY — MOCK TEST 072

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MSQ | 1 | A, C |
| 2 | NAT | 1 | 5 |
| 3 | MSQ | 1 | A, C, D |
| 4 | NAT | 1 | 2.5 |
| 5 | MSQ | 1 | A, C |
| 6 | NAT | 2 | 4.5 |
| 7 | MSQ | 2 | B, C |
| 8 | NAT | 2 | 3.6 |
| 9 | NAT | 2 | -50 |
| 10 | NAT | 2 | 2 |
| 11 | NAT | 1 | 52 |
| 12 | NAT | 1 | 4 |
| 13 | MSQ | 1 | A, B, D |
| 14 | MSQ | 1 | A, C |
| 15 | NAT | 1 | 1 |
| 16 | NAT | 1 | 1 |
| 17 | MSQ | 1 | A, C |
| 18 | NAT | 1 | 60 |
| 19 | NAT | 1 | 2 |
| 20 | NAT | 1 | 5 |
| 21 | NAT | 1 | 820 |
| 22 | NAT | 1 | 8 |
| 23 | MCQ | 1 | B |
| 24 | NAT | 1 | 0.5 |
| 25 | NAT | 1 | 1024 |
| 26 | MSQ | 1 | A, B |
| 27 | NAT | 1 | 0.25 |
| 28 | NAT | 1 | 4 |
| 29 | MSQ | 1 | A, B |
| 30 | NAT | 1 | -1.5 |
| 31 | MCQ | 1 | A |
| 32 | MSQ | 1 | A, C |
| 33 | NAT | 1 | 52 |
| 34 | NAT | 1 | 86 |
| 35 | MSQ | 1 | A, B |
| 36 | NAT | 2 | 5 |
| 37 | NAT | 2 | 2 |
| 38 | MSQ | 2 | A, B, D |
| 39 | NAT | 2 | 178 |
| 40 | NAT | 2 | 4 |
| 41 | NAT | 2 | 8 |
| 42 | NAT | 2 | 3 |
| 43 | NAT | 2 | 2 |
| 44 | MSQ | 2 | A, B, D |
| 45 | MSQ | 2 | A, C |
| 46 | NAT | 2 | 19 |
| 47 | NAT | 2 | 2 |
| 48 | NAT | 2 | 1 |
| 49 | NAT | 2 | 4 |
| 50 | MSQ | 2 | A, B |
| 51 | NAT | 2 | 12 |
| 52 | NAT | 2 | 4 |
| 53 | MSQ | 2 | A, C |
| 54 | NAT | 2 | 12 |
| 55 | NAT | 2 | 16 |
| 56 | NAT | 2 | 4 |
| 57 | NAT | 2 | 6 |
| 58 | MSQ | 2 | A, B |
| 59 | MSQ | 2 | A, C, D |
| 60 | NAT | 2 | 1.19 |
| 61 | NAT | 2 | 0.6667 (accepted range 0.66665–0.66675) |
| 62 | MSQ | 2 | A, B, D |
| 63 | NAT | 2 | 2 |
| 64 | MSQ | 2 | A, C |
| 65 | MSQ | 2 | A, B, C |
