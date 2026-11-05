# GATE CS 2027 — Full-Length Mock Test 016

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

Q1–Q5 and Q11–Q35 carry one mark each; all other questions carry two marks each. MCQs have exactly one correct option. MSQs require all correct options and have no partial credit. Incorrect MCQs incur a penalty equal to one-third of their marks; incorrect MSQ/NAT answers and unattempted questions score zero. General Aptitude contributes 15 marks, Engineering Mathematics 13, and core CS 72. Numerical answers are exact unless a rounding format is explicitly given.

## Section A — General Aptitude

### Q1. [1 Mark] [NAT]

A factory produces 300 units with a 2% defect rate and another 200 units with a 5% defect rate. What percentage of the combined output is defective?

**Answer format:** Exact finite decimal percentage, without the percent sign.

### Q2. [1 Mark] [MCQ]

A point initially at (2,0) is reflected first across the line y=x and then across the line x=1. What are its final coordinates?

A. (2,2)
B. (0,0)
C. (0,2)
D. (2,−2)

### Q3. [1 Mark] [MCQ]

Which sequence correctly orders an evidence-based correction: P, test the revised version; Q, identify the error; R, revise the faulty step; S, compare the original result with the requirement?

A. P–R–Q–S
B. S–Q–R–P
C. R–S–P–Q
D. Q–P–S–R

### Q4. [1 Mark] [NAT]

A fair six-sided die is rolled twice independently. What is the probability that the second result exceeds the first? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q5. [1 Mark] [MCQ]

“The proposed change is reversible: the previous configuration can be restored.” Which meaning of reversible applies?

A. Impossible to undo.
B. Capable of being undone.
C. Required to happen twice.
D. Unrelated to the previous configuration.

### Q6. [2 Marks] [NAT]

An investment grows by the same annual factor for two years, reaching 144% of its original value. In a third year it falls by 25%. What is its final value as a percentage of its original value?

**Answer format:** Integer percentage, without the percent sign.

### Q7. [2 Marks] [MCQ]

A company observes that all of its highest-selling products received heavy advertising. Which additional comparison most directly helps assess whether advertising raised sales rather than merely being assigned to products already expected to sell well?

A. Comparable products with similar pre-advertising sales but different advertising exposure.
B. Only the names of the highest-selling products.
C. The colour of the advertising department's walls.
D. A list excluding every low-advertising product.

### Q8. [2 Marks] [NAT]

A 5×5 grid of unit squares is rotated by 90 degrees about its centre. How many distinct orbits of squares are there under repeated applications of this rotation? Squares in the same orbit count once.

**Answer format:** Integer.

### Q9. [2 Marks] [NAT]

Let a1=1 and a(n+1)=a(n)+n². Find a5.

**Answer format:** Integer.

### Q10. [2 Marks] [NAT]

Two concentric circles have radii 5 and 3. A straight chord of the larger circle is tangent to the smaller circle. What is the chord's length?

**Answer format:** Integer.

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

A constant-propagation analysis proves x=4 on every feasible path reaching `y=3*x-2`. Arithmetic is exact. What replacement for the right-hand side is justified?

A. 12
B. 10
C. 2
D. No constant replacement can ever be made.

### Q12. [1 Mark] [NAT]

An unlimited supply of coins of denominations 1 and 3 is used to make amount 5. If order matters, how many sequences of coins have total value 5?

**Answer format:** Integer.

### Q13. [1 Mark] [NAT]

A fair coin and a double-headed coin are selected with equal probability. The selected coin is tossed twice and both outcomes are heads. What is the probability that a third toss of the same coin is heads?

**Answer format:** Exact finite decimal.

### Q14. [1 Mark] [MCQ]

A system's measured cache hit rate rises after an optimization, but its clock period also increases. Which conclusion is justified without further data?

A. Total execution time necessarily decreases.
B. Hit rate alone is insufficient to establish an execution-time improvement.
C. The instruction count must become zero.
D. A higher hit rate necessarily implies a shorter clock period.

