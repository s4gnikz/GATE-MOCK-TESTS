# Worked Solutions — Mock Test 033

## Q1

**Correct answer:** B

“Had the survey included” is inversion of a past counterfactual condition. Its unreal past consequence is “would have been,” B. A uses an incompatible future perfect; C describes an awkward progressive state rather than the completed past consequence; D does not supply the required conditional consequence.

## Q2

**Correct answer:** 9.375

With old marked price 100, the old selling price is 80. The new marked price is125 and its selling price is 0.7×125=87.5. The relative increase is (7.5/80)×100=9.375%. The change in discount percentage is not itself the change in selling price.

## Q3

**Correct answer:** A, C

K being coordinator implies L available. Since L is unavailable, K cannot coordinate (A). Exactly one of L,M must therefore coordinate (C). Either may do so; being unavailable was not stated to prohibit coordinating, so B is not forced. If L coordinates, M need not, and N's availability is unconstrained, so D is not forced. Do not add an unstated availability requirement.

## Q4

**Correct answer:** B

The combined map is (x,y)→(y+2,x−1). Matching (5,3) gives y=3,x=4, so B. A maps to (6,2), C to (3,5), and D to (8,0). Reversing a composition requires undoing the translation before the reflection.

## Q5

**Correct answer:** C

The stated rise in evening visits and fall in morning visits establish a timing redistribution, C. Aggregate counts do not identify visitors, so A,B are not supported. Unchanged total visits do not rule out convenience or other benefits, so D is not supported. Visits and distinct users are different quantities.

## Q6

**Correct answer:** 6

Choose the two students who receive their own first-choice projects in C(4,2)=6 ways. The remaining two must exchange their first choices; leaving either correct would also leave the other correct. Each chosen pair therefore gives exactly one assignment, for six total. “Exactly two” rules out the identity permutation.

## Q7

**Correct answer:** 2.5

Initially successes are 80+95=175 out of 200, or87.5%. Later they are160+95=255 out of300, or85%. The decrease is2.5 percentage points. The regional rates are unchanged; changing their weights changes the combined rate.

## Q8

**Correct answer:** 12

The cut reaches x=4, so undoing that fold joins the two mirrored half-cuts into one rectangle of width2 and height1. Undoing the y=3 fold produces a second disjoint rectangle, at y from4 to5. Each hole has perimeter2(2+1)=6, for total12. The shared crease is not an internal hole boundary after unfolding; summing four separate unit-square perimeters would count it twice.
## Q9

**Correct answer:** A

Inspection immediately follows calibration, and release lies after inspection but before trial. This forces C,I,R,T, optionA. B breaks immediacy; C reverses calibration and inspection; D places release after trial. Each condition must hold in the same ordering.

## Q10

**Correct answer:** 0.4444 (accepted range 0.44435–0.44445)

Of C(4,2)=6 equally likely ball pairs, two are monochromatic, so P(record1)=1/3 and P(record0)=2/3. Independent repetitions differ in either order, giving2×(1/3)(2/3)=4/9≈0.4444. Restoring the bag makes the repetitions independent despite dependence within each draw pair.

## Q11

**Correct answer:** A, C, D

Each column is covered by two rows, so no implicant is essential (A). One row covers only two columns, requiring at least two rows. Both {P,R} and {Q,S} cover all four, proving C,D and disproving B. A row in one minimum cover is not necessarily present in every minimum cover.

## Q12

**Correct answer:** 13

There are24 child-pointer positions at12 non-null vertices. Exactly11 point to other vertices because a tree has11 edges. The remaining24−11=13 are null, each producing one null call. Counting only missing leaves would miss null child pointers at one-child vertices.

## Q13

**Correct answer:** 18

The first parenthesized expression has inner value2+3=5, doubled to10. The second has inner value4, doubled to8. Their outer sum is18. Parentheses have an explicit semantic action here; treating them as ordinary grouping alone gives the wrong result.

## Q14

**Correct answer:** C

Negating the universal yields an existential counterexample x. The implication fails when P(x) holds and its consequent ∃yR(x,y) fails; the latter negates to ∀y¬R(x,y). This is C. A retains a universal x; B negates the antecedent incorrectly; D requires only one failed witness instead of absence of every witness.

