# Worked Solutions — Mock Test 064

## Q1

**Correct answer:** 3.2

Concept: weighted percentages. The two batches contain 300(0.02)=6 and 200(0.05)=10 defective units. Thus 100(16/500)=3.2%. Averaging the two percentages without their batch weights is incorrect.

## Q2

**Correct answer:** 2

Reflecting x=4 across x=4 leaves it unchanged, so the first fold contributes no distinct second x-coordinate. The two y-preimages are2 and6. The distinct original points are(4,2),(4,6), giving two, not four. Fold-line points must not be counted twice.

## Q3

**Correct answer:** C
**Concept:** Narrative reference and causal order.

R initiates the first inspection. S refers to that inspection and identifies the defect. Q repairs the identified defect and starts the second inspection. P gives that second inspection's result. Thus R,S,Q,P is coherent. A repairs before identifying the crack; B uses the inspection reference before its introduction; D places repair and retesting before the initiating event.

**Common misconception:** Pronoun references and causal dependencies constrain order even when each sentence is grammatical alone.

## Q4

**Correct answer:** 0.2000 (accepted range 0.19995–0.20005)

There are six equally likely unordered pairs. One is two red, one two blue and four mixed. The report excludes the blue pair, leaving five pairs; one is all red. The probability is1/5. The observer did not reveal that a particular designated draw was red, which would define a different condition.

## Q5

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The clause requiring revisions explicitly limits the panel's support, so qualified means conditional or limited, B. A uses another meaning of the word that is not intended here. C contradicts the stated support, and D contradicts the stated conditions. Context distinguishes a qualified endorsement from an unqualified one.

## Q6

**Correct answer:** 3.23 (range 3.225–3.235)

**Concept:** Compound growth equivalence.

The three-year factor is 1.25×0.8×1.1=1.1. A constant annual rate r must satisfy (1+r)³=1.1, giving 100r=100(1.1^(1/3)−1)=3.228011…%. Rounded answer 3.23; accepted range 3.225–3.235.

**Common misconception:** Averaging annual percentage changes arithmetically.

## Q7

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

At n=40 the expression is1600+40+41=1681=41², composite. Thus C supplies a counterexample. A and B are positive examples and cannot prove universality; D only establishes oddness in one case, which is not primality. One verified counterexample refutes a universal conjecture.

## Q8

**Correct answer:** 5

Write the array as[[a,b],[c,d]]. Since the second row and second column have maxima1, b,c,d are at most1. The first row and first column maxima2 force a=2. Remaining conditions are max(c,d)=1 and max(b,d)=1. If d=1, b,c can each be0 or1, giving4 arrays. If d=0, both b,c must be1, giving1 more. Total5. Orthographic maxima do not uniquely determine hidden column heights.

## Q9

**Correct answer:** 31

Concept: telescoping a recurrence. a5=a1+1²+2²+3²+4²=1+30=31. The last increment is 4², since the recurrence's left index is n+1. Including 5² is an off-by-one error.

## Q10

**Correct answer:** 0.5

**Concept:** Displacement volume.

The immersed sphere displaces (4/3)π(1.5)³=4.5π cubic metres. The tank's horizontal area is 9π, so the rise is 4.5π/(9π)=0.5 m. The assumptions exclude spilling and partial immersion.

**Common misconception:** Using the sphere's surface area rather than its volume.

## Q11

**Correct answer:** 21

**Concept:** Equal-weight spanning trees.

Every spanning tree on four vertices has three edges. With every edge weighted seven, all spanning trees weigh 3×7=21 and are minimum.

**Common misconception:** Counting graph edges rather than the three edges selected by a tree.

## Q12

**Correct answer:** B, D

Let q=P(A∩B). The feasible interval is max(0,0.8+0.7−1)≤q≤min(0.8,0.7), or0.5≤q≤0.7. B chooses0.6 and D implies q=0.5, both feasible. A is below the lower bound. C would give q=0.5·0.7=0.35, also impossible. A conditional probability must be compatible with the other supplied probabilities.

## Q13

**Correct answer:** 4

