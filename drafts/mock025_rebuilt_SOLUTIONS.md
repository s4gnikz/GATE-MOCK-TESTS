# Worked Solutions — GATE CS 2027 Mock Test 025

## Q1

**Correct answer:** B

B explicitly compares one cost with the other cost, using “that” to refer to cost. A compares an activity's cost with a machine rather than its replacement cost; C lacks parallel grammatical structures; D is malformed. Parallel comparison makes the intended quantities unambiguous.

## Q2

**Correct answer:** 60

Let the initial volume be V. The removed ten litres contain6 litres of milk. The final milk volume is0.6V−6, and the final total remains V. A1:1 ratio requires0.6V−6=0.5V, so V=60. Water replacement restores volume but not milk.

## Q3

**Correct answer:** A, C

An existing auditor is a reviewer and therefore not an intern, proving A. The same containment/exclusion argument applies to all auditors, proving C. Non-interns need not be auditors, so B is not implied. Nothing requires interns to exist, so D is not implied. Existential information must be carried only through justified set inclusions.

## Q4

**Correct answer:** 1

Reflection exchanges coordinates. C becomes(1,0), then(2,−1); B becomes(0,2), then(1,1). The requested difference is2−1=1. Apply translation after reflection, as specified.

## Q5

**Correct answer:** C

The passage says intermediate passengers may wait longer, not that every one's total journey must increase. C overstates both universality and the total-time conclusion. A,B,D accurately reflect the location-specific and tentative nature of the findings. Distinguish waiting time from total journey time.

## Q6

**Correct answer:** 24

The mathematics books have one allowed relative order and create four gaps around/between them. Place the three literature books in three distinct gaps to prevent adjacency: choose(4,3)=4 choices of gaps, with3!=6 assignments of distinct literature books. Total24. The fixed order of mathematics books removes a factor3! that would otherwise occur.

## Q7

**Correct answer:** 5

Profits are30 in each year, but margins are30/120=25% and30/150=20%. The decrease is5 percentage points. Unchanged profit does not imply unchanged profit margin, and a percentage-point difference is not a relative percentage change.

## Q8

**Correct answer:** 32

The cut unfolds into a diamond with vertices(3,4),(4,3),(5,4),(4,5). Each side has length sqrt2, so its perimeter is4sqrt2 and its square is32. The fold boundaries become interior symmetry axes, not extra hole-boundary segments.

## Q9

**Correct answer:** B

The stated chain is closure < measurement < replacement < reopening. Measurement is forced between the two specified events, making B correct. A happens afterward, C is not mentioned, and D contradicts the explicit chain. Temporal precedence is transitive here.

## Q10

**Correct answer:** 0.4286 (accepted range 0.42855–0.42865)

There are4²−3²=7 ordered outcomes with maximum4. An even sum requires both entries even; among even values{2,4}, the pairs with at least one4 are(2,4),(4,2),(4,4), three outcomes. Conditional probability3/7≈0.4286. Do not count only unordered pairs because doubles and unequal pairs have different multiplicities.

## Q11

**Correct answer:** 18

For a binary tree, if L is the number of leaves and D the number of two-child nodes, edge counting gives D=L−1=7, independently of unary-node count. Add eight leaves, seven binary nodes and three unary nodes:18 vertices. Unary chains change total size without changing the leaf/binary-node identity.

## Q12

**Correct answer:** A, C

The sole common lower bound maximal under the order is0, and the least common upper bound is1, so A is true. Every pair has a meet and join, making C true. Incomparability of a,b disproves B, and1 disproves D. A lattice need not be a total order.

## Q13

**Correct answer:** -6

Taking determinants gives det(P)det(A)=det(L)det(U)=1×6. One row interchange has det(P)=−1, hence det(A)=−6. The permutation sign must be retained when reconstructing the determinant from pivoted factors.

## Q14

**Correct answer:** 1

COUNT(v) ignores NULLs. Group1 has count1 and fails the HAVING condition; group2 has count0 and passes. The query emits one group row. COUNT(*) would instead count the physical rows and behave differently.

## Q15

**Correct answer:** 1000

Each1100-bit packet occupies one millisecond and carries1000 payload bits. Hence payload throughput is1000 bits/ms. The link's raw rate includes headers and is not all useful payload.

