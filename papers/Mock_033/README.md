# GATE CS 2027 — Full-Length Mock Test 033

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

Q1–Q5 and Q11–Q35 carry one mark each; Q6–Q10 and Q36–Q65 carry two marks each. General Aptitude contributes 15 marks, Engineering Mathematics 13, and core Computer Science 72.

Select exactly one option for MCQ and all correct options for MSQ. Incorrect MCQs lose one third of the question's marks. MSQ and NAT have no negative marking; MSQ has no partial credit. Unattempted questions receive zero. Follow the stated NAT precision. The answer key is placed after Question 65.

---

## Section A — General Aptitude

### Q1. [1 Mark] [MCQ]

Choose the grammatically correct completion: “Had the survey included night-shift workers, its conclusion ____ different.”

A. will have been
B. would have been
C. would be being
D. had been being

### Q2. [1 Mark] [NAT]

An item's marked price is increased by 25%, and the discount is changed from 20% of the old marked price to 30% of the new marked price. By what percentage does its selling price increase?

**Answer format:** Exact decimal percentage, without the % sign.

### Q3. [1 Mark] [MSQ]

Exactly one of K,L,M is a coordinator. K is a coordinator only if L is available. L is unavailable. If M is a coordinator, N is available. Which conclusions necessarily follow?

A. K is not the coordinator.
B. L is the coordinator.
C. Either L or M is the coordinator.
D. N is available.

### Q4. [1 Mark] [MCQ]

A point is first reflected across y=x, then translated by (2,−1). Which point maps to (5,3)?

A. (3,4)
B. (4,3)
C. (6,1)
D. (1,6)

### Q5. [1 Mark] [MCQ]

Read the statement: “When the library extended its hours, evening visits increased. Total daily visits stayed unchanged because morning visits fell by the same amount. The data alone do not establish whether additional people began using the library.” Which inference is supported?

A. Every new evening visitor was previously a morning visitor.
B. The number of distinct users increased.
C. The distribution of visits across the day changed.
D. Extending hours caused no benefit to any visitor.

### Q6. [2 Marks] [NAT]

Four students each receive one distinct project, with assignments chosen from all 4! possibilities. Exactly two students must receive their first-choice project. The four first-choice projects are all different. How many assignments satisfy this requirement?

**Answer format:** Exact integer.

### Q7. [2 Marks] [NAT]

A service runs in two regions. In region X, 80% of requests succeed; in region Y, 95% succeed. Initially each region receives 100 requests. Later the number in X doubles while Y still receives 100; each regional success rate stays unchanged. By how many percentage points does the combined success rate decrease?

**Answer format:** Exact decimal, without the % sign.

### Q8. [2 Marks] [NAT]

A rectangular sheet occupies 0≤x≤8 and 0≤y≤6. Fold its right half onto the left along x=4, then fold its top half onto the bottom along y=3. In the folded rectangle, cut out the entire small rectangle 3<x≤4, 1<y<2 through all layers. What is the total perimeter of all resulting internal holes after the sheet is unfolded? The cut reaches the folded edge x=4, but does not touch y=3 or the original sheet's outer boundary.

**Answer format:** Exact integer, in the same length units.

### Q9. [2 Marks] [MCQ]

Four events occurred once each: calibration C, inspection I, trial T, and release R. Calibration preceded trial; inspection immediately followed calibration; release occurred after inspection but before trial. Which order is consistent?

A. C,I,R,T
B. C,R,I,T
C. I,C,R,T
D. C,I,T,R

### Q10. [2 Marks] [NAT]

A bag contains two red and two blue balls. Draw two without replacement. If their colors match, record 1; otherwise record 0. Repeat the entire experiment independently after restoring the bag. What is the probability that the two recorded values differ?

**Answer format:** Decimal rounded to four places.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MSQ]

A prime-implicant chart has four columns m0,m1,m2,m3 and four rows. P covers m0,m1; Q covers m1,m2; R covers m2,m3; S covers m0,m3. All rows have equal literal cost and no other prime implicants exist. Which statements hold?

A. No row is essential.
B. Every minimum cover contains P.
C. {P,R} is a minimum cover.
D. Removing P still leaves a cover using two rows.

### Q12. [1 Mark] [NAT]

A recursive routine visits a binary tree as follows. A null pointer returns immediately; a non-null call invokes the routine on both children, even when a child pointer is null. If the tree has 12 non-null vertices, how many calls receive a null pointer?