### Q15. [1 Mark] [NAT]

An algorithm partitions a size-27 input into three equal subproblems at each nontrivial call, stopping at size one. How many internal calls occur in its complete recursion tree?

**Answer format:** Integer.

### Q16. [1 Mark] [NAT]

Among the positive divisors of 12 ordered by divisibility, what is the maximum size of an antichain?

**Answer format:** Integer.

### Q17. [1 Mark] [MSQ]

For A with rows (0,1),(1,0), which statements are true?

A. A is nonsingular.
B. A has an LU factorization with unit-diagonal lower-triangular L and upper-triangular U without any row permutation.
C. Swapping the rows permits such an LU factorization.
D. Every nonsingular matrix must permit elimination without pivoting.

### Q18. [1 Mark] [MCQ]

An HTTP cache has two stored representations of the same URL, selected by different values of a request header named in Vary. Why must that header be considered during lookup?

A. The same URL can require different cached representations depending on that header.
B. Vary means every cached representation has an infinite lifetime.
C. HTTP never uses request headers.
D. The header changes the TCP sequence-number arithmetic.

### Q19. [1 Mark] [MCQ]

A recognizer accepts every member of L and may loop on nonmembers. Which extra guarantee would make that same machine a decider for L?

A. It uses at least two tape symbols.
B. It halts on every input, rejecting every nonmember.
C. It accepts one input quickly.
D. It has a finite written description.

### Q20. [1 Mark] [NAT]

A 16 KiB cache has four ways and 64-byte lines. How many sets does it have? Count data capacity only; 1 KiB=1024 bytes.

**Answer format:** Integer.

### Q21. [1 Mark] [MCQ]

A memory allocator has two nonadjacent free holes of 40 bytes each, but no free hole of 60 bytes. A request needs a contiguous 60-byte block. What explains failure despite 80 free bytes in total?

A. External fragmentation.
B. Internal fragmentation inside the requested block before it is allocated.
C. A necessary arithmetic overflow.
D. The existence of exactly two CPU cores.

### Q22. [1 Mark] [MSQ]

A page has been modified in memory since it was loaded from disk. Which statements about replacement are correct in an ordinary write-back paging system?

A. Its dirty status may require writing its current contents to backing storage before its frame is reused.
B. A clean page with an unchanged backing copy may be discarded without such a write.
C. Every page fault proves the evicted page was dirty.
D. Dirty status alone determines which page every replacement policy must choose.

### Q23. [1 Mark] [MCQ]

A transport-layer port number is primarily used to distinguish what?

A. Application endpoints on a host.
B. Individual bits within one Ethernet frame.
C. Physical pins on a memory chip.
D. Cache-line offsets inside a processor.

### Q24. [1 Mark] [NAT]

Evaluate ∫₀¹ x/(1+x²) dx, rounded to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q25. [1 Mark] [NAT]

A B+ tree internal node contains six separator keys. Under the usual k-keys/k+1-children rule, how many child pointers does it contain?

**Answer format:** Integer.

### Q26. [1 Mark] [MCQ]

A transfer transaction subtracts from one account but crashes before adding to the other. Recovery leaves the subtraction permanent while undoing no part and completing no addition. Which transaction property is directly broken?

A. Atomicity.
B. A requirement that all transactions be read-only.
C. A requirement that every table contain one row.
D. No property because part of the transaction succeeded.

### Q27. [1 Mark] [NAT]

A directory contains three hard links to the same ordinary file. One link is removed. How many directory hard links to that file remain, assuming no other changes?

**Answer format:** Integer.

### Q28. [1 Mark] [MSQ]

Which Boolean expressions equal x for all x,y?

A. x+xy
B. x(x+y)
C. x+y
D. x XOR x

### Q29. [1 Mark] [NAT]

An empty stack processes push(1),push(2),pop,push(3),pop,pop. What is the sum of the three popped values?

**Answer format:** Integer.

