# Worked Solutions — Mock Test 100

## Q1

**Correct answer:** 32

**Concept:** Second-order recurrence evaluation.

The successive terms are 1,2,4,8,16,32. Each calculation uses the preceding two terms; induction also verifies a_n=2^(n−1).

**Common misconception:** Ignoring the coefficient two on the second preceding term.

## Q2

**Correct answer:** 5 (exact)
**Concept:** Rectangle constraints and area change.

If sides are u≥v, then u+v=20 and uv=96. Hence (u−v)²=400−384=16, so u−v=4 and sides are 12,8. The new area is 13×7=91, a decrease of 5. Equivalently, uv−(u+1)(v−1)=u−v+1=5.

**Common misconception:** Equal and opposite side changes preserve perimeter but not area.

## Q3

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: agreement and past tense. In the neither/nor construction the nearer subject is singular supervisor, giving was. The decision occurred yesterday, requiring announced. B supplies both. A has the wrong second verb and plural agreement; C lacks a finite past-tense second verb; D uses present announce. Check both blanks, not just one.

## Q4

**Correct answer:** 19

**Concept:** Weighted subgroup percentages.

Remote part-timers form 0.60×0.25=0.15 of all employees. Other part-timers form 0.40×0.10=0.04. Together they are 0.19, or 19%.

**Common misconception:** Adding subgroup percentages without weighting their group sizes.

## Q5

**Correct answer:** 2 (exact)

**Concept:** General Aptitude — Deductive logic

1. The biconditional requires exactly one of C and D to be selected.
2. The other selected person must be A or B. Selecting A would also require B, producing three people, which is forbidden.
3. Hence the possible pairs are {B,C} and {B,D}: two pairs.

**Common misconception:** An implication does not require its antecedent to be true.

## Q6

**Correct answer:** 5

Undo the90-degree counterclockwise rotation by mapping final coordinates(u,v) to(v,−u), obtaining(−2,3). Reflection across x=1 maps original(x,y) to(2−x,y), so2−x=−2 and y=3. The original point is(4,3), at distance sqrt(16+9)=5. Undo composed transformations in reverse order.

## Q7

**Correct answer:** A, C
**Concept:** Truth-value consistency.

If ON, the truth values are true,false,false: only one statement is true. If OFF, they are false,true,true: exactly two are true. Hence OFF is forced and B,C are truthful, proving A,C. B incorrectly includes A; D overlooks the consistent OFF assignment.

**Common misconception:** Evaluate a statement about another statement using the same candidate state.

## Q8

**Correct answer:** 18

Arrange B,B,C in three distinct orders. Each has four gaps around/between its letters. Put the two identical A's in two distinct gaps to avoid adjacency: choose(4,2)=6 choices. Total3×6=18. Selecting distinct gaps prevents AA without distinguishing the two A copies.

## Q9

**Correct answer:** 25

**Concept:** Weighted averages and relative percentage changes.

A's initial share is2/3. If its new share is x, the combined rate is0.9x+0.6(1−x)=0.75, giving x=1/2. The relative fall is[(2/3−1/2)/(2/3)]×100=25%. The change in percentage points is16 2/3, which is not the requested relative percentage decrease.

**Misconception:** Confusing a change in share with the percentage change of that share.

## Q10

**Correct answer:** 6

The punch at x=4 lies on the vertical fold, so unfolding in x does not produce two distinct centres. Reflection in y gives centres (4,1),(4,7), two holes. The other punch produces (2,2),(6,2),(2,6),(6,6), four holes. All six are separated by far more than twice the radius. Counting every punch as four holes double-counts centres fixed by a fold reflection.

## Q11

**Correct answer:** B

Candidates I, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) IV.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: PDA acceptance-mode conversion. After consuming all input in an original final state, drain mode can empty the protected stack and accept, A. If input remains, drain mode has no consuming transitions and cannot meet the all-input-consumed requirement, D; B is therefore false. The fresh marker protects against premature empty-stack acceptance and must be distinguished from original symbols, so C is false. Acceptance requires both the stack/final-state condition and complete input consumption.

