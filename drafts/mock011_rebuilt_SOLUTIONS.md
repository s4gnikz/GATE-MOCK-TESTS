# GATE CS 2027 — Mock 011: Worked Solutions

## Q1

**Correct answer:** A

**Concept:** Reconciling aggregate and subgroup changes.

If some existing visits move later, evening attendance rises while the daily total stays constant, so A is consistent. B directly contradicts the unchanged daily total. C contradicts the unchanged total when evening attendance rises. D asserts an error without evidence.

**Common misconception:** Interpreting growth in one time segment as growth in the whole day.

## Q2

**Correct answer:** 10

**Concept:** Choosing nonadjacent positions.

For reserved indices i<j<k, map them to i,j−1,k−2. Nonadjacency makes these three distinct increasing positions in {1,…,5}. Conversely each such triple reconstructs a valid reservation set. Thus the count is choose(5,3)=10.

**Common misconception:** Subtracting adjacent pairs independently when their overlaps matter.

## Q3

**Correct answer:** 4

**Concept:** Weighted profit percentages.

If each item costs one unit, profit is 40×0.25−60×0.10=4 units on total cost 100. The overall profit is 4%.

**Common misconception:** Taking the unweighted average of 25% and −10% despite different quantities.

## Q4

**Correct answer:** A

**Concept:** Unfolding as reflection.

Folding superposes a point and its reflection across the crease, so the punch produces that reflected pair. A holds. The punch is away from the fold, refuting B. Separation depends on distance from the fold, refuting C. A general reflected pair is not a quarter-turn pair, refuting D.

**Common misconception:** Replacing reflection by rotation.

## Q5

**Correct answer:** A

**Concept:** Cause, intermediate effect, observation, interpretation.

Q disconnects power; S describes the lost signal; P is the alarm response; R interprets the test. B places the response first, C begins with a consequence before its cause, and D states the conclusion before the observed result. A gives the causal order.

**Common misconception:** Ignoring the events referred to by “then” and “this”.

## Q6

**Correct answer:** 0.2432

**Concept:** Conditional binomial probability.

With k correct answers the score is 3k−(3−k)=4k−3, positive exactly when k≥1. P(k=2)=choose(3,2)(1/4)²(3/4)=9/64. P(k≥1)=1−(3/4)³=37/64. Their ratio is 9/37=0.243243…, rounding to 0.2432. Accepted range: 0.24315–0.24325.

**Common misconception:** Conditioning on at least two correct answers instead of deriving the score threshold.

## Q7

**Correct answer:** A

**Concept:** Contextual meaning and limited claims.

The passage explicitly uses “economical” for efficient use of components, making A correct. It does not establish low cost (B), no components (C), or necessarily higher cost (D).

**Common misconception:** Converting a statement about resource efficiency into an unsupported price claim.

## Q8

**Correct answer:** 3.23

**Concept:** Compound growth equivalence.

The three-year factor is 1.25×0.8×1.1=1.1. A constant annual rate r must satisfy (1+r)³=1.1, giving 100r=100(1.1^(1/3)−1)=3.228011…%. Rounded answer 3.23; accepted range 3.225–3.235.

**Common misconception:** Averaging annual percentage changes arithmetically.

## Q9

**Correct answer:** C

**Concept:** Comparison groups and causal uncertainty.

A shared external factor is compatible with both decreases, so C states the justified limitation. A attributes the whole effect without isolating causes; B claims exact absence of an effect without adequate evidence; D extrapolates a universal relationship from one period.

**Common misconception:** Replacing an unsupported positive causal claim with an equally unsupported zero-effect claim.

## Q10

**Correct answer:** 12

**Concept:** Painted cuboid edges.

Exactly-two-face cubes occur along edges excluding corners. Four edges parallel to the length contribute 4(4−2)=8, four parallel to width contribute 4(3−2)=4, and four parallel to height contribute 4(2−2)=0. The total is 12.

**Common misconception:** Counting corner cubes, which have three painted faces.

## Q11

**Correct answer:** A, C

**Concept:** Undirected DFS edge structure.

Undirected DFS has tree and ancestor–descendant non-tree edges; cross edges between completed unrelated subtrees would have discovered the second subtree while exploring the first. This establishes A and refutes B. The undirected parent edge appears again in adjacency traversal and is not a separate cycle, proving C. DFS need not visit by distance layers, so D is false.

**Common misconception:** Applying directed DFS cross-edge categories unchanged to undirected graphs.

