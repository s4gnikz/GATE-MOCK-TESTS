# GATE CS 2027 — Full-Length Mock Test 081

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

Choose the pair that completes the sentence grammatically.

Each of the instruments that ___ damaged during transport ___ now been recalibrated.

A. were; has  
B. was; have  
C. were; have  
D. was; has

### Q2. [1 Mark] [NAT]

An item's marked price is increased by 25%, and the discount is changed from 20% of the old marked price to 30% of the new marked price. By what percentage does its selling price increase?

**Answer format:** Exact decimal percentage, without the % sign.

### Q3. [1 Mark] [MCQ]

Every certified sample was tested. Some tested samples were rejected. Which conclusion must follow?

A. Some certified samples were rejected.
B. Every tested sample was certified.
C. No untested sample was certified.
D. Every rejected sample was certified.

### Q4. [1 Mark] [MCQ]

Unit cubes form four vertical stacks on a 2×2 footprint, with height rows (1,3) and (2,1). Orthogonal projections onto the horizontal plane and the two vertical coordinate planes count overlapping projected squares only once. What is the sum of the areas of these three projections, in square units?

A. 7
B. 11
C. 12
D. 14

### Q5. [1 Mark] [MCQ]

A report states: “Every village whose water supply was tested met the safety standard. Some villages could not be reached during the survey.” Which conclusion is justified by these statements alone?

A. Every village met the safety standard.
B. At least one untested village failed the standard.
C. No tested village failed the standard.
D. The untested villages had safer water than the tested villages.

### Q6. [2 Marks] [MCQ]

Seven distinct people A, B, C, D, E, F and G sit around a circular table. A and B must sit next to each other. Neither C and D nor E and F may sit next to each other. Rotations of an arrangement are identical; reflections are different. How many arrangements are possible?

A. 96  
B. 120  
C. 144  
D. 240

### Q7. [2 Marks] [MSQ]

A dataset contains 1 twice, 3 three times and 7 once. Two additional observations, both equal to x, are added. The resulting mean is 4. Which statements are correct about the resulting eight observations?

A. x=7.  
B. The median is 3.  
C. There is a unique mode, 7.  
D. The range is 6.

### Q8. [2 Marks] [NAT]

Two fair six-sided dice are rolled. Given that their sum is prime, what is the probability that their product is divisible by 3? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q9. [2 Marks] [MCQ]

A report states: “The valve was closed before the pressure was measured. The pressure measurement preceded replacing the gauge. After the replacement, the valve was reopened.” Which event must lie between valve closure and gauge replacement?

A. Reopening the valve.
B. Measuring the pressure.
C. A second valve closure.
D. No event is forced between them.

### Q10. [2 Marks] [NAT]

Three counters are drawn independently with replacement from a box containing one counter of each of four colours. What is the expected number of distinct colours observed?

**Answer format:** Exact decimal.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

A greedy coin algorithm repeatedly takes the largest denomination not exceeding the remaining amount. With denominations1,4,6 and target8, how many more coins does greedy use than an optimal solution?

A. 0
B. 1
C. 2
D. 3

### Q12. [1 Mark] [MSQ]

For the grammar S→aSb | SS | ε, which statements are correct?

A. Every generated string contains equally many a's and b's.
B. Every generated string has all a's before all b's.
C. The string abab is generated.
D. The string ba is generated.

### Q13. [1 Mark] [MCQ]

A pushdown automaton recognizes {a^n b^n : n≥0}. It pushes one marker per a, then pops one per b, rejecting any a after a b. Which extra condition is needed to avoid accepting strings with fewer b's than a's?

A. Accept as soon as the first b is read.
B. At end of input, require that no unmatched a markers remain.
C. Require at least one input symbol.
D. Ignore the stack once any b has been read.

### Q14. [1 Mark] [NAT]

A four-bit ALU performs a logical left shift by one on bit pattern1011, discarding the outgoing most significant bit and filling the low bit with0. Interpret the result as a signed two's-complement integer. What value results?

**Answer format:** Integer.

### Q15. [1 Mark] [MCQ]

A half-adder adds bits x,y without a carry input. Which pair gives (sum,carry)?

A. (x XOR y, x AND y)
B. (x OR y, x XOR y)
C. (x AND y, x OR y)
D. (NOT x, NOT y)

### Q16. [1 Mark] [NAT]

