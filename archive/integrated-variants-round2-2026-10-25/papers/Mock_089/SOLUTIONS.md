# Worked Solutions — Mock Test 089

## Q1

**Correct answer:** C

In C, the introductory phrase modifies the subject technician, assigning the haste correctly. A grammatically attaches the introductory modifier to instrument; D explicitly describes the instrument as hurried. B's wording is unnatural and does not correctly express the intended modifier relationship. A human performer should be the subject governed by this introductory phrase.

## Q2

**Correct answer:** 11.11 (two decimals)
**Concept:** Profit margin versus markup.

Selling price is 100×0.9=90 and profit is 90−80=10. As a percentage of selling price, this is 100×10/90=11.111…%, rounded to 11.11%. Dividing by cost would instead give a 12.5% markup.

**Common misconception:** Profit percentage requires the denominator specified in the question.

## Q3

**Correct answer:** C

**Concept:** Exclusive truth conditions.

If the key is in drawer 1, both P and Q are true. In drawer 2, both are false. In drawer 3, P is false and Q true, so exactly one holds. C alone satisfies the premises; A,B fail and D incorrectly includes them.

**Common misconception:** Reading “exactly one” as “at least one”.

## Q4

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

1. Reflection maps (x,y) to (x,-y).
2. Clockwise quarter-turn maps (u,v) to (v,-u). The combined map is (x,y) to (-y,-x).
3. Applying it separately to the labelled vertices gives (-1,-1), (-1,-3), (-2,-1).
- Original option A: All three vertices obey (-y,-x).
- Original option B: This is the combined map for a counterclockwise rotation after reflection.
- Original option C: This applies clockwise rotation without the preceding reflection.
- Original option D: This applies counterclockwise rotation without reflection.

## Q5

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Reading comprehension and inference.

Weekly visits may be redistributed across times without increasing their total. In addition, one visitor can make several visits, so distinct visitors cannot be inferred from visit totals. B identifies both gaps. A wrongly excludes redistribution; C asserts an unsupported decrease; D replaces a possibility with an assertion about every visitor.

**Common misconception:** Treating counts of events as counts of distinct people, or a before/after association as proof of recruitment.

## Q6

**Correct answer:** 60

**Concept:** Disjoint composition cases.

Allowed committees contain two engineers and two designers, or three engineers and one designer. Counts are choose(5,2)choose(3,2)=30 and choose(5,3)choose(3,1)=30. Their sum is 60.

**Common misconception:** Including four engineers despite the designer requirement.

## Q7

**Correct answer:** 5

Profits are30 in each year, but margins are30/120=25% and30/150=20%. The decrease is5 percentage points. Unchanged profit does not imply unchanged profit margin, and a percentage-point difference is not a relative percentage change.

## Q8

**Correct answer:** 5

Undo the second fold: the cut x=5 reflects to x=7 in the first packet. Undo the first fold: x=5 and7 reflect across x=4 to x=3 and1. The full-height cuts are therefore at1,3,5,7, dividing the rectangle into five strips. The fold lines themselves are not cuts.

## Q9

**Correct answer:** A

Inspection immediately follows calibration, and release lies after inspection but before trial. This forces C,I,R,T, optionA. B breaks immediacy; C reverses calibration and inspection; D places release after trial. Each condition must hold in the same ordering.

## Q10

**Correct answer:** 0.3333 (range 0.33325–0.33335)

Concept: conditional subset counting. Fix the first person's subset. Among the ten possible second subsets, nine differ from it. For their union to include all five elements, the second subset must include both elements outside the first and one of its three elements. Thus three of the nine eligible subsets work, giving 1/3. Round to 0.3333; range 0.33325–0.33335. The conditioning excludes the identical subset from the denominator.

## Q11

**Correct answer:** 6

The elements in the given set divisible by both2 and3 are6 and12. Under divisibility,6 precedes12, so6 is their least upper bound. The numerically largest common multiple is not the join.

## Q12

**Correct answer:** 1

