# Worked Solutions — Mock Test 004

Review provenance is recorded separately; no human review is claimed.

## Q1

**Correct answer:** 22  
**Concept:** Alternating recurrence.

Applying the stated rule gives 1,3,5,11,21,43. Therefore a6−a5=43−21=22. The added term alternates +1,−1; it is not always positive.

**Common misconception:** Ignoring the parity-dependent term when extrapolating a sequence.

## Q2

**Correct answer:** 5  
**Concept:** Rectangle constraints and area change.

If sides are u≥v, then u+v=20 and uv=96. Hence (u−v)²=400−384=16, so u−v=4 and sides are 12,8. The new area is 13×7=91, a decrease of 5. Equivalently, uv−(u+1)(v−1)=u−v+1=5.

**Common misconception:** Equal and opposite side changes preserve perimeter but not area.

## Q3

**Correct answer:** C  
**Concept:** Agreement in nested clauses.

“Reports that are missing” takes a plural verb in the relative clause. The main subject is singular “the number,” so its verb is “is.” C gives both. A gets both wrong; B misses the main subject; D misses the relative-clause subject.

**Common misconception:** The noun closest to a verb is not always that verb's subject.

## Q4

**Correct answer:** 11.11  
**Concept:** Profit margin versus markup.

Selling price is 100×0.9=90 and profit is 90−80=10. As a percentage of selling price, this is 100×10/90=11.111…%, rounded to 11.11%. Dividing by cost would instead give a 12.5% markup.

**Common misconception:** Profit percentage requires the denominator specified in the question.

## Q5

**Correct answer:** B, D  
**Concept:** Quantified deduction.

The witness that is both A and B is C and therefore not D, proving B. Every B is C and no C is D, proving D. A generalizes the one known A witness to every A. C asserts an overlap with D that is neither required nor supplied.

**Common misconception:** An existential premise cannot generally be promoted to a universal conclusion.

## Q6

**Correct answer:** C  
**Concept:** Composition of plane transformations.

R maps (x,y) to (−y,x), and F swaps coordinates. R then F gives (2,−1); F then R gives (−2,1). C is correct. A reverses the requested order; B gives intermediate-style transformations; D assumes the two transformations commute.

**Common misconception:** A rotation and a reflection generally depend on composition order.

## Q7

**Correct answer:** B  
**Concept:** Survey evidence and causality.

The survey establishes only what respondents reported. Voluntary selection may bias their composition, and no comparison separates the app's effect from other causes. B preserves those limits. A overgeneralizes and asserts causality; C treats self-selection as representativeness; D mistakes absence of causal evidence for proof of no benefit.

**Common misconception:** Failure to establish a causal claim does not establish its negation.

## Q8

**Correct answer:** 216  
**Concept:** Restricted digit permutations.

The final digit is 0 or 5. Ending in 0 leaves 5!=120 arrangements, all with nonzero first digit. Ending in 5 leaves five digits including zero: there are 5!−4!=96 arrangements whose first digit is nonzero. Total 216.

**Common misconception:** The leading-zero restriction affects the two ending-digit cases differently.

## Q9

**Correct answer:** A, B, D  
**Concept:** Mean, median, mode and range.

The original sum is 2+9+7=18. Mean four after adding two x values gives 18+2x=32, hence x=7. The sorted data are 1,1,3,3,3,7,7,7. The middle pair is 3,3, so the median is 3; both 3 and 7 occur three times, so there is no unique mode. Range is 7−1=6. Thus A,B,D hold and C fails.

**Common misconception:** A mean change need not change the median, and a mode need not be unique.

## Q10

**Correct answer:** A, C  
**Concept:** Folding a cube net.

Take B as the front face. Its neighbours A,C,D,F fold to left,right,top,bottom, while E beyond D becomes the back. Opposite pairs are A/C, B/E and D/F. A/E and E/F therefore share edges, proving A,C. B and D list opposite pairs, not adjacent faces.

**Common misconception:** Squares separated in the flat net may become adjacent after folding.

## Q11

**Correct answer:** 5  
**Concept:** Updating first and second moments.