## Q16

**Correct answer:** 0.3333 (accepted range 0.33325–0.33335)

F(x)=integral0^x 2t dt=x². Integrating again over[0,1] gives1/3, rounded0.3333. The outer integral is of the accumulated function F, not directly of f.

## Q17

**Correct answer:** A, B

The first computed x is overwritten before any read, so it is dead and removable under the no-side-effect assumptions: A,B. Only the second definition reaches return, disproving C. That reaching definition is needed, disproving D. A dead value is identified by uses, not merely by repeated assignment names.

## Q18

**Correct answer:** 4096

An address selecting one of256 words needs8 bits. Add eight independent control bits for16 per word. Total256×16=4096 bits. The word count and word width must both be included.

## Q19

**Correct answer:** 16384

Each chip stores2048 bytes. Eight chips total16384 bytes. Equivalently each parallel pair stores2048 two-byte words, or4096 bytes; four pairs give16384. Widening the data path increases capacity per selected row, not the number of local rows.

## Q20

**Correct answer:** 0.02

Main memory is reached only after an L1 miss and an L2 miss conditional on that event. Probability0.1×(1−0.8)=0.02. The conditional L2 hit fraction must not be subtracted directly from the unconditional L1 miss fraction.

## Q21

**Correct answer:** A, B

Correct mutex acquisition serializes the two regions, so no update is lost: A,B. Either thread may acquire first, disproving C. An unmatched unlock does not replace mutual exclusion and may itself be invalid, disproving D.

## Q22

**Correct answer:** A, C

Every equal-block string belongs to a*b*, but L is the standard nonregular equal-count language while R is regular. Thus A,C are true. This example disproves B; L is infinite, disproving D. Regular supersets may contain nonregular subsets.

## Q23

**Correct answer:** C

After fewer than n−1 inspections all returning1, at least two uninspected positions remain possible locations of0, each consistent with the rotation promise. Thus n−1 inspections can be necessary, and a linear scan suffices. C is correct; A,B are too small and D exceeds the tight bound. Duplicates can remove the information needed for logarithmic rotated-array search.

## Q24

**Correct answer:** B, C

The language makes each read an observable action, so eliminating one changes behavior even when values match: B,C. This disproves A. Observability imposes no requirement that consecutive values differ, making D false. Value equivalence alone does not establish effect equivalence.

## Q25

**Correct answer:** 3

Rotation makes10 the root,20 its right child, and15 the left child of20;30 remains20's right child. Searching30 visits10,20,30: three nodes. Rotation preserves inorder order but changes search depths.

## Q26

**Correct answer:** B

One A is free, so Q can obtain it, finish and release B; P then obtains B. B is correct and C,D false. With multiple instances, a resource-allocation cycle alone need not establish deadlock, disproving A.

## Q27

**Correct answer:** A, B, C

Each of A,B,C has a NULL component and is exempt from matching under the stated rule. D has two non-null components and cannot match an empty referenced table. Apply the supplied composite-key rule rather than treating each component as an independent foreign key.

## Q28

**Correct answer:** 1

States00,01,10 already belong to the cycle. The remaining state11 enters it at00 in one edge, so the maximum is1. Entry time differs from time to return to the initial state.

## Q29

**Correct answer:** 3

For p=1 or2, string a³ is long enough but every permitted nonempty pumped part has length1 or2; pumping down leaves a nonmultiple-of-three length. For p=3, every eligible string has at least three a's; choose y=a³, and every pump changes the length by a multiple of three. Thus3 is both necessary and sufficient.

## Q30

**Correct answer:** C

Scores are(6+3)/3=3, (8+4)/4=3 and(5+1)/1=6. R has the largest, so C is correct; P,Q do not win and D incorrectly equates all scores. Waiting time is normalized by service demand.

## Q31

**Correct answer:** 40

The transformed mean is10−2×4=2 and variance is(−2)²×9=36. Therefore E[Y²]=Var(Y)+(E[Y])²=36+4=40. Translation changes the mean but not variance; negative scaling still squares in the variance.

## Q32

**Correct answer:** 0

Every one-bit flip toggles total parity, including a flip of the parity bit itself. None of the five patterns passes the check. Detection is being asked, not localization or correction.