## Q12

**Correct answer:** 7

Concept: B+ internal-node separators. Six ordered separators partition the search domain into seven child intervals, so k+1=7 pointers. This is an internal node, not a leaf's record-pointer count.

## Q13

**Correct answer:** 2.6667 (accepted range 2.66665–2.66675)

The old squared-deviation sum is 4 observations×variance 4=16. Adding observations equal to the old mean leaves the mean at 5 and adds zero squared deviation. Divide 16 by the new population size 6 to obtain 8/3≈2.6667. The population denominator is 6, not the sample-variance denominator 5.

## Q14

**Correct answer:** 4

The base production accounts for the first d. Each recursive production adds one more d, so five digits require four recursive applications. Attribute evaluation follows the parse structure but does not change the production count.

## Q15

**Correct answer:** 5

Three faults require three page reads. The two dirty victims also require writes; the clean victim does not. Total3+2=5 page transfers. A page fault is not necessarily exactly one disk transfer.

## Q16

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Harmonic running-time sum.

For a fixed i there are floor(n/i) calls. Their sum is Θ(nH_n)=Θ(n log n): replacing each floor by n/i changes the sum by less than n. A and C underestimate the harmonic accumulation; B treats the inner loop as n iterations for every i.

**Common misconception:** A nested loop need not be quadratic when its step size depends on the outer index.

## Q17

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Lexicographic row-count minimization favours2 over3 regardless of the secondary cost, so A holds. Cost-first favours6 over8, proving B. These different outcomes disprove C and demonstrate D's ambiguity. State the optimization objective before comparing covers.

## Q18

**Correct answer:** A
**Concept:** Full-adder outputs.

With x=y=1, the total is 2+c. Its low bit is c and its carry is always one, yielding A. B incorrectly complements the sum; C,D incorrectly make carry depend on c.

**Common misconception:** Carry indicates a total of at least two, which is already guaranteed by x=y=1.

## Q19

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

A is a valid implication: the union of two finite sets would be finite. Its antecedent cannot actually hold here because {a,b}* is infinite. B follows from regular complement closure and regular languages being context-free. D follows because finite languages are regular. C fails for nonregular context-free languages: if their complement were regular, complement closure would make the original regular too. A statement can be necessarily true because its premise is impossible.

## Q20

**Correct answer:** 4
**Concept:** Exhaustive Boolean complement combinations.

For any x,y, the four argument pairs in the XOR are exactly 00,01,10,11 in some order. AND is 1 on exactly one of them. Therefore their XOR is always 1, on all four assignments.

**Common misconception:** Complementing both coordinates produces the full input table here, not four independent unknown values.

## Q21

**Correct answer:** -0.75

An inverse y satisfies3*y=0, the identity. Thus3+y+3y=0, yielding y=−3/4=−0.75, which belongs to the domain. The operation is commutative, so it is also the left inverse. Multiplicative inverse under an unfamiliar group law need not be the reciprocal under ordinary multiplication.

## Q22

**Correct answer:** 52

**Concept:** Row-major indexing.

Two full rows contribute ten integers, followed by three integers within the final row. The offset is (2×5+3)×4=52 bytes.

**Common misconception:** Multiplying the row index by the number of rows rather than columns.

## Q23

**Correct answer:** 3

Concept: simultaneous next-state evaluation. States follow 10→11→00→01→10→11. After five edges the value is binary 11, or three. Using updated Q0 in the expression for Q1 would incorrectly model a synchronous update as sequential assignment.

## Q24

**Correct answer:** 6

Every vertex loses one of its three edges, leaving degree2. The resulting six-vertex graph is a single cycle of length6. A spanning tree results by deleting any one of its six edges, giving6 trees. Degree2 alone would not guarantee one cycle for arbitrary larger bipartite graphs; here two separate simple bipartite cycles would require at least eight vertices.

## Q25