**Answer format:** Exact integer.

### Q13. [1 Mark] [NAT]

A syntax-directed translator for expressions uses E→E+T with E.val=Eleft.val+T.val, E→T with E.val=T.val, T→digit with T.val=digit.value, and T→(E) with T.val=2×E.val. What value is assigned to the complete expression (2+3)+(4)?

**Answer format:** Exact integer.

### Q14. [1 Mark] [MCQ]

Over a nonempty domain, which formula is the negation of “For every x, if P(x), there exists y such that R(x,y)”?

A. For every x, P(x) and for every y, not R(x,y).
B. There exists x such that not P(x) and there exists y with R(x,y).
C. There exists x such that P(x) and for every y, not R(x,y).
D. There exists x such that P(x) and there exists y with not R(x,y).

### Q15. [1 Mark] [NAT]

A is a 3×3 real matrix with determinant 2. Form B by interchanging its first two rows and then multiplying its third column by −3. What is det(2B)?

**Answer format:** Exact integer.

### Q16. [1 Mark] [NAT]

An open-addressed hash table has 12 slots. A key probes slots (5+i·s) mod 12 for i=0,1,2,… . Among integers s from 1 through 11, how many choices visit every slot before repetition?

**Answer format:** Exact integer.

### Q17. [1 Mark] [MSQ]

L is a language over {a,b}, and its complement is taken with respect to {a,b}*. Which statements necessarily hold?

A. If both L and its complement are finite, then {a,b}* is finite.
B. If L is regular, its complement is context-free.
C. If L is context-free, its complement is regular.
D. If L is finite, its complement is regular.

### Q18. [1 Mark] [MCQ]

A language has lexically nested procedures. Procedure P contains Q and R; Q calls R. In a stack activation record for R, which relationship is correct under the usual static-link and dynamic-link model?

A. Both links point to Q's activation record.
B. The static link identifies P's activation; the dynamic link identifies Q's activation.
C. The static link identifies Q's activation; the dynamic link identifies P's activation.
D. Both links identify P's activation regardless of the caller.

### Q19. [1 Mark] [NAT]

An in-place transpose of a row-major 3×4 array permutes old linear index i into new linear index (i mod4)×3+floor(i/4), for 0≤i<12. Starting at index1 and repeatedly applying this permutation, how many distinct indices occur before returning to1?

**Answer format:** Exact integer.

### Q20. [1 Mark] [MSQ]

A combinational block has Boolean inputs a,b,c and outputs s=a XOR b XOR c and k=ab OR ac OR bc. Which statements hold?

A. The numerical sum a+b+c equals s+2k.
B. k is 1 exactly when all three inputs are 1.
C. Complementing all three inputs complements s and complements k.
D. Distinct input triples always produce distinct output pairs (s,k).

### Q21. [1 Mark] [MCQ]

For positive integers n, let f(n)=n if n is even and f(n)=n² if n is odd. Which asymptotic statement holds?

A. f(n)=Theta(n).
B. f(n)=Theta(n²).
C. f(n)=Omega(n²).
D. f(n)=O(n²) and f(n)=Omega(n), but neither A nor B holds.

### Q22. [1 Mark] [MSQ]

A SQL table declares id as PRIMARY KEY and parent_id as a nullable foreign key referencing id in the same table. There are no other constraints. Which statements hold?

A. A row may have parent_id=NULL.
B. The declarations alone prevent a row from referencing itself.
C. The declarations alone prevent a cycle involving two rows.
D. Every non-NULL parent_id must match an existing id when the foreign-key constraint is checked.

### Q23. [1 Mark] [NAT]

Let f(x)=x² sin(1/x) for x≠0 and f(0)=0. What is f'(0)?

**Answer format:** Exact integer.

### Q24. [1 Mark] [MCQ]

A system has one instance each of resources R and S. P holds R and waits for S. Q holds S and waits for R. Resources cannot be preempted, and neither process releases its held resource until its request is satisfied. Which single policy change directly breaks a necessary deadlock condition for this execution?

A. Raise both process priorities equally.
B. Allow a waiting process's held resource to be forcibly reclaimed.
C. Add another ready process that requests neither resource.
D. Increase the CPU clock frequency.

### Q25. [1 Mark] [NAT]

