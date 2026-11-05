# GATE CS 2027 — Mock 012: Worked Solutions

## Q1

**Correct answer:** 17

**Concept:** Applying an alternating recurrence.

The terms are 3,6,5,10,9,18,17. Six updates produce the seventh term, 17.

**Common misconception:** Repeating only one operation or counting the initial term as an update.

## Q2

**Correct answer:** 4.8

**Concept:** Two expressions for triangle area.

The hypotenuse is √(6²+8²)=10. Area is (1/2)6×8=24, also (1/2)10h. Therefore h=48/10=4.8 cm.

**Common misconception:** Using a perpendicular side as the hypotenuse when applying the area formula.

## Q3

**Correct answer:** B

**Concept:** Clear subject assignment in modifying clauses.

B explicitly gives Meera as the subject of submitting and checking, with the correct time order. A leaves an introductory participial clause grammatically attached to “the figures”; C makes figures submit a report; D grammatically describes Meera as having been submitted. These defects prevent the unambiguous intended statement.

**Common misconception:** Assuming a reader's ability to guess the intended actor repairs a dangling modifier.

## Q4

**Correct answer:** 19

**Concept:** Weighted subgroup percentages.

Remote part-timers form 0.60×0.25=0.15 of all employees. Other part-timers form 0.40×0.10=0.04. Together they are 0.19, or 19%.

**Common misconception:** Adding subgroup percentages without weighting their group sizes.

## Q5

**Correct answer:** C

**Concept:** Exclusive truth conditions.

If the key is in drawer 1, both P and Q are true. In drawer 2, both are false. In drawer 3, P is false and Q true, so exactly one holds. C alone satisfies the premises; A,B fail and D incorrectly includes them.

**Common misconception:** Reading “exactly one” as “at least one”.

## Q6

**Correct answer:** A

**Concept:** Ordered three-dimensional transformations.

The first transformation gives (−2,1,3). Applying the second to these updated coordinates gives (−2,−3,1), A. B interchanges axes differently, C loses the required signs, and D reverses the second rotation's signs.

**Common misconception:** Applying both transformations to the original coordinates rather than composing them.

## Q7

**Correct answer:** B

**Concept:** Self-selection and causal direction.

People already inclined to exercise might choose locations near parks. This is the alternative causal direction described by B. Different measurement units (A) do not invalidate association; C reverses the reported association without justification; D denies the very selection mechanism identified.

**Common misconception:** Assuming location was assigned independently of residents' preferences.

## Q8

**Correct answer:** 48

**Concept:** Circular arrangements with opposite-pair constraints.

Fix one specified person to remove rotational duplication; their partner's opposite seat is forced. Assign the other three couples to the three remaining opposite seat-pairs in 3! ways, then orient each couple in two ways. Total 3!×2³=48. Reflections have not been identified and are correctly counted separately.

**Common misconception:** Dividing by rotations again after already fixing an anchor person.

## Q9

**Correct answer:** 10

**Concept:** A target weighted rate.

After two days, 30 of 40 jobs are complete. With x Wednesday jobs, all completed, require (30+x)/(40+x)≥0.8. This simplifies to 0.2x≥2, or x≥10. Ten is feasible and achieves exactly 80%.

**Common misconception:** Averaging daily percentages without weighting the daily job counts.

## Q10

**Correct answer:** 3

**Concept:** Unfolded cuts and connectivity.

The cut removes [1,2] and its reflection [10,11]. The remaining positive-length intervals are [0,1), (2,10), and (11,12], giving three pieces. Boundary conventions do not affect the count under the stated rule.

**Common misconception:** Counting cuts rather than resulting connected components.

## Q11

**Correct answer:** A

**Concept:** LOOK direction and reversal point.

Starting upward, the head serves 55 then 70, reverses at the final pending request, and serves 30 then 10. A matches. B reverses too soon; C changes direction before serving all upward requests; D skips nearer upward request 55 on its outward pass.

**Common misconception:** Confusing LOOK with shortest-seek-first or with movement to the disk's physical endpoint.

## Q12

**Correct answer:** A, C

**Concept:** Encapsulation across routed hops.

The router removes the incoming link framing and constructs an outgoing frame appropriate to the next hop, proving A. IP and link addresses address different scopes, proving C. The next-hop frame address generally differs, refuting B; routed IP delivery still needs the destination IP address, refuting D.

