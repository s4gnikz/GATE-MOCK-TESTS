# GATE CS 2027 — Mock 006: Worked Solutions

Use the NAT precision and accepted ranges in the question paper's final answer key.

## Q1

**Correct answer:** B  
**Concept:** Necessary conditions.

“Only registered participants may enter” means permitted entry implies registration, which is B. It does not promise a seat, so A is false. A registered person might be denied a seat, making C unsupported. D contradicts the entry restriction.

**Common misconception:** A necessary eligibility condition is not a guarantee of availability.

## Q2

**Correct answer:** 3.2  
**Concept:** Successive dilution.

Each withdrawal removes 2/10 of the alcohol currently present; adding water does not replace alcohol. The retained fraction per operation is 0.8. After two operations, alcohol volume is 5×0.8²=3.2 litres.

**Common misconception:** The second withdrawal has a lower alcohol concentration than the first.

## Q3

**Correct answer:** B  
**Concept:** Ordering constraints.

A must precede B, and B must precede C, so B can be neither first nor last. A can be first in A,B,D,C. C can be last in that same order. D can be first in D,A,B,C. Thus A,C,D do not meet the stated condition, and B does.

**Common misconception:** Not every position must be uniquely determined to exclude both extreme positions for a runner.

## Q4

**Correct answer:** A, C  
**Concept:** Orientation under isometries.

Rotations preserve orientation, so A holds. A single reflection reverses it, refuting B. Two reflections reverse orientation twice, preserving it, so C holds. Translation preserves orientation, but the one reflection in D reverses it, making D false.

**Common misconception:** Preserving lengths does not imply preserving clockwise versus counterclockwise orientation.

## Q5

**Correct answer:** B  
**Concept:** Concession in sentence structure.

The acceptance occurs despite a concern; “notwithstanding” supplies that concessive meaning and takes the following noun phrase. “Because” would require a different grammatical construction here and changes the intended relation. “Therefore” and “consequently” express consequence, not concession, and do not fit before this noun phrase. B is correct.

**Common misconception:** A word can signal a logical relation without fitting the grammatical structure of the blank.

## Q6

**Correct answer:** 45  
**Concept:** Overall average speed including idle time.

Total elapsed time is 180/40=4.5 hours. The first 90 km takes 90/45=2 hours, and the stop takes 0.5 hour. The second part therefore takes 2 hours, giving speed 90/2=45 km/h.

**Common misconception:** Average speed uses total elapsed time, including the stop specified in the question.

## Q7

**Correct answer:** B  
**Concept:** Inclusion–exclusion with a restricted denominator.

One hundred people read at least one paper. Intersection size is 70+60−100=30. Exactly-one readership is 100−30=70. The requested fraction among the 100 readers is 70/100=7/10. B is correct; A counts both-paper readers, while C,D use incorrect counts or denominators.

**Common misconception:** “Among those who read at least one” changes the denominator from the full survey size.

## Q8

**Correct answer:** 18  
**Concept:** Boundary tracing of overlapping shapes.

The outer polygon can be traced through (0,0),(4,0),(4,1),(6,1),(6,3),(2,3),(2,2),(0,2). Its successive side lengths are 4,1,2,2,4,1,2,2, summing to 18. The portions hidden inside the overlap are not part of the outer boundary.

**Common misconception:** Adding the separate rectangle perimeters counts internal boundary segments.

## Q9

**Correct answer:** 4  
**Concept:** Tournament totals and a deficit invariant.

There are C(6,2)=15 matches. A decisive match contributes three points in total, whereas a draw contributes two. With no draws the total would be 45; each draw lowers it by one. Thus 45−41=4 matches were drawn.

**Common misconception:** A drawn match awards one point to each of two teams, not one point in total.

## Q10

**Correct answer:** 4  
**Concept:** Conditional sample space.

The ten qualifying ordered outcomes are (1,2),(2,1), …, (5,6),(6,5), all equally likely. Each possible maximum 2,3,4,5,6 occurs twice. Its conditional mean is (2+3+4+5+6)/5=4.

**Common misconception:** The conditioning event changes which dice outcomes are relevant; the unconditional expected maximum does not apply.

## Q11

**Correct answer:** A, C  
**Concept:** Tagged translations and stale mappings.

