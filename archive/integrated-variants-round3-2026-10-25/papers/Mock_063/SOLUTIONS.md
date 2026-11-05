# Worked Solutions — Mock Test 063

## Q1

**Correct answer:** B

Concept: induction versus proof. The observation establishes correctness only on the tested executions, which is B. A extrapolates to all programs, C invents universal failure outside the suite, and D denies the possibility of a revealing new test. Finite testing alone is not a universal correctness proof.

## Q2

**Correct answer:** 4
**Concept:** Ratios at different times.

Write present ages as 4k,3k. Then 5(4k+8)=6(3k+8), so 2k=8 and k=4. The present ages are 16 and 12, whose difference is 4. Eight years later they are 24 and 20, confirming the ratio 6:5.

**Common misconception:** Equal additions to ages do not preserve their ratio.

## Q3

**Correct answer:** C

The required numerical answer is **10**, so select **C**.

The increment2n+1 is (n+1)²−n², so telescoping gives an=n²+1. The strict condition n²+1>100 holds first at n=10, since a9=82 and a10=101. The initial value adds1 to the usual square sequence.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 10 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -5 and is outside the source answer's accepted range.
- **C: Correct.** It matches the derived answer at the required precision.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q4

**Correct answer:** C

The required numerical answer is **49**, so select **C**.

The two base triangles are similar, so their base ratio is sqrt(9/16)=3/4. The two side triangles each have area sqrt(9×16)=12, by the shared-height area ratios induced by the diagonal intersection. Total9+16+12+12=49. Equivalently, total area is(sqrt9+sqrt16)²; simply adding the given areas omits the side triangles.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 49 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -24 and is outside the source answer's accepted range.
- **C: Correct.** It matches the derived answer at the required precision.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q5

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

In C, the introductory phrase modifies the subject technician, assigning the haste correctly. A grammatically attaches the introductory modifier to instrument; D explicitly describes the instrument as hurried. B's wording is unnatural and does not correctly express the intended modifier relationship. A human performer should be the subject governed by this introductory phrase.

## Q6

**Correct answer:** 28.5714 (accepted range 28.57135–28.57145)

Normalize the budget to100. Food rises from40 to50, and other costs remain25, leaving25 for transport instead of35. The reduction is10 out of35, or100·10/35=200/7≈28.5714%. The denominator is the original transport allocation, not the total budget.

## Q7

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

If p were true, the implication would force q true, contradicting exactly one true proposition. Thus A holds. The sole true proposition must be q or r, giving B and D. Either can be the true one, so C is not forced.

## Q8

**Correct answer:** C

The required numerical answer is **6**, so select **C**.

**Concept:** Area divisibility plus constructive tiling.

Every tile has area six, so an integer square side s must have s² divisible by both two and three. Thus s is divisible by six and cannot be smaller than six. A 6×6 square can be divided into three rows of height two and two columns of width three, proving feasibility.

**Common misconception:** Giving an area bound without showing a tiling exists.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 6 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -3 and is outside the source answer's accepted range.
- **C: Correct.** It matches the derived answer at the required precision.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q9

**Correct answer:** C

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The observed group difference establishes association in this sample, proving A. Optional enrolment and absent baseline information leave alternative explanations, so B is true. C claims individual causal improvements unsupported by the data. D invents equality of prior achievement. A group mean comparison alone cannot remove selection effects.

## Q10

**Correct answer:** B

The required numerical answer is **84**, so select **B**.

**Concept:** Integer optimization with a capacity constraint.

Let x items use A and 20−x use B. Time is 2x+20−x=20+x≤28, so x≤8. Cost is 3x+5(20−x)=100−2x, decreasing in x. Choose x=8, giving cost 84 and exactly 28 hours.

**Common misconception:** Choosing the cheaper method for every item without checking time feasibility.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 84 and is outside the source answer's accepted range.
- **B: Correct.** It matches the derived answer at the required precision.
- **C: Incorrect.** Its value differs from the required answer by -42 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q11

**Correct answer:** 1

After both unlinks, the link count is zero but one open reference remains. Closing its descriptor removes that final reference, allowing reclamation. One further operation is needed. Unlinking names is not the same as closing open-file references.

## Q12

**Correct answer:** D

The required numerical answer is **4**, so select **D**.

**Concept:** Computer Organization and Architecture — Cache mapping

All references map to set 0. References 0 and2 miss and fill both lines. The next0 hits and makes2 least recently used. Reading 4 misses and evicts 2. The final2 therefore misses, evicting0. There are four misses; set 1 is unused.

