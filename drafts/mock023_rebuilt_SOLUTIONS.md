# Worked Solutions — GATE CS 2027 Mock Test 023

## Q1

**Correct answer:** C

Both f(n)=2n and f(n)=2n+(n−1)(n−2)(n−3) fit all observations but give different values at4. Thus C is true and A,B unjustified. D is contradicted by either example. Finite observations do not specify an unrestricted function uniquely.

## Q2

**Correct answer:** 4

Any full projection has four occupied cells, and one cube covers only one cell of that projection, so at least four cubes are needed. Occupy coordinates000,011,101,110, using0/1 coordinates. Their projection onto each coordinate pair contains all four pairs, attaining the bound. Projection coverage does not require all eight cubes.

## Q3

**Correct answer:** 2

The recurrence gives a(n)=n². The inequality is2n+1>n², which for positive integers holds only at n=1,2. At n=3 it fails, and n²−2n−1 increases thereafter. The ten-term range therefore contains two solutions.

## Q4

**Correct answer:** 49

The two base triangles are similar, so their base ratio is sqrt(9/16)=3/4. The two side triangles each have area sqrt(9×16)=12, by the shared-height area ratios induced by the diagonal intersection. Total9+16+12+12=49. Equivalently, total area is(sqrt9+sqrt16)²; simply adding the given areas omits the side triangles.

## Q5

**Correct answer:** B

B permits a different reviewer for each report, expressing for every report there exists a reviewer. A requires one reviewer for all; C requires every reviewer for all; D denies reading. The order of quantifiers changes the claim.

## Q6

**Correct answer:** 9

Thirty questions were attempted. With w wrong and30−w correct, the score is4(30−w)−w=120−5w=75. Thus w=9. Omitted questions do not incur a penalty, and a wrong response costs five marks relative to a correct one.

## Q7

**Correct answer:** D

If A is absent, the three statements are true,false,true. If B is absent, they are false,false,false. If C is absent, they are true,true,false. The counts of true statements are2,0,2, never1. Thus none of A,B,C can be the absent person under all conditions and D is correct. The task requires checking consistency, not assuming the conditions have a solution.
## Q8

**Correct answer:** A, C

A reflection reverses orientation and a rotation preserves it, proving A. Two reversals restore orientation and both maps preserve distances, proving C. Two different parallel-line reflections can give a nonzero translation, disproving B. Translation preserves area, disproving D. Orientation preservation does not mean every point is fixed.

## Q9

**Correct answer:** D

The qualification explicitly denies inferring impossibility from zero observed failures. D asserts exactly that inference and conflicts. A restates the observation; B and C acknowledge untested possibilities and future revision. Empirical absence is not a universal logical proof.

## Q10

**Correct answer:** 18

Arrange B,B,C in three distinct orders. Each has four gaps around/between its letters. Put the two identical A's in two distinct gaps to avoid adjacency: choose(4,2)=6 choices. Total3×6=18. Selecting distinct gaps prevents AA without distinguishing the two A copies.

## Q11

**Correct answer:** 5

Packet1 arrives completely at1 ms and occupies the output from1 to3 ms. Packet2 arrives completely at2 ms, waits until3, and leaves at5. Store-and-forward reception and output queuing must both be counted.

## Q12

**Correct answer:** 2

Each outer1 has an equal inner1 and is rejected. Outer2 has no match. OuterNULL also has no true equality match, even against innerNULL, so it survives NOT EXISTS. Two rows remain. NOT EXISTS is not interchangeable with NOT IN when NULLs occur.

## Q13

**Correct answer:** 5

Left2 exceeds right1, contributing1; left5 exceeds only1, contributing1; left7 exceeds1,5,6, contributing3. Total5. Equal5 values are not inversions because the comparison is strict.

## Q14

**Correct answer:** A, C

For every nonzero signed integer x, x/x=1, proving A. A dominating nonzero fact remains useful if x is unchanged, proving C. If x can be zero, replacement suppresses the invalid division, so B and D are false under the requirement to preserve the stated behavior. Algebraic identities have preconditions.

## Q15

**Correct answer:** 2

Two successful waits consume the initial two permits. The third thread blocks until a signal occurs, which has not yet happened. Therefore at most two enter. Atomicity of waits prevents multiple threads from consuming the same permit.

## Q16

**Correct answer:** A, C

y receives4 before x is replaced by9, so z=4+9=13. A and C are true. Ordinary value assignment does not alias variables, making B and D false. Propagation must respect which definition reaches each use.

## Q17

**Correct answer:** 8