**Common misconception:** Treating hop-local addresses as unchanged end-to-end identifiers.

## Q13

**Correct answer:** 37

**Concept:** Logical shift and unsigned interpretation.

10010110₂ shifted right twice with zero fill becomes 00100101₂, equal to 32+4+1=37.

**Common misconception:** Sign-extending as if an arithmetic shift had been requested.

## Q14

**Correct answer:** B

**Concept:** Pointer offsets and postfix increment.

p points to a[1]=4. Therefore *(p+1) is a[2]=6, giving B. A yields the old pointed-to value 4 before advancing p; C is 4+1=5; D is a[0]=2. Each option is evaluated independently from the stated declaration.

**Common misconception:** Confusing addition to the pointed-to value with addition to the pointer.

## Q15

**Correct answer:** 1

**Concept:** Memory-resident sparse index lookup.

The index identifies the data block without a disk access because it is resident. The present record then requires one data-block read. No additional search across disk blocks is needed under the given index assumptions.

**Common misconception:** Charging a disk read for an explicitly memory-resident index.

## Q16

**Correct answer:** A

**Concept:** Control links versus lexical links.

The dynamic link identifies the caller's activation for return-time restoration. A holds. A static link follows lexical enclosure and need not identify the caller, refuting B. Symbol-table and heap-object pointers in C,D do not restore the caller's activation.

**Common misconception:** Assuming caller and lexical parent always coincide.

## Q17

**Correct answer:** A, B

**Concept:** Equivalent Boolean XOR forms.

A lists the two unequal-input minterms. Expanding B gives xx′+xy′+yx′+yy′=xy′+x′y, so B is identical. C is XNOR, true on equal inputs. D is also true at x=y=1, where XOR is false.

**Common misconception:** Confusing inclusive OR with exclusive OR.

## Q18

**Correct answer:** 4

**Concept:** Iterated floor roots.

The values are 1024→32→5→2→1. Four replacements occur before the stopping condition holds.

**Common misconception:** Approximating every root without applying the floor at each stage.

## Q19

**Correct answer:** A

**Concept:** Gray-code adjacency in Karnaugh maps.

The order makes each adjacent pair differ in one variable, including 10 next to 00 at wraparound. Such pairs can combine while eliminating one literal. A holds. B wrongly universalizes a display convention; C confuses reordering with changing function values; D states the opposite adjacency condition.

**Common misconception:** Ignoring edge wraparound when reasoning about adjacent map cells.

## Q20

**Correct answer:** 62.5

**Concept:** Reserved capacity utilization.

The connection reserves 64000 bits of transmission capacity in one second and uses 40000 for payload. Utilization is 100×40000/64000=62.5%.

**Common misconception:** Using binary kilo despite the explicit decimal definition.

## Q21

**Correct answer:** C

**Concept:** Regular versus unbounded matching requirements.

C has regular expression (aa)*b*. A requires matching two unbounded counts and is nonregular. For B, pumping a sufficiently long prime-length unary word by q extra copies of a nonempty pumped block, where q is the chosen prime length, gives composite length q(1+|y|), violating the prime condition. D is nonregular: distinct prefixes 0^n1 are distinguished by suffixes 0^n1, since equality of the two zero-block lengths is required for the resulting two-one word to be a square.

**Common misconception:** Treating all numerical length restrictions as nonregular; fixed modular restrictions are regular.

## Q22

**Correct answer:** 2

**Concept:** Reachability after unlinking.

B.next originally points to C, and C.next is H. The assignment changes B.next to H, so traversal is H→A→B→H. A and B remain reachable; C remains allocated but is outside this list traversal. Two data nodes are counted.

**Common misconception:** Equating allocated nodes with nodes reachable from the list head.

## Q23

**Correct answer:** B

**Concept:** A counterexample to greedy coin selection.

Greedy chooses 4, then 1, then 1, using three coins. The feasible choice 3+3 uses two, and one coin cannot make six. Thus B is correct. A gives the wrong greedy count; C ignores denomination one; D ignores 3+3.

**Common misconception:** Assuming the familiar greedy rule works for every denomination system.

## Q24

**Correct answer:** 0.8333

**Concept:** Probability normalization.