All four inputs with a=0 are on-set or don't-care, so cube NOT a covers them and contains one literal. Any expansion to a literal-free cube would include off-set inputs with a=1. Thus this is the largest permissible prime cube that covers the on-set. Don't-care inputs may assist expansion but cannot override specified zeros.

## Q13

**Correct answer:** 2

NOT EXISTS retains A's1 and NULL: neither has a TRUE equality match in B. It rejects2. NOT IN retains none:2 has a match and the other comparisons involve UNKNOWN due to NULL. Counts2 and0 differ by2. UNKNOWN is not TRUE in a WHERE filter.

## Q14

**Correct answer:** 6

The first fork creates two branches. Its child enters the then branch and one fork produces2 descendants reaching the end. Its parent enters the else branch, where two successive forks double the population twice, producing4 descendants. Total2+4=6. Children created inside a chosen branch continue there; they do not reevaluate the earlier if using a newly returned fork value.

## Q15

**Correct answer:** -24

A unit lower triangular matrix has determinant1. The upper triangular determinant is2×(−3)×4=−24; multiplicativity gives det(A)=−24. No permutation sign is introduced because none is used.

## Q16

**Correct answer:** 11

Every directed edge contributes once to outdegree and once to indegree, including a loop. Thus both total degrees equal the edge count11. A loop does not contribute twice to either separate directed degree. The six-vertex count and number of loops do not alter the identity.

## Q17

**Correct answer:** A, C

After buffered data is drained, orderly end-of-stream is reported by a zero return on a positive-length receive(A). TCP supports independent directional shutdown, so continued sending can remain valid(C). Zero here is a count, not a delivered data byte(B), and TCP supplies a byte stream without a separate application shutdown record(D).

## Q18

**Correct answer:** 2

Concept: local sensitivity of majority. Initial output is one. Flipping either of the two one bits leaves only one one and changes output to zero. Flipping the zero gives 111 and retains one. Hence two flips change output. Different input positions need not have equal influence at a particular state.

## Q19

**Correct answer:** 9

**Concept:** Address width versus word width.

Selecting among 512=2⁹ microinstructions requires nine bits. The 40-bit microinstruction width determines storage per entry, not the number of address bits.

**Common misconception:** Using microinstruction width as its address width.

## Q20

**Correct answer:** B

**Concept:** Shared storage versus synchronization.

Shared memory provides access to common data but does not automatically order protocol steps or exclude conflicting operations, proving B. A and C are false restrictions; D incorrectly supplies automatic serialization.

**Common misconception:** Assuming communication visibility is sufficient for a race-free protocol.

## Q21

**Correct answer:** 1

After adding c, the three-edge route costs4+3c and the direct edge costs5+c. Direct is strictly cheaper when5+c<4+3c, or c>1/2. The smallest positive integer is1. Adding a constant per edge does not add the same amount to paths with different edge counts.

## Q22

**Correct answer:** -5
**Concept:** Polynomials of triangular matrices.

The matrix polynomial remains upper triangular, with diagonal values 1²−1−1=−1, 2²−2−1=1, and 3²−3−1=5. Its determinant is their product −5, independently of the entries above the diagonal.

**Common misconception:** The arbitrary upper entries do not affect a triangular matrix's determinant.

## Q23

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** ON filtering in an outer join.

For L.id=1, only R's row (1,5) satisfies both ON predicates. For L.id=2, no row matches, so LEFT JOIN supplies a NULL-extended row. C is correct. A drops the preserved unmatched row; B ignores R.v>0; D overlooks the successful match.

**Common misconception:** A filter in ON can preserve an unmatched left row that the same filter in WHERE would remove.

## Q24

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Output-sensitive lower bounds.

There are C(n,2)=n(n−1)/2 distinct pairs to emit. Constant work per output gives Ω(n²), so D is the tight bound from output size. A,B,C are asymptotically weaker and do not express the tight output-size requirement.

**Common misconception:** An efficient internal algorithm cannot avoid the time needed to materialize its required output.

## Q25

**Correct answer:** 6.6667 (range 6.66665–6.66675)