Different ASIDs distinguish P's and Q's translations, so switching need not flush P's entries (A). Both ASID and virtual page number are needed to identify a particular translation, refuting B. Recycling an ASID may make old entries falsely match a new address space, so invalidation may be required (C). Changing a mapping can still make a tagged entry stale, refuting D.

**Common misconception:** Tags avoid unnecessary context-switch flushes but do not make stale entries correct.

## Q12

**Correct answer:** 60  
**Concept:** Collision-detection round-trip bound.

The worst return time is twice 2.4 microseconds, or 4.8 microseconds. At 100×10⁶ bits/s, that duration transmits 480 bits. Dividing by eight gives 60 bytes. The question explicitly ignores other standard-specific minimum-frame rules.

**Common misconception:** Use round-trip propagation time, not just one-way propagation time.

## Q13

**Correct answer:** 3  
**Concept:** Antichains and a chain-cover upper bound.

The set {4,5,6} is an antichain, establishing a lower bound of three. Partition the entire poset into chains {1,2,4}, {3,6}, and {5}. Any antichain contains at most one member of each chain, giving an upper bound of three. The maximum is exactly three.

**Common misconception:** Exhibiting a large antichain alone does not prove it is largest; an upper bound is also needed.

## Q14

**Correct answer:** 12  
**Concept:** Minimizing a quadratic under linear constraints.

Let x=y=t, so z=6−2t. Then x²+y²+z²=2t²+(6−2t)²=6(t−2)²+12. The minimum is 12, achieved at (2,2,2).

**Common misconception:** Satisfying the linear equations leaves a family of solutions; the quadratic objective selects one.

## Q15

**Correct answer:** C  
**Concept:** Three-way partitioning on repeated keys.

The initial partition scans n keys in Θ(n). Every key falls into the equal part, leaving both recursive parts empty. No further nontrivial partition is performed. C is correct. A,B ignore the initial scan, and D assumes repeated recursive handling of equal keys, which this variant explicitly avoids.

**Common misconception:** Quicksort's behaviour on equal keys depends on the specified partition scheme.

## Q16

**Correct answer:** A, C, D  
**Concept:** Reachability and residual-language equivalence.

The strings ε,a,b,ab reach p,q,r,s, respectively, proving A. From either p or q, acceptance occurs exactly when a future suffix contains b; they are equivalent, so B is false. r and s accept every suffix and are equivalent (C). Before the first b the machine alternates between p and q; after a b it stays in an accepting sink, proving D.

**Common misconception:** Distinct reachable states need not remain distinct after minimization.

## Q17

**Correct answer:** A  
**Concept:** Redundant dependencies in a minimal cover.

A→C follows transitively from A→B and B→C, so it can be removed. Neither remaining dependency follows from the other, and their single-attribute left sides have no extraneous attributes. A is a minimal cover. B cannot derive A→B; C cannot derive B→C; D lacks a singleton right-hand side and cannot derive B→C either.

**Common misconception:** Preserving A's closure alone does not preserve dependencies with other determinants.

## Q18

**Correct answer:** 1  
**Concept:** NAND realization of exclusive OR.

Evaluating inputs 00,01,10,11 gives y=0,1,1,0. OR gives 0,1,1,1. The results differ only at 11, hence one assignment. Equivalently, the four-NAND network implements XOR.

**Common misconception:** XOR and OR differ at the all-one input even though they agree at three of four assignments.

## Q19

**Correct answer:** B  
**Concept:** Handles in bottom-up parsing.

The stack suffix id matches T→id and must first become T. The stack then becomes E+T, permitting E→E+T. B is the next step. A reduces a right-hand side not yet present; C reverses a production in the wrong direction on the wrong symbol; D ignores reductions that remain after all tokens have been shifted.

**Common misconception:** Exhausting input does not imply that parsing is finished; reductions may still be necessary.

## Q20

**Correct answer:** 702  
**Concept:** TCP sequence space.

SYN uses 400, data use 401 through 700, and FIN uses 701. Acknowledgment names the next expected sequence number, 702. Equivalently, compute 400+1+300+1.

**Common misconception:** SYN and FIN consume sequence numbers despite not being ordinary application data bytes.

## Q21

**Correct answer:** A, C  
**Concept:** Expression kills and a must-analysis join.

Changing c does not change either operand, so the first predecessor preserves availability (A). Assigning a invalidates the previously computed value of a+b on the second path, refuting B. The must join intersects predecessor facts and therefore omits the expression (C). Union could falsely reuse a value on the second path, so D is unsound.

