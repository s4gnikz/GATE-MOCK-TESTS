# Worked Solutions — Mock Test 040

## Q1

**Correct answer:** B
**Concept:** Mean versus dispersion.

Reduced variability means reduced dispersion under the reported measure, so B follows. It need not eliminate all variation (A), make the unchanged mean zero (C), or establish bias relative to a true value (D).

**Common misconception:** Precision and accuracy are distinct properties.

## Q2

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Unfolding as reflection.

Folding superposes a point and its reflection across the crease, so the punch produces that reflected pair. A holds. The punch is away from the fold, refuting B. Separation depends on distance from the fold, refuting C. A general reflected pair is not a quarter-turn pair, refuting D.

**Common misconception:** Replacing reflection by rotation.

## Q3

**Correct answer:** A

**Concept:** Experimental sequencing.

A hypothesis must be formulated before designing its test; the test is then conducted and its result recorded. A follows Q,R,S,P. B designs before formulating, C reverses the process, and D records a result before testing.

**Common misconception:** Ignoring the dependency expressed by “that hypothesis” and “that test”.

## Q4

**Correct answer:** 0.4167 (range 0.41665–0.41675)

Concept: equally likely ordered outcomes. For first results 1 through 6, there are respectively 5,4,3,2,1,0 larger second results. Probability=15/36=5/12=0.416666…. Rounded answer 0.4167; accepted range 0.41665–0.41675. Equality outcomes must be excluded before splitting the remaining probability equally.

## Q5

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Contingent on means dependent on fulfilment of the condition, so B preserves the meaning. A removes the dependency, C substitutes a temporal statement, and D says the outcome holds regardless of the condition. A condition is not the same as a chronological relation.

## Q6

**Correct answer:** A

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Logarithm bases and domain constraints.

Put y=log₂x. The domain requires x>0 and x≠1, hence y≠0. Change of base gives log_x16=4/y, so 4/y=y and y²=4. Therefore x=2²=4 or x=2⁻²=1/4. A and B satisfy the original equation. C has a negative base and argument for real logarithms; D uses the invalid base 1.

**Common misconception:** A logarithm base may lie between zero and one; only positivity and exclusion of one are required.

## Q7

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Substitution gives3,7,13, establishing A; at4 the rule gives16+4+1=21, proving D. The extra product vanishes at1,2,3 but not at4, so C is true and B false. Finite observations can support a pattern without uniquely determining its continuation.

## Q8

**Correct answer:** 6

Write the heights as[[a,b],[c,d]]. The second row is at most1, so the column maximum2 forces a=2, and the column maximum3 forces b=3. The second row must have at least one height1; choosing(c,d)=(1,0) or(0,1) adds exactly1. Minimum total2+3+1=6. The row and column maxima need not be realized by four separate tall columns.

## Q9

**Correct answer:** D

The required numerical answer is **11**, so select **D**.

The flip counts are1,2,1,3,1,2,1 for000→001→010→011→100→101→110→111. Their sum is11. Binary carries can flip several positions at once; this is not a Gray-code listing.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 11 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -5 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q10

**Correct answer:** D

The required numerical answer is **25**, so select **D**.

The triangles AOB and COD are similar, so AB/CD=OA/OC=2/3. Triangles AOB and BOC share the altitude from B to AC, so their areas are in the ratio OA/OC=2/3; hence BOC has area6. Similarly AOD has area6. Summing the four triangles gives4+6+9+6=25. Diagonals do not generally bisect each other in a trapezium, so the four areas need not be equal.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 25 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -12 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q11

**Correct answer:** A

A younger result waits in the reorder buffer until all preceding instructions can commit, allowing precise architectural state at an older exception(A). Early issue and additional execution units(B,C) affect execution timing but do not enforce visibility ordering. Branch-direction prediction(D) does not establish exception ordering.

## Q12

**Correct answer:** C

The required numerical answer is **2**, so select **C**.

Concept: local sensitivity of majority. Initial output is one. Flipping either of the two one bits leaves only one one and changes output to zero. Flipping the zero gives 111 and retains one. Hence two flips change output. Different input positions need not have equal influence at a particular state.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 2 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **C: Correct.** It matches the derived answer at the required precision.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q13

**Correct answer:** 768

The two successful calls have written768+512=1280 bytes. The remainder is2048−1280=768. A partial return reports progress rather than a requirement to restart from the original buffer; retries must advance the pointer and reduce the requested length.

## Q14