## Q12

**Correct answer:** B

**Concept:** Thread-private execution state and shared memory.

Separate stacks do not isolate shared heap storage, so unsynchronized accesses can race: B. A incorrectly infers isolation; C conflates sharing memory with sharing register state; D describes a private-copy mechanism that ordinary threads do not provide.

**Common misconception:** Treating all data accessed by a thread as private because its stack is private.

## Q13

**Correct answer:** 0.6667

**Concept:** Odd/even symmetry in integration.

x cos x is odd, so its integral on [−1,1] vanishes. The remaining integral is 2∫₀¹x²dx=2/3=0.666666…, rounding to 0.6667. Accepted range: 0.66665–0.66675.

**Common misconception:** Integrating both terms laboriously without using symmetry, or treating their sum as wholly odd.

## Q14

**Correct answer:** A

**Concept:** Aligned prefix aggregation.

The adjacent third octets 4 and 5 differ only in the last bit and form an aligned pair. Their common prefix yields 10.0.4.0/23, A. B and D include additional /24 blocks. C has host bits set and is not the aligned network-address notation of the requested block.

**Common misconception:** Aggregating by adjacency without checking prefix alignment.

## Q15

**Correct answer:** -1

**Concept:** BST deletion by inorder successor.

Node 3 has right child 6, whose left child is 4. The successor of 3 is therefore 4. Copying 4 into node 3's position and removing the old leaf 4 leaves node 6 without a left child. The specified absent-child answer is −1.

**Common misconception:** Removing the entire successor subtree rather than just its old node.

## Q16

**Correct answer:** A

**Concept:** Necessary versus sufficient conditions.

The pumping property is necessary for regularity, so its failure implies nonregularity, proving A. Its converse is not supplied by the lemma, refuting B. Infinite regular languages such as a* refute C. Every sufficiently large bound also works once a pumping length works, refuting D.

**Common misconception:** Reversing a one-way implication.

## Q17

**Correct answer:** 5

**Concept:** Recovering a missing observation before sorting.

The total must be 5×6=30. Known observations sum to 25, so x=5. The sorted list is 2,4,5,8,11, whose middle entry is 5.

**Common misconception:** Using the mean as the median without reconstructing the data.

## Q18

**Correct answer:** A, C

**Concept:** Blocking message-queue operations.

A receive frees capacity and may enable a sender, giving A. A blocked process need not spin, giving C. Applications can deadlock through cyclic waits even with bounded queues, so B is false. Finite capacity directly refutes D.

**Common misconception:** Mistaking a useful synchronization mechanism for a guarantee of application-wide progress.

## Q19

**Correct answer:** 2

**Concept:** Memory bank selection.

Four chips are needed: 64/16=4. Each chip uses fourteen internal address bits for its 16 KiB locations. The full memory needs sixteen address bits, leaving two to select one of four chips.

**Common misconception:** Confusing data width with address depth.

## Q20

**Correct answer:** A, B

**Concept:** Right inverses throughout a monoid.

For a, choose b with ab=e. Choose c with bc=e. Associativity gives a=a(bc)=(ab)c=c, hence ba=bc=e. Thus every a has a two-sided inverse, establishing A and the group property B. Groups need not commute (C false), and inverses must satisfy the equations rather than being arbitrary (D false, as any nontrivial group illustrates).

**Common misconception:** Assuming one-sided inverses remain one-sided when the inverse-existence condition applies to every element.

## Q21

**Correct answer:** C

**Concept:** Joining constant-propagation facts.

Both 4 and 7 can reach B, so no single constant describes all executions at entry. C holds. A or B would exclude a feasible path; D is false because each path assigns x.

**Common misconception:** Selecting one predecessor's fact instead of merging all feasible predecessors.

## Q22

**Correct answer:** 100

**Concept:** NAT connection-identification capacity.

There are 40099−40000+1=100 ports. All other translated endpoint fields are fixed by the question, so each live connection needs one distinct port; the limit is 100.

**Common misconception:** Omitting an endpoint in an inclusive interval or assuming unspecified public addresses can be used.

## Q23

**Correct answer:** 5

**Concept:** Hit lookup plus conditional miss penalty.

Every access costs two ns; a fraction 0.05 additionally costs 60 ns. The mean is 2+0.05×60=5 ns.

**Common misconception:** Charging the miss penalty on every access or excluding the cache lookup on a miss.

## Q24

**Correct answer:** A

