# GATE CS 2027 — Full-Length Mock Test 047

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

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An engineer tests a device at every integer temperature from 0°C through 100°C. It operates correctly in all tests. No rule governing its behaviour between tested temperatures is known. Which statements are justified solely by these observations?

**Candidates**

**I.** The device operates correctly at 37°C under the tested conditions.

**II.** The device must operate correctly at 37.5°C.

**III.** The observations are compatible with a device that fails at 37.5°C.

**IV.** The device must operate correctly at every integer temperature above 100°C.

A. I and II  
B. I and III  
C. I and IV  
D. II and III

### Q2. [1 Mark] [NAT]

A2×2×2 array of unit cubes has all eight cubes present. Two cubes sharing one full face are removed. What is the total exposed surface area of the remaining solid, including newly exposed faces?

**Answer format:** Integer square units.

### Q3. [1 Mark] [NAT]

A sequence is formed by writing one copy of 1, two copies of 2, three copies of 3, and so on. What is the sum of the entries in positions 90 through 94, counting the first entry as position 1?

**Answer format:** Exact integer.

### Q4. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A circular track has two concentric lane centre-lines of radii r and r+1 metres. Two runners move at equal constant speeds toward a finish on a fixed radial line. The inner runner starts on that line and runs one complete lap. The outer runner starts ahead of that line and runs the remainder of the circuit. Both start simultaneously. By how many metres along the outer lane must its start be advanced from the finish line so that the runners finish simultaneously?

A. π  
B. 2π  
C. πr  
D. 2πr

### Q5. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Choose the words completing both blanks in standard formal English: “The number of reports that ___ missing ___ now smaller.”

A. is; are  
B. are; are  
C. are; is  
D. is; is

### Q6. [2 Marks] [NAT]

A100-kg salt solution contains10% salt by mass. Exactly20kg of water evaporates, with no salt lost. Then10kg of the remaining uniform solution is removed and replaced by10kg of pure water. What is the final salt percentage by mass?

**Answer format:** Exact percentage without the percent sign.

### Q7. [2 Marks] [MSQ]

Five distinct talks A,B,C,D,E are scheduled in positions 1 through 5. C is last. A occurs before C. Exactly one talk lies between B and D. E is neither first nor last. Which statements are true over schedules satisfying all these conditions?

A. A can be fourth.  
B. A must occur before E.  
C. E can be third.  
D. B and D must both occupy odd-numbered positions.

### Q8. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A point initially at (1,2,3) is first rotated 90 degrees about the z-axis by the rule (x,y,z)→(−y,x,z). It is then rotated 90 degrees about the x-axis by the rule (x,y,z)→(x,−z,y). What is the final point?

A. (−2,−3,1)  
B. (−3,1,−2)  
C. (2,3,1)  
D. (−2,3,−1)

### Q9. [2 Marks] [MCQ]

A library reports: “After online reservations began, the fraction of issued books returned late fell. However, the number of late returns increased because the number of issued books rose substantially. The figures do not identify what would have happened without online reservations.” Which interpretation is justified?

A. Online reservations caused every borrower to return books sooner.
B. A lower late-return fraction is incompatible with more late returns.
C. The number of timely returns must have fallen.
D. A larger borrowing volume can coexist with a lower late-return fraction and more late returns, without establishing a causal effect.

### Q10. [2 Marks] [NAT]

Five distinct files must be assigned to two labelled storage boxes. Each box must receive at least two files. Two specified files must go to different boxes. How many assignments satisfy both conditions?

**Answer format:** Integer.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

How many three-element subsets of {1,2,3,4,5,6,7} contain4 and contain no pair of consecutive integers?

**Answer format:** Integer.

### Q12. [1 Mark] [NAT]

For grammar S→AB, A→a|ε, B→b|ε, how many distinct terminal strings are generated?

**Answer format:** Integer.

### Q13. [1 Mark] [NAT]

