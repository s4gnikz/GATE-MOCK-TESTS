# Worked Solutions — Mock Test 048

## Q1

**Correct answer:** C

Concept: cumulative frequencies. The median is the thirteenth ordered observation. The first two bins contain 4+6=10 observations, and the third extends the cumulative count to 20. Hence observation 13 lies in [20,30), C. A and B finish too early; D starts after observation 20. The bin containing the mean need not be identifiable from these data.

## Q2

**Correct answer:** A

A punch away from both folds unfolds to all four sign combinations of its nonzero coordinates. A is exactly such a reflection orbit. B violates reflection symmetry, while C,D contain only two of the four distinct images. Being away from folds prevents coincident mirrored centres.

## Q3

**Correct answer:** C

Both weighing and obtaining the address must precede mailing; their mutual order is unspecified. A and B satisfy this, and D accurately recognizes both possibilities. C places address acquisition after mailing, contradicting the account. Partial order information need not specify a unique chronology.

## Q4

**Correct answer:** 4
**Concept:** Unfolding reflections.

Each fold doubles the number of layers. The punch passes through four distinct sheet locations, which separate on unfolding. Being away from folds and boundaries ensures the four holes do not coincide or merge.

**Common misconception:** A hole on a fold can behave differently; the stated location rules that out.

## Q5

**Correct answer:** B

The clause beginning “only if” imposes a condition on the endorsement. Thus B is the contextual meaning. A is the occupational sense of qualified, C wrongly asserts withdrawal, and D contradicts the stated reservation. Interpret vocabulary through its surrounding claim.

## Q6

**Correct answer:** 6

After n days the first-to-second ratio is(3/2)^n/8. At n=5, (3/2)^5=243/32<8; at n=6 it is729/64>8. The ratio increases strictly, so day6 is the first crossing. Compare end-of-day values and require strict inequality.

## Q7

**Correct answer:** 16 (exact)
**Concept:** Counting orders satisfying cyclic inequalities.

All four assertions cannot be true, since they form a strict cycle; all four cannot be false for the same reason in reverse. Exactly three true assertions occur in four orders: choose which assertion is false, and the other three force a single chain. Reversing each order gives four orders with exactly one true assertion. The remaining 4!−4−4=16 have exactly two true assertions.

**Common misconception:** The four pairwise comparisons are constrained by transitivity, so their truth values are not independent coin tosses.

## Q8

**Correct answer:** 24

The four top faces contribute4. Exterior vertical boundaries contribute twice the sum of all heights because each column has two outer sides:2(3+1+2+2)=16. Internal height differences contribute |3−1|+|2−2|+|3−2|+|1−2|=4. Thus the exposed area is4+16+4=24. Hidden interfaces between equal-height columns contribute no exposed area.

## Q9

**Correct answer:** 41

**Concept:** Recurrence evaluation and summation.

The first four terms are 2,5,11,23. Their sum is 41. Alternatively a_n+1 doubles at each step, so a_n=3×2^(n−1)−1, and the four-term sum is 3(2⁴−1)−4=41.

**Common misconception:** Reporting the fourth term instead of the requested sum.

## Q10

**Correct answer:** 2.6667 (accepted range 2.66665–2.66675)

The two centres and either intersection point form an equilateral triangle. At each centre, the arc inside the other disk therefore subtends 120 degrees. Each exposed boundary arc subtends 240 degrees and has length (240/360)×2πr=4πr/3. Two such arcs give P=8πr/3, so the requested ratio is 8/3, rounding to 2.6667. The common internal arcs are not part of the union's perimeter.

## Q11

**Correct answer:** A

**Concept:** Characterizing a recursive grammar.

Each a is prepended and each b appended around the remaining S. Thus all generated words are a^n b^m, with counts independently chosen; every such word is obtainable. A is correct. B and C impose unjustified equal counts or alternation; D includes ba, which cannot be generated.

**Common misconception:** Assuming grammar ambiguity changes the generated language into all strings.

## Q12

**Correct answer:** 2 (exact)

**Concept:** Operating Systems — System calls

1. dup creates a second descriptor referring to the same open-file description, so the offset is shared.
2. The two reads move the offset to 2 and then 5.
3. The absolute seek resets it to 1. The final one-byte read moves it to 2.

**Common misconception:** Duplicated descriptors share an offset; reopening the path would create an independent offset.

## Q13

**Correct answer:** 3