## Q15

**Correct answer:** 48

A row swap negates the determinant to−2; column scaling by−3 changes it to6. Multiplying a3×3 matrix by2 multiplies its determinant by2³=8. Hence det(2B)=48. Scalar multiplication affects all three rows, not just one.

## Q16

**Correct answer:** 4

The probe cycle length is12/gcd(12,s), so all12 slots are reached iff gcd(12,s)=1. The valid strides are1,5,7,11, four choices. A nonzero stride alone does not guarantee full coverage.

## Q17

**Correct answer:** A, B, D

A is a valid implication: the union of two finite sets would be finite. Its antecedent cannot actually hold here because {a,b}* is infinite. B follows from regular complement closure and regular languages being context-free. D follows because finite languages are regular. C fails for nonregular context-free languages: if their complement were regular, complement closure would make the original regular too. A statement can be necessarily true because its premise is impossible.

## Q18

**Correct answer:** B

Static links implement lexical scope, so R refers to its lexical parent P. Dynamic links implement return/unwinding along actual calls, so R's caller Q is identified. Thus B; A confuses lexical and dynamic parents, C swaps them, and D ignores the actual caller. Sibling procedures share a lexical parent without calling through it.

## Q19

**Correct answer:** 5

The cycle is1→3→9→5→4→1. For example9 maps to(9 mod4)×3+floor(9/4)=3+2=5. Five distinct indices participate. This permutation tracks moved storage positions, not five repeated transposes of changing array dimensions; the same explicitly given mapping is used every time.

## Q20

**Correct answer:** A, C

The outputs encode the count of true inputs: s is its low bit and k its high bit, proving A. Complementing three inputs changes count m to3−m, complementing both bits, proving C. k is1 for counts2 and3, so B is false. Several triples share a count, so D is false. These are full-adder outputs, not an injective code for the input triple.

## Q21

**Correct answer:** D

For all n≥1, n≤f(n)≤n². Along odd n, f(n)/n=n grows unbounded, excluding Theta(n). Along even n, f(n)/n²=1/n tends to zero, excluding Omega(n²) and Theta(n²). Thus only D holds. Asymptotic bounds must hold for every sufficiently large input, not only a subsequence.

## Q22

**Correct answer:** A, D

The nullable declaration permits A. A non-NULL foreign-key value must match its referenced key when checked, giving D. Neither self-reference nor cyclic reference violates these key constraints, so B,C are false. A foreign key enforces existence, not a tree structure.

## Q23

**Correct answer:** 0

The derivative at zero is the limit of [f(h)−f(0)]/h=h sin(1/h). Its absolute value is at most|h|, tending to zero. Thus f'(0)=0. Substituting zero into the expression for f'(x) valid only at nonzero x is not justified.

## Q24

**Correct answer:** B

Reclaiming a resource removes the no-preemption condition and can let one process finish, breaking the circular wait execution. Priorities, an unrelated ready process, and CPU speed do not release either held resource, so A,C,D do not resolve this resource cycle. Scheduling progress elsewhere is not resolution of the deadlocked pair.

## Q25

**Correct answer:** 1

The first edge recovers111→000. Six more edges advance six times modulo5, ending at001, value1. Directly treating111 as a modulo5 numeric state ignores the explicit illegal-state recovery transition.

## Q26

**Correct answer:** 7

The pumped block consists only of a's and its length k is1,2,or3. Pumping with exponent i changes the a-count to3+(i−1)k. Equating this to9 gives i=1+6/k, respectively7,4,3. The largest required exponent is7. The exponent may depend on the decomposition; one need not use the same exponent for every legal block. This finite instance illustrates the pumping contradiction mechanism rather than constituting a full proof for every pumping length.
## Q27

**Correct answer:** D

accept returns a separate connected socket, while the listening socket can keep accepting, D. A incorrectly replaces the listening endpoint; B confuses accepting with application data transmission; C wrongly couples the descriptors' lifetimes. Closing a connected endpoint does not inherently close the listener.