A circuit-switched connection reserves 64 kbit/s continuously for a one-second interval but carries only 40,000 payload bits during that interval. With 1 kbit=1000 bits, what is its payload utilization percentage?

**Answer format:** Exact finite decimal percentage, without the percent sign.

### Q17. [1 Mark] [NAT]

Distinct values1,2,3,4,5 arrive in that order at a single stack. Each value is pushed exactly once and popped exactly once; pushes and pops may be interleaved. How many distinct full output permutations can have4 as their first popped value?

**Answer format:** Integer.

### Q18. [1 Mark] [NAT]

In an ER model, each employee belongs to exactly one department, and each department may have any number of employees. There are12 employees and four departments. How many employee-department relationship instances exist?

**Answer format:** Integer.

### Q19. [1 Mark] [MCQ]

A compiler lowers `if (p) x=a; else x=b; use(x);` to a control-flow graph. What must both branch arms do before the common use(x) block?

A. Define x along their respective paths.
B. Execute both assignments unconditionally in source order.
C. Eliminate the branch condition regardless of its value.
D. Assign the same constant to x in every case.

### Q20. [1 Mark] [NAT]

A file's inode initially has two hard links and one open file descriptor referring to it. Both hard links are removed. There are no other references, and reclamation occurs only when link count and open-reference count are both zero. How many further reference-removing operations are needed before the inode can be reclaimed?

**Answer format:** Integer.

### Q21. [1 Mark] [MSQ]

Which words belong to the language denoted by a*b | ab*?

A. aab
B. abb
C. ab
D. ba

### Q22. [1 Mark] [MCQ]

On an eight-bit two's-complement machine, x has bits 11111011. Define arithmetic right shift as copying the sign bit and logical right shift as inserting zero. What signed values result from one arithmetic right shift and one logical right shift, respectively?

A. −2 and 125
B. −3 and 125
C. −3 and −3
D. −2 and −2

### Q23. [1 Mark] [MCQ]

An undirected connected graph has distinct edge weights except that two edges share a weight. Which assertion is necessarily true?

A. It has at least two minimum spanning trees.
B. Every maximum-weight edge is absent from every minimum spanning tree.
C. Any edge that is uniquely lightest across some cut belongs to every minimum spanning tree.
D. Kruskal's algorithm fails unless all weights are distinct.

### Q24. [1 Mark] [MCQ]

A JK flip-flop is initially 0. Across four successive active clock edges, its (J,K) inputs are (1,0),(1,1),(0,0),(0,1). What are the four successive output values?

A. 1,0,0,0
B. 1,1,1,0
C. 0,1,1,0
D. 1,0,1,0

### Q25. [1 Mark] [NAT]

A machine fetches a 32-bit instruction using a 16-bit-wide memory interface. Each memory transfer takes one cycle and provides two adjacent bytes. The instruction is aligned to a two-byte boundary, and no overlapping or caching occurs. How many cycles are required to fetch it?

**Answer format:** Integer.

### Q26. [1 Mark] [NAT]

R(A,B)={(1,2),(1,3),(2,3)}. Using set semantics, form T(A,C) by joining R(A,B) with a renamed copy R(B,C) on B and projecting on A,C. Rename R's B attribute to C before taking the difference T−R. How many tuples are in this difference?

**Answer format:** Integer.

### Q27. [1 Mark] [MCQ]

A process successfully calls exec to replace its program. Which statement is correct under the usual UNIX process model?

A. Its process identifier changes because a new process is created.
B. All open file descriptors necessarily close.
C. Execution eventually returns to the instruction after the successful exec call.
D. The process keeps its identifier but executes the replacement program.

### Q28. [1 Mark] [NAT]

An Ethernet learning switch has hosts A,B,C on distinct ports1,2,3. Its forwarding table is initially empty. It learns a source address before deciding how to forward that frame. In order, it receives unicast frames A→B, B→A, and C→A. There is no aging or other traffic. How many frame copies in total are transmitted by the switch over its output ports?

**Answer format:** Exact integer.

### Q29. [1 Mark] [MCQ]

On domain {0,1}, let R(x,y) mean x=y. Which pair gives the truth values of ∀x∃y R(x,y) and ∃y∀x R(x,y), in that order?

A. False, false
B. True, false
C. False, true
D. True, true

### Q30. [1 Mark] [NAT]

