# GATE CS 2027 — Full-Length Mock Test 051

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

A transport report says: “The new service is faster for passengers who board at either endpoint. Intermediate-stop passengers may wait longer because fewer vehicles stop there.” Which policy conclusion exceeds what the passage establishes?

A. Benefits can differ by boarding location.
B. Endpoint journey speed alone does not describe every passenger's experience.
C. Every intermediate-stop passenger necessarily has a longer total journey.
D. Reduced stopping frequency may increase some waiting times.

### Q2. [1 Mark] [NAT]

Five distinct books A,B,C,D,E are placed in a row. A must appear somewhere before B, and C and D must not be adjacent. How many arrangements satisfy both conditions?

**Answer format:** Integer.

### Q3. [1 Mark] [NAT]

A school has two classes. In the first,18 of30 students passed an examination. Across both classes,42 of60 students passed. What percentage of the second class passed?

**Answer format:** Exact percentage without the percent sign.

### Q4. [1 Mark] [MCQ]

A square sheet occupies 0≤x≤8, 0≤y≤8. Fold the right half onto the left along x=4, then fold the upper half onto the lower along y=4. A point hole is punched at (1,3) in the folded sheet through all layers. After unfolding, what is the greatest distance between two holes?

A. 6  
B. 2√10  
C. 8  
D. 4√5

### Q5. [1 Mark] [MCQ]

A narrative says: “The team archived the original readings before recalibrating the instrument. It then repeated the measurements. Only after this repetition did it compare the two sets of readings.” Which event necessarily happened immediately before the comparison among the three later events mentioned?

A. Archiving the original readings
B. Repeating the measurements
C. Recalibrating the instrument
D. Discarding the original readings

### Q6. [2 Marks] [NAT]

Two rectangular sheets occupy [0,4]×[0,2] and [2,6]×[1,3] in a coordinate plane. Their overlap is glued and becomes internal to the combined flat shape. What is the perimeter of their union?

**Answer format:** Integer length units.

### Q7. [2 Marks] [MCQ]

“The panel described the evidence as suggestive rather than conclusive; its recommendation was consequently provisional.” Which revision preserves both the strength of the evidence and the status of the recommendation?

A. The evidence proved the claim, so the recommendation was final.
B. The evidence offered some support, so the recommendation remained open to revision.
C. The evidence disproved the claim, so the recommendation was withdrawn.
D. The evidence was irrelevant, so the recommendation was unanimous.

### Q8. [2 Marks] [NAT]

Two positive numbers have product 64 and satisfy log₂x−log₂y=2. Find x+y.

**Answer format:** Integer.

### Q9. [2 Marks] [MCQ]

A square's side is increased by 10%. A circle's radius is increased by 10%. Which pair gives the percentage increases in their areas?

A. 10%,10%
B. 20%,20%
C. 21%,21%
D. 21%,10%

### Q10. [2 Marks] [NAT]

A 4×4 grid of unit squares is coloured like a chessboard, with adjacent squares having opposite colours. How many axis-aligned 2×2 subgrids contain exactly two squares of each colour?

**Answer format:** Integer.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

A circular singly linked list has traversal 1→2→3→4→1, and tail points to node 4. Execute tail.next=tail.next.next. Then insert a new node 5 immediately after tail and set tail to this new node. What traversal starts at the new head tail.next?

A. 1,2,3,4,5  
B. 5,2,3,4  
C. 2,3,4,5  
D. 2,3,5,4

### Q12. [1 Mark] [MCQ]

A binary CRC generator polynomial has nonzero constant term and contains the factor x+1. Which error pattern is guaranteed to be detected, irrespective of its positions within a sufficiently long codeword?

A. Every error with exactly four flipped bits.
B. Every error with an odd number of flipped bits.
C. Every error with any even number of flipped bits.
D. Every nonzero error pattern.

### Q13. [1 Mark] [MCQ]

A process opens a file descriptor, sets its close-on-exec flag, and forks. The child successfully execs a new program. The parent does not exec or close the descriptor. Which statement is correct?

A. The descriptor is closed in both processes by the child's exec.
B. It remains open in the parent but is closed in the child during exec.
C. The flag prevents fork from creating a child.
D. The descriptor must remain open in the child because it was inherited.

### Q14. [1 Mark] [MSQ]

