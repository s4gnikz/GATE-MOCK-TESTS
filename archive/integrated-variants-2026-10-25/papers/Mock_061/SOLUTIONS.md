# Worked Solutions — Mock Test 061

## Q1

**Correct answer:** A

Q establishes the discrepant readings; S explains the diagnosis; P describes the repair; R gives the subsequent test. Thus Q,S,P,R is required. B uses “this discrepancy” before its referent and puts the second trial before repair. C diagnoses the defect after the repair and trial. D introduces repair before the problem. Follow explicit references and causal dependencies, not just grammatical possibility.

## Q2

**Correct answer:** 0.6667 (accepted range 0.66665–0.66675)

P(A and boy)=1/2, whereas P(B and boy)=(1/2)(1/2)=1/4. The posterior is (1/2)/(3/4)=2/3, rounding to 0.6667. Sampling a household first does not make the five children equally likely; counting three of four boys would use a different experiment.

## Q3

**Correct answer:** C

The reply permits both agreement and refusal as interpretations, so C captures its ambiguity. A describes length without addressing meaning; B describes evidential support; D contradicts the possibility of refusal. The explanatory clause establishes the relevant sense without requiring a claim about the witness's intent.

## Q4

**Correct answer:** 20 (exact)

**Concept:** General Aptitude — Powers and logarithms

1. Eight is 2^3, so three doublings take 12 hours and one doubling takes 4 hours.
2. Thirty-two is 2^5, requiring five doublings. The time is 5*4=20 hours.

**Common misconception:** Exponential growth relates elapsed time to the logarithm of the multiplication factor.

## Q5

**Correct answer:** B

**Concept:** Testing a proposed predictor with comparison data.

B supplies observations where the suspected condition is present and absent, allowing comparison. A and D claim certainty without the missing evidence; C deliberately keeps the comparison condition unobserved.

**Common misconception:** Counting only instances consistent with a hypothesis instead of testing alternatives.

## Q6

**Correct answer:** 2

The first rotation leaves the original−x face pointing−x. The second positive y rotation maps−x to+z. Hence the original−x face ends upward, code2. Equivalently the composite maps(x,y,z) to(y,−z,−x), and solving for output(0,0,1) gives input(−1,0,0). The axes are fixed world axes, not changing body axes.

## Q7

**Correct answer:** B
**Concept:** Precedence-constrained parallel tasks.

Run A and B from time zero on the two workers. They finish at 4 and 3; C then runs from 4 to 6. The chain A→C requires at least 4+2=6 hours, so this schedule is optimal. B is correct; A violates that lower bound, while C,D fail to use available concurrency optimally.

**Common misconception:** Worker capacity cannot remove a precedence constraint.

## Q8

**Correct answer:** 8
**Concept:** Constrained lattice paths.

There are 2 paths to (1,1) and C(5,2)=10 paths from there to (4,3), for 20 paths through the required point. Forbidden paths additionally pass through (3,2): their count is 2×C(3,1)×C(2,1)=12. Subtracting gives 8. The monotone directions ensure these visits have the indicated order and no path is counted twice.

**Common misconception:** Count forbidden paths subject to the required visit, rather than all paths through the forbidden point.

## Q9

**Correct answer:** C

**Concept:** Reference and causal sequencing.

R introduces the result and competing explanations. P's “these explanations” refers back to them and introduces the repeat. Q describes that repeat's outcome; S states the ensuing conclusion. Thus R–P–Q–S is required. A uses an unresolved reference, B reports the repeat before introducing it, and D places the conclusion before its grounds.

**Common misconception:** Ordering sentences by vocabulary alone instead of their logical dependencies.

## Q10

**Correct answer:** 7.8

**Concept:** Successive price factors and fee base.

For cost 100, marked price is 125 and discounted price 125×0.88=110. The fee is 2.2, leaving net proceeds 107.8 and profit 7.8% on cost.

**Common misconception:** Charging the transaction percentage on cost instead of the specified selling price.

## Q11

**Correct answer:** B

**Concept:** Shannon expansion and multiplexers.

At x=0, F=yz; at x=1, F=y+z. Thus B supplies the two cofactors. A reverses them; C fails when y=z=1 and x=0; D fails, for example, at x=y=z=0.