The original sum is 50. The remaining sum is 4×11=44, so the removed observation is 6. The original sum of squares is 5(8+10²)=540. Removing 6² leaves 504. New variance is 504/4−11²=126−121=5.

**Common misconception:** Variance cannot be updated using only the mean without tracking the second moment.

## Q12

**Correct answer:** B  
**Concept:** Quotient-group element order.

H={0,4,8}. A multiple k(5+H) is the identity coset exactly when 5k mod 12 belongs to H, equivalently 5k is divisible by 4. The least positive k is 4. A confuses |H| with the coset's order; C and D are larger than the least returning multiple.

**Common misconception:** Element order in a quotient is determined by return to the subgroup, not necessarily return to zero in the original group.

## Q13

**Correct answer:** 8  
**Concept:** Pipeline overlap with a load-use stall.

Three instructions in five stages take 3+5−1=7 cycles without stalls. The LOAD-to-first-ADD dependence adds one bubble. The second ADD obtains its operands by the stated forwarding, adding none. Total eight cycles.

**Common misconception:** A dependency does not imply a stall when forwarding supplies the value at the required stage.

## Q14

**Correct answer:** 2  
**Concept:** Articulation vertices.

Removing 1 separates vertex 5 from the triangle. Removing 2 separates vertices 3,4 from 1,5. Removing 3 or 4 leaves the triangle's other route; removing leaf 5 does not disconnect the remainder. Thus only 1 and 2 are articulation vertices.

**Common misconception:** A vertex on a cycle may still be an articulation point if it connects that cycle to the rest of the graph.

## Q15

**Correct answer:** A, C  
**Concept:** Pumping-lemma quantifiers and a forced pumping region.

The bound |xy|≤p confines nonempty y to the first zero block, proving A. Pumping up adds zeros only before the single 1, so the two sides no longer match: B is false. Pumping down removes at least one zero from only that side, proving C. A nonregularity proof must defeat every permitted decomposition for its chosen witness; D is false.

**Common misconception:** The adversary chooses the decomposition; a proof must control all of its permitted choices.

## Q16

**Correct answer:** A, C  
**Concept:** Matching, vertex cover and bipartiteness.

Edges {a,2},{b,3},{c,1} give a size-three matching. No matching exceeds the smaller side's size three, proving A. The side {a,b,c} is a vertex cover, disproving B. The graph remains bipartite and has edges, so its chromatic number is exactly two, proving C. A matching cannot cover an odd number of vertices, refuting D.

**Common misconception:** Deleting selected cross-edges does not necessarily reduce maximum matching size.

## Q17

**Correct answer:** 0.21875  
**Concept:** Independent backoff events.

Either the first chooses zero and the second does not, or vice versa. These disjoint cases give 2×(1/8)×(7/8)=7/32=0.21875.

**Common misconception:** “Exactly one” excludes the case in which both stations choose zero.

## Q18

**Correct answer:** B  
**Concept:** Heap deletion and sift-down.

Move 3 to the root and remove the last slot: [3,8,7,6,5,4]. Swap with larger child 8, then larger child 6, giving [8,6,7,3,5,4]. A unnecessarily sorts the keys; C violates root heap order; D swaps the wrong lower-level elements.

**Common misconception:** A heap is partially ordered; deleting its root does not sort the remaining array.

## Q19

**Correct answer:** A, B, D  
**Concept:** Lossless decomposition and dependency preservation.

The intersection is B, which determines R2's attributes, so the decomposition is lossless. A→B is checkable in R1 and B→C in R2, preserving both. Each component's determinant is its key, so both are BCNF. In R, B does not determine A, and B→C violates BCNF. Thus A,B,D are true and C false.

**Common misconception:** A decomposition may improve normal form while also being lossless and dependency-preserving.

## Q20

**Correct answer:** A, B, D  
**Concept:** Liveness over alternative paths.

c is read by the test. A true branch uses the current a; a false branch uses the current b. The old x is overwritten on either branch before return reads x. Therefore a,b,c are live, while old x is not. This proves A,B,D and refutes C.

**Common misconception:** Liveness uses existence of a future use on some path, not a requirement that every path uses the value.

## Q21

**Correct answer:** B  
**Concept:** Transient forwarding loops during routing updates.