How many permutations f of {1,2,3,4} satisfy f(f(x))=x for every x and have exactly two fixed points?

**Answer format:** Integer.

### Q14. [1 Mark] [NAT]

A recursive function is mathematically defined by f(0)=0, f(1)=1 and f(n)=f(n−1)−f(n−2) for n≥2. Find f(2027).

**Answer format:** Integer, possibly negative.

### Q15. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An open-addressed hash table has seven slots and uses h1(k)=k mod 7 and h2(k)=1+(k mod 5), probing (h1(k)+j*h2(k)) mod 7 for j=0,1,... . Keys 10,17,24 are inserted in that order into an empty table. Key 10 is then deleted and its slot marked with a tombstone. Which statements are correct?

**Candidates**

**I.** Searching for 24 must continue past the tombstone.

**II.** Replacing that tombstone with a never-used marker preserves all successful searches.

**III.** A subsequent insertion of absent key 31 may reuse the tombstone slot.

**IV.** The deletion permanently reduces the maximum number of keys the table can hold to six.

A. I and IV  
B. II and III  
C. I and III  
D. II and IV

### Q16. [1 Mark] [MSQ]

In a production S→XY, the inherited attribute X.i is defined to equal the synthesized attribute Y.v. Y.v depends only on the tokens in Y's subtree and on no attributes of X. Which statements are correct?

A. This rule violates the usual L-attributed restriction for an inherited attribute of X.
B. This dependency necessarily creates a cycle in the attribute graph.
C. A suitable evaluation order can compute Y.v before assigning X.i.
D. The grammar must be syntactically ambiguous because this attribute rule exists.

### Q17. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For n≥2, consider the following pseudocode, with constant-time integer operations:

```text
j=1;
for i=1 to n:
    while j<=i:
        j=2*j;
```

What is the tight asymptotic running time?

A. Theta(log n)  
B. Theta(n log n)  
C. Theta(n)  
D. Theta(n²)

### Q18. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A page has been modified in memory since it was loaded from disk. Which statements about replacement are correct in an ordinary write-back paging system?

**Candidates**

**I.** Its dirty status may require writing its current contents to backing storage before its frame is reused.

**II.** A clean page with an unchanged backing copy may be discarded without such a write.

**III.** Every page fault proves the evicted page was dirty.

**IV.** Dirty status alone determines which page every replacement policy must choose.

A. III and IV  
B. I and II  
C. I and III  
D. I and IV

### Q19. [1 Mark] [NAT]

An in-place transpose of a row-major 3×4 array permutes old linear index i into new linear index (i mod4)×3+floor(i/4), for 0≤i<12. Starting at index1 and repeatedly applying this permutation, how many distinct indices occur before returning to1?

**Answer format:** Exact integer.

### Q20. [1 Mark] [MCQ]

A learning Ethernet switch's forwarding table is initially empty. Host A on port 1 sends a unicast frame to host B, which is on port 2. The switch has three ports and no filtering restrictions. What does the switch do with this first frame?

A. Learn B on port 1 and forward only to port 2.
B. Learn A on port 1 and flood through ports 2 and 3.
C. Learn A on port 2 and drop the frame.
D. Learn both A and B from the frame and forward only to port 2.

### Q21. [1 Mark] [NAT]

A 32-bit-wide memory module is constructed from chips each organized as 1024 words × 8 bits. How many chips are needed to obtain 1024 words × 32 bits, with all chips sharing address inputs?

**Answer format:** Integer.

### Q22. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Procedure outer contains local variable x and returns an inner function that later reads x. The language permits that returned function to be called after outer returns. Which statements hold for a correct implementation?

**Candidates**

**I.** The lifetime of captured x must extend beyond outer's return when the returned function still needs it.

**II.** A pointer into an already reclaimed stack frame always suffices to implement the returned function.

**III.** An environment stored outside the reclaimed stack frame can preserve x.

**IV.** The inner function must read a new unrelated variable named x from its caller's frame.