Rotation makes10 the root,20 its right child, and15 the left child of20;30 remains20's right child. Searching30 visits10,20,30: three nodes. Rotation preserves inorder order but changes search depths.

## Q14

**Correct answer:** 2

Concept: BFS queue timing. Processing s enqueues a,b. Dequeue a, leaving [b]; enqueue c, giving [b,c]. Just before enqueuing d, the queue therefore has two vertices. Vertices already processed are not still queued.

## Q15

**Correct answer:** A, C

**Concept:** Input exhaustion and state/stack-dependent continuation.

A final state may be visited with unread input. Acceptance still requires consuming all the input, so C is true. If a later transition requires a particular stack top that the modification erased, a formerly accepting continuation can disappear; A is true. This counterexample disproves B's universal claim. Final states need not be terminal and may have outgoing transitions, so D is false.

**Misconception:** Confusing entering a final state with successful acceptance regardless of remaining input.

## Q16

**Correct answer:** 65534
**Concept:** End-around carry in one's-complement checksums.

The ordinary sum is 0x10000. Fold the carry into the low word to obtain 0x0001. Its 16-bit complement is 0xFFFE, decimal 65534. Discarding the carry would instead yield the wrong checksum 65535.

**Common misconception:** One's-complement addition is not ordinary addition modulo 2¹⁶.

## Q17

**Correct answer:** A, B, D
**Concept:** Liveness over alternative paths.

c is read by the test. A true branch uses the current a; a false branch uses the current b. The old x is overwritten on either branch before return reads x. Therefore a,b,c are live, while old x is not. This proves A,B,D and refutes C.

**Common misconception:** Liveness uses existence of a future use on some path, not a requirement that every path uses the value.

## Q18

**Correct answer:** A, B, D
**Concept:** Finite cancellation monoids.

Left multiplication by a is injective by cancellation and hence onto on the finite set (A). Thus some b satisfies ab=e. Now a(ba)=(ab)a=a=ae; cancel a to get ba=e. Every element has a two-sided inverse, proving B and D. Noncommutative finite groups, such as the permutations of three elements under composition, refute C.

**Common misconception:** Finiteness is crucial when converting an injective self-map into a surjective one.

## Q19

**Correct answer:** 512

**Concept:** Instruction-field bit allocation.

Each register field needs log₂32=5 bits. Three such fields and the immediate use 15+8=23 bits. The remaining nine opcode bits encode 2⁹=512 patterns.

**Common misconception:** Subtracting the number of registers instead of the field width.

## Q20

**Correct answer:** 3 (exact)

**Concept:** Databases — ER model

1. Project is identified by (dept_id, project_code), because project_code alone may repeat.
2. Task adds its own partial key, giving (dept_id, project_code, task_no).
3. Dropping any attribute can merge allowed distinct tasks, so all three are necessary.

**Common misconception:** A weak owner can itself have a composite identifying key.

## Q21

**Correct answer:** 0

Index2 has children at indices4,5 in a seven-element heap. Both must have larger keys than their parent in a distinct-key min-heap, but7 is the largest available key. The stipulated position is impossible, so there are zero such heaps. A heap's largest key must be at a leaf, though a particular leaf is not prescribed.

## Q22

**Correct answer:** B
**Concept:** Allocated storage and sizeof.

Allocated storage persists until freed even if its pointer variable leaves scope (B), though losing every pointer can make it unreachable. malloc does not initialize it to zero (A). sizeof *p determines the int type's size without reading its value here (C). Allocation is three times sizeof(int), not necessarily three bytes (D).

**Common misconception:** Pointer-variable lifetime and allocated-object lifetime differ.

## Q23

**Correct answer:** 5

**Concept:** Complement in a divisor lattice.

Since 30 has prime factors 2,3,5, a complement of 6=2×3 must supply 5 but neither 2 nor 3. Thus y=5, with gcd one and lcm thirty.

**Common misconception:** Using arithmetic subtraction instead of the lattice's meet and join.

## Q24

**Correct answer:** A, C, D

Each column is covered by two rows, so no implicant is essential (A). One row covers only two columns, requiring at least two rows. Both {P,R} and {Q,S} cover all four, proving C,D and disproving B. A row in one minimum cover is not necessarily present in every minimum cover.

## Q25

**Correct answer:** A, C