### Q30. [1 Mark] [MCQ]

A DMA transfer completes while the CPU executes unrelated instructions. What mechanism can notify the CPU without requiring it to poll continuously?

A. A completion interrupt.
B. Deleting every CPU register.
C. Changing every virtual address to zero.
D. Disabling the device permanently before completion.

### Q31. [1 Mark] [MCQ]

In `x=1; x=2; print(x);`, the first assignment has no side effects apart from storing x. Why may it be removed?

A. Its value is overwritten before any use.
B. Every assignment of the constant one is invalid.
C. print never reads its argument.
D. The second assignment must also be removed.

### Q32. [1 Mark] [NAT]

A Karnaugh-map group contains eight minterms of a four-variable function and forms a valid Boolean cube. How many literals remain in its product term?

**Answer format:** Integer.

### Q33. [1 Mark] [MCQ]

Which word belongs to (ab|ba)* but not to (ab)*?

A. abab
B. baab
C. aabb
D. aaa

### Q34. [1 Mark] [NAT]

Five nonnegative real observations have total 20. What is the greatest possible median? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q35. [1 Mark] [NAT]

A tree has ten vertices. What is the sum of its vertex degrees?

**Answer format:** Integer.

### Q36. [2 Marks] [NAT]

A five-stage pipeline has stage logic delays 1,2,3,4,5 ns and a 0.2 ns latch overhead per stage. Its longest stage is split into two 2.5 ns logic stages, producing six stages. Both designs issue one instruction per cycle without hazards. For a batch of twenty instructions starting with an empty pipeline, what is the ratio of old completion time to new completion time? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q37. [2 Marks] [MSQ]

For grammar S→SS | a | ε, which statements are true?

A. Its language is a*.
B. The word a has infinitely many distinct parse trees.
C. Every generated word has exactly one parse tree.
D. The grammar is LL(1) as written.

### Q38. [2 Marks] [NAT]

A byte-addressed processor fetches instructions of lengths 2 or 4 bytes. Starting at address 100, it executes a 2-byte instruction, a 4-byte instruction, and then a 2-byte PC-relative branch. The branch target is computed from the next-instruction address plus a signed displacement measured in two-byte units. The branch displacement is −3. What is the target byte address?

**Answer format:** Integer.

### Q39. [2 Marks] [MSQ]

A transaction's lock sequence is lock-S(A), lock-X(B), unlock-S(A), lock-S(C), commit, unlock-X(B), unlock-S(C). Use basic two-phase locking to mean that no new lock is acquired after the first unlock. Use strictness to mean that exclusive locks are held until commit or abort. Which statements are correct?

A. The sequence violates basic two-phase locking.
B. The sequence obeys basic two-phase locking because X(B) is held until commit.
C. Its exclusive-lock release satisfies the specified strictness condition.
D. Holding X(B) until commit repairs every possible two-phase-locking violation automatically.

### Q40. [2 Marks] [MCQ]

A DFS of a directed graph has discovery/finish intervals u:[2,11] and v:[4,7]. Edge u→v exists but is not a tree edge. How is it classified under standard DFS edge categories?

A. Back edge.
B. Forward edge.
C. Cross edge.
D. Impossible because intervals may never nest.

### Q41. [2 Marks] [NAT]

A Boolean cover must cover columns {1,2,3}. Available implicants are P covering {1,2} at cost 3, Q covering {2,3} at cost 2, R covering {1} at cost 1, and S covering {3} at cost 1. Costs add, and any subset of implicants may be chosen. What is the minimum total cover cost?

**Answer format:** Integer.

### Q42. [2 Marks] [MCQ]

A BST has root 40, with left child 20 and right child 60. Node 60 has left child 50; node 50 has left child 45; node 45 has right child 47. All unspecified child links are null. Delete key 40 by copying its inorder successor's key into the root and then removing the successor's original node, reconnecting that node's child if necessary. In the resulting tree, what are respectively the parent key of node 47 and the inorder successor key of 47?

