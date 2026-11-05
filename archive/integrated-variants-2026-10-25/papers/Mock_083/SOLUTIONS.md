# Worked Solutions — Mock Test 083

## Q1

**Correct answer:** C

Concept: scope of evidence. The report explicitly permits average passenger delay to fall while average car time rises, so C follows. A replaces averages by a claim about every traveller; B asserts an unmeasured effect; D extrapolates one corridor to all corridors. Preserve both the population and the qualifier of a reported result.

## Q2

**Correct answer:** 36

**Concept:** Positional constraints on permutations.

The specified books occupy one of three position pairs: (1,3),(2,4),(3,5). Orient the two books in two ways, then arrange the other three in 3! ways. Total 3×2×6=36.

**Common misconception:** Treating the specified books as adjacent when exactly one intervening book is required.

## Q3

**Correct answer:** B
**Concept:** Mean versus dispersion.

Reduced variability means reduced dispersion under the reported measure, so B follows. It need not eliminate all variation (A), make the unchanged mean zero (C), or establish bias relative to a true value (D).

**Common misconception:** Precision and accuracy are distinct properties.

## Q4

**Correct answer:** A

Concept: composition of reflections. Reflection across y=x swaps coordinates, giving (0,2). Reflection across x=1 changes x to 2−x, giving (2,2). A is correct. B changes the second coordinate incorrectly; C stops after the first reflection; D introduces an unwarranted vertical reflection. Reflection order matters.

## Q5

**Correct answer:** C
**Concept:** Narrative reference and causal order.

R initiates the first inspection. S refers to that inspection and identifies the defect. Q repairs the identified defect and starts the second inspection. P gives that second inspection's result. Thus R,S,Q,P is coherent. A repairs before identifying the crack; B uses the inspection reference before its introduction; D places repair and retesting before the initiating event.

**Common misconception:** Pronoun references and causal dependencies constrain order even when each sentence is grammatical alone.

## Q6

**Correct answer:** B

**Concept:** General Aptitude — Elementary probability and statistics

1. In Bag I, P(RR)=6/15 and P(same)=7/15. In Bag II, P(RR)=1/10 and P(same)=4/10.
2. Before conditioning, P(RR)=(1/2)(6/15+1/10)=1/4, and P(same)=(1/2)(7/15+4/10)=13/30.
3. Since RR is a subset of same, P(RR | same)=(1/4)/(13/30)=15/26.

- **A:** Conditioning on same does not leave red and blue equally likely.
- **B:** The ratio of the mixture probabilities is 15/26.
- **C:** This is not the ratio P(RR)/P(same).
- **D:** Conditioning cannot be replaced by the initial proportion in a bag.

**Common misconception:** Conditional probabilities from different bags cannot be averaged without updating their weights.

## Q7

**Correct answer:** C

The statement explicitly allows withdrawal before inspection and forbids it afterward, exactly C. A ignores the post-inspection restriction. B invents an exception. D confuses ending a withdrawal right with cancellation. The timing qualifies the agreement's provisional nature.

## Q8

**Correct answer:** 8

Divisibility by6 forces a≥1 and b≥1. For b=1, the bound2^a≤24 permits a=1,2,3,4. For b=2, it permits2^a≤8, giving three choices. For b=3, only a=1 works; b≥4 permits none. Unique prime factorization makes these4+3+1=8 distinct integers. The bound N≤72 does not require N to divide72.

## Q9

**Correct answer:** C

Concept: repeated ordered transformations. Reverse CAT to TAC and advance by 1,2,3 to obtain UCE. Reverse UCE to ECU and advance again to obtain FEX, C. A stops after the first application; B advances the wrong letters or positions; D does not follow the specified two-stage procedure. The position-dependent shifts must be applied after each reversal.

## Q10

**Correct answer:** 18

Four separate cubes contribute24 unit faces. Exactly three pairs share full faces: the first and second, the second and third, and the third and fourth. Each shared face removes two exposed faces, giving 24−2×3=18. Other contacts are at most along edges or vertices and remove zero surface area.

## Q11

**Correct answer:** 2

r1(x) before w2(x), and also w1(x) before w2(x), create edge T1→T2. r2(x) before w1(x) creates T2→T1. Repeated conflicts in one direction count only once, giving2 directed edges. The two reads alone do not conflict.

## Q12