A. II and IV  
B. III and IV  
C. I and II  
D. I and III

### Q23. [1 Mark] [MCQ]

On domain {0,1}, let R(x,y) mean x=y. Which pair gives the truth values of ∀x∃y R(x,y) and ∃y∀x R(x,y), in that order?

A. False, false
B. True, false
C. False, true
D. True, true

### Q24. [1 Mark] [NAT]

An 8-bit signed two's-complement fixed-point format has four fractional bits. Two encoded operands represent 1.5 and −0.75. Their full-precision product is rounded back to this format, with no overflow. Interpreting the final 8-bit encoding as an unsigned integer, what is its value?

**Answer format:** Exact integer.

### Q25. [1 Mark] [MSQ]

A nondeterministic PDA begins with one bottom symbol Z on its stack. It has exactly these moves: on input a with top Z, replace Z by XZ; on input b with top X, pop X; on empty input with top Z, pop Z. There are no moves with an empty stack. Acceptance requires the entire input to be consumed and the stack to be empty. Which strings are accepted?

A. epsilon
B. ab
C. aabb
D. abab

### Q26. [1 Mark] [MSQ]

A complete DFA over {a,b} starts at p and accepts only in r or s. Its transition table is:

| State | a | b |
|---|---|---|
| p | q | r |
| q | p | s |
| r | r | r |
| s | s | s |

Which statements are correct?

A. All four states are reachable.
B. p and q are distinguishable by some suffix.
C. r and s are equivalent.
D. The language is exactly the set of strings containing at least one b.

### Q27. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A system's measured cache hit rate rises after an optimization, but its clock period also increases. Which conclusion is justified without further data?

A. Total execution time necessarily decreases.  
B. Hit rate alone is insufficient to establish an execution-time improvement.  
C. The instruction count must become zero.  
D. A higher hit rate necessarily implies a shorter clock period.

### Q28. [1 Mark] [NAT]

A TCP sender transmits a SYN with sequence number 400, then 300 data bytes, then a FIN. There are no retransmissions or other data. What acknowledgment number acknowledges everything through the FIN? SYN and FIN each occupy one sequence number.

**Answer format:** Integer.

### Q29. [1 Mark] [NAT]

A real3×3 matrix has rank2. A consistent linear system Ax=b therefore has a solution set that is an affine space of what dimension?

**Answer format:** Integer.

### Q30. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

R(A,B,C) has functional dependencies A→B and B→C, and no others except their consequences. Decompose it into R1(A,B) and R2(B,C). Which statements are correct?

A. The decomposition is lossless.  
B. The decomposition preserves the given dependencies.  
C. The original R is in BCNF.  
D. Both component schemas are in BCNF.

### Q31. [1 Mark] [NAT]

A cache stores64 data bytes in four-byte blocks and is four-way set associative. How many sets does it contain?

**Answer format:** Integer.

### Q32. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A sequential detector emits a pulse when the latest three input bits are 101, allowing overlapping matches. It reads 10101 from left to right, starting with no previous bits. How many pulses are emitted?

A. 1  
B. 2  
C. 3  
D. 5

### Q33. [1 Mark] [NAT]

A normalized binary floating-point format has a fixed number of significant bits, enough exponent range, and spacing0.25 between successive values in[8,16). It rounds to nearest with ties to an even least significant significand bit. What is the rounded value of9.125?

**Answer format:** Exact decimal.

### Q34. [1 Mark] [NAT]

A disk head is at cylinder 50. Pending requests are at 10,45,55,90. Shortest-seek-time-first scheduling breaks an equal-distance tie in favour of the lower cylinder. No new requests arrive. What total cylinder distance is travelled to serve all requests?

**Answer format:** Integer.

### Q35. [1 Mark] [MCQ]

For every real x, define f(x)=|x-1|+|x+1| and g(x)=f(f(x)-3). At exactly which points is g not differentiable?

A. x=-1 and x=1 only  
B. x=-2,-1,1,2  
C. x=-2 and x=2 only  
D. At no real point