Let u=(1,2,3)ᵀ, v=(2,−1,0)ᵀ, and A=I+uvᵀ. What is the entry in row2,column1 of A^(−1)?

**Answer format:** Exact signed number.

### Q31. [1 Mark] [NAT]

For x≠1, f(x)=(x³−1)/(x−1). What value must be assigned to f(1) to make f continuous at1?

**Answer format:** Exact number.

### Q32. [1 Mark] [NAT]

Two increasing runs contain four and three distinct keys respectively, with all seven keys different. Every original left-run position precedes every right-run position. Exactly five cross inversions exist, where a cross inversion is a left key greater than a right key. Standard merging compares the first remaining keys, emits the smaller, and stops comparisons as soon as either run is exhausted. What is the minimum possible number of key comparisons?

**Answer format:** Numeric value; integer.

### Q33. [1 Mark] [NAT]

A discrete random variable takes values 0,1,2 with probabilities k,2k,3k respectively. What is P(X≥1)? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q34. [1 Mark] [MCQ]

A rooted binary tree has five distinct node labels. Its preorder traversal is A,B,C,D,E and its postorder traversal is C,B,E,D,A. Left and right child positions are distinguished. How many different binary trees have both of these traversals?

A. 1  
B. 2  
C. 4  
D. 8

### Q35. [1 Mark] [NAT]

A permutation f of {1,2,3,4,5} maps 1→2, 2→3, 3→1, 4→5 and 5→4. How many fixed points does the composition f^2026 have, where the exponent denotes repeated composition?

**Answer format:** Integer.

### Q36. [2 Marks] [MSQ]

In tuple relational calculus, R(x) is a unary relation containing {1,2}. Consider the expression {x | NOT R(x)}, with x ranging over the entire interpretation domain. Which statements hold?

A. Over domain {1,2,3}, its result is {3}.
B. Over domain {1,2,3,4}, its result is still {3}.
C. Its result depends on values outside R, so it is not domain-independent.
D. Replacing the formula by R(x) AND NOT R(x) yields a domain-independent empty result.

### Q37. [2 Marks] [MSQ]

A binary search tree stores distinct keys. An algorithm claims that checking only “each left child is smaller than its parent and each right child is larger” is sufficient to validate the whole BST. Which statements are correct?

A. The local condition is necessary.
B. The local condition is sufficient.
C. A tree with root10, left child5 and5's right child12 is a counterexample to sufficiency.
D. Propagating ancestor-imposed lower and upper bounds can detect the counterexample.

### Q38. [2 Marks] [NAT]

For real a, let f_a(x)=x³−3ax on the closed interval [−1,1]. There is exactly one value of a for which f_a has two distinct global minimizers on that interval. Find a.

**Answer format:** Exact finite decimal.

### Q39. [2 Marks] [MSQ]

A binary min-heap contains distinct keys. Its array uses one-based indexing. Which statements must hold for every heap of at least seven elements?

A. The second-smallest key is at index2 or3.
B. The third-smallest key is necessarily at index4 or5.
C. The parent of a node always has a smaller key than that node.
D. The array is globally sorted in increasing order.

### Q40. [2 Marks] [NAT]

Integers a,b,c,d independently range over the full eight-bit two's-complement range. What is the minimum signed two's-complement width sufficient to represent every exact value of ab−cd, without overflow?

**Answer format:** Integer bits.

### Q41. [2 Marks] [NAT]

Starting from an empty queue, execute enqueue 1, enqueue 2, dequeue, enqueue 3, enqueue 4, dequeue, enqueue 5. Transfer the remaining queue elements to an initially empty stack by repeatedly dequeuing and pushing. Then pop the entire stack and interpret the emitted digits as a decimal integer. What integer is obtained?

**Answer format:** Integer.

### Q42. [2 Marks] [NAT]

A recursive DFS starts at s in a directed graph with edges s→a,s→b,a→c,b→c,c→d. Each adjacency list is processed in alphabetical order. A vertex is marked immediately upon its first visit. How many edges lead to vertices already marked at the moment that edge is examined?

**Answer format:** Integer.

### Q43. [2 Marks] [MSQ]

A binary floating-point system has four significant bits including the leading 1, unbounded exponents, and round-to-nearest with ties to even after each addition. Starting at x=8, perform x=x+0.5 sixteen times. Which statements are correct?