The mean value theorem on[−1,3] gives f(3)−f(−1)=4f'(c)≥8. Equality is attained by f(x)=2x, which also satisfies f(0)=0. A lower bound alone would not establish the smallest possible value without this attaining example.

## Q18

**Correct answer:** 111

The effective starting address is100−12+20=108. A32-bit word occupies four bytes, ending at111. The index scale is applied before adding the displacement, and the last byte is three beyond the first.

## Q19

**Correct answer:** A, C

Alternation gives each simulation unbounded progress, so an acceptance by either is eventually observed: A,C are true. Both may run forever without acceptance, disproving B. The acceptance rule is either, not both, so it neither implements intersection nor guarantees a decision; D is false.

## Q20

**Correct answer:** 6

Shifting1011 yields0110 after discarding the outgoing1. Its sign bit is0, so its signed value is6. This wraps the original signed−5 rather than computing an exact unbounded multiplication by two.

## Q21

**Correct answer:** A, C

Both a and b are at level1; a discovers c at level2 before any level2 node can create a level3 discovery. b discovers d at level2. Thus A,C are true and B false. Other graphs can have several shortest predecessors and order-dependent parents, disproving D. BFS distance uniqueness does not imply parent uniqueness.

## Q22

**Correct answer:** 0.5

Conditioning on the red coin being heads leaves the independent blue coin equally likely heads or tails. Exactly one head requires blue tails, probability1/2. A report about a specified coin differs from the event “at least one head”.

## Q23

**Correct answer:** A, B, D

Meet and join in a subset lattice are intersection and union, giving{b} and{a,b,c}. Thus A,B are true. Neither set contains the other, so C is false. The empty set is contained in every subset, proving D. Lattice order is inclusion, not cardinality alone.

## Q24

**Correct answer:** 0

If b OR c is false, b=c=0. The two remaining conjuncts require a and NOT a simultaneously, impossible. No assignment qualifies. This is also the resolution implication from(a OR b) and(NOT a OR c) to(b OR c).

## Q25

**Correct answer:** A

An element is pushed onto I, transferred once to O and eventually popped; it is never returned to I. A is true. A transfer can take linear time in the current size, disproving B's worst-case claim. Reversal puts the oldest element on top, preserving FIFO and disproving C. Enqueue can push I regardless of O, so D is false. Amortized constant cost differs from per-operation worst-case cost.

## Q26

**Correct answer:** 4

All four parity pairs are reachable. For any two different pairs, append a suffix whose parities make the first pair(odd,odd); the second then fails at least one parity. All four states are distinguishable and necessary, and the parity-pair construction attains four.

## Q27

**Correct answer:** A, C

Linearity gives H(c+e)=Hc+He=He for a codeword c. Thus C is true. If e is a nonzero codeword, He=0 and the change is undetected, proving A and disproving B,D. A zero syndrome means code membership, not absence of error.

## Q28

**Correct answer:** -24

A unit lower triangular matrix has determinant1. The upper triangular determinant is2×(−3)×4=−24; multiplicativity gives det(A)=−24. No permutation sign is introduced because none is used.

## Q29

**Correct answer:** 2

The four minterms fix the first two variables to0 and allow all settings of the last two. One product of the complemented first two variables covers exactly the on-set and has two literals. Dropping either literal introduces off-set inputs, so fewer literals cannot suffice.

## Q30

**Correct answer:** 400

Worst-case return delay is twice20 microseconds, or40 microseconds. At10 bits per microsecond, the timing requirement is400 bits. This calculation uses only the supplied propagation model, not an additional standard-specific minimum frame size.

## Q31

**Correct answer:** 3

Integrating the identity gives integral(f(x))+integral(f(1−x))=6. Substitution u=1−x makes the two integrals equal, so each is3. No pointwise symmetry of f itself is required.

## Q32

**Correct answer:** A, C, D

The nullable foreign key permits NULL, proving A. A non-null value must match an existing id, proving D; its own id is a possible match, proving C. Mutual references between two existing rows also satisfy the foreign key, disproving B. Referential integrity does not impose an acyclic hierarchy.

## Q33

**Correct answer:** 3

Among R's children, A points to B and B to C: two sibling pointers. Among A's children, D points to E: one. C's sole child and last siblings have null right-sibling pointers. Total3. These pointers connect siblings, not parent-child pairs.

## Q34

**Correct answer:** B

A thread holding Y must already have acquired X, so two threads cannot split the locks in opposite acquisition orders. The common order excludes circular wait, proving B and disproving A. It gives neither equal waits nor absence of waiting, so C,D are false. Deadlock prevention is weaker than immediate access or fairness.