## Q28

**Correct answer:** 3

Compute t=a+b, u=t*t, and result=u+t. These are three arithmetic instructions. Each of the distinct operations represented in the common-subexpression DAG is needed under the given restrictions. Repeated textual occurrences of a+b share one computed value.

## Q29

**Correct answer:** 6.8

Y²=X4, with values16,1,0,1,16. Their equally weighted average is34/5=6.8. Squaring E[Y] would not compute E[Y²]; expectation does not commute with squaring.

## Q30

**Correct answer:** 8

Parity equality is transitive, so composition gives no pairs outside R. Reflexivity supplies a witness for each existing pair, so R composed with R=R. There are two parity classes of size2, contributing2²+2²=8 pairs. Composition counts resulting ordered pairs, not how many witnesses each has.

## Q31

**Correct answer:** A, C

A usable cached or otherwise known address can avoid a fresh lookup, A. The redirected hostname may need its own DNS resolution, C. Distinct hostnames need not resolve to the same address, so B is false. A response cannot change a request already transmitted; following a redirect involves another request, so D is false.

## Q32

**Correct answer:** A, B, D

A determines B, so it supplies AB and hence C; B on the left of AB→C is extraneous (A). C then determines D, making the direct A→D redundant (B). A determines all attributes and is minimal, proving D. Without C→D, the closure of C contains only C, so that dependency is not redundant and C is false. Removing an entire dependency differs from removing an extraneous attribute within another one.

## Q33

**Correct answer:** 45055

The highest mapped address has high nibble1010 and all twelve low bits1: hexadecimalAFFF. In decimal this is10×4096+4095=45055. The chip occupies one aligned4KiB window, not the entire64KiB address space.

## Q34

**Correct answer:** 0.9

Every request pays2ns, and a fraction1−h pays an additional50ns. Thus7=2+50(1−h), giving1−h=0.1 and h=0.9. Using50ns as the entire miss time would omit the nonoverlapped cache lookup.

## Q35

**Correct answer:** 10

The burst2 job starts at0. After it ends at2, one switch delays the burst3 job to3. That job ends at6, and the next switch delays the burst5 job to7. Waiting times are0,3,7, totaling10. Context-switch time is waiting time for jobs still ready.


## Q36

**Correct answer:** A, C

Each router decapsulates the incoming link frame and constructs an outgoing frame for the next link, so link addresses can change (A). Forwarding decrements TTL (C). In the stipulated absence of NAT/tunneling, end-to-end IP addresses remain H and J, making B false. A first-hop Ethernet destination can be the router's local interface, not the remote host, so D is false. Link-layer delivery and end-to-end addressing have different scopes.

## Q37

**Correct answer:** 3

Earliest finish selects A, then B, then D, earning3+3+2=8. The optimal weighted choice is C followed by D, earning9+2=11. No schedule containing C can also contain A or B, and the best schedule without C earns8, so11 is optimal. The excess is3. Earliest-finish selection optimizes cardinality of unweighted compatible activities, not arbitrary profits.

## Q38

**Correct answer:** 4

One packet takes (1200/k+75)/1000 seconds per link. With a two-link pipeline, the last of k packets arrives after k+1 packet times. Minimizing (k+1)(1200/k+75) is equivalent to minimizing1200/k+75k. For positive real k, AM–GM gives a minimum when1200/k=75k, hence k=4. Four is an allowed divisor of1200, so it is also the integer optimum. Packet headers impose a cost on excessive segmentation.

## Q39

**Correct answer:** 5.75

The six-bit signed scaled range is−32..31, or−8..7.75 after dividing by4. The first sum is4.5, the second exact sum9 saturates to7.75, and the final subtraction2 yields5.75. Summing first and saturating only once would incorrectly give7. Saturation is applied after each operation as specified.

## Q40

**Correct answer:** A, C

x−x is always exactly zero within range, and x*0 likewise, so A,C preserve value and do not remove possible traps. B removes the divide-by-zero trap when x=0. D removes a possible overflow trap in x+1 at the maximum integer, even though the algebraic result would be x. Algebraic identities require attention to the stated arithmetic semantics.