For A→B, the switch learns A on port1, but B is unknown, so it floods to ports2,3: two copies. B→A teaches B on port2 and is forwarded only to port1: one copy. C→A teaches C on port3 and also uses only port1: one copy. Total2+1+1=4. Learning uses source addresses; the first destination does not become known merely because it appeared as a destination.

## Q14

**Correct answer:** -0.1667 (range -0.16675–-0.16665)
**Concept:** A third-order limit.

The expansion sin x=x−x³/6+O(x⁵) gives limit −1/6. Equivalently, apply l'Hôpital three times to obtain −cos x/6 at zero. Rounded to four places, the answer is −0.1667.

**Common misconception:** Keeping only the linear approximation sin x≈x discards the leading term needed by this quotient.

## Q15

**Correct answer:** B, D

Concept: backward liveness. After `x=d`, only y is needed by return. Immediately before that assignment, d is needed as its source and y remains needed, so B and D are live after statement two. The old x is overwritten before any further use, making A false; c has already had its last use, making C false. Syntactic liveness precedes any deletion of the dead assignment.

## Q16

**Correct answer:** C

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Equivalent Boolean XOR forms.

A lists the two unequal-input minterms. Expanding B gives xx′+xy′+yx′+yy′=xy′+x′y, so B is identical. C is XNOR, true on equal inputs. D is also true at x=y=1, where XOR is false.

**Common misconception:** Confusing inclusive OR with exclusive OR.

## Q17

**Correct answer:** A

**Concept:** Left factoring with an empty suffix.

Extract the shared initial a, leaving suffixes b,c,ε. A produces exactly ab,ac,a. B puts the common a at the end; C permits arbitrarily long suffixes; D leaves X unreachable and produces only a.

**Common misconception:** Dropping ε when one production equals the common prefix.

## Q18

**Correct answer:** 1 (exact)
**Concept:** CSR decoding and strong connectivity.

Edges are 0→1,0→3,2→0,2→2,2→3,3→1. Vertex 2 reaches all vertices, and every vertex reaches sink 1. Adding 1→2 makes all vertices mutually reachable. Zero additions cannot suffice because 1 initially has no outgoing edge. Therefore the minimum is one.

**Common misconception:** The self-loop at 2 does not connect it back from other vertices.

## Q19

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The first p symbols are all a, so every permitted nonempty v consists solely of a's. Pumping down reduces only their count and leaves all p b's, proving A. B contradicts this location; C reverses the universal quantification required to refute the lemma; D violates |v|≥1. One convenient split is insufficient: the argument must cover all legal splits.

## Q20

**Correct answer:** 2

The old word has5+8=13 bits; the new one has3+8=11. Savings are2 bits. Six combinations fit in3 bits, but the unchanged address field must still be counted in both widths.

## Q21

**Correct answer:** B

Let initial a=a0 and b=b0. Then t=a0+b0, and the increment makes the last expression a0+1+b0=t+1. B is valid. A omits the increment; C subtracts instead of adding; D omits a0. The expression text repeats, but a's changed value prevents direct reuse of t without adjustment.

## Q22

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

SELECT DISTINCT x produces one row containing NULL. The outer COUNT(*) counts that row, giving1. COUNT(DISTINCT x), however, ignores NULL values and has no non-NULL distinct values to count, giving0. D is correct. A discards the surviving row, B fails to eliminate duplicates, and C treats the NULL as a counted value in Q2. A DISTINCT result row and a counted non-NULL aggregate input are different objects.

## Q23

**Correct answer:** 3
**Concept:** Binary-search trace.

The compared keys are 8, then 12, then 14. The third comparison finds equality. Midpoint rounding and the stated inclusive halves determine this sequence.

**Common misconception:** The worst-case search depth is not necessarily the depth of a particular target.

## Q24

**Correct answer:** 7

Concept: duplicate-suppressed flooding. Source S sends on its two incident links. Routers A and B each have degree three and each forwards on two links after its first arrival. C has degree two and forwards on one. Total=2+2+2+1=7 transmissions. Arrival order can choose which link is excluded but does not change these counts; later duplicates never trigger further sends.

## Q25

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Nonnegative rather than strictly positive weights.