## Q33

**Correct answer:** A, C

The DFS tree path from an ancestor to the current vertex plus a back edge forms a directed cycle, proving A and C. An edge to a finished vertex can be a forward or cross edge without a cycle, so B is false. One local cycle does not imply all vertices mutually reach each other, disproving D.

## Q34

**Correct answer:** -0.75

An inverse y satisfies3*y=0, the identity. Thus3+y+3y=0, yielding y=−3/4=−0.75, which belongs to the domain. The operation is commutative, so it is also the left inverse. Multiplicative inverse under an unfamiliar group law need not be the reciprocal under ordinary multiplication.
## Q35

**Correct answer:** -1.5

The raw unsigned value is244, interpreted as signed244−256=−12. Three fractional bits scale by8, giving−12/8=−1.5. Determine signed integer value before applying the fixed-point scale.

## Q36

**Correct answer:** 1

Deleting e leaves six edges and retains connectivity on six vertices. A spanning tree needs five edges and exists in every connected graph, so one further appropriate edge removal suffices. Arbitrarily deleting a bridge would not be an appropriate choice.

## Q37

**Correct answer:** A, B, C

N behaves identically on every input. It accepts every string if the embedded simulation accepts, and no strings otherwise, proving A,B. An emptiness decider could therefore distinguish arbitrary acceptance by negating its result, proving C. Producing N requires only embedding the simulation instructions, not resolving their outcome, so D is false.

## Q38

**Correct answer:** B, C

If a spanning tree contained e, deleting e splits it into two components; the cycle contains another crossing edge with smaller weight, enabling a cheaper replacement. Hence no MST contains e, proving B and disproving A. The rest of the cycle provides a path around e, so C is true. When weights tie, replacing e need not reduce cost and e may belong to some MST, disproving D.

## Q39

**Correct answer:** 180

The first service reaches100 at time100 and cannot be diverted. It then moves80 cylinders to20, finishing at180. Arrival at time10 affects waiting time but does not preempt the in-progress movement.

## Q40

**Correct answer:** 4

With distinct keys, a maximum cannot have a child in a min-heap. Leaves are indices4,5,6,7, and the maximum can occupy any chosen leaf in a valid arrangement. Thus four positions are possible. Heap order constrains ancestors but not the ordering among leaves.

## Q41

**Correct answer:** A, B, D

At the first '<', longest match among the listed tokens is'<<', then the remaining'=' forms its own token. A,B,D are true. A lexer does not invent an unlisted token based on adjacency, so C is false.

## Q42

**Correct answer:** 4

A determines B and C. No dependency derives A from a set lacking it, so precisely the subsets containing A are superkeys: A,AB,AC,ABC. There are four. Only A is minimal and hence a candidate key.

## Q43

**Correct answer:** 3

Paths s→a→t and s→b→t cost6 and9. Path s→b→a→t costs1+1+2=4 and is uniquely best. It contains three edges. The fewest-edge path need not minimize weight.

## Q44

**Correct answer:** A, C

Different acceptance at the current state is distinguished by the empty suffix, proving A. If successors were distinguishable by suffix z, the original states would be distinguished by the leading symbol followed by z, proving C. One common transition is insufficient, so B is false. Unreachability from the designated start says nothing about the two states' future languages, making D false.

## Q45

**Correct answer:** 8

Usable block space is4096−16=4080 bytes, fitting34 records exactly. Seven blocks hold238 records, insufficient for250; eight suffice. Ceiling division is required because the last block may be partial.

## Q46

**Correct answer:** 12

The sum of degrees is3+3+2+2+2=12. Adjacency lists with both endpoints store exactly this many entries, corresponding to six undirected edges. Do not divide by two when counting stored neighbour entries.

## Q47

**Correct answer:** 0.0078125

The first retry collision probability is1/8; conditional on it, the independent second retry collides with probability1/16. Product1/128=0.0078125. The expanding choice range changes the second factor.

## Q48

**Correct answer:** B, C

A small addend can round away at a large magnitude, proving B. Subtracting nearby rounded quantities can expose their prior approximation errors, proving C. Rounding at intermediate operations can break associativity, making A false. Finite precision and exponent range cannot represent all arbitrarily large integers exactly, disproving D.

