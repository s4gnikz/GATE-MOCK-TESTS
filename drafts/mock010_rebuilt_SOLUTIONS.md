# GATE CS 2027 — Mock 010: Worked Solutions

## Q1

**Correct answer:** C

**Concept:** Vocabulary in context.

The following clause explicitly attaches a condition to the endorsement, establishing C. A is a different meaning of “qualified” and is not supported here. B removes the condition, while D denies the support that the sentence explicitly reports.

**Common misconception:** Choosing a familiar dictionary meaning without checking its context.

## Q2

**Correct answer:** 64

**Concept:** Changing logarithm bases.

Put y=log₂x. Then log₄x=y/2, so 3y/2=9 and y=6. Therefore x=2⁶=64.

**Common misconception:** Treating logarithms with different bases as equal terms.

## Q3

**Correct answer:** B

**Concept:** Induction versus universal deduction.

The observations support a tentative pattern restricted to the observed circumstances, as B says. A generalizes across every route and bus; C makes an unsupported dry-weather claim; D treats association as proof of a unique cause. None of those stronger claims follows.

**Common misconception:** Turning repeated observations into a logically necessary universal statement.

## Q4

**Correct answer:** 54

**Concept:** Surface changes under removal.

The original area is 6×3²=54. Each corner removal removes three exterior unit faces and exposes three previously internal faces. No two removed corner cubes share a face, so these changes do not overlap. The net area change is zero.

**Common misconception:** Subtracting the old external faces without adding newly exposed faces.

## Q5

**Correct answer:** 32

**Concept:** Successive increments.

Six terms require five increments: 2,3,5,7,11. Thus the sixth term is 4+2+3+5+7+11=32.

**Common misconception:** Applying six increments to obtain the sixth term.

## Q6

**Correct answer:** 2

**Concept:** Area constraints with an internal border.

For width w, the planted area is (40−2w)(30−2w)=1200−264=936. This gives w²−35w+66=0, or (w−2)(w−33)=0. Only w=2 satisfies the required width less than 15.

**Common misconception:** Using the outer perimeter times width without subtracting corner overlaps.

## Q7

**Correct answer:** C

**Concept:** Reference and causal sequencing.

R introduces the result and competing explanations. P's “these explanations” refers back to them and introduces the repeat. Q describes that repeat's outcome; S states the ensuing conclusion. Thus R–P–Q–S is required. A uses an unresolved reference, B reports the repeat before introducing it, and D places the conclusion before its grounds.

**Common misconception:** Ordering sentences by vocabulary alone instead of their logical dependencies.

## Q8

**Correct answer:** 19.2

**Concept:** Repeated dilution.

Each withdrawal removes one fifth of the salt currently present. The initial three litres of salt therefore become 3×(4/5)²=1.92 litres in a restored total volume of ten litres. The percentage is 19.2.

**Common misconception:** Removing the same amount of salt on both withdrawals despite dilution.

## Q9

**Correct answer:** 10

**Concept:** Interleaving ordered chains.

Choose three of five positions for A,B,C; their order in those positions is forced. D,E fill the remaining two in their forced order. The number is choose(5,3)=10.

**Common misconception:** Multiplying by permutations within chains whose order is fixed.

## Q10

**Correct answer:** 16

**Concept:** Reflection when unfolding.

Undoing the horizontal fold yields y=2 and y=6. Undoing the vertical fold yields x=1 and x=7. The four holes are (1,2),(1,6),(7,2),(7,6), so their x-coordinates sum to 16.

**Common misconception:** Reflecting about the coordinate axes instead of the actual fold lines.

## Q11

**Correct answer:** 20.5

**Concept:** Expected successful sequential search cost.

There are 1000/25=40 equally populated blocks, making the target block uniform among positions 1 through 40. Expected reads are (1+40)/2=20.5.

**Common misconception:** Using half the block count without the endpoint correction for a successful search.

## Q12

**Correct answer:** B

**Concept:** Probe-cycle length.

The visited slots are 1,5,9,3,7, then 1 again. The period is 10/gcd(10,4)=5. Hence B holds: empty even slots cannot be reached. A and C give incorrect period lengths. D is false because the arithmetic sequence is independent of table contents.

**Common misconception:** Assuming every nonzero step visits the entire table.

## Q13

**Correct answer:** 13

**Concept:** Recursion depth including the base case.

