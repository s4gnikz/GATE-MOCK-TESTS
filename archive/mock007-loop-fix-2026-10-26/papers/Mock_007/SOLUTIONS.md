# GATE CS 2027 — Mock 007: Worked Solutions

Exact and rounded NAT acceptance rules are in the paper's answer key.

## Q1

**Correct answer:** B  
**Concept:** Modifier attachment.

In B, “exhausted” directly modifies researchers. A attaches the introductory modifier to experiment, C explicitly describes the samples as exhausted, and D again modifies experiment. Only B conveys the required meaning.

**Common misconception:** A nearby adjective need not describe the intended actor unless the sentence attaches it clearly.

## Q2

**Correct answer:** 4  
**Concept:** Ratios at different times.

Write present ages as 4k,3k. Then 5(4k+8)=6(3k+8), so 2k=8 and k=4. The present ages are 16 and 12, whose difference is 4. Eight years later they are 24 and 20, confirming the ratio 6:5.

**Common misconception:** Equal additions to ages do not preserve their ratio.

## Q3

**Correct answer:** A, C  
**Concept:** Weighted means with positive weights.

The combined mean is a convex combination of 40,60,80 with all weights positive, so it lies strictly between 40 and 80 (A). Equal sizes give 60 (C). Sizes 2,1,1 give mean 55, refuting B and D.

**Common misconception:** An unweighted mean of group means is valid only with suitable group weights.

## Q4

**Correct answer:** 1  
**Concept:** Symmetries preserving labels or colours.

Any valid rotation must fix the unique red point (1,0). Among angles in [0,360), only the zero-degree rotation does this. The uncoloured set would have four rotational symmetries, but three do not preserve colour.

**Common misconception:** Geometric symmetry can be destroyed by a distinguishing mark.

## Q5

**Correct answer:** C  
**Concept:** Dependency ordering.

Locating the fault precedes restoring the backup; restoration precedes testing; successful testing precedes reopening. Thus R,P,Q,S is forced. A restores before diagnosis, B reopens before testing, and D tests before restoration.

**Common misconception:** A plausible narrative order still has to satisfy every explicit prerequisite.

## Q6

**Correct answer:** 24  
**Concept:** Adjacency exclusion.

Choose C's end seat in two ways. For each choice, the four remaining people have 4!=24 orders, of which 2×3!=12 place AB or BA together as a block. Therefore 2(24−12)=24 valid orders remain.

**Common misconception:** Exclude both internal orders of an adjacent pair.

## Q7

**Correct answer:** 25  
**Concept:** Successive percentage changes.

Normalize the original price to 100. The increased price is 120 and the target is 90. The reduction is 30/120×100=25%, measured against the increased price.

**Common misconception:** The two percentage changes use different bases.

## Q8

**Correct answer:** 0.25  
**Concept:** Conditional counting with parity.

Of C(6,2)=15 pairs, C(3,2)=3 are odd-odd and have odd product. Twelve pairs satisfy the condition. Within them, an even sum requires even-even, giving C(3,2)=3 favourable pairs. The probability is 3/12=1/4.

**Common misconception:** Odd-odd pairs have even sum but must be removed by the conditioning event.

## Q9

**Correct answer:** A, C  
**Concept:** Truth-value consistency.

If ON, the truth values are true,false,false: only one statement is true. If OFF, they are false,true,true: exactly two are true. Hence OFF is forced and B,C are truthful, proving A,C. B incorrectly includes A; D overlooks the consistent OFF assignment.

**Common misconception:** Evaluate a statement about another statement using the same candidate state.

## Q10

**Correct answer:** 2.25  
**Concept:** Order statistics without replacement.

For minimum k=1,…,6, the other two selected values can be chosen in C(8−k,2) ways. The expectation is [1×21+2×15+3×10+4×6+5×3+6×1]/C(8,3)=126/56=2.25. Alternatively, the four gaps before, between, and after the three selected ranks are exchangeable, yielding expected first rank (8+1)/(3+1).

**Common misconception:** The minimum is not uniform over its possible values.

## Q11

**Correct answer:** 11  
**Concept:** Reachability closure.