A compiler lowers the condition (p!=0) AND ((*p)>0) using short-circuit evaluation. The pointer p may be null. Which statements are correct?

A. The dereference may be skipped when p is null.
B. Evaluating both operands before combining their Boolean values always preserves behaviour.
C. A control-flow edge can bypass the dereference after a false first test.
D. The second comparison must be evaluated before the first comparison.

### Q15. [1 Mark] [NAT]

For x≠1, f(x)=(x³−1)/(x−1). What value must be assigned to f(1) to make f continuous at1?

**Answer format:** Exact number.

### Q16. [1 Mark] [NAT]

A random variable X takes values 0,1,2 with probabilities1/4,1/2,1/4. Define Y=1 if X=1, and Y=0 otherwise. What is the covariance Cov(X,Y)?

**Answer format:** Exact integer.

### Q17. [1 Mark] [NAT]

A four-input priority encoder gives highest priority to D3, then D2, D1,D0, and outputs the two-bit index of the highest asserted input. Its validity output is one whenever any input is one. How many four-bit input patterns produce code 10 with validity one?

**Answer format:** Integer.

### Q18. [1 Mark] [MCQ]

Coins of denominations 1,3,4 are available without limit. For amount 6, which statement correctly evaluates the rule “repeatedly choose the largest coin not exceeding the remaining amount”?

A. It uses two coins and is optimal.
B. It uses three coins, whereas an optimal solution uses two.
C. It cannot make amount 6 at all.
D. Every feasible solution uses three coins.

### Q19. [1 Mark] [MCQ]

A positive-edge-triggered D flip-flop has asynchronous active-low reset. Its clock remains low while reset is asserted. What happens to Q?

A. Q resets without waiting for a rising clock edge.
B. Q can change only at the next rising edge, even under reset.
C. Q must toggle repeatedly while reset remains asserted.
D. Q becomes equal to the complement of D.

### Q20. [1 Mark] [NAT]

A binary buddy allocator manages a contiguous1024-byte region and rounds each allocation up to a power of two. Four256-byte blocks at offsets0,256,512,768 are allocated. The blocks at offsets0 and512 are then freed; the others remain allocated. With no relocation, what is the largest single allocation request, in bytes, that can now be satisfied?

**Answer format:** Integer.

### Q21. [1 Mark] [MCQ]

The following basic block uses exact mathematical integers and ordinary scalar variables, with no aliases or externally visible intermediate states. All three final variable values must be preserved. Which replacement is equivalent for every initial value of b and c?
```text
a = b + c
b = a - c
c = a - b
```

A. a = b + c  
B. a = b + c; b = c  
C. a = b + c; c = a  
D. a = b + c; b = a; c = 0

### Q22. [1 Mark] [MCQ]

For relation R(A,B,C), consider F={A→B, A→C, B→C}. Which is a minimal cover with singleton right-hand sides equivalent to F?

A. {A→B, B→C}
B. {A→C, B→C}
C. {A→B, A→C}
D. {A→BC}

### Q23. [1 Mark] [MSQ]

L is a Turing-recognizable language, and the halting problem has a computable many-one reduction to L. Which statements must hold?

A. L is undecidable.  
B. L is not Turing-recognizable.  
C. The complement of L is not Turing-recognizable.  
D. The reduction gives a total decision procedure for L.

### Q24. [1 Mark] [NAT]

In a collision-detection network, the maximum one-way propagation delay is20 microseconds. A sender must still be transmitting when a worst-case collision indication returns. At10 megabits per second, what is the minimum frame length, in bits, required by this timing condition alone?

**Answer format:** Integer.

### Q25. [1 Mark] [NAT]

An empty stack processes push(1),push(2),pop,push(3),pop,pop. What is the sum of the three popped values?

**Answer format:** Integer.

### Q26. [1 Mark] [NAT]

Starting with [1,2,3,4,5,6], perform a stable partition that puts all even values before all odd values while preserving order within each group. Only swaps of adjacent elements are permitted. What is the minimum number of swaps?

**Answer format:** Integer.

### Q27. [1 Mark] [MSQ]

Functions f:A→B and g:B→C have injective composition g∘f. Which statements necessarily follow?

A. f is injective.
B. g is injective on all of B.
C. g is injective when restricted to f(A).
D. f is surjective onto B.

### Q28. [1 Mark] [MSQ]

The following code operates on ordinary integer variables; assignment copies a value and does not create an alias.