### Q36. [2 Marks] [MSQ]

A singly linked list is acyclic. A pointer p identifies a non-tail node, but the predecessor of p is unavailable. A proposed deletion copies the successor's value into p and bypasses that successor. Which statements are correct?

A. The resulting value sequence matches deleting p's original value at that position.
B. The operation preserves the identity of every node that ordinary deletion of p would preserve.
C. It requires p to have a successor under the stated implementation.
D. External references to node identities can make this different from actually deleting node p.

### Q37. [2 Marks] [NAT]

A positive binary floating-point format has two exponent bits and two stored fraction bits. Exponent fields 01 and 10 represent normalized values (1.f)×2^(E−1), where E is the unsigned exponent-field value. Field 00 represents subnormals (0.f)×2⁰; field 11 is reserved. What is the ratio of the largest finite positive value to the smallest positive value?

**Answer format:** Integer.

### Q38. [2 Marks] [MSQ]

An interrupt handler increments a counter for every delivered interrupt. A device sets one pending bit whenever an event occurs; further events while that bit is1 do not accumulate. The handler clears the bit once on entry. Which statements are correct?

A. The counter necessarily equals the number of device events.
B. Two events arriving before the handler clears the bit may cause only one counter increment.
C. Replacing the pending bit with an adequately sized event counter can preserve event multiplicity if updates and reads are synchronized correctly.
D. Faster handler execution alone logically guarantees exact event counts for every possible event timing.

### Q39. [2 Marks] [NAT]

An IPv4 receiver obtains three fragments of one original datagram. Their (fragment offset,payload length,MF) triples are(0,400,1),(75,200,1),(100,120,0). Offsets are in standard IPv4 units; all payload lengths are in bytes. No other fragments have arrived. How many original payload bytes are still missing?

**Answer format:** Exact integer.

### Q40. [2 Marks] [NAT]

A paged process uses virtual addresses of16 bits with1024-byte pages. A valid page-table entry maps virtual page5 to physical frame12. What physical byte address corresponds to virtual byte address5500?

**Answer format:** Integer.

### Q41. [2 Marks] [MCQ]

A proof for L={aⁿbⁿcⁿ:n≥0} chooses aᵖbᵖcᵖ in the context-free pumping lemma. Why does |vxy|≤p help show every valid decomposition fails for some pumping exponent?

A. It forces v and y both to be empty.
B. It prevents the pumpable region from spanning all three blocks, so pumping changes some counts without changing all three equally, or disrupts the block order.
C. It forces the entire word to have length at most p.
D. It proves the language finite.

### Q42. [2 Marks] [MSQ]

A B+ tree index has all data entries in leaves, and linked leaves support ordered scans. Which statements are correct?

A. Searching once for the lower range bound can be followed by leaf-link traversal for the rest of the range.
B. Every subsequent leaf necessarily requires a fresh root-to-leaf search.
C. Internal separator keys can duplicate key values present in leaves.
D. Leaf links by themselves eliminate the need to locate the first relevant leaf.

### Q43. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A router must advertise exactly all IPv4 addresses from 10.4.1.0 through 10.4.6.255, inclusive, using ordinary CIDR prefixes. No address outside this interval may be covered, and no exception routes are allowed. What is the smallest number of prefixes required?

A. 2  
B. 3  
C. 4  
D. 6

### Q44. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A DMA device is programmed with a physical frame address, and it does not consult the process's page table on subsequent writes. An operating system is considering evicting and reusing that frame before DMA completion. Which statements are correct?

**Candidates**

**I.** Pinning the frame until completion can prevent reuse during the transfer.

**II.** Keeping the process's virtual address unchanged alone guarantees that reuse is safe.

**III.** Reusing the frame can direct later DMA writes into another allocation.

**IV.** The DMA device automatically follows any new page-table mapping under the stated model.

A. III and IV  
B. I and III  
C. I and II  
D. I and IV