Division requires every B value in S for a selected A. Initially only 1 has both x and y, while P={1,2}, proving A and refuting B. Adding (2,y) makes both A values qualify, proving C. If S becomes {x}, both already have x, so D is false. Division expresses a universal matching condition.

## Q26

**Correct answer:** D

The shift yields floor(−3.5)=−4, while division truncates to−3. Difference−4−(−3)=−1, option D. A treats both rounding directions as identical; B reverses subtraction; C is unrelated to the two resulting integers.

## Q27

**Correct answer:** 0.000004
**Concept:** Effective access time and unit conversion.

The additional fault cost is 10,000,000 ns. Require 200+p×10,000,000≤240. Thus p≤40/10,000,000=0.000004. The wording says additional delay, so the normal 200 ns is not replaced on faults.

**Common misconception:** Mixing milliseconds and nanoseconds can cause an error of a millionfold.

## Q28

**Correct answer:** C

TCP provides an ordered byte stream. A read can return some available bytes, including bytes spanning application writes. Thus C is true. Timing can prevent the first call from gathering either particular length, so A and B are not guaranteed. TCP does not preserve write boundaries, making D false. Applications needing records must provide framing.

## Q29

**Correct answer:** A, C

**Concept:** Unique-light-edge cut property.

If an MST omitted e, adding e creates a cycle containing another crossing edge. That crossing edge is heavier because e is uniquely minimum; replacing it gives a lighter spanning tree, contradiction. Thus A and C hold. An MST may cross the cut through several edges, refuting B. A triangle with distinct edge weights supplies a cut-minimum edge that is not a bridge, refuting D.

**Common misconception:** Assuming an MST must cross every cut exactly once.

## Q30

**Correct answer:** A, C, D

Transposition reverses product order, giving Aᵀ=UᵀLᵀ, so A is true. Set y=Lᵀx; solve Uᵀy=b first, then Lᵀx=y, proving C. Reversing those solves in B generally solves the wrong product because the factors need not commute. Transposing a unit lower-triangular matrix gives unit upper triangular, proving D.

## Q31

**Correct answer:** 0.667 (exact)

**Concept:** Engineering Mathematics — Integration

1. The two expressions cross at x=1/3. The maximum is 1-2x to its left and x to its right.
2. The two integrals are [x-x^2] from 0 to 1/3 = 2/9 and [x^2/2] from 1/3 to 1 = 4/9.
3. Their sum is 2/3, which rounds to 0.667.

**Common misconception:** Integrate the upper expression separately on each side of its crossover.

## Q32

**Correct answer:** B
**Concept:** Handles in bottom-up parsing.

The stack suffix id matches T→id and must first become T. The stack then becomes E+T, permitting E→E+T. B is the next step. A reduces a right-hand side not yet present; C reverses a production in the wrong direction on the wrong symbol; D ignores reductions that remain after all tokens have been shifted.

**Common misconception:** Exhausting input does not imply that parsing is finished; reductions may still be necessary.

## Q33

**Correct answer:** A, C

Conditional next-address logic can select using a status flag(A), while a microinstruction can drive multiple nonconflicting controls in one cycle(C). Control stores can be read-only, so B is false. Different instructions or conditional paths may traverse different numbers of microinstructions, so D is false. Microprogramming specifies control sequencing; it does not impose equal instruction latency or writable storage.

## Q34

**Correct answer:** A

**Concept:** One-bit addition.

Unequal inputs yield sum one, giving XOR. Both inputs one produce carry one, giving AND. A combines these correctly. B mishandles 11 in its sum, C swaps incompatible functions, and D does not implement addition even at 00.

**Common misconception:** Using OR as the sum bit without checking the two-one case.

## Q35

**Correct answer:** B

At most one observation of the first dataset is strictly below2, and at most one of the second is below2 because its median is9. Thus the combined third observation is at least2. Similarly, at most two combined observations exceed9, so the fourth is at most9. Their average lies in[2,9], proving B. For datasets(0,2,3) and(8,9,10), the median is5.5 and need not be an observed value, disproving D. Datasets(0,2,2) and(2,9,9) give combined median2, disproving A. Extreme tail observations make the mean arbitrarily large or small, disproving C.

## Q36

**Correct answer:** A, B, D

Along a path from s to t, the potential terms telescope to h(s)−h(t), proving A and therefore B. On a cycle this difference is zero, proving D. Arbitrary potentials need not remove negative edges; h=0 preserves any originally negative edge, disproving C. Choosing feasible potentials is an additional step, separate from path-order preservation.