**Concept:** Truth-table synthesis.

The possible values are 0,1,2,3. Exactly 2 and 3 are prime, and both have a=1, so A realizes the required function. B includes 1 and excludes 2; C includes 1 and excludes 3; D excludes prime 2.

**Common misconception:** Treating 1 as prime.

## Q25

**Correct answer:** A, C

**Concept:** Dead assignments and liveness.

A states precisely that the assigned value cannot be observed on any outgoing path. With a pure, nontrapping right-hand side, the assignment can be removed. C is the corresponding liveness criterion. B provides a path that may need the value; D has no semantic relevance.

**Common misconception:** Removing an assignment that is unused on only some paths.

## Q26

**Correct answer:** B

**Concept:** Availability of expressions after operand redefinition.

p contains the product using the old a, while q uses the input value, which may differ. B explains why the expression is no longer available for reuse. A is an incorrect universal prohibition, C is not implied, and D contradicts the first assignment.

**Common misconception:** Matching expression text without tracking its operands' reaching values.

## Q27

**Correct answer:** 12

**Concept:** Cache address decomposition.

There are 4096/64=64 lines, requiring six index bits. A 64-byte line needs six offset bits. The remaining 24−6−6=12 bits form the tag.

**Common misconception:** Counting the total data bytes as the number of cache lines.

## Q28

**Correct answer:** B

**Concept:** Enumeration without an end-of-output signal.

A correct enumerator must eventually print every member and no nonmember; it need not announce exhaustion. It can keep testing strings forever after its last output, so B holds. A adds an unjustified termination test; C confuses enumeration duration with membership decidability; D is refuted by an enumerator that never prints.

**Common misconception:** Requiring finite languages to have enumerators that halt after their last member.

## Q29

**Correct answer:** 2

**Concept:** Articulation vertices.

Removing c separates the a,b edge from d,e. Removing d separates e from the triangle. Removing a or b leaves a connected path through the other triangle vertices; removing endpoint e also leaves a connected graph. Exactly c,d qualify.

**Common misconception:** Equating all vertices incident on cycle edges with articulation points.

## Q30

**Correct answer:** 2

**Concept:** Heap insertion path.

The new 1 occupies index 7, whose parent at index 3 contains 3. Swap once, then compare with the root 2 and swap again. Two exchanges suffice and produce root 1.

**Common misconception:** Comparing with adjacent array entries rather than parent indices.

## Q31

**Correct answer:** A, C

**Concept:** Unique-light-edge cut property.

If an MST omitted e, adding e creates a cycle containing another crossing edge. That crossing edge is heavier because e is uniquely minimum; replacing it gives a lighter spanning tree, contradiction. Thus A and C hold. An MST may cross the cut through several edges, refuting B. A triangle with distinct edge weights supplies a cut-minimum edge that is not a bridge, refuting D.

**Common misconception:** Assuming an MST must cross every cut exactly once.

## Q32

**Correct answer:** 3

**Concept:** Set difference, intersection, and union.

R−S={1,3} and S∩T={4}. Their union is {1,3,4}, containing three tuples.

**Common misconception:** Treating set union as concatenation with duplicates, or reversing the difference.

## Q33

**Correct answer:** A

**Concept:** Asynchronous reset priority.

Asserting an asynchronous reset changes Q independently of a clock edge, so A holds even while the clock remains low. B describes synchronous reset, C incorrectly substitutes toggling, and D is unrelated to reset behaviour.

**Common misconception:** Applying the normal data-sampling edge condition to an asynchronous control.

## Q34

**Correct answer:** A

**Concept:** Universal quantification with a domain restriction.

A requires Works(e,d) for each d that is a department, while not constraining other domain objects. B requires merely one department. C demands that every domain object be a department and assigned, which is too strong. D expresses no assignments. If Department is empty, A correctly holds vacuously for every employee.

**Common misconception:** Using conjunction instead of implication to restrict a universal quantifier.

## Q35

**Correct answer:** 78

**Concept:** Inclusion–exclusion for forbidden fixed points.

Begin with 5!=120. Subtract 4!=24 for each of the forbidden events π(1)=1 and π(2)=2, then add 3!=6 for their intersection. The result is 120−24−24+6=78.

**Common misconception:** Subtracting the overlap twice without restoring it.

## Q36

**Correct answer:** 1

**Concept:** Outer joins and NULL-sensitive aggregates.