**Common misconception:** Interchanging the inputs selected by zero and one.

## Q12

**Correct answer:** -0.75

An inverse y satisfies3*y=0, the identity. Thus3+y+3y=0, yielding y=−3/4=−0.75, which belongs to the domain. The operation is commutative, so it is also the left inverse. Multiplicative inverse under an unfamiliar group law need not be the reciprocal under ordinary multiplication.

## Q13

**Correct answer:** A, B
**Concept:** TCP byte-stream delivery.

TCP preserves byte order, but not send-call boundaries. Buffering and arrival timing permit a single five-byte return or a one-byte return followed by four, proving A and B. With a blocking socket and no closure, lack of data causes waiting, not a zero return; C is false. Ordered delivery excludes D.

**Common misconception:** TCP provides a byte stream, not an application-message boundary for every send call.

## Q14

**Correct answer:** A, B, D
**Concept:** Substitution into a sequential characteristic equation.

For J=K=0, Q′=Q, proving A. For J=K=1, Q′=NOT Q, proving B. For J=1,K=0, Q′=(NOT Q)+Q=1, so C is false. For J=0,K=1, both terms vanish, so D is true.

**Common misconception:** Force-set and force-reset inputs must be checked against the specified characteristic equation.

## Q15

**Correct answer:** A
**Concept:** SQL aggregate treatment of NULL and duplicates.

COUNT(*) counts four rows. COUNT(x) excludes the one NULL but retains both rows with value 2, giving three. A is correct. B excludes NULL from COUNT(*); C,D mistakenly apply DISTINCT.

**Common misconception:** COUNT(column) is not COUNT(DISTINCT column).

## Q16

**Correct answer:** A, D

Concept: PDA acceptance-mode conversion. After consuming all input in an original final state, drain mode can empty the protected stack and accept, A. If input remains, drain mode has no consuming transitions and cannot meet the all-input-consumed requirement, D; B is therefore false. The fresh marker protects against premature empty-stack acceptance and must be distinguished from original symbols, so C is false. Acceptance requires both the stack/final-state condition and complete input consumption.

## Q17

**Correct answer:** 3

Concept: bipartite matching and vertex covers. Removing a perfect matching from K3,3 leaves a six-cycle. Its three disjoint alternate edges require at least three cover vertices. Either original bipartition side covers every remaining edge with three vertices. Thus the minimum is three. A matching supplies a lower bound even after other edges are deleted.

## Q18

**Correct answer:** 3288

**Concept:** Final-page internal fragmentation.

Three 4096-byte pages are needed, allocating 12288 bytes. Unused bytes in the last page are 12288−9000=3288. Earlier pages are full because the region begins on a boundary.

**Common misconception:** Counting whole unused pages as part of this allocation.

## Q19

**Correct answer:** 5

Classify by the unique occurrence's starting position. At position1, avoiding another occurrence forces the third bit to1, giving0010 and0011. At position2, both exterior bits must be1, giving1001. At position3, the second bit must be1, giving0100 and1100. Thus there are five. Treating occurrences as disjoint would mishandle strings containing000.

## Q20

**Correct answer:** 5

Initially three frames are shared. The first parent write to page0 makes one private copy, increasing the count to4; its second write uses that same private frame. The child's first write to page1 makes another copy, giving5. Repeated writes do not repeatedly copy an already private page.

## Q21

**Correct answer:** 400

**Concept:** Summing odd increments.

T(n)=Σ_(i=1)^n(2i−1)=2n(n+1)/2−n=n². Therefore T(20)=400.

**Common misconception:** Treating the recurrence's incremental cost as the total.

## Q22

**Correct answer:** 4

The expression contains+ , / , − and*, each emitted once after its children. The postfix form is ab+cde/−*, with four operators. Translation changes order, not the expression tree's operator count.

## Q23

**Correct answer:** 2

Blocks40 and41 form one contiguous extent;90 forms another. A single extent would include unrequested blocks42–89, contrary to the question. Logical consecutiveness does not guarantee physical consecutiveness.

## Q24

**Correct answer:** A, B

**Concept:** B+ tree structural invariants.