```text
x = 4
y = x
x = 9
z = y + x
```

Which statements are correct?

A. z is13.
B. y is9 at the end.
C. The value assigned by the first line contributes to z.
D. Changing x on line3 also changes y.

### Q29. [1 Mark] [NAT]

Let A be the real matrix with rows (0,−1),(1,0), and I the 2×2 identity. What is det(I+A+A²)?

**Answer format:** Integer.

### Q30. [1 Mark] [NAT]

A scalar five-stage pipeline issues one instruction each cycle when unobstructed. A taken branch incurs two lost issue cycles; an untaken branch incurs none. An execution contains100 instructions, including20 branches, of which12 are taken. Ignore pipeline filling and draining and assume no other stalls. How many issue cycles are needed?

**Answer format:** Integer.

### Q31. [1 Mark] [NAT]

A byte-addressed machine fetches a four-byte instruction beginning at address100. Its PC-relative branch displacement is a signed count of four-byte words measured from the address immediately following the instruction. If the displacement is−3, what is the branch target byte address?

**Answer format:** Integer.

### Q32. [1 Mark] [MCQ]

A B+ tree supports scanning all keys in sorted order. Which property directly allows continuing from one leaf to the next without returning to the root after every leaf?

A. Leaf-level sibling links.
B. Equal key values in every internal node.
C. One separate root per leaf.
D. Absence of separators in internal nodes.

### Q33. [1 Mark] [NAT]

Eight-bit two's-complement fixed-point words have four fractional bits. Add raw words 0xC8 and 0x34 using eight-bit addition. What real value does the resulting word represent?

**Answer format:** Exact finite decimal, possibly negative.

### Q34. [1 Mark] [NAT]

For x>0, f(x)=ln x−x/2. At what x does f attain its global maximum?

**Answer format:** Integer.

### Q35. [1 Mark] [NAT]

A complete DFA has states0,1,2. Reading a sends0→1,1→2,2→2. Reading b leaves every state unchanged. A reset word sends all three possible starting states to the same state. What is the length of a shortest reset word?

**Answer format:** Integer.

### Q36. [2 Marks] [NAT]

Grammar E→E+E | E*E | n allows all binary parenthesizations and specifies no precedence. Each n is a numeric literal with its usual value; + and * have ordinary integer meanings. How many distinct numerical values arise from parse trees for `1+2*3+4`?

**Answer format:** Integer.

### Q37. [2 Marks] [NAT]

A box is chosen uniformly from two boxes, GG containing two gold coins and GS containing one gold and one silver coin. Consider two observation protocols. In protocol U, an inspector picks one coin uniformly and shows it. In protocol P, the inspector always shows a gold coin if the chosen box has one. Under each protocol a gold coin is shown. By how much does P(GG | shown gold, protocol U) exceed P(GG | shown gold, protocol P)?

**Answer format:** Decimal rounded to four places.

### Q38. [2 Marks] [MCQ]

An eight-bit ALU compares signed two's-complement operands A=0x80 and B=0x01 by computing A−B modulo 256. Let N be the result's sign bit, V the signed subtraction-overflow flag, and L the correct signed-less-than result. Which triple (N,V,L) is correct?

A. (1,0,1)
B. (0,0,0)
C. (1,1,0)
D. (0,1,1)

### Q39. [2 Marks] [MSQ]

A write-ahead logging system uses undo and redo records. A transaction's commit record is forced to stable storage before success is reported, but its changed data pages need not yet be on disk. Which statements hold?

A. Redo may be required after a crash for a transaction already reported committed.
B. A dirty data page may be written before its corresponding update log record is durable without violating write-ahead logging.
C. Forcing the commit record can ensure earlier records in the same sequential log are durable as well.
D. A committed transaction must be undone merely because its data page was not flushed before the crash.

### Q40. [2 Marks] [NAT]

A binary floating-point system retains three significant bits including the leading 1, has unbounded exponent range, and rounds each addition to nearest with ties to an even last retained bit. Let fl denote this rounding. For a=8, b=1, c=−8, what is fl(a+fl(b+c))−fl(fl(a+b)+c)? All three operands are represented exactly.

**Answer format:** Exact integer.

### Q41. [2 Marks] [MSQ]

Let F(x,y,z)=xy+yz+zx using Boolean AND and OR. Define its Boolean difference with respect to x as F(0,y,z) XOR F(1,y,z). Which statements are correct?