## Q37

**Correct answer:** 5

Concept: subgroup enumeration. Subgroup orders divide six. There is one trivial subgroup, three order-two subgroups generated by the three transpositions, and one order-three subgroup generated by either 3-cycle. All are cyclic and abelian. The only order-six subgroup is S3 itself, which is nonabelian. Total=1+3+1=5. The two 3-cycles generate the same subgroup and must not be counted twice.

## Q38

**Correct answer:** D
**Concept:** Division, candidate domains and vacuous truth.

With no required courses, every Student identifier satisfies QI's universal condition, giving {1,2}. QII considers only identifiers appearing in Enrollment, namely {1}; each vacuously covers all required courses. D is correct. A treats a universal over an empty set as false; B incorrectly narrows QI's domain; C adds identifier 2 to the division's specified candidate domain.

**Common misconception:** Equivalent-looking universal queries can differ because their candidate tuple domains differ.

## Q39

**Correct answer:** 4

Balanced middle probing on15 keys forms four decision levels with capacities1,2,4,8. A deepest successful key requires four comparisons. Counting splits without the final equality test would undercount.

## Q40

**Correct answer:** 0.75

**Concept:** Recovery-path lengths and expected first-entry time.

The five valid initial states contribute zero. Invalid 6 reaches 2 in one edge; 5 follows 5→6→2 in two; 7 follows 7→5→6→2 in three. The uniform expectation is (1+2+3)/8=0.75 edges.

**Common misconception:** Averaging only over invalid initial states despite the specified distribution over all states.

## Q41

**Correct answer:** B

**Concept:** Programming and Data Structures — C programming and pointers

In the first call, t points to a[0], and assigning *p=q changes the caller's p to a+1. The next statement makes a[0]=2+5=7, and the last makes a[1]=6. In the second call, t points to a[1], while the caller's p changes back to a. Therefore a[1]=6+7=13 and then a[0]=8. The final offset p-a is 0.

A omits the last increment of a[0]. B matches the trace. C fails to follow the second call's target changes. D is false: each side effect occurs in a separate full expression, all pointers stay within the valid array, and no incompatible-type access occurs.

- **A:** False: omits the final increment of a[0].
- **B:** True: the program prints 8 13 0.
- **C:** False: fails to track pointer target reassignment across function calls.
- **D:** False: all pointer arithmetic and side effects are within valid bounds and fully sequenced without undefined behavior.

**Common misconception:** Saving the pointer value in t preserves its old target even when a pointer-to-pointer argument changes the caller's p.

## Q42

**Correct answer:** 12

**Concept:** Degree counts in labelled-tree encodings.

In the Prüfer correspondence for six labelled vertices, the code has length four and label i appears di−1 times. The required multiset is {1,1,2,3}. Its distinct orderings number 4!/2!=12, each corresponding to exactly one labelled tree. The degree sum is ten, as required for a six-vertex tree.

**Common misconception:** Using degree rather than degree minus one as the code multiplicity.

## Q43

**Correct answer:** 2

The two exact occurrences of if become IF by tie priority. if2 and iff have longer identifier matches and become ID. Thus two ID tokens appear. Keyword priority applies only after longest-match selection, not to a prefix of a longer token.

## Q44

**Correct answer:** A, D

Concept: complete address decoding. First interval has high bits A15A14=00, so A is correct. Second interval has A15A14A13=010, giving D. B would also enable the chip over 0x6000–0x7FFF, creating unwanted aliases. Mapped capacity is 16+8=24 KiB of 64 KiB, leaving 40 KiB, so C is false. Chip offset bits and chip-selection bits serve different roles.

## Q45

**Correct answer:** 5

Let C(n) count calls with argument2 within F(n). C(0)=C(1)=0 and C(2)=1. For n>2, C(n)=C(n−1)+C(n−2), so C(3)=1,C(4)=2,C(5)=3,C(6)=5. Counting distinct arguments would give one occurrence of2 and ignore repeated evaluation without memoization.

## Q46

**Correct answer:** 12 (exact)

**Concept:** Operating Systems — Concurrency and synchronization

