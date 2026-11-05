# GATE CS 2027 — Full-Length Mock Test 012

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

Q1–Q5 and Q11–Q35 carry one mark each; all other questions carry two marks each. Every MCQ has one correct option and every MSQ has multiple correct options. Select all and only correct MSQ options; no partial credit is awarded. Incorrect MCQs lose one-third of their marks. Incorrect MSQ/NAT answers and unattempted questions receive zero. General Aptitude, Engineering Mathematics and core CS contribute 15,13,72 marks respectively. NAT rounding instructions apply only where stated.

## Section A — General Aptitude

### Q1. [1 Mark] [NAT]

A sequence starts with 3. To obtain successive terms, alternately multiply by 2 and subtract 1, starting with multiplication. What is its seventh term?

**Answer format:** Integer.

### Q2. [1 Mark] [NAT]

A right triangle has perpendicular sides 6 cm and 8 cm. What is the altitude from its right-angle vertex to its hypotenuse?

**Answer format:** Exact finite decimal centimetres.

### Q3. [1 Mark] [MCQ]

Which sentence unambiguously states that Meera checked the figures before submitting the report?

A. Before submitting the report, the figures were checked by Meera.
B. Before Meera submitted the report, she checked the figures.
C. The figures submitted the report after Meera checked them.
D. Having been submitted, Meera checked the report's figures.

### Q4. [1 Mark] [NAT]

In a company, 60% of employees work remotely. Of the remote employees, 25% work part-time. Of the remaining employees, 10% work part-time. What percentage of all employees work part-time?

**Answer format:** Integer percentage, without the percent sign.

### Q5. [1 Mark] [MCQ]

Exactly one of statements P and Q is true. P says “The key is in drawer 1.” Q says “The key is not in drawer 2.” The key is in exactly one of drawers 1,2,3. Where is it?

A. Drawer 1
B. Drawer 2
C. Drawer 3
D. The premises permit all three drawers.

### Q6. [2 Marks] [MCQ]

A point initially at (1,2,3) is first rotated 90 degrees about the z-axis by the rule (x,y,z)→(−y,x,z). It is then rotated 90 degrees about the x-axis by the rule (x,y,z)→(x,−z,y). What is the final point?

A. (−2,−3,1)
B. (−3,1,−2)
C. (2,3,1)
D. (−2,3,−1)

### Q7. [2 Marks] [MCQ]

“A survey found that residents near parks reported more exercise. The survey did not record whether those residents had chosen their neighbourhoods because they already exercised regularly.” Which limitation is most directly identified?

A. Park proximity and exercise were measured in different units.
B. Pre-existing exercise preferences may influence residential location, so the survey alone cannot establish the direction of causation.
C. The survey proves that parks reduce exercise.
D. Self-selection is impossible in residential choices.

### Q8. [2 Marks] [NAT]

Four distinct couples sit around a circular table in eight equally spaced seats. Each person's partner must sit directly opposite. Arrangements differing only by rotation are identical; mirror images are distinct. How many arrangements are possible?

**Answer format:** Integer.

### Q9. [2 Marks] [NAT]

A service centre completed 18 of 20 jobs on Monday and 12 of 20 on Tuesday. On Wednesday it completes every job it receives. What is the minimum number of Wednesday jobs needed to make the combined three-day completion rate at least 80%?

**Answer format:** Integer.

### Q10. [2 Marks] [NAT]

A rectangular paper strip extends from x=0 to x=12. It is folded at x=6 so the right half lies on the left. A cut through all layers removes the closed interval 1≤x≤2 from the folded strip, across its full width. After unfolding, how many connected pieces of paper remain? Ignore zero-width boundaries.

**Answer format:** Integer.

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

A disk scheduler uses LOOK, moving toward increasing cylinder numbers. The head is at 40; pending requests are 10,30,55,70. No further requests arrive. Which service order follows?

A. 55,70,30,10
B. 30,10,55,70
C. 55,30,70,10
D. 70,55,30,10

### Q12. [1 Mark] [MSQ]

An IP packet traverses two Ethernet links through an IP router, with no tunnelling. Which statements hold?