Active argument lengths at the deepest point are 12,11,…,1,0, giving thirteen activations. None has returned before the base case is reached.

**Common misconception:** Counting recursive edges instead of active calls.

## Q14

**Correct answer:** A, C

**Concept:** Strict asymptotic domination.

f/g=(log₂n)/√n tends to zero. This proves f=o(g), hence also f=O(g), establishing C and A. The reciprocal ratio is unbounded, refuting B and Θ-equivalence in D.

**Common misconception:** Assuming a logarithmic factor exceeds every fractional power.

## Q15

**Correct answer:** A

**Concept:** Quantifiers in the pumping lemma.

Regularity promises at least one pumpable valid decomposition. Showing that one chosen decomposition fails does not exclude another. For the selected word, every allowed y lies in the initial zeros and has positive length; pumping it down breaks equal counts. That universal step repairs the proof, as A says. B is not required, C incorrectly bans a permitted pumping exponent, and D reverses the length condition.

**Common misconception:** Choosing the adversary's decomposition in a nonregularity proof.

## Q16

**Correct answer:** 768

**Concept:** Burst count and occupied bus time.

The transfer has 4096/16=256 bursts. Each occupies three bus cycles, so occupied time is 256×3=768 cycles. No additional interburst delay is specified or requested.

**Common misconception:** Confusing elapsed transfer time with occupied bus cycles.

## Q17

**Correct answer:** 6

**Concept:** Determinant effects of elementary operations.

Swapping two rows changes −2 to 2. Scaling a column by three then changes the determinant to 6.

**Common misconception:** Applying a row-swap sign change twice or scaling by the matrix dimension.

## Q18

**Correct answer:** A

**Concept:** JK flip-flop transition rules.

(1,0) sets the output to 1; (1,1) toggles it to 0; (0,0) retains 0; (0,1) resets it to 0. Thus A is correct. B fails to toggle, C fails to set initially, and D changes state on the hold input.

**Common misconception:** Treating the toggle input as another set input.

## Q19

**Correct answer:** 130

**Concept:** Recomputing shortest-seek choices.

The initial tie between 45 and 55 chooses 45. The full order is 50→45→55→90→10, with distances 5,10,35,80. Their sum is 130. Each choice uses the head's current position, not its original position.

**Common misconception:** Sorting requests once by initial distance instead of making successive local choices.

## Q20

**Correct answer:** A, C

**Concept:** Recognizability of complementary languages.

Interleave one step of each recognizer. Exactly one language contains the input, so one simulation eventually accepts; that determines membership and yields a decider. Thus A and C hold. A decidable language need not be regular, refuting B. A recognizer can still loop on nonmembers even when another decider exists, refuting D.

**Common misconception:** Confusing existence of a decider with termination of every recognizer.

## Q21

**Correct answer:** B

**Concept:** CRC detection using a polynomial factor.

An undetected error polynomial must be divisible by the generator, hence by x+1. Over GF(2), this implies E(1)=0, meaning an even number of nonzero coefficients. Any odd-weight error has E(1)=1 and is detected. B is correct. Even-weight errors may be undetected, so A and C are not universal guarantees; a nonzero multiple of the generator refutes D.

**Common misconception:** Treating a CRC as detecting every nonzero corruption.

## Q22

**Correct answer:** 3

**Concept:** Epsilon closure and accepted words.

The start epsilon closure reaches b. From b, any number of zeros may be consumed, followed by at least one 1 to reach c; further ones stay in c. The language is 0*1+. Length-three words are 001,011,111: three.

**Common misconception:** Counting epsilon moves as input symbols or allowing zeros after reaching c.

## Q23

**Correct answer:** 52

**Concept:** Row-major indexing.

Two full rows contribute ten integers, followed by three integers within the final row. The offset is (2×5+3)×4=52 bytes.

**Common misconception:** Multiplying the row index by the number of rows rather than columns.

## Q24

**Correct answer:** 0.65625

**Concept:** Unique minimum in independent discrete choices.

Choose the unique minimum station in three ways. If its value is m, each other station has 3−m larger choices. Qualifying outcomes number 3(3²+2²+1²+0²)=42 out of 4³=64. Probability 42/64=0.65625.

**Common misconception:** Requiring all three counters to be distinct, though the two nonminimum counters may tie.

## Q25

**Correct answer:** -4.5