The total probability is 6k=1, so k=1/6. Therefore P(X≥1)=2k+3k=5/6=0.833333…, rounding to 0.8333. Accepted range: 0.83325–0.83335.

**Common misconception:** Adding unnormalized weights as if they were probabilities.

## Q25

**Correct answer:** A

**Concept:** Microprogrammed versus hardwired control.

Stored control-word sequences characterize microprogramming, and altering them can alter sequencing, establishing A. Such a design still needs sequencing logic, refuting B. C incorrectly assigns microinstruction fetching to the hardwired design. The ISA need not expose internal control formats, refuting D.

**Common misconception:** Treating an instruction-set specification as a specification of internal control implementation.

## Q26

**Correct answer:** 5

**Concept:** Circular queue distance.

The occupied length is (rear−front+8) mod 8=(3−6+8) mod 8=5. Occupied slots are 6,7,0,1,2; rear=3 is the next insertion slot.

**Common misconception:** Counting the rear slot as already occupied.

## Q27

**Correct answer:** A

**Concept:** Reusing a common scalar subexpression.

Compute the shared sum once and square it: one addition and one multiplication. A does this. B gives 2ab, C also gives 2ab, and D gives a+2b; none equals (a+b)² for all operands.

**Common misconception:** Confusing algebraic expansion with a computation that preserves all terms.

## Q28

**Correct answer:** 0

**Concept:** Relational composition.

Taking two steps around the three-cycle yields R∘R={(1,3),(2,1),(3,2)}. None is in the original forward one-step relation, so the intersection is empty.

**Common misconception:** Treating relational composition as set intersection or union.

## Q29

**Correct answer:** 3288

**Concept:** Final-page internal fragmentation.

Three 4096-byte pages are needed, allocating 12288 bytes. Unused bytes in the last page are 12288−9000=3288. Earlier pages are full because the region begins on a boundary.

**Common misconception:** Counting whole unused pages as part of this allocation.

## Q30

**Correct answer:** 3

**Concept:** Image contained in kernel for a square-zero map.

A²=0 implies im(A)⊆ker(A). If rank is r, rank–nullity gives r≤6−r, so r≤3. Three independent 2×2 nilpotent blocks with rows (0,1),(0,0) attain rank three, proving the maximum.

**Common misconception:** Concluding A itself must be zero merely because A² is zero.

## Q31

**Correct answer:** A, C

**Concept:** Rolle's theorem and compact-interval extrema.

Rolle's theorem gives A, while continuity on the closed bounded interval gives C. Nonconstant examples such as 1+x(2−x) refute B. To refute D, use 1+x(x−2)(x+1): its endpoint values are one but its derivative at one is nonzero.

**Common misconception:** Assuming Rolle's point must be the midpoint.

## Q32

**Correct answer:** 0.5714

**Concept:** Conditioning on a union.

Independence gives P(A∩B)=0.2, hence P(A∪B)=0.4+0.5−0.2=0.7. Since A⊆A∪B, the conditional probability is 0.4/0.7=4/7=0.571428…, rounding to 0.5714. Accepted range: 0.57135–0.57145.

**Common misconception:** Assuming A stays independent of an event that explicitly includes A.

## Q33

**Correct answer:** A

**Concept:** Leaf chains in B+ trees.

Sibling links allow a scan to continue directly to the next leaf, establishing A. B is not a B+ tree invariant; C describes no ordinary single-root B+ tree; D removes needed navigation separators and does not explain scanning.

**Common misconception:** Assuming every successive key retrieval must begin at the root.

## Q34

**Correct answer:** B

**Concept:** Universal decomposition requirement in a CFL pumping proof.

For a claimed pumping length, choose an appropriate long word, then show that every valid decomposition has some pumping exponent leaving the language. B states the needed decomposition range. A restricts it incorrectly, C violates |vy|>0, and D omits the central proof obligation.

**Common misconception:** Choosing a convenient decomposition that the pumping property never promised would work.

## Q35

**Correct answer:** 1

**Concept:** Demand paging on a legal access.

The missing resident page triggers one fault. Successful handling installs it and restarts the access, which then succeeds under the stated assumptions. Validity and permission do not mean residency.

**Common misconception:** Treating every fault as an illegal-address error.

## Q36

**Correct answer:** A, C

**Concept:** Direction of many-one reductions.