A. The router normally constructs a new link-layer frame for the outgoing link.
B. The incoming Ethernet destination address must remain the outgoing Ethernet destination address.
C. End-to-end IP addressing and hop-local link-layer addressing serve different scopes.
D. Ethernet framing removes the need for an IP destination address across routed networks.

### Q13. [1 Mark] [NAT]

An eight-bit ALU performs logical right shift on the bit pattern 10010110 by two positions, inserting zeros. What unsigned integer does the result represent?

**Answer format:** Integer.

### Q14. [1 Mark] [MCQ]

In C, let `int a[4]={2,4,6,8}; int *p=a+1;`. Which expression evaluates to 6 without undefined behaviour?

A. *p++
B. *(p+1)
C. *p+1
D. *(p-1)

### Q15. [1 Mark] [NAT]

A sorted file has 64 data blocks. A sparse primary index has one entry per data block and fits in a single memory-resident index block. A key search uses that index to identify the correct data block; keys are distinct. How many disk block reads are needed to retrieve a present record, assuming the data block is not cached?

**Answer format:** Integer.

### Q16. [1 Mark] [MCQ]

In an activation record, which link is normally used to restore the caller's activation when a procedure returns, regardless of lexical nesting?

A. The dynamic link.
B. The static link in every case.
C. A pointer to the global symbol table.
D. A pointer to the first heap object.

### Q17. [1 Mark] [MSQ]

For Boolean variables x,y, which expressions equal x XOR y for all inputs?

A. x′y + xy′
B. (x+y)(x′+y′)
C. xy + x′y′
D. x+y

### Q18. [1 Mark] [NAT]

For n=1024, a loop starts with i=n and repeatedly replaces i by floor(√i), stopping when i≤1. How many replacements are made? The square root is exact before taking the floor.

**Answer format:** Integer.

### Q19. [1 Mark] [MCQ]

In a four-variable Karnaugh map, why are columns labelled 00,01,11,10 rather than 00,01,10,11?

A. Every pair of horizontally adjacent columns, including wraparound, then differs in exactly one bit.
B. Binary numbers must always be written in Gray-code order.
C. The order changes the function's truth table values.
D. Adjacent columns must differ in both bits.

### Q20. [1 Mark] [NAT]

A circuit-switched connection reserves 64 kbit/s continuously for a one-second interval but carries only 40,000 payload bits during that interval. With 1 kbit=1000 bits, what is its payload utilization percentage?

**Answer format:** Exact finite decimal percentage, without the percent sign.

### Q21. [1 Mark] [MCQ]

Which language is regular?

A. {aⁿbⁿ : n≥0}
B. {aᵖ : p is prime}
C. {aⁿbᵐ : n,m≥0 and n is even}
D. {ww : w∈{0,1}*}

### Q22. [1 Mark] [NAT]

A circular singly linked list has a sentinel H and three data nodes A,B,C, with links H→A→B→C→H. Execute `B.next = B.next.next`, without freeing any node. How many data nodes remain reachable by following next from H before returning to H?

**Answer format:** Integer.

### Q23. [1 Mark] [MCQ]

Coins of denominations 1,3,4 are available without limit. For amount 6, which statement correctly evaluates the rule “repeatedly choose the largest coin not exceeding the remaining amount”?

A. It uses two coins and is optimal.
B. It uses three coins, whereas an optimal solution uses two.
C. It cannot make amount 6 at all.
D. Every feasible solution uses three coins.

### Q24. [1 Mark] [NAT]

A discrete random variable takes values 0,1,2 with probabilities k,2k,3k respectively. What is P(X≥1)? Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q25. [1 Mark] [MCQ]

Two control-unit designs implement the same instruction-set behaviour. One stores sequences of control words in a control memory; the other generates signals through fixed combinational/sequential logic. Which statement is correct?

A. The first is microprogrammed; changing its control words may change instruction sequencing without redesigning all control logic.
B. The first cannot contain any sequencing logic.
C. The second must fetch a microinstruction from control memory every cycle.
D. Both designs must expose the same internal control-word format to application programs.

### Q26. [1 Mark] [NAT]