A. The difference equals y+z.
B. The difference equals y XOR z.
C. The difference is independent of x.
D. The difference equals yz.

### Q42. [2 Marks] [NAT]

A microinstruction controls three mutually exclusive groups containing 5,3 and 9 signals respectively. In each group, at most one signal may be asserted, and “none” is also needed. A fully encoded design gives each group its own minimum-width binary field. There are also four independent control signals represented by one bit each. How many control bits are required, excluding sequencing and address fields?

**Answer format:** Integer.

### Q43. [2 Marks] [MSQ]

Let L={empty set, {a}, {b}, {c}, {a,c}, {b,c}, {a,b,c}}, ordered by inclusion. Notice that {a,b} is absent. Meets and joins are taken within L. A complement of x is a y with meet(x,y)=empty set and join(x,y)={a,b,c}. An order automorphism is a bijection L->L preserving the order in both directions. Which statements are correct?

A. L is a distributive lattice.  
B. Exactly six elements of L have at least one complement.  
C. L has exactly two order automorphisms.  
D. The join of {a} and {b} is {a,b,c}.

### Q44. [2 Marks] [MSQ]

Starting with three empty page frames, process the reference string 1,2,3,1,4,2,5. Which statements are correct?

A. FIFO incurs five page faults.  
B. LRU incurs six page faults.  
C. This example proves FIFO never faults more often than LRU on any reference string.  
D. Increasing the frame count cannot increase LRU's faults for a fixed reference string starting empty.

### Q45. [2 Marks] [NAT]

For this straight-line block, return is the only observable use after the last assignment. Count named scalar variables only, not constants or temporary arithmetic results.

```text
a = input()
b = input()
c = a + b
a = c + 1
d = b + a
return d
```

What is the maximum number of simultaneously live named variables immediately after any assignment in this block?

**Answer format:** Integer.

### Q46. [2 Marks] [MSQ]

A transaction's lock sequence is lock-S(A), lock-X(B), unlock-S(A), lock-S(C), commit, unlock-X(B), unlock-S(C). Use basic two-phase locking to mean that no new lock is acquired after the first unlock. Use strictness to mean that exclusive locks are held until commit or abort. Which statements are correct?

A. The sequence violates basic two-phase locking.
B. The sequence obeys basic two-phase locking because X(B) is held until commit.
C. Its exclusive-lock release satisfies the specified strictness condition.
D. Holding X(B) until commit repairs every possible two-phase-locking violation automatically.

### Q47. [2 Marks] [MCQ]

A full binary recursion tree has n=2^k leaves at depth k, with the root at depth0. Every call at depth d allocates and initializes2^d buffer cells, retains them while processing its children sequentially in depth-first order, then frees them before returning. Leaves also allocate their stated buffers. What are the tight orders of total cell initializations and maximum simultaneously live buffer cells, respectively?


A. (Θ(n²),Θ(n))
B. (Θ(n log n),Θ(n))
C. (Θ(n²),Θ(n²))
D. (Θ(n log n),Θ(log n))

### Q48. [2 Marks] [MSQ]

An n-bit two's-complement adder adds two operands and retains n result bits. Which conditions imply signed overflow?

A. Two positive operands produce a negative result.
B. Two negative operands produce a nonnegative result.
C. A positive and a negative operand produce a negative result.
D. The carry into the sign bit differs from the carry out of the sign bit.

### Q49. [2 Marks] [MSQ]

The input sequence 1,2,3,4,5 is passed through one stack. Each input may be pushed only in this order; a pop emits the current top. Which output permutations are possible?

A. 3,2,1,5,4
B. 3,1,2,4,5
C. 2,4,3,5,1
D. 4,2,3,1,5

### Q50. [2 Marks] [MSQ]

Distinct keys are inserted into an unbalanced BST. Which statements are correct?

A. Inserting sorted ascending keys can produce height n−1 for n keys, counting edges.
B. The inorder traversal is sorted regardless of insertion order.
C. Every insertion order produces the same tree shape.
D. A sorted inorder traversal proves that search always takes logarithmic time.

### Q51. [2 Marks] [MSQ]

An undirected multigraph has vertices u,v and two distinct parallel edges between them. A cycle of length two using the two distinct edges is considered a cycle. DFS tracks the edge used to enter each vertex. Which statements are true?