**Common misconception:** Total cache capacity does not prevent conflicts when blocks map to one set.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 4 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -2 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q13

**Correct answer:** B

The required numerical answer is **4**, so select **B**.

**Concept:** Grammar-induced associativity.

The left-recursive production groups the expression as (9−3)−2. Attributes compute 6, then 4. The parse does not group it as 9−(3−2).

**Common misconception:** Evaluating a chain using an associativity inconsistent with its parse tree.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 4 and is outside the source answer's accepted range.
- **B: Correct.** It matches the derived answer at the required precision.
- **C: Incorrect.** Its value differs from the required answer by -2 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q14

**Correct answer:** D

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) I, IV and omits valid candidate(s) II, III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Physical sharing versus metadata representation.

A frame may have several virtual aliases, making B true. A single stored pair can equal only one of the two distinct(process, virtual-page) pairs, so A is false. Retaining a list of aliases permits lookup of both and resolves this particular representation problem, so C is true. Different virtual page numbers can map to the same physical frame; D is false.

**Misconception:** Treating a limitation of a simplified page-table format as a hardware prohibition on sharing.

## Q15

**Correct answer:** D

The required numerical answer is **0.48**, so select **D**.

After the first key chooses any bucket, the second must avoid one bucket (probability4/5) and the third avoid two (3/5). Product12/25=0.48. Uniform independent placements allow multiplication of these conditional probabilities.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 0.04 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -0.24 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 0.26 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q16

**Correct answer:** 12

**Concept:** Bounded positive compositions.

Without upper bounds there are choose(7,2)=21 positive triples. If x≥5, setting x′=x−4 leaves three positive entries summing to four, giving choose(3,2)=3 choices; similarly for y or z. Two entries cannot both be at least five. Therefore 21−3×3=12.

**Common misconception:** Applying a nonnegative-composition formula without adjusting positivity.

## Q17

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Bounded simulation and decidability.

A is decidable by simulating at most 100 transitions. C is decidable by checking whether any rejecting state is reachable from the DFA's start state. B is the general halting problem. D is undecidable: given machine M and input w, construct a machine that ignores its own input and simulates M on w; it halts on all inputs exactly when M halts on w.

**Common misconception:** A finite description does not imply a computable bound on an arbitrary computation's duration.

## Q18

**Correct answer:** B

The required numerical answer is **3**, so select **B**.

1. Track E0: even b count but not currently accepting; E1: even b count and last symbol a; O: odd b count. In O the last symbol does not affect future acceptance, so one state suffices.
2. Transitions are E0 --a--> E1, E1 --a--> E1, both E states --b--> O; O --a--> O and O --b--> E0. E0 is initial and E1 alone accepts.
3. E1 is distinguished from the others by the empty suffix; E0 and O are distinguished by suffix a. All three are reachable, proving minimality.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 3 and is outside the source answer's accepted range.
- **B: Correct.** It matches the derived answer at the required precision.
- **C: Incorrect.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q19

**Correct answer:** B

Static links implement lexical scope, so R refers to its lexical parent P. Dynamic links implement return/unwinding along actual calls, so R's caller Q is identified. Thus B; A confuses lexical and dynamic parents, C swaps them, and D ignores the actual caller. Sibling procedures share a lexical parent without calling through it.

## Q20

**Correct answer:** C

The required numerical answer is **1040**, so select **C**.

Concept: lower-bound-adjusted indexing. Each row has four elements. Element offset=(4−2)·4+(1−(−1))=10. Byte address=1000+4·10=1040. Both index origins must be subtracted before computing the offset.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 1040 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -520 and is outside the source answer's accepted range.
- **C: Correct.** It matches the derived answer at the required precision.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q21

**Correct answer:** D

The required numerical answer is **30**, so select **D**.

**Concept:** Coloring a cycle.

For a cycle of length n, the number of labelled q-colorings is (q−1)ⁿ+(−1)ⁿ(q−1). Taking n=5,q=3 gives 2⁵−2=30. One derivation fixes the first color and tracks whether the current path endpoint equals that color: if E_k,D_k are counts, E_{k+1}=D_k and D_{k+1}=2E_k+D_k, starting E_1=1,D_1=0. This gives D_5=10, and multiplying by three first-color choices gives 30.

**Common misconception:** Coloring a path and then forgetting the closing edge overcounts cycle colorings.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 30 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -15 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q22

