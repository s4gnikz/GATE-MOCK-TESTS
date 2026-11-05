# Worked Solutions — Mock Test 072

## Q1

**Correct answer:** A, C

Signed implies archived, which implies not editable, proving A. An editable form exists and cannot be signed, proving C. Unsigned forms need not be editable: an unsigned archived form is consistent with all premises, refuting B. Nothing requires any signed form, so D is not entailed. Universal statements alone do not establish existence.

## Q2

**Correct answer:** 5

Concept: inverse folding. Immediately before the second fold, positions 2 and 4 both map to the puncture at 4. Undoing the first fold gives original positions 2,8 from folded position 2 and 4,6 from folded position 4. All four positions are distinct. Their mean is (2+4+6+8)/4=5. Each fold must be inverted across every layer actually present.

## Q3

**Correct answer:** A, C, D

F must precede each of I,A, and both must precede P, so F is first and P last(A,C). The middle events can be ordered I,A or A,I, giving exactly two possibilities(D). B holds only in the first order, not necessarily. A partial order specifies constraints rather than one uniquely determined narrative.

## Q4

**Correct answer:** 2.5

The red ball's position is uniform among1,2,3,4, and that position equals the stopping draw count. The mean is(1+2+3+4)/4=2.5. Sampling stops at the red ball but does not bias its initial random position.

## Q5

**Correct answer:** A, C
**Concept:** Contraposition and existential information.

Passed calibration implies installed, so not installed implies did not pass calibration (A). The second premise explicitly supplies C. B reverses the first implication; D adds an unsupported connection between testing and calibration.

**Common misconception:** “Did not pass” need not mean a test was taken and failed; it is the negation of passing.

## Q6

**Correct answer:** 4.5

BC is horizontal, so the altitude from A is x=0. Side AC has slope(0−8)/(6−0)=−4/3; the perpendicular altitude from B has slope3/4 and equation y=(3/4)(x+6). At x=0 it gives y=4.5. Altitudes are perpendicular to opposite sides and are not generally angle bisectors or medians.

## Q7

**Correct answer:** B, C

For a list of length n, final position i holds the negative of original entry n+1−i under either order, proving B for all entries and lengths. Reversal and negation each undo themselves, and they commute; applying the composition twice restores the input(C). One example does not prove a universal statement(A), and commutation does not mean either operation is the identity(D). The argument applies equally to repeated values and an empty list.

## Q8

**Correct answer:** 3.6
**Concept:** Expected payout.

Different colours occur with probability 2×(3/6)(3/5)=3/5. The payout is 6 on that event and zero otherwise, so expectation is 6×3/5=3.6.

**Common misconception:** The second draw uses a denominator of five, not six.

## Q9

**Correct answer:** -50

From a1 to a101 there are100 updates. Group them as(1−2)+(3−4)+...+(99−100). Each of50 pairs contributes−1, so a101=−50. There are100 increments, not101, because the initial term is already specified.

## Q10

**Correct answer:** 2

Each square has area16. An area28 union implies overlap32−28=4. The overlap is a square of side4−t, so(4−t)²=4. Because0≤t≤4, 4−t=2 and t=2. The other algebraic root lies outside the allowed displacement range.

## Q11

**Correct answer:** 52

**Concept:** Row-major indexing.

Two full rows contribute ten integers, followed by three integers within the final row. The offset is (2×5+3)×4=52 bytes.

**Common misconception:** Multiplying the row index by the number of rows rather than columns.

## Q12

**Correct answer:** 4

The empty word reaches(even,even), b reaches(odd,even), a reaches(odd,odd), and ab reaches(even,odd). All four states are therefore reachable. The two parities are not identical because b changes length without changing the a count.

## Q13

**Correct answer:** A, B, D

The writes are to x and y separately, so A holds. Together they leave0,0 and violate the invariant, proving B,D. In a serial order, the second transaction sees the first variable become0 and does not perform its conditional write, preserving the invariant; C is false. This is a write-skew pattern rather than a direct write collision.

## Q14

**Correct answer:** A, C

T2 reads T1's uncommitted write, so A is true; it commits before that writer aborts, proving C. Recoverability requires a reader to commit only after the writer it depends on commits, so B is false. Strictness disallows reading the uncommitted written value, refuting D. Commit order matters in addition to the read/write order.

## Q15

**Correct answer:** 1