**Correct answer:** 3

For p=1 or2, string a³ is long enough but every permitted nonempty pumped part has length1 or2; pumping down leaves a nonmultiple-of-three length. For p=3, every eligible string has at least three a's; choose y=a³, and every pump changes the length by a multiple of three. Thus3 is both necessary and sufficient.

## Q26

**Correct answer:** 4

Including4 excludes3 and5. Choose two remaining elements from{1,2,6,7}; the only prohibited pairs are{1,2} and{6,7}. Thus C(4,2)−2=4. They are{1,4,6},{1,4,7},{2,4,6},{2,4,7}. Avoiding neighbours of4 is necessary but not enough; the selected other pair must also be nonconsecutive.

## Q27

**Correct answer:** 7

Group A needs four choices including none, requiring2 bits. Group B needs six choices including none, requiring3 bits. Two independent signals need2 more bits. Total7. The explicit none option must be included before rounding each field width upward.

## Q28

**Correct answer:** A, B

**Concept:** B+ tree structural invariants.

Separators may copy leaf key values, so A holds. Balance keeps all leaves at one depth, giving B. Data entries are at leaves, refuting C; root occupancy has special exceptions, refuting D.

**Common misconception:** Importing ordinary B-tree data-placement rules unchanged into B+ trees.

## Q29

**Correct answer:** B

Greedy chooses6,1,1: three coins. Two4 coins suffice, and one coin cannot equal8, so the optimum is two. B is correct. A wrongly describes the greedy output; C gives both counts incorrectly; D ignores valid representations. Greedy optimality depends on the denomination system.

## Q30

**Correct answer:** 400

**Concept:** Summing odd increments.

T(n)=Σ_(i=1)^n(2i−1)=2n(n+1)/2−n=n². Therefore T(20)=400.

**Common misconception:** Treating the recurrence's incremental cost as the total.

## Q31

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

p initially points to B. The second assignment connects A to C. The third connects B to A, and the final assignment moves head to B. The reachable list is B→A→C. Thus B is correct; A and C place the links in different orders, while D ignores the rewiring. Trace node identities separately from pointer-variable names.

## Q32

**Correct answer:** B

Lexical scope identifies Outer regardless of which procedure calls Inner, so the static link in B locates the intended activation. A follows call history to Caller. C follows recency without lexical meaning. D cannot by itself locate a non-global activation's local x. Dynamic and static nesting need not coincide.

## Q33

**Correct answer:** 4

**Concept:** Width expansion of memory chips.

Each chip supplies eight bits at the shared word address. Four in parallel supply 32 bits while retaining the 1024-word depth.

**Common misconception:** Expanding depth instead of width.

## Q34

**Correct answer:** A

Concept: transport demultiplexing. Ports identify application endpoints on a host, in combination with transport/address context (A). B concerns link framing; C hardware pins; D processor addressing. These are not transport-port roles. A port number by itself is not a globally unique connection identifier.

## Q35

**Correct answer:** 1.5

Each packet takes0.5 seconds per link. Packet1 uses the links over[0,0.5] and[0.5,1]; packet2 uses them over[0.5,1] and[1,1.5]. Completion is1.5 seconds. Store-and-forward prevents forwarding a packet before its full arrival, but different links can transmit different packets concurrently.

## Q36

**Correct answer:** 3

**Concept:** Wait-for graph cycles.

The edges are P→Q, Q→R, R→P and S→Q. P,Q,R form a directed cycle. S depends on it but no path returns to S, so S is not on a cycle. Exactly three processes satisfy the question, even though S cannot make progress either under the stated rules.

**Common misconception:** Equating every process blocked behind a cycle with membership in the cycle itself.

## Q37

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** CRC error-polynomial divisibility.

Modulo G, x³=x+1. Successive reductions give x⁴=x²+x, x⁵=x²+x+1, x⁶=x²+1 and x⁷=1. Thus x⁷+1 has zero remainder (A), while x⁶+1 has remainder x² (B false). A single-bit error is x^k; a polynomial with nonzero constant term and degree three cannot divide a monomial, proving C. A burst of length at most three is x^kB(x) with nonzero B of degree at most two. Since G is coprime to x, divisibility would require G to divide B, impossible by degree; D holds.