To decide A using a decider for B, compute f(x) and run that decider; total computability guarantees termination, proving A. The same composition with a recognizer shows that recognizable B would imply recognizable A; its contrapositive proves C. B and D fail, for example, when A is empty and B is a nonrecognizable language with a known fixed nonmember used as the constant output of f. An easy source language does not force an easy target.

**Common misconception:** Reversing the direction in which a reduction transfers an upper bound.

## Q37

**Correct answer:** 2

**Concept:** Ties among optimal compatible subsets.

Before time 4, either A and B together or C alone gives value eight, and no compatible selection exceeds eight. D is compatible with both and adds one, giving optimal value nine. The two maximizing subsets are {A,B,D} and {C,D}.

**Common misconception:** Returning one optimal solution without counting another with the same value.

## Q38

**Correct answer:** C

**Concept:** Undo/redo recovery.

T1 committed, so recovery ensures its X=8 update is present through redo if necessary. T2 did not commit, so its Y=9 update must be undone to Y=4 if it reached disk. The final pair is (8,4), C. A loses committed work, B retains uncommitted work, and D does both.

**Common misconception:** Letting the accidental precrash disk state determine the final recovered values.

## Q39

**Correct answer:** 1

**Concept:** Essential coverage and minimum covers.

Column 2 is covered only by P, making P mandatory. After P, columns 4,5,6 remain and R covers all three. No single implicant covers all columns, so {P,R} is a two-implicant optimum. Neither Q nor S alone completes P, making that minimum cover unique. The answer counts covers, not implicants, and is one.

**Common misconception:** Reporting the minimum number of implicants instead of the number of minimum covers.

## Q40

**Correct answer:** A, B, C

**Concept:** Modular identities and unsigned division.

A is repeated addition modulo 2^w. B follows cancellation in the modular additive group. For unsigned values, logical right shift by one equals truncating division by two, giving C. D fails already at x=1, where division gives zero and multiplication gives two since w≥2.

**Common misconception:** Importing signed-overflow or sign-extension concerns into explicitly unsigned modular arithmetic.

## Q41

**Correct answer:** 3

**Concept:** Topological orders of a precedence graph.

The only constraint is T1 before T3. The orders are T1,T2,T3; T1,T3,T2; and T2,T1,T3. Equivalently, half of the 3! permutations satisfy the single ordered-pair constraint.

**Common misconception:** Assuming an acyclic schedule has only one equivalent serial order.

## Q42

**Correct answer:** C

**Concept:** Unequal constant-fraction recursion splits.

At each nonterminal level, total subproblem sizes sum to at most n, giving O(n) work per level. Every root-to-leaf path has O(log n) depth because the largest child shrinks by a fixed factor, so O(n log n) follows. For the first Θ(log n) levels before even the smallest descendants reach base size, aggregate work is Θ(n) per level, giving the matching lower bound. Thus C holds; A and B omit required level work and D overestimates it.

**Common misconception:** Assuming only exactly equal halves give an n log n recurrence.

## Q43

**Correct answer:** B

**Concept:** Precision limits of an abstract domain.

At the merge, x can be 2 or 3 and is not a known constant, so A is false. A constant-only evaluator may treat both operands as unknown and fail to retain their equality, whereas algebra proves x−x=0. B captures that distinction. Each execution uses the same x twice, so C is impossible; unknown p does not invalidate the identity, refuting D.

**Common misconception:** Treating separate occurrences of the same variable as independently chosen values.

## Q44

**Correct answer:** 1

**Concept:** Polynomial long division over GF(2).

Starting with 1101000, XOR shifted 1011 successively to eliminate leading ones:

```text
1101000 XOR 1011000 = 0110000
0110000 XOR 0101100 = 0011100
0011100 XOR 0010110 = 0001010
0001010 XOR 0001011 = 0000001
```

The remainder is 001, unsigned value one. Subtraction is XOR, without borrows.

**Common misconception:** Performing ordinary integer division instead of polynomial division.

## Q45

**Correct answer:** 400

**Concept:** Round-trip collision-detection bound.

A worst-case collision notification takes twice the one-way propagation delay, or four microseconds. At 100×10⁶ bits/s, the sender must transmit for at least 4×10⁻⁶ seconds, corresponding to 400 bits. The question specifies an ideal protocol rather than an Ethernet framing minimum.