**Common misconception:** Having evaluated an expression somewhere earlier is insufficient if an operand was subsequently assigned.

## Q22

**Correct answer:** 2816  
**Concept:** Cache addressing fields and metadata.

There are 4096/32=128 lines, requiring seven index bits. A line offset takes five bits. The tag therefore takes 32−7−5=20 bits. Adding valid and dirty bits gives 22 metadata bits per line, or 128×22=2816 bits overall.

**Common misconception:** Cache data capacity excludes tag and status storage unless explicitly stated otherwise.

## Q23

**Correct answer:** C  
**Concept:** Regular restriction of a nonregular language.

The intersection in C contains only a³b³, a finite regular language. A is the standard nonregular equal-count language. B equals L itself because all members already have a*b* form. If D were regular, complementing it would make L regular, a contradiction. Only C is regular.

**Common misconception:** Intersecting a nonregular language with a regular one can yield a regular result.

## Q24

**Correct answer:** B  
**Concept:** Arithmetic versus logical shifts.

11111011 represents −5. Arithmetic right shift gives 11111101, which is −3; logical right shift gives 01111101, which is 125. B matches. A assumes truncation toward zero for the arithmetic shift; C,D fail to insert zero at the high bit for the logical shift.

**Common misconception:** Arithmetic right shift of a negative odd integer rounds toward negative infinity, unlike truncating integer division in some languages.

## Q25

**Correct answer:** 3  
**Concept:** Postorder expression translation.

The parenthesized sum yields `a b +`; unary minus then appends `neg`; multiplication appends `c *`. The full sequence is `a b + neg c *`, leaving three tokens before neg.

**Common misconception:** A unary operator in postfix still follows its entire operand expression, not merely the first identifier.

## Q26

**Correct answer:** 30  
**Concept:** Coloring a cycle.

For a cycle of length n, the number of labelled q-colorings is (q−1)ⁿ+(−1)ⁿ(q−1). Taking n=5,q=3 gives 2⁵−2=30. One derivation fixes the first color and tracks whether the current path endpoint equals that color: if E_k,D_k are counts, E_{k+1}=D_k and D_{k+1}=2E_k+D_k, starting E_1=1,D_1=0. This gives D_5=10, and multiplying by three first-color choices gives 30.

**Common misconception:** Coloring a path and then forgetting the closing edge overcounts cycle colorings.

## Q27

**Correct answer:** B  
**Concept:** Parity composition.

The first gate computes a XOR b and the second computes (a XOR b) XOR c. This is 1 for one or three input ones, exactly odd parity. B holds. A excludes three ones incorrectly; C is a majority function; D includes 000 even though XOR there is 0.

**Common misconception:** Three-input XOR is not “exactly one input is 1.”

## Q28

**Correct answer:** 0.3466  
**Concept:** Integration by substitution.

Set u=1+x², so du=2x dx. The integral becomes (1/2)∫₁² du/u=(ln 2)/2≈0.3465735903, which rounds to 0.3466.

**Common misconception:** The substitution introduces a factor of one-half and changes both limits.

## Q29

**Correct answer:** 1.160  
**Concept:** Identifying a binomial parameter.

The equality is (1−p)⁴=6p²(1−p)². Since 0<p<1, cancel (1−p)² and take positive square roots: 1−p=√6 p. Thus p=1/(1+√6), and E[X]=4p≈1.159591794, rounding to 1.160.

**Common misconception:** A binomial probability includes the combinatorial factor C(4,2)=6.

## Q30

**Correct answer:** A, B, D  
**Concept:** Substitution into a sequential characteristic equation.

For J=K=0, Q′=Q, proving A. For J=K=1, Q′=NOT Q, proving B. For J=1,K=0, Q′=(NOT Q)+Q=1, so C is false. For J=0,K=1, both terms vanish, so D is true.

**Common misconception:** Force-set and force-reset inputs must be checked against the specified characteristic equation.

## Q31

**Correct answer:** B  
**Concept:** Process creation versus image replacement.

fork creates the child. Its successful exec replaces the child's current program image while retaining its process identity, so B holds. A confuses exec with process creation; C changes the wrong process; D describes a return to the old program, which does not occur after a successful exec.

**Common misconception:** Launching a new program image need not create a new process.