A. (45,50)
B. (50,50)
C. (50,60)
D. (45,60)

### Q43. [2 Marks] [NAT]

A stream encodes records as one unsigned length byte L followed by L payload bytes. A zero length marks the end and contributes no payload. The stream is read in arbitrary chunks. Successful reads return the byte sequences [3,65,66], then [67,2], then [68,69,0], in that order. Between the first two successful reads, a call returns −1 with EINTR and consumes no bytes; the program retries. A correct parser retains incomplete records across reads. How many payload bytes belong to complete records before the end marker?

**Answer format:** Integer.

### Q44. [2 Marks] [NAT]

How many subgroups of the permutation group S3 are abelian? Include the trivial subgroup and count distinct subgroups, not isomorphism types.

**Answer format:** Integer.

### Q45. [2 Marks] [NAT]

A connected weighted graph has exactly five edges forming a five-vertex cycle with successive edge weights 2,7,3,6,4. What is the additional cost of a minimum-weight spanning tree constrained to include the weight-7 edge, compared with an unconstrained MST?

**Answer format:** Integer.

### Q46. [2 Marks] [MCQ]

A directed graph has edges s→a of weight 1, a→b of weight 0, b→a of weight 0, and b→t of weight 2. Walks may revisit vertices. Which statement is correct?

A. The shortest s-to-t walk weight is unbounded below.
B. The shortest weight is 3 and only one shortest walk exists.
C. The shortest weight is 3 and infinitely many shortest walks exist.
D. No walk from s to t exists.

### Q47. [2 Marks] [NAT]

A graph consists of a cycle on five vertices and one additional vertex adjacent to all five cycle vertices. What is its chromatic number?

**Answer format:** Integer.

### Q48. [2 Marks] [NAT]

How many distinct arrangements of AAABBBCCC have no two A symbols adjacent? Identical letters are indistinguishable.

**Answer format:** Integer.

### Q49. [2 Marks] [MSQ]

Consider `p=A[i]; A[j]=7; q=A[i];` with valid indices, no other changes, and exact ordinary array storage. Which statements are correct?

A. If i≠j is proved, the final load may be replaced by p.
B. With no relation known between i,j, the final load may always be replaced by p.
C. If i=j is proved, the final load's value is 7.
D. The store can never affect any later load from A.

### Q50. [2 Marks] [NAT]

In a four-bit adder, each propagate signal P_i=A_i XOR B_i is available at time 2, each generate G_i=A_i AND B_i at time 1, and input carry C0 at time 0. AND and OR gates each add one unit delay, with unlimited fan-in. A ripple implementation uses C_(i+1)=G_i OR (P_i AND C_i). A lookahead implementation directly forms C4 as the OR of its five standard product terms. How many delay units earlier is C4 available with lookahead than with ripple? Use the latest-input timing bound for every gate.

**Answer format:** Integer.

### Q51. [2 Marks] [MCQ]

A full-adder sum bit is implemented using a 4-to-1 mux with select bits a,b and remaining input c. Which data inputs (D0,D1,D2,D3) are correct?

A. (0,c,c,1)
B. (c,c′,c′,c)
C. (c′,c,c,c′)
D. (0,0,1,1)

### Q52. [2 Marks] [NAT]

A 10,000-bit payload is split into k equal packets, each with a 100-bit header, and sent through two equal-rate links via a store-and-forward router. Both links have rate R, propagation is negligible, links can work concurrently, and packets are transmitted back-to-back. k is a positive integer dividing 10,000. What k minimizes completion time of the final packet?

**Answer format:** Integer.

### Q53. [2 Marks] [NAT]

A sequential detector outputs one exactly when the prefix read so far ends in 101; otherwise it outputs zero. Overlapping occurrences are detected. Starting with no input history, how many one outputs occur while reading 1010101, one bit per clock?

**Answer format:** Integer.

### Q54. [2 Marks] [MSQ]

A nondeterministic PDA can make epsilon moves and may have infinite branches. Which statements about searching its computation tree are true?