**Correct answer:** 2

Offset 3072 is in logical data block 3. It is beyond the direct block, so one single-indirect pointer block and the target data block are required. Logical blocks 0,1,2 remain holes. Thus two blocks are allocated, not four data blocks.

## Q13

**Correct answer:** D
**Concept:** Chip selection and local addressing.

Each chip covers 0x1000 bytes. Chip bases are 0x8000,0x9000,0xA000,0xB000. Address 0x9ABC lies in chip 1 at offset 0xABC. A fails both the range and local-offset requirement; B chooses the next chip; C exceeds the maximum local offset 0xFFF.

**Common misconception:** Local chip addresses exclude the bits used to select the chip.

## Q14

**Correct answer:** 0.5

**Concept:** Second-order exponential behaviour.

eˣ=1+x+x²/2+O(x³). Cancellation of the constant and linear terms leaves the quotient tending to 1/2.

**Common misconception:** Using only the first-order approximation after its terms cancel.

## Q15

**Correct answer:** 16

Every binary word can be split into initial a's followed by zero or more blocks consisting of b and the run of a's immediately after it. Thus the expression denotes all words over {a,b}, and there are 2^4=16 length-four words. Repeated stars do not impose a limit on the number of b's.

## Q16

**Correct answer:** A, C

Each link supplies its own framing, so A,C are true. Its checksum must correspond to its own frame rather than blindly copying the incoming one, refuting B. Changing encapsulation does not require changing the application message, refuting D.

## Q17

**Correct answer:** C

The first assignment makes x=0, so y=b. The later x=7 does not change the previously stored y. C is correct. A incorrectly uses the later x, B ignores multiplication by zero, and D loses the contribution of b. Track definitions at their points of use.

## Q18

**Correct answer:** C

**Concept:** Joining constant-propagation facts.

Both 4 and 7 can reach B, so no single constant describes all executions at entry. C holds. A or B would exclude a feasible path; D is false because each path assigns x.

**Common misconception:** Selecting one predecessor's fact instead of merging all feasible predecessors.

## Q19

**Correct answer:** 0

Squaring either possible X gives Y=4 with probability1. A constant random variable has zero variance. Nonzero variability of X does not imply variability after a many-to-one transformation.

## Q20

**Correct answer:** A, B

The first computed x is overwritten before any read, so it is dead and removable under the no-side-effect assumptions: A,B. Only the second definition reaches return, disproving C. That reaching definition is needed, disproving D. A dead value is identified by uses, not merely by repeated assignment names.

## Q21

**Correct answer:** A, C

If f(a1)=f(a2), applying g gives a1=a2, proving injectivity(A). Every a equals g(f(a)), so g reaches all of A(C). For a counterexample to B,D, take A={0},B={0,1},f(0)=0,and g(0)=g(1)=0. The stated identity holds, but f misses1 and f(g(1))=0≠1. A left inverse does not force a two-sided inverse.

## Q22

**Correct answer:** 3

**Concept:** Image contained in kernel for a square-zero map.

A²=0 implies im(A)⊆ker(A). If rank is r, rank–nullity gives r≤6−r, so r≤3. Three independent 2×2 nilpotent blocks with rows (0,1),(0,0) attain rank three, proving the maximum.

**Common misconception:** Concluding A itself must be zero merely because A² is zero.

## Q23

**Correct answer:** B

**Concept:** IPv4 subnet boundaries.

A /27 leaves five host bits and covers addresses 96 through 127. The last address is broadcast, so the highest host is 126. A is broadcast, C lies outside the subnet, and D is valid but not highest.

**Common misconception:** Assigning the all-one host field to a host.

## Q24

**Correct answer:** D

Substitute z=y: F=xy+(NOT x)y=y(x+NOT x)=y. Thus D is correct. A depends on an unrelated selector, B complements the required value, and C changes with x. When a multiplexer's two data inputs agree, its selector cannot affect its output.

## Q25

**Correct answer:** A, C

**Concept:** Rolle's theorem and compact-interval extrema.

Rolle's theorem gives A, while continuity on the closed bounded interval gives C. Nonconstant examples such as 1+x(2−x) refute B. To refute D, use 1+x(x−2)(x+1): its endpoint values are one but its derivative at one is nonzero.

**Common misconception:** Assuming Rolle's point must be the midpoint.