Dijkstra requires no negative edge, so zero weights are permitted, A. Zero edges or equal-cost routes can give equal distances, C. Paths need not be unique, refuting B, and zero cycles do not decrease path costs without bound, refuting D.

**Common misconception:** Confusing zero-weight cycles with negative-weight cycles.

## Q26

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

A thread holding Y must already have acquired X, so two threads cannot split the locks in opposite acquisition orders. The common order excludes circular wait, proving B and disproving A. It gives neither equal waits nor absence of waiting, so C,D are false. Deadlock prevention is weaker than immediate access or fairness.

## Q27

**Correct answer:** 4

The visited bank numbers are3,1,7,5, then3. Equivalently the period is8/gcd(8,6)=4. The starting address shifts the visited residue class but does not change this period.

## Q28

**Correct answer:** -24

A unit lower triangular matrix has determinant1. The upper triangular determinant is2×(−3)×4=−24; multiplicativity gives det(A)=−24. No permutation sign is introduced because none is used.

## Q29

**Correct answer:** 2

**Concept:** Boolean dependence on a variable.

The two product terms cannot both be1. At a=1, f=b; at a=0, f=c. Flipping a changes the output precisely when b differs from c: assignments(0,1) and(1,0). Thus there are2 assignments.

**Misconception:** Counting both initial values of a even though the question asks for assignments to(b,c).

## Q30

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: sequential consistency and ordering cycles. Running A entirely before B yields (0,1), so A is possible; reversing their order yields (1,0), so C is possible. Performing both writes before both reads yields (1,1), so D is possible. To obtain (0,0), A's read must precede B's write and B's read must precede A's write. Together with the two program-order edges this would form a strict ordering cycle, impossible in a sequentially consistent total order. Thus B is false. Weak-memory outcomes must not be assumed under the stated stronger model.

## Q31

**Correct answer:** A, D

Dovetailing finds an accepting candidate if one exists, proving A. If M is total, every candidate test terminates, proving D. For arbitrary M, even the empty word can encode an unbounded acceptance computation, so finiteness of the candidate set does not give a decider, refuting B. The property is undecidable by reducing machine acceptance to a machine that simulates only on ε and rejects other candidates. If its complement were also recognizable, dovetailing both recognizers would decide it; hence C is false.

## Q32

**Correct answer:** 1

**Concept:** HAVING after NULL-sensitive aggregation.

Group A has one non-NULL v and group B two. Only B satisfies COUNT(v)=2, leaving one group.

**Common misconception:** Counting the NULL row in COUNT(v).

## Q33

**Correct answer:** 0.7854 (accepted range 0.78535–0.78545)

Write the integral as I. Replacing x by1−x leaves the denominator unchanged and yields numerator1−x. Adding the two forms gives2I=∫0¹ dx/[x²+(1−x)²]. Put u=2x−1; the last integral becomes∫(−1 to1) du/(1+u²)=π/2. Hence I=π/4≈0.785398. Symmetry replaces the numerator, not the denominator by a constant.

## Q34

**Correct answer:** 40

The transformed mean is10−2×4=2 and variance is(−2)²×9=36. Therefore E[Y²]=Var(Y)+(E[Y])²=36+4=40. Translation changes the mean but not variance; negative scaling still squares in the variance.

## Q35

**Correct answer:** 3

**Concept:** Epsilon closure and accepted words.

The start epsilon closure reaches b. From b, any number of zeros may be consumed, followed by at least one 1 to reach c; further ones stay in c. The language is 0*1+. Length-three words are 001,011,111: three.

**Common misconception:** Counting epsilon moves as input symbols or allowing zeros after reaching c.

## Q36

**Correct answer:** 200

**Concept:** Fragment payload and offset units.

The payload is 2000 bytes. Each full fragment can carry 820−20=800 bytes, already divisible by eight. Payload sizes are 800,800,400. The last starts 1600 data bytes after the original payload's start, so its encoded offset is 1600/8=200.

**Common misconception:** Including fragment headers in payload offsets or reporting byte units instead of eight-byte units.

## Q37

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The consumer takes mutex then blocks on full=0, proving A. A producer can take an empty slot token but cannot take mutex, so it cannot insert and signal full, proving B. Any initially empty finite buffer still starts full=0, so merely increasing capacity does not fix the ordering, disproving C. Waiting for an item before taking mutex avoids holding that mutex while waiting on full, proving D.