Separators may copy leaf key values, so A holds. Balance keeps all leaves at one depth, giving B. Data entries are at leaves, refuting C; root occupancy has special exceptions, refuting D.

**Common misconception:** Importing ordinary B-tree data-placement rules unchanged into B+ trees.

## Q25

**Correct answer:** A, C

A strict greater-than shift never moves an equal predecessor past the key, so A holds. On sorted input no predecessor exceeds its key, proving C. A non-strict comparison can move equal records past each other, disproving B. Shifts correspond to strict inversions; distinct descending records already disprove D. Equality is crucial to stability but not to the shift count claimed in D.

## Q26

**Correct answer:** 5

Squares modulo8 are0,1,4, repeating for the probe sequence. Only three distinct slots are reachable. If all three are occupied, the remaining five can still be empty but inaccessible to that insertion. A low overall load does not guarantee that a particular probing scheme visits an empty slot.

## Q27

**Correct answer:** A

U used an uncommitted value that disappears when T aborts. Cascading recovery therefore rolls back U's dependent execution, even if U wrote nothing. A is correct. B invents a conflict: read–read pairs are not conflicts. C and D assert unjustified universal abort rules. Read-only does not mean immune to dirty data.

## Q28

**Correct answer:** 12

Concept: pointer and pointee increments. `*p++` means `*(p++)`: x receives 2 and p advances to a[1]. `++*p` increments that element from 4 to 5 and gives y=5. The sum is 2+5+5=12. Incrementing a pointer and incrementing the pointed value are different operations.

## Q29

**Correct answer:** 45055

The highest mapped address has high nibble1010 and all twelve low bits1: hexadecimalAFFF. In decimal this is10×4096+4095=45055. The chip occupies one aligned4KiB window, not the entire64KiB address space.

## Q30

**Correct answer:** 5

**Concept:** Hit lookup plus conditional miss penalty.

Every access costs two ns; a fraction 0.05 additionally costs 60 ns. The mean is 2+0.05×60=5 ns.

**Common misconception:** Charging the miss penalty on every access or excluding the cache lookup on a miss.

## Q31

**Correct answer:** A, B

Substituting x=0 leaves y AND1=y, proving A; x=1 leaves 1 AND z=z, proving B. With x=0,y=1,z=0, F=1 but yz=0, refuting C. With x=1,y=0,z=0, F=0 while x XOR y XOR z=1, refuting D. The expression implements a selector, not a three-way parity operation.

## Q32

**Correct answer:** C

304 validates reuse of the stored representation rather than supplying a replacement body; C follows. A confuses status metadata with content, B confuses validation with deletion, and D assumes a body that the validation response does not supply.

## Q33

**Correct answer:** A

**Concept:** Engineering Mathematics — Propositional and predicate logic

1. Negating the outer quantifiers changes forall x exists y into exists x forall y.
2. Negating the conjunction gives NOT R(x,y) OR NOT forall z (R(x,z) -> z=y).
3. The inner negation is exists z [R(x,z) AND z!=y]. Substitution gives A. The original formula says each x has exactly one R-successor; its negation allows an x with none or more than one.

- **A:** It follows all three quantifier and connective changes.
- **B:** For a two-element identity relation the original is true, but this option is also true by choosing x!=y.
- **C:** For a singleton empty relation the original is false, but this conjunction is false.
- **D:** For a universal relation on two elements the original is false; this option is false because z=y defeats its universal conjunct.

**Common misconception:** Negating unique existence requires accounting for both zero and multiple witnesses.

## Q34

**Correct answer:** 32

Each nonbase call creates two children with argument reduced by one. There are five branching levels before the leaves, giving2^5=32 base calls. The question asks only for leaves, not all63 invocations.

## Q35

**Correct answer:** A

**Concept:** Control links versus lexical links.

The dynamic link identifies the caller's activation for return-time restoration. A holds. A static link follows lexical enclosure and need not identify the caller, refuting B. Symbol-table and heap-object pointers in C,D do not restore the caller's activation.

**Common misconception:** Assuming caller and lexical parent always coincide.

## Q36

**Correct answer:** C