## Q26

**Correct answer:** B

**Concept:** Inherited descriptors and open file descriptions.

Both descriptors refer to the same open file description, which contains the current offset. B is correct. A describes separately maintained execution state, C incorrectly makes ordinary stack storage shared, and D contradicts the distinct process identities created by fork.

**Common misconception:** Equating a copied descriptor table with separately opened files.

## Q27

**Correct answer:** A, C, D

**Concept:** Programming and Data Structures — Binary search trees

With a nonempty right subtree, the successor is its minimum-key node, found by following left-child links from x's right child. It therefore lies in that subtree and has no left child. It can have a right child: for root 10 with children5,15 and node15 having right child 20, the successor of 10 is 15. Hence A,C,D hold and B fails.

- **A:** True: successor is the minimum of the nonempty right subtree.
- **B:** False: the minimum node can have a right child.
- **C:** True: a left child would have a smaller key in that same subtree.
- **D:** True: a right child does not violate minimality in the right subtree.

**Common misconception:** The successor's lack of a left child does not make it necessarily a leaf.

## Q28

**Correct answer:** 2

Using the first S production i times and the first T production j times gives a^i b^j a^j b^(2i), of length3i+2j. Nonnegative solutions to3i+2j=6 are(i,j)=(0,3),(2,0), producing bbbaaa and aabbbb. They are distinct, so the count is2. Different derivation stages contribute different amounts to total length.

## Q29

**Correct answer:** A, B, D
**Concept:** Traversal reconstruction.

Preorder gives root A. A is first in inorder, so it has no left subtree. Repeating the argument gives a right-only chain A→B→C→D (A,B). Postorder visits that chain backward, D,C,B,A (D). C describes the opposite chain and contradicts inorder.

**Common misconception:** Equal preorder and inorder sequences do not indicate a balanced tree.

## Q30

**Correct answer:** 768

The two successful calls have written768+512=1280 bytes. The remainder is2048−1280=768. A partial return reports progress rather than a requirement to restart from the original buffer; retries must advance the pointer and reduce the requested length.

## Q31

**Correct answer:** 5

Packet1 arrives completely at1 ms and occupies the output from1 to3 ms. Packet2 arrives completely at2 ms, waits until3, and leaves at5. Store-and-forward reception and output queuing must both be counted.

## Q32

**Correct answer:** 2

Concept: BFS queue timing. Processing s enqueues a,b. Dequeue a, leaving [b]; enqueue c, giving [b,c]. Just before enqueuing d, the queue therefore has two vertices. Vertices already processed are not still queued.

## Q33

**Correct answer:** A, C
**Concept:** Blocking versus busy waiting.

A blocked reader can be descheduled, requiring no polling CPU work (A). A writer's successful operation may enable it to resume (C). The writer's ability to make progress refutes necessary system deadlock (B), and it does not require the reader to be executing (D).

**Common misconception:** A blocked process is not synonymous with a deadlocked system.

## Q34

**Correct answer:** 3 (exact)

**Concept:** Databases — ER model

1. Project is identified by (dept_id, project_code), because project_code alone may repeat.
2. Task adds its own partial key, giving (dept_id, project_code, task_no).
3. Dropping any attribute can merge allowed distinct tasks, so all three are necessary.

**Common misconception:** A weak owner can itself have a composite identifying key.

## Q35

**Correct answer:** C

**Concept:** Consensus term and static hazards.

When b=c=1, the function should stay1 while a changes. Unequal delays can briefly make both original product outputs0. The term bc is continuously1 during the transition and covers that gap. It is logically redundant: whenever bc=1, either a=1 makes ab=1 or a=0 makes(NOT a)c=1. Thus C removes this hazard without changing the function. A and D incorrectly turn the function on at a=b=c=0. B incorrectly turns it on at a=1,b=c=0. They also do not provide the required stable cover during the specified transition.

**Misconception:** Equating Boolean equivalence with identical transient circuit behaviour.

## Q36

**Correct answer:** 0.21484375

A valid even-parity word remains valid exactly when an even number of bits flips. Excluding no change, the possibilities are two or four flips. Their total probability is C(4,2)(1/4)²(3/4)²+(1/4)^4=54/256+1/256=55/256=0.21484375. The undetected-error probability excludes the zero-error event.

## Q37