A synchronous modulo-5 counter uses three flip-flops. Legal states 000,001,010,011,100 advance cyclically in that order; each illegal state goes to 000 on the next edge. From initial state 111, what unsigned state value appears after seven clock edges?

**Answer format:** Exact integer.

### Q26. [1 Mark] [NAT]

In a pumping-lemma argument for L={a^n b^m : n,m≥0 and n≠m}, consider z=a³b⁹ and every decomposition z=uvw satisfying |uv|≤3 and |v|≥1. For each decomposition, choose an integer i≥0 such that uv^i w has equally many a's and b's. What is the largest i required among these decompositions?

**Answer format:** Exact integer.
### Q27. [1 Mark] [MCQ]

A TCP server has a listening socket l. A successful accept(l) returns connected socket c. Which statement is correct?

A. The listening socket becomes c and can no longer accept connections.
B. Every write to l broadcasts data to all accepted clients.
C. Closing c necessarily closes l.
D. l can continue accepting other connections while c serves the accepted connection.

### Q28. [1 Mark] [NAT]

A translator emits three-address code for (a+b)*(a+b)+(a+b), reusing each already computed identical pure subexpression. Inputs are available in variables; assignments that perform no arithmetic are not counted. What is the minimum number of arithmetic instructions using only binary + and * and no algebraic reassociation?

**Answer format:** Exact integer.

### Q29. [1 Mark] [NAT]

X is uniformly distributed over {−2,−1,0,1,2}, and Y=X². What is E[Y²]?

**Answer format:** Exact decimal.

### Q30. [1 Mark] [NAT]

A relation R on {1,2,3,4} is defined by xRy iff x and y have the same parity. How many ordered pairs belong to R composed with R?

**Answer format:** Exact integer.

### Q31. [1 Mark] [MSQ]

A browser already knows a server's IP address and establishes a new TCP connection to request an HTTP resource. The server responds with a redirection to a different hostname. Which statements hold?

A. The initial request need not perform a new DNS query if its address is already usable.
B. The redirect guarantees that the original server's IP address is valid for the new hostname.
C. Following the redirect may require resolving the new hostname.
D. An HTTP redirect changes the destination address of the already transmitted request.

### Q32. [1 Mark] [MSQ]

Relation R(A,B,C,D) has dependencies A→B, AB→C, C→D, A→D. Which statements hold?

A. B is extraneous in the left side of AB→C.
B. A→D can be removed without changing the set of implied dependencies.
C. C→D can be removed without changing the set of implied dependencies.
D. A is a candidate key.

### Q33. [1 Mark] [NAT]

A byte-addressed processor has a 16-bit address bus. A 4 KiB memory chip is selected exactly when address bits A15..A12 equal 1010; A11..A0 address bytes within the chip. What is the largest decimal byte address mapped to the chip?

**Answer format:** Exact integer.

### Q34. [1 Mark] [NAT]

A two-level memory system checks a cache in 2 ns. On a miss, it then accesses main memory in 50 ns; the cache check and memory access do not overlap. A measured average access time is 7 ns. What is the cache hit probability?

**Answer format:** Exact decimal.

### Q35. [1 Mark] [NAT]

Three jobs arrive at time 0 with CPU bursts 2,3,5. Nonpreemptive shortest-job-first runs them. A context switch costs one time unit between consecutive jobs, but there is no cost before the first job. What is the sum of their waiting times?

**Answer format:** Exact integer.


### Q36. [2 Marks] [MSQ]

Host H sends an IPv4 packet through two routers to host J. Each link uses Ethernet, and there is no NAT, tunneling, or fragmentation. Which statements hold for normal forwarding?

A. The source and destination Ethernet addresses can change at each routed hop.
B. The source and destination IPv4 addresses change at every routed hop.
C. The IPv4 TTL decreases at each router that forwards the packet.
D. An Ethernet destination address on the first link must be J's Ethernet address even when J is on another subnet.

### Q37. [2 Marks] [NAT]

Four activities have (start,finish,profit) triples A=(0,2,3), B=(2,4,3), C=(0,4,9), D=(4,5,2). Activities sharing only an endpoint are compatible. A greedy algorithm selects a remaining compatible activity with earliest finish, breaking a tie in favor of earlier alphabetical label. By how much does the maximum achievable total profit exceed this algorithm's profit?

**Answer format:** Exact integer.

### Q38. [2 Marks] [NAT]