There are 6!/(2×2×2) = 90 interleavings preserving each read-before-write order. Enumerate them while retaining a private register for each thread; the final values are [1, 3, 4, 5, 6, 7, 8, 9, 11, 12, 14, 17], giving 12 distinct outcomes. A direct derivation partitions by the last writer: if A is last, its read can see 0,3,5,8, giving 1,7,11,17; if B is last, its read can see 0,1,5,6,11, giving 3,4,8,9,14; if C is last, its read can see 0,1,3,4,7, giving 5,6,8,9,12. The union of these sets gives the stated answer. The values before a last writer's read come only from the other two threads, which may themselves overlap.

**Common misconception:** Atomic reads and writes do not make a read-modify-write pair atomic.

## Q47

**Correct answer:** A, B

The usable DNS cache can supply the address without a new query(A). An entity-tag conditional request can receive a not-modified response and reuse the body(B). DNS freshness concerns name-to-address information, not resource freshness(C). HTTP receipt does not reset DNS TTL(D). The two caches have independent validity rules.

## Q48

**Correct answer:** A, B, D

If the complement were regular, complementing it again would make L regular, a contradiction; A is true. The union in B equalsΣ*, which is regular. C is false: for L={a^n b^n}, intersection with the infinite regular language a* is just{ε}. For D, if deleting a finite set made L regular, adding back the finitely many removed words would make L regular by closure under finite union; this is impossible. Nonregularity is not preserved under every intersection.

## Q49

**Correct answer:** A

**Concept:** Computer Organization and Architecture — Memory hierarchy and performance

The expected additional cost of an L1 miss is 6+0.20×60=18 ns. The initial mean is 1+0.10×18=2.8 ns. The redesigned mean is t+0.05×18=t+0.9 ns. Strict improvement requires t+0.9<2.8, or t<1.9 ns. The L2 miss probability is local, so only the fraction 0.10×0.20 (or 0.05×0.20) of all accesses reaches memory.

- **A:** True: the redesign saves 0.9 ns of expected miss cost, so L1 can rise by less than that.
- **B:** False: it ignores the redesigned system's remaining 0.9 ns expected miss cost.
- **C:** False: this is sufficient but not necessary; for example t=1.8 ns also improves performance.
- **D:** False: values such as t=3 ns satisfy it but are slower than the original.

**Common misconception:** Local miss rates must be multiplied along the hierarchy, and a hit-time increase affects every access.

## Q50

**Correct answer:** 4

Only key1 matches. Each of A's two occurrences matches each of B's two, giving2×2=4 rows. Keys2 and3 have no partners. Projection without DISTINCT preserves those four occurrences under bag semantics. A join is not a one-to-one pairing of duplicate rows.

## Q51

**Correct answer:** C

The pumping lemma is a necessary condition for regularity, not a characterization. Its conclusion alone therefore does not establish regularity, so C is correct. A incorrectly reverses the implication; B and D assert additional classifications not supplied by the condition. A failed attempt to contradict pumping is not a regularity proof.

## Q52

**Correct answer:** A, B

**Concept:** Removing necessary deadlock conditions.

A imposes one resource order and rules out a circular wait. B prevents hold-and-wait because an unsuccessful acquisition holds neither resource. C changes scheduling priority but cannot supply the blocked resource. D explicitly allows the original hold-and-wait cycle. Thus only A and B guarantee prevention here.

**Common misconception:** Expecting CPU scheduling changes to resolve a resource cycle.

## Q53

**Correct answer:** 684

The IP payload has600+8=608 bytes. Each fragment can carry at most 380 payload bytes, but a nonfinal payload must be a multiple of 8, so the first carries376 and the second232. Payload remains608 in total; two IP headers add40 and two link overheads add36. Total 608+40+36=684. The UDP header is included once, not repeated per IP fragment.

## Q54

**Correct answer:** 3.2

Serialization takes1200/600=2 seconds and1200/1200=1 second. Store-and-forward requires both for this one packet. Add two propagation delays of0.1, giving3.2 seconds. There is no packet splitting to permit overlapping transmission of separate packets.

## Q55

**Correct answer:** 10

Concept: queue order at a quantum boundary. Timeline: P 0–2; Q 2–4; R 4–5; P 5–7; Q 7–8; P 8–9. At time 2 the queue is Q,R,P by the specified arrival rule. Completion times are 9,8,5. Waiting times C−arrival−burst are 4,4,2, total ten. A boundary convention can change later queue order and must not be assumed silently.

## Q56

**Correct answer:** -3