**Correct answer:** D

Concept: preserving probe-chain semantics. A tombstone can be remembered as a potential insertion location, but searching must continue for an existing equal key. D does this. A creates a duplicate; B and C confuse a formerly occupied slot with a never-used stopping slot. Deletion must not break searches for displaced entries.

## Q15

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: transport demultiplexing. Ports identify application endpoints on a host, in combination with transport/address context (A). B concerns link framing; C hardware pins; D processor addressing. These are not transport-port roles. A port number by itself is not a globally unique connection identifier.

## Q16

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Generating function with initial conditions.

For F=Σa_nx^n, summing the recurrence for n≥2 gives F−x=3xF−2x²F. Thus F=x/(1−3x+2x²)=x/((1−x)(1−2x)). A has the wrong constant coefficient; B has the wrong recurrence sign; C also has nonzero constant coefficient.

**Common misconception:** A recurrence denominator alone does not determine a generating function; initial conditions determine its numerator.

## Q17

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

If either predicate holds universally, their pointwise disjunction does too, so A is true. On a two-element domain, let P hold only at the first element and Q only at the second. Then F is true but G false, proving C and disproving B. On a singleton, both reduce to the same P-or-Q statement, proving D. Universal quantification does not generally distribute over disjunction.

## Q18

**Correct answer:** A

The required numerical answer is **111**, so select **A**.

The effective starting address is100−12+20=108. A32-bit word occupies four bytes, ending at111. The index scale is applied before adding the displacement, and the last byte is three beyond the first.

**Option check**
- **A: Correct.** It matches the derived answer at the required precision.
- **B: Incorrect.** Its value differs from the required answer by 111 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by -55 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q19

**Correct answer:** D

The required numerical answer is **18**, so select **D**.

The first parenthesized expression has inner value2+3=5, doubled to10. The second has inner value4, doubled to8. Their outer sum is18. Parentheses have an explicit semantic action here; treating them as ordinary grouping alone gives the wrong result.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 18 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -9 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q20

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

For t=7, the read-timestamp test7<5 is false, but7<9 is true, so ignore. For t=4, the first test4<5 already aborts. C is the pair. A,D incorrectly perform the obsolete write; B reverses the priority of the two checks. Each attempt starts from the specified same metadata.

## Q21

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: amortized geometric copying. Copies occur at sizes 1,2,4,... below n. Their sum is less than 2n, so A holds and B fails. An append at a full capacity proportional to n copies Θ(n) elements, making C true and D false. Amortized constant time does not mean worst-case constant time per operation.

## Q22

**Correct answer:** A, C

The rule gives (Project,Role)→Employee. Neither project nor role alone determines an assignment under the given constraints, so their pair is a candidate key (A). C describes a direct violation of that dependency. B fails because one employee can hold multiple roles on a project. D discards which roles the employee fills and therefore loses information. A ternary key constrains a combination of two participating entities, not either participant separately.

## Q23

**Correct answer:** B
**Concept:** Array parameters and local pointer reassignment.

The parameter a is a pointer to x[0]; p saves that pointer. Advancing local a makes it point to x[1], without changing the caller's array or p. With n=3, a[n−2]=a[1] refers to x[2], which becomes p[0]+a[0]=4+7=11. x[0] stays 4. Only B matches; A treats pointer advancement as shifting array contents, and C,D miss the actual target.

**Common misconception:** Reassigning a pointer parameter and modifying its pointed-to object are different operations.

## Q24

**Correct answer:** 1

Greedy chooses4,1,1, using three coins. An optimum is3,3, using two; one coin cannot make6. The difference is1. A denomination system need not support the greedy-choice property.

## Q25

**Correct answer:** A, C

The empty string begins and ends with an empty stack, so A is true. Every accepted prefix avoids a pop from empty, establishing C. Equal totals are insufficient: '())(' has equal totals but its third character tries to pop an empty stack. Thus B and D are false. Global balance and prefix balance are separate requirements.

## Q26

**Correct answer:** A

**Concept:** Doubly linked neighbour repair.

Bypassing X requires P's forward pointer to reach N and N's backward pointer to reach P, A. B changes the wrong directions; C retains X; D creates self-links rather than preserving the remaining chain.

**Common misconception:** Updating only the forward chain or reversing the pointer directions.

## Q27

**Correct answer:** C
**Concept:** ON filtering in an outer join.