**Correct answer:** D
**Concept:** Harmonic running-time sum.

For a fixed i there are floor(n/i) calls. Their sum is Θ(nH_n)=Θ(n log n): replacing each floor by n/i changes the sum by less than n. A and C underestimate the harmonic accumulation; B treats the inner loop as n iterations for every i.

**Common misconception:** A nested loop need not be quadratic when its step size depends on the outer index.

## Q23

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Reachability of negative cycles.

The only path to b is s→a→b, of length five. Neither c nor d is reachable, so their negative cycle cannot affect paths from s. A,C hold; B,D incorrectly apply an unreachable cycle to reachable distances.

**Common misconception:** A negative cycle matters to a source-to-target distance only when it can participate in a source-to-target walk.

## Q24

**Correct answer:** 1

All four inputs with a=0 are on-set or don't-care, so cube NOT a covers them and contains one literal. Any expansion to a literal-free cube would include off-set inputs with a=1. Thus this is the largest permissible prime cube that covers the on-set. Don't-care inputs may assist expansion but cannot override specified zeros.

## Q25

**Correct answer:** 0.3466 (range 0.34655–0.34665)
**Concept:** Integration by substitution.

Set u=1+x², so du=2x dx. The integral becomes (1/2)∫₁² du/u=(ln 2)/2≈0.3465735903, which rounds to 0.3466.

**Common misconception:** The substitution introduces a factor of one-half and changes both limits.

## Q26

**Correct answer:** A

The required numerical answer is **3**, so select **A**.

Concept: pointer rewiring. After swapping the two links, 1 points to 4 and 3 points to 2; the other links remain 4→3 and 2→1. Starting at 1, two traversals give 1→4→3, hence three. Track actual pointers rather than the original list memberships.

**Option check**
- **A: Correct.** It matches the derived answer at the required precision.
- **B: Incorrect.** Its value differs from the required answer by 3 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q27

**Correct answer:** A

The required numerical answer is **3**, so select **A**.

Between polls0 and25, arrivals occur at10 and20. Between25 and50, arrivals occur at30,40,50, with the arrival at50 preceding the poll. The pattern repeats every50 microseconds, so at most three bytes accumulate, and that number is attained. Capacity2 overflows before the poll at50.

**Option check**
- **A: Correct.** It matches the derived answer at the required precision.
- **B: Incorrect.** Its value differs from the required answer by 3 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q28

**Correct answer:** 500

**Concept:** Cumulative acknowledgment boundaries.

ACK2500 acknowledges every byte below2500, covering the first three listed segments. Only[2500,3000), of length500, remains unacknowledged among the listed bytes. The acknowledgment number names the next expected byte, not the last received byte.

**Misconception:** Counting byte2500 as acknowledged or assuming the ACK covers only one segment.

## Q29

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

After buffered data is drained, orderly end-of-stream is reported by a zero return on a positive-length receive(A). TCP supports independent directional shutdown, so continued sending can remain valid(C). Zero here is a count, not a delivered data byte(B), and TCP supplies a byte stream without a separate application shutdown record(D).

## Q30

**Correct answer:** 2

x XOR x is always0, so the output is0 OR y=y. The assignments with y=1 and either x value produce1, giving two. Tied inputs are not independent signals.

## Q31

**Correct answer:** D

The required numerical answer is **2**, so select **D**.

Concept: rank and consistency. Row three is row one plus row two; the first two rows are independent. Consistency requires 3=1+t, so t=2. Then rank is two in three unknowns, leaving one free parameter and infinitely many solutions. A dependent coefficient row does not guarantee consistency for arbitrary right-hand sides.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 2 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q32

**Correct answer:** C

The required numerical answer is **0**, so select **C**.

The derivative at zero is the limit of [f(h)−f(0)]/h=h sin(1/h). Its absolute value is at most|h|, tending to zero. Thus f'(0)=0. Substituting zero into the expression for f'(x) valid only at nonzero x is not justified.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by 2 and is outside the source answer's accepted range.
- **C: Correct.** It matches the derived answer at the required precision.
- **D: Incorrect.** Its value differs from the required answer by 3 and is outside the source answer's accepted range.


## Q33

**Correct answer:** D
**Concept:** Direct-mapped conflicts.

Pairs A,B,C map to the same line within each pair: residues 1,2,3 respectively. Blocks 4 and 5 map to lines 0 and 1 and can coexist. Thus D is correct.