A. Breadth-first search will eventually find an accepting computation if one exists with finitely many transitions, assuming finite branching.
B. Naive depth-first search that never backtracks from an infinite branch always finds every accepting computation.
C. An epsilon loop can trap such a depth-first search despite another accepting branch.
D. Breadth-first search necessarily halts and rejects every nonmember of every context-free language without any further algorithmic construction.

### Q55. [2 Marks] [NAT]

A ternary relationship R(A,B,C) uses domains of sizes 2,3,4 respectively. Constraints require that each pair (A,B) determines at most one C and each pair (A,C) determines at most one B. What is the maximum possible number of relationship tuples?

**Answer format:** Integer.

### Q56. [2 Marks] [MSQ]

Let L be a language that is not context-free. Which statements are true?

A. Its reversal Lᴿ cannot be context-free.
B. Every homomorphic image of L must be non-context-free.
C. Intersecting L with any regular language must remain non-context-free.
D. A homomorphism erasing every symbol can map L to a regular language.

### Q57. [2 Marks] [NAT]

A single process runs the following pseudocode. Every fork succeeds; the child receives return value zero and the parent a positive value. Each process prints once after the loop.

```text
for i = 0,1,2:
    if fork() == 0:
        break
print(i)
```

A process completing all iterations has i=3 at print time. What is the sum of all printed integers, regardless of output order?

**Answer format:** Integer.

### Q58. [2 Marks] [NAT]

An eight-bit one's-complement checksum adds bytes 0xFE and 0x02 using end-around carry, then complements the resulting eight bits. What unsigned integer is the checksum?

**Answer format:** Integer.

### Q59. [2 Marks] [MCQ]

A programming language permits arbitrarily nested comments, with tokens OPEN and CLOSE marking comment boundaries. Why is a fixed finite-state lexer, with no extra stack or counter, insufficient to recognize exactly the balanced comment sequences of unbounded depth?

A. It would need to distinguish arbitrarily many outstanding OPEN counts.
B. Every finite input requires infinitely many processing steps.
C. The two-token alphabet is infinite.
D. All non-nested comments are also nonregular by definition.

### Q60. [2 Marks] [NAT]

Under set semantics, R(A,B)={(1,x),(1,y),(2,x),(3,z)} and S(B)={x,y}. How many A values are in π_A(R)−π_A(R⋈S), where the natural join uses B?

**Answer format:** Integer.

### Q61. [2 Marks] [NAT]

A binary min-heap with fifteen distinct keys uses array indices 1–15. Across all valid assignments of those keys to a heap, how many different indices can contain the third-smallest key?

**Answer format:** Integer.

### Q62. [2 Marks] [NAT]

A sequence satisfies a0=0 and a_n=2a_(n−1)+n for n≥1. Find lim as n→∞ of a_n/2ⁿ.

**Answer format:** Integer.

### Q63. [2 Marks] [NAT]

An undirected simple graph has 64 vertices and m edges. Compare a bit-packed adjacency matrix of exactly 64² bits with an adjacency-list representation using 32 bits for each of 65 header/offset entries and 16 bits for each of the 2m neighbour entries. Ignore all other overhead. What is the smallest integer m for which the matrix occupies strictly less storage than these lists?

**Answer format:** Integer.

### Q64. [2 Marks] [MSQ]

A bounded-buffer implementation starts empty with semaphores empty=N, full=0, mutex=1, where N>0. The producer executes wait(empty),wait(mutex),insert,signal(mutex),signal(full). The consumer incorrectly executes wait(mutex),wait(full),remove,signal(empty),signal(mutex). Which statements are correct?

A. If the consumer acquires mutex first, it can block on full while preventing the producer from acquiring mutex.
B. The given order is guaranteed deadlock-free because every semaphore is eventually signalled in the source code.
C. Moving the consumer's wait(full) before wait(mutex), leaving its remaining operations in order, removes this particular deadlocking acquisition order.
D. Initializing full to N correctly represents the stated initially empty buffer.