For L.id=1, only R's row (1,5) satisfies both ON predicates. For L.id=2, no row matches, so LEFT JOIN supplies a NULL-extended row. C is correct. A drops the preserved unmatched row; B ignores R.v>0; D overlooks the successful match.

**Common misconception:** A filter in ON can preserve an unmatched left row that the same filter in WHERE would remove.

## Q28

**Correct answer:** C

The required numerical answer is **2**, so select **C**.

**Concept:** Rank–nullity from a row dependence.

The third row is the sum of the first two. Those first rows are independent, so rank is two. Four columns give nullity 4−2=2.

**Common misconception:** Subtracting rank from the number of rows instead of the domain dimension.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 2 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **C: Correct.** It matches the derived answer at the required precision.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q29

**Correct answer:** -4.5

**Concept:** A third-order trigonometric limit.

Using sin u=u−u³/6+O(u⁵), the numerator is −27x³/6+O(x⁵). Dividing by x³ and taking the limit gives −27/6=−4.5. Assigning this value at zero ensures continuity.

**Common misconception:** Keeping only the linear sine approximation after its term has cancelled.

## Q30

**Correct answer:** 3

Simultaneous transitions are 00→01→10→00. Thus the first return takes three edges. The next-state equations use the old bits; updating one bit first and then using its new value would model a different circuit.

## Q31

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Regular versus unbounded matching requirements.

C has regular expression (aa)*b*. A requires matching two unbounded counts and is nonregular. For B, pumping a sufficiently long prime-length unary word by q extra copies of a nonempty pumped block, where q is the chosen prime length, gives composite length q(1+|y|), violating the prime condition. D is nonregular: distinct prefixes 0^n1 are distinguished by suffixes 0^n1, since equality of the two zero-block lengths is required for the resulting two-one word to be a square.

**Common misconception:** Treating all numerical length restrictions as nonregular; fixed modular restrictions are regular.

## Q32

**Correct answer:** 2 (exact)

**Concept:** Engineering Mathematics — Random variables and distributions

1. P(X=0)=exp(-lambda) and P(X=1)=lambda exp(-lambda), so lambda=1.
2. A Poisson variable has variance lambda and mean lambda. Thus E[X^2]=Var(X)+(E[X])^2=lambda+lambda^2=2.

**Common misconception:** The second moment is not the variance alone.

## Q33

**Correct answer:** 1000

Each1100-bit packet occupies one millisecond and carries1000 payload bits. Hence payload throughput is1000 bits/ms. The link's raw rate includes headers and is not all useful payload.

## Q34

**Correct answer:** C

Candidates II, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) IV.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) I, III and omits valid candidate(s) II, IV.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: frame lifetime in tail calls. Q uses the address of x, so a correct transformation must retain valid storage and the intended value for that use, B. Tail position by itself does not justify overwriting all of P's frame, D. A ignores the live addressed object; C contradicts the explicitly passed pointer. Tail-call optimization is constrained by observable storage lifetimes.

## Q35

**Correct answer:** B, C, D
**Concept:** Interleaving and lost updates.

For 2, both threads read 0 before either first write, then both read 1 before either second write. For 4, run the threads serially. For 3, let the first pair of increments lose one update, reaching 1, then execute the two remaining increments serially.

Value 1 cannot be final: the final write is a thread's second write. Its preceding read occurs after its first write, which wrote at least 1; no operation writes 0, so that final read is at least 1 and the final write at least 2. Thus A is false and B,C,D are true.

**Common misconception:** Atomic individual accesses do not make a read-modify-write increment atomic.

## Q36

**Correct answer:** 3

p is always evaluated. If p is false, q is skipped and r is evaluated: subset{p,r}. If p and q are true, r is skipped: {p,q}. If p is true and q false, all three are evaluated. These are three distinct subsets. Truth assignments sharing a control path need not create new subsets.

## Q37

**Correct answer:** A

The required numerical answer is **25.5**, so select **A**.

**Concept:** Additive expected delays.

Every reference pays 1+2 ns for the lookups. Expected walk penalty is 0.10×200=20 ns, and expected data-miss penalty is 0.05×50=2.5 ns. Total 25.5 ns. Independence between the two miss events is unnecessary for summing their expected additive costs.

**Common misconception:** A conditional lookup sequence does not mean the always-performed data lookup should be weighted only by TLB misses.

**Option check**
- **A: Correct.** It matches the derived answer at the required precision.
- **B: Incorrect.** Its value differs from the required answer by 25.5 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by -12.7 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1.0 and is outside the source answer's accepted range.