### Q45. [2 Marks] [MSQ]

For a Turing machine started on a blank tape, consider the property that it eventually enters a designated state PRINT. Which statements are true for arbitrary encoded machines?

A. The set of machines having the property is recognizable.
B. Simulating a machine for a sufficiently large fixed number of steps decides the property for every machine.
C. The property is undecidable, since a machine can simulate an arbitrary machine/input pair and enter PRINT exactly when that simulation halts.
D. The complement is also recognizable.

### Q46. [2 Marks] [MCQ]

A compiler translates `if (p && q) x=1; else x=2;` with short-circuit evaluation. Evaluating p or q may have side effects, and each Boolean expression's result is determined at its evaluation. Which transformation preserves the evaluations and assignments for all executions?

A. Evaluate q first, then p, and test their conjunction.
B. Evaluate both p and q unconditionally, then test their conjunction.
C. Evaluate p; if false assign 2, otherwise evaluate q and assign 1 if q is true and 2 otherwise.
D. Evaluate p twice and q only if the second evaluation is true.

### Q47. [2 Marks] [NAT]

A translator has one public IPv4 address and six available public source ports. It distinguishes mappings using the public source port together with the remote IP-and-port endpoint. It permits reuse of a public port for different remote endpoints, but not for the same remote endpoint. Connections target exactly two distinct remote endpoints. What is the maximum number of simultaneous mappings under this model?

**Answer format:** Integer.

### Q48. [2 Marks] [NAT]

A syntax-directed definition evaluates a binary numeral by left-recursive production B→B₁ digit, with B.val=2×B₁.val+digit.val. A leaf digit has its numeric value. To support a binary point, production N→B . F uses N.val=B.val+F.val, and F→digit F₁ uses F.val=(digit.val+F₁.val)/2, with F→ε assigned 0. What value is assigned to `101.011`? Enter the exact decimal value.

**Answer format:** Exact finite decimal.

### Q49. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A fractional knapsack permits dividing items; all weights and values are positive. Which statements are correct?

**Candidates**

**I.** Sorting by decreasing value/weight yields an optimal packing.

**II.** Sorting by decreasing absolute value always yields an optimal packing.

**III.** With distinct ratios, an optimum produced by the ratio rule has at most one partially selected item.

**IV.** The same ratio rule is guaranteed optimal when items become indivisible.

A. I and IV  
B. II and III  
C. I and III  
D. II and IV

### Q50. [2 Marks] [NAT]

A database initially has x=100. Transaction T1 adds20 to x and commits. A later transaction T2 reads the committed value, subtracts5, and aborts. Recovery uses transaction rollback to restore T2's before-image; T1 is not undone. What is the recovered value of x?

**Answer format:** Exact integer.

### Q51. [2 Marks] [MCQ]

Under basic timestamp ordering, x initially has read timestamp 0 and write timestamp 0. T10 with timestamp 10 successfully reads x. T5 with timestamp 5 then attempts to write x. Which action is required? Thomas's write rule, if considered, may ignore an obsolete write only when it does not violate the read-timestamp test.

A. Accept the write because x has never been written.  
B. Ignore the write under Thomas's rule without aborting T5.  
C. Reject the write and abort T5 because its timestamp is below x's read timestamp.  
D. Decrease x's read timestamp to 5 and accept.

### Q52. [2 Marks] [NAT]

Three objects are sampled uniformly without replacement from five objects, two of which are red. Let X be the number of red objects selected. Find Var(X).

**Answer format:** Exact finite decimal.

### Q53. [2 Marks] [MSQ]

Let f:{a,b,c}→{0,1} satisfy f(a)=f(b)=0 and f(c)=1. Which statements are correct?

A. Exactly two functions g:{0,1}→{a,b,c} satisfy f composed with g equal to the identity on{0,1}.
B. Some function g satisfies g composed with f equal to the identity on{a,b,c}.
C. Every g satisfying the identity in A is injective.
D. f is injective.