A message of 1200 bytes traverses two store-and-forward links in series, each operating at 8000 bits/s. It is divided into k equal-payload packets, each with a 75-byte header, where k is a positive divisor of1200. Links can operate simultaneously on different packets. Ignore propagation and processing delays. What value of k minimizes the time at which the complete message arrives?

**Answer format:** Exact integer.

### Q39. [2 Marks] [NAT]

A signed fixed-point accumulator uses 6-bit two's-complement encoding with two fractional bits and saturates after each addition to its representable range. Starting at zero, add4.5, then4.5, then−2.0. What is the final represented value?

**Answer format:** Exact decimal.

### Q40. [2 Marks] [MSQ]

A compiler optimizes signed integer expressions. In this question, signed overflow traps, division by zero traps, and expressions have no side effects other than such traps. Which replacements preserve both value and whether a trap occurs for every integer x in the representable range?

A. x−x → 0
B. x/x → 1
C. x*0 → 0
D. (x+1)−1 → x

### Q41. [2 Marks] [NAT]

A singly linked structure has nodes0,1,2,3,4,5 and next pointers 0→1→2→3→4→5→2. Floyd's cycle-detection algorithm starts slow=fast=node0. In each iteration, slow advances once and fast twice, then equality is tested. What is the node label at the first equality after an iteration?

**Answer format:** Exact integer.

### Q42. [2 Marks] [NAT]

Disk cylinders range from0 to199. The head is at50 and moves upward. Pending requests are at20,60,90. Under SCAN, service all requests encountered, continue to199 before reversing if requests remain below, and stop as soon as the last pending request is served. Under LOOK, reverse at the largest pending request instead. How many more cylinders does SCAN travel than LOOK for this batch?

**Answer format:** Exact integer.

### Q43. [2 Marks] [NAT]

A segmented memory uses separate base and limit values for each segment. A byte access of length L at offset o is valid iff o≥0 and o+L≤limit. Segment2 has base1000 and limit100. A four-byte word is requested at offset98. How many bytes from the requested word can the processor access before trapping if the whole access is checked atomically before any memory read?

**Answer format:** Exact integer.

### Q44. [2 Marks] [MSQ]

A toy floating-point format has four significant binary bits and round-to-nearest, ties-to-even. It supports all exponents needed below. Which real values round to exactly1.5?

A. 1.4375
B. 1.49
C. 1.5625
D. 1.625

### Q45. [2 Marks] [NAT]

A process references pages A,B,C,A,D,B. There are three initially empty frames. A page fault loads the requested page, and the optimal offline replacement policy evicts the page whose next use is farthest in the future, treating no future use as infinity. How many fewer page faults does this policy incur than FIFO on this trace?

**Answer format:** Exact integer.

### Q46. [2 Marks] [NAT]

A real3×3 matrix A has eigenvalues1,2,4, each once. Define B=A²−3A+2I. What is the rank of B?

**Answer format:** Exact integer.

### Q47. [2 Marks] [NAT]

A sorted data file occupies64 blocks. A sparse primary index has one entry per data block and occupies4 blocks, with16 entries per index block. A second index level has one entry per first-level block and fits in one block. No blocks are cached. A successful point lookup follows the root, one first-level index block, then its data block. Compared with binary search directly on the64 data blocks, whose worst-case successful lookup requires7 block reads, how many block reads are saved in that worst-case comparison?

**Answer format:** Exact integer.

### Q48. [2 Marks] [NAT]

A B+ tree leaf can hold at most four keys and must hold at least two unless it is the root. The root currently has three leaf children with keys [2,4], [6,8], and [10,12,14]. Delete key6. Prefer borrowing from the right sibling if it has more than its minimum; otherwise borrow from the left if possible; otherwise merge with the right. How many leaf children does the root have afterward?

**Answer format:** Exact integer.

### Q49. [2 Marks] [NAT]

A direct-mapped cache has four lines and one word per line. Word address w maps to line w mod4. Starting empty, it accesses words0,4,1,5,0,4,1,5. A fully associative cache of four lines, using LRU and starting empty, sees the same trace. How many misses in the direct-mapped cache are eliminated by the fully associative cache?

**Answer format:** Exact integer.

### Q50. [2 Marks] [NAT]