Initially B reaches D through A at cost two, below direct cost four. After the change, A's new best route is through B at cost five, below direct cost ten. During the mixed-table interval A sends to B and B sends back to A. B is correct. A and C ignore the actual chosen next hops; D incorrectly assumes independently correct snapshots imply a consistent network-wide snapshot.

**Common misconception:** Correct shortest-path computation does not eliminate transient loops when updates are asynchronous.

## Q22

**Correct answer:** A, C  
**Concept:** Availability of expressions across calls.

If neither operand can change, the expression value is preserved. A guarantees inaccessible unchanged locals; C supplies a direct effect proof. Unknown effects on mutable globals make B insufficient. D ignores definitions and side effects. Thus A,C hold.

**Common misconception:** Textual equality is only part of common-subexpression eligibility; intervening modifications matter.

## Q23

**Correct answer:** 1  
**Concept:** MST repair after an edge deletion.

Initially use AB=1, either AC or BC at 2, and either AD or CD at 3: weight 6. Without AB, both AC and BC are needed to connect B to A through C, together with a weight-three D edge, giving 7. Increase: one.

**Common misconception:** The cost increase is a replacement tradeoff, not the deleted edge's entire contribution.

## Q24

**Correct answer:** 6  
**Concept:** Index probes with cached data-page reuse.

Read the three index pages, then distinct data pages {4,7,9}. Repeated records on already read pages cause no additional read. Total 3+3=6.

**Common misconception:** Record count and distinct data-page count are different I/O measures.

## Q25

**Correct answer:** A, C  
**Concept:** Reductions and recognizability of complements.

If L were decidable, compose its decider with the given reduction to decide halting, impossible; A holds. B contradicts the premise. If both L and its complement were recognizable, dovetail their recognizers to decide L, contradicting A; hence C holds. D mistakes a reduction into L for an algorithm deciding membership in L.

**Common misconception:** A recognizable target can still encode an undecidable problem.

## Q26

**Correct answer:** B  
**Concept:** SSTF fairness under ongoing arrivals.

Repeated nearby requests can always offer a shorter seek than the distant request. The scheduler can keep choosing them forever, proving B. A's bound ignores future arrivals. C confuses local efficiency with fairness. D only resolves equal distances and cannot defeat strictly nearer arrivals.

**Common misconception:** A finite queue argument cannot establish starvation freedom under unbounded new arrivals.

## Q27

**Correct answer:** 50  
**Concept:** B+ deletion and separator removal.

Deleting 40 leaves [30], below the two-key minimum. Merge it into left sibling [10,20] to form [10,20,30]. The remaining right leaf is [50,60], so the root now separates these two leaves with 50. Separator 30 is removed, not retained as a third leaf boundary.

**Common misconception:** Leaf merging changes parent separators even when the root itself remains valid.

## Q28

**Correct answer:** 36  
**Concept:** Surjections after identifying domain elements.

Treat {1,2} as one effective element, giving four labelled units mapping onto three labels. Inclusion-exclusion yields 3⁴−3×2⁴+3×1⁴=81−48+3=36.

**Common misconception:** The equality constraint reduces the number of independently assigned domain units; it does not reduce the codomain.

## Q29

**Correct answer:** C  
**Concept:** Static hazards and the consensus term.

Before and after A changes, F is 1. Unequal direct and complemented path delays can temporarily make both original products 0. BC remains 1 throughout, bridging the transition. It is redundant: when BC=1, either AB or (NOT A)C already makes the steady-state output 1. AC and A(NOT C) still depend on A; the latter is also 0 here and changes the function elsewhere. (NOT B)C is 0 during this transition and changes the function, for example at A=1,B=0,C=1. Thus A,B,D fail.

**Common misconception:** Boolean equivalence alone does not ensure glitch-free behaviour under unequal delays.

## Q30

**Correct answer:** 1  
**Concept:** CSR decoding and strong connectivity.

Edges are 0→1,0→3,2→0,2→2,2→3,3→1. Vertex 2 reaches all vertices, and every vertex reaches sink 1. Adding 1→2 makes all vertices mutually reachable. Zero additions cannot suffice because 1 initially has no outgoing edge. Therefore the minimum is one.