### Q54. [2 Marks] [NAT]

A five-stage in-order pipeline has stages IF,ID,EX,MEM,WB, one cycle each. ALU results can be forwarded from EX/MEM or MEM/WB to EX, but load data becomes available only after MEM. A dependent instruction immediately following a load must stall one cycle. No other stalls occur. For the sequence below, how many total cycles elapse from the first IF through the last WB, starting empty?

```text
load r1, [r0]
add  r2, r1, r3
sub  r4, r2, r5
load r6, [r4]
add  r7, r6, r2
```

**Answer format:** Integer.

### Q55. [2 Marks] [MSQ]

DFAs D1,D2 over the same alphabet have n and m states. Their complete product automaton tracks ordered state pairs. Which accepting-pair choices recognize the specified language?

A. Both component states accepting: L(D1)∩L(D2).
B. Exactly one component state accepting: the symmetric difference of the languages.
C. At least one component state accepting: the concatenation L(D1)L(D2).
D. First component accepting and second not accepting: L(D1)−L(D2).

### Q56. [2 Marks] [NAT]

A real2×2 matrix A has eigenvalues2 and3. What is det(A²−5A+7I)?

**Answer format:** Exact number.

### Q57. [2 Marks] [NAT]

A robot must advance exactly eight units. Each move advances either one or two units, and two two-unit moves may not be consecutive. Different ordered move sequences are counted separately. How many valid sequences exist?

**Answer format:** Integer.

### Q58. [2 Marks] [NAT]

An initially empty sparse file has an inode with four direct block pointers and one single-indirect pointer. Blocks are1024 bytes and pointers are4 bytes. A write of one byte at file offset6144 allocates only the necessary data block and any necessary indirect block. Unwritten holes need no data blocks. Exclude the already existing inode. How many bytes of newly allocated blocks are needed?

**Answer format:** Integer.

### Q59. [2 Marks] [NAT]

A queue is implemented by input stack I and output stack O. Enqueue pushes onto I. Dequeue transfers every element of I to O only when O is empty, then pops O. Initially both stacks are empty. Perform: enqueue 1–6; dequeue twice; enqueue 7–9; dequeue four times; enqueue 10; dequeue twice. Each individual stack push or pop costs one unit; no other operations are counted. What is the total cost?

**Answer format:** Integer.

### Q60. [2 Marks] [NAT]

Packets A, B and C are sent back-to-back in that order through two links and a store-and-forward router. Their transmission times on link 1 are respectively 3, 1 and 2 ms; on link 2 they are respectively 1, 4 and 2 ms. Each link has a propagation delay of 2 ms. The router forwards complete packets in arrival order as soon as link 2 is free. Links operate concurrently; processing time is zero. How many milliseconds after the first bit of A leaves the source does the last bit of C reach the destination?

**Answer format:** Integer milliseconds.

### Q61. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For powers of two n≥4, a recurrence is T(n)=3T(n/2)+n²/log₂n, with positive constant base costs for n≤2. What is its asymptotic order?

A. Θ(n²)  
B. Θ(n²/log n)  
C. Θ(n^(log₂3) log n)  
D. Θ(n² log log n)

### Q62. [2 Marks] [NAT]

An open box is made by removing equal squares of side x from the corners of a 12×12 square sheet and folding the sides. For 0<x<6, what is the maximum box volume?

**Answer format:** Integer cubic units.

### Q63. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A rooted ordered full binary tree has exactly four leaves. Every internal node has a left and a right child, and the root has depth 0. Which lists can be the depths of its leaves in left-to-right order?

**Candidates**

**I.** (1,2,3,3)

**II.** (2,1,3,3)

**III.** (2,2,2,2)

**IV.** (3,3,1,2)

A. II and IV  
B. III and IV  
C. I and II  
D. I and III

### Q64. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

The following code uses unbounded integers. The input y is arbitrary.