A. The graph contains a cycle under the stated convention.
B. Ignoring every edge to the parent vertex is always a correct cycle-detection rule for multigraphs.
C. Ignoring only the entering edge, rather than every edge to its parent endpoint, permits detection of the other parallel edge.
D. The second edge cannot affect cycle existence because it has the same endpoints.

### Q52. [2 Marks] [MSQ]

A simple undirected graph has vertices A,B,C,D,E,F. Each edge of triangle ABC and each edge of triangle DEF has weight 1. Edges AD, BE and CF have weight 2, and edge AE has weight 3. There are no other edges. Two spanning trees are distinct when their edge sets differ. Which statements are correct?

A. The minimum spanning-tree weight is 6.  
B. There are exactly 27 minimum spanning trees.  
C. There are exactly 45 spanning trees of weight 7.  
D. Every spanning tree of weight 7 uses exactly two weight-2 edges.

### Q53. [2 Marks] [NAT]

Five distinguishable bins each hold at most two identical tokens. In how many ways can exactly five tokens be distributed among the bins?

**Answer format:** Integer.

### Q54. [2 Marks] [NAT]

An expression parser uses grammar E→E−E | num. It resolves every shift/reduce conflict on `−` by shifting. What value does it assign to `20−5−3` using exact arithmetic?

**Answer format:** Integer.

### Q55. [2 Marks] [NAT]

A binary min-heap with distinct keys has array[1,4,2,8,5,3,7], using one-based indexing. Delete the minimum by moving the last key to the root, reducing the size, then repeatedly swapping it with its smaller child while needed. Then insert key0 by bubbling it upward. What key occupies array index3 after both operations?

**Answer format:** Integer.

### Q56. [2 Marks] [MSQ]

An inode contains four direct pointers, one single-indirect pointer and one double-indirect pointer. A block is 1024 bytes and each pointer is 4 bytes. Indirect blocks contain only pointers. A nonsparse file contains exactly 263 completely full data blocks, numbered logically from 0. Allocate only the indirect blocks needed for these data blocks. The inode is already in memory. Which statements are correct?

A. Exactly three indirect blocks are allocated.  
B. With no other blocks cached, reading the data in logical block 260 requires three block reads, including the data block.  
C. Logical block 259 is reached through the double-indirect pointer.  
D. The file contains 269312 bytes of data.

### Q57. [2 Marks] [NAT]

Evaluate the integral from0 to2 of |x²−1| with respect to x.

**Answer format:** Exact number.

### Q58. [2 Marks] [MCQ]

After a successful fork, both processes execute `counter++`, where counter was an ordinary private global integer equal to 5 before fork. There is no shared-memory mapping. After both increments, what are their counter values?

A. Each process has value 6 in its own address space.
B. Both necessarily observe a shared value 7.
C. The child must have value 1.
D. The parent must retain value 5.

### Q59. [2 Marks] [NAT]

Starting from an empty queue, execute enqueue 1, enqueue 2, dequeue, enqueue 3, enqueue 4, dequeue, enqueue 5. Transfer the remaining queue elements to an initially empty stack by repeatedly dequeuing and pushing. Then pop the entire stack and interpret the emitted digits as a decimal integer. What integer is obtained?

**Answer format:** Integer.

### Q60. [2 Marks] [NAT]

An IPv4 datagram has a20-byte header and1800 bytes of payload. It traverses a link with MTU620 bytes, then one with MTU420 bytes. All fragments use20-byte headers; fragments are not reassembled between links. Each router makes each nonfinal fragment as large as permitted by eight-byte alignment. How many fragments reach the destination?

**Answer format:** Integer.

### Q61. [2 Marks] [MSQ]

A lexer uses longest match among tokens '<','<=','<<','=' and identifiers. Which statements about input x<<=y are correct?

A. After identifier x, the next token is'<<'.
B. The next token after'<<' is'='.
C. The lexer must invent a'<<=' token because three symbols are adjacent.
D. Choosing'<' first would violate longest match among the stated tokens.

### Q62. [2 Marks] [NAT]

A network advertises exactly the address range10.8.0.0 through10.8.5.255, inclusive, using nonoverlapping CIDR prefixes and no addresses outside this range. What is the minimum number of prefixes required?

**Answer format:** Exact integer.

### Q63. [2 Marks] [MSQ]