**Correct answer:** B
**Concept:** Bayesian updating of a hidden Bernoulli source.

The likelihoods of exactly two successes are 3(1/4)²(3/4)=9/64 and 3(1/2)³=24/64. Multiplying by priors gives relative weights 9 and 48, so posterior probabilities are 3/19 and 16/19. The predictive success probability is (3/19)(1/4)+(16/19)(1/2)=35/76. A ignores the posterior mixture; C is the posterior probability of source I rather than a trial success; D is not the posterior-weighted value.

**Common misconception:** Trials are independent conditional on the hidden source, not necessarily unconditionally.

## Q38

**Correct answer:** 2

Stack height begins at1, increases by1 on a and decreases by1 on b. An accepted length-five word needs two a's and three b's, with the height positive at every proper prefix. The only such words are aabbb and ababb. Other permutations empty the stack too early, preventing further input consumption. Final count balance alone is insufficient.

## Q39

**Correct answer:** A, C

The device's memory update need not replace a noncoherent CPU cache entry, so A is possible and C can be necessary. DMA completion does not supply the excluded coherence guarantee, disproving B. Physical sharing and coherence are distinct properties, making D false.

## Q40

**Correct answer:** B
**Concept:** Prediction penalties and clock-period tradeoffs.

Old CPI is 1+0.20×0.60×3=1.36, giving 1.36 ns per instruction. New CPI is 1+0.20×0.10×3=1.06, with time 1.06×1.1=1.166 ns. Speedup is 1.36/1.166≈1.166. B is closest. A reverses the comparison; C ignores the longer clock; D treats the new execution time as 1 ns per instruction.

**Common misconception:** Improving CPI can be partly offset by a longer clock period.

## Q41

**Correct answer:** 1.5
**Concept:** Optimal BST comparison cost.

With b at the root, cost is 0.5×1+(0.2+0.3)×2=1.5. With a at the root, the best right subtree puts b above c, costing 0.2+2×0.5+3×0.3=2.1. With c at the root, the best left subtree puts b above a, costing 0.3+2×0.5+3×0.2=1.9. The remaining shapes are worse within those root choices, so 1.5 is optimal.

**Common misconception:** Minimizing height alone does not account for nonuniform search probabilities.

## Q42

**Correct answer:** 2

First read the pointer at1012; its value2040 supplies the second read's address for the operand. Thus two data-memory reads are required. Address arithmetic itself is not a memory read, and the operand's four bytes are one specified word read here.

## Q43

**Correct answer:** 3

C×Required is empty. Subtracting R and projecting still gives the empty set, and C−empty=C. Thus u,v,w all qualify by vacuous satisfaction of all required courses. Restricting candidates to students appearing in R would incorrectly exclude w from this explicitly defined query.

## Q44

**Correct answer:** 2

Dijkstra extracts a at tentative distance1 and sets t to2. It then extracts t before b, reporting2. The actual path s→b→a→t costs4−5+1=0, and the other paths cost2 or14, so the shortest distance is0. Difference2−0=2. The negative edge invalidates the assumption behind early finalization.

## Q45

**Correct answer:** A, C, D

Threads in one process share its virtual address space and conventional descriptor table, so A and C are true and B false. Each thread still needs a separate execution context and ordinarily a separate stack, making D true. Shared resources require synchronization; sharing does not imply identical instruction pointers or stack contents.

## Q46

**Correct answer:** A

**Concept:** Direction of heap-order repair.

Decreasing a key cannot make it exceed a child that was previously at least its old value. It can become smaller than its parent, requiring upward repair, A. B reverses the direction; C exaggerates the local violation; D ignores the parent relation.

**Common misconception:** Applying the same repair direction to both increasing and decreasing keys.

## Q47

**Correct answer:** A, B, D
**Concept:** MST structure and the next distinct weight.

AB is uniquely lightest across the cut {B}, so every MST includes it (A). Connecting C to the AB component costs at least 2, and D costs at least 3. Weight 6 is achieved by choosing AC or BC, and independently BD or CD: four trees (B). A tree using AB,AC,AD has weight 7, and integer weights permit no value strictly between 6 and 7, so C is false. AD occurs in no weight-6 tree, and increasing its weight cannot improve another tree or damage these four, proving D.

**Common misconception:** Distinct trees of minimum weight are not the same as trees of the next strictly greater weight.