**Common misconception:** The self-loop at 2 does not connect it back from other vertices.

## Q31

**Correct answer:** A, C  
**Concept:** One-step implicant combination.

A has matching dash positions and differs only in its first bit, yielding --01. C similarly differs only in the third position, yielding -0-1. B changes dash structure and cannot be combined by the stated rule. D differs in all four bits. Thus A,C are valid.

**Common misconception:** Covered sets may be related without satisfying the exact one-step combination rule.

## Q32

**Correct answer:** 244  
**Concept:** Signed PC-relative displacement.

The next instruction address is 0x104=260. The signed byte 0xFC represents −4, and its scaled displacement is −16. Target=260−16=244=0xF4.

**Common misconception:** The displacement is signed and scaled, and its reference address is after the branch instruction.

## Q33

**Correct answer:** A, C  
**Concept:** Segmentation bounds within allocated pages.

5000=4096+904 and is below 6000, so A holds. Offset 5999 is the last byte, proving C. Offsets at least 6000 violate the segment bound, even when their containing page exists; B and D are false.

**Common misconception:** Page allocation granularity does not erase an independent segment-length protection boundary.

## Q34

**Correct answer:** A, C  
**Concept:** Reachability of negative cycles.

The only path to b is s→a→b, of length five. Neither c nor d is reachable, so their negative cycle cannot affect paths from s. A,C hold; B,D incorrectly apply an unreachable cycle to reachable distances.

**Common misconception:** A negative cycle matters to a source-to-target distance only when it can participate in a source-to-target walk.

## Q35

**Correct answer:** D  
**Concept:** Generating function with initial conditions.

For F=Σa_nx^n, summing the recurrence for n≥2 gives F−x=3xF−2x²F. Thus F=x/(1−3x+2x²)=x/((1−x)(1−2x)). A has the wrong constant coefficient; B has the wrong recurrence sign; C also has nonzero constant coefficient.

**Common misconception:** A recurrence denominator alone does not determine a generating function; initial conditions determine its numerator.

## Q36

**Correct answer:** A, C  
**Concept:** C sequencing and side effects.

A reads the old i to calculate i+1 and then assigns it, which is defined. In C, B reads i for the left index without sequencing that read relative to the increment on the right, so behaviour is undefined. The left operand of && is sequenced before the right, so C is defined. D has two unsequenced modifications of i in function arguments, so is undefined.

**Common misconception:** Function arguments are not evaluated in a guaranteed left-to-right order in C; short-circuit operators have different sequencing rules.

## Q37

**Correct answer:** 40  
**Concept:** Fragment offset units and overlapping intervals.

The first fragment covers [0,1000). The second begins at 120×8=960 and covers [960,1560). Their intersection [960,1000) contains 40 byte positions. This count does not assume that the overlapping payload bytes agree.

**Common misconception:** Fragment-offset fields are not byte offsets.

## Q38

**Correct answer:** D  
**Concept:** Lexer states and longest match.

The tokens are string literal "if", keyword if, and identifier if2. The comment is discarded. The string's content is not tokenized as source code, and longest match keeps if2 as one identifier. Thus one keyword and three total tokens. A counts comment/string text as keywords; B counts if2 as a keyword; C retains an extra token from discarded or split text.

**Common misconception:** Keyword recognition depends on lexical context and full token boundaries.

## Q39

**Correct answer:** A, C  
**Concept:** Recovery conditions versus serializability.

T2 reads from T1 and commits after T1; T3 reads from T2 and commits after T2, so the schedule is recoverable. Both reads occur before the producing transaction commits, so it is neither cascadeless nor strict. Conflict edges are T1→T2→T3 with no cycle. Thus A,C hold and B,D fail.

**Common misconception:** Recoverability permits dirty reads if commit dependencies are respected; cascadelessness does not.

## Q40

**Correct answer:** C  
**Concept:** Read timestamps in timestamp ordering.

After the read, RTS(x)=10 while WTS(x)=0. T5's write has timestamp 5<RTS(x), meaning a later transaction already read a value that would have preceded this write in timestamp order. T5 must abort. A ignores that read; B misuses the obsolete-write exception; D destroys the recorded ordering information.