## Q35

**Correct answer:** 3

Only S→aSb introduces terminals, adding one a and one b per application. The target contains three of each, forcing exactly three applications. It is derivable by concatenating aabb and ab using SS, so the forced count is attainable. Extra SS and epsilon expansions cannot change the required terminal-producing count.


## Q36

**Correct answer:** 3

Before t=x, x and y are live. After it, y and t are live; after x=y, x and t are live. These three pairs form a triangle in the name-interference graph, requiring three fixed registers, which suffice. Peak simultaneous liveness is only two, but different pairs overlap at different points; the prohibition on splitting or rewriting matters.

## Q37

**Correct answer:** 1.36

Mean=(6+t)/5 and mean square=(14+t²)/5. Variance=(4t²−12t+34)/25. Its derivative(8t−12)/25 is positive for t≥3, so the minimum occurs at t=3 and is34/25=1.36. An unconstrained minimum at1.5 would violate the allowed range.

## Q38

**Correct answer:** 7

The unique minimum tree uses weights1,2,3 and totals6. The tree AB,BC,DA has weight7. Since all edge weights are integers, no spanning-tree weight lies strictly between6 and7, so7 is the next possible optimum. Constructing a tree attains the lower bound.

## Q39

**Correct answer:** A, C

A has matching dash positions and differs only in the third bit, producing0--1. C differs only in the last bit and produces-10-. B has different dash positions and cannot be combined by the stated rule. D differs in four positions. Adjacency is determined by fixed-bit differences, not visual proximity of the rows.

## Q40

**Correct answer:** A, C

A→D→C already implies AB→C, so deleting AB→C preserves the closure and A is true. Starting from C without C→B reaches no other attribute, so that dependency is not redundant and B is false. A determines D,C,B and is minimal as a singleton, making C true. D reaches C,B but not A, so D is false. Testing redundancy requires closure under the set with the tested dependency removed.
## Q41

**Correct answer:** A, C, D

A valid BST satisfies the local comparisons, so A is true. The stated tree passes those checks but puts12 in10's left subtree, violating the ancestor constraint; C is true and B false. Carrying the upper bound10 into the whole left subtree detects12, proving D. Parent-only checks omit inherited constraints.

## Q42

**Correct answer:** B

The first phase stores a prefix; the second must match its reverse, consuming one stack symbol per input symbol. A successful branch therefore divides an even-length palindrome equally. B is true. NPDA acceptance requires some successful branch, not every guess, disproving A. One stack is sufficient, disproving C. End-of-input remains mandatory, disproving D.

## Q43

**Correct answer:** 64

The low bit selects between2k and2k+1 for each six-bit upper address k. Thus there are2^6=64 disjoint pairs. Arbitrary unaligned consecutive addresses cannot be selected by changing only the low bit.

## Q44

**Correct answer:** 2

Addresses6,7 map to local row floor(address/4)=1; addresses8,9 map to row2. The banks are2,3,0,1, but only two distinct rows are involved. An unaligned word may cross a local-row boundary even when each byte maps to a different bank.

## Q45

**Correct answer:** B, C

An intervening write to the pointed-to object can change the repeated expression's value, proving C and disproving A. A valid no-modification proof restores availability and allows reuse, so B is true. Calls can have memory effects, making D false. Source-level repetition is insufficient without effect analysis.

## Q46

**Correct answer:** 3

B combines its link cost1 to A with A's stale distance2, adopting3. A's advertised route actually depended on the failed path through B, but ordinary distance-vector information does not reveal that dependency. This is the beginning of a count-to-infinity problem.

## Q47

**Correct answer:** A, C

Different source addresses make the supplied context keys different, proving A and disproving B. Once the context is identified, offset locates a payload piece within it, so C is true. Fragments may be interleaved and reordered; arrival order does not replace the supplied key, making D false. Identification values are not globally unique across senders.
## Q48

**Correct answer:** 86

Normalize original time to100 units. Memory stalls become40/2=20; other time becomes60×1.1=66. Total86 units, or86% of original time. Applying the10% slowdown to the entire workload would overstate the penalty.

## Q49

**Correct answer:** A, B, D

The /25 covers addresses128–255 and is more specific, so200 uses Y and100 uses X: A,B are true. Lookup is based on prefix length, not installation order, making C false. Removing the /25 leaves the matching /24 for200, proving D.

## Q50

**Correct answer:** A, B, C