A. The final stored x is 8.  
B. The exact real-arithmetic result would be 16.  
C. Every one of the sixteen additions is exact in this format.  
D. Instead adding 2 to the initial x four times gives stored result 16.

### Q44. [2 Marks] [NAT]

What is the maximum value of x²(1−x) for0≤x≤1? Round to four decimal places.

**Answer format:** Decimal rounded to four places.

### Q45. [2 Marks] [MSQ]

A byte-addressed 16-bit address space contains a 16 KiB chip at 0x0000–0x3FFF and an 8 KiB chip at 0x4000–0x5FFF. Both chips use active-high enables and are fully decoded, with A15 the most significant address bit. Which statements are correct?

A. The 16 KiB chip's enable can be NOT A15 AND NOT A14.
B. The 8 KiB chip's enable can be NOT A15 AND A14, without considering A13.
C. Exactly 32 KiB of the address space is unmapped by these chips.
D. The 8 KiB chip's enable can be NOT A15 AND A14 AND NOT A13.

### Q46. [2 Marks] [MSQ]

A parent creates a pipe and then forks. Both processes initially inherit both pipe ends. The parent closes its own write end and reads until EOF. The child writes some data and then becomes idle without exiting or closing either descriptor. Assume all data already written have been read. Which statements are correct?

A. The parent's next blocking read must return EOF immediately.
B. The child's still-open write descriptor prevents EOF at the parent.
C. Closing the child's read descriptor alone is sufficient to cause EOF at the parent.
D. If the child closes its write descriptor and no other write descriptors exist, the parent can observe EOF.

### Q47. [2 Marks] [NAT]

A cache performs write-through with a write buffer of capacity two pending writes. Stores occur at cycles0,1,2. Each buffered write occupies memory for five cycles, serially, and the first begins immediately at cycle0. A completed write leaves the buffer at the start of its completion cycle; a blocked store can enter then. How many cycles does the third store wait before entering the buffer? Count the in-service write as occupying one buffer slot.

**Answer format:** Integer.

### Q48. [2 Marks] [MCQ]

A directed multigraph has vertices 1,2,3 and the following adjacency matrix, where entry Mij is the number of distinct edges from i to j:

```text
M = [0 2 1]
    [1 0 1]
    [0 1 1].
```

Count the closed walks of length four that never traverse the same directed edge twice. Vertices may repeat, and opposite-direction edges are distinct. The two parallel edges from 1 to 2 are distinguishable. Count ordered edge sequences together with their starting vertex; cyclic rotations are counted separately whenever the resulting ordered sequences differ.

How many such walks exist?

A. 7  
B. 12  
C. 16  
D. 24

### Q49. [2 Marks] [MSQ]

Let L be a language that is not context-free. Which statements are true?

A. Its reversal Lᴿ cannot be context-free.
B. Every homomorphic image of L must be non-context-free.
C. Intersecting L with any regular language must remain non-context-free.
D. A homomorphism erasing every symbol can map L to a regular language.

### Q50. [2 Marks] [NAT]

A box is chosen uniformly from two boxes, GG containing two gold coins and GS containing one gold and one silver coin. Consider two observation protocols. In protocol U, an inspector picks one coin uniformly and shows it. In protocol P, the inspector always shows a gold coin if the chosen box has one. Under each protocol a gold coin is shown. By how much does P(GG | shown gold, protocol U) exceed P(GG | shown gold, protocol P)?

**Answer format:** Decimal rounded to four places.

### Q51. [2 Marks] [MSQ]

Consider exact integers, pure arithmetic, and an arbitrary input n. A compiler proposes moving the division in this loop to just before the loop:

```text
i = 0
while i < n:
    t = 100 / n
    use(t)
    i = i + 1
```

Integer division truncates toward zero; division by zero traps. `use` does not modify n. Which statements are correct?

A. The expression 100/n is loop invariant.
B. Unconditionally hoisting it is semantics-preserving for every integer n.
C. Hoisting it inside a preceding `if n > 0` guard preserves division behaviour and use results.
D. Invariance alone is insufficient to justify evaluating the expression on a path where the original did not evaluate it.

### Q52. [2 Marks] [MCQ]

A compiler may reuse the caller's activation record for a tail call when no work remains after the callee returns and no live local address must survive. Which recursive return expression is eligible under exact integers and ordinary call-by-value semantics, assuming the recursive call otherwise meets these conditions?

