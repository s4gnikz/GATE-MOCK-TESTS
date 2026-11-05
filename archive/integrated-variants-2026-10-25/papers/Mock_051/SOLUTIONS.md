# Worked Solutions — Mock Test 051

## Q1

**Correct answer:** C

The passage says intermediate passengers may wait longer, not that every one's total journey must increase. C overstates both universality and the total-time conclusion. A,B,D accurately reflect the location-specific and tentative nature of the findings. Distinguish waiting time from total journey time.

## Q2

**Correct answer:** 36 (exact)
**Concept:** Permutations with adjacency and order restrictions.

There are 5!=120 arrangements. Adjacent C,D can be treated as a block with two internal orders, giving 2×4!=48. Thus 72 avoid adjacency. Exchanging labels A and B pairs these arrangements without changing C,D adjacency; exactly half have A before B. Answer: 72/2=36.

**Common misconception:** Requiring A before B does not require them to be adjacent.

## Q3

**Correct answer:** 80

The second class has60−30=30 students and42−18=24 passes. Its pass percentage is100·24/30=80. The combined70% cannot be assigned to each class separately.

## Q4

**Correct answer:** B
**Concept:** Reflection under folding.

Undoing the folds gives x coordinates 1 and 7 and y coordinates 3 and 5. The four holes are (1,3),(1,5),(7,3),(7,5). Opposite corners have distance √(6²+2²)=√40=2√10. A counts only the horizontal separation; C is the side length of the original sheet; D corresponds to a different diagonal.

**Common misconception:** A fold reflects a coordinate about its crease; it does not simply translate a hole by half the sheet width.

## Q5

**Correct answer:** B

The stated order is archive, recalibrate, repeat, compare. Among those events, repeating directly precedes comparison, so B. A,C are earlier, and D never occurs in the account. The question concerns the narrated event ordering, not whether unmentioned activities occurred between them.

## Q6

**Correct answer:** 18
**Concept:** Boundary tracing of overlapping shapes.

The outer polygon can be traced through (0,0),(4,0),(4,1),(6,1),(6,3),(2,3),(2,2),(0,2). Its successive side lengths are 4,1,2,2,4,1,2,2, summing to 18. The portions hidden inside the overlap are not part of the outer boundary.

**Common misconception:** Adding the separate rectangle perimeters counts internal boundary segments.

## Q7

**Correct answer:** B

Suggestive evidence provides support without establishing certainty; a provisional recommendation can be revised. B preserves both meanings. A upgrades both to certainty and finality, C reverses the evidentiary direction, and D substitutes irrelevance and unanimity, neither stated. The qualifying words control the strength of the claim.

## Q8

**Correct answer:** 20

**Concept:** Combining logarithmic ratio and product.

The logarithm difference gives log₂(x/y)=2, so x=4y. From xy=64, 4y²=64 and positivity gives y=4,x=16. Their sum is 20.

**Common misconception:** Replacing a difference of logarithms by the logarithm of a difference.

## Q9

**Correct answer:** C
**Concept:** Quadratic scaling.

Both areas are proportional to the square of the changed linear dimension. Multiplying that dimension by 1.1 multiplies area by 1.21, a 21% increase. C is correct. A,D confuse linear and area scaling; B omits the additional 0.1² term.

**Common misconception:** Percentage changes in length and area are not equal.

## Q10

**Correct answer:** 9

**Concept:** Counting local patterns in a grid.

Every adjacent 2×2 chessboard block has two squares of each colour. Its top-left square can occupy three rows and three columns, giving 3×3=9 subgrids.

**Common misconception:** Counting only disjoint 2×2 blocks when overlapping subgrids are allowed.

## Q11

**Correct answer:** C
**Concept:** Circular-list pointer updates.

The first update bypasses node 1, making node 2 the head. Inserting 5 after old tail 4 sets 4.next=5 and 5.next=2. Updating tail to 5 leaves head=2. Thus traversal is 2,3,4,5. A retains the deleted node; B starts at the tail; D inserts 5 before rather than after node 4.

**Common misconception:** In a tail-only circular-list representation the head is defined indirectly as tail.next.

## Q12

**Correct answer:** B

**Concept:** CRC detection using a polynomial factor.

An undetected error polynomial must be divisible by the generator, hence by x+1. Over GF(2), this implies E(1)=0, meaning an even number of nonzero coefficients. Any odd-weight error has E(1)=1 and is detected. B is correct. Even-weight errors may be undetected, so A and C are not universal guarantees; a nonzero multiple of the generator refutes D.