**Common misconception:** Thomas's rule does not authorize ignoring a violation of the read-timestamp check.

## Q41

**Correct answer:** A, B, D  
**Concept:** Page replacement histories and the stack property.

FIFO fills 1,2,3; hits 1; replaces 1 by 4; hits 2; replaces 2 by 5: five faults. LRU's hit on 1 makes 2 least recent; 4 evicts 2, the next 2 evicts 3, and 5 evicts 1: six faults. A,B hold. One example cannot establish C. LRU's resident sets are nested as frame capacity grows, proving D.

**Common misconception:** A replacement policy with the stack property need not beat every other policy on every individual trace.

## Q42

**Correct answer:** C  
**Concept:** Comparison lower bounds with partial order information.

There are C(6,3)=20 possible interleavings preserving both run orders. A binary comparison tree needs depth at least ceil(log₂20)=5. Standard merging compares until one run empties and uses at most five comparisons, attaining the bound. A and B cannot distinguish twenty orders; D is not minimal.

**Common misconception:** Known sorted runs reduce the possibilities from 6!, but do not eliminate uncertainty about their interleaving.

## Q43

**Correct answer:** 4  
**Concept:** Relational axioms as graph constraints.

The relation is a simple undirected graph with degree two at every vertex and no triangle. One or two vertices cannot provide two distinct neighbours; three vertices force a triangle. A four-cycle has degree two, is symmetric and irreflexive, and any two-edge path has nonadjacent endpoints (including a return to its start). Thus four is attainable and minimal.

**Common misconception:** The quantified condition includes repeated variables, so irreflexivity must remain consistent with length-two return walks.

## Q44

**Correct answer:** 6  
**Concept:** Carry-lookahead path delays.

Propagates arrive at time 2 and generates at time 1. The expanded carry products involving propagates arrive by time 3; the final OR produces c1–c4 by time 4. In particular c3 can arrive at 4, so s3's final XOR finishes at 6; s1 and s2 have the same upper bound. s0 is ready at 4 and c4 at 4. Latest output time is 6.

**Common misconception:** Expanding carry logic removes the ripple chain, but the final sum XOR still adds delay after carry generation.

## Q45

**Correct answer:** B  
**Concept:** Probe-cycle length and coprimality.

The cycle length is 12/gcd(h2,12). It equals twelve exactly for h2=1,5,7,11. Four of eleven equally likely choices qualify, giving 4/11. A uses twelve rather than eleven choices; C counts non-coprime steps; D ignores short cycles.

**Common misconception:** A nonzero second hash is insufficient when the table size is composite.

## Q46

**Correct answer:** 8  
**Concept:** Remembering a fixed suffix and distinguishability.

Store the last three bits, padding the initial history with zeros, giving eight states; accept when its oldest bit is 1. This rejects lengths below three. Every three-bit history is reachable. Two different histories differ at some position; append zero, one or two zeros so that the differing position becomes third from the right. Exactly one resulting word is accepted. All eight states are distinct residuals.

**Common misconception:** An NFA can guess the relevant 1, but a DFA must retain all relevant suffix possibilities simultaneously.

## Q47

**Correct answer:** B  
**Concept:** Saturation versus modular overflow.

S saturates 7+3 to 7, then adds −5 to obtain 2. W represents 10 as signed −6, then wraps −6−5=−11 to signed 5. Thus (2,5). A delays saturation until the end; C fails to wrap the second W addition; D reports intermediate values.

**Common misconception:** Applying overflow rules after each operation differs from applying them only to the final exact result.

## Q48

**Correct answer:** 20  
**Concept:** Encoded control fields.

The independent signals need twelve bits. Including “none,” the groups have 5,6,4 choices and need ceil(log₂5)=3, ceil(log₂6)=3 and log₂4=2 bits. Total 12+3+3+2=20.

**Common misconception:** A group needs a distinct code for inactivity as well as each active signal.

## Q49

**Correct answer:** A, B, C  
**Concept:** Row dependence, null space, and consistency.