From either 1 or 2 every vertex is reachable, giving four pairs for each source. From 3, only 3 and 4 are reachable; from 4, only 4 is reachable. Reflexivity is included. The total is 4+4+2+1=11.

**Common misconception:** Reflexive transitive closure includes zero-length paths and does not add reverse reachability arbitrarily.

## Q12

**Correct answer:** C  
**Concept:** Lower and upper bounds with duplicate keys.

The first 4 is at index 4, while the first value greater than 4 is 7 at index 6. Thus C gives (4,6). A begins before any 4; B stops at the last equal value rather than after it; D starts at the second equal value.

**Common misconception:** Upper bound is the first strictly greater element, not the final matching element.

## Q13

**Correct answer:** A, B, D  
**Concept:** Finite cancellation monoids.

Left multiplication by a is injective by cancellation and hence onto on the finite set (A). Thus some b satisfies ab=e. Now a(ba)=(ab)a=a=ae; cancel a to get ba=e. Every element has a two-sided inverse, proving B and D. Noncommutative finite groups, such as the permutations of three elements under composition, refute C.

**Common misconception:** Finiteness is crucial when converting an injective self-map into a surjective one.

## Q14

**Correct answer:** -0.1667  
**Concept:** A third-order limit.

The expansion sin x=x−x³/6+O(x⁵) gives limit −1/6. Equivalently, apply l'Hôpital three times to obtain −cos x/6 at zero. Rounded to four places, the answer is −0.1667.

**Common misconception:** Keeping only the linear approximation sin x≈x discards the leading term needed by this quotient.

## Q15

**Correct answer:** 5  
**Concept:** Counting linear extensions of a DAG.

The valid orders are ABCD,ABDC,BACD,BADC,BDAC. To derive the list, if A is first then B must be second and C,D can follow in either order. If B is first, either A is next followed by C,D in either order, or D precedes A and then C. Total 2+3=5.

**Common misconception:** Vertices that have no edge between them can still be indirectly constrained by other vertices.

## Q16

**Correct answer:** B  
**Concept:** DFA state requirements.

Use two accepting states for having read even or odd length, plus a rejecting sink for a forbidden b in an even position. The parity states are distinguishable by suffix b: allowed after even length, forbidden after odd length. The sink is distinguished by ε. All three are reachable, so three are necessary and sufficient. A is too small; C,D are not minimal.

**Common misconception:** A condition on positions requires parity tracking even when both parity states can accept at input exhaustion.

## Q17

**Correct answer:** 4  
**Concept:** Exhaustive Boolean complement combinations.

For any x,y, the four argument pairs in the XOR are exactly 00,01,10,11 in some order. AND is 1 on exactly one of them. Therefore their XOR is always 1, on all four assignments.

**Common misconception:** Complementing both coordinates produces the full input table here, not four independent unknown values.

## Q18

**Correct answer:** 8  
**Concept:** VIPT index constraints.

A page has 12 offset bits, of which six address a byte within a cache line. At most six more can index sets, allowing 64 sets. The cache has 32768/64=512 lines, requiring at least 512/64=8 ways. Eight is a power of two and attains the bound.

**Common misconception:** The page offset must hold both the line-offset and set-index fields.

## Q19

**Correct answer:** C  
**Concept:** ON filtering in an outer join.

For L.id=1, only R's row (1,5) satisfies both ON predicates. For L.id=2, no row matches, so LEFT JOIN supplies a NULL-extended row. C is correct. A drops the preserved unmatched row; B ignores R.v>0; D overlooks the successful match.

**Common misconception:** A filter in ON can preserve an unmatched left row that the same filter in WHERE would remove.

## Q20

**Correct answer:** A, C  
**Concept:** Error-detection parity.

Each flipped bit toggles total parity. Any odd number of flips changes even to odd and is detected, proving A,C. Two flips restore the original parity, refuting B; the same counterexample refutes D.

**Common misconception:** A parity bit detects every odd-weight error, not every nonzero error.

## Q21

**Correct answer:** B  
**Concept:** Priority aging.

Waiting gradually improves a job's urgency, counteracting indefinite postponement by newly arriving high-priority jobs. This is B. It does not change mutex acquisition order (A), page allocation (C), or cache/DMA coherence (D).