## Q32

**Correct answer:** A  
**Concept:** Reconstructing a binary tree from traversals.

Preorder selects A as root; inorder splits its left labels D,B,E and right labels C,F. The left subtree has root B with children D,E; the right has root C with right child F. Postorder is D,E,B,F,C,A. Only A matches; B visits B before completing its left subtree, and C,D misorder or mix the two subtrees.

**Common misconception:** Preorder identifies each subtree's root, while inorder determines which labels belong to each side.

## Q33

**Correct answer:** A  
**Concept:** Counting shortest paths across BFS layers.

The layers are {s}, {a,b}, {c,d}, {t}, so the shortest length is three. The numbers of shortest paths to a,b are 1,1; to c,d they are 1,2; and to t the sum is 1+2=3. Equivalently, the paths are s-a-c-t, s-a-d-t, and s-b-d-t. A is correct. B counts only the two predecessors of t, C miscounts layers as edges, and D counts a nonexistent route through b-c.

**Common misconception:** A BFS parent tree stores one witness path per vertex, not necessarily all shortest paths.

## Q34

**Correct answer:** A, C  
**Concept:** Domain independence in relational calculus.

E1 is exactly the fixed tuples of R, so enlarging an external domain adds nothing to it (A). E2 contains all domain values not in R; any new domain value enters it, proving C and refuting B. E1 need not include domain values absent from R, refuting D.

**Common misconception:** Unrestricted negation can make a query depend on values not stored in the database.

## Q35

**Correct answer:** 15  
**Concept:** Static storage across recursive and successive calls.

During f(2), the three local a values are 1,2,3, yielding x=6. The static k remains 3. During f(1), the values are 4,5, yielding y=9. The printed sum is 15. Each invocation's local a retains its own value while k is shared across calls.

**Common misconception:** A static local is initialized once, not once per invocation or once per top-level call.

## Q36

**Correct answer:** 4  
**Concept:** Packet scheduling when paths diverge.

On S→R, A occupies 0–1 ms, B 1–2, and C 2–3. On R→D, A occupies 1–2; B does not use this link. C is unavailable until time 3, so it occupies 3–4. Arrival completes at 4 ms.

**Common misconception:** An idle downstream link cannot forward a packet before the upstream transmission finishes.

## Q37

**Correct answer:** A, C  
**Concept:** Mutual exclusion versus progress.

Both threads can set their flags before either tests the other, after which both wait forever with flags true (A). For simultaneous entry, both would need to read the other's flag false after setting their own true. Sequential consistency cannot order those four events that way: whichever thread sets its flag first prevents the other from passing once that other sets its own. Thus mutual exclusion holds (C), and B is false. Volatile alone does not change the allowed flag-setting interleaving or add a tie-breaker, refuting D.

**Common misconception:** Mutual exclusion does not imply deadlock freedom or progress.

## Q38

**Correct answer:** 5  
**Concept:** Counting trees with required and forbidden edges.

K4 has 4²=16 spanning trees, each with three edges. By symmetry each of six edges belongs to 16×3/6=8 trees. Trees containing both AB and AC already connect A,B,C; D may attach by AD,BD,or CD, giving three trees. Thus trees containing AB but not AC number 8−3=5. The subtraction concerns the intersection of the required and forbidden conditions.

**Common misconception:** Required edges sharing a vertex do not behave like independent events in a uniformly selected spanning tree.

## Q39

**Correct answer:** 1  
**Concept:** Queueing versus transmission delay.

Each packet needs 1000/10⁶ seconds=1 ms to transmit. Their start times are 0,1,2 ms, which are also their waiting times because all arrive at zero. Average queueing delay is (0+1+2)/3=1 ms. Including each packet's own transmission would instead give average completion delay 2 ms.

**Common misconception:** Queueing delay excludes the service time under the definition given.

## Q40

**Correct answer:** 50  
**Concept:** BST deletion and ancestor relationships.

The inorder predecessor of 20 is 10. Replacing 20 by 10 removes its old leaf, leaving the 30 subtree (with 25 and 35) to the right of the replacement. The inorder successor of root 40 is 50, the minimum in its right subtree. Root becomes 50 and its former leaf is removed. Node 25 remains in the left subtree, while 70 is in the right subtree, so their lowest common ancestor is the new root 50.