```text
if y > 0:
    x = 2
else:
    x = 2
if x == 2:
    z = 7
else:
    z = y
```

Which statements are correct about the values and constant-propagation opportunities?

**Candidates**

**I.** z is always7.

**II.** y must equal2 after the first conditional.

**III.** A flow-sensitive constant-propagation analysis can establish x=2 at the join and remove the unreachable second else branch.

**IV.** The two different predecessor blocks force x to be nonconstant at their join even when both assign2.

A. II and III  
B. II and IV  
C. III and IV  
D. I and III

### Q65. [2 Marks] [MSQ]

A schedule is `r1(x), w1(x), r2(x), c1, c2`, where T2 reads the value written by T1. Which statements are correct?

A. It is recoverable.
B. It is cascadeless.
C. T2 could require cascading rollback if T1 aborted before its displayed commit instead.
D. T2 commits before T1 in the displayed schedule.

---

## ANSWER KEY — MOCK TEST 047

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | B |
| 2 | NAT | 1 | 22 |
| 3 | NAT | 1 | 68 |
| 4 | MSQ | 1 | A, C, D |
| 5 | MSQ | 1 | A, B, D |
| 6 | NAT | 2 | 10.9375 |
| 7 | MSQ | 2 | A, C |
| 8 | MSQ | 2 | B, C, D |
| 9 | MCQ | 2 | D |
| 10 | NAT | 2 | 12 |
| 11 | NAT | 1 | 4 |
| 12 | NAT | 1 | 4 |
| 13 | NAT | 1 | 6 |
| 14 | NAT | 1 | -1 |
| 15 | MCQ | 1 | C |
| 16 | MSQ | 1 | A, C |
| 17 | MSQ | 1 | A, B, D |
| 18 | MCQ | 1 | B |
| 19 | NAT | 1 | 5 |
| 20 | MCQ | 1 | B |
| 21 | NAT | 1 | 4 |
| 22 | MCQ | 1 | D |
| 23 | MCQ | 1 | B |
| 24 | NAT | 1 | 238 |
| 25 | MSQ | 1 | A, B, D |
| 26 | MSQ | 1 | A, C, D |
| 27 | MSQ | 1 | A, C, D |
| 28 | NAT | 1 | 702 |
| 29 | NAT | 1 | 1 |
| 30 | MCQ | 1 | C |
| 31 | NAT | 1 | 4 |
| 32 | MSQ | 1 | A, C, D |
| 33 | NAT | 1 | 9 |
| 34 | NAT | 1 | 130 |
| 35 | MCQ | 1 | C |
| 36 | MSQ | 2 | A, C, D |
| 37 | NAT | 2 | 14 |
| 38 | MSQ | 2 | B, C |
| 39 | NAT | 2 | 200 |
| 40 | NAT | 2 | 12668 |
| 41 | MCQ | 2 | B |
| 42 | MSQ | 2 | A, C |
| 43 | MSQ | 2 | A, B, D |
| 44 | MCQ | 2 | B |
| 45 | MSQ | 2 | A, C |
| 46 | MCQ | 2 | C |
| 47 | NAT | 2 | 12 |
| 48 | NAT | 2 | 5.375 |
| 49 | MCQ | 2 | C |
| 50 | NAT | 2 | 120 |
| 51 | MCQ | 2 | C |
| 52 | NAT | 2 | 0.36 |
| 53 | MSQ | 2 | A, C |
| 54 | NAT | 2 | 11 |
| 55 | MSQ | 2 | A, B, D |
| 56 | NAT | 2 | 1 |
| 57 | NAT | 2 | 19 (exact) |
| 58 | NAT | 2 | 2048 |
| 59 | NAT | 2 | 38 (exact) |
| 60 | NAT | 2 | 14 |
| 61 | MSQ | 2 | A, C, D |
| 62 | NAT | 2 | 128 |
| 63 | MCQ | 2 | D |
| 64 | MCQ | 2 | D |
| 65 | MSQ | 2 | A, C |