Concept: extremal median. Sort the observations. If the median is m, the three largest values sum to at least 3m and the other two are nonnegative. Thus m≤20/3. Values 0,0,20/3,20/3,20/3 attain the bound. Round to 6.6667; range 6.66665–6.66675. A median need not equal the mean.

## Q26

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Since each element is its own inverse, (ab)^(−1)=b^(−1)a^(−1)=ba, proving A. If they commute, (ab)²=a²b²=e; ab≠e because a≠b, so its order is2, proving C. Conversely order2 gives ab=(ab)^(−1)=ba, proving D. Noncommuting transpositions in a permutation group satisfy the individual square conditions, refuting B. Individual involutions need not commute.

## Q27

**Correct answer:** 3

**Concept:** Epsilon closure and accepted words.

The start epsilon closure reaches b. From b, any number of zeros may be consumed, followed by at least one 1 to reach c; further ones stay in c. The language is 0*1+. Length-three words are 001,011,111: three.

**Common misconception:** Counting epsilon moves as input symbols or allowing zeros after reaching c.

## Q28

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A usable cached or otherwise known address can avoid a fresh lookup, A. The redirected hostname may need its own DNS resolution, C. Distinct hostnames need not resolve to the same address, so B is false. A response cannot change a request already transmitted; following a redirect involves another request, so D is false.

## Q29

**Correct answer:** 8

Two chips in parallel give each16-bit word. Four such banks provide1024/256=4 times the depth. Therefore2·4=8 chips are required. Expanding width alone would still leave only256 addresses.

## Q30

**Correct answer:** 3

*p++ means*(p++): x receives the old a[0]=1 and p advances to a[1]. The next statement adds1 to a[1]=2, yielding3. The increment changes the pointer, not the dereferenced integer in the first statement.

## Q31

**Correct answer:** B

**Concept:** Lexical recognition versus semantic binding.

A lexer can identify a spelling as an identifier without resolving its declaration, which may require scope information. B is correct. A asserts an unnecessary implementation rule; C leaps from lexical validity to type correctness; D misclassifies whitespace.

**Common misconception:** Treating tokenization, name resolution and type checking as the same analysis.

## Q32

**Correct answer:** 3

The transition over C advances S→·CC to S→C·C. Closure adds C→·cC and C→·d because the dot precedes C. Thus GOTO contains three items. The completed item S→CC· belongs to a later transition, not this one.

## Q33

**Correct answer:** -1

Concept: recurrence periodicity. Values starting at n=0 are 0,1,1,0,−1,−1,0,1. The pair (0,1) repeats at positions 6,7, so the recurrence repeats with period six. 2027 mod 6=5, giving −1. Repeated evaluation is unnecessary once the state pair recurs.

## Q34

**Correct answer:** 2

Concept: existential guard plus universal restriction. x=1 has neighbours a,b, both in S; x=2 has only a; x=3 has c, which fails. Hence x=1,2 satisfy the predicate, count two. The existential clause excludes vacuous success for x values with no R tuple.

## Q35

**Correct answer:** 4

A can produce0,1,2 or3 copies of a, with B producing the remainder. Each split has a unique parse within A and B, giving four trees. Although each component grammar is unambiguous, their concatenation has an ambiguous boundary.

## Q36

**Correct answer:** 225

**Concept:** Counting permutations by cycle type.

The allowed partitions of six into even lengths are 6, 4+2, and 2+2+2. They contribute 5!=120, choose(6,4)×3!×1!=90, and 6!/(2³×3!)=15. The total is 225.

**Common misconception:** Distinguishing the order of disjoint cycles or their cyclic starting points.

## Q37

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

A displaced key's probe chain can cross a deleted slot, so turning it into EMPTY would terminate search prematurely(A). Remembering a tombstone while checking the remaining chain avoids duplicate insertion and allows reuse(B). Searches must continue past tombstones, disproving C and explaining the added unsuccessful-search work in D. Deleted and never-used slots have different historical meanings.