**Concept:** A third-order trigonometric limit.

Using sin u=u−u³/6+O(u⁵), the numerator is −27x³/6+O(x⁵). Dividing by x³ and taking the limit gives −27/6=−4.5. Assigning this value at zero ensures continuity.

**Common misconception:** Keeping only the linear sine approximation after its term has cancelled.

## Q26

**Correct answer:** B

**Concept:** FIRST and FOLLOW in LL(1) parsing.

At S the alternatives begin with distinct a and b. At A and B, c selects the nonempty production and the end marker in FOLLOW selects ε. No table cell has two entries, proving B. A ignores separate nonterminals and lookaheads; C ignores the leading symbols; D claims nonexistent left recursion.

**Common misconception:** Declaring a conflict merely because terminal symbols occur in different productions.

## Q27

**Correct answer:** 4

**Concept:** Grammar-induced associativity.

The left-recursive production groups the expression as (9−3)−2. Attributes compute 6, then 4. The parse does not group it as 9−(3−2).

**Common misconception:** Evaluating a chain using an associativity inconsistent with its parse tree.

## Q28

**Correct answer:** 52

**Concept:** Variance of an independent linear combination.

Independence removes the covariance term, and the constant contributes no variance. Thus Var(2X−3Y+7)=2²×4+(−3)²×4=16+36=52.

**Common misconception:** Carrying the negative coefficient into variance without squaring it.

## Q29

**Correct answer:** -1.5

**Concept:** Signed fixed-point scaling.

The unsigned pattern is 232; in eight-bit two's complement it means 232−256=−24. Four fractional bits scale this by 2⁻⁴, giving −24/16=−1.5.

**Common misconception:** Interpreting the raw bit pattern as unsigned before applying fractional scaling.

## Q30

**Correct answer:** B

**Concept:** B+ leaf splitting and separator copies.

The stipulated leaves are [4,7,9] and [12,15]. The right leaf's smallest key is 12, so B is correct. A is the left leaf's largest key, C is internal to the left leaf, and D is the right leaf's largest key. None matches the given separator policy.

**Common misconception:** Applying a different split convention despite an explicit rule.

## Q31

**Correct answer:** 14

**Concept:** First-fit fragmentation.

Allocating seven leaves holes 3,6,14. The five-unit request skips the first hole and reduces the second to one, leaving 3,1,14. The largest remains 14.

**Common misconception:** Using the smallest suitable hole globally rather than scanning from the start.

## Q32

**Correct answer:** 3

**Concept:** Equivalence classes defined by a statistic.

Possible cardinalities 0,1,2,3,4 produce remainders 0,1,2. Each remainder is realized, and equal remainders form one class. Hence there are three classes, not five cardinality classes.

**Common misconception:** Treating distinct cardinalities as distinct classes despite reduction modulo three.

## Q33

**Correct answer:** A, C

**Concept:** Characteristic polynomial and diagonalization.

The characteristic polynomial is (λ−2)(λ+1)=λ²−λ−2. Cayley–Hamilton gives A²−A−2I=0, proving A. Distinct real eigenvalues give two independent real eigenvectors, proving C. The determinant is −2, so B is false. For example, the upper triangular matrix with rows (2,1),(0,−1) has these eigenvalues but is not symmetric, refuting D.

**Common misconception:** Confusing real diagonalizability with orthogonal diagonalizability of symmetric matrices.

## Q34

**Correct answer:** 1.2

**Concept:** Average branch-stall cost.

A fraction 0.20×0.25=0.05 of instructions mispredict, adding 0.05×4=0.2 cycles per instruction. Add the base CPI of one to obtain 1.2.

**Common misconception:** Applying the conditional misprediction rate to all instructions.

## Q35

**Correct answer:** A

**Concept:** Ties-to-even binary rounding.

The value 1.101₂ lies halfway between 1.10₂ and 1.11₂. The retained least significant bit in 1.10 is zero, so ties-to-even selects A. B chooses the odd last bit; C and D are not the adjacent nearest values.

**Common misconception:** Always rounding an exact halfway case upward.

## Q36

**Correct answer:** B

**Concept:** Closures and environment lifetime.

F and G need separate cells associated with their separate outer activations, and those cells must remain alive while captured. B provides both identity and lifetime. A wrongly merges cells, C leaves dangling references, and D implements caller-dependent lookup rather than lexical capture.