Reachable nonterminals are S,A,B. A is productive through a. B has no terminating production: every derivation retains B, so neither B nor S is productive. C is productive but unreachable. Only A satisfies both conditions, giving1. Reachability and productivity are independent checks.

## Q16

**Correct answer:** 1

Concept: implicant dimension. Eight=2³ minterms vary over three of the four coordinates. One coordinate remains fixed and supplies the sole literal. A valid cube is necessary; an arbitrary collection of eight minterms need not simplify this way.

## Q17

**Correct answer:** A, C

Both a and b are at level1; a discovers c at level2 before any level2 node can create a level3 discovery. b discovers d at level2. Thus A,C are true and B false. Other graphs can have several shortest predecessors and order-dependent parents, disproving D. BFS distance uniqueness does not imply parent uniqueness.

## Q18

**Correct answer:** 60
**Concept:** Collision-detection round-trip bound.

The worst return time is twice 2.4 microseconds, or 4.8 microseconds. At 100×10⁶ bits/s, that duration transmits 480 bits. Dividing by eight gives 60 bytes. The question explicitly ignores other standard-specific minimum-frame rules.

**Common misconception:** Use round-trip propagation time, not just one-way propagation time.

## Q19

**Correct answer:** 2

Concept: hard links. Removing one directory entry decrements the number of links by one, from three to two. The other names still reference the same file. Removing one name does not necessarily delete the underlying file.

## Q20

**Correct answer:** 5

Arguments are19,9,4,2,1. There are five invocations, with the last returning without recursion. The count includes both endpoints of the call chain.

## Q21

**Correct answer:** 820

Concept: moments of an affine transformation. E[Z]=3·10−2=28 and Var(Z)=3²·4=36. Since E[Z²]=Var(Z)+(E[Z])², the answer is 36+784=820. Variance alone is not the second raw moment.

## Q22

**Correct answer:** 8

Parity equality is transitive, so composition gives no pairs outside R. Reflexivity supplies a witness for each existing pair, so R composed with R=R. There are two parity classes of size2, contributing2²+2²=8 pairs. Composition counts resulting ordered pairs, not how many witnesses each has.

## Q23

**Correct answer:** B

The stated token classes give identifier x, two separate minus operators and unsigned integer12. B is correct. A invents a signed integer token, C violates identifier boundaries, and D introduces an explicitly excluded operator. Unary-versus-binary classification is deferred to parsing.

## Q24

**Correct answer:** 0.5

There are 16 equally likely ordered pairs and 12 unequal ones. Six unequal pairs have minimum zero: (0,j),(j,0) for j=1,2,3. The conditional probability is 6/12. Equal backoffs, including (0,0), are excluded by the condition.

## Q25

**Correct answer:** 1024

The two high address bits decode to one of four chip enables. Each read selects one chip, while10 address bits distinguish1024 bytes. Product1×1024=1024. Parallel connection of address pins does not mean that all chips should drive the data bus simultaneously.

## Q26

**Correct answer:** A, B

A spanning tree must connect v, and e is its sole possible connection. Thus every spanning tree, including every minimum one, contains e. C is false because a mandatory bridge can have any weight. Removing e isolates v, refuting D. The bridge argument does not depend on distinct or positive weights.

## Q27

**Correct answer:** 0.25

Conditional on any allowed choice2,3 or4 by A, independent B matches that choice with probability1/4. Averaging the same probability over those three choices leaves1/4. Restricting A's choices does not restrict B's independent choices.

## Q28

**Correct answer:** 4

**Concept:** Element order in a multiplicative group.

Powers of 3 modulo 10 are 3,9,7,1. The first return to the identity is the fourth power, so the order is four.

**Common misconception:** Using the additive order instead of the multiplicative group operation.

## Q29

**Correct answer:** A, B

Concept: limits on dense subsets. Since |f(x)|=|x|, f tends to zero at zero and f(0)=0, proving A. For nonzero x, the difference quotient f(x)/x is 1 on rationals and −1 on irrationals; rational and irrational inputs occur arbitrarily close to zero, so this quotient has no limit and no derivative exists. B is true and D false. At one the rational and irrational limits are 1 and −1, so C is false. Continuity of the function does not force its difference quotient to converge.

## Q30

**Correct answer:** -1.5

**Concept:** Signed fixed-point scaling.