### Q65. [2 Marks] [MCQ]

A four-port Ethernet switch initially has dynamic entries A→1, B→2, C→3 and no entry for D. It learns or updates the source port before forwarding each frame, floods an unknown destination to every port except ingress, and has no entry expiry during this sequence. Four frames arrive in order: (ingress 3, source A, destination B), (ingress 2, source B, destination A), (ingress 3, source C, destination D), (ingress 4, source D, destination C). Which lists their respective egress-port sets?

A. {2}; {3}; {1,2,4}; {3}
B. {2}; {1}; {1,2,4}; {3}
C. {2}; {3}; {1,2,3,4}; {3}
D. {2}; {3}; {4}; {1,2,3}

## ANSWER KEY — MOCK TEST 016

NAT answers are exact except for specified rounded ranges.

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | NAT | 1 | 3.2 |
| 2 | MCQ | 1 | A |
| 3 | MCQ | 1 | B |
| 4 | NAT | 1 | 0.4167 (range 0.41665–0.41675) |
| 5 | MCQ | 1 | B |
| 6 | NAT | 2 | 108 |
| 7 | MCQ | 2 | A |
| 8 | NAT | 2 | 7 |
| 9 | NAT | 2 | 31 |
| 10 | NAT | 2 | 8 |
| 11 | MCQ | 1 | B |
| 12 | NAT | 1 | 4 |
| 13 | NAT | 1 | 0.9 |
| 14 | MCQ | 1 | B |
| 15 | NAT | 1 | 13 |
| 16 | NAT | 1 | 2 |
| 17 | MSQ | 1 | A, C |
| 18 | MCQ | 1 | A |
| 19 | MCQ | 1 | B |
| 20 | NAT | 1 | 64 |
| 21 | MCQ | 1 | A |
| 22 | MSQ | 1 | A, B |
| 23 | MCQ | 1 | A |
| 24 | NAT | 1 | 0.3466 (range 0.34655–0.34665) |
| 25 | NAT | 1 | 7 |
| 26 | MCQ | 1 | A |
| 27 | NAT | 1 | 2 |
| 28 | MSQ | 1 | A, B |
| 29 | NAT | 1 | 6 |
| 30 | MCQ | 1 | A |
| 31 | MCQ | 1 | A |
| 32 | NAT | 1 | 1 |
| 33 | MCQ | 1 | B |
| 34 | NAT | 1 | 6.6667 (range 6.66665–6.66675) |
| 35 | NAT | 1 | 18 |
| 36 | NAT | 2 | 1.1886 (range 1.18855–1.18865) |
| 37 | MSQ | 2 | A, B |
| 38 | NAT | 2 | 102 |
| 39 | MSQ | 2 | A, C |
| 40 | MCQ | 2 | B |
| 41 | NAT | 2 | 3 |
| 42 | MCQ | 2 | B |
| 43 | NAT | 2 | 5 |
| 44 | NAT | 2 | 5 |
| 45 | NAT | 2 | 1 |
| 46 | MCQ | 2 | C |
| 47 | NAT | 2 | 4 |
| 48 | NAT | 2 | 700 |
| 49 | MSQ | 2 | A, C |
| 50 | NAT | 2 | 6 |
| 51 | MCQ | 2 | B |
| 52 | NAT | 2 | 10 |
| 53 | NAT | 2 | 3 |
| 54 | MSQ | 2 | A, C |
| 55 | NAT | 2 | 6 |
| 56 | MSQ | 2 | A, D |
| 57 | NAT | 2 | 6 |
| 58 | NAT | 2 | 254 |
| 59 | MCQ | 2 | A |
| 60 | NAT | 2 | 1 |
| 61 | NAT | 2 | 6 |
| 62 | NAT | 2 | 2 |
| 63 | NAT | 2 | 64 |
| 64 | MSQ | 2 | A, C |
| 65 | MCQ | 2 | A |