The joined rows contain B.v values 5,NULL,NULL,NULL: two matches for id 1, one match for id 2, and a null-extended row for id 3. COUNT(B.v) counts only the single non-NULL value, giving one. COUNT(*) would instead count four.

**Common misconception:** Counting outer-join rows when a nullable expression is the aggregate argument.

## Q37

**Correct answer:** B

**Concept:** Mutual exclusion versus progress.

Both can set their flag before either checks the other's flag, leaving both spinning forever. Progress therefore fails. Mutual exclusion still holds: a thread entering has its own flag true, preventing the other from passing its test until that flag is cleared after the critical section. B captures both facts. A overlooks the preceding writes, C overlooks the deadlocking interleaving, and D invents a turn variable.

**Common misconception:** Treating absence of simultaneous entry as a complete synchronization proof.

## Q38

**Correct answer:** 2

**Concept:** Longest-match tokenization and keyword priority.

Tokens are identifier(ifx), <, keyword(if), =, =, identifier(x). The longer ifx is not split into a keyword and identifier; the standalone if wins the equal-length tie. There are two identifiers.

**Common misconception:** Giving keyword priority before applying longest match.

## Q39

**Correct answer:** 2

**Concept:** Path enumeration with a negative DAG edge.

The three paths are s–a–t of weight 8, s–b–t of weight 4, and s–a–b–t of weight 3. The latter two meet the threshold, giving two. A negative edge is allowed without any cycle because the graph is acyclic.

**Common misconception:** Counting only shortest paths when a threshold includes multiple path weights.

## Q40

**Correct answer:** A, C, D

**Concept:** Graph representation costs.

The full matrix has n² entries regardless of m, proving A. Without extra indexing, finding a row's neighbours scans n entries, so B is false for small degrees. A list traversal costs its entries plus constant access overhead, proving C. Lists contain n headers and 2m edge entries, proving D.

**Common misconception:** Assuming an adjacency matrix can skip zero entries without an additional structure.

## Q41

**Correct answer:** 6

**Concept:** Strict inversions in stable insertion sort.

The leading 4 forms inversions with all four later elements. The 3 forms two more with the later 1 and 2. No other inversions exist; equal 1 values are not shifted past one another. Each strict inversion causes one shift, for six shifts.

**Common misconception:** Counting equal-valued pairs as inversions in a stable implementation.

## Q42

**Correct answer:** 7

**Concept:** Counting compositions with a parity constraint.

There can be zero, one, or two size-3 steps. The even possibilities are zero and two. Zero gives the all-one sequence. Two threes leave two ones, and arranging this multiset gives 4!/(2!2!)=6 sequences. Total 1+6=7.

**Common misconception:** Counting unordered step counts rather than ordered step sequences.

## Q43

**Correct answer:** 1

**Concept:** Window limits after acknowledgment processing.

The acknowledgment reduces outstanding data from six to four MSS. The active window is min(cwnd,rwnd)=min(10,5)=5 MSS. Therefore at most 5−4=1 additional MSS may be sent.

**Common misconception:** Using the old receive window or forgetting to subtract data still in flight.

## Q44

**Correct answer:** A

**Concept:** Completion, complementation, and state distinguishability.

The original language is a^k for k≥2. Add a dead state for every missing b transition, with self-loops on both symbols. Complementing accepting states gives a complete four-state DFA. The four original-language states corresponding to prefixes ε,a,aa,b are distinguishable: a separates ε from a; ε separates aa from ε or a; and an appropriate a-suffix separates b from each nondead prefix. Complementation preserves distinguishability. Thus four is minimal; B is too small and C,D exceed the exhibited minimum.

**Common misconception:** Complementing the accepting set of a partial DFA without first representing rejecting undefined transitions.

## Q45

**Correct answer:** A, B

**Concept:** Removing necessary deadlock conditions.

A imposes one resource order and rules out a circular wait. B prevents hold-and-wait because an unsuccessful acquisition holds neither resource. C changes scheduling priority but cannot supply the blocked resource. D explicitly allows the original hold-and-wait cycle. Thus only A and B guarantee prevention here.

**Common misconception:** Expecting CPU scheduling changes to resolve a resource cycle.

## Q46

**Correct answer:** 958200

**Concept:** CPU overhead under different I/O mechanisms.

Interrupt-driven cost is 12000×80=960000 cycles. DMA uses twelve blocks, costing 12(120+30)=1800 cycles. Savings are 960000−1800=958200 cycles.

**Common misconception:** Omitting per-block setup or counting DMA completion interrupts per byte.