**Common misconception:** Key replacement affects later ancestor labels even if much of the tree's shape is unchanged.

## Q41

**Correct answer:** A, B, C  
**Concept:** Lossless BCNF decomposition versus dependency preservation.

The intersection is A, which determines R1=AB, proving losslessness (A). R1 has key A; R2 has no nontrivial projected dependency with a non-superkey determinant, so both are BCNF (B). To refute preservation of BC→A, take R1={(1,b),(2,b)} and R2={(1,c),(2,c)}. Both obey their projected dependencies, but their join contains (1,b,c),(2,b,c), violating BC→A (C). A alone cannot determine C in the original schema, so it is not a key (D is false).

**Common misconception:** Losslessness and dependency preservation are different properties.

## Q42

**Correct answer:** 17  
**Concept:** Pipeline fill/drain and nonoverlapping penalties.

Eight instructions in an ideal five-stage pipeline need 8+5−1=12 cycles. Add one load-use stall and two taken-branch penalties of two cycles each: 12+1+4=17. The explicit nonoverlap assumption makes this addition valid.

**Common misconception:** Counting only instruction issue cycles omits the four-cycle pipeline fill/drain overhead.

## Q43

**Correct answer:** B  
**Concept:** Register coloring and an odd cycle.

A five-cycle has edges but no triangle, so its largest clique has size two. Alternating two colors around the cycle forces equal colors at the closing edge, making two registers insufficient. Three suffice, for example a=1,b=2,c=1,d=2,e=3. B is correct. A misses the odd-cycle obstruction; C,D invent a triangle, and D also overallocates registers.

**Common misconception:** The maximum clique gives a lower bound on required colors, not always an exact answer.

## Q44

**Correct answer:** 17  
**Concept:** Sliding-window working sets.

The five four-reference windows are (1,2,1,3), (2,1,3,4), (1,3,4,2), (3,4,2,4), and (4,2,4,5). Their distinct-page counts are 3,4,4,3,3. The requested sum is 17.

**Common misconception:** Repeated references count once within a working set, and old pages leave when their last reference exits the window.

## Q45

**Correct answer:** A, C  
**Concept:** Boolean substitution with dependent inputs.

Substitute s=a: F=(NOT a)a+ab=ab, proving A. With a=0, F is always zero, refuting B. NAND(a,b) followed by inversion computes ab, proving C. OR differs at (a,b)=(0,1), refuting D.

**Common misconception:** A selector tied to a data input is not an independent Boolean variable.

## Q46

**Correct answer:** 1  
**Concept:** Modular arithmetic in truncated multiplication.

Keeping eight bits means 13b≡0 modulo 256. Since gcd(13,256)=1, 13 has a multiplicative inverse modulo 256. Multiplying by that inverse gives b≡0 modulo 256. Only b=0 lies in the specified range.

**Common misconception:** A nonzero full product can wrap to zero, but only when the multiplier and modulus permit such a nonzero solution.

## Q47

**Correct answer:** 40  
**Concept:** Fixed-width rotation composed with XOR.

45 is 101101. Rotating left two places yields 110110; XOR 001111 gives 111001 (57). Rotate that left two places to obtain 100111; XOR 001111 gives 101000, which is 40. Both rotations stay within six bits.

**Common misconception:** Rotation wraps discarded high bits into low positions, whereas a shift would discard them.

## Q48

**Correct answer:** A, B, D  
**Concept:** MST structure and the next distinct weight.

AB is uniquely lightest across the cut {B}, so every MST includes it (A). Connecting C to the AB component costs at least 2, and D costs at least 3. Weight 6 is achieved by choosing AC or BC, and independently BD or CD: four trees (B). A tree using AB,AC,AD has weight 7, and integer weights permit no value strictly between 6 and 7, so C is false. AD occurs in no weight-6 tree, and increasing its weight cannot improve another tree or damage these four, proving D.

**Common misconception:** Distinct trees of minimum weight are not the same as trees of the next strictly greater weight.

## Q49

**Correct answer:** 1  
**Concept:** Canonical LR(0) state identity.

Whenever the dot is before d in C→·d, shifting d yields the singleton item set {C→d·}. Its closure adds nothing. All such transitions therefore reach the same canonical LR(0) state, regardless of how many predecessor states can shift d. Exactly one state contains this completed item.

**Common misconception:** Canonical state construction merges identical item sets; it does not create a separate state for each incoming transition.