**Common misconception:** Assuming every local variable's lifetime must end when its defining call returns.

## Q37

**Correct answer:** 2

**Concept:** Boolean constraint propagation.

For the AND to be one, each adjacent pair must differ. Once a is chosen, b=¬a, c=a, d=¬a are forced. The satisfying assignments are 0101 and 1010, giving two.

**Common misconception:** Counting the three XOR constraints as independent choices despite shared variables.

## Q38

**Correct answer:** A, C

**Concept:** Recoverability and cascading aborts.

r2(X) reads the uncommitted w1(X), proving A. Recoverability would require T1 to commit before T2 commits; instead T1 aborts after c2, so B is false. T2's dependence requires aborting it when T1 aborts, but T2 has already committed, establishing C's problem. Strict schedules prohibit this read of an uncommitted write, so D is false.

**Common misconception:** Treating a completed commit as evidence that a schedule satisfies recovery constraints.

## Q39

**Correct answer:** 5

**Concept:** Farthest-future replacement.

The initial 0 and 1 references fault. The next 0 hits. On 2, evict 0, which never returns. The next 1 hits. On 3, evict 2, whose next use is later than 1's. The next 1 hits; the final 2 faults. Thus faults occur at positions 1,2,4,6,8, totalling five. Farthest-future replacement is optimal; alternatively, when 3 arrives, keeping 2 instead forces a fault on the intervening 1, so a fifth fault is unavoidable.

**Common misconception:** Looking at past recency when an offline future-aware optimum is requested.

## Q40

**Correct answer:** C

**Concept:** Precedence cycles and observed reads.

r1(X) before w2(X) gives T1→T2. r2(Y) before w1(Y) gives T2→T1. The cycle refutes both serial orders in A and B. In serial T1,T2, T2 reads Y=1; in serial T2,T1, T1 reads X=1, so neither reproduces both zero reads. Thus C holds. D overlooks read–write conflicts across transactions.

**Common misconception:** Checking only write–write conflicts.

## Q41

**Correct answer:** 960

**Concept:** Signed displacement and address units.

11110110₂ is 246 unsigned, or −10 as an eight-bit signed displacement. Scaling to bytes gives −40. The defined base is the next-instruction address, so the target is 1000−40=960.

**Common misconception:** Ignoring either sign extension or the word-to-byte scale.

## Q42

**Correct answer:** B

**Concept:** Aligning distances to shared suffixes.

If two acyclic lists share a node, all successors of that node are shared. After discarding the length difference from the longer prefix, the two pointers have equal distances to the end. Advancing together therefore reaches the first shared node together, or reaches null if disjoint. B uses linear time and constant extra storage. A and C confuse equal values with identity; D supplies no intersection test and mutates links.

**Common misconception:** Inferring physical node sharing from equal stored data.

## Q43

**Correct answer:** 15

**Concept:** Accounting across a two-stack queue.

The four enqueues cost four pushes. The first dequeue transfers A and B (four operations) and pops A (one). The second dequeue pops B (one). The third transfers C and D (four) and pops C (one). Total 4+4+1+1+4+1=15.

**Common misconception:** Transferring the input stack while an older item remains in the output stack.

## Q44

**Correct answer:** 5

**Concept:** Parse trees and Catalan recurrence.

Let C(n) count trees with n leaves. C(1)=1, and splitting the root's ordered children gives C(n)=Σ C(i)C(n−i). Thus C(2)=1, C(3)=2 and C(4)=1×2+1×1+2×1=5.

**Common misconception:** Counting derivation schedules instead of distinct tree structures.

## Q45

**Correct answer:** 32

**Concept:** Constrained univariate maximization.

Substitute y=6−x to get h(x)=6x²−x³ on [0,6]. Its derivative is 3x(4−x), so the interior maximum is at x=4,y=2 and equals 32. Both endpoints give zero.

**Common misconception:** Assuming symmetry forces x=y even when the objective weights them differently.

## Q46

**Correct answer:** 4

**Concept:** Degree sums and constructive feasibility.

There are 12×2=24 assignments. Giving all eight engineers two assignments uses 16. Each engineer raised to four needs two extra, so at most four can reach four. To attain it, let H1–H4 be four engineers and L1–L4 the others. Assign four projects to the cyclic pairs H1H2,H2H3,H3H4,H4H1. Assign eight further projects H_iL_i and H_iL_(i+1), with indices modulo four. Every H has four projects and every L two. Hence the bound four is attainable.