The unsigned pattern is 232; in eight-bit two's complement it means 232−256=−24. Four fractional bits scale this by 2⁻⁴, giving −24/16=−1.5.

**Common misconception:** Interpreting the raw bit pattern as unsigned before applying fractional scaling.

## Q31

**Correct answer:** A

The initial in matches the keyword and identifier patterns at equal length, so priority makes it a keyword. The dot is its own token. The entire inner is a five-letter identifier, longer than the keyword prefix in; longest match therefore selects the identifier. A is correct. B and D ignore keyword priority for the first token. C incorrectly lets keyword priority override a longer identifier match. Priority resolves ties only after maximal length is determined.

## Q32

**Correct answer:** A, C

The direct path costs 2, while s→b→a costs 5−4=1, proving A. Settling a at 2 before exploring b can prevent correction, proving C. The graph is acyclic, refuting B. Its shortest path to a has two edges despite an available one-edge path, refuting D. Negative edges, even without a negative cycle, invalidate the usual Dijkstra settling guarantee.

## Q33

**Correct answer:** 52

**Concept:** Variance of an independent linear combination.

Independence removes the covariance term, and the constant contributes no variance. Thus Var(2X−3Y+7)=2²×4+(−3)²×4=16+36=52.

**Common misconception:** Carrying the negative coefficient into variance without squaring it.

## Q34

**Correct answer:** 86
**Concept:** Endianness versus numeric bit shifts.

The loaded word is 0x78563412. Shifting right by 16 yields 0x00007856. The stored halfword 0x7856 places 0x56 at the lower address 102 and 0x78 at 103. Hexadecimal 56 equals 5×16+6=86.

**Common misconception:** Endianness determines byte order in memory, not which bits a numeric right shift discards.

## Q35

**Correct answer:** A, B

An open descriptor refers to the opened file object rather than repeatedly resolving its pathname. Thus R retains F(A), while the replaced directory entry sends a later open to G(B). C confuses the directory entry with the existing open-file reference. D is false because the open reference can keep F alive after its last name is removed. Atomic replacement affects pathname visibility, not the identity of already-open files.

## Q36

**Correct answer:** 5

**Concept:** Linear probing across tombstones.

The four inserted keys occupy slots 3,4,5,6. Deleting 17 makes slot 4 a tombstone. Search for 31 begins at 3 and inspects 3,4,5,6,0, stopping at never-used slot 0. The tombstone cannot terminate the search because colliding keys may lie beyond it. Five slots are inspected.

**Common misconception:** Treating a deleted slot as indistinguishable from a never-used slot during search.

## Q37

**Correct answer:** 2

Row stride is4+p words and must be even. With p=0, block indices of the first words are0,2,4,6, mapping to sets0,2,0,2, so it fails. The next permitted p is2; stride6 gives block indices0,3,6,9 and sets0,3,2,1, all distinct. Therefore minimum padding2 words. Padding changes mapping through block indices, not directly through byte or word offsets alone.

## Q38

**Correct answer:** A, B, D

The /25 covers addresses128–255 and is more specific, so200 uses Y and100 uses X: A,B are true. Lookup is based on prefix length, not installation order, making C false. Removing the /25 leaves the matching /24 for200, proving D.

## Q39

**Correct answer:** 178

Concept: matrix-chain optimization. The five parenthesizations have costs:

- ((AB)C)D: 100+80+120=300.
- (A(BC))D: 160+400+120=680.
- (AB)(CD): 100+48+30=178.
- A((BC)D): 160+240+150=550.
- A(B(CD)): 48+60+150=258.

Minimum is 178. Multiplication dimensions change with each intermediate result; multiplying the locally cheapest pair is not a general optimality proof.

## Q40

**Correct answer:** 4

One packet takes (1200/k+75)/1000 seconds per link. With a two-link pipeline, the last of k packets arrives after k+1 packet times. Minimizing (k+1)(1200/k+75) is equivalent to minimizing1200/k+75k. For positive real k, AM–GM gives a minimum when1200/k=75k, hence k=4. Four is an allowed divisor of1200, so it is also the integer optimum. Packet headers impose a cost on excessive segmentation.

## Q41

**Correct answer:** 8

The subtree rooted at2 contains2,4,5,6, four vertices. Vertex7 originally has depth2. After attaching2 below7, its depth changes from1 to3, an increase2; every descendant of2 increases by the same2. The other vertices do not move, so total increase is4·2=8. Reattaching a subtree changes all its descendant depths, not just its root's.