## Q48

**Correct answer:** A, C

**Concept:** Reversal matching versus copying.

Even palindromes are context-free: a PDA can guess the midpoint and match the second half by stack reversal, proving A. The copy language is not context-free. Intersecting it with 0*1*0*1* gives matching separated zero and one blocks; the word 0^p1^p0^p1^p cannot satisfy every CFL pumping requirement because a length-p window cannot change both separated copies of each affected block while retaining their equalities and order. This refutes B. On the unary alphabet the copy language is exactly (00)*, proving C. CFLs are not closed under general CFL intersection, refuting D.

**Common misconception:** Assuming a stack can compare a second copy in the same order as easily as a reversed copy.

## Q49

**Correct answer:** 3

The first three sends fill the three slots. The fourth finds no capacity and blocks before completing, so three have completed. Counting attempted sends would give four, which is not the requested quantity.

## Q50

**Correct answer:** 1

The graph is connected with five vertices and five edges. Its real signed incidence matrix has rank n−1=4, so rank-nullity gives kernel dimension5−4=1. The triangle supplies the single independent cycle; the edges to4 and5 do not add cycles. Arbitrary edge orientation changes signs, not rank.

## Q51

**Correct answer:** B, C

An intervening write to the pointed-to object can change the repeated expression's value, proving C and disproving A. A valid no-modification proof restores availability and allows reuse, so B is true. Calls can have memory effects, making D false. Source-level repetition is insufficient without effect analysis.

## Q52

**Correct answer:** 1

For(1,1), y=1 has outgoing second values1 and2, including2≠x, so reject. For(1,2), R(2,2) supplies z=2≠1, so reject. For(2,2), the only z is2=x, so accept. For(3,1), both z=1,2 differ from3, so reject. Exactly one tuple survives. The inner lookup is on the outer y value, not on its x.

## Q53

**Correct answer:** 0

**Concept:** Meet/join compatibility in a divisor lattice.

For positive integers, gcd(x,12)lcm(x,12)=12x. The requested values force 6×72=12x, hence x=36. But gcd(36,12)=12, not 6. Therefore no element satisfies both requirements, and the count is zero. In prime-exponent terms, the requested gcd has exponent one of 2 while 12 has exponent two, forcing x's exponent to one; their lcm could then not have exponent three of 2 as 72 does.

**Common misconception:** Treating the product identity as sufficient without checking the separate gcd and lcm constraints.

## Q54

**Correct answer:** B
**Concept:** DISTINCT aggregates and NULL exclusion.

Department A has two distinct non-NULL salaries {10,20} and sum 40; both predicates hold. Department B has one distinct non-NULL salary {20} and sum 20; neither predicate holds. Therefore only A is returned, option B. A omits a qualifying group, C selects the failing group, and D includes both.

**Common misconception:** COUNT(DISTINCT salary) ignores NULL, and SUM still counts repeated non-NULL rows.

## Q55

**Correct answer:** A, C

After signal(full), the consumer can pass its wait and read while the producer is paused before writing, proving A. Atomic operations do not reorder the intervening ordinary write, refuting B,D. Publishing full only after writing ensures that this signal cannot authorize an early read, proving C under the stated one-producer, one-consumer ordering. Synchronization operations must surround the data access in the correct order.

## Q56

**Correct answer:** D
**Concept:** Lexer states and longest match.

The tokens are string literal "if", keyword if, and identifier if2. The comment is discarded. The string's content is not tokenized as source code, and longest match keeps if2 as one identifier. Thus one keyword and three total tokens. A counts comment/string text as keywords; B counts if2 as a keyword; C retains an extra token from discarded or split text.

**Common misconception:** Keyword recognition depends on lexical context and full token boundaries.

## Q57

**Correct answer:** 3

**Concept:** Gaussian elimination multipliers.

The first-column multipliers are L21=4/2=2 and L31=8/2=4. After eliminating column one, row two is (0,1,1) and row three (0,3,5). The next multiplier is L32=3/1=3, leaving final U33=2.

**Common misconception:** Computing a second-stage multiplier from the original, uneliminated matrix entries.

## Q58

**Correct answer:** 4

The root can split at either plus sign. Splitting at the first leaves three operands with two operators on the right, admitting two binary parenthesizations. Splitting at the last similarly admits two on the left. These are disjoint cases, yielding4. Splitting at the multiplication yields the fifth possible parse tree, which is excluded by the root requirement. No unstated precedence convention applies.