**Common misconception:** Establishing a numerical upper bound without checking the relationship constraints permit it.

## Q47

**Correct answer:** A, B, C

**Concept:** Prime implicants and forbidden expansion.

A covers 0,1; dropping a′ would add minterm 4, and dropping b′ would add 3, both OFF. B covers 2,6; dropping b adds 4 and dropping c′ adds 3, so it is prime. C covers 5,7; dropping a adds 3 and dropping c adds 4, so it is prime. D covers 0,1,4,5 and includes OFF minterm 4, so it is not even an implicant.

**Common misconception:** Checking only that a product covers some ON minterms without checking all of its coverage.

## Q48

**Correct answer:** B

**Concept:** Earliest-finish activity selection.

Choose B, then C, then D to obtain three activities. Choosing A first allows E afterwards but no third activity, proving B. A's claimed count is false. C is false because earliest-finish already achieves three. The compatible sets {A,E} and {B,C,D} are both maximal but have different sizes, refuting D.

**Common misconception:** Equating maximality with maximum cardinality.

## Q49

**Correct answer:** A, C

**Concept:** Stack recognition and homomorphism closure.

A deterministic PDA pushes the prefix until #, then pops and compares each following bit, accepting exactly on a complete match; thus A holds. Mapping # to ε is a homomorphism, and CFLs are closed under homomorphism, proving C. A finite automaton cannot remember arbitrary prefixes: distinct prefixes x,y are distinguished by suffix #xᴿ, so infinitely many distinguishable prefixes refute regularity in B. D confuses individually finite inputs with a uniform finite memory bound.

**Common misconception:** Believing a visible midpoint removes the need to remember unbounded prefix content.

## Q50

**Correct answer:** 6

**Concept:** Short-circuit paths over truth assignments.

If P is false, Q is skipped and R is tested: four assignments of Q,R yield exactly two tests. If P is true and Q true, R is skipped: two choices of R yield two tests. If P is true and Q false, all three tests run. Therefore six of eight assignments qualify.

**Common misconception:** Counting syntactically present comparisons rather than comparisons actually executed.

## Q51

**Correct answer:** 2

**Concept:** Full binary-tree leaf identities.

With i internal nodes and l leaves, l=i+1 and i+l=19, giving l=10. The four internal nodes with two leaf children account for eight leaves whose siblings are leaves. The other two leaves each have an internal-node sibling.

**Common misconception:** Counting parents rather than leaves when subtracting the sibling pairs.

## Q52

**Correct answer:** 18

**Concept:** Feasible 0/1 combinations.

No three items fit because the three lightest weigh 9. Feasible pairs have values 14 at weight 5, 15 at weight 6, 18 at weight 7 from items of weights 2 and 5, and 17 at weight 7 from weights 3 and 4. Singles are at most 12. The optimum is 18.

**Common misconception:** Applying fractional-knapsack value-density choices to indivisible items.

## Q53

**Correct answer:** A, C

**Concept:** Value relations across redefinitions.

Let initial a be a0. Then t=a0+b, final a=a0+1, u=t+1 and v=t. Therefore final a+b−1 equals t (A), and u may be replaced by t+1 (C). B lowers u by one. D removes a definition whose value is still required, so it cannot preserve all final values.

**Common misconception:** Reusing an expression after one operand changes without adjusting its value relation.

## Q54

**Correct answer:** 202

**Concept:** Modular subtraction.

37−91=−54, and retaining eight bits gives −54 modulo 256, which is 202. Equivalently complementing 91 gives 164, and 37+164+1=202.

**Common misconception:** Reporting the mathematical signed difference when the unsigned retained value is requested.

## Q55

**Correct answer:** 13

**Concept:** Encoded control fields with idle choices.

The groups need 6,4 and 10 distinct encodings after including “none”. Their widths are ceil(log₂6)=3, log₂4=2 and ceil(log₂10)=4. Add the four independent bits: 3+2+4+4=13.

**Common misconception:** Omitting the “none” code or encoding independent signals as mutually exclusive.

## Q56

**Correct answer:** B

**Concept:** Recursion-tree harmonic sums.