A. `return 1 + f(n-1);`
B. `return f(n-1) * n;`
C. `return f(n-1, acc*n);`
D. `return g(f(n-1));`

### Q53. [2 Marks] [NAT]

An IPv4 datagram has total length 2020 bytes, including a 20-byte header. It crosses a link with MTU 820 bytes. Routers use 20-byte headers for all fragments and maximize the data in each fragment subject to IPv4 alignment rules. What is the fragment-offset field of the last fragment, in its encoded eight-byte units?

**Answer format:** Integer.

### Q54. [2 Marks] [NAT]

An undirected graph has edges AB of weight x, BC of weight2, AC of weight5, AD of weight1, and CD of weight4. For how many integer choices x in {0,1,2,3,4,5,6} does the graph have more than one minimum spanning tree?

**Answer format:** Integer.

### Q55. [2 Marks] [MCQ]

A proof for L={aⁿbⁿcⁿ:n≥0} chooses aᵖbᵖcᵖ in the context-free pumping lemma. Why does |vxy|≤p help show every valid decomposition fails for some pumping exponent?

A. It forces v and y both to be empty.
B. It prevents the pumpable region from spanning all three blocks, so pumping changes some counts without changing all three equally, or disrupts the block order.
C. It forces the entire word to have length at most p.
D. It proves the language finite.

### Q56. [2 Marks] [MSQ]

A Boolean function F(x,y,z) satisfies F(x,y,z)=F(x,y,z′) for every assignment. Which statements must hold?

A. z is inessential: the two cofactors at z=0 and z=1 are identical.
B. F can be implemented by a function of x,y alone.
C. F must be constant.
D. Every sum-of-products expression for F must contain a literal z or z′.

### Q57. [2 Marks] [NAT]

A pipe initially contains no bytes and has two open write descriptors referring to its write end, one in P and one in Q. P writes 5 bytes and closes its descriptor. Reader R requests 10 bytes and receives the available 5. R then performs another blocking read while Q still holds its descriptor but never writes. Later Q closes that descriptor. How many bytes does R's second read return upon completion? Assume no signals or errors.

**Answer format:** Exact integer.

### Q58. [2 Marks] [MSQ]

Two threads each execute the following twice, sharing x initially 0:

```text
r = atomic_read(x)    // r is private to this thread
atomic_write(x, r+1)
```

All reads and writes are sequentially consistent, but the read/write pair is not atomic. Each thread preserves its own program order. Which final values of x are possible after both threads finish?

A. 1
B. 2
C. 3
D. 4

### Q59. [2 Marks] [NAT]

An organization owns192.0.2.0/24. The ranges192.0.2.0/26 and192.0.2.192/26 are reserved and cannot be included in a free-space advertisement. What is the minimum number of CIDR prefixes whose union is exactly the remaining addresses?

**Answer format:** Integer.

### Q60. [2 Marks] [NAT]

A directed acyclic graph has edges s→a of weight 4, s→b of weight 2, a→b of weight −3, a→t of weight 4, b→t of weight 2. How many distinct s-to-t paths have total weight at most 4?

**Answer format:** Integer.

### Q61. [2 Marks] [MSQ]

Two Turing machines recognize languages L1,L2 over a finite alphabet, but may loop on nonmembers. Which assertions hold?

A. Nonemptiness of L1 intersect L2 can be recognized by dovetailing simulations on all strings.
B. Running both machines to completion on each string before considering the next always recognizes nonemptiness of their intersection.
C. If both accept some common string, a fair dovetailing search eventually finds one.
D. Failure to find a common accepted string after any finite amount of simulation proves their intersection empty.

### Q62. [2 Marks] [MSQ]

Let L={empty set, {a}, {b}, {c}, {a,c}, {b,c}, {a,b,c}}, ordered by inclusion. Notice that {a,b} is absent. Meets and joins are taken within L. A complement of x is a y with meet(x,y)=empty set and join(x,y)={a,b,c}. An order automorphism is a bijection L->L preserving the order in both directions. Which statements are correct?

A. L is a distributive lattice.  
B. Exactly six elements of L have at least one complement.  
C. L has exactly two order automorphisms.  
D. The join of {a} and {b} is {a,b,c}.

### Q63. [2 Marks] [NAT]