## Q42

**Correct answer:** 3

Before rotation,20 is depth0;10,30 depth1;25,40 depth2;22,27 depth3. After rotation,30 is depth0;20,40 depth1;10,25 depth2;22,27 depth3. Exactly25,22,27 retain their depths, giving3. The middle subtree moves from being30's left subtree to20's right, and the root shift compensates for that reassignment.

## Q43

**Correct answer:** 2

The retained ranges are.0–.63 and.128–.255, represented by10.1.0.0/26 and10.1.0.128/25. Thus two prefixes suffice. One prefix describes a single contiguous aligned range and cannot include both retained ranges while omitting the gap. Two is therefore minimal.

## Q44

**Correct answer:** A, B, D

The identity holds over integers and remains equal after reduction modulo2^w, proving A,B. Whether the rewrite helps depends on instruction costs and target code generation, proving D. Semantic reasoning must still respect the language and representation, so the broad permission in C is false. Equivalence and profitability are separate tests.

## Q45

**Correct answer:** A, C

Both items have value density2. Any feasible packing of total weight5 achieves the maximum value10, proving A. A whole four-unit item plus one unit from the other also attains it, proving C. The allocation2.5+2.5 has two partial items, refuting B, and many such allocations refute D. A greedy algorithm can produce an optimum with at most one partial item without that property holding for every optimum.

## Q46

**Correct answer:** 19

Concept: separated repeated parts. If there are k twos, there are 8−2k ones. Their gaps provide 9−2k possible positions for at most one two each. Counts for k=0,1,2,3 are C(9,0)=1, C(7,1)=7, C(5,2)=10, C(3,3)=1; k=4 is impossible without adjacency. Total=19. Equivalently use a_n=a_(n−1)+a_(n−3) with a0=1,a1=1,a2=2.

## Q47

**Correct answer:** 2

R's lexical parent is P, not its caller Q. Its static link therefore reaches P; P's static link reaches Main. Two links suffice. Dynamic links would instead follow R→Q→P→Main. Static scope follows declaration nesting rather than the calling sequence.

## Q48

**Correct answer:** 1

Near8 the spacing is2. The exact sum9 is a tie between8 and10, rounded to8 because its significand low bit is even. The first expression is therefore0. The value1−8=−7 is exactly representable with three significant bits, so the second expression becomes8−7=1 exactly. The absolute difference is1. Reassociation changes intermediate rounding.

## Q49

**Correct answer:** 4

Concept: quantum tradeoffs. Steady-state useful fraction is q/(q+1), at least 0.8 iff q≥4. The fifth process starts after four quanta and four switches, at 4(q+1), at most 20 iff q≤4. Thus q=4 is the only choice. Initial-response time and steady-state efficiency impose different inequalities.

## Q50

**Correct answer:** A, B

Q covers a superset of P's columns at lower cost. If a cover contains P but not Q, replacing P by Q preserves coverage and reduces cost; if it already contains Q, dropping P preserves coverage. Thus A,B hold. C ignores dominance, and D ignores the objective's cost comparison: a larger but more expensive row need not dominate.

## Q51

**Correct answer:** 12

The root's three distinct child subtrees can be ordered in3!=6 ways. Vertex a's two leaves can be ordered in2!=2 ways. Vertex b has only one child, contributing one choice. Distinct labels make these choices give distinct preorder strings, so6×2=12. Permutations within a subtree cannot interleave its preorder block with another subtree.

## Q52

**Correct answer:** 4

For f(x)=x³−3x, stationary points are±1. Checking those and endpoints±2 gives absolute value2 in all four cases; monotonicity between stationary points shows no larger value occurs. Alternatively f(x)=2 factors as(x−2)(x+1)²=0 and f(x)=−2 as(x+2)(x−1)²=0. The distinct maximizers are−2,−1,1,2, giving4. Count distinct locations rather than root multiplicities.

## Q53

**Correct answer:** A, C
**Concept:** Unequal-count context-free language.

Split L into i<j and i>j; a PDA can match counts with its stack and accept an unmatched excess on either side, so their union is context-free (A). Its complement within a*b* is exactly the equal-count language (C). If L were regular, subtracting it from regular a*b* would make that equal-count language regular, a contradiction, so B is false. ε has equal zero counts and is excluded (D false).