Row 1 minus twice row 2 plus row 3 is zero, so rank is at most 2. The upper-left 2×2 minor has determinant 1, making rank exactly 2 (A). Direct multiplication sends (1,−2,1)ᵀ to zero; nullity is one, so this vector spans the null space (B). The same dependence requires b1−2b2+b3=0. It is sufficient because the first two independent equations can be solved and the third is then their combination (C). Adding any multiple of the nonzero null vector to a solution gives another solution, disproving D.

**Common misconception:** Consistency and uniqueness are separate conditions; a nontrivial null space rules out uniqueness.

## Q50

**Correct answer:** D  
**Concept:** Longest-prefix fallback after withdrawal.

160 lies in the withdrawn /17 but outside the surviving /18, so it falls back to the /16 via B. 200 remains inside the /18, so uses D. A skips valid more-specific routes; B retains the withdrawn route; C ignores the surviving /18.

**Common misconception:** Withdrawing a prefix does not withdraw its more-specific routes.

## Q51

**Correct answer:** A, C  
**Concept:** Directory links versus open-file references.

An open descriptor keeps the unlinked file available until the reference is released, proving A and refuting B. Removed pathnames no longer resolve to it, proving C. Open descriptors are not directory hard links; the hard-link count is zero, refuting D.

**Common misconception:** Removing a name is not necessarily the same as immediately destroying the referenced data.

## Q52

**Correct answer:** A, C  
**Concept:** Continuity and oscillating difference quotients.

|f(x)|≤|x| proves continuity. Its difference quotient at zero is sin(1/x), which has no limit, so B is false. For g, the quotient x sin(1/x) tends to zero, proving C. For x≠0, g′(x)=2x sin(1/x)−cos(1/x), which fails to approach g′(0)=0, so D is false.

**Common misconception:** Existence of a derivative at a point does not imply continuity of the derivative there.

## Q53

**Correct answer:** B  
**Concept:** Rapidly growing loop indices and dominant work.

The i values are 2,4,16,…,2^(2^(k−1))=√n; the next value equals n and is excluded. Work equals the sum of these indices. The last term gives a √n lower bound, and preceding terms decrease at least geometrically, giving an O(√n) upper bound. A counts only outer iterations; C includes the excluded n-sized iteration; D multiplies two inappropriate bounds.

**Common misconception:** The number of outer iterations is not the total cost when their bodies have sharply different sizes.

## Q54

**Correct answer:** A, C, D  
**Concept:** Counter recovery and output waveforms.

States 6 and 7 enter 0 after one edge, proving A and refuting B. On states 0–5, q2=1 only for 4 and 5, two out of six intervals, proving C. The low bit has sequence 0,1,0,1,0,1 before returning to 0, proving D.

**Common misconception:** The physical number of state bits does not force a cycle containing all eight bit patterns.

## Q55

**Correct answer:** 11  
**Concept:** Range–precision tradeoff.

Round-to-nearest error is at most half an LSB, 2^(−f−1). Requiring at most 0.01 gives f≥6; f=5 would allow 1/64>0.01. With six fractional bits, positive maximum is (2^(w−1)−1)/64. Covering 15 requires 2^(w−1)≥961, hence w≥11. Eleven bits with six fractional bits satisfy both constraints.

**Common misconception:** Meeting the error bound alone does not ensure sufficient integer range.

## Q56

**Correct answer:** A, B, D  
**Concept:** Lossy decomposition of ternary relationships.

All three original tuples survive. Their projections additionally support (s1,p1,j2): each of its three pairs appears somewhere. No other new tuple is possible: s2 has only p1 and j2, and pair (p2,j1) is absent. The join therefore has four tuples. Each original SP pair appears once and determines J. A,B,D hold; the spurious tuple itself refutes C.

**Common misconception:** Pairwise compatibility does not prove that a three-way combination occurred in the original relation.

## Q57

**Correct answer:** 0.80  
**Concept:** Tail probabilities of an independent minimum.

For integer k≥1, P(X≥k)=(2/3)^k. Independence gives P(min(X,Y)≥k)=(4/9)^k. Summing the nonnegative integer variable's tails yields E[min]=Σ_(k≥1)(4/9)^k=(4/9)/(5/9)=4/5=0.80.