## Q41

**Correct answer:** 4

After successive iterations, (slow,fast) is(1,2),(2,4),(3,2),(4,4). The first tested equality is at node4. Initial equality is deliberately not tested, and the meeting point need not be the cycle entrance node2.

## Q42

**Correct answer:** 218

SCAN travels50→199→20, a distance149+179=328. LOOK travels50→90→20, a distance40+70=110. The extra distance is218=2(199−90). The stop rule excludes any additional travel after servicing20; otherwise endpoint conventions could change the answer.

## Q43

**Correct answer:** 0

The requested end offset is98+4=102, exceeding the limit100. The entire access fails the atomic bounds check before any byte is read, so zero bytes are accessed. Two requested byte addresses lie within the segment, but that does not authorize a partial read under these semantics.

## Q44

**Correct answer:** A, B, C

Near1.5, adjacent representable values are1.375,1.5,1.625, with spacing0.125. The midpoint boundaries are1.4375 and1.5625. The significand of1.5 is1.100, whose last retained bit is even; both ties therefore round to1.5. A,C are included, B is strictly inside the interval, and D is already exactly represented at1.625. Ties on both sides can select the same even significand.

## Q45

**Correct answer:** 0

FIFO faults on A,B,C and D. The intervening A hit does not change insertion order; D evicts A. The final B is still resident, so FIFO has4 faults. The optimal policy also needs the four distinct pages at least once and can keep B when D arrives, attaining4. The difference is zero. A familiar trace need not exhibit a strict advantage for an optimal policy.

## Q46

**Correct answer:** 1

Three distinct eigenvalues imply a basis of eigenvectors. Applying polynomial p(t)=t²−3t+2=(t−1)(t−2) gives eigenvalues0,0,6 for B in that basis. Exactly one is nonzero, so rank B=1. Without diagonalizability, simply counting nonzero eigenvalues would not generally determine rank; it is justified here by distinct eigenvalues of A.

## Q47

**Correct answer:** 4

The specified indexed lookup reads root, one lower index block, and one data block:3 reads. Against the stated7-read binary-search worst case, it saves4. There is no cache assumption that permits omitting the root read. The index's4 physical blocks are not all read in one lookup.

## Q48

**Correct answer:** 3

Deleting6 leaves [8], below the two-key minimum. The right sibling [10,12,14] has three keys, so it lends10, yielding[8,10] and[12,14]. No leaf is merged and the root retains three children. Root separator values must be adjusted, but that does not alter the child count.

## Q49

**Correct answer:** 4

Words0,4 conflict in line0 and words1,5 in line1. Alternation makes all eight direct-mapped accesses miss. The fully associative cache holds all four distinct words after four compulsory misses; the second round is entirely hits. The miss reduction is8−4=4. Equal capacity does not imply equal conflict behavior.

## Q50

**Correct answer:** 12

Three enqueues give3 pushes. Each element transfers from I to O exactly once, giving3 pops and3 pushes. Each of the three dequeues gives one pop from O. Total3+6+3=12. The second dequeue does not transfer c because b is still in O; this preserves FIFO order.

## Q51

**Correct answer:** A, B

The assignment x=0 proves the condition true. The other branch and input call are unreachable, and y=4 gives z=16. Thus A,B. C would execute dead code unnecessarily and alter behavior; D ignores feasibility and confuses syntactic assignment presence with possible execution. Reachability can increase the precision of constant propagation.

## Q52

**Correct answer:** 1

The true best choice is B+C with weight6 and value11; A+C gives9. With ascending updates, processing C can reuse C three times, giving12 at capacity6. No unbounded combination at weight≤6 exceeds12, so the faulty result is12 and the excess1. Descending capacity updates prevent using the current item more than once in0/1 knapsack.

## Q53

**Correct answer:** 2

The endpoint values are f(2)=2 and f(−2)=−2, so the secant slope is1. Solve3c²−3=1, giving c=±2/sqrt(3). Both lie strictly between−2 and2, yielding two points. The theorem guarantees at least one, not necessarily uniqueness.

## Q54

**Correct answer:** 32