A cache starts empty, has two sets with two ways each, and uses LRU within each set. Block b maps to set b modulo2. Compare reference sequences0,2,4,0,2,4 and0,3,6,0,3,6. Each reference accesses one block, and the cache is reset between sequences. How many more misses occur in the first sequence than in the second?

**Answer format:** Integer.

### Q64. [2 Marks] [MSQ]

Consider `p=A[i]; A[j]=7; q=A[i];` with valid indices, no other changes, and exact ordinary array storage. Which statements are correct?

A. If i≠j is proved, the final load may be replaced by p.
B. With no relation known between i,j, the final load may always be replaced by p.
C. If i=j is proved, the final load's value is 7.
D. The store can never affect any later load from A.

### Q65. [2 Marks] [NAT]

Table A(id) contains rows 1,2,3. Table B(id,v) contains (1,5),(1,NULL),(2,NULL). Evaluate the query under ordinary SQL bag and NULL semantics:

```sql
SELECT COUNT(B.v)
FROM A LEFT JOIN B ON A.id = B.id;
```

What integer does it return?

**Answer format:** Integer.

---

## ANSWER KEY — MOCK TEST 081

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | A |
| 2 | NAT | 1 | 9.375 |
| 3 | MCQ | 1 | C |
| 4 | MCQ | 1 | D |
| 5 | MCQ | 1 | C |
| 6 | MCQ | 2 | A |
| 7 | MSQ | 2 | A, B, D |
| 8 | NAT | 2 | 0.5333 (range 0.53325–0.53335) |
| 9 | MCQ | 2 | B |
| 10 | NAT | 2 | 2.3125 |
| 11 | MCQ | 1 | B |
| 12 | MSQ | 1 | A, C |
| 13 | MCQ | 1 | B |
| 14 | NAT | 1 | 6 |
| 15 | MCQ | 1 | A |
| 16 | NAT | 1 | 62.5 |
| 17 | NAT | 1 | 4 |
| 18 | NAT | 1 | 12 |
| 19 | MCQ | 1 | A |
| 20 | NAT | 1 | 1 |
| 21 | MSQ | 1 | A, B, C |
| 22 | MCQ | 1 | B |
| 23 | MCQ | 1 | C |
| 24 | MCQ | 1 | A |
| 25 | NAT | 1 | 2 |
| 26 | NAT | 1 | 0 (exact) |
| 27 | MCQ | 1 | D |
| 28 | NAT | 1 | 4 |
| 29 | MCQ | 1 | B |
| 30 | NAT | 1 | -4 |
| 31 | NAT | 1 | 3 |
| 32 | NAT | 1 | 6 (exact) |
| 33 | NAT | 1 | 0.8333 (range 0.83325–0.83335) |
| 34 | MCQ | 1 | C |
| 35 | NAT | 1 | 2 |
| 36 | MSQ | 2 | A, C, D |
| 37 | MSQ | 2 | A, C, D |
| 38 | NAT | 2 | 0.25 |
| 39 | MSQ | 2 | A, C |
| 40 | NAT | 2 | 16 |
| 41 | NAT | 2 | 543 |
| 42 | NAT | 2 | 1 |
| 43 | MSQ | 2 | A, B, D |
| 44 | NAT | 2 | 0.1481 (accepted range 0.14805–0.14815) |
| 45 | MSQ | 2 | A, D |
| 46 | MSQ | 2 | B, D |
| 47 | NAT | 2 | 3 |
| 48 | MCQ | 2 | B |
| 49 | MSQ | 2 | A, D |
| 50 | NAT | 2 | 0.1667 (accepted range 0.16665–0.16675) |
| 51 | MSQ | 2 | A, C, D |
| 52 | MCQ | 2 | C |
| 53 | NAT | 2 | 200 |
| 54 | NAT | 2 | 1 |
| 55 | MCQ | 2 | B |
| 56 | MSQ | 2 | A, B |
| 57 | NAT | 2 | 0 |
| 58 | MSQ | 2 | B, C, D |
| 59 | NAT | 2 | 2 |
| 60 | NAT | 2 | 2 |
| 61 | MSQ | 2 | A, C |
| 62 | MSQ | 2 | B, C, D |
| 63 | NAT | 2 | 3 |
| 64 | MSQ | 2 | A, C |
| 65 | NAT | 2 | 1 |