**Common misconception:** The expected minimum is not the minimum of the two expectations.

## Q58

**Correct answer:** B  
**Concept:** SLR FOLLOW-based reductions.

FOLLOW(A)={a,c}. The state reached after initial d contains S→d·c and A→d·, producing a shift/reduce conflict on c. The state reached after b d contains S→bd·a and A→d·, producing one on a. A has no other completed-production state; completed S productions reduce only on end marker, with no conflicting shift. Thus exactly two states conflict. A overlooks both; C merges distinct prefix states; D introduces an extra conflict unsupported by an item set.

**Common misconception:** SLR applies the entire FOLLOW set at a completed item, even where a more context-specific LR lookahead would be narrower.

## Q59

**Correct answer:** C  
**Concept:** Shared open-file offsets after dup.

fd1 and fd2 share an open-file description and offset; fd3 does not. The first reads advance the shared offset to 3 and fd3's offset to 1. Seeking fd2 to 1 also sets fd1's offset to 1. Its final two-byte read returns bc. A ignores the seek; B resets to zero; D starts at offset two.

**Common misconception:** Descriptor identity is different from the identity of the underlying open-file description.

## Q60

**Correct answer:** A  
**Concept:** NAT mapping keys.

Endpoint-dependent keys distinguish H1→S1, H1→S2 and H2→S1: three. Endpoint-independent keys distinguish only H1:5000 and H2:5000: two. A is correct. B reverses the policies, C unnecessarily splits the independent mapping, and D merges H1's two dependent destinations.

**Common misconception:** Equal private port numbers do not merge different private hosts, while destination dependence may split one host-port pair.

## Q61

**Correct answer:** 32  
**Concept:** Coupled recursion and a two-step invariant.

Substitute twice: f(n)=2f(n−2) and g(n)=2g(n−2). For even n=2k, f(n)=2^k f(0). Hence f(10)=2⁵=32. The simultaneous recurrence must use both previous values, not a newly updated one.

**Common misconception:** Sequentially updating the two quantities can accidentally implement a different recurrence.

## Q62

**Correct answer:** 4096  
**Concept:** Partial address decoding and aliases.

Only twelve address bits reach the chip, so it contains 2¹²=4096 physical bytes. Within the selected 16 KiB window, varying the ignored two bits creates four aliases per byte, not four independent copies. For example 0x8123,0x9123,0xA123,0xB123 select the same physical byte.

**Common misconception:** The address window's size can exceed actual device storage when decoding is incomplete.

## Q63

**Correct answer:** 7  
**Concept:** Balanced parentheses with a depth bound.

A nonempty primitive balanced block of maximum depth at most two has the form '(' followed by k copies of '()' then ')', contributing k+1 pairs. Every depth-at-most-two string decomposes uniquely into such blocks. Thus strings with four pairs correspond to compositions of 4, of which there are 2³=8. Exactly one, ()()()(), has maximum depth one. Subtract it to obtain seven with depth exactly two.

**Common misconception:** Counting all balanced strings ignores the nesting-depth restriction; counting depth at most two still includes depth one.

## Q64

**Correct answer:** A, C, D  
**Concept:** Marked reversal languages and closure.

A deterministic PDA pushes the symbols before #, then compares and pops them after #; a final state indicates exactly matched input, proving A. Intersecting L with 0*#0* gives {0^n#0^n}, which is nonregular by the pumping lemma, so L cannot be regular and B is false. CFLs are closed under homomorphisms, including erasing #, proving C. In 0*#1*, the left word contains only zeros while its reversal must contain only ones, forcing both empty; D follows.

**Common misconception:** A visible midpoint enables deterministic stack switching, but does not make unbounded matching a finite-state task.

## Q65

**Correct answer:** 13  
**Concept:** Syntax-directed attributes for reversed positional value.

Successive (v,p) pairs are (1,2),(1,4),(5,8),(13,16),(13,32). Each new bit receives the next power of two rather than shifting the accumulated value left. Final v=13, the value of reversed bit string 01101.

**Common misconception:** Scanning left to right does not force ordinary most-significant-bit-first interpretation; the attribute equations determine the weights.