**Common misconception:** Using one-way propagation or inserting standard-specific framing constraints excluded by the assumptions.

## Q46

**Correct answer:** A

**Concept:** Tree reconstruction from traversals.

Preorder makes A the root. Inorder splits left D,B,E from right C,F. The left subtree root is B with children D,E; the right subtree root is C with right child F. Postorder is D,E,B,F,C,A, option A. B places B before E, C reverses children and right-subtree order, and D interleaves nodes from different subtrees.

**Common misconception:** Preserving preorder's root-first order while attempting a postorder traversal.

## Q47

**Correct answer:** 4

**Concept:** Address aliasing under incomplete decoding.

The low twelve bits are fixed to 0x123, and A15,A14 are fixed to 1,0. A13,A12 can independently be 00,01,10,11, producing addresses 0x8123,0x9123,0xA123,0xB123. All select the same location. There are four aliases.

**Common misconception:** Assuming every machine address bit is decoded uniquely by a chip.

## Q48

**Correct answer:** A, B, D

**Concept:** Product automata with Boolean acceptance predicates.

Both components accepting implements intersection (A). Exactly one implements symmetric difference (B). First accepting and second rejecting implements set difference (D). At least one implements union, not concatenation, so C is false. Concatenation needs tracking a split point rather than merely simultaneous acceptance of the entire same input.

**Common misconception:** Confusing Boolean combination of whole-word acceptance with sequential language composition.

## Q49

**Correct answer:** B

**Concept:** Directory-link count versus open references.

Removing the two links removes names but the open descriptor still keeps the file available. Closing the last descriptor then leaves no links or open references, permitting reclamation, B. A leaves both a link and an open reference; C and D do not remove the remaining reference.

**Common misconception:** Equating removal of a filename with immediate destruction of an open file's storage.

## Q50

**Correct answer:** 0

**Concept:** Interval enumeration in a subset lattice.

The meet is {b} and the join {a,b,c}. The interval contains exactly {b},{a,b},{b,c},{a,b,c}. The first and last are comparable with both X,Y; X is comparable with itself, as is Y. None is incomparable with both, so the count is zero.

**Common misconception:** Considering {a,c}, which is incomparable with both but does not contain the required meet {b}.

## Q51

**Correct answer:** A, B

**Concept:** Process-image replacement versus process identity.

The specified semantics preserve the PID and unmarked descriptors while replacing the address space, directly giving A and B. Old heap pointers have no guarantee of their old objects after replacement, refuting C. D contradicts the descriptor-preservation rule.

**Common misconception:** Treating successful exec as creation of a new process or preservation of the old memory image.

## Q52

**Correct answer:** 9

**Concept:** Synchronous distance-vector updates with stale information.

Using initial (1,2,2), round one yields A=min(1+2,1+2)=3, B=min(1+1,1+2)=2, C=2. From (3,2,2), round two yields A=3, B=min(4,3)=3, C=3. The sum is nine. Every router uses the same previous-round snapshot, not updates already computed within the current round.

**Common misconception:** Mixing synchronous rounds with sequential in-place updates or silently applying poison reverse.

## Q53

**Correct answer:** 80

**Concept:** Interleaving subtree insertion sequences.

Root 4 must be first. Choose three of the remaining six positions for left-subtree keys, in choose(6,3)=20 ways. Within the left subtree, 2 must precede 1 and 3, whose order has two choices. The right subtree similarly has two orders after 6. Total 20×2×2=80.

**Common misconception:** Requiring all left-subtree insertions to precede all right-subtree insertions.

## Q54

**Correct answer:** A, B, D

**Concept:** Structural description of a grammar's language.

Each S expansion adds a at the front and b at the end; T generates an arbitrary central block of c symbols. Thus the language is {aⁿcᵐbⁿ:n,m≥0}. A and B follow. abcc puts c symbols after b and cannot be generated, so C is false. aacbb has n=2,m=1, proving D.

**Common misconception:** Tracking symbol counts without tracking their ordering restrictions.

## Q55

**Correct answer:** C

**Concept:** Mux selection and dependency.

Select 00 gives constant zero and select 11 constant one, both independent of x. Select 01 gives x and 10 gives its complement, both dependent. C lists exactly the correct settings. A and B omit one; D lists the dependent settings.