A circular queue uses an array of length eight and reserves one slot to distinguish full from empty. Front points to the next item to remove and rear to the next slot to fill. If front=6 and rear=3, how many items are present?

**Answer format:** Integer.

### Q27. [1 Mark] [MCQ]

Three-address code evaluates `(a+b)*(a+b)` with exact scalar arithmetic and unchanged operands. Which sequence computes it using only two arithmetic operations?

A. t=a+b; r=t*t
B. t=a*b; r=t+t
C. t=a+a; r=t*b
D. t=a+b; r=t+b

### Q28. [1 Mark] [NAT]

Let R={(1,2),(2,3),(3,1)}. Its composition R∘R contains (x,z) when some y satisfies (x,y)∈R and (y,z)∈R. How many pairs belong to R∩(R∘R)?

**Answer format:** Integer.

### Q29. [1 Mark] [NAT]

A paging system uses 4 KiB pages. A process requires 9,000 bytes of contiguous virtual storage starting at a page boundary. How many bytes of internal fragmentation are present in its allocated final page if all required pages are allocated?

**Answer format:** Integer bytes; 1 KiB=1024 bytes.

### Q30. [1 Mark] [NAT]

A real 6×6 matrix A satisfies A²=0. What is the largest possible rank of A?

**Answer format:** Integer.

### Q31. [1 Mark] [MSQ]

A function f is continuous on [0,2], differentiable on (0,2), and satisfies f(0)=f(2)=1. Which conclusions must hold?

A. Some c∈(0,2) satisfies f′(c)=0.
B. f is constant on [0,2].
C. f attains both a maximum and a minimum on [0,2].
D. f′(1)=0 necessarily.

### Q32. [1 Mark] [NAT]

Events A and B are independent, with P(A)=0.4 and P(B)=0.5. Find P(A | A∪B). Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q33. [1 Mark] [MCQ]

A B+ tree supports scanning all keys in sorted order. Which property directly allows continuing from one leaf to the next without returning to the root after every leaf?

A. Leaf-level sibling links.
B. Equal key values in every internal node.
C. One separate root per leaf.
D. Absence of separators in internal nodes.

### Q34. [1 Mark] [MCQ]

To use the pumping lemma for context-free languages to prove non-context-freeness, a proof must handle which choice of decomposition w=uvxyz?

A. Only the lexicographically first decomposition.
B. Every decomposition satisfying |vxy|≤p and |vy|>0, after choosing a suitable w with |w|≥p.
C. Only decompositions with v=y=ε.
D. No decomposition, because choosing a long word is sufficient.

### Q35. [1 Mark] [NAT]

A process's page table marks page 5 as valid but not resident. The process reads page 5 with sufficient access permission. How many page faults are generated by this single memory access, assuming fault handling loads the page successfully and no other fault occurs?

**Answer format:** Integer.

### Q36. [2 Marks] [MSQ]

Languages A and B satisfy A≤mB: a total computable function f obeys x∈A iff f(x)∈B. Which implications necessarily hold?

A. If B is decidable, A is decidable.
B. If A is decidable, B is decidable.
C. If A is not recognizable, B is not recognizable.
D. If B is not recognizable, A is not recognizable.

### Q37. [2 Marks] [NAT]

Weighted activities have half-open intervals and values: A=[0,2), value 4; B=[2,4), value 4; C=[0,4), value 8; D=[4,5), value 1. How many distinct compatible subsets achieve the maximum total value? The empty subset is permitted but need not be optimal.

**Answer format:** Integer.

### Q38. [2 Marks] [MCQ]

A recovery system uses immediate updates with write-ahead logging, undo of uncommitted transactions and redo of committed transactions. Since the last checkpoint, the log records T1 changing X from 5 to 8, T2 changing Y from 4 to 9, and T1 committing. A crash occurs before T2 commits. Disk may contain either old or new values of each item. After recovery, what must (X,Y) be?

A. (5,4)
B. (8,9)
C. (8,4)
D. (5,9)

### Q39. [2 Marks] [NAT]

A prime-implicant chart has six required columns 1–6 and four available implicants. Their coverage is P:{1,2,3}, Q:{3,4}, R:{4,5,6}, S:{1,5,6}. All implicants have equal cost. How many distinct minimum-cardinality covers of all columns exist?