## Q38

**Correct answer:** 8 (exact)

**Concept:** Databases — B-trees and B+ trees

Inserting 35 splits the middle leaf into [20,25] and [30,35]. The root now has four children and separators 20,30,40. Split it into two internal nodes, with separator 30 in a new root. The two child internal nodes have separators 20 and 40. At this point there are four leaves, two internal children and one root: seven nodes.

Inserting 55 splits [40,45,50,55] into [40,45] and [50,55]. Its parent acquires separator 50 and has three children, so it does not overflow. The final tree has five leaves and three internal nodes, for eight nodes.

**Common misconception:** A leaf split can trigger an internal split and creation of a root; later splits need not propagate to the root.

## Q39

**Correct answer:** 0.375
**Concept:** Conditional permutations and derangements.

There are 5!−4!=96 permutations in which 1 is not fixed. For exactly one fixed point, choose it from the other four elements, then derange the remaining four: !4=4!(1−1+1/2!−1/3!+1/4!)=9. Favourable count is 4×9=36. Conditional probability is 36/96=0.375.

**Common misconception:** After choosing the sole fixed point, every remaining element—including 1—must be deranged.

## Q40

**Correct answer:** 24

The first triangle has 3!=6 colorings. Once its bridge endpoint's color is fixed, the second bridge endpoint has two choices. Its remaining two triangle vertices must use the two other colors, in 2!=2 orders. Thus 6×2×2=24. Multiplying two independent triangle counts would ignore the bridge restriction.

## Q41

**Correct answer:** 5

**Concept:** SQL bag semantics.

Each of the two copies of 1 joins to 2 and 3, contributing four rows. The single 2 joins to 3, contributing one more. Equal values do not join under strict inequality. Total five rows.

**Common misconception:** Deduplicating input values when neither DISTINCT nor a set operation is present.

## Q42

**Correct answer:** 203

The first four issues occur at0,1,2,3 and complete at100,101,102,103. Each completion frees a slot for another issue in that same cycle. Those four new requests finish at200,201,202,203. The last completion is203. Unlimited parallelism would wrongly allow all eight misses to issue by7; fully serial service would ignore the four outstanding slots.

## Q43

**Correct answer:** 16
**Concept:** Width and depth expansion of memory chips.

Two four-bit-wide chips in parallel provide one eight-bit byte at each of 8K addresses, making an 8 KiB bank. Eight such banks provide 64 KiB. Total chips are 2×8=16. Equivalently, total required bits divided by bits per chip gives (64×1024×8)/(8×1024×4)=16.

**Common misconception:** A chip word is four bits here, not a byte; both width and address depth must be expanded.

## Q44

**Correct answer:** A, B, D

p is a valid one-past pointer. Subtracting a within the same array yields3(A), stepping back and dereferencing yields6(B), and comparing with the same one-past pointer is defined(D). Dereferencing p itself accesses no array element and is undefined(C). Formation and comparison of one-past pointers are permitted; dereference is not.

## Q45

**Correct answer:** A, C

A establishes descending score order first; the later stable department sort groups departments while retaining that score order and original tie order within each. C directly uses the desired composite key and stability, so both work. B makes score the primary final key and can intermix departments. D reverses the original order of equal-key records, which later stable sorts retain rather than restore. Stable multi-pass sorting processes the least significant key first.

## Q46

**Correct answer:** 3

Concept: primitive cyclic arrangements. There are C(6,3)=20 labelled words. A smaller least period divides six. Period one cannot give three ones; period three repeats twice and has an even total number of ones. Period two gives only 010101 and 101010. Excluding these leaves 18 words, each in an orbit of six distinct rotations. Therefore 18/6=3 classes. Division by six is valid only after removing shorter-period words.

## Q47

**Correct answer:** 32 (exact)
**Concept:** Coupled recursion and a two-step invariant.

Substitute twice: f(n)=2f(n−2) and g(n)=2g(n−2). For even n=2k, f(n)=2^k f(0). Hence f(10)=2⁵=32. The simultaneous recurrence must use both previous values, not a newly updated one.