**Common misconception:** Treating inversion of an input as independence from that input.

## Q56

**Correct answer:** 2

**Concept:** Sink components of a condensation graph.

The SCCs are {a,b}, {c,d}, {e}, {f}. Their cross-component edges form {a,b}→{c,d}→{e}, while {f} is isolated. Only {e} and {f} have no outgoing component edge, so there are two sinks.

**Common misconception:** Excluding an isolated component from the sink count.

## Q57

**Correct answer:** B

**Concept:** Many-to-one threading and blocking calls.

Every user thread needs the single kernel-scheduled execution context. When it blocks, none of those threads can execute through it, establishing B. A and C invent additional kernel contexts; D imagines execution without a runnable scheduled context.

**Common misconception:** Assuming the number of user threads equals the number of independently schedulable kernel threads.

## Q58

**Correct answer:** 2.5

**Concept:** Nested conditional cache-miss probabilities.

All accesses cost one ns. An L1 miss adds an average 5+0.20×50=15 ns. Weighting by the L1 miss probability gives 1+0.10×15=2.5 ns. The main-memory access probability is 0.10×0.20=0.02, not 0.20.

**Common misconception:** Applying a local L2 miss rate to all CPU memory accesses.

## Q59

**Correct answer:** 1

**Concept:** Pivoting before LU elimination.

After the swap, rows are (2,1,0),(0,1,1),(4,3,2). The first-column multipliers are zero and two. Eliminating row three gives (0,1,2); dividing its second entry by the row-two pivot one gives L32=1. The final U33 is then one.

**Common misconception:** Reading elimination multipliers from the unswapped matrix.

## Q60

**Correct answer:** 12

**Concept:** Relationship degree bounds and attainability.

Six employees with outdegree at most two give at most twelve pairs. Number them cyclically 0–5 and let each mentor the next two employees modulo six. This gives exactly two outgoing and two incoming pairs for every employee, with no self-pairs, attaining twelve.

**Common misconception:** Treating the minimum incoming-degree requirement as incompatible with the maximum outgoing-degree bound without checking a construction.

## Q61

**Correct answer:** 1.8333

**Concept:** Splitting an absolute-value integral at sign changes.

x²−x=x(x−1) is nonnegative on [−1,0] and [1,2] and nonpositive on [0,1]. The three contributions are 5/6,1/6,5/6 respectively, summing to 11/6=1.833333…. Accepted range: 1.83325–1.83335.

**Common misconception:** Taking the absolute value of the signed total integral instead of integrating the absolute value.

## Q62

**Correct answer:** 13.75

**Concept:** Within-group and between-group population variance.

The weights are 1/4 and 3/4, and the combined mean is 6.5. Variance is (1/4)[1+(2−6.5)²]+(3/4)[9+(8−6.5)²]=13.75. Equivalently, within-group variance 7 plus between-group variance (1/4)(3/4)(8−2)²=6.75 gives 13.75.

**Common misconception:** Averaging only subgroup variances and ignoring differences in means.

## Q63

**Correct answer:** A, B, C

**Concept:** Liveness at a loop fixed point.

At L, p is read by the test, so C is live. The exit branch reads x, and B's assignment also reads old x, so A is live. The path into B reads old y before assigning y=0, making B live. These paths establish all three at the least fixed point; no use of z can propagate liveness, so D is false.

**Common misconception:** Treating a later assignment to y as killing its earlier use within the same iteration.

## Q64

**Correct answer:** 1

**Concept:** Arbitrary heap deletion may require upward repair.

Move final value 17 into index 4, whose parent at index 2 contains 15. Swap them once. Now 17 has parent 20 and children 15 and 10; all satisfy max-heap order. The resulting heap is [20,17,18,15,10,12]. No further swap is needed.

**Common misconception:** Always sifting down after deleting a nonroot heap element.

## Q65

**Correct answer:** 0.75

**Concept:** Recovery-path lengths and expected first-entry time.

The five valid initial states contribute zero. Invalid 6 reaches 2 in one edge; 5 follows 5→6→2 in two; 7 follows 7→5→6→2 in three. The uniform expectation is (1+2+3)/8=0.75 edges.

**Common misconception:** Averaging only over invalid initial states despite the specified distribution over all states.