**Common misconception:** Treating a CRC as detecting every nonzero corruption.

## Q13

**Correct answer:** B
**Concept:** Descriptor inheritance and exec flags.

The child inherits the descriptor and its close-on-exec flag. Its successful exec closes that descriptor in the child. The parent has a separate descriptor table and neither execs nor closes it, so its descriptor remains open. B is correct; A incorrectly propagates the close, C invents a fork restriction, and D ignores the flag.

**Common misconception:** Sharing an open file description does not make descriptor-table close operations global to all processes.

## Q14

**Correct answer:** A, C

If p is null, the first comparison is false and short-circuit evaluation bypasses the dereference, proving A,C. Eager evaluation in B could introduce an invalid null dereference. D reverses the required order. Correct intermediate code must preserve which expressions are evaluated, not just a truth-table identity on safe operands.

## Q15

**Correct answer:** 3

For x≠1, factoring the numerator gives f(x)=x²+x+1. Its limit at1 is3, the unique continuous extension. The original undefined quotient does not prevent a removable extension.

## Q16

**Correct answer:** 0

E[X]=1,E[Y]=1/2, and XY equals1 only when X=1, giving E[XY]=1/2. Cov(X,Y)=1/2−1×1/2=0. This does not imply independence: Y is a nonconstant deterministic function of X. Zero covariance can coexist with dependence.

## Q17

**Correct answer:** 4

Concept: priority encoding. Code 10 requires D3=0 and D2=1. D1 and D0 are arbitrary, giving 2²=4 patterns. Validity is automatically one because D2 is asserted. Lower-priority asserted inputs do not change the code.

## Q18

**Correct answer:** B

**Concept:** A counterexample to greedy coin selection.

Greedy chooses 4, then 1, then 1, using three coins. The feasible choice 3+3 uses two, and one coin cannot make six. Thus B is correct. A gives the wrong greedy count; C ignores denomination one; D ignores 3+3.

**Common misconception:** Assuming the familiar greedy rule works for every denomination system.

## Q19

**Correct answer:** A

**Concept:** Asynchronous reset priority.

Asserting an asynchronous reset changes Q independently of a clock edge, so A holds even while the clock remains low. B describes synchronous reset, C incorrectly substitutes toggling, and D is unrelated to reset behaviour.

**Common misconception:** Applying the normal data-sampling edge condition to an asynchronous control.

## Q20

**Correct answer:** 256

**Concept:** Buddy alignment and external fragmentation.

Offset0's256-byte buddy is offset256, which remains allocated. Offset512's buddy is offset768, also allocated. The two free blocks are not buddies and cannot coalesce. Thus there are512 free bytes in total, but the largest satisfiable single request is256 bytes.

**Misconception:** Equating total free space with the largest available contiguous buddy block.

## Q21

**Correct answer:** A

**Concept:** Compiler Design — Local optimization

Write initial values b0,c0. The first statement sets a=b0+c0. The second sets b=(b0+c0)-c0=b0. The third reads this restored b and sets c=(b0+c0)-b0=c0. Thus b and c end unchanged, and only a=b+c is required.

- **A:** True: a becomes the sum and b,c retain their original values.
- **B:** False: it changes b whenever b0 differs from c0.
- **C:** False: it changes c to b0+c0 rather than preserving c0.
- **D:** False: it generally changes both b and c.

**Common misconception:** Algebraic simplification must track which version of each variable an expression uses.

## Q22

**Correct answer:** A
**Concept:** Redundant dependencies in a minimal cover.

A→C follows transitively from A→B and B→C, so it can be removed. Neither remaining dependency follows from the other, and their single-attribute left sides have no extraneous attributes. A is a minimal cover. B cannot derive A→B; C cannot derive B→C; D lacks a singleton right-hand side and cannot derive B→C either.

**Common misconception:** Preserving A's closure alone does not preserve dependencies with other determinants.

## Q23

**Correct answer:** A, C
**Concept:** Reductions and recognizability of complements.

If L were decidable, compose its decider with the given reduction to decide halting, impossible; A holds. B contradicts the premise. If both L and its complement were recognizable, dovetail their recognizers to decide L, contradicting A; hence C holds. D mistakes a reduction into L for an algorithm deciding membership in L.