**Common misconception:** Scheduling starvation and resource deadlock require different remedies.

## Q22

**Correct answer:** A, B  
**Concept:** Homomorphic images.

aⁿbⁿ has 2n symbols, each mapped to 0, so its image is 0²ⁿ (A). The expression (00)* recognizes the image, proving B. The original equal-count language remains nonregular, refuting C. Neither symbol is erased; each has a one-symbol image, refuting D.

**Common misconception:** A homomorphism can merge distinctions that made the original language nonregular.

## Q23

**Correct answer:** 1.2  
**Concept:** Conditioning independent Poisson counts on their sum.

The conditional distribution is Binomial(3,2/(2+3)). This follows directly by dividing P(X=k,Y=3−k) by P(X+Y=3), producing C(3,k)(2/5)^k(3/5)^(3−k). The conditional mean is 3×2/5=1.2.

**Common misconception:** Conditioning on the total changes X's Poisson distribution to a binomial distribution.

## Q24

**Correct answer:** 2  
**Concept:** In-order acceptance across sequence wraparound.

The first 15 is discarded; 14 is accepted, making 15 expected. The first 0 is discarded; then 15 is accepted, followed by 0 and 1. The next expected value is 2. Discarded frames do not remain buffered under the given rule.

**Common misconception:** This receiver cannot advance through a previously discarded out-of-order frame when a gap later closes.

## Q25

**Correct answer:** -5  
**Concept:** Polynomials of triangular matrices.

The matrix polynomial remains upper triangular, with diagonal values 1²−1−1=−1, 2²−2−1=1, and 3²−3−1=5. Its determinant is their product −5, independently of the entries above the diagonal.

**Common misconception:** The arbitrary upper entries do not affect a triangular matrix's determinant.

## Q26

**Correct answer:** 14336  
**Concept:** Expanding opcodes.

Of 256 eight-bit prefixes, 56 remain after assigning 200 two-register opcodes. Each unused prefix can extend through all 256 patterns in the remaining eight bits. The maximum is 56×256=14336 no-operand instructions, with no collision with assigned register-format prefixes.

**Common misconception:** The register fields become opcode bits only under unused leading prefixes.

## Q27

**Correct answer:** 0.000004  
**Concept:** Effective access time and unit conversion.

The additional fault cost is 10,000,000 ns. Require 200+p×10,000,000≤240. Thus p≤40/10,000,000=0.000004. The wording says additional delay, so the normal 200 ns is not replaced on faults.

**Common misconception:** Mixing milliseconds and nanoseconds can cause an error of a millionfold.

## Q28

**Correct answer:** A, B  
**Concept:** Heap-order ancestry.

The smallest key occupies the root. If the second-smallest were deeper than a root child, its parent would have to be smaller as well, introducing a second smaller key in addition to the root. Thus only indices 2 or 3 are possible, and either is achievable. C,D have an intervening parent and are impossible.

**Common misconception:** Heap order constrains ancestors, not the full left-to-right order of the array.

## Q29

**Correct answer:** B  
**Concept:** CHECK and SQL UNKNOWN.

A CHECK rejects FALSE, but accepts TRUE or UNKNOWN. Positive integers make x>0 TRUE; NULL makes it UNKNOWN. Zero and negative integers make it FALSE. Thus B is correct, A incorrectly rejects NULL, and C,D incorrectly admit FALSE cases.

**Common misconception:** A CHECK predicate alone is not a NOT NULL constraint.

## Q30

**Correct answer:** B  
**Concept:** Language of a left-recursive grammar.

Each recursive step appends either a or b to the right of the remaining A, and the terminating production replaces A by c. The result is c followed by any string over {a,b}, namely B. A,C place c at the wrong end; D unnecessarily forces alternating pairs.

**Common misconception:** Left recursion describes a derivation mechanism, not the position of the terminal base symbol in the final word.

## Q31

**Correct answer:** C  
**Concept:** Gray/binary conversion.