**Common misconception:** Context-free unequal-count languages need not be regular.

## Q54

**Correct answer:** 12

**Concept:** Relationship degree bounds and attainability.

Six employees with outdegree at most two give at most twelve pairs. Number them cyclically 0–5 and let each mentor the next two employees modulo six. This gives exactly two outgoing and two incoming pairs for every employee, with no self-pairs, attaining twelve.

**Common misconception:** Treating the minimum incoming-degree requirement as incompatible with the maximum outgoing-degree bound without checking a construction.

## Q55

**Correct answer:** 16

A rounds to16KiB at[0,16), B to16KiB at[16,32), and C to32KiB at[32,64). Freeing A releases its16KiB block. Its buddy is B's occupied block, so no coalescence is possible. The largest satisfiable request is16KiB. Total free capacity and largest contiguous buddy block are not interchangeable.

## Q56

**Correct answer:** 4

When high bits are equal, the low-bit comparison is correct. When a1=1,b1=0, the full comparison is true but the low comparison is false on three of four low-bit pairs. When a1=0,b1=1, the full comparison is false but the low comparison is true on one pair. Total3+1=4 disagreements. Higher significance dominates lower bits.

## Q57

**Correct answer:** 6

The first fork gives two processes. Each then forks, giving four, of which the two newly created children enter the conditional body and each fork once more. Total6. The condition is evaluated separately in each parent/child return path.

## Q58

**Correct answer:** A, B

For1≤k≤p, p²<p²+k≤p²+p<(p+1)² because the gap to the next square is2p+1. Pumping y twice therefore produces a nonsquare length for every legal decomposition. A and B are true. No particular k needs to be chosen, so C is false. The contradiction disproves regularity, making D false. The uniform inequality is what handles the pumping lemma's existential decomposition.

## Q59

**Correct answer:** A, C, D

Doubling w gives even length, proving A. abba is an even palindrome but its halves ab and ba differ, refuting B. abab=(ab)(ab) is not a palindrome, proving C. Reversing ww gives reverse(w)reverse(w), proving D. Repetition and reflection are different symmetries.

## Q60

**Correct answer:** 1.19

There are20×0.25=5 mispredictions, adding15 cycles to the baseline104. Total execution time is119 cycles and CPI=119/100=1.19. The ideal fill/drain cost is already included in104 and must neither be omitted nor added twice.

## Q61

**Correct answer:** 0.6667 (accepted range 0.66665–0.66675)

For bag A, P(first blue,second red)=(1/3)(2/2)=1/3. For bag B it is (2/3)(1/2)=1/3. Averaging gives joint probability1/3. By symmetry of draw positions, the second-red probability is (1/2)(2/3)+(1/2)(1/3)=1/2. The requested conditional probability is (1/3)/(1/2)=2/3, rounded to0.6667. Conditioning changes the bag mixture; one cannot simply average the two within-bag conditional probabilities with the original equal weights.

## Q62

**Correct answer:** A, B, D

A PDA can match the a and b blocks of L1 and then ignore the c count; similarly L2 matches b and c, proving A. Simultaneously satisfying both equalities forces all three counts equal, proving B. This intersection is the standard non-context-free three-equal-block language, disproving C. Context-free languages are closed under union, so D is true. Closure under union must not be confused with closure under intersection.

## Q63

**Correct answer:** 2

**Concept:** Relational division as a universal requirement.

A values 1 and 3 each pair with both x and y. Value 2 pairs only with x and fails the requirement. The division result has two tuples.

**Common misconception:** Counting any matching B value rather than requiring all values in S.

## Q64

**Correct answer:** A, C

Short-circuit semantics already skip f() in A,C, so replacing those expressions removes no executed side effect and preserves the constant result. In B,D, f() is evaluated first even though the final value is predetermined; replacing the whole expression would suppress its effects. Boolean algebra alone is insufficient for effectful expressions.

## Q65

**Correct answer:** A, B, C

The ideals are empty,{a},{b},{a,b},{a,b,c},{a,b,c,d}, so A is true. Unions and intersections of downward-closed sets remain downward-closed and are respectively least upper and greatest lower bounds, proving B,C. These set operations satisfy the distributive laws, refuting D. Incomparability in the underlying poset does not destroy distributivity of its ideal lattice.