A queue is implemented using two stacks. Enqueue pushes onto input stack I. Dequeue pops from output stack O; if O is empty, it first transfers every element of I to O, one pop and one push per transferred element. Starting empty, execute enqueue(a), enqueue(b), dequeue, enqueue(c), dequeue, dequeue. How many primitive stack pushes and pops are performed in total?

**Answer format:** Exact integer.

### Q51. [2 Marks] [MSQ]

A constant-propagation pass treats integer comparisons exactly and removes unreachable branches. Integer arithmetic is unbounded. Consider:

```text
x=0;
if x==0 { y=4; } else { y=input(); }
z=y*y;
```

Which statements hold?

A. The call input() is unreachable.
B. z can be replaced by16 after proving the branch condition.
C. It is necessary to execute input() to determine whether z is constant.
D. y is nonconstant solely because one syntactic assignment uses input().

### Q52. [2 Marks] [NAT]

A 0/1 knapsack has capacity6. Items A,B,C have (weight,value) pairs (3,5),(4,7),(2,4). Each item can be selected at most once. A faulty implementation updates its one-dimensional DP array in increasing capacity order for each item, allowing an item to be reused. By how much can its final dp[6] exceed the true optimum, starting with all entries zero and processing items A,B,C in that order?

**Answer format:** Exact integer.

### Q53. [2 Marks] [NAT]

For f(x)=x³−3x on[−2,2], how many points c in the open interval satisfy the mean value theorem equation f'(c)=[f(2)−f(−2)]/4?

**Answer format:** Exact integer.

### Q54. [2 Marks] [NAT]

A divide-and-conquer algorithm splits n distinct elements into two equal halves, recursively finds the maximum of each, and compares the two maxima once. Its base case on one element performs no comparisons. For n=64, how many comparisons could be saved if the algorithm were instead required to return both maximum and minimum and used the optimal pairwise algorithm, compared with running the stated maximum algorithm twice, once with comparisons reversed?

**Answer format:** Exact integer.

### Q55. [2 Marks] [NAT]

A box is chosen uniformly from two boxes, GG containing two gold coins and GS containing one gold and one silver coin. Consider two observation protocols. In protocol U, an inspector picks one coin uniformly and shows it. In protocol P, the inspector always shows a gold coin if the chosen box has one. Under each protocol a gold coin is shown. By how much does P(GG | shown gold, protocol U) exceed P(GG | shown gold, protocol P)?

**Answer format:** Decimal rounded to four places.
### Q56. [2 Marks] [NAT]

A binary code consists of all length4 bit strings having even parity. A codeword is transmitted through a channel where each bit independently flips with probability1/4. What is the probability that at least one bit changes but the received string is another valid codeword?

**Answer format:** Exact decimal.

### Q57. [2 Marks] [MSQ]

Let P be the set of all subsets of {a,b,c}, ordered by inclusion. Remove only {a,b,c}, keeping the other seven elements. Which statements hold in the resulting poset?

A. Every pair still has a greatest lower bound.
B. Every pair still has a least upper bound.
C. The empty set remains the least element.
D. There is a greatest element.

### Q58. [2 Marks] [NAT]

A loop has these basic blocks; variables are integers and input p is read again at each visit to B1.

```text
B1: p=read(); if p goto B2 else B3;
B2: x=x+1; goto B1;
B3: return x;
```

Using standard backward liveness, how many variables among {p,x} are live at the entry of B1, before p=read()?

**Answer format:** Exact integer.

### Q59. [2 Marks] [NAT]

For Boolean variables x,y,z, define F=(x XOR y) AND (y XOR z). How many input triples make F=1?

**Answer format:** Exact integer.

### Q60. [2 Marks] [MSQ]

An algorithm is given a Turing machine M promised to halt on every input and an integer n≥0. Which tasks can be decided by an algorithm that terminates on every promised input?

A. Determine whether M accepts every binary string of length exactly n.
B. Determine whether M accepts at least one binary string of length at most n.
C. Determine whether M accepts every binary string of arbitrary length.
D. Determine whether M accepts no binary strings of arbitrary length.

### Q61. [2 Marks] [NAT]

A database initially has x=100. Transaction T1 adds20 to x and commits. A later transaction T2 reads the committed value, subtracts5, and aborts. Recovery uses transaction rollback to restore T2's before-image; T1 is not undone. What is the recovered value of x?

**Answer format:** Exact integer.

### Q62. [2 Marks] [NAT]