Left cancellation makes x↦ax injective. On a finite set it is then surjective, proving A and giving b with ab=e, proving B. Now a(ba)=(ab)a=a=ae, so cancellation yields ba=e, proving C. On an infinite set an injective map need not be surjective; nonnegative integers under addition supply a cancellative monoid with noninvertible positive elements, disproving D.

## Q51

**Correct answer:** 3

A15-element binary heap is perfect with levels0–3. The new root value is below every other key, so it swaps down at every internal level and stops only at a leaf, after three swaps. The larger-child rule selects the path but does not change its length here.

## Q52

**Correct answer:** A, B, D

Regular and context-free languages are closed under homomorphism, including erasing homomorphisms, so A,B are true. Erasing all symbols turns every string into ε; a nonempty input language therefore maps to{ε}, proving D and providing a counterexample to C. Homomorphisms can discard the structure responsible for nonregularity.

## Q53

**Correct answer:** 2

The two exact occurrences of if become IF by tie priority. if2 and iff have longer identifier matches and become ID. Thus two ID tokens appear. Keyword priority applies only after longest-match selection, not to a prefix of a longer token.

## Q54

**Correct answer:** 23

P completes at2. After a switch Q runs from3 to7. After another switch R runs from8 to14. All arrive at0, so their turnaround times are2,7,14, summing23. Switching overhead contributes to subsequent completion times even when the burst ordering is fixed.

## Q55

**Correct answer:** 4

When high bits are equal, the low-bit comparison is correct. When a1=1,b1=0, the full comparison is true but the low comparison is false on three of four low-bit pairs. When a1=0,b1=1, the full comparison is false but the low comparison is true on one pair. Total3+1=4 disagreements. Higher significance dominates lower bits.

## Q56

**Correct answer:** 2

Each block holds4000/80=50 records, so the file has20 data blocks. Its20 sparse entries occupy320 bytes and fit in one index block. A successful lookup reads that block and one data block: two reads. Record count affects index size, but does not require scanning all data blocks.

## Q57

**Correct answer:** B, C

A distinguishing future sequence disproves equivalence, so B is true. Equivalent Moore states must have equal current outputs and equivalent successors for each input, proving C. Equal output now alone leaves future behavior unconstrained, making A false. Encodings are internal labels, not external observations, so D is false.

## Q58

**Correct answer:** 2

Entry(1,1) of A³ counts directed walks of length3 from1 back to1. They are1→2→4→1 and1→3→4→1, giving2. Matrix powers count walks of an exact length, not arbitrary reachability or only simple paths in general.

## Q59

**Correct answer:** 90

SSTF first serves45, distance5. From45 it chooses70 at distance25 rather than10 at35. It then moves60 to10. Total5+25+60=90. Re-evaluate distances from the new head position after each request.

## Q60

**Correct answer:** 3

After inserting4, the root leaf splits into[1,2] and[3,4], with root separator3. Inserting5 then6 splits the right leaf into[3,4] and[5,6], adding separator5. The leaves are[1,2],[3,4],[5,6]: three. Promoted B+ separator keys remain in the leaves under the stated convention.

## Q61

**Correct answer:** A, B, D

The |xy|≤p condition puts nonempty y entirely in the first p zeros, proving A. Removing it preserves all p ones but reduces zeros, proving B. This works for every possible allowed length of y, so C is false. The contradiction establishes nonregularity, proving D. The string is chosen before the decomposition but handles all legal decompositions.

## Q62

**Correct answer:** 4

An odd five-cycle requires three colours. Each of p and q is adjacent to every cycle vertex, so neither may use any of those three colours, establishing a four-colour lower bound. Give p and q the same fourth colour because they are nonadjacent; this attains four. The two universal-to-cycle vertices do not require distinct extra colours.
## Q63

**Correct answer:** 20

Among all5!=120 permutations, the six relative orders of1,2,3 occur equally often by relabelling those three elements. Exactly one is allowed, giving120/6=20. Equivalently choose their three positions in10 ways, fill them in increasing order, and arrange4,5 in two ways.

## Q64

**Correct answer:** 12668

Virtual5500 has page number5 and offset5500−5×1024=380. Replace the page number by frame12 and preserve the offset:12×1024+380=12668. Translation changes the frame portion, not the within-page displacement.

## Q65

**Correct answer:** A, B, D

Along a path from s to t, the potential terms telescope to h(s)−h(t), proving A and therefore B. On a cycle this difference is zero, proving D. Arbitrary potentials need not remove negative edges; h=0 preserves any originally negative edge, disproving C. Choosing feasible potentials is an additional step, separate from path-order preservation.