## Q38

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A deterministic PDA is a restricted nondeterministic PDA, so its language is context-free (A). Final-state and empty-stack acceptance have equivalent expressive power for nondeterministic PDAs; the standard simulation gives C. Deterministic PDAs recognize only a proper subset of context-free languages, so B is false. D can introduce acceptance in previously nonfinal states after input consumption. An equivalence theorem about machine classes is not permission to alter acceptance states arbitrarily.

## Q39

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

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

## Q40

**Correct answer:** 2
**Concept:** Amdahl's law with a target speedup.

Normalize old time to one. A speedup of 1.25 requires new time 1/1.25=0.8. If the component's speedup is s, then 0.6+0.4/s=0.8. Thus 0.4/s=0.2 and s=2.

**Common misconception:** A 25% speed increase means a 20% time reduction, not a 25% time reduction.

## Q41

**Correct answer:** 4

Only key1 matches. Each of A's two occurrences matches each of B's two, giving2×2=4 rows. Keys2 and3 have no partners. Projection without DISTINCT preserves those four occurrences under bag semantics. A join is not a one-to-one pairing of duplicate rows.

## Q42

**Correct answer:** 1440

The1500-byte outer packet contains a20-byte tunnel header plus the inner20-byte IP header,20-byte TCP header and payload. Hence the payload bound is1500−20−20−20=1440. All three headers consume the outer MTU; the inner packet is not exempt from the tunnel overhead.

## Q43

**Correct answer:** 48

Choose the unordered pair of positions for A,B at distance 2: (1,3),(2,4),(3,5),(4,6). The remaining positions admit respectively 2,1,1,2 adjacent position pairs for C,D. For each such selection, orient A,B in two ways, orient C,D in two ways, and arrange the two other books in two ways. The total is (2+1+1+2)×2×2×2=48. Therefore the required count is 48.

## Q44

**Correct answer:** 4

The reachable cycle is 000,001,011,111,110,100, then 000. Exactly 011 and110 have two set bits. Twelve observations consist of two complete six-state cycles, giving4 output-one observations. Count the initial state as requested; do not assume the register traverses all eight binary states.

## Q45

**Correct answer:** A

**Concept:** Deferred referential-integrity checks.

The final pair of rows references existing keys in both tables. Deferred checking permits constructing that mutually dependent state within the transaction, whereas immediate checking rejects the first insertion into either initially empty table. A holds. Deferral changes checking time, not the final constraint, refuting B,C; D denies the achievable valid state.

**Common misconception:** Treating deferred checking as disabling the constraint permanently.

## Q46

**Correct answer:** 30

**Concept:** Product scaling in fixed-point arithmetic.

The represented values are 24/16 and 20/16. Their product has raw integer numerator 480 and scale 256. To return to scale 16, divide 480 by 16, giving encoded integer 30 exactly. No rounding adjustment is necessary in this case.

**Common misconception:** Retaining the doubled fractional-bit scale as if it were the destination format.

## Q47

**Correct answer:** 5

0,2 miss into set0;1 misses into set1. The next0 hits and makes0 most recent in set0. Access4 misses and evicts2. Access2 then misses and evicts0. The final1 hits in its unaffected set. There are5 misses. LRU order is maintained separately for each set.

## Q48

**Correct answer:** 2

Concept: normalized recurrences and generating sums. Divide by 2ⁿ: b_n=b_(n−1)+n/2ⁿ, b0=0. Thus b_n=Σ(k=1..n)k/2ᵏ. From Σk xᵏ=x/(1−x)² for |x|<1, the limit at x=1/2 is two. Equivalently a_n=2^(n+1)−n−2. Solving only the homogeneous recurrence would miss the limiting coefficient.

## Q49

**Correct answer:** B
**Concept:** Rapidly growing loop indices and dominant work.

The i values are 2,4,16,…,2^(2^(k−1))=√n; the next value equals n and is excluded. Work equals the sum of these indices. The last term gives a √n lower bound, and preceding terms decrease at least geometrically, giving an O(√n) upper bound. A counts only outer iterations; C includes the excluded n-sized iteration; D multiplies two inappropriate bounds.

**Common misconception:** The number of outer iterations is not the total cost when their bodies have sharply different sizes.

