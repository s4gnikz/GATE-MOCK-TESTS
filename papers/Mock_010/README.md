# GATE CS 2027 — Full-Length Mock Test 010

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

Q1–Q5 and Q11–Q35 carry one mark each. Q6–Q10 and Q36–Q65 carry two marks each. MCQs have exactly one correct option; MSQs have multiple correct options and award no partial credit. An incorrect MCQ loses one-third of its marks. Incorrect MSQs, NATs and unattempted questions score zero. GA contributes 15 marks, Engineering Mathematics 13, and core CS 72. Answer NATs in the stated format. Unless specified, arithmetic is exact and logarithms in algorithmic bounds have any fixed base greater than one.

## Section A — General Aptitude

### Q1. [1 Mark] [MCQ]

“The panel's endorsement was qualified: it supported the proposal provided that the drainage plan was revised.” Here, “qualified” most nearly means:

A. Issued by technically trained people.
B. Unreserved.
C. Subject to a condition.
D. Withdrawn completely.

### Q2. [1 Mark] [NAT]

A positive real number x satisfies log₂x + log₄x = 9. Find x.

**Answer format:** Integer.

### Q3. [1 Mark] [MCQ]

Every one of twelve sampled buses on a route arrived late on a rainy morning. Which conclusion is supported without treating this sample as a proof about every bus?

A. Rain makes every bus on every route late.
B. The observations suggest lateness on this route under these conditions, but do not establish a universal rule.
C. No bus on this route can arrive on time in dry weather.
D. Rain is proven to be the only possible cause of lateness.

### Q4. [1 Mark] [NAT]

A solid cube consists of 27 unit cubes in a 3×3×3 arrangement. All eight corner unit cubes are removed. What is the total surface area exposed to air, including the newly exposed surfaces, in square units?

**Answer format:** Integer.

### Q5. [1 Mark] [NAT]

A sequence starts at 4. Its successive increments are the prime numbers in increasing order, beginning with 2. What is its sixth term?

**Answer format:** Integer.

### Q6. [2 Marks] [NAT]

A rectangular garden is 40 m by 30 m. A path of uniform width runs just inside all four boundaries, leaving a rectangular planted region. If the path occupies 264 m², find its width, which is less than 15 m.

**Answer format:** Integer metres.

### Q7. [2 Marks] [MCQ]

Arrange the sentences into a coherent paragraph.

P. To distinguish these explanations, the researchers repeated the trial with freshly calibrated instruments.
Q. The repeated trial again found the increase, weakening the calibration explanation.
R. The first trial showed a temperature increase, but the team was unsure whether it was real or caused by instrument drift.
S. They therefore concluded that further investigation of the physical cause was warranted.

A. P–R–Q–S
B. R–Q–P–S
C. R–P–Q–S
D. S–R–P–Q

### Q8. [2 Marks] [NAT]

A well-mixed tank contains 10 litres of a 30% salt solution by volume. Two litres are removed and replaced by two litres of pure water. After thorough mixing, the operation is repeated once. What is the final salt percentage? Volumes are additive.

**Answer format:** Exact finite decimal percentage, without the percent sign.

### Q9. [2 Marks] [NAT]

Five distinct presentations A,B,C,D,E occupy five consecutive slots. A must precede B, B must precede C, and D must precede E. There are no other constraints. How many valid schedules exist?

**Answer format:** Integer.

### Q10. [2 Marks] [NAT]

A square sheet occupies 0≤x≤8 and 0≤y≤8. First fold its right half onto its left half along x=4, then fold the upper half of the folded sheet downward along y=4. A hole is punched through every layer at (1,2) in the folded sheet. After unfolding, what is the sum of the x-coordinates of all distinct holes?

**Answer format:** Integer.

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

An unordered file has 1,000 fixed-size records, 25 records per disk block, and no index. A successful equality search scans blocks in a fixed order and stops on the block containing the target record. Each record is equally likely to be the target. What is the expected number of block reads?

**Answer format:** Exact finite decimal.

### Q12. [1 Mark] [MCQ]