Decode by prefix XOR: b2=1,b1=1 XOR 0=1,b0=1 XOR 1=0, giving binary 110=6. The next integer is 111=7, whose Gray code is 100. C is correct. A is the decoded current binary word; B is next binary rather than Gray; D is neither conversion result.

**Common misconception:** Incrementing a Gray word as an ordinary binary number does not generally advance its decoded integer by one.

## Q32

**Correct answer:** B  
**Concept:** Integer promotion and unsigned conversion.

The addition is performed after integer promotion and is representable; assignment converts the result back modulo 256. Starting at an even value and adding two modulo 256 always leaves i even. It never becomes 255, and every even eight-bit value is less than 255. The loop is infinite (B). A,C wrongly claim termination; D mistakes conversion wraparound for signed overflow.

**Common misconception:** Promotion does not prevent wraparound when a representable sum is assigned back to a narrower unsigned type.

## Q33

**Correct answer:** A, C  
**Concept:** Aliasing and load reuse.

If p and q address different objects, the intervening store cannot alter *p, so u=t is valid (A). If they alias and the original value is 3, the first load gives t=3, the store writes 7, and the second load gives u=7 (C). That case refutes B and D.

**Common misconception:** Different pointer variable names do not prove distinct target objects.

## Q34

**Correct answer:** 16  
**Concept:** Bank conflicts and service timing.

All four addresses map to bank 0. The starts are therefore at times 0,4,8,12, despite the global one-request-per-cycle capacity. Results arrive four cycles after each start, so the last arrives at 16.

**Common misconception:** Multiple banks help only when the access pattern distributes requests across them.

## Q35

**Correct answer:** B  
**Concept:** Descriptor inheritance and exec flags.

The child inherits the descriptor and its close-on-exec flag. Its successful exec closes that descriptor in the child. The parent has a separate descriptor table and neither execs nor closes it, so its descriptor remains open. B is correct; A incorrectly propagates the close, C invents a fork restriction, and D ignores the flag.

**Common misconception:** Sharing an open file description does not make descriptor-table close operations global to all processes.

## Q36

**Correct answer:** B  
**Concept:** A recurrence with dominant nonrecursive work.

Let f(n)=n²/log₂n. Relative to f(n), the next recursion level contributes 3f(n/2)/f(n)=(3/4)log₂n/(log₂n−1), which is bounded below one for all sufficiently large n. The levels therefore sum geometrically to Θ(f(n)); the finite last levels and leaf cost n^(log₂3) are lower order. B follows. A drops the denominator; C treats the leaves as dominant; D applies a boundary-case logarithmic accumulation that does not occur.

**Common misconception:** A logarithmic divisor does not automatically put a recurrence into the critical Master-theorem case.

## Q37

**Correct answer:** A, C  
**Concept:** Stack permutations.

A is produced by pushing 1,2,3, popping all three, then pushing 4,5 and popping both. C is produced by push 1,2/pop 2; push 3,4/pop 4,3; push 5/pop 5,1. In B, after popping 3 the top is 2, blocking 1. In D, after popping 4 the top is 3, blocking 2. Thus A,C are possible and B,D are not.

**Common misconception:** Unread input cannot remove an already stacked obstruction to the next requested output.

## Q38

**Correct answer:** 25.5  
**Concept:** Additive expected delays.

Every reference pays 1+2 ns for the lookups. Expected walk penalty is 0.10×200=20 ns, and expected data-miss penalty is 0.05×50=2.5 ns. Total 25.5 ns. Independence between the two miss events is unnecessary for summing their expected additive costs.

**Common misconception:** A conditional lookup sequence does not mean the always-performed data lookup should be weighted only by TLB misses.

## Q39

**Correct answer:** 16  
**Concept:** Exact arithmetic ranges before choosing a representation.

An eight-bit signed product ranges from −128×127=−16256 to (−128)²=16384. Independent products make the difference range −32640 through 32640. Fifteen signed bits cover only −16384 through 16383; sixteen cover −32768 through 32767. Therefore sixteen are necessary and sufficient, despite the generic rule that subtracting arbitrary sixteen-bit values might need seventeen.

**Common misconception:** Intermediate bit widths alone can overestimate the attainable range when products occupy only part of that representation.