## Q50

**Correct answer:** B  
**Concept:** A reduction must preserve a distinguishing yes/no condition.

If M halts on w, N accepts every input, so L(N)=Σ*. Otherwise N accepts none, so L(N)=∅. Both are regular, and a regularity test answers yes in either case; B identifies the failure. The construction merely simulates M and needs no advance halting knowledge, refuting A. C is the opposite of the actual outcomes, and D incorrectly forbids standard simulation.

**Common misconception:** Encoding halting into a machine's behaviour is not enough; the target property must distinguish the two cases.

## Q51

**Correct answer:** 2  
**Concept:** Amdahl's law with a target speedup.

Normalize old time to one. A speedup of 1.25 requires new time 1/1.25=0.8. If the component's speedup is s, then 0.6+0.4/s=0.8. Thus 0.4/s=0.2 and s=2.

**Common misconception:** A 25% speed increase means a 20% time reduction, not a 25% time reduction.

## Q52

**Correct answer:** B  
**Concept:** Expected distinct blocks via indicators.

For each of ten blocks, a random record request misses that block with probability 9/10. All ten requests miss it with probability (9/10)¹⁰, so its probability of being read at least once is 1−(9/10)¹⁰. Sum ten such indicators to obtain B. A ignores repeated blocks. C counts distinct records rather than blocks. D is only the probability that one specified block is never requested.

**Common misconception:** Linearity of expectation does not require the block-hit indicators to be independent.

## Q53

**Correct answer:** 27  
**Concept:** Nonadjacent selections and parity.

With length eight, an even number of ones means an even number k of zeros. Nonadjacent zeros permit k=0,2,4. The number of ways to place k nonadjacent positions among eight is C(9−k,k), obtained by compressing the compulsory gaps between zeros. Sum C(9,0)+C(7,2)+C(5,4)=1+21+5=27.

**Common misconception:** Enforcing parity alone or excluding adjacent zeros alone does not enforce both conditions together.

## Q54

**Correct answer:** A, B, D  
**Concept:** Products of rank-one projections.

Since uᵀu=vᵀv=2 and uᵀv=1, PQ=uvᵀ/4. This is a nonzero outer product and has rank one (A). Its trace is vᵀu/4=1/4 (B). Its (1,2) entry is zero while its (2,1) entry is 1/4, refuting symmetry (C). The vector u is an eigenvector with eigenvalue 1/4; the two-dimensional kernel vᵀx=0 supplies two zero eigenvalues, proving D.

**Common misconception:** Two symmetric matrices need not have a symmetric product unless they commute.

## Q55

**Correct answer:** B  
**Concept:** Longest-prefix matching before metric comparison.

The destination lies in all three explicit blocks, including /25's range 172.16.5.128–255. The /25 is the longest match and therefore wins before metrics are compared. B is correct. A applies the tie-breaker across unequal prefix lengths; C prefers the broadest rather than narrowest match; D ignores the deterministic selection rule.

**Common misconception:** A better metric on a shorter prefix does not override longest-prefix matching under the stated policy.

## Q56

**Correct answer:** A  
**Concept:** Circular-array indices and occupancy.

Initially occupancy is (2−6) mod 8=4. The operations change head/tail as follows: dequeue (7,2), enqueue (7,3), enqueue (7,4), dequeue (0,4), enqueue (0,5). Occupancy is 4−1+1+1−1+1=5, agreeing with (5−0) mod 8. A is correct; B has the right indices but inconsistent occupancy, and C,D miscount index advances.

**Common misconception:** Index wraparound does not reset queue occupancy to zero.

## Q57

**Correct answer:** 3  
**Concept:** Counting distinct optimal knapsack subsets.

With E selected, four units of capacity remain. The best addition is A+B, value 6, for total value 11. C or D adds only 4 and cannot be paired with A or B within the remaining capacity. Without E, choosing C+D leaves room for exactly one of A,B, also giving value 11 in two ways. Choosing at most one of C,D yields at most A+B+C or A+B+D, value 10. Thus the optimum is 11 and exactly ABE,ACD,BCD attain it.

**Common misconception:** Items with equal weights and values remain distinct when counting subsets.

## Q58

**Correct answer:** 0.25  
**Concept:** Comparing boundary and stationary minima.