An open-addressed hash table of size 10 uses probes h(k,i)=(h₁(k)+4i) mod 10. A key has h₁(k)=1. Which statement is correct?

A. Its probe sequence visits all ten slots before repeating.
B. It visits exactly five slots, so insertion can fail while some slots remain empty.
C. It visits only slot 1.
D. Its sequence depends on the values stored in occupied slots.

### Q13. [1 Mark] [NAT]

A recursive function on a string returns 0 for the empty string; otherwise it returns one plus the value on the suffix obtained by deleting the first character. An implementation makes no tail-call optimization. For an input of length 12, how many activations of this function are simultaneously present at the deepest point, including the base-case activation?

**Answer format:** Integer.

### Q14. [1 Mark] [MSQ]

Let f(n)=n log₂n and g(n)=n^(3/2), for integers n≥2. Which statements are true?

A. f is O(g).
B. g is O(f).
C. f is o(g).
D. f and g are Θ-equivalent.

### Q15. [1 Mark] [MCQ]

A proposed proof applies the regular-language pumping lemma to L={0ⁿ1ⁿ:n≥0}. After choosing w=0ᵖ1ᵖ, it picks the particular decomposition x=ε,y=0,z=0^(p−1)1ᵖ and shows that this decomposition fails when pumped. What must be repaired to make the argument valid?

A. The proof must show failure for every decomposition satisfying |xy|≤p and |y|>0.
B. The proof must show that L is finite.
C. Pumping down is forbidden; only pumping up is permitted.
D. The selected word must have length less than p.

### Q16. [1 Mark] [NAT]

A DMA transfer moves 4 KiB using bursts of 16 bytes. Each burst occupies the memory bus for 3 cycles, and different bursts do not overlap. How many bus cycles are occupied by the transfer? Here 1 KiB=1024 bytes.

**Answer format:** Integer.

### Q17. [1 Mark] [NAT]

A 3×3 matrix A has det(A)=−2. B is formed by interchanging A's first two rows, then multiplying the third column by 3. Find det(B).

**Answer format:** Integer.

### Q18. [1 Mark] [MCQ]

A JK flip-flop is initially 0. Across four successive active clock edges, its (J,K) inputs are (1,0),(1,1),(0,0),(0,1). What are the four successive output values?

A. 1,0,0,0
B. 1,1,1,0
C. 0,1,1,0
D. 1,0,1,0

### Q19. [1 Mark] [NAT]

A disk head is at cylinder 50. Pending requests are at 10,45,55,90. Shortest-seek-time-first scheduling breaks an equal-distance tie in favour of the lower cylinder. No new requests arrive. What total cylinder distance is travelled to serve all requests?

**Answer format:** Integer.

### Q20. [1 Mark] [MSQ]

A language L is recognizable by a Turing machine, and its complement is also recognizable. Which conclusions follow?

A. L is decidable.
B. L must be regular.
C. A decider can interleave simulations of the two recognizers on the same input.
D. Every recognizer for L must halt on every input.

### Q21. [1 Mark] [MCQ]

A binary CRC generator polynomial has nonzero constant term and contains the factor x+1. Which error pattern is guaranteed to be detected, irrespective of its positions within a sufficiently long codeword?

A. Every error with exactly four flipped bits.
B. Every error with an odd number of flipped bits.
C. Every error with any even number of flipped bits.
D. Every nonzero error pattern.

### Q22. [1 Mark] [NAT]

An NFA has states s,a,b,c, start state s, and only c accepting. Its transitions are s —ε→ a, a —ε→ b, b —0→ b, b —1→ c, and c —1→ c. There are no other transitions. How many strings of length three are accepted?

**Answer format:** Integer.

### Q23. [1 Mark] [NAT]

A C array `int a[3][5]` is stored in row-major order, with sizeof(int)=4 bytes. What is the byte offset of a[2][3] from the start of the array?

**Answer format:** Integer.

### Q24. [1 Mark] [NAT]

Three Ethernet stations independently select uniformly from {0,1,2,3} as their backoff counters for one contention attempt. What is the probability that exactly one station selects the smallest counter?

**Answer format:** Exact finite decimal.

### Q25. [1 Mark] [NAT]