**Common misconception:** Distinct memory blocks can still compete for exactly the same direct-mapped cache line.

## Q34

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

This is write skew under the stated snapshot rule. The write sets are {A} and {B}, so both pass the conflict test and both flags become zero: A,C,D are true. In either serial order, the second transaction sees the first flag cleared and does not clear its own flag, making B false. Disjoint writes do not imply preservation of an invariant involving both items.

## Q35

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** DNS record types.

AAAA records associate names with IPv6 addresses, A. Ethernet addresses, TCP sequence information and HTTP bodies belong to different mechanisms, eliminating B,C,D.

**Common misconception:** Confusing address resolution at different network layers.

## Q36

**Correct answer:** 78

The clock period is maximum stage delay5 plus overhead1, or6 ns. Four cycles produce the first result and nine more produce the next nine, totaling13 cycles. Time13×6=78 ns. Sum of unpipelined stage delays is not the pipeline clock period.

## Q37

**Correct answer:** 258

LOOK travels50→70→20, distance20+50=70. SCAN travels50→199→20, distance149+179=328. The excess is328−70=258, twice the unnecessary outward distance199−70. Both stop at20 because no requests remain; do not add a final sweep to cylinder0.

## Q38

**Correct answer:** D

The required numerical answer is **3**, so select **D**.

Compute t=a+b, u=t*t, x=u+t: three binary operations. Sharing avoids reevaluating a+b. All three distinct required operations remain under this stated local optimization.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 3 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q39

**Correct answer:** 2

**Concept:** Ties among optimal compatible subsets.

Before time 4, either A and B together or C alone gives value eight, and no compatible selection exceeds eight. D is compatible with both and adds one, giving optimal value nine. The two maximizing subsets are {A,B,D} and {C,D}.

**Common misconception:** Returning one optimal solution without counting another with the same value.

## Q40

**Correct answer:** C
**Concept:** Recursion-tree cost with a nonuniform nested loop.

For each i, there are i iterations of j and Θ(log i+1) iterations of k. Summing gives Θ(n² log n), using the i values from n/2 through n for a matching lower bound. The recurrence is T(n)=2T(n/2)+Θ(n² log n). At successive recursion depths the quadratic factor drops geometrically after accounting for the number of subproblems, so total cost remains Θ(n² log n). A loses a loop factor; B loses the k loop's logarithm; D adds an unnecessary logarithm for recursion depth despite the geometric decrease.

**Common misconception:** Multiplying root work by recursion depth is incorrect when per-level work decreases geometrically.

## Q41

**Correct answer:** 4

Concept: Mealy-style output to Moore-state memory. A reached state must encode the preceding bit for the next output and the output currently displayed. All four pairs (preceding bit,last output) are reachable. States with different displayed outputs are distinct immediately; states with the same displayed output but different preceding bits produce different outputs upon the next zero. Thus four are necessary and sufficient. The initial state can share the state for (0,0), since its initial output is ignored.

## Q42

**Correct answer:** D

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Process-image replacement versus process identity.

The specified semantics preserve the PID and unmarked descriptors while replacing the address space, directly giving A and B. Old heap pointers have no guarantee of their old objects after replacement, refuting C. D contradicts the descriptor-preservation rule.

**Common misconception:** Treating successful exec as creation of a new process or preservation of the old memory image.

## Q43

**Correct answer:** 1

Rear advances for six successful enqueues in total, ending at6 modulo5=1. Front advances twice to2; the queue then holds four elements, the maximum allowed with one reserved slot. Dequeues do not move rear.

## Q44

**Correct answer:** A, C

TCP offers a byte stream, not application-write messages, proving A. UDP datagrams can be carried in multiple IPv4 fragments, refuting B; IP reassembly can present the complete datagram to UDP, proving C. Routers replace link-specific framing on different links, refuting D. Transport units and link/network transmission units need not align one-for-one.

## Q45

**Correct answer:** 24
**Concept:** Full binary recursion trees.

Every internal invocation has exactly two children; there are 13 unit-segment leaves. A full binary tree with L leaves has L−1 internal nodes, so there are 13+12=25 invocations and markers. In postorder the root emits last. Immediately before that final emission, the other 24 have been emitted.

**Common misconception:** Unequal split sizes change the shape but not the full-binary-tree leaf/internal-node identity.

## Q46

**Correct answer:** 30

**Concept:** Product scaling in fixed-point arithmetic.