**Common misconception:** A recognizable target can still encode an undecidable problem.

## Q24

**Correct answer:** 400

Worst-case return delay is twice20 microseconds, or40 microseconds. At10 bits per microsecond, the timing requirement is400 bits. This calculation uses only the supplied propagation model, not an additional standard-specific minimum frame size.

## Q25

**Correct answer:** 6

Concept: stack tracing. The three pops return 2, then 3, then 1. Their sum is 6. Last-in-first-out order determines individual outputs even though their total equals the sum of all pushed values here.

## Q26

**Correct answer:** 6

**Concept:** Inversions under stable partition.

Each odd-before-even pair must cross once: 1 precedes three evens, 3 precedes two, and 5 precedes one. Thus at least six adjacent swaps are necessary. Moving each even left across preceding odds attains this bound and preserves both internal orders.

**Common misconception:** Counting displaced elements instead of pair crossings.

## Q27

**Correct answer:** A, C

If f mapped two distinct A elements together, their compositions would coincide, contradicting injectivity; A follows. Distinct points of f(A) also cannot be identified by g, proving C. g may identify points outside that image without affecting the composition, so B is not necessary. For example, embedding a smaller set in B need not be onto, disproving D.

## Q28

**Correct answer:** A, C

y receives4 before x is replaced by9, so z=4+9=13. A and C are true. Ordinary value assignment does not alias variables, making B and D false. Propagation must respect which definition reaches each use.

## Q29

**Correct answer:** 1
**Concept:** Matrix polynomial reduction.

Multiplication gives A²=−I. Hence I+A+A²=A, whose determinant is 0×0−(−1)×1=1. Reducing the polynomial before evaluating its determinant avoids unnecessary arithmetic.

**Common misconception:** Determinants do not distribute over matrix addition.

## Q30

**Correct answer:** 124

There are100 issue slots for actual instructions and12×2=24 lost slots for taken branches. Total124. Untaken branches cause no penalty under the stated model; pipeline filling and draining are explicitly excluded.

## Q31

**Correct answer:** 92

The base is104, after the four-byte instruction. The displacement is−3·4=−12 bytes. Target104−12=92. Both the reference point and displacement units matter.

## Q32

**Correct answer:** A

**Concept:** Leaf chains in B+ trees.

Sibling links allow a scan to continue directly to the next leaf, establishing A. B is not a B+ tree invariant; C describes no ordinary single-root B+ tree; D removes needed navigation separators and does not explain scanning.

**Common misconception:** Assuming every successive key retrieval must begin at the root.

## Q33

**Correct answer:** -0.25

Concept: fixed-point scaling. Raw signed integers are −56 and 52, representing −3.5 and 3.25. Their sum is −4, raw FC, scaled by 1/16 to −0.25. The raw hex result alone is not the represented real value.

## Q34

**Correct answer:** 2

**Concept:** Global maximum from derivative sign.

f′(x)=1/x−1/2 is positive below two and negative above two. Thus x=2 gives the global maximum on x>0; f tends to −∞ at both ends of the domain.

**Common misconception:** Solving f′=0 without checking whether the stationary point is a maximum.

## Q35

**Correct answer:** 2

Neither one-letter word resets: b is the identity and a maps the state set to{1,2}. Reading aa maps every state to2. Therefore the minimum length is2. Resetting concerns all starting states, not only a designated initial state.

## Q36

**Correct answer:** 4

Concept: ambiguity and semantic values. The five parenthesizations yield 13 for ((1+2)*3)+4, 11 for (1+(2*3))+4, 21 for (1+2)*(3+4), 11 for 1+((2*3)+4), and 15 for 1+(2*(3+4)). Distinct values are {11,13,15,21}, count four. Different parse trees need not produce different numerical values.

## Q37

**Correct answer:** 0.1667 (accepted range 0.16665–0.16675)

Under U, gold has likelihood1 in GG and1/2 in GS, giving posterior(1/2)/(1/2+1/4)=2/3. Under P, gold is guaranteed from either box, so the observation carries no information and the posterior remains1/2. The difference is1/6≈0.1667. Conditioning must include how an observation was selected; the visible color alone does not determine its likelihood.

## Q38

**Correct answer:** D

Concept: signed comparison after overflow. A represents −128 and B represents one. Exact difference −129 wraps to 127=0x7F, giving N=0 and V=1. Signed less-than is N XOR V=1. Thus D. A wrongly uses the unrepresentable exact difference's sign as the stored sign; B misses overflow; C gives the wrong stored sign and comparison. A subtraction's sign alone is insufficient when it overflows.