For x≠0, let f(x)=(sin(3x)−3x)/x³, with angles in radians. What value should be assigned to f(0) to make f continuous at zero?

**Answer format:** Exact finite decimal.

### Q26. [1 Mark] [MCQ]

For grammar S→aA | bB, A→c | ε, B→c | ε, which statement about predictive parsing is correct?

A. The two ε-productions necessarily cause an LL(1) conflict.
B. The grammar is LL(1); the choice at S is distinguished by a or b, and the nullable choices use the end marker.
C. The common terminal c makes the two alternatives of S indistinguishable.
D. Left recursion prevents predictive parsing.

### Q27. [1 Mark] [NAT]

A syntax-directed translation uses E→E₁−T with E.val=E₁.val−T.val, E→T with E.val=T.val, and T→digit with its numeric value. What value is assigned to the expression 9−3−2 under this grammar?

**Answer format:** Integer.

### Q28. [1 Mark] [NAT]

Independent random variables X and Y each have variance 4. Find Var(2X−3Y+7).

**Answer format:** Integer.

### Q29. [1 Mark] [NAT]

An eight-bit two's-complement fixed-point representation uses four fractional bits. What real number does bit pattern 11101000 represent?

**Answer format:** Exact finite decimal.

### Q30. [1 Mark] [MCQ]

A B+ tree leaf stores at most four keys. An insertion gives the sorted leaf [4,7,9,12,15]. The split rule keeps the first three keys in the left leaf and the final two in the right leaf; it copies the smallest key in the right leaf into the parent. Which key is copied?

A. 9
B. 12
C. 7
D. 15

### Q31. [1 Mark] [NAT]

Three free memory holes, in address order, have sizes 10,6,14 units. First-fit allocation handles requests of size 7 and then 5, splitting holes and performing no coalescing. What is the size of the largest remaining hole?

**Answer format:** Integer.

### Q32. [1 Mark] [NAT]

On the power set of {1,2,3,4}, define X~Y exactly when |X| and |Y| have the same remainder modulo 3. How many equivalence classes does this relation have?

**Answer format:** Integer.

### Q33. [1 Mark] [MSQ]

A real 2×2 matrix A has distinct eigenvalues 2 and −1. Which statements must hold?

A. A²−A−2I=0.
B. A is singular.
C. A is diagonalizable over the real numbers.
D. A must be symmetric.

### Q34. [1 Mark] [NAT]

A pipeline issues one instruction per cycle except for branch-misprediction stalls. Branches are 20% of instructions, 25% of branches are mispredicted, and every misprediction adds four nonoverlapping stall cycles. Ignoring filling and draining, find its average CPI.

**Answer format:** Exact finite decimal.

### Q35. [1 Mark] [MCQ]

A binary floating-point format rounds to nearest, ties to even, with three significant bits including the leading 1. Exponents can represent all values in this question. What is the rounded representation of 1.101₂?

A. 1.10₂
B. 1.11₂
C. 1.00₂
D. 10.0₂

### Q36. [2 Marks] [MCQ]

A language permits a function to return a nested function that refers to its local variable x. Two separate calls to the outer function return functions F and G, capturing different x variables. Both returned functions are called after the outer calls have returned. Which implementation preserves lexical scoping and separate mutable x variables?

A. Put every captured x in the same global cell.
B. Keep each captured environment alive beyond the outer call and associate the appropriate environment with each returned function.
C. Keep only a pointer into the outer function's discarded stack frame.
D. Copy the current value of x anew from the most recent caller whenever F or G is invoked.

### Q37. [2 Marks] [NAT]

For four Boolean inputs a,b,c,d, let F=(a XOR b) AND (b XOR c) AND (c XOR d). How many input assignments make F=1?

**Answer format:** Integer.

### Q38. [2 Marks] [MSQ]

A schedule has operations in this order: w1(X), r2(X), w2(Y), c2, a1. Here ci commits transaction i and ai aborts it; no earlier versions of X are read. Which statements are correct?

A. Transaction 2 reads an uncommitted value.
B. The schedule is recoverable.
C. A cascading-abort requirement arises, but transaction 2 has already committed.
D. The schedule is strict.