For outer value i=n/2^r, r=0..k, the inner loop executes r+1 times. The total is1+2+...+(k+1)=(k+1)(k+2)/2, or Θ(k²)=Θ((log n)²). Thus C is correct. A misses the growing inner count, while B,D overestimate it by treating geometric index values as linearly many iterations.

## Q37

**Correct answer:** 2

Repeated movement by−8 modulo18 partitions indices into gcd(18,8)=2 cycles, each of length9. One consists of the even indices and one of the odd indices. The algorithm starts one cycle per component, hence twice. The rotation amount alone is not the number of disjoint cycles.

## Q38

**Correct answer:** 15

Concept: aliasing in linked structures. Reversal makes 4→3→2→1→null. B still points to node 9, whose next pointer is still node 3; node 3's next has changed to 2. Thus B now visits 9,3,2,1, sum 15. The nodes are shared objects, not independent copies of their labels.

## Q39

**Correct answer:** A, C

Concept: duplicate minima. The two pushes of one store only one auxiliary minimum. Popping one removes that minimum even though the other one remains in the data stack, so A is true and B false. Storing equal minima as separate entries keeps their multiplicities synchronized, C. Never removing minima would retain values after their last occurrence was popped, so D fails. An auxiliary summary must represent duplicate occurrences or their counts.

## Q40

**Correct answer:** A, C

Each router decapsulates the incoming link frame and constructs an outgoing frame for the next link, so link addresses can change (A). Forwarding decrements TTL (C). In the stipulated absence of NAT/tunneling, end-to-end IP addresses remain H and J, making B false. A first-hop Ethernet destination can be the router's local interface, not the remote host, so D is false. Link-layer delivery and end-to-end addressing have different scopes.

## Q41

**Correct answer:** A, C

**Concept:** Pipe EOF and inherited descriptors.

An empty pipe yields EOF only when no referring write descriptor remains open, proving A. An inherited but unused writer still prevents EOF, so closing unused writers in both processes is needed for the intended EOF protocol, giving C. B leaves an open parent writer; D ignores it and substitutes EOF for blocking. Both are false.

**Common misconception:** Assuming that a process which never writes cannot keep a pipe's write end alive.

## Q42

**Correct answer:** A, B, D
**Concept:** Context-free closure with regular languages.

Intersecting a CFL with a regular language preserves context-freeness (A). L minus R equals L∩complement(R), and a regular complement is regular, proving B. Union with R, itself a CFL, preserves context-freeness (D). C is not guaranteed: choose R=Σ* and a CFL L whose complement is not context-free, such as the complement of {aⁿbⁿcⁿ} over {a,b,c}; that L is context-free by separating incorrectly ordered strings and unequal adjacent block counts. Then R minus L is the non-CFL equal-three-count language.

**Common misconception:** Set difference is not symmetric; complementing the regular operand is safe, complementing an arbitrary CFL is not.

## Q43

**Correct answer:** 7

The third coefficient row equals the sum of the first two rows. Consistency therefore requires k=2+5=7. The first two rows are independent, so at k=7 the rank is2 with three unknowns, giving infinitely many solutions. For other k the dependent left sides conflict with the right sides. Zero determinant alone would not establish consistency.

## Q44

**Correct answer:** 10

Concept: packet pipelining and overhead. One packet transmission takes (10000/k+100)/R. The first packet crosses two links in two such intervals, then one finishes per interval; completion takes (k+1)(10000/k+100)/R. Its k-dependent part is 100k+10000/k, at least 2sqrt(100·10000)=2000, with equality at k=10. Ten divides 10000, so the continuous optimum is also feasible. Ignoring headers incorrectly favors indefinitely smaller packets.

## Q45

**Correct answer:** 4

The shared a+b node is one. Multiplying it by itself adds one. b+a is a distinct ordered-child addition node, adding one; the outer sum adds one. Total4. Sharing identical syntax does not automatically use commutativity to identify reversed operands.

## Q46

**Correct answer:** 4

Track (main,victim). A reads memory and gives (A,empty). B reads memory and gives (B,A). A hits the victim and swaps to (A,B). C misses both, reads memory, and gives (C,A), discarding B. Finally B misses both again and reads memory. Four memory reads occur. A victim-cache hit is a swap rather than an additional memory fetch.