## Q39

**Correct answer:** A, C

Commit can be durable while data remains only buffered, so redo may be needed(A). Forcing a position in a sequential log can make all earlier records durable(C). WAL requires the update's log record to be durable before its data page is flushed, contradicting B. Missing flushed data for a committed transaction calls for redo, not automatic undo(D).

## Q40

**Correct answer:** 1

At magnitude 8, representable values immediately around 9 are 8 and 10. The midpoint rounds to 8 because its final significand bit is even. Thus fl(fl(8+1)−8)=0. On the other grouping, 1−8=−7 is exactly representable with three significant bits, and 8−7=1 is exact. The requested difference is 1−0=1. Rounding after intermediate operations breaks associativity.

## Q41

**Correct answer:** B, C

Concept: Boolean sensitivity. F(0,y,z)=yz; F(1,y,z)=y+z. Their XOR is one exactly when y and z differ, giving y XOR z (B). The substituted expression has no x (C). A fails at y=z=1 because the difference is zero but OR is one; D fails at y=1,z=0 because the difference is one but AND is zero. Boolean difference uses XOR, not ordinary subtraction.

## Q42

**Correct answer:** 13

**Concept:** Encoded control fields with idle choices.

The groups need 6,4 and 10 distinct encodings after including “none”. Their widths are ceil(log₂6)=3, log₂4=2 and ceil(log₂10)=4. Add the four independent bits: 3+2+4+4=13.

**Common misconception:** Omitting the “none” code or encoding independent signals as mutually exclusive.

## Q43

**Correct answer:** B, C, D

**Concept:** Engineering Mathematics — Partial orders and lattices

1. Intersections remain in L, so they are meets. All unions are in L except {a} union {b}; for that pair the least available upper bound is {a,b,c}. Hence L is a lattice, but joins need not equal unions.
2. Distributivity fails: {c} meet ({a} join {b})={c}, whereas ({c} meet {a}) join ({c} meet {b})=empty set.
3. Bottom and top complement one another. {a} has complements {b} and {b,c}; {b} has complements {a} and {a,c}; {a,c} and {b,c} are consequently complemented too. The remaining element {c} has no complement: the only nonempty elements disjoint from it are {a} and {b}, and their individual joins with {c} are below top. Thus six elements have complements.
4. Among the three atoms, {c} uniquely has two immediate upper covers; {a} and {b} each have one. Any automorphism must fix {c} and may only fix or swap {a},{b}. The two choices determine all other images, and both are valid. Thus there are exactly two automorphisms.

- **A:** The explicit distributive-law calculation yields {c} on one side and empty set on the other.
- **B:** Only {c} lacks any complement.
- **C:** An automorphism fixes {c}; its only freedom is the swap of a and b.
- **D:** Because {a,b} is absent, the only common upper bound for the two atoms is top.

**Common misconception:** An inclusion-ordered family can have joins different from set union, so it need not inherit Boolean distributivity.

## Q44

**Correct answer:** A, B, D
**Concept:** Page replacement histories and the stack property.

FIFO fills 1,2,3; hits 1; replaces 1 by 4; hits 2; replaces 2 by 5: five faults. LRU's hit on 1 makes 2 least recent; 4 evicts 2, the next 2 evicts 3, and 5 evicts 1: six faults. A,B hold. One example cannot establish C. LRU's resident sets are nested as frame capacity grows, proving D.

**Common misconception:** A replacement policy with the stack property need not beat every other policy on every individual trace.

## Q45

**Correct answer:** 2

Working backward, after d's assignment only d is live. After the reassignment of a, b and new a are live. After c's assignment, b and c are live; old a is dead because it is overwritten before another use. After b's input, a and b are live; after a's input, only a is live. The maximum is2. Counting every defined variable would retain obsolete values and overestimate liveness.

## Q46

**Correct answer:** A, C

Concept: locking conditions. Unlock-S(A) starts the shrinking phase; later lock-S(C) violates basic 2PL (A true, B false). X(B) is released after commit, meeting the specifically defined exclusive-lock retention condition (C true). Retaining X(B) does not remove the new shared-lock acquisition, so D is false. The question separates strictness of release from the full strict-2PL protocol.

## Q47

**Correct answer:** A