For a≤0, f′=3(x²−a)≥0, giving a unique minimum at −1. For a≥1, f′≤0 throughout the interval, giving a unique minimum at 1 (including the boundary case). For 0<a<1, the only interior local minimum is t=√a; compare it with the endpoint −1, since the function increases from t to 1. Their values are −2t³ and −1+3t². Equality requires 2t³+3t²−1=0=(2t−1)(t+1)², so t=1/2 and a=1/4. At this value −1 and 1/2 are distinct global minimizers; elsewhere one candidate is strictly lower.

**Common misconception:** On a closed interval, comparing only stationary points can miss an endpoint global minimum.

## Q59

**Correct answer:** 32  
**Concept:** Leaf splitting and separator maintenance.

Insert 15 into the left leaf to obtain [5,10,15]. Inserting 12 overflows it to [5,10,12,15], which splits into [5,10] and [12,15]. The root separators become 12 and 20. Inserting 30 changes the last leaf to [20,25,30] without splitting or changing its minimum. The root separator sum is 12+20=32.

**Common misconception:** A leaf split promotes a separator copy; the separator key remains in the leaf under the stated B+ tree rule.

## Q60

**Correct answer:** B, C  
**Concept:** Object lifetime after function return.

A's automatic scalar and D's automatic array cease to exist when their functions return; their pointers do not permit later access to live objects. B's static object persists throughout program execution. C's allocated object persists until freed, which the question excludes before the first access. Thus B,C are valid and A,D are not.

**Common misconception:** Returning an address does not extend the lifetime of the object at that address.

## Q61

**Correct answer:** 9  
**Concept:** Exact insertion-sort comparison counting.

Inserting 1 compares against 5 once. Inserting 4 compares against 5 then 1: two comparisons. Inserting 2 compares against 5,4,1: three. Inserting 3 compares against 5,4,2: three. Total 1+2+3+3=9. Successful shifts and the final failed key comparison are both comparisons, but reaching the boundary adds no key comparison.

**Common misconception:** The number of key comparisons can exceed the number of shifts.

## Q62

**Correct answer:** 16  
**Concept:** Width and depth expansion of memory chips.

Two four-bit-wide chips in parallel provide one eight-bit byte at each of 8K addresses, making an 8 KiB bank. Eight such banks provide 64 KiB. Total chips are 2×8=16. Equivalently, total required bits divided by bits per chip gives (64×1024×8)/(8×1024×4)=16.

**Common misconception:** A chip word is four bits here, not a byte; both width and address depth must be expanded.

## Q63

**Correct answer:** A, B, D  
**Concept:** Prefix closure and recognizer dovetailing.

For a DFA of L, mark as accepting every state from which an original accepting state is reachable; the same transitions then recognize Pref(L), proving A. For recognizable L, on x dovetail recognizer runs for xy over all finite y and accept when one accepts, proving B. C is false: over {0,1}, let L={w1 0^|w|:w∈{0,1}*}. Every binary x is a prefix of x1 0^|x|, so Pref(L) is all binary strings, but L is nonregular: intersecting with 0*1 0* yields {0ⁿ1 0ⁿ}, a nonregular language. Finally, ε prefixes every word, so D holds for nonempty L.

**Common misconception:** Taking all prefixes can erase complexity; regularity of the prefix closure does not imply regularity of the original language.

## Q64

**Correct answer:** C  
**Concept:** Short-circuit control flow with side effects.

The original evaluates p exactly once; when false it skips q and assigns 2. When true it evaluates q exactly once and uses its result to choose 1 or 2. C reproduces that sequence. A changes evaluation order, B evaluates q on a previously skipped path, and D duplicates p's evaluation. Side effects make all three changes observably different on some execution.

**Common misconception:** Boolean equivalence alone does not preserve evaluation behaviour of expressions with side effects.

## Q65

**Correct answer:** A, C, D  
**Concept:** Basic versus strict two-phase locking.

Basic 2PL orders transactions consistently by their lock points and guarantees conflict serializability (A). It can still release a write lock before commit, allowing another transaction to read a value later rolled back, so B is false. Two transactions may each hold one lock while requesting the other's during their growing phases, giving deadlock (C). Keeping exclusive locks until commit prevents another transaction from acquiring a read lock on an uncommitted written item, so D is true.

**Common misconception:** Serializability, absence of cascading aborts, and deadlock freedom are separate properties.