### Q39. [2 Marks] [NAT]

A process has four virtual pages numbered 0–3, initially absent from memory, and two frames. It accesses pages 0,1,0,2,1,3,1,2 in that order. Under optimal offline page replacement, what is the minimum possible number of page faults?

**Answer format:** Integer.

### Q40. [2 Marks] [MCQ]

Initially X=Y=0. Transactions perform r1(X), r2(Y), w1(Y=1), w2(X=1), and then both commit. Each read sees the initial value. Which statement is correct?

A. The schedule is conflict serializable in order T1,T2.
B. The schedule is conflict serializable in order T2,T1.
C. The precedence graph has a cycle, and neither serial order reproduces both reads.
D. No conflict exists because the writes target different items.

### Q41. [2 Marks] [NAT]

A machine uses byte addresses. An instruction has a signed eight-bit displacement, measured in four-byte words relative to the address immediately after the instruction. The next-instruction address is 1000 and the displacement field is 11110110₂. What is the effective target byte address?

**Answer format:** Integer.

### Q42. [2 Marks] [MCQ]

Two finite, acyclic, singly linked lists may share a suffix by node identity. Their heads are h1 and h2. Which algorithm finds the first shared node, or reports none, in O(m+n) time and O(1) extra space?

A. Compare only the values stored in corresponding nodes.
B. Measure both lengths, advance the longer list by their difference, then advance both pointers together until they are identical or both null.
C. Return the first pair of nodes having equal stored values, regardless of identity.
D. Reverse one list and return its new head without examining the other list.

### Q43. [2 Marks] [NAT]

A queue is implemented with an input stack and an output stack. Enqueue pushes onto the input stack. Dequeue pops the output stack; if it is empty, all items from the input stack are first moved to it, one pop and one push per item. Count only individual stack pushes and pops. Starting empty, perform enqueue(A), enqueue(B), dequeue, enqueue(C), enqueue(D), dequeue, dequeue. How many stack operations are performed in total?

**Answer format:** Integer.

### Q44. [2 Marks] [NAT]

For grammar S→SS | a, how many distinct parse trees generate the word aaaa? Left and right children are ordered; different orders of expanding nodes in the same tree do not create different trees.

**Answer format:** Integer.

### Q45. [2 Marks] [NAT]

For real x,y≥0 with x+y=6, maximize x²y. What is the maximum value?

**Answer format:** Integer.

### Q46. [2 Marks] [NAT]

A database has 12 projects and 8 engineers. Every project has exactly two distinct assigned engineers; every engineer must be assigned to at least two and at most four projects. What is the maximum possible number of engineers assigned to four projects?

**Answer format:** Integer.

### Q47. [2 Marks] [MSQ]

For F(a,b,c)=Σm(0,1,2,5,6,7), with a the most significant bit in the minterm index, which products are prime implicants? A prime implicant is an implicant from which no literal can be removed while remaining an implicant.

A. a′b′
B. bc′
C. ac
D. b′

### Q48. [2 Marks] [MCQ]

Activities have half-open intervals A=[0,4), B=[1,2), C=[2,3), D=[3,5), E=[4,6). Which statement correctly compares greedy rules for maximizing the number of nonoverlapping activities?

A. Earliest starting time always yields an optimum and selects three here.
B. Earliest finishing time can select B,C,D, while choosing A first limits the total to two.
C. Shortest duration is the only rule that can produce three here.
D. Every maximal compatible set must have the same cardinality.

### Q49. [2 Marks] [MSQ]