At depth d there are2^d calls, each initializing2^d cells, so total initializations sum4^d from d=0 to k, which is Θ(4^k)=Θ(n²). Sequential depth-first processing keeps only one root-to-leaf chain of buffers live at once; its sizes sum1+2+...+2^k=2n−1, giving Θ(n). A follows. B,D undercount total work, and C counts allocations from nonoverlapping sibling calls as simultaneously live.

## Q48

**Correct answer:** A, B, D

**Concept:** Signed overflow in two's-complement addition.

For equal-sign operands, a result with the opposite sign is outside the signed range, giving A and B. The equivalent bit-level test is XOR of carry into and out of the sign bit, giving D. Opposite-sign addition stays within the signed range, so C is false.

**Common misconception:** Using the carry-out bit alone as the signed overflow flag.

## Q49

**Correct answer:** A, C
**Concept:** Stack permutations.

A is produced by pushing 1,2,3, popping all three, then pushing 4,5 and popping both. C is produced by push 1,2/pop 2; push 3,4/pop 4,3; push 5/pop 5,1. In B, after popping 3 the top is 2, blocking 1. In D, after popping 4 the top is 3, blocking 2. Thus A,C are possible and B,D are not.

**Common misconception:** Unread input cannot remove an already stacked obstruction to the next requested output.

## Q50

**Correct answer:** A, B

Ascending insertion gives a right-child chain with n−1 edges, so A is true. The BST invariant ensures that inorder traversal returns sorted keys, proving B. For keys1,2,3, inserting2 first can give a balanced root, whereas inserting1,2,3 gives a chain; C is false. The chain has sorted inorder output but linear worst-case search, refuting D. Traversal order does not certify balance.

## Q51

**Correct answer:** A, C

Concept: edge identities in multigraph DFS. Traversing one edge u→v and returning on the other forms the allowed length-two cycle, A. At v, only the entering edge should be ignored; the other edge to the already visited parent reveals the cycle, C. B incorrectly ignores both edges; D discards a structurally distinct edge. Parent-vertex exclusion assumes a simple graph.

## Q52

**Correct answer:** A, B, C

**Concept:** Algorithms — Minimum spanning trees and constrained counting

1. A spanning tree needs five edges and must connect the two triangles. Four unit edges and one weight-2 connector give weight 6. A lighter tree cannot connect all six vertices, since every connector weighs at least 2.
2. For weight 6, choose a spanning tree in each triangle in 3 ways each, then one of AD, BE, CF in 3 ways. This gives 3×3×3=27.
3. A weight-7 tree has either four unit edges and AE, or three unit edges and two weight-2 connectors. The first case gives 3×3=9.
4. In the second case choose the two connectors in 3 ways. The three unit edges must split as two in one triangle and one in the other: taking all three from a triangle would create a cycle. There are 2 choices of which triangle gets two edges, 3 choices of its spanning tree, and 2 choices of the other triangle's single edge. That edge must attach its otherwise unconnected third vertex to a connector endpoint. Thus this case contributes 3×2×3×2=36.
5. Total weight-7 trees: 9+36=45.

- **A:** Correct: the lower bound 6 is attained.
- **B:** Correct: the three independent choices give 27 distinct edge sets.
- **C:** Correct: the two disjoint weight compositions give 45 trees.
- **D:** Incorrect: a spanning tree in each triangle together with AE has weight 7 and uses no weight-2 edge.

**Common misconception:** Equal-weight edges create multiple optima, and counting the next weight requires checking connectivity and cycles, not just the number of chosen edges.

## Q53

**Correct answer:** 51
**Concept:** Bounded compositions and generating functions.

The answer is the coefficient of x⁵ in (1+x+x²)⁵. Without upper bounds there are C(9,4)=126 solutions. For a chosen bin holding at least three tokens, remove three tokens: C(6,4)=15 remaining solutions. Subtract 5×15=75. Two bins cannot each hold three when the total is five, so no intersection correction is needed. The result is 126−75=51.

**Common misconception:** Identical tokens do not make the distinguishable bins interchangeable.

## Q54

**Correct answer:** 18
**Concept:** Conflict resolution and associativity.

After seeing 20−5 with another minus ahead, shifting postpones reduction. The parser forms the right subtree 5−3 first, yielding 20−(5−3)=18. Reducing instead would give left association and value 12.

**Common misconception:** Associativity comes from parser rules or conflict policy, not from the visual order of operators alone.