The represented values are 24/16 and 20/16. Their product has raw integer numerator 480 and scale 256. To return to scale 16, divide 480 by 16, giving encoded integer 30 exactly. No rounding adjustment is necessary in this case.

**Common misconception:** Retaining the doubled fractional-bit scale as if it were the destination format.

## Q47

**Correct answer:** 0.3210 (accepted range 0.32095–0.32105)

Of 27 equally likely ordered draws, 3 have one distinct colour and 6 have all three; the remaining 18 have exactly two. Therefore E[D]=(3+36+18)/27=19/9 and E[D²]=(3+72+54)/27=43/9. Variance is 43/9−(19/9)²=26/81≈0.32098765, rounding to 0.3210. The number of distinct colours is not binomial because colour-presence indicators are dependent.

## Q48

**Correct answer:** 24
**Concept:** Strong components of a tournament.

There are 64 orientations in total. A non-strong tournament on four vertices is either transitive, giving 4!=24 orders, or consists of a directed three-cycle and a fourth vertex that beats all three or loses to all three. The latter gives 4 choices of singleton, 2 cycle orientations, and 2 directions, totaling 16. These cases are disjoint and exhaustive because a nontrivial strongly connected tournament needs at least three vertices. Therefore strongly connected tournaments number 64−24−16=24.

**Common misconception:** A tournament with a directed cycle need not be strongly connected as a whole.

## Q49

**Correct answer:** A, B, D

**Concept:** Engineering Mathematics — Eigenvalues and eigenvectors

1. Bu=Au+u(v^T u)=2u-2u=0, so zero is an eigenvalue.
2. Choose a basis (u,w1,w4) in which Aw1=w1 and Aw4=4w4. Distinct eigenvalues ensure this is a basis. In this basis A is diag(2,1,4), and u v^T has nonzero entries only in its first row, whose first entry is -2.
3. Therefore B is upper triangular with diagonal (0,1,4). These distinct real eigenvalues make B diagonalizable, and exactly two are nonzero, so rank(B)=2.
4. Commutation need not hold. In this basis choose v^T=(-2,1,0). Then B has first row (0,1,0); AB has entry (1,2)=2, whereas BA has that entry 1. A and B do not commute.

- **A:** u is a nonzero vector in the null space of B.
- **B:** The three eigenvalues are 0,1,4, all distinct and real.
- **C:** The explicit choice A=diag(2,1,4), u=(1,0,0)^T, v=(-2,1,0)^T is a counterexample.
- **D:** Similarity to a diagonal matrix with exactly two nonzero entries gives rank two.

**Common misconception:** A rank-one change need not commute with the original matrix, even when its image is an eigenspace.

## Q50

**Correct answer:** 32

**Concept:** Constrained univariate maximization.

Substitute y=6−x to get h(x)=6x²−x³ on [0,6]. Its derivative is 3x(4−x), so the interior maximum is at x=4,y=2 and equals 32. Both endpoints give zero.

**Common misconception:** Assuming symmetry forces x=y even when the objective weights them differently.

## Q51

**Correct answer:** A, B

Concept: CFG language and ambiguity. Productions create only a symbols, and repeated concatenation generates any number, including zero, so A holds. A tree for a can be wrapped as S→SS with one child deriving ε, repeatedly, producing infinitely many distinct trees; B holds. That also disproves C. An LL(1) grammar is unambiguous, and this grammar additionally has immediate left recursion, so D fails. Infinitely many derivations here correspond to genuinely different trees, not merely different expansion orders.

## Q52

**Correct answer:** 240

Concept: ER cardinality as a surjective assignment. Five employees distributed among four nonempty departments must have group sizes 2,1,1,1. Choose the pair of employees in C(5,2)=10 ways, its department in four ways, then biject the remaining employees to the three departments in 3!=6 ways. Total=10·4·6=240. Relationship instances distinguish employee and department identities.

## Q53

**Correct answer:** A, C, D

For false flag both blocks end with x=0,y=1, proving A. For true flag the original produces x=1,y=2 while the proposal produces x=1,y=1, refuting B. The conditional assignment invalidates an unconditional x=0 assumption, proving C. If y is unobservable and only the stated operations occur, both blocks leave the same x for either flag, proving D. Correct optimization depends on both control flow and which results are observable.

## Q54

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

R−S={(1,y),(2,x)}, so its A-projection is{1,2}, proving A. Separately the projections are{1,2} and{1}, whose difference is{2}, proving B. The surviving(1,y) gives D and directly disproves C's proposed distributivity. Projection can collapse tuples that difference distinguishes.