Left grouping gives sat(7+3)=7, followed by sat(7−3)=4. Right grouping gives sat(3−3)=0, then sat(7+0)=7. The requested difference is4−7=−3. Saturating addition is not associative, even though ordinary integer addition is.

## Q57

**Correct answer:** A, C

Both original S alternatives have FIRST set {a}, causing an LL(1) table conflict: A. Factoring leaves alternatives b and c with disjoint FIRST sets, giving the equivalent LL(1) grammar in C; this disproves B. Each generated string, ab or ac, has a unique parse tree, so D is false. Failure of a particular grammar to be LL(1) does not imply ambiguity or impossibility of an LL(1) grammar for its language.

## Q58

**Correct answer:** 4

The cycles are (0), (1,2,4,8), (3,6,12,9), (5,10), and (7,14,13,11). Only (0) is a fixed point, leaving four nontrivial cycles. Each index appears once because multiplication by 2 is invertible modulo 15. Counting moves or moved elements would give a different quantity from the number of cycles.

## Q59

**Correct answer:** 2

Work modulo2. (u+v)(v+w)+uw simplifies to uv+v+vw=v(u+1+w). It is1 precisely when v=1 and u=w, giving(0,1,0) and(1,1,1). The duplicate uw terms cancel in parity arithmetic.

## Q60

**Correct answer:** A, B, D

**Concept:** Commuting idempotents and joint eigenspaces.

An idempotent is diagonalizable with eigenvalues 0 and 1. Commuting idempotents preserve one another's eigenspaces and can be diagonalized together. Let k be the dimension where both eigenvalues are 1. The dimensions for joint eigenvalues (1,1),(1,0),(0,1),(0,0) are k,3−k,2−k,k−1. Nonnegativity forces k=1 or 2. Thus rank(E−F)=5−2k is 3 or 1 (A), trace(E+F)=3+2=5 (B), and rank(EF)=k need not be 2 (C false). If k=1, E+F has eigenvalues 2,1,1,1 and determinant 2; if k=2 it has a zero eigenvalue and determinant 0 (D).

**Common misconception:** Identifying the product's rank with the smaller rank without considering the intersection.

## Q61

**Correct answer:** A, C

Concept: affine hashing over a prime field. Given outputs r,s, subtract the equations to get a(x−y)=r−s modulo five. Since x−y is nonzero, its inverse determines one a, and then b is determined, proving A. Equal outputs occur exactly when a=0, with probability 1/5, proving C and disproving B because these functions are constant. Conditional on a≠0, outputs can never be equal, whereas independent uniforms would be equal with probability 1/5; D is false. Conditioning can destroy pairwise independence.

## Q62

**Correct answer:** A, C

Every string has finitely many predecessors in length-lexicographic order, and D halts on each. Therefore every member is eventually reached and printed, proving A. The enumerator continues testing strings even when L is empty or finite, so B is false and C true. Individual termination suffices for progress; no known uniform runtime bound is needed, disproving D. Enumeration need not announce when the final member has been printed.

## Q63

**Correct answer:** A, C
**Concept:** Join multiplicities under set semantics and functional dependencies.

Each of two R rows matches both S rows on B=x. J contains (1,x,p),(1,x,q),(2,x,p),(2,x,q), so A holds. Each A value has two C values, refuting B. Projecting away C yields exactly the two original R rows, proving C. B=x occurs in four tuples, so it is not a key, refuting D.

**Common misconception:** Set semantics eliminate duplicate complete tuples, not distinct matching combinations.

## Q64

**Correct answer:** 2

Concept: normalized recurrences and generating sums. Divide by 2ⁿ: b_n=b_(n−1)+n/2ⁿ, b0=0. Thus b_n=Σ(k=1..n)k/2ᵏ. From Σk xᵏ=x/(1−x)² for |x|<1, the limit at x=1/2 is two. Equivalently a_n=2^(n+1)−n−2. Solving only the homogeneous recurrence would miss the limiting coefficient.

## Q65

**Correct answer:** 7

Below4, spacing is1/4, so the predecessor is3.75; above4, spacing is1/2, so the successor is4.5. The rounding interval for4 therefore extends from midpoint3.875 to midpoint4.25. Both ties round to4 because its significand1000 has even low bit, whereas neighbouring significands1111 and1001 have odd low bits. Multiplying endpoints by16 gives k=62 through68 inclusive, seven integers. The rounding interval is asymmetric at a binade boundary.