## Q55

**Correct answer:** 2

Deleting1 gives provisional[7,4,2,8,5,3]. Swapping down through2 and then3 gives[2,4,3,8,5,7]. Insert0 at index7 and swap with its parent at3, then with the root. Final array[0,4,2,8,5,7,3] has2 at index3. Reheapification uses actual parent/child positions, not global sorting.

## Q56

**Correct answer:** A, B, D

**Concept:** Operating Systems — File systems

Each indirect block holds 1024/4=256 pointers. The direct range is 0-3 and the single-indirect range is 4-259. The remaining logical blocks 260-262 require a double-indirect root and one lower-level indirect block. Together with the single-indirect block, this gives three allocated indirect blocks.

A is true by the count above. B is true: read the double-indirect root, its selected lower-level block, and the data block. C is false: 259 is the last single-indirect data block. D is true because 263*1024=269312 bytes.

- **A:** True: 1 single-indirect block + 1 double-indirect root + 1 double-indirect second-level block = 3 metadata blocks.
- **B:** True: reading block 260 uncached requires reading double-indirect root, double-indirect child, and data block (3 disk reads).
- **C:** False: block index 259 is single-indirect, not double-indirect.
- **D:** True: file size is 263 * 1024 = 269,312 bytes.

**Common misconception:** Metadata-block allocation depends on the populated part of the pointer tree, not its maximum possible capacity.

## Q57

**Correct answer:** 2

The expression inside the absolute value changes sign at1. The integral is ∫0¹(1−x²)dx+∫1²(x²−1)dx=2/3+4/3=2. Integrating x²−1 without splitting would cancel part of the area that the absolute value makes positive.

## Q58

**Correct answer:** A

**Concept:** Forked private state.

Each process starts with its own logical copy of counter=5 and increments it to six. Copy-on-write implementation details do not turn the ordinary global into shared writable state. Thus A holds; B assumes sharing, while C,D contradict the executed increment and inherited value.

**Common misconception:** Confusing initially identical contents with a shared variable.

## Q59

**Correct answer:** 543
**Concept:** Queue and stack order composition.

The two dequeues remove 1 and 2. The final queue is front-to-back 3,4,5. Pushing that order puts 5 on top, and the pops emit 5,4,3, yielding 543.

**Common misconception:** Transferring through a stack reverses the surviving queue order, not the original entire input history.

## Q60

**Correct answer:** 6

On MTU620 the maximum aligned payload is600, so the original payload becomes three600-byte fragments. On MTU420 the maximum aligned payload is400. Each existing600-byte fragment splits into400 and200 bytes; both are multiples of8, so the original-fragment more-fragments status is consistent even for a final piece of a nonfinal original fragment. Six fragments reach the destination. Recombining payload across first-hop fragment boundaries to obtain five fragments is not allowed without reassembly.

## Q61

**Correct answer:** A, B, D

At the first '<', longest match among the listed tokens is'<<', then the remaining'=' forms its own token. A,B,D are true. A lexer does not invent an unlisted token based on adjacency, so C is false.

## Q62

**Correct answer:** 2

Use10.8.0.0/22 for the first four /24 blocks and10.8.4.0/23 for the remaining two. One CIDR prefix always contains a power-of-two number of addresses; six /24 blocks have1536 addresses, which is not a power of two. Hence one is impossible and two suffice. A /21 would advertise unwanted addresses10.8.6.0 through10.8.7.255.

## Q63

**Correct answer:** A, C, D

The owner key together with the partial key distinguishes every room, proving A. Equal room numbers in different buildings disprove B and explain D. A required, non-null foreign key checks existence of the owner; combined with the composite Room key it implements this mapping, so C is true. A partial key is unique only relative to its owner.

## Q64

**Correct answer:** A, C

An aligned two-byte word uses both banks at one word address, proving A. An odd-start two-byte load crosses an aligned-word boundary, refuting B. Independent bank enables permit a one-byte store without changing its neighbour, proving C. Endianness concerns byte significance, not whether an address number is even, refuting D.

## Q65

**Correct answer:** 3

No four-cell cube avoids both000 and111: fixing any one variable still admits one of them. Thus a valid cube covers at most two of the six1-inputs, giving a lower bound of three terms. The cubes a'c, bc' and ab' cover disjoint pairs001/011,010/110,100/101, attaining three. A power-of-two group cannot cross a specified zero.