**Answer format:** Integer.

### Q40. [2 Marks] [MSQ]

Variables x and y are unsigned w-bit integers, w≥2, and all arithmetic is modulo 2^w. Which transformations preserve values for all x,y?

A. Replace x+x by 2*x.
B. Replace (x+y)−y by x.
C. Replace x/2 by x>>1, where division truncates and >> is logical.
D. Replace x/2 by x*2.

### Q41. [2 Marks] [NAT]

A precedence graph for a transaction schedule has exactly three vertices T1,T2,T3 and the single edge T1→T3. How many serial orders are conflict-equivalent to the schedule?

**Answer format:** Integer.

### Q42. [2 Marks] [MCQ]

For positive integer n, an algorithm splits into subproblems of sizes floor(n/3) and n−floor(n/3), then does Θ(n) additional work, with constant-time base cases for n≤2. What is its asymptotic running time?

A. Θ(log n)
B. Θ(n)
C. Θ(n log n)
D. Θ(n²)

### Q43. [2 Marks] [MCQ]

A compiler analyzes `if (p) x=2; else x=3; y=x-x;`, with exact integer arithmetic and no aliases. Which statement distinguishes simple constant propagation from an algebraic simplification?

A. At the merge x is a single known constant 2.
B. A nonrelational constant-only analysis that evaluates operations only on constant operands may leave y unknown, while the identity x−x=0 proves y is zero.
C. y can equal 1 because x has two possible values.
D. Algebraic simplification is invalid because p is unknown.

### Q44. [2 Marks] [NAT]

A systematic CRC encoder uses generator polynomial x³+x+1, represented by 1011. For data bits 1101, append three zeros and divide by 1011 over GF(2). Interpret the three-bit remainder as an unsigned integer. What is that integer?

**Answer format:** Integer.

### Q45. [2 Marks] [NAT]

An ideal shared-medium collision-detection protocol has a maximum one-way propagation delay of 2 microseconds between stations and a data rate of 100 million bits per second. Ignore all repeater, processing and framing overhead. What is the minimum number of transmitted bits required for the sender still to be transmitting when a worst-case collision signal returns? Equality at the boundary is allowed.

**Answer format:** Integer bits.

### Q46. [2 Marks] [MCQ]

A binary tree has distinct labels. Its preorder is A,B,D,E,C,F and its inorder is D,B,E,A,C,F. Which postorder is correct?

A. D,E,B,F,C,A
B. D,B,E,F,C,A
C. E,D,B,C,F,A
D. D,E,F,B,C,A

### Q47. [2 Marks] [NAT]

A byte-addressed machine has 16 address lines. A 4 KiB memory chip uses A0–A11 internally and is selected whenever A15=1 and A14=0; A12 and A13 are ignored by its select circuit. How many distinct machine addresses refer to the chip location with internal offset 0x123?

**Answer format:** Integer.

### Q48. [2 Marks] [MSQ]

DFAs D1,D2 over the same alphabet have n and m states. Their complete product automaton tracks ordered state pairs. Which accepting-pair choices recognize the specified language?

A. Both component states accepting: L(D1)∩L(D2).
B. Exactly one component state accepting: the symmetric difference of the languages.
C. At least one component state accepting: the concatenation L(D1)L(D2).
D. First component accepting and second not accepting: L(D1)−L(D2).

### Q49. [2 Marks] [MCQ]

An ordinary file has two hard links and is open through one file descriptor. Both directory entries are unlinked, but the descriptor remains open. Under a file system that preserves unlinked files while open, which event permits reclaiming the file's storage, assuming no new references arise?

A. Removing only the first hard link.
B. Closing the final open descriptor after both links have been removed.
C. Reading the first byte through the descriptor.
D. Merely changing the current directory.

### Q50. [2 Marks] [NAT]

In the subset lattice of {a,b,c}, let X={a,b} and Y={b,c}. How many subsets Z satisfy X∩Y⊆Z⊆X∪Y and are incomparable with both X and Y under inclusion?

**Answer format:** Integer.