**Common misconception:** Sequentially updating the two quantities can accidentally implement a different recurrence.

## Q48

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Ordered parse trees and language versus grammar ambiguity.

Let c_n count trees with n a-leaves. c_1=1 and c_n=Σ(c_i c_(n−i)), giving c_2=1,c_3=2,c_4=5,c_5=14. Every tree has exactly one leftmost derivation, so A,B hold. A tree also has a rightmost derivation, but that is not a new tree; C is false. The generated language is a+, a regular language, so D is true.

**Common misconception:** An ambiguous context-free grammar can generate a regular language.

## Q49

**Correct answer:** A, C

Concept: nondeterministic midpoint matching. To consume abba and empty its pushed portion, push and matching lengths must both be two, proving A. The matched suffix ba is the reversal of prefix ab. A guess after one symbol cannot ignore a mismatch or extra input, so B is false. For abab the only possible balanced lengths are two and two, but suffix ab is not the reversal ba, so C is true. Nondeterministic acceptance needs one successful branch; incorrect guesses do not invalidate another accepting branch, so D fails.

## Q50

**Correct answer:** 2

The original orbit is2,10,6,2,... because gcd(8,12)=4. Those three slots are occupied. With step5 the probes begin2,7; slot7 is empty. Thus two probes suffice. A table can have free slots while a non-coprime probe step fails to reach them.

## Q51

**Correct answer:** A, B, C

After b, the relevant items include S→b·Ac, S→b·da, and A→·d. Shifting d gives the two LR(0) items in A. FOLLOW(A)={a,c}, so SLR reduces A→d on a while S→bd·a shifts a: B holds and D fails. In canonical LR(1), A was introduced here only by S→b·Ac, so its lookahead is c. Reducing on c and shifting on a are compatible, establishing C. FOLLOW merges contexts that LR(1) lookaheads keep separate.

## Q52

**Correct answer:** A

Candidates II, IV are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) IV.
- **D: Incorrect.** It includes invalid candidate(s) I, III and omits valid candidate(s) II, IV.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: instance-level functional dependencies. Each AB pair occurs once, so AB→C holds (B). Repeated C=p always has B=x; q and r each have B=y, so C→B holds (D). A=1 has C=p and q, disproving A. C=p occurs with A=1 and 2, disproving C. A dependency is checked by equal determinant values, not by counting columns or rows alone.

## Q53

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Counting-semaphore permits.

Each signal contributes one permit, and Q needs two, so eventual scheduling lets it print (A). If Q arrives before the first signal it blocks, proving C. Counting permits do not collapse (B false), and Q cannot complete both waits before the second permit is produced (D false).

**Common misconception:** Counting semaphores preserve multiple permits, unlike a single Boolean notification flag.

## Q54

**Correct answer:** 8

**Concept:** Pointer-to-row indexing.

p+1 points to the second three-element row; *(*(p+1)+2) is its third element, 6. (*p)[1] is the second element of the first row, 2. Their sum is eight.

**Common misconception:** Advancing a pointer-to-array by one integer instead of by one full row.

## Q55

**Correct answer:** 76

**Concept:** Array strides and lower-bound adjustment.

The final dimension has three elements, and the middle dimension four. Adjusted indices are 0−(−1)=1, 4−2=2, and 1−0=1. The linear element offset is (1×4+2)×3+1=19, giving 19×4=76 bytes.

**Common misconception:** Using raw indices without subtracting nonzero lower bounds.

## Q56

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

For fixed i, the inner work is1+2+4+...+2^floor(log2 i), which lies between i and2i. Summing over i=1..n givesΘ(n²), so B is correct. A counts doubling iterations but ignores their growing work; C multiplies by a spurious log factor; D ignores the outer linear range. Geometric inner workloads must be summed, not bounded by their maximum at every iteration.

## Q57

**Correct answer:** 7
**Concept:** State transition tracing of a feedback shift register.

Applying all next-state equations simultaneously gives 001→011→111→110→101→010→100→001. No earlier state equals the initial state. The first return is after seven edges.

**Common misconception:** Next-state equations all use the old bits; updating bits sequentially computes a different machine.