## Q38

**Correct answer:** A

The required numerical answer is **1**, so select **A**.

Concept: field-wise versus joint encoding. Separate fields need ceil(log₂9)+ceil(log₂5)+8=4+3+8=15 bits. Legal joint choices number 9·5·2⁸=11520, between 2¹³ and 2¹⁴, requiring 14 bits. Excess=1. Independent field padding can waste combinations that a joint code could use.

**Option check**
- **A: Correct.** It matches the derived answer at the required precision.
- **B: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 2 and is outside the source answer's accepted range.


## Q39

**Correct answer:** B
**Concept:** Signed fixed-point multiplication and ties-to-even.

0xE6 represents −26/16=−1.625, and 0x1C represents 28/16=1.75. Their product is −2.84375, exactly halfway between −45/16 and −46/16. The even retained integer is −46, giving −2.875 and byte 256−46=210=0xD2. A is the odd tie neighbour; C loses the sign; D rounds to an unrelated representable value.

**Common misconception:** Ties-to-even uses the retained integer's low bit, including for negative values; it is not simply rounding toward zero.

## Q40

**Correct answer:** 1

For(1,1), y=1 has outgoing second values1 and2, including2≠x, so reject. For(1,2), R(2,2) supplies z=2≠1, so reject. For(2,2), the only z is2=x, so accept. For(3,1), both z=1,2 differ from3, so reject. Exactly one tuple survives. The inner lookup is on the outer y value, not on its x.

## Q41

**Correct answer:** A, B, D
**Concept:** Products of rank-one projections.

Since uᵀu=vᵀv=2 and uᵀv=1, PQ=uvᵀ/4. This is a nonzero outer product and has rank one (A). Its trace is vᵀu/4=1/4 (B). Its (1,2) entry is zero while its (2,1) entry is 1/4, refuting symmetry (C). The vector u is an eigenvector with eigenvalue 1/4; the two-dimensional kernel vᵀx=0 supplies two zero eigenvalues, proving D.

**Common misconception:** Two symmetric matrices need not have a symmetric product unless they commute.

## Q42

**Correct answer:** B, C

A small addend can round away at a large magnitude, proving B. Subtracting nearby rounded quantities can expose their prior approximation errors, proving C. Rounding at intermediate operations can break associativity, making A false. Finite precision and exponent range cannot represent all arbitrarily large integers exactly, disproving D.

## Q43

**Correct answer:** B

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The pumping lemma guarantees the existence of a suitable decomposition for each sufficiently long string. To refute regularity one must defeat every permitted decomposition, so A is true. The bound |xy|≤p forces nonempty y wholly into the first block of a's, so B is true. The lemma requires |y|>0, making C false. It allows every string of length at least p, including2p, making D false. Quantifier order is essential to pumping arguments.

## Q44

**Correct answer:** 3

A has eigenvalues1 and2, with eigenvectors(1,1)ᵀ and(1,2)ᵀ. Write v=α(1,1)ᵀ+β(1,2)ᵀ. Then A^n v=α(1,1)ᵀ+2^nβ(1,2)ᵀ. Boundedness forces β=0, and x+y=2α=6 gives α=3, so x=3. A component along the expanding eigenvector cannot remain bounded.

## Q45

**Correct answer:** A, B

For id=1 only employee 11 passes the ON condition; both counts are 1. For id=2 the left join supplies one NULL-extended row. COUNT(*) counts it, while COUNT(E.eid) ignores its NULL, yielding n=1,m=0. Hence A,B are true and D false. Moving the active filter to WHERE rejects that NULL-extended row, removing id=2 and disproving C. Filtering matches and filtering the joined result have different effects on outer joins.

## Q46

**Correct answer:** C
**Concept:** Conditional HTTP validation.

A matching entity tag permits the server to report that the cached representation may be reused without transferring the full representation body. The client still sends the request and receives the validation response, so a network round trip remains (C). A confuses validation with a fresh local-cache hit. B incorrectly assigns a representation body to 304. D makes an unsupported claim about unrelated caches.

**Common misconception:** Saving transferred bytes and eliminating network latency are different benefits.

## Q47

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Both first operations are sends and require a receive that neither process has reached; A is true and B false. If Q receives first, it matches P's send, after which Q's send can match P's receive; C is true. A mutex can keep a needed partner from entering its communication sequence and does not create a receive, so D is false. Textual presence of matching operations is insufficient when blocking order prevents reaching them.

## Q48