## Q50

**Correct answer:** 256
**Concept:** Reuse distance and capacity misses.

Each row occupies one aligned cache line, so a column scan visits 16 different lines. Between successive accesses to one row's line, 15 other distinct lines are accessed, exceeding the capacity of eight. LRU therefore evicts every line before its next use. All 16×16=256 element reads miss, despite each row's elements sharing one line.

**Common misconception:** Spatial locality helps only when the line remains resident until the nearby element is accessed.

## Q51

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Earliest-finish selection gives B,C,E,G, a feasible four-activity schedule. The earliest-finish exchange argument guarantees that its cardinality is maximum, so m=4. To count all maximum subsets, partition by the first activity. Starting with A forces D,F,H to fit three more, yielding {A,D,F,H}. Starting with B, the next activity can be C or D. If it is C, the final pair can be (E,G), (E,H), or (F,H). If it is D, the final pair must be (F,H). Starting with C or any later activity permits at most three activities total, so adds no maximum subset. The five maximum subsets are {A,D,F,H}, {B,C,E,G}, {B,C,E,H}, {B,C,F,H}, and {B,D,F,H}. Hence (m,r)=(4,5).
- Original option A: False: B,C,E,G is already a feasible set of four activities.
- Original option B: False: it omits one of the five listed optimal subsets, often the one beginning with the later-finishing A.
- Original option C: True: earliest-finish greedy establishes m=4, and partitioning by the first two choices gives five optimal subsets.
- Original option D: False: earliest-finish greedy reaches four and is optimal; five compatible activities cannot be selected.

## Q52

**Correct answer:** 12 (exact)

**Concept:** Operating Systems — Concurrency and synchronization

There are 6!/(2×2×2) = 90 interleavings preserving each read-before-write order. Enumerate them while retaining a private register for each thread; the final values are [1, 3, 4, 5, 6, 7, 8, 9, 11, 12, 14, 17], giving 12 distinct outcomes. A direct derivation partitions by the last writer: if A is last, its read can see 0,3,5,8, giving 1,7,11,17; if B is last, its read can see 0,1,5,6,11, giving 3,4,8,9,14; if C is last, its read can see 0,1,3,4,7, giving 5,6,8,9,12. The union of these sets gives the stated answer. The values before a last writer's read come only from the other two threads, which may themselves overlap.

**Common misconception:** Atomic reads and writes do not make a read-modify-write pair atomic.

## Q53

**Correct answer:** 0.6875

For Y=10, Y.val=1/2+0/4=1/2 and Y.len=2. For Z=11, Z.val=1/2+1/4=3/4. Concatenation shifts Z's fraction right by Y.len places: X.val=1/2+(3/4)/4=11/16=0.6875. Using Z.len in this shift happens to match here but is not the stated general rule; the preceding prefix length determines placement.

## Q54

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Conflict versus view serializability with blind writes.

On x, the first two writes create T1→T2, while the second and third create T2→T1. This cycle rules out conflict serializability. For view equivalence, x's final writer T1 forces T2 before T1. The read of y by T3 reads T2's write, forcing T2 before T3. No constraint orders T1 versus T3. Thus the two serial orders are T2,T1,T3 and T2,T3,T1. A is correct. B,D incorrectly ignore the conflict cycle; C incorrectly treats it as proof against view serializability.

**Common misconception:** Blind writes allow some view-serializable schedules to fail conflict serializability.

## Q55

**Correct answer:** B, C
**Concept:** Object lifetime after function return.

A's automatic scalar and D's automatic array cease to exist when their functions return; their pointers do not permit later access to live objects. B's static object persists throughout program execution. C's allocated object persists until freed, which the question excludes before the first access. Thus B,C are valid and A,D are not.

**Common misconception:** Returning an address does not extend the lifetime of the object at that address.

## Q56

**Correct answer:** B, D