Over alphabet {0,1}, a DFA must accept exactly strings whose length is divisible by3 and whose number of1s is even. What is the minimum number of states in a complete DFA?

**Answer format:** Exact integer.

### Q63. [2 Marks] [NAT]

A DMA controller transfers a block of400 bytes over a shared bus. Each burst transfers20 bytes and holds the bus for5 cycles. Between consecutive bursts it releases the bus for3 cycles, during which the CPU may use it. The first burst begins at cycle0, and no gap follows the last burst. How many cycles elapse before DMA completes?

**Answer format:** Exact integer.

### Q64. [2 Marks] [NAT]

A rooted tree has root r with children a,b,c. Vertex a has two leaf children, b has one leaf child, and c is a leaf. How many different preorder sequences of vertex labels are possible if the order of children at every vertex may be chosen independently? All seven vertex labels are distinct.

**Answer format:** Exact integer.

### Q65. [2 Marks] [NAT]

An ideal single-issue pipeline executes100 instructions in104 cycles, including filling and draining. Of these instructions,20 are conditional branches. A prediction scheme mispredicts exactly25% of those branches; every misprediction introduces3 extra cycles. No other stalls occur. What is the resulting CPI, using total execution cycles divided by100?

**Answer format:** Exact decimal.



---

## ANSWER KEY — MOCK TEST 033

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | B |
| 2 | NAT | 1 | 9.375 |
| 3 | MSQ | 1 | A, C |
| 4 | MCQ | 1 | B |
| 5 | MCQ | 1 | C |
| 6 | NAT | 2 | 6 |
| 7 | NAT | 2 | 2.5 |
| 8 | NAT | 2 | 12 |
| 9 | MCQ | 2 | A |
| 10 | NAT | 2 | 0.4444 (accepted range 0.44435–0.44445) |
| 11 | MSQ | 1 | A, C, D |
| 12 | NAT | 1 | 13 |
| 13 | NAT | 1 | 18 |
| 14 | MCQ | 1 | C |
| 15 | NAT | 1 | 48 |
| 16 | NAT | 1 | 4 |
| 17 | MSQ | 1 | A, B, D |
| 18 | MCQ | 1 | B |
| 19 | NAT | 1 | 5 |
| 20 | MSQ | 1 | A, C |
| 21 | MCQ | 1 | D |
| 22 | MSQ | 1 | A, D |
| 23 | NAT | 1 | 0 |
| 24 | MCQ | 1 | B |
| 25 | NAT | 1 | 1 |
| 26 | NAT | 1 | 7 |
| 27 | MCQ | 1 | D |
| 28 | NAT | 1 | 3 |
| 29 | NAT | 1 | 6.8 |
| 30 | NAT | 1 | 8 |
| 31 | MSQ | 1 | A, C |
| 32 | MSQ | 1 | A, B, D |
| 33 | NAT | 1 | 45055 |
| 34 | NAT | 1 | 0.9 |
| 35 | NAT | 1 | 10 |
| 36 | MSQ | 2 | A, C |
| 37 | NAT | 2 | 3 |
| 38 | NAT | 2 | 4 |
| 39 | NAT | 2 | 5.75 |
| 40 | MSQ | 2 | A, C |
| 41 | NAT | 2 | 4 |
| 42 | NAT | 2 | 218 |
| 43 | NAT | 2 | 0 |
| 44 | MSQ | 2 | A, B, C |
| 45 | NAT | 2 | 0 |
| 46 | NAT | 2 | 1 |
| 47 | NAT | 2 | 4 |
| 48 | NAT | 2 | 3 |
| 49 | NAT | 2 | 4 |
| 50 | NAT | 2 | 12 |
| 51 | MSQ | 2 | A, B |
| 52 | NAT | 2 | 1 |
| 53 | NAT | 2 | 2 |
| 54 | NAT | 2 | 32 |
| 55 | NAT | 2 | 0.1667 (accepted range 0.16665–0.16675) |
| 56 | NAT | 2 | 0.21484375 |
| 57 | MSQ | 2 | A, C |
| 58 | NAT | 2 | 1 |
| 59 | NAT | 2 | 2 |
| 60 | MSQ | 2 | A, B |
| 61 | NAT | 2 | 120 |
| 62 | NAT | 2 | 6 |
| 63 | NAT | 2 | 157 |
| 64 | NAT | 2 | 12 |
| 65 | NAT | 2 | 1.19 |