**Common misconception:** CRC guarantees depend on error structure, not just the number of flipped bits.

## Q38

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The identifier is the pair, permitting the same room number under different owners, proving A and refuting B. BuildingID contributes to identification, proving C. Replacing it with another owner's identifier can duplicate an existing pair, proving D. A partial key is not a global key.

## Q39

**Correct answer:** 174

Represent R as a 3×3 Boolean matrix. The first formula says every row is nonempty, giving 7³ matrices. The second forbids a column of three ones. For a specified all-one column, each row's other two entries are free, giving 4³ matrices; for two specified all-one columns there are 2³; for all three there is one. Inclusion-exclusion yields 7³−3×4³+3×2³−1=174. The two quantifier orders impose distinct row and column conditions.

## Q40

**Correct answer:** B

Candidates II, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) IV.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) I, III and omits valid candidate(s) II, IV.
- **D: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The first two writes give an edge T1→T2; the last two give T2→T1. The graph has a cycle, so A and C are false. There are no read-from relationships to preserve, and T1 is the final writer. Serial order T2,T1 has the same final writer, so B and D are true. Blind writes permit view equivalence even when conflict serializability fails.

## Q41

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Bounded simulation.

The allowed simulation horizon is computable and finite for every input. Test acceptance initially and after each permitted step, stopping no later than |x| steps; this decides membership, proving A and C. It requires no unbounded halting decision, so B is false. Behaviour on another input cannot invalidate acceptance within this input's finite bound, refuting D.

**Common misconception:** Treating every question about a Turing machine's behaviour as an undecidable halting question.

## Q42

**Correct answer:** 3

Compute t=a+b, u=t*t, x=u+t: three binary operations. Sharing avoids reevaluating a+b. All three distinct required operations remain under this stated local optimization.

## Q43

**Correct answer:** 4 (exact)

**Concept:** Engineering Mathematics — Matrices determinants and linear systems

1. AX=XA means the entries repeat under a simultaneous cyclic shift of row and column indices. Symmetry therefore forces X to have rows [a,b,c,b], [b,a,b,c], [c,b,a,b], [b,c,b,a].
2. The zero-row-sum requirement gives a+c+2b=0. The vector (1,-1,1,-1) has eigenvalue mu=a+c-2b=-4b. Every vector (p,q,-p,-q) has eigenvalue nu=a-c; this is a two-dimensional eigenspace. Together with the all-ones vector, these spaces span R^4.
3. X^2=X holds exactly when mu and nu each belong to {0,1}, since the remaining eigenvalue is already zero.
4. Every ordered pair (mu,nu) determines one matrix: b=-mu/4, a=mu/4+nu/2, c=mu/4-nu/2. There are 2*2=4 pairs and hence four matrices.

**Common misconception:** The commuting and symmetry constraints couple entries before idempotence is imposed; an arbitrary projection is not allowed.

## Q44

**Correct answer:** 1

Optimal prefix weights are 4,7,9,13,13. For the fifth vertex, taking it gives9+3=12, below omitting it at 13. For the fourth, taking it gives7+6=13, above omitting at 9. The second vertex's7 beats the first vertex's4. Thus the unique optimal set is positions 2,4, with weight13; the count is 1. Ties between consecutive prefix optimum values need not imply multiple optimal sets for the same prefix.

## Q45

**Correct answer:** 1
**Concept:** Scheduling by earliest deadline and a lower bound.

Earliest-deadline order is C,A,B,D, with completion times 1,3,6,8 and latenesses −2,−1,0,1. Its maximum lateness is 1. No schedule can do better: total processing time is 8, so the last job finishes at 8, while every deadline is at most 7. The last job's lateness is at least 1. The exhibited schedule attains the lower bound.