## Q47

**Correct answer:** 6

**Concept:** Grammar generation and distinct terminal strings.

Each nonempty production introduces one a and one b, so length-four strings must have two of each: there are at most choose(4,2)=6. All six are generated: aabb via a(S=ab)b(S=ε); abab via a(S=ε)b(S=ab); abba via a(S=ε)b(S=ba); and their symbol-swapped versions bbaa,baba,baab using the second production. Thus the count is six regardless of ambiguity.

**Common misconception:** Counting parse trees or assuming the balance condition alone proves all balanced strings are generated.

## Q48

**Correct answer:** A, B

**Concept:** Foreign keys versus uniqueness and participation.

The primary key is cid, so multiple distinct child rows can share a parent, proving A. A non-NULL foreign key must find a referenced parent, proving B. No constraint forces parents to have children, so C is false. A foreign key need not be unique, refuting D.

**Common misconception:** Importing the referenced key's uniqueness into the referencing column.

## Q49

**Correct answer:** B

**Concept:** SLR actions from items and FOLLOW sets.

S→L·=R prescribes a shift on '='. The completed R→L· prescribes a reduction on every symbol in FOLLOW(R), including '='. Both actions enter the same cell, creating the shift–reduce conflict B. A ignores the reduction rule, C requires a second completed production, and D confuses ordinary completion with the augmented start acceptance item.

**Common misconception:** Using LR(1) item-specific lookahead reasoning in an SLR table built from FOLLOW sets.

## Q50

**Correct answer:** A, C

**Concept:** Quantifier order and nonempty domains.

A common witness y works for every x and therefore supplies a witness for each x, proving A. C follows by choosing any y in the nonempty domain. B fails for equality on {0,1}: each x has its own equal y, but no y equals both. D fails for a relation containing only (0,0) on that domain, because x=1 lacks a witness.

**Common misconception:** Moving an existential quantifier across a universal one without changing its permitted dependence.

## Q51

**Correct answer:** 2

**Concept:** Candidate-key closure and minimality.

C never appears on a dependency's right-hand side, so every key must contain C. It must also contain A or B: without either, neither can be derived. AC determines B and D, while BC first determines A and then D. Both are minimal. Every other key contains one of these, so exactly two candidate keys exist.

**Common misconception:** Counting nonminimal superkeys as candidate keys.

## Q52

**Correct answer:** 30

**Concept:** Product scaling in fixed-point arithmetic.

The represented values are 24/16 and 20/16. Their product has raw integer numerator 480 and scale 256. To return to scale 16, divide 480 by 16, giving encoded integer 30 exactly. No rounding adjustment is necessary in this case.

**Common misconception:** Retaining the doubled fractional-bit scale as if it were the destination format.

## Q53

**Correct answer:** 11

**Concept:** Pipeline completion plus load-use stalls.

Five instructions in five stages take 5+5−1=9 cycles without stalls. The first load's consumer adds one stall, and the second load's immediate consumer adds another. The intervening ALU dependencies are forwarded, including the address dependency into the second load. Total 11 cycles.

**Common misconception:** Stalling for ALU dependencies already covered by forwarding, or omitting one load-use penalty.

## Q54

**Correct answer:** 5

**Concept:** Linear probing across tombstones.

The four inserted keys occupy slots 3,4,5,6. Deleting 17 makes slot 4 a tombstone. Search for 31 begins at 3 and inspects 3,4,5,6,0, stopping at never-used slot 0. The tombstone cannot terminate the search because colliding keys may lie beyond it. Five slots are inspected.

**Common misconception:** Treating a deleted slot as indistinguishable from a never-used slot during search.

## Q55

**Correct answer:** B

**Concept:** Listening versus connected sockets.

Accept returns connected sockets with their own lifetimes. Closing the listening socket stops accepting new connections through it but does not itself close c1,c2, proving B and refuting A. No descriptor is automatically promoted to a listener (C), and the established connections retain separate byte streams (D).

**Common misconception:** Treating all accepted connections as the same socket as the listener.

## Q56

**Correct answer:** 0

**Concept:** Rounding and loss of a small addend.

Near 16, four-bit precision has spacing two. The exact sum 17 lies midway between 16=1.000₂×2⁴ and 18=1.001₂×2⁴. Ties-to-even selects 16. Adding −16 then gives zero exactly. In contrast, a different grouping can retain a different result, illustrating nonassociativity.