**Correct answer:** A

The required numerical answer is **15**, so select **A**.

**Concept:** Accounting across a two-stack queue.

The four enqueues cost four pushes. The first dequeue transfers A and B (four operations) and pops A (one). The second dequeue pops B (one). The third transfers C and D (four) and pops C (one). Total 4+4+1+1+4+1=15.

**Common misconception:** Transferring the input stack while an older item remains in the output stack.

**Option check**
- **A: Correct.** It matches the derived answer at the required precision.
- **B: Incorrect.** Its value differs from the required answer by 15 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by -7 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q49

**Correct answer:** 1

The true best choice is B+C with weight6 and value11; A+C gives9. With ascending updates, processing C can reuse C three times, giving12 at capacity6. No unbounded combination at weight≤6 exceeds12, so the faulty result is12 and the excess1. Descending capacity updates prevent using the current item more than once in0/1 knapsack.

## Q50

**Correct answer:** A, B, C

**Concept:** Computer Organization and Architecture — Memory interfacing

The region is 0x8000–0xBFFF, so its upper two address bits are 10. A13:A12 enumerate the four 4 KiB subregions, and A11:A0 choose one of 4096 bytes in each chip. Hence A and B hold. Ignoring A14 enables both 0x8000–0xBFFF and 0xC000–0xFFFF; the chip and offset bits are unchanged when A14 flips, so each byte has two aliases, establishing C. In D, A0 is unused, so adjacent byte addresses have the same chip and local address. A12 also redundantly enters the chip's address and decoder, leaving parts inaccessible; one-to-one addressing fails.

- **A:** True: the upper bits 10 identify the 16 KiB window and the next two choose its four chips.
- **B:** True: B123−8000=3123 hexadecimal, giving bank 3 and offset 123.
- **C:** True: toggling the ignored A14 yields another enabled address for the same storage cell.
- **D:** False: ignoring A0 aliases every adjacent address pair.

**Common misconception:** Partial address decoding causes aliasing; chip capacity alone does not guarantee unique processor addresses.

## Q51

**Correct answer:** A, B, D

**Concept:** Finite execution traces versus unbounded halting.

Simulating at most k steps decides acceptance and halting within that bound, establishing A,B. Recording the finite sequence of complete configurations permits exact repetition testing, establishing D. Unbounded halting for arbitrary M,x is undecidable, so C is false.

**Common misconception:** Treating bounded and unbounded execution questions as equally undecidable.

## Q52

**Correct answer:** A, B, D
**Concept:** Rank of a composition.

The image of B has dimension three. A's one-dimensional kernel can remove at most one dimension from that image, so rank(AB)≥2, proving A and excluding C. Taking A=B=diag(1,1,1,0) gives rank three (B). Taking A=diag(1,1,1,0) and B=diag(1,1,0,1) gives AB=diag(1,1,0,0), rank two (D).

**Common misconception:** Knowing the two individual ranks does not uniquely determine the product rank; the kernel/image alignment matters.

## Q53

**Correct answer:** B

The required numerical answer is **8**, so select **B**.

Concept: overflow in an otherwise valid cancellation. For x=−4,...,3, doubling stays in −8,...,7 and exact halving recovers x: eight values. For x=4,...,7, the wrapped product is 2x−16 and halving gives x−8. For x=−8,...,−5, it is 2x+16 and halving gives x+8. None of these recover x. Algebraic cancellation can fail when the intermediate representation overflows.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 8 and is outside the source answer's accepted range.
- **B: Correct.** It matches the derived answer at the required precision.
- **C: Incorrect.** Its value differs from the required answer by -4 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q54

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Expansion gives xz+(NOT x)y+yz; the consensus term yz is redundant, yielding A,B. If y=z, selection by x yields that common value, proving D. For x=1,y=0,z=1, F=1 while yz=0, refuting C.

## Q55

**Correct answer:** A

**Concept:** Completion, complementation, and state distinguishability.

The original language is a^k for k≥2. Add a dead state for every missing b transition, with self-loops on both symbols. Complementing accepting states gives a complete four-state DFA. The four original-language states corresponding to prefixes ε,a,aa,b are distinguishable: a separates ε from a; ε separates aa from ε or a; and an appropriate a-suffix separates b from each nondead prefix. Complementation preserves distinguishability. Thus four is minimal; B is too small and C,D exceed the exhibited minimum.

**Common misconception:** Complementing the accepting set of a partial DFA without first representing rejecting undefined transitions.