Let L={w#wᴿ : w∈{0,1}*}, where # is a separator and wᴿ denotes reversal. Which statements are correct?

A. A deterministic pushdown automaton can recognize L by switching from pushing to matching at #.
B. L is regular because the separator locates its midpoint.
C. Removing # from every word of L produces a context-free language.
D. A finite automaton can always store the entire prefix w because each individual input is finite.

### Q50. [2 Marks] [NAT]

Evaluate `(P && Q) || R` by left-to-right short-circuit rules, where P,Q,R are Boolean comparisons with no side effects. Among the eight possible assignments of truth values to P,Q,R, how many cause exactly two of the three comparisons to be evaluated?

**Answer format:** Integer.

### Q51. [2 Marks] [NAT]

A full binary tree, in which every node has zero or two children, has 19 nodes. Exactly four internal nodes have two leaf children each. How many leaves have a sibling that is an internal node?

**Answer format:** Integer.

### Q52. [2 Marks] [NAT]

A 0/1 knapsack has capacity 7. Four items have (weight,value) pairs (2,6),(3,8),(4,9),(5,12), and each item can be taken at most once. What is the optimal value?

**Answer format:** Integer.

### Q53. [2 Marks] [MSQ]

A basic block is `t=a+b; a=a+1; u=a+b; v=t;`. Arithmetic is exact, and scalar variables have no aliases. Which transformations preserve the final values of a,t,u,v for all initial a,b?

A. Replace `v=t` by `v=a+b-1` after the other statements.
B. Replace `u=a+b` by `u=t`.
C. Replace `u=a+b` by `u=t+1`.
D. Delete `t=a+b` while leaving `v=t` unchanged and without introducing another definition of t.

### Q54. [2 Marks] [NAT]

An ALU implements unsigned eight-bit subtraction A−B by adding A, the bitwise complement of B, and 1. Let A=37 and B=91. What unsigned integer is represented by the retained eight result bits?

**Answer format:** Integer.

### Q55. [2 Marks] [NAT]

A microinstruction controls three mutually exclusive groups containing 5,3 and 9 signals respectively. In each group, at most one signal may be asserted, and “none” is also needed. A fully encoded design gives each group its own minimum-width binary field. There are also four independent control signals represented by one bit each. How many control bits are required, excluding sequencing and address fields?

**Answer format:** Integer.

### Q56. [2 Marks] [MCQ]

An algorithm splits a size-n problem, where n is a power of two, into two half-size subproblems and then merges in Θ(n/log₂n) time for n≥4. Its running time satisfies T(n)=2T(n/2)+Θ(n/log₂n), with constant base cases at n≤2. What is the tight bound?

A. Θ(n)
B. Θ(n log log n)
C. Θ(n log n)
D. Θ(n²)

### Q57. [2 Marks] [NAT]

An undirected network has edges AB=2, AC=7, BC=1, BD=6, CD=2. Node A's link-state database is complete and correct. The edge BC fails and is removed. By how much does the shortest-path distance from A to D increase after recomputation?

**Answer format:** Integer.

### Q58. [2 Marks] [NAT]

In a four-variable Boolean minimization problem, the only ON minterms are 0,1,2,3 and the only don't-care minterms are 8,9,10,11. All remaining minterms are OFF. Variables are a,b,c,d from most to least significant. What is the minimum number of literals in a single product term covering every ON minterm without covering an OFF minterm?

**Answer format:** Integer.

### Q59. [2 Marks] [NAT]

Box A is selected with probability 1/3 and box B with probability 2/3. A contains three red and two blue balls; B contains one red and four blue balls. Two balls are drawn without replacement from the selected box. Given that exactly one is red, what is the probability that the selected box was A? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q60. [2 Marks] [NAT]

In the divisibility poset of positive divisors of 72, how many elements x satisfy gcd(x,12)=6 and lcm(x,12)=72?

**Answer format:** Integer.

### Q61. [2 Marks] [MCQ]

Let L be any context-free language and R any regular language over the same alphabet. Which language is guaranteed to be context-free?

A. L∩R
B. The complement of L
C. The intersection of L with every context-free language
D. The set difference R−L for every such L,R

### Q62. [2 Marks] [NAT]

For A with rows (2,1,1),(4,3,3),(8,7,9), compute a Doolittle factorization A=LU without row swaps, where L has diagonal entries 1. What is L₃₂?

**Answer format:** Integer.

### Q63. [2 Marks] [NAT]

An IPv4 datagram has total length 2020 bytes, including a 20-byte header. It crosses a link with MTU 820 bytes. Routers use 20-byte headers for all fragments and maximize the data in each fragment subject to IPv4 alignment rules. What is the fragment-offset field of the last fragment, in its encoded eight-byte units?

**Answer format:** Integer.

### Q64. [2 Marks] [NAT]

A file-system inode contains four direct block pointers and one single-indirect pointer. Each disk block is 1024 bytes and each pointer is four bytes. No other addressing scheme exists. What is the largest file size in bytes that this inode can address? Indirect-block storage is not part of the file's data.

**Answer format:** Integer.

### Q65. [2 Marks] [MSQ]

A single-threaded process has a pipe with buffered data. It forks, after which both processes retain their inherited read and write descriptors. Neither writes more data. Which statements hold for blocking reads with a positive requested byte count?

A. After the buffered data is drained, the child can receive end-of-file only after all write descriptors referring to the pipe have been closed.
B. Closing only the child's write descriptor necessarily makes the next empty-pipe read return end-of-file while the parent's write descriptor remains open.
C. Closing unused write descriptors in both processes is needed if their intended protocol relies on detecting end-of-file.
D. A read from an empty pipe always returns zero immediately, even with an open writer.

## ANSWER KEY — MOCK TEST 010

NAT answers are exact except for the rounded answer whose accepted range is shown.

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | C |
| 2 | NAT | 1 | 64 |
| 3 | MCQ | 1 | B |
| 4 | NAT | 1 | 54 |
| 5 | NAT | 1 | 32 |
| 6 | NAT | 2 | 2 |
| 7 | MCQ | 2 | C |
| 8 | NAT | 2 | 19.2 |
| 9 | NAT | 2 | 10 |
| 10 | NAT | 2 | 16 |
| 11 | NAT | 1 | 20.5 |
| 12 | MCQ | 1 | B |
| 13 | NAT | 1 | 13 |
| 14 | MSQ | 1 | A, C |
| 15 | MCQ | 1 | A |
| 16 | NAT | 1 | 768 |
| 17 | NAT | 1 | 6 |
| 18 | MCQ | 1 | A |
| 19 | NAT | 1 | 130 |
| 20 | MSQ | 1 | A, C |
| 21 | MCQ | 1 | B |
| 22 | NAT | 1 | 3 |
| 23 | NAT | 1 | 52 |
| 24 | NAT | 1 | 0.65625 |
| 25 | NAT | 1 | -4.5 |
| 26 | MCQ | 1 | B |
| 27 | NAT | 1 | 4 |
| 28 | NAT | 1 | 52 |
| 29 | NAT | 1 | -1.5 |
| 30 | MCQ | 1 | B |
| 31 | NAT | 1 | 14 |
| 32 | NAT | 1 | 3 |
| 33 | MSQ | 1 | A, C |
| 34 | NAT | 1 | 1.2 |
| 35 | MCQ | 1 | A |
| 36 | MCQ | 2 | B |
| 37 | NAT | 2 | 2 |
| 38 | MSQ | 2 | A, C |
| 39 | NAT | 2 | 5 |
| 40 | MCQ | 2 | C |
| 41 | NAT | 2 | 960 |
| 42 | MCQ | 2 | B |
| 43 | NAT | 2 | 15 |
| 44 | NAT | 2 | 5 |
| 45 | NAT | 2 | 32 |
| 46 | NAT | 2 | 4 |
| 47 | MSQ | 2 | A, B, C |
| 48 | MCQ | 2 | B |
| 49 | MSQ | 2 | A, C |
| 50 | NAT | 2 | 6 |
| 51 | NAT | 2 | 2 |
| 52 | NAT | 2 | 18 |
| 53 | MSQ | 2 | A, C |
| 54 | NAT | 2 | 202 |
| 55 | NAT | 2 | 13 |
| 56 | MCQ | 2 | B |
| 57 | NAT | 2 | 3 |
| 58 | NAT | 2 | 1 |
| 59 | NAT | 2 | 0.4286 (range 0.42855–0.42865) |
| 60 | NAT | 2 | 0 |
| 61 | MCQ | 2 | A |
| 62 | NAT | 2 | 3 |
| 63 | NAT | 2 | 200 |
| 64 | NAT | 2 | 266240 |
| 65 | MSQ | 2 | A, C |