**Common misconception:** Performing both additions exactly and rounding only once at the end.

## Q57

**Correct answer:** 76

**Concept:** Array strides and lower-bound adjustment.

The final dimension has three elements, and the middle dimension four. Adjusted indices are 0−(−1)=1, 4−2=2, and 1−0=1. The linear element offset is (1×4+2)×3+1=19, giving 19×4=76 bytes.

**Common misconception:** Using raw indices without subtracting nonzero lower bounds.

## Q58

**Correct answer:** 6

**Concept:** Preemptive shortest-remaining-time scheduling.

Run J1 on [0,1), J2 on [1,2), J3 on [2,3), J2 on [3,6), then J1 on [6,12). Waiting times from completion−arrival−burst are J1:12−0−7=5; J2:6−1−4=1; J3:3−2−1=0. Total six.

**Common misconception:** Comparing original burst lengths rather than remaining lengths after preemption.

## Q59

**Correct answer:** 7936

**Concept:** Expanding opcodes and instruction-space accounting.

Type A uses 32×2⁶=2048 instruction patterns. The remaining 65536−2048=63488 patterns can be grouped into eight patterns per Type B opcode, one for each register. Thus at most 63488/8=7936 opcodes fit. This bound is achievable: A uses 32 ten-bit prefixes; each of the other 992 ten-bit prefixes can be extended by three bits to form eight thirteen-bit Type B opcodes, giving 992×8=7936.

**Common misconception:** Counting unused opcodes without reserving all register combinations for each opcode.

## Q60

**Correct answer:** 26

**Concept:** Pointer-to-pointer updates and alias redirection.

Initially q points to p and p points to a. The first update changes a from 4 to 6. Assigning *q=r redirects p to b. The second update changes b from 7 to 10, so *p is also 10. The printed sum is 6+10+10=26.

**Common misconception:** Assuming changing a local parameter cannot update the caller's pointer when its address was passed.

## Q61

**Correct answer:** 3

**Concept:** Consistency after combining dependent variables.

Put u=x+z. The distinct equations become u+ty=1 and tu+y=0. Their determinant is 1−t². For t≠±1 they have a solution, and x,z can split u arbitrarily. At t=1 the same left side would equal both 1 and 0; at t=−1 one equation's left side is the negative of the other's, but the right sides are incompatible. The consistent integer values are −2,0,2: three.

**Common misconception:** Declaring every singular coefficient matrix inconsistent, or failing to inspect the singular cases separately.

## Q62

**Correct answer:** 5

**Concept:** Persistent HTTP scheduling with a connection limit.

The initial handshake consumes RTT 1 and the HTML consumes RTT 2. During RTT 3 the existing connection fetches image 1 while the second connection opens. During RTT 4 both connections fetch images 2 and 3. RTT 5 fetches image 4. This is optimal: by time 4 only one image can complete on the first connection during RTT 3 and two during RTT 4, so at most three images could be done. The fourth requires a fifth RTT.

**Common misconception:** Treating the second connection as already available when the images are first discovered.

## Q63

**Correct answer:** A, C, D

**Concept:** Equivalent NPDA acceptance conventions through conversion.

Final-state acceptance can be converted using a new protected bottom symbol and an epsilon cleanup phase after an old final state. Empty-stack acceptance can be converted using a bottom marker and a new final state reached on detecting the emptied original stack. With full input consumption required, these constructions preserve languages, establishing A,C,D. An unchanged machine can have a final state with nonempty stack, or empty its stack in a nonfinal state, so B is false.

**Common misconception:** Confusing equivalence of language families with equivalence of conventions on an unchanged machine.

## Q64

**Correct answer:** 19

**Concept:** Counting a pruned recursion tree.

Nonleaf levels handle positions 1 through 5. Their call counts are 1,2,3,5,8: a prefix ending in exclusion allows two next choices; one ending in inclusion allows only exclusion. This yields the Fibonacci recurrence for successive prefix counts. Sum 1+2+3+5+8=19. The thirteen final output calls are leaves and are excluded.

**Common misconception:** Counting a full binary tree despite pruning adjacent selections.

## Q65

**Correct answer:** 3

**Concept:** Continuity required before derivative matching.

Differentiability implies continuity, so the left limit b must equal f(0)=1. The right derivative of e^(2x) at zero is 2. The left derivative of ax+b is a, hence a=2. Therefore a+b=3.

**Common misconception:** Matching slopes while neglecting the function-value continuity condition.