## Q58

**Correct answer:** 7.3333 (accepted range 7.33325–7.33335)

Execution intervals are A0–2,B2–4,C4–5,A5–7,B7–8,A8–9. Completion times are A9,B8,C5, and all arrivals are0. Mean turnaround is22/3≈7.3333. Waiting time would additionally subtract CPU bursts.

## Q59

**Correct answer:** 4
**Concept:** FOLLOW through nullable sequences.

In S→ABc, the suffix after A is Bc. B can start with a via A, d via nullable A followed by D, or b directly; B can also vanish, exposing c. Thus a,b,c,d all enter FOLLOW(A). In B→AD, D contributes d and can vanish, so FOLLOW(B) contributes c, adding nothing new. FOLLOW(A) is exactly {a,b,c,d}, of size four. The trailing c in S prevents an end marker from propagating to these occurrences.

**Common misconception:** A nullable symbol requires examining the entire suffix, not only the next symbol's nonempty FIRST set.

## Q60

**Correct answer:** 4

The specified indexed lookup reads root, one lower index block, and one data block:3 reads. Against the stated7-read binary-search worst case, it saves4. There is no cache assumption that permits omitting the root read. The index's4 physical blocks are not all read in one lookup.

## Q61

**Correct answer:** A, C

**Concept:** Theory of Computation — Closure properties and regular restrictions

1. L is context-free: it is the union of the context-free languages with i=j and with j=k. R is regular, expressed as a*(epsilon|b|bb)c*.
2. For each fixed j in {0,1,2}, membership of L intersect R requires i=j or k=j. Its portion for that j is a^j b^j c* union a* b^j c^j. These are regular, and their finite union is regular.
3. L minus R equals L intersect the complement of R. A context-free language intersected with a regular language remains context-free.
4. L minus R is not regular. Intersect it with the regular language a*b* (no c symbols). Since j>2, the alternative j=k=0 is impossible, leaving {a^n b^n:n≥3}, which is nonregular. A regular L minus R could not have this nonregular regular-language intersection.
5. In L intersect S we have i=k, together with i=j or j=k. Either alternative forces all three counts equal. Thus the intersection is {a^n b^n c^n:n≥0}, which is not context-free. For the standard pumping argument, choose a^p b^p c^p: a pumping window of length at most p cannot cover all three blocks, so pumping changes at least one count while leaving another unchanged, or violates block order.

- **A:** Correct: the middle block is bounded, giving a finite union of regular languages.
- **B:** Incorrect: the c-free regular slice proves nonregularity.
- **C:** Correct: difference by a regular language preserves context-freeness.
- **D:** Incorrect: the equal-outer-count restriction forces three equal block counts.

**Common misconception:** Intersection with a regular language preserves context-freeness, but intersection with another context-free language need not; bounded and unbounded restrictions behave differently.

## Q62

**Correct answer:** 958200

**Concept:** CPU overhead under different I/O mechanisms.

Interrupt-driven cost is 12000×80=960000 cycles. DMA uses twelve blocks, costing 12(120+30)=1800 cycles. Savings are 960000−1800=958200 cycles.

**Common misconception:** Omitting per-block setup or counting DMA completion interrupts per byte.

## Q63

**Correct answer:** 29

With no2s, there are2⁴=16 strings. With exactly two2s, they must form one adjacent pair: three positions for that pair and2² assignments to the other positions, giving12. With four2s, only2222 occurs, adding1. Odd numbers of2s cannot have all runs even. Thus a4=16+12+1=29. Counting a pair as an independent block is safe here because the four2 case is handled separately.

## Q64

**Correct answer:** 2

The free addresses are.64 through.191, totaling128. This interval is not aligned to a /25 boundary; a single /25 starts at.0 or.128 and would include reserved addresses. Two /26 prefixes,.64/26 and.128/26, cover the interval exactly. Address count alone does not establish CIDR alignment.

## Q65

**Correct answer:** 218

SCAN travels50→199→20, a distance149+179=328. LOOK travels50→90→20, a distance40+70=110. The extra distance is218=2(199−90). The stop rule excludes any additional travel after servicing20; otherwise endpoint conventions could change the answer.