## Q47

**Correct answer:** 8

Immediately after fork the parent has3 threads and the child1. Each adds2, yielding5+3=8. Fork's specified child-thread rule differs from copying every parent thread.

## Q48

**Correct answer:** 2

All minterms with A=1 are included, and all with B=0 are included; the excluded minterms 4,5,6,7 have A=0,B=1. Thus F=A OR (NOT B), requiring two literals. A zero-literal constant or single literal cannot have precisely these four zero assignments out of sixteen. The two literals therefore achieve the lower bound. C,D disappear because each corresponding K-map group spans both their values.

## Q49

**Correct answer:** A, B, D

The |xy|≤p condition puts nonempty y entirely in the first p zeros, proving A. Removing it preserves all p ones but reduces zeros, proving B. This works for every possible allowed length of y, so C is false. The contradiction establishes nonregularity, proving D. The string is chosen before the decomposition but handles all legal decompositions.

## Q50

**Correct answer:** 2

Insert 6 into the left leaf, producing[2,5,6]. Inserting 7 produces[2,5,6,7], split into[2,5] and[6,7]; separator 6 is added alongside the existing separator 8. The root now has three leaf children and two keys, within its capacity. Leaf promotion copies rather than removes the separator key from the new leaf.

## Q51

**Correct answer:** 0.1667 (accepted range 0.16665–0.16675)

Taylor expansion gives exp(x)=1+x+x²/2+x³/6+O(x4). Thus f(x)=1/2+x/6+O(x²), requiring f(0)=1/2 and giving derivative1/6. The continuous extension value and its derivative are different coefficients.

## Q52

**Correct answer:** A, B, D

With x=0 the loop is skipped, proving A. With x=1, every update keeps x positive and strictly increases it, so the original never returns while the rewritten code returns immediately, proving B. C ignores observable termination; D correctly recognizes that obligation. An unused computed value does not automatically make its entire computation removable.

## Q53

**Correct answer:** 256
**Concept:** Reuse distance and capacity misses.

Each row occupies one aligned cache line, so a column scan visits 16 different lines. Between successive accesses to one row's line, 15 other distinct lines are accessed, exceeding the capacity of eight. LRU therefore evicts every line before its next use. All 16×16=256 element reads miss, despite each row's elements sharing one line.

**Common misconception:** Spatial locality helps only when the line remains resident until the nearby element is accessed.

## Q54

**Correct answer:** 14

The first instruction uses EX in cycle3. Instruction2 occupies EX in cycles4–6; subsequent EX occupancies are7 for instruction3,8 for instruction4,9–11 for instruction5, and12 for instruction6. Instruction6 then uses MEM13 and WB14. Equivalently, six ordinary instructions need6+4=10 cycles and the two extended EX occupancies add2 each. There is one shared EX resource, so the multiplications cannot overlap there.

## Q55

**Correct answer:** A, C
**Concept:** Recognizer scheduling for union and intersection.

For union, dovetailing eventually discovers an acceptance from either recognizer, proving A. Sequential execution in B can loop forever on the first machine even when the second would accept. For intersection, members make both sequential recognitions accept; nonmembers never make both accept, so C is a valid recognizer even if it sometimes loops. D can accept a member whose recognizing computation takes more than one million steps, so it is invalid.

**Common misconception:** A strategy unsuitable for union may still be suitable for intersection because the required acceptance conditions differ.

## Q56

**Correct answer:** 6

Concept: cardinality under two functional constraints. For each fixed A, the B–C pairs form a matching: neither a B nor a C can occur twice with different partners. Maximum matching size=min(3,4)=3. Two A values allow 2·3=6 tuples, attained by using three distinct B–C pairs for each A. Multiplying domain sizes ignores the dependencies.

## Q57

**Correct answer:** C

**Concept:** Algorithms — Greedy algorithms