## Q40

**Correct answer:** A, C, D  
**Concept:** Euler degree conditions and bipartite alternation.

The graph is connected, with two degree-3 vertices and three degree-2 vertices. Exactly two odd vertices yield an Euler trail (A), but no Euler circuit (B false). A path can alternate between sides of sizes three and two, beginning and ending in the larger side, so C holds. A cycle would need equal numbers from both parts, impossible when it visits all five vertices, proving D.

**Common misconception:** Euler conditions concern edge use and degrees; Hamiltonian conditions concern visiting vertices.

## Q41

**Correct answer:** 12  
**Concept:** Cardinality bounds from functional dependencies.

For each fixed A, AB→C permits at most one C per each of four B values, bounding the total by 3×4=12. AC→B requires those C choices to be distinct for a fixed A; five C values are available, so four distinct choices are possible. Use the same injective assignment from four B values to four C values for each A to attain twelve tuples.

**Common misconception:** A dependency-based upper bound must also be checked for compatibility with the other dependencies.

## Q42

**Correct answer:** 1.5  
**Concept:** CPU/I/O overlap and ready-queue waiting.

A runs from 0 to 2, then performs I/O from 2 to 5. B runs from 2 to 6. A waits from 5 to 6 and completes its final CPU burst from 6 to 8. A's ready waiting is 1 and B's is 2, averaging 1.5. I/O time is not ready-queue waiting.

**Common misconception:** A blocked process and a ready process contribute differently to waiting-time calculations.

## Q43

**Correct answer:** C  
**Concept:** Timestamp ordering in wait-die.

T1 is older than the holder T2, so it waits for x. T2 is older than holder T3, so it waits for y. T3 is younger than holder T1, so it aborts when requesting z. Only C matches. A,B reverse the requester/holder age test; D ignores the final younger-on-older request.

**Common misconception:** Under wait-die, the younger requester aborts; this differs from policies in which an older requester aborts a younger holder.

## Q44

**Correct answer:** 35  
**Concept:** Microinstruction field widths.

There are 16 control bits, log₂8=3 condition-selection bits, and two log₂256=8-bit addresses. Total width is 16+3+8+8=35. Both outcomes have explicit address fields, so no fall-through address saving applies.

**Common misconception:** Encoding one branch condition does not also encode its target addresses.

## Q45

**Correct answer:** 0.375  
**Concept:** Conditional permutations and derangements.

There are 5!−4!=96 permutations in which 1 is not fixed. For exactly one fixed point, choose it from the other four elements, then derange the remaining four: !4=4!(1−1+1/2!−1/3!+1/4!)=9. Favourable count is 4×9=36. Conditional probability is 36/96=0.375.

**Common misconception:** After choosing the sole fixed point, every remaining element—including 1—must be deranged.

## Q46

**Correct answer:** 0.5  
**Concept:** A minimax lower bound and construction.

Let M=max|p(x)|. The identity p(−1)+p(1)−2p(0)=2 holds for every monic quadratic. By the triangle inequality, 2≤|p(−1)|+|p(1)|+2|p(0)|≤4M, so M≥1/2. The polynomial x²−1/2 stays in [−1/2,1/2] on the interval and attains the bound. Thus the minimum is 0.5.

**Common misconception:** Optimizing only at a stationary point does not by itself bound the maximum over the whole interval.

## Q47

**Correct answer:** A  
**Concept:** Pointer updates and reachability.

t first saves node 3. Then node 2 points to node 5, and node 4 points to node 3. Node 3 still points to node 4, so those two form a separate cycle, but it is unreachable from node 1. The traversal from the specified head is 1,2,5,NULL. A is correct; B,C assume a different splice, and D confuses an unreachable cycle with the head's traversal.

**Common misconception:** A cycle elsewhere in the allocated nodes need not be reachable from the list head.

## Q48

**Correct answer:** 7  
**Concept:** Resource-constrained instruction scheduling.

Run P on the multiplier during 0–3 and Q during 3–6. Compute R on the adder during 3–4, overlapping Q. Then S runs during 6–7. The multiplier's two operations require six cycles total, and S must follow the completion of both products through its dependencies, so finishing before seven is impossible. Seven is attained.