Concept: sortable floating-point bit keys. Positive encodings grow with magnitude, so B. Negative raw encodings also grow with magnitude but that makes their numerical values smaller, disproving C. Raw unsigned ordering puts positive encodings before negative ones, disproving A. Complementing negatives reverses their magnitude order and places them below 0x80; flipping the sign bit of positives places them above. Thus D preserves increasing numeric order for the specified finite nonzero values. Excluding NaNs and signed-zero ties is important to the stated strict comparison.

## Q57

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Closures and environment lifetime.

F and G need separate cells associated with their separate outer activations, and those cells must remain alive while captured. B provides both identity and lifetime. A wrongly merges cells, C leaves dangling references, and D implements caller-dependent lookup rather than lexical capture.

**Common misconception:** Assuming every local variable's lifetime must end when its defining call returns.

## Q58

**Correct answer:** 3.2

Serialization takes1200/600=2 seconds and1200/1200=1 second. Store-and-forward requires both for this one packet. Add two propagation delays of0.1, giving3.2 seconds. There is no packet splitting to permit overlapping transmission of separate packets.

## Q59

**Correct answer:** 7

**Concept:** A worst-case resource deadlock bound.

With six resources, each process can hold two and wait for its third, producing deadlock. With seven, if all three are unfinished, at most six can be held while each remains short of its maximum; a free instance then permits some waiting process to reach three and finish. After it releases resources, the remaining processes can similarly progress. Equivalently the sufficient bound is Σ(max_i−1)+1=3×2+1=7, and the six-instance construction proves minimality.

**Common misconception:** Requiring all maximum demands simultaneously, or counting scheduling starvation as resource deadlock.

## Q60

**Correct answer:** 5
**Concept:** CPU affinity, assignment, and local scheduling order.

If C goes to CPU 1, CPU 0 executes B then A with waits 0,3, while CPU 1 executes C,D in either order with waits 0,2. Total waiting is 5. If C goes to CPU 0, its three bursts are 2,3,4; shortest-first minimizes their sum to 0+2+5=7, and D waits zero on CPU 1. These exhaust C's two possible placements. Deliberate idle time cannot reduce waiting because every job is already available. The minimum is 5.

**Common misconception:** Selecting a per-CPU ordering alone is insufficient when a flexible job's CPU assignment changes the attainable total.

## Q61

**Correct answer:** 38 (exact)
**Concept:** Two-stack queue operation accounting.

There are ten enqueue pushes and eight dequeue pops. The first dequeue transfers six items from I to O. After six total dequeues O is empty. Before the seventh dequeue, I contains 7,8,9,10, so four more items transfer. Ten transfers each require one pop and one push, contributing twenty operations. Total 10+8+20=38.

**Common misconception:** Transfers occur only when the output stack is empty, not on every dequeue or enqueue.

## Q62

**Correct answer:** 5

For flips at i<j, the error polynomial is x^i(1+x^(j−i)). Since g has nonzero constant term, the shift x^i does not affect divisibility. Modulo g, x³=1 and neither x nor x² is1, so the separation must be a multiple of3. Separation3 gives four pairs and separation6 gives one, total5. There are21 possible pairs overall, but only these have zero syndrome.

## Q63

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Gaps between successive squares.

Pumping once extra gives length p²+d. It exceeds p² because d≥1, but d≤p<2p+1, so it is below (p+1)². Thus it is not a square and leaves the language, A. B reverses the inequality; C is false; D invents an alphabet restriction.

**Common misconception:** Failing to bound the pumped length between consecutive allowed lengths.

## Q64

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Uses before overwrites.

The first x value is used immediately in y=x*c before being overwritten, and y is then returned. Neither definition is dead, so C holds. A,D ignore the intervening use of x; B ignores return y. The later x=0 may itself be dead under the stated observability assumption, but that is not one of the two assignments asked about.

**Common misconception:** A later overwrite does not kill earlier uses that already consumed the previous value.

## Q65

**Correct answer:** 3

Concept: implication propagation and model counting. The first clause forces at least one of p,q. Each implies r, so r must be true; then r implies s and s implies t. The only freedom is (p,q)=(1,0),(0,1),(1,1), giving three assignments. Counting each implication independently would overcount inconsistent combinations.