A comparison tree for a single extremum uses n−1=63 comparisons, so two runs use126. The pairwise algorithm first compares32 pairs, then finds the maximum of32 winners in31 comparisons and the minimum of32 losers in31 more. Its total is94, saving32. Pairwise classification allows one comparison to contribute information toward both extrema.

## Q55

**Correct answer:** 0.1667 (accepted range 0.16665–0.16675)

Under U, gold has likelihood1 in GG and1/2 in GS, giving posterior(1/2)/(1/2+1/4)=2/3. Under P, gold is guaranteed from either box, so the observation carries no information and the posterior remains1/2. The difference is1/6≈0.1667. Conditioning must include how an observation was selected; the visible color alone does not determine its likelihood.
## Q56

**Correct answer:** 0.21484375

A valid even-parity word remains valid exactly when an even number of bits flips. Excluding no change, the possibilities are two or four flips. Their total probability is C(4,2)(1/4)²(3/4)²+(1/4)^4=54/256+1/256=55/256=0.21484375. The undetected-error probability excludes the zero-error event.

## Q57

**Correct answer:** A, C

Intersection of any two remaining subsets is still a remaining subset and is their greatest lower bound, giving A. The empty set remains below all, giving C. The pair {a,b},{c} has no upper bound in the reduced poset because its only possible upper bound was the removed full set. Hence B,D are false. Removing a top element can destroy joins while preserving all meets.

## Q58

**Correct answer:** 1

x is needed either for B2's update or B3's return, so it is live at B1 entry. The incoming value of p is overwritten by read() before any use; it is not live at entry, though the new p is live after that assignment until the branch. Thus exactly one of the two variables is live. Loops require a fixed-point computation, but a definite kill before every use still removes the old value.

## Q59

**Correct answer:** 2

Both XORs must be1, requiring x≠y and y≠z. Over binary values, this means x=z=NOT y. The triples are010 and101, two in total. The conditions are not independent choices for all three inputs.

## Q60

**Correct answer:** A, B

There are finitely many strings in each bounded-length set. Run M on every candidate; the promise guarantees every run finishes, allowing A,B to be decided. The promise does not bound the number of inputs. For undecidability, construct a total machine that simulates a chosen machine on a fixed input for |w| steps. Accepting iff it has halted makes emptiness equivalent to nonhalting; accepting iff it has not halted makes universality equivalent to nonhalting. Thus C,D remain undecidable even on promised total machines. A per-input termination guarantee is not a bound on all inputs collectively.

## Q61

**Correct answer:** 120

After T1 commits, x=120. T2's before-image is therefore120, and its provisional value is115. Rolling back T2 restores120 while retaining the committed earlier transaction. Undo is transaction-specific; restoring the database's initial100 would wrongly erase T1.

## Q62

**Correct answer:** 6

Track the pair(length mod3, number of1s mod2), giving six states and one accepting pair(0,0). All pairs are reachable: at any sufficiently large length of a chosen residue, choose either zero or one1. For any two distinct pairs, choose a suffix whose length cancels the first residue and whose1-count parity cancels the first parity; sufficiently long suffixes allow either parity. The second pair then fails at least one condition, so all six are distinguishable and six is minimal. A product construction alone establishes only an upper bound; distinguishability supplies the lower bound.

## Q63

**Correct answer:** 157

There are400/20=20 bursts, occupying100 cycles. Only19 gaps lie between them, taking57 cycles. Completion occurs after157 cycles. Adding a twentieth gap would count time after completion, contrary to the stated boundary condition.

## Q64

**Correct answer:** 12

The root's three distinct child subtrees can be ordered in3!=6 ways. Vertex a's two leaves can be ordered in2!=2 ways. Vertex b has only one child, contributing one choice. Distinct labels make these choices give distinct preorder strings, so6×2=12. Permutations within a subtree cannot interleave its preorder block with another subtree.

## Q65

**Correct answer:** 1.19

There are20×0.25=5 mispredictions, adding15 cycles to the baseline104. Total execution time is119 cycles and CPI=119/100=1.19. The ideal fill/drain cost is already included in104 and must neither be omitted nor added twice.