An ER model has entity Building with key building_id and weak entity Room with partial key room_no. Each Room belongs to exactly one Building; room_no is unique within a building but may repeat across buildings. Which statements are correct for the relational mapping?

A. The pair(building_id,room_no) can identify Room rows.
B. room_no alone is necessarily a candidate key of Room.
C. A non-null foreign key from Room.building_id to Building implements the required owner reference, together with the appropriate Room key.
D. Removing building_id from Room loses information needed to distinguish equally numbered rooms in different buildings.

### Q64. [2 Marks] [MSQ]

A16-bit memory interface consists of two independently enabled eight-bit banks. The low bank holds even byte addresses; the high bank holds odd byte addresses. One bus transaction accesses both bytes of one aligned two-byte word, and can enable either bank or both. Which statements are correct?

A. An aligned two-byte load can be serviced in one transaction.
B. A two-byte load starting at an odd address always fits in one aligned-word transaction.
C. A byte store can preserve the other byte by enabling only its target bank.
D. Changing endianness changes which numerical byte address is even.

### Q65. [2 Marks] [NAT]

A three-variable Boolean function is1 on every input except000 and111. Product terms may cover only1-inputs. What is the minimum number of product terms in a sum-of-products implementation?

**Answer format:** Integer.

---

## ANSWER KEY — MOCK TEST 051

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | C |
| 2 | NAT | 1 | 36 (exact) |
| 3 | NAT | 1 | 80 |
| 4 | MCQ | 1 | B |
| 5 | MCQ | 1 | B |
| 6 | NAT | 2 | 18 |
| 7 | MCQ | 2 | B |
| 8 | NAT | 2 | 20 |
| 9 | MCQ | 2 | C |
| 10 | NAT | 2 | 9 |
| 11 | MCQ | 1 | C |
| 12 | MCQ | 1 | B |
| 13 | MCQ | 1 | B |
| 14 | MSQ | 1 | A, C |
| 15 | NAT | 1 | 3 |
| 16 | NAT | 1 | 0 |
| 17 | NAT | 1 | 4 |
| 18 | MCQ | 1 | B |
| 19 | MCQ | 1 | A |
| 20 | NAT | 1 | 256 |
| 21 | MCQ | 1 | A |
| 22 | MCQ | 1 | A |
| 23 | MSQ | 1 | A, C |
| 24 | NAT | 1 | 400 |
| 25 | NAT | 1 | 6 |
| 26 | NAT | 1 | 6 |
| 27 | MSQ | 1 | A, C |
| 28 | MSQ | 1 | A, C |
| 29 | NAT | 1 | 1 |
| 30 | NAT | 1 | 124 |
| 31 | NAT | 1 | 92 |
| 32 | MCQ | 1 | A |
| 33 | NAT | 1 | -0.25 |
| 34 | NAT | 1 | 2 |
| 35 | NAT | 1 | 2 |
| 36 | NAT | 2 | 4 |
| 37 | NAT | 2 | 0.1667 (accepted range 0.16665–0.16675) |
| 38 | MCQ | 2 | D |
| 39 | MSQ | 2 | A, C |
| 40 | NAT | 2 | 1 |
| 41 | MSQ | 2 | B, C |
| 42 | NAT | 2 | 13 |
| 43 | MSQ | 2 | B, C, D |
| 44 | MSQ | 2 | A, B, D |
| 45 | NAT | 2 | 2 |
| 46 | MSQ | 2 | A, C |
| 47 | MCQ | 2 | A |
| 48 | MSQ | 2 | A, B, D |
| 49 | MSQ | 2 | A, C |
| 50 | MSQ | 2 | A, B |
| 51 | MSQ | 2 | A, C |
| 52 | MSQ | 2 | A, B, C |
| 53 | NAT | 2 | 51 |
| 54 | NAT | 2 | 18 |
| 55 | NAT | 2 | 2 |
| 56 | MSQ | 2 | A, B, D |
| 57 | NAT | 2 | 2 |
| 58 | MCQ | 2 | A |
| 59 | NAT | 2 | 543 |
| 60 | NAT | 2 | 6 |
| 61 | MSQ | 2 | A, B, D |
| 62 | NAT | 2 | 2 |
| 63 | MSQ | 2 | A, C, D |
| 64 | MSQ | 2 | A, C |
| 65 | NAT | 2 | 3 |