## Q49

**Correct answer:** 2

The reduction replaces three grammar-symbol entries with one, decreasing the count by two. State-stack entries in a particular LR implementation are not what this explicitly grammar-symbol count asks for.

## Q50

**Correct answer:** 5

Unused space inside the allocated partitions is8−7=1,12−10=2 and20−18=2 KiB, summing5. This is internal waste within allocated partitions, not separate free holes.

## Q51

**Correct answer:** A, C

After locating the lower bound, linked leaves permit ordered scanning, proving A and disproving B. Separator values can also appear among leaf keys, so C is true. The links still require a starting leaf to be located, disproving D. Search navigation and sequential continuation are complementary.

## Q52

**Correct answer:** 3

OR is false only when no bits are1. XOR is false for an even count of1s. They therefore differ exactly on assignments with two1s, of which choose(3,2)=3. The all-three-ones assignment makes both true.

## Q53

**Correct answer:** B

p−1=a+3 points to the last actual element and may be dereferenced. p itself is one-past, so A,D dereference outside the array. p+1 goes beyond even the permitted one-past pointer, making C invalid. Forming a boundary pointer does not authorize reading at it.

## Q54

**Correct answer:** 2

After hit A, recency order is B,C,A. D misses and evicts B, leaving C,A,D. B then misses and evicts C. Two misses occur. Hits update LRU order even though no data is loaded.

## Q55

**Correct answer:** 6

Different endpoint bits contribute exactly one1 and may be chosen in two orders. Exactly one more1 is placed in the three interior positions, giving three choices. Total2×3=6. The endpoint constraint fixes part of the total Hamming weight.

## Q56

**Correct answer:** A, C

The device's memory update need not replace a noncoherent CPU cache entry, so A is possible and C can be necessary. DMA completion does not supply the excluded coherence guarantee, disproving B. Physical sharing and coherence are distinct properties, making D false.

## Q57

**Correct answer:** 8

The candidate distances are2+7=9 via A and5+3=8 via B. The router selects8. A neighbour's advertisement must be combined with the link cost to that neighbour.

## Q58

**Correct answer:** 32

Values are a0=1,a1=1,a2=2,a3=4,a4=8,a5=16,a6=32. For n≥2, subtracting consecutive prefix-sum recurrences gives an=2a(n−1). The doubling begins after the exceptional initial pair.

## Q59

**Correct answer:** 78

The clock period is maximum stage delay5 plus overhead1, or6 ns. Four cycles produce the first result and nine more produce the next nine, totaling13 cycles. Time13×6=78 ns. Sum of unpipelined stage delays is not the pipeline clock period.

## Q60

**Correct answer:** 2

Global FIFO cycles four distinct pages through three frames; every reference faults, for eight. Under local allocation, P incurs its two initial faults and then hits, while Q alternates two pages in one frame and faults four times. Local total6, so global incurs two more. Protecting one process's working set can change the outcome despite identical total frame count.
## Q61

**Correct answer:** A, B

The fixed bits yield a NOT c; b,d are absent because all their combinations are covered. Thus A,B are true and C false. Specified zeros cannot be included in a valid exact SOP group, making D false.

## Q62

**Correct answer:** 4

Apply S→aS three times and then S→b once. Total four steps. Every recursive step adds exactly one leading a, so no shorter derivation can produce three a's.

## Q63

**Correct answer:** A, B, D

Subsequent fragment starts must be expressible in eight-byte offset units, so nonfinal payload lengths are multiples of eight: A. The final payload need not be padded to that boundary, proving B. The offset requires multiplication by eight, disproving C, and refers to original payload positions rather than counting each fragment's new header, proving D. Length and offset use different units.
## Q64

**Correct answer:** A, B, D

Implication transitivity gives p→r, proving A. Its contrapositive is NOT r→NOT p, proving B. The premises prohibit p true with r false, proving D. The converse r→p need not hold, so C is false. Implication chains do not reverse direction.

## Q65

**Correct answer:** 4

Balanced middle probing on15 keys forms four decision levels with capacities1,2,4,8. A deepest successful key requires four comparisons. Counting splits without the final equality test would undercount.