## Q59

**Correct answer:** A

Concept: switch learning followed by forwarding. First learn A→3 and forward to known B→2. Then B's frame to A goes to 3. C's frame to unknown D floods to 1,2,4, excluding ingress 3. Finally learn D→4 and forward to known C→3. A lists these sets. B retains A's stale entry; C floods back onto ingress; D assumes an unknown D location and then ignores known C. Learning uses the source, lookup uses the destination.

## Q60

**Correct answer:** B
**Concept:** Runs versus accepted strings.

An accepting run must eventually take q→r on the sole symbol a. Before doing so it may traverse the ε-cycle any finite number of times. Thus only a is accepted, but it has infinitely many finite accepting runs (B). A confuses runs with words; C never reaches final r without reading a; D incorrectly treats nondeterminism as forcing an infinite cycle.

**Common misconception:** Nondeterministic acceptance needs one finite accepting run; nonaccepting infinite alternatives do not prevent it.

## Q61

**Correct answer:** 0.6817 (range 0.68165–0.68175)

Concept: integrating an upper envelope. The crossing r in [0,1] solves r²=1−r, so r=(sqrt(5)−1)/2. The maximum is 1−x on [0,r] and x² on [r,1]. Integral=r−r²/2+(1−r³)/3. Using r²=1−r and r³=2r−1 reduces it to (5sqrt(5)−3)/12=0.6816949906…. Round to 0.6817; range 0.68165–0.68175. Integrating one branch over the entire interval would miss where the larger function changes.

## Q62

**Correct answer:** 9

Before failure X chooses Z at cost5+0=5, while Y's advertised7 is consistent with cost2 to X plus X's5. After the X–Z link fails, the stored alternative is2+7=9 via Y. That information is stale and creates a route pointing back toward X, but the stipulated distance-vector calculation still advertises9. Reasoning from actual current reachability rather than the stored advertisement would miss the specified protocol behaviour.

## Q63

**Correct answer:** 40
**Concept:** Fixed-width rotation composed with XOR.

45 is 101101. Rotating left two places yields 110110; XOR 001111 gives 111001 (57). Rotate that left two places to obtain 100111; XOR 001111 gives 101000, which is 40. Both rotations stay within six bits.

**Common misconception:** Rotation wraps discarded high bits into low positions, whereas a shift would discard them.

## Q64

**Correct answer:** B

**Concept:** Programming and Data Structures — C programming and pointers

In the first call, t points to a[0], and assigning *p=q changes the caller's p to a+1. The next statement makes a[0]=2+5=7, and the last makes a[1]=6. In the second call, t points to a[1], while the caller's p changes back to a. Therefore a[1]=6+7=13 and then a[0]=8. The final offset p-a is 0.

A omits the last increment of a[0]. B matches the trace. C fails to follow the second call's target changes. D is false: each side effect occurs in a separate full expression, all pointers stay within the valid array, and no incompatible-type access occurs.

- **A:** False: omits the final increment of a[0].
- **B:** True: the program prints 8 13 0.
- **C:** False: fails to track pointer target reassignment across function calls.
- **D:** False: all pointer arithmetic and side effects are within valid bounds and fully sequenced without undefined behavior.

**Common misconception:** Saving the pointer value in t preserves its old target even when a pointer-to-pointer argument changes the caller's p.

## Q65

**Correct answer:** A

**Concept:** Digital Logic — Combinational circuits

Fixing bc=00 leaves at most two ones, so I0=0. Fixing bc=01 or 10 supplies one one, so both a and d must be one: I1=I2=ad. Fixing bc=11 supplies two ones, so either a or d suffices: I3=a+d. This is Shannon decomposition with respect to the select variables.

- **A:** True: the four cofactors are 0, ad, ad, a+d.
- **B:** False: for bc=01, a=1,d=0 it outputs 1 with only two ones; for bc=11,a=1,d=0 it also misses a required 1.
- **C:** False: for bc=00,a=d=1 it outputs 1 despite only two ones; bc=11,a=d=0 is another false positive.
- **D:** False: bc=01,a=d=1 has three ones and must yield 1.

**Common misconception:** MUX data inputs are cofactors, not the select variables themselves.