**Common misconception:** Parallel functional units permit overlap, but a final dependent operation still supplies a lower bound after the bottleneck resource finishes.

## Q49

**Correct answer:** 188  
**Concept:** C-SCAN movement including wraparound.

From 40 the head moves upward to 99, servicing 50 and 90: 59 cylinders. The jump to 0 costs 99. It then reaches 10 and 30, adding 30. Total 59+99+30=188. The question explicitly counts the jump and uses C-SCAN rather than C-LOOK.

**Common misconception:** Different circular-scan variants differ in whether they travel to the physical endpoints.

## Q50

**Correct answer:** 520  
**Concept:** MTU budgeting across headers.

Each packet can carry 1280−20−20=1240 application bytes. Two full packets carry 2480 bytes, leaving 3000−2480=520 for the final packet. Headers are outside that requested payload size.

**Common misconception:** TCP payload and total IPv4 packet size are not interchangeable.

## Q51

**Correct answer:** A, B  
**Concept:** Reachability of and from negative cycles.

The reachable a→b→a cycle has weight −1; it can be repeated arbitrarily before continuing from b to c, so s-to-c walk weights are unbounded below (A). No edge from that component reaches t; the only s-to-t route has weight 5 (B). Thus C is false. c has no outgoing edges and cannot reach the cycle, refuting D.

**Common misconception:** A negative cycle affects destinations reachable from it, not every reachable vertex indiscriminately.

## Q52

**Correct answer:** C  
**Concept:** Tail-call position.

In C, argument evaluation acc*n happens before the call, and the returned value is passed straight to the caller with no subsequent work. In A and B the caller must still add or multiply after f returns. In D, g must be called after f returns, so f is not the tail call being considered. Only C satisfies the stated eligibility condition for its recursive call.

**Common misconception:** An expression occurring after the word return is not necessarily a tail call.

## Q53

**Correct answer:** 1.5  
**Concept:** Optimal BST comparison cost.

With b at the root, cost is 0.5×1+(0.2+0.3)×2=1.5. With a at the root, the best right subtree puts b above c, costing 0.2+2×0.5+3×0.3=2.1. With c at the root, the best left subtree puts b above a, costing 0.3+2×0.5+3×0.2=1.9. The remaining shapes are worse within those root choices, so 1.5 is optimal.

**Common misconception:** Minimizing height alone does not account for nonuniform search probabilities.

## Q54

**Correct answer:** 9233  
**Concept:** Two-level address translation.

The virtual page number is 35=2×16+3, giving root index 2 and leaf index 3. The mapping supplies physical frame 9, while the byte offset stays 17. Physical address is 9×1024+17=9233.

**Common misconception:** Translation changes the page/frame number, not the offset within the page.

## Q55

**Correct answer:** B  
**Concept:** Cumulative acknowledgments with reordering.

Until bytes 1000–1099 arrive, byte 1000 remains the first missing byte, so each of the first three ACKs is 1000. Once that segment arrives, buffered data make all bytes through 1399 contiguous, so the ACK advances to 1400. B matches; A,C,D incorrectly acknowledge across a gap or ignore buffered data.

**Common misconception:** Duplicate ACKs can result from reordering without actual packet loss.

## Q56

**Correct answer:** A, B, D  
**Concept:** Context-free closure with regular languages.

Intersecting a CFL with a regular language preserves context-freeness (A). L minus R equals L∩complement(R), and a regular complement is regular, proving B. Union with R, itself a CFL, preserves context-freeness (D). C is not guaranteed: choose R=Σ* and a CFL L whose complement is not context-free, such as the complement of {aⁿbⁿcⁿ} over {a,b,c}; that L is context-free by separating incorrectly ordered strings and unequal adjacent block counts. Then R minus L is the non-CFL equal-three-count language.

**Common misconception:** Set difference is not symmetric; complementing the regular operand is safe, complementing an arbitrary CFL is not.

## Q57

**Correct answer:** 18  
**Concept:** Conflict resolution and associativity.