## Q56

**Correct answer:** A

**Concept:** Tree reconstruction from traversals.

Preorder makes A the root. Inorder splits left D,B,E from right C,F. The left subtree root is B with children D,E; the right subtree root is C with right child F. Postorder is D,E,B,F,C,A, option A. B places B before E, C reverses children and right-subtree order, and D interleaves nodes from different subtrees.

**Common misconception:** Preserving preorder's root-first order while attempting a postorder traversal.

## Q57

**Correct answer:** 496

Every unordered pair of distinct array positions is compared exactly once: at the first recursive split that separates its members. Thus total comparisons are C(32,2)=496. Equivalently, T(n)=2T(n/2)+n²/4 with T(1)=0 yields n(n−1)/2. This merge phase is quadratic pair enumeration, not the usual linear merge of sorted arrays.

## Q58

**Correct answer:** B

The required numerical answer is **300**, so select **B**.

The latest collision indication requires a round trip of2·12=24 microseconds. At100×10^6 bits/s this corresponds to2400 bits, or300 bytes. Using the one-way delay would halve the required frame and could let transmission finish before collision detection.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 300 and is outside the source answer's accepted range.
- **B: Correct.** It matches the derived answer at the required precision.
- **C: Incorrect.** Its value differs from the required answer by -150 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q59

**Correct answer:** C

The required numerical answer is **1**, so select **C**.

DFS follows s→a→c→d, then returns to s and visits b. On b→c, c is already marked. All other edges first discover their targets, so exactly one examined edge has an already marked destination. Marking on entry prevents repeated exploration of the shared descendant.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **C: Correct.** It matches the derived answer at the required precision.
- **D: Incorrect.** Its value differs from the required answer by 2 and is outside the source answer's accepted range.


## Q60

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Bayesian updating of a hidden Bernoulli source.

The likelihoods of exactly two successes are 3(1/4)²(3/4)=9/64 and 3(1/2)³=24/64. Multiplying by priors gives relative weights 9 and 48, so posterior probabilities are 3/19 and 16/19. The predictive success probability is (3/19)(1/4)+(16/19)(1/2)=35/76. A ignores the posterior mixture; C is the posterior probability of source I rather than a trial success; D is not the posterior-weighted value.

**Common misconception:** Trials are independent conditional on the hidden source, not necessarily unconditionally.

## Q61

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Mutual exclusion versus progress.

Both can set their flag before either checks the other's flag, leaving both spinning forever. Progress therefore fails. Mutual exclusion still holds: a thread entering has its own flag true, preventing the other from passing its test until that flag is cleared after the critical section. B captures both facts. A overlooks the preceding writes, C overlooks the deadlocking interleaving, and D invents a turn variable.

**Common misconception:** Treating absence of simultaneous entry as a complete synchronization proof.

## Q62

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Multiple resource instances and cycle insufficiency.

R can finish without another resource and release one A. Q then obtains A, completes and releases B (and A); P obtains B and finishes. Thus A and D hold. The apparent P–Q cycle does not prevent this external release, establishing C and refuting B.

**Common misconception:** Applying the single-instance cycle criterion to a resource type with multiple instances.

## Q63

**Correct answer:** B, C

The shortest-path equality gives dist(v,d)=dist(u,d)−cost(u,v)<dist(u,d), so B is true. A directed cycle would require a strict descent back to the original distance, impossible; A is false. In a finite graph, an indefinitely continuing route would repeat a vertex, so with a next hop at every non-destination it must reach d; C is true. Zero-cost edges allow equality and can create cycles among tied next hops, so D is false. Exact distances and strictly positive costs are essential assumptions.

## Q64

**Correct answer:** A, C

**Concept:** Loop joins and fixed-point facts.

The initial edge carries zero while iterations can carry one,two,…, so C holds and no single constant generally describes all header visits, A. B ignores the back edge. Constant propagation does not generally determine arbitrary input-dependent loop counts, so D is false.

**Common misconception:** Propagating an initialization through a modifying loop as an invariant.

## Q65

**Correct answer:** A

**Concept:** Deferred referential-integrity checks.

The final pair of rows references existing keys in both tables. Deferred checking permits constructing that mutually dependent state within the transaction, whereas immediate checking rejects the first insertion into either initially empty table. A holds. Deferral changes checking time, not the final constraint, refuting B,C; D denies the achievable valid state.

**Common misconception:** Treating deferred checking as disabling the constraint permanently.