### Q51. [2 Marks] [MSQ]

A process successfully executes a new program image through an exec-like operation with the following specified semantics: its PID is retained, its old address space is replaced, and descriptors marked close-on-exec are closed while others remain open. Which observations are possible immediately afterwards?

A. The PID is unchanged although the executed code is different.
B. An unmarked file descriptor remains usable by the new program.
C. Every pointer into the old heap is guaranteed to remain valid with its old object.
D. Every inherited descriptor must have been closed.

### Q52. [2 Marks] [NAT]

Routers A,B,C form a triangle with all three link costs 1. A also has a cost-1 link to destination D. Initially their distances to D are (1,2,2). The A–D link fails. They then run synchronous distance-vector rounds without split horizon or poison reverse. In each round every router computes its new distance using neighbours' distances from the preceding round; A cannot use its failed direct link. The first round uses the stated initial distances. What is the sum of A,B,C's distances after the second round?

**Answer format:** Integer.

### Q53. [2 Marks] [NAT]

How many insertion orders of the distinct keys 1–7 produce an ordinary unbalanced BST whose root is 4, whose left subtree has root 2 and leaves 1,3, and whose right subtree has root 6 and leaves 5,7? There is no rebalancing.

**Answer format:** Integer.

### Q54. [2 Marks] [MSQ]

For grammar S→aSb | T and T→cT | ε, which statements are true?

A. Every generated word has equally many a and b symbols.
B. Every generated word has all c symbols between its a and b blocks.
C. The grammar generates abcc.
D. The grammar generates aacbb.

### Q55. [2 Marks] [MCQ]

A 4-to-1 multiplexer has select bits s1,s0 and data inputs D0=0,D1=x,D2=x′,D3=1. For which select settings is its output independent of x?

A. Only 00.
B. Only 11.
C. 00 and 11.
D. 01 and 10.

### Q56. [2 Marks] [NAT]

A directed graph has edges a→b,b→a,b→c,c→d,d→c,d→e and isolated vertex f. How many strongly connected components have no outgoing edge to a different component?

**Answer format:** Integer.

### Q57. [2 Marks] [MCQ]

A process has four user-level threads mapped to one kernel-scheduled thread. The mapping does not replace blocking system calls with asynchronous operations. One user thread makes a blocking read that blocks the kernel thread. Which consequence follows while that kernel thread remains blocked?

A. The other user threads in the process automatically run on three other cores.
B. None of its user threads can run through that blocked sole kernel thread.
C. The process obtains four new kernel threads automatically.
D. User-level scheduling can execute instructions without any runnable kernel thread.

### Q58. [2 Marks] [NAT]

An L1 cache lookup takes 1 ns and misses on 10% of accesses. An L1 miss incurs an additional L2 lookup of 5 ns. Of accesses that reach L2, 20% miss and incur another 50 ns to memory. No delays overlap. What is the average access time in ns?

**Answer format:** Exact finite decimal.

### Q59. [2 Marks] [NAT]

Matrix A has rows (0,1,1),(2,1,0),(4,3,2). Swap its first two rows to obtain PA, then compute PA=LU with unit diagonal L and no further row swaps. What is L₃₂?

**Answer format:** Integer.

### Q60. [2 Marks] [NAT]

Six employees participate in a directed Mentors relationship. Self-mentoring is forbidden. Each employee may mentor at most two others and must be mentored by at least one other employee. A pair (u,v) means u mentors v. What is the maximum possible number of distinct pairs?

**Answer format:** Integer.

### Q61. [2 Marks] [NAT]

Evaluate ∫ from −1 to 2 of |x²−x| dx. Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q62. [2 Marks] [NAT]

Population A has mean 2 and population variance 1. Population B has mean 8 and population variance 9, and contains three times as many observations as A. What is the population variance after combining all observations? Use divisor N for each population variance, not N−1.

**Answer format:** Exact finite decimal.

### Q63. [2 Marks] [MSQ]

Consider this loop with scalar variables and no aliases:

```text
L: if p goto B else E
B: x = x + y
   y = 0
   goto L
E: return x
```