After seeing 20−5 with another minus ahead, shifting postpones reduction. The parser forms the right subtree 5−3 first, yielding 20−(5−3)=18. Reducing instead would give left association and value 12.

**Common misconception:** Associativity comes from parser rules or conflict policy, not from the visual order of operators alone.

## Q58

**Correct answer:** 31  
**Concept:** Representation storage crossover.

The matrix uses 64²=4096 bits. Lists use 64×32+2m×32=2048+64m bits. Strictly less requires m<32; the largest integer is 31. Counting one entry per undirected edge would miss its two stored directions.

**Common misconception:** Equality at the crossover does not satisfy a strict storage-saving requirement.

## Q59

**Correct answer:** B  
**Concept:** Runs versus accepted strings.

An accepting run must eventually take q→r on the sole symbol a. Before doing so it may traverse the ε-cycle any finite number of times. Thus only a is accepted, but it has infinitely many finite accepting runs (B). A confuses runs with words; C never reaches final r without reading a; D incorrectly treats nondeterminism as forcing an infinite cycle.

**Common misconception:** Nondeterministic acceptance needs one finite accepting run; nonaccepting infinite alternatives do not prevent it.

## Q60

**Correct answer:** 6  
**Concept:** Isolated on-set minterms.

There are C(4,2)=6 on-set minterms. Flipping any one bit changes Hamming weight to one or three, both off-set. Therefore no implicant can omit even one literal without covering a forbidden neighbour. Each product term covers just one on-set minterm, so exactly six terms are necessary and sufficient.

**Common misconception:** A visually symmetric function need not have a compact two-level SOP representation.

## Q61

**Correct answer:** 11.273  
**Concept:** First-step equations with a periodic environment.

Let A,B be expected additional tosses with no trailing head and the next toss odd/even, respectively; let C,D be the corresponding expectations with one trailing head. Then A=1+(D+B)/2, B=1+C/4+3A/4, C=1+B/2, D=1+3A/4. Substitution gives 5A−4B=12 and 7B−6A=10. Solving yields A=124/11=11.272727… . The experiment starts in state A, so the answer rounds to 11.273.

**Common misconception:** The trailing-symbol state alone is insufficient when the next toss probability depends on parity.

## Q62

**Correct answer:** 14  
**Concept:** Normal and subnormal value ranges.

The largest finite value uses exponent 10 (E=2) and fraction .11: 1.75×2=3.5. The smallest positive value is subnormal exponent 00 and fraction .01: 0.25×1=0.25. Their ratio is 3.5/0.25=14.

**Common misconception:** Subnormal values do not include the implicit leading 1 of normalized values.

## Q63

**Correct answer:** A, C, D  
**Concept:** Universal SQL comparisons and UNKNOWN.

ALL over an empty relation is TRUE, so all T rows pass initially (A), refuting B. With one NULL, every comparison is UNKNOWN, so no WHERE row passes (C). With one value 2, the condition is simply x>2, satisfied only by 3 (D).

**Common misconception:** Empty-set universal truth differs from an UNKNOWN comparison against a NULL value.

## Q64

**Correct answer:** A, C  
**Concept:** Recognizer scheduling for union and intersection.

For union, dovetailing eventually discovers an acceptance from either recognizer, proving A. Sequential execution in B can loop forever on the first machine even when the second would accept. For intersection, members make both sequential recognitions accept; nonmembers never make both accept, so C is a valid recognizer even if it sometimes loops. D can accept a member whose recognizing computation takes more than one million steps, so it is invalid.

**Common misconception:** A strategy unsuitable for union may still be suitable for intersection because the required acceptance conditions differ.

## Q65

**Correct answer:** A, B, D  
**Concept:** A decreasing distance as a loop-prevention invariant.

With w(v,u)>0, d(u)=d(v)−w(v,u)<d(v), proving D; strict decrease around a directed cycle is impossible, proving A. With a zero-cost A–B link and unit-cost links from both A and B to t, both distances are 1. Each may choose the other as an equal-cost next hop, producing a cycle despite exact distances (B). This example refutes C.

**Common misconception:** Nonnegative costs suffice for shortest-distance algorithms, but strict decrease of chosen forwarding distances needs positive costs or an additional tie rule.