## Q55

**Correct answer:** 1601

In milliseconds, circuit time is1+L/2000 and packet time is(L+100·ceil(L/900))/1000. Circuit wins exactly when L+200·ceil(L/900)>2000. For1≤L≤900, the left side is at most1100. For901≤L≤1800, it becomes L+400 and exceeds2000 first at L=1601. This is the first qualifying range, so1601 is minimal. Equality at1600 is not a strict win.

## Q56

**Correct answer:** A, B, C

Near1.5, adjacent representable values are1.375,1.5,1.625, with spacing0.125. The midpoint boundaries are1.4375 and1.5625. The significand of1.5 is1.100, whose last retained bit is even; both ties therefore round to1.5. A,C are included, B is strictly inside the interval, and D is already exactly represented at1.625. Ties on both sides can select the same even significand.

## Q57

**Correct answer:** A

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The error is explicitly a multiple of g, so its remainder is zero, proving A. Adding it to a valid codeword leaves a divisible polynomial, proving B. C contradicts this construction. The polynomial has three nonzero terms at shifted degrees, not one, refuting D. CRC detection depends on divisibility, not merely on nonzero errors.

## Q58

**Correct answer:** D

The required numerical answer is **-5**, so select **D**.

**Concept:** Depth changes under rotation.

After the left rotation, x moves down one level and y up one, cancelling their contributions. Every node in A moves down one (+4 total), every node in C moves up one (−9), and B's nodes remain at the same depth. Nodes outside the rotated subtree are unchanged. Net comparison-count change is 4−9=−5.

**Common misconception:** Moving B's nodes with y even though the rotation reattaches B beneath x at their original depth.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by -5 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by 2 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q59

**Correct answer:** D

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I, IV and omits valid candidate(s) II, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Lost updates under atomic individual accesses.

If both loads read zero before either store, both later store one, yielding B. If one complete increment precedes the other's load, the result is two, C. A store always writes at least one, so final zero is impossible; with only two increments no load can see two before a third increment, so three is impossible.

**Common misconception:** Treating a source-level increment as atomic despite its specified separate steps.

## Q60

**Correct answer:** 102

Concept: variable instruction lengths and branch base. Branch starts at 100+2+4=106; next-instruction address=108. Displacement is −3·2=−6 bytes. Target=108−6=102. Neither branch-start addressing nor treating the displacement as bytes matches the stated architecture.

## Q61

**Correct answer:** 2

First100+60=160 exceeds127, wraps to−96 and overflows. Then−96−60=−156 is below−128, wraps to100 and also overflows. Both operations signal overflow, although the final wrapped result equals the original x. Algebraic cancellation of the final result does not eliminate intermediate overflow flags.

## Q62

**Correct answer:** 5

Start at height1. Two a's push four symbols, reaching height5; the following four b's return it to1 without underflow. The maximum is5. Include the bottom marker and the two-symbol push rule.

## Q63

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Each component is context-free: a PDA matches the first two blocks for L1 or the last two for L2. Union closure proves A. Membership in both forces all three counts equal, proving C. That intersection is the standard non-context-free three-equal-block language and therefore is not regular, disproving B. If the union were regular, intersecting it with the regular language a+ b+ (no c) would be regular. That intersection is {a^n b^n:n≥1}, which is nonregular, so D is false. The regular restriction excludes L2's c-free strings with positive b-count.

## Q64

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Summing coupled loop costs.

For each i, work runs i floor(n/i) times, at most n, giving O(n²). For i>n/2, floor(n/i)=1, and the sum of these i values alone is Θ(n²), giving a matching lower bound. Thus B is tight. A omits the innermost factor, C treats all three bounds as independent n, and D ignores the outer iterations.

**Common misconception:** Multiplying maximum loop bounds without using their dependence on i.

## Q65

**Correct answer:** A, C, D
**Concept:** Safe loop-invariant code motion.

n never changes, so 100/n is invariant on iterations where it is evaluated (A). But when n=0 the original loop executes no iterations and does not divide; unconditional hoisting introduces a trap, refuting B. Guarding the hoisted evaluation with n>0 evaluates it exactly when the loop has at least one iteration, where n is nonzero and the same quotient is used throughout (C). This demonstrates D: invariance does not ensure safety on newly executed paths.

**Common misconception:** Removing repeated computation may introduce an exception even when the expression's inputs are unchanged.