The value of p does not change in this code, but liveness analysis conservatively treats both outgoing edges of L as feasible each time. Which variables are live at entry to L at the least fixed point?

A. x
B. y
C. p
D. A separate variable z that is never used or assigned here.

### Q64. [2 Marks] [NAT]

A binary max-heap is stored from index 1 as [20,15,18,8,10,12,17]. Delete the element at index 4 by moving the final element into that position and shrinking the array. Restore heap order using swaps with parents or children as necessary. How many swaps are required after the replacement?

**Answer format:** Integer.

### Q65. [2 Marks] [NAT]

A three-bit synchronous machine interprets its state as an unsigned integer s. For s∈{0,1,2,3,4}, its next state is (s+1) mod 5. Invalid states 5,6,7 go respectively to 6,2,5 on the next clock. The initial state is chosen uniformly from all eight bit patterns. What is the expected number of clock edges until the machine first reaches a valid state, counting zero if it starts valid?

**Answer format:** Exact finite decimal.

## ANSWER KEY — MOCK TEST 012

NAT answers are exact except where rounded ranges are supplied.

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | NAT | 1 | 17 |
| 2 | NAT | 1 | 4.8 |
| 3 | MCQ | 1 | B |
| 4 | NAT | 1 | 19 |
| 5 | MCQ | 1 | C |
| 6 | MCQ | 2 | A |
| 7 | MCQ | 2 | B |
| 8 | NAT | 2 | 48 |
| 9 | NAT | 2 | 10 |
| 10 | NAT | 2 | 3 |
| 11 | MCQ | 1 | A |
| 12 | MSQ | 1 | A, C |
| 13 | NAT | 1 | 37 |
| 14 | MCQ | 1 | B |
| 15 | NAT | 1 | 1 |
| 16 | MCQ | 1 | A |
| 17 | MSQ | 1 | A, B |
| 18 | NAT | 1 | 4 |
| 19 | MCQ | 1 | A |
| 20 | NAT | 1 | 62.5 |
| 21 | MCQ | 1 | C |
| 22 | NAT | 1 | 2 |
| 23 | MCQ | 1 | B |
| 24 | NAT | 1 | 0.8333 (range 0.83325–0.83335) |
| 25 | MCQ | 1 | A |
| 26 | NAT | 1 | 5 |
| 27 | MCQ | 1 | A |
| 28 | NAT | 1 | 0 |
| 29 | NAT | 1 | 3288 |
| 30 | NAT | 1 | 3 |
| 31 | MSQ | 1 | A, C |
| 32 | NAT | 1 | 0.5714 (range 0.57135–0.57145) |
| 33 | MCQ | 1 | A |
| 34 | MCQ | 1 | B |
| 35 | NAT | 1 | 1 |
| 36 | MSQ | 2 | A, C |
| 37 | NAT | 2 | 2 |
| 38 | MCQ | 2 | C |
| 39 | NAT | 2 | 1 |
| 40 | MSQ | 2 | A, B, C |
| 41 | NAT | 2 | 3 |
| 42 | MCQ | 2 | C |
| 43 | MCQ | 2 | B |
| 44 | NAT | 2 | 1 |
| 45 | NAT | 2 | 400 |
| 46 | MCQ | 2 | A |
| 47 | NAT | 2 | 4 |
| 48 | MSQ | 2 | A, B, D |
| 49 | MCQ | 2 | B |
| 50 | NAT | 2 | 0 |
| 51 | MSQ | 2 | A, B |
| 52 | NAT | 2 | 9 |
| 53 | NAT | 2 | 80 |
| 54 | MSQ | 2 | A, B, D |
| 55 | MCQ | 2 | C |
| 56 | NAT | 2 | 2 |
| 57 | MCQ | 2 | B |
| 58 | NAT | 2 | 2.5 |
| 59 | NAT | 2 | 1 |
| 60 | NAT | 2 | 12 |
| 61 | NAT | 2 | 1.8333 (range 1.83325–1.83335) |
| 62 | NAT | 2 | 13.75 |
| 63 | MSQ | 2 | A, B, C |
| 64 | NAT | 2 | 1 |
| 65 | NAT | 2 | 0.75 |