**Common misconception:** Lateness can be negative; it is not the same as tardiness, which truncates negative values to zero.

## Q46

**Correct answer:** 9

The first store enters at0 and frees the buffer at3. Subsequent stores enter at3,6,9, respectively. Requested earlier issue times do not bypass a full buffer. The fourth is accepted at9; its later completion at12 is not what was asked.

## Q47

**Correct answer:** 16
**Concept:** Width and depth expansion of memory chips.

Two four-bit-wide chips in parallel provide one eight-bit byte at each of 8K addresses, making an 8 KiB bank. Eight such banks provide 64 KiB. Total chips are 2×8=16. Equivalently, total required bits divided by bits per chip gives (64×1024×8)/(8×1024×4)=16.

**Common misconception:** A chip word is four bits here, not a byte; both width and address depth must be expanded.

## Q48

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

With x=0 the loop is skipped, proving A. With x=1, every update keeps x positive and strictly increases it, so the original never returns while the rewritten code returns immediately, proving B. C ignores observable termination; D correctly recognizes that obligation. An unused computed value does not automatically make its entire computation removable.

## Q49

**Correct answer:** 167 (exact)

**Concept:** Digital Logic — Fixed-point arithmetic

E7 has unsigned value 231 and signed raw value 231−256=−25, representing −25/16. Hexadecimal 39 is 57, representing 57/16. Their product is −1425/256. To encode with four fractional bits, multiply by 16, obtaining raw value −1425/16 = −89.0625. The nearest integer is −89; there is no tie. Its 8-bit two's-complement encoding is 256−89=167. The represented rounded value is −89/16.

**Common misconception:** Multiplication doubles the fractional-bit count; rounding must follow rescaling before two's-complement encoding.

## Q50

**Correct answer:** 1

BFS gives distance1 to a,b and distance2 to c,d. Vertex d's only predecessor at distance1 is a, so the sole shortest route is s→a→d. Although c has two shortest paths, extending either through c→d takes three edges and does not contribute to shortest paths to d. Count only predecessors one level earlier.

## Q51

**Correct answer:** 17
**Concept:** Sliding-window working sets.

The five four-reference windows are (1,2,1,3), (2,1,3,4), (1,3,4,2), (3,4,2,4), and (4,2,4,5). Their distinct-page counts are 3,4,4,3,3. The requested sum is 17.

**Common misconception:** Repeated references count once within a working set, and old pages leave when their last reference exits the window.

## Q52

**Correct answer:** 3

**Concept:** Continuity required before derivative matching.

Differentiability implies continuity, so the left limit b must equal f(0)=1. The right derivative of e^(2x) at zero is 2. The left derivative of ax+b is a, hence a=2. Therefore a+b=3.

**Common misconception:** Matching slopes while neglecting the function-value continuity condition.

## Q53

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Product automata with Boolean acceptance predicates.

Both components accepting implements intersection (A). Exactly one implements symmetric difference (B). First accepting and second rejecting implements set difference (D). At least one implements union, not concatenation, so C is false. Concatenation needs tracking a split point rather than merely simultaneous acceptance of the entire same input.

**Common misconception:** Confusing Boolean combination of whole-word acceptance with sequential language composition.

## Q54

**Correct answer:** A, C, D
**Concept:** Basic versus strict two-phase locking.

Basic 2PL orders transactions consistently by their lock points and guarantees conflict serializability (A). It can still release a write lock before commit, allowing another transaction to read a value later rolled back, so B is false. Two transactions may each hold one lock while requesting the other's during their growing phases, giving deadlock (C). Keeping exclusive locks until commit prevents another transaction from acquiring a read lock on an uncommitted written item, so D is true.

**Common misconception:** Serializability, absence of cascading aborts, and deadlock freedom are separate properties.

## Q55

**Correct answer:** 7