Write n=2^k. At depth j with subproblem size at least four, the aggregate merge cost is Θ(n/(k−j)). Summing j=0,…,k−2 gives Θ(n Σ_(r=2)^k 1/r)=Θ(n log k). The leaves cost Θ(n), so the result is Θ(n log log n), B. A omits the growing harmonic factor, C treats every level as Θ(n), and D overcounts beyond the recursion-tree work.

**Common misconception:** Applying only the basic polynomial-gap Master Theorem cases to a logarithmic boundary case.

## Q57

**Correct answer:** 3

**Concept:** Shortest paths after an edge failure.

Originally A–B–C–D costs 2+1+2=5. After deleting BC, A–B–D costs 8 and A–C–D costs 9, with positive-weight detours unable to improve either. The new optimum is 8, an increase of 3.

**Common misconception:** Keeping a path that still contains the failed edge in the recomputation.

## Q58

**Correct answer:** 1

**Concept:** Don't-care expansion.

The ON and don't-care minterms together are exactly the assignments with b=0. The term b′ covers all ON minterms and no OFF minterm, using one literal. A zero-literal term would be constant one and cover every OFF minterm, so one is minimal.

**Common misconception:** Treating don't-care values as required zeros or as required ones in the final function.

## Q59

**Correct answer:** 0.4286

**Concept:** Bayes' rule after sampling without replacement.

For A, exactly one red has probability (3×2)/choose(5,2)=3/5. For B it is (1×4)/10=2/5. The weighted probabilities are (1/3)(3/5)=1/5 and (2/3)(2/5)=4/15. Thus P(A|one red)=(1/5)/(1/5+4/15)=3/7=0.428571…, rounding to 0.4286. Accepted range: 0.42855–0.42865.

**Common misconception:** Comparing likelihoods without incorporating the unequal prior box probabilities.

## Q60

**Correct answer:** 0

**Concept:** Meet/join compatibility in a divisor lattice.

For positive integers, gcd(x,12)lcm(x,12)=12x. The requested values force 6×72=12x, hence x=36. But gcd(36,12)=12, not 6. Therefore no element satisfies both requirements, and the count is zero. In prime-exponent terms, the requested gcd has exponent one of 2 while 12 has exponent two, forcing x's exponent to one; their lcm could then not have exponent three of 2 as 72 does.

**Common misconception:** Treating the product identity as sufficient without checking the separate gcd and lcm constraints.

## Q61

**Correct answer:** A

**Concept:** CFL closure with a regular constraint.

A PDA for L can be combined with a DFA for R by storing their finite control states together and retaining the PDA stack, proving A. CFLs are not closed under complement or arbitrary CFL intersection, so B and C are not guaranteed. D would include the complement of L by taking R to be the full language, so it too is not guaranteed.

**Common misconception:** Extending intersection closure with regular languages to arbitrary context-free languages.

## Q62

**Correct answer:** 3

**Concept:** Gaussian elimination multipliers.

The first-column multipliers are L21=4/2=2 and L31=8/2=4. After eliminating column one, row two is (0,1,1) and row three (0,3,5). The next multiplier is L32=3/1=3, leaving final U33=2.

**Common misconception:** Computing a second-stage multiplier from the original, uneliminated matrix entries.

## Q63

**Correct answer:** 200

**Concept:** Fragment payload and offset units.

The payload is 2000 bytes. Each full fragment can carry 820−20=800 bytes, already divisible by eight. Payload sizes are 800,800,400. The last starts 1600 data bytes after the original payload's start, so its encoded offset is 1600/8=200.

**Common misconception:** Including fragment headers in payload offsets or reporting byte units instead of eight-byte units.

## Q64

**Correct answer:** 266240

**Concept:** Direct and indirect addressing capacity.

The indirect block stores 1024/4=256 data-block pointers. Together with four direct pointers, the inode addresses 260 data blocks, or 260×1024=266240 bytes. The indirect block itself is metadata and is not another file-data block.

**Common misconception:** Counting the pointer block as part of addressable file content.

## Q65

**Correct answer:** A, C

**Concept:** Pipe EOF and inherited descriptors.

An empty pipe yields EOF only when no referring write descriptor remains open, proving A. An inherited but unused writer still prevents EOF, so closing unused writers in both processes is needed for the intended EOF protocol, giving C. B leaves an open parent writer; D ignores it and substitutes EOF for blocking. Both are false.

**Common misconception:** Assuming that a process which never writes cannot keep a pipe's write end alive.