Earliest-finish selection gives B,C,E,G, a feasible four-activity schedule. The earliest-finish exchange argument guarantees that its cardinality is maximum, so m=4. To count all maximum subsets, partition by the first activity. Starting with A forces D,F,H to fit three more, yielding {A,D,F,H}. Starting with B, the next activity can be C or D. If it is C, the final pair can be (E,G), (E,H), or (F,H). If it is D, the final pair must be (F,H). Starting with C or any later activity permits at most three activities total, so adds no maximum subset. The five maximum subsets are {A,D,F,H}, {B,C,E,G}, {B,C,E,H}, {B,C,F,H}, and {B,D,F,H}. Hence (m,r)=(4,5).

- **A:** False: B,C,E,G is already a feasible set of four activities.
- **B:** False: it omits one of the five listed optimal subsets, often the one beginning with the later-finishing A.
- **C:** True: earliest-finish greedy establishes m=4, and partitioning by the first two choices gives five optimal subsets.
- **D:** False: earliest-finish greedy reaches four and is optimal; five compatible activities cannot be selected.

**Common misconception:** An earliest-finish greedy algorithm finds one optimum, but it does not enumerate every optimal schedule.

## Q58

**Correct answer:** 0.375

**Concept:** Conditional density over a planar region.

P(Y>X²)=∫₀¹(1−x²)dx=2/3. The weighted first moment over that event is ∫₀¹x(1−x²)dx=1/4. Dividing gives (1/4)/(2/3)=3/8=0.375.

**Common misconception:** Conditioning by substituting Y=X² instead of integrating the region above the curve.

## Q59

**Correct answer:** 3

Concept: weighted covering. Q+R covers all columns at cost 2+1=3. No cost below three works: the only cost-two choices are Q alone, missing 1, or R+S, missing 2; any cost-one choice also fails. Thus three is optimal. Minimizing cost need not coincide with an arbitrary minimum-cardinality cover.

## Q60

**Correct answer:** 6 (exact)
**Concept:** Carry-lookahead path delays.

Propagates arrive at time 2 and generates at time 1. The expanded carry products involving propagates arrive by time 3; the final OR produces c1–c4 by time 4. In particular c3 can arrive at 4, so s3's final XOR finishes at 6; s1 and s2 have the same upper bound. s0 is ready at 4 and c4 at 4. Latest output time is 6.

**Common misconception:** Expanding carry logic removes the ripple chain, but the final sum XOR still adds delay after carry generation.

## Q61

**Correct answer:** 9

Concept: CRC undetected two-bit errors. An error is xʲ(xᵏ+1), k the positive separation. Since G has constant term one, xʲ is coprime to it. Modulo G, successive nonzero powers of x have period seven: 1,x,x²,x+1,x²+x,x²+x+1,x²+1, then 1. Thus k must be a multiple of seven. Available separations are 7 and 14, giving 15−7=8 and 15−14=1 pairs, total nine. Two-bit errors are not necessarily detected for every frame length.

## Q62

**Correct answer:** 15

**Concept:** Involutions with a prescribed fixed-point count.

f²=id implies f is a permutation and every cycle has length one or two. Choose the sole fixed point in five ways; pair the remaining four elements into two unordered pairs in three ways. Each pair forms a transposition. Total 5×3=15.

**Common misconception:** Counting pair orders or orientations as distinct functions.

## Q63

**Correct answer:** 18

**Concept:** Feasible 0/1 combinations.

No three items fit because the three lightest weigh 9. Feasible pairs have values 14 at weight 5, 15 at weight 6, 18 at weight 7 from items of weights 2 and 5, and 17 at weight 7 from weights 3 and 4. Singles are at most 12. The optimum is 18.

**Common misconception:** Applying fractional-knapsack value-density choices to indivisible items.

## Q64

**Correct answer:** A, C

With a full buffer and no consumer progress, a further blocking write can wait indefinitely, proving A. An open read endpoint is merely a reference, not an action consuming data, so B is false. Closing all readers changes the endpoint condition, rather than leaving an ordinary full pipe with a potential reader, proving C. A finite buffer cannot absorb unlimited data without draining, so D is false. Capacity can postpone blocking but cannot replace consumer progress.

## Q65

**Correct answer:** 3

C×Required is empty. Subtracting R and projecting still gives the empty set, and C−empty=C. Thus u,v,w all qualify by vacuous satisfaction of all required courses. Restricting candidates to students appearing in R would incorrectly exclude w from this explicitly defined query.