Concept: nullable-occurrence deletion with deduplication. Distinct S right-hand sides are ABA, BA, AA, AB, A, B, ε. Deleting the left A and B or deleting B and the right A both produce A, so they count once. Total seven, rather than the eight occurrence-subset choices. Identical grammar productions are not duplicated by distinct derivational deletion choices.

## Q56

**Correct answer:** 0

**Concept:** Rounding and loss of a small addend.

Near 16, four-bit precision has spacing two. The exact sum 17 lies midway between 16=1.000₂×2⁴ and 18=1.001₂×2⁴. Ties-to-even selects 16. Adding −16 then gives zero exactly. In contrast, a different grouping can retain a different result, illustrating nonassociativity.

**Common misconception:** Performing both additions exactly and rounding only once at the end.

## Q57

**Correct answer:** 15

**Concept:** Accounting across a two-stack queue.

The four enqueues cost four pushes. The first dequeue transfers A and B (four operations) and pops A (one). The second dequeue pops B (one). The third transfers C and D (four) and pops C (one). Total 4+4+1+1+4+1=15.

**Common misconception:** Transferring the input stack while an older item remains in the output stack.

## Q58

**Correct answer:** 133

Concept: stolen-cycle accounting. Every full four-cycle group completes three CPU instructions and one DMA transfer. After 33 groups (132 cycles), the CPU has completed 99 instructions and DMA 33 transfers, so DMA is still active. Cycle 133 is not stolen and completes instruction 100. Treating 100 CPU cycles as elapsed cycles ignores stalls; assuming all 64 transfers finish first ignores overlap.

## Q59

**Correct answer:** 2

**Concept:** Full binary-tree leaf identities.

With i internal nodes and l leaves, l=i+1 and i+l=19, giving l=10. The four internal nodes with two leaf children account for eight leaves whose siblings are leaves. The other two leaves each have an internal-node sibling.

**Common misconception:** Counting parents rather than leaves when subtracting the sibling pairs.

## Q60

**Correct answer:** A, B

Ascending insertion gives a right-child chain with n−1 edges, so A is true. The BST invariant ensures that inorder traversal returns sorted keys, proving B. For keys1,2,3, inserting2 first can give a balanced root, whereas inserting1,2,3 gives a chain; C is false. The chain has sorted inorder output but linear worst-case search, refuting D. Traversal order does not certify balance.

## Q61

**Correct answer:** 14
**Concept:** Normal and subnormal value ranges.

The largest finite value uses exponent 10 (E=2) and fraction .11: 1.75×2=3.5. The smallest positive value is subnormal exponent 00 and fraction .01: 0.25×1=0.25. Their ratio is 3.5/0.25=14.

**Common misconception:** Subnormal values do not include the implicit leading 1 of normalized values.

## Q62

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The unnormalized joint weights at(1,0),(1,1),(2,0),(2,1) are1,2,2,3, summing to8, so A. Summing the Y=1 column gives5/8, proving C. Given Y=0, X=1,2 have probabilities1/3,2/3, so the conditional mean is5/3, proving D. Independence fails since P(1,0)=1/8 differs from P(X=1)P(Y=0)=(3/8)(3/8)=9/64, refuting B.

## Q63

**Correct answer:** 3
**Concept:** Candidate-key closure and minimality.

B never appears on a right-hand side, so every key contains B. AB determines C then D; BC determines D then A; BD determines A then C. Each pair is minimal, and B alone determines none of A,C,D. Any larger key contains one of these pairs and is not minimal. There are exactly three candidate keys.

**Common misconception:** Supersets of candidate keys are superkeys, not additional candidate keys.

## Q64

**Correct answer:** 0.375

Six ordered pairs have absolute difference1: (0,1),(1,0),(1,2),(2,1),(2,3),(3,2). Out of16 equally likely pairs, probability6/16=0.375. Either station may have the larger counter.

## Q65

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Only reachable incoming values describe possible executions. Ignoring the unreachable7 leaves constant5, proving A,B. Including it would join5 with7 and lose constancy, proving C. D contradicts this example. Semantic reachability can sharpen a syntactic data-flow join.

