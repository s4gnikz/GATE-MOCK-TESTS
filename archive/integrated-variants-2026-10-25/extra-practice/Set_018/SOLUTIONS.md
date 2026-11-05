# Worked Solutions — Additional Practice Set 018

## Q1

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

1. A base tree uses S -> aSb with the inner S -> epsilon.
2. Replace the root with S -> SS, placing the previous tree on one child and S -> epsilon on the other. The yield remains ab.
3. Repeating this operation creates arbitrarily large finite trees with the same yield, so their count is infinite.
- Original option A: The base tree is not unique; an empty sibling adds a second shape.
- Original option B: The construction can be repeated after two trees have been obtained.
- Original option C: There is no finite size bound on added empty siblings.
- Original option D: The unbounded family consists of distinct finite trees.

## Q2

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

## Q3

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Digital Logic — Boolean algebra

The two occurrences of x cancel under XOR. If z=0, both AND terms are0 and D=0. If z=1, their values are y and NOT y, whose XOR is 1. Thus D=z independently of x and y.

- **A:** False: when x=0,z=1 the result is 1.
- **B:** False: when y=0,z=1 the result is 1.
- **C:** True: flipping y affects F exactly when z=1.
- **D:** False: z=0 yields D=0, not 1.

**Common misconception:** A Boolean input's influence may be gated by another variable even when the output also contains XOR.

## Q4

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Compiler Design — Lexical analysis

After reading a, the lexer has an accepting position for token a, but ab*c is still possible. It must continue across all n b symbols because a subsequent c would make them part of the longer token. The following d rules out that longer token. No position after the first a was accepting for a token beginning there, so the lexer returns to the position after a. It has inspected n+1 characters beyond that accepting position. This amount is unbounded as n grows.

A and B propose fixed bounds disproved by large n. C is correct. D would violate longest match on inputs that end the prefix with c instead of d.

- **A:** False: proposes a fixed bound of at most one character, disproved by inputs with large n.
- **B:** False: proposes a fixed bound of at most two characters, disproved by inputs with large n.
- **C:** True: before returning token a, the lexer must inspect all n occurrences of b plus character d, requiring n+1 lookahead characters, which is unbounded as n grows.
- **D:** False: violates longest match; token a cannot be emitted immediately because longer candidate ab*c may follow.

**Common misconception:** Recognition by a finite automaton does not guarantee a fixed bound on longest-match backup.

## Q5

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Annihilating polynomial and eigenvalue multiplicities.

The minimal polynomial divides (t−1)(t+1), whose roots are real and distinct. Thus M is diagonalizable with eigenvalues ±1. Trace zero and dimension four force two of each. The determinant is 1 and rank(M−I)=2, proving A,B,C. D need not hold: the block [[1,1],[0,−1]] squares to I but is not symmetric; combine it with diagonal entries 1,−1 for a four-dimensional counterexample.

**Common misconception:** Real diagonalizability does not imply orthogonal diagonalizability or symmetry.

## Q6

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

## Q7

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** SSTF fairness under ongoing arrivals.

Repeated nearby requests can always offer a shorter seek than the distant request. The scheduler can keep choosing them forever, proving B. A's bound ignores future arrivals. C confuses local efficiency with fairness. D only resolves equal distances and cannot defeat strictly nearer arrivals.

**Common misconception:** A finite queue argument cannot establish starvation freedom under unbounded new arrivals.

## Q8

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Shared open-file offsets after dup.

fd1 and fd2 share an open-file description and offset; fd3 does not. The first reads advance the shared offset to 3 and fd3's offset to 1. Seeking fd2 to 1 also sets fd1's offset to 1. Its final two-byte read returns bc. A ignores the seek; B resets to zero; D starts at offset two.

**Common misconception:** Descriptor identity is different from the identity of the underlying open-file description.

## Q9

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** An epsilon production selected by FOLLOW.

b belongs to FOLLOW(A), since S→Ab. With lookahead b, the predictive table selects A→ε: remove A from the stack and do not advance input. B is correct. A consumes a token too early; C requires lookahead a; D ignores the epsilon/FOLLOW rule.

**Common misconception:** A table entry for an epsilon alternative is determined by FOLLOW, not by a literal input epsilon.

## Q10

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Tagged translations and stale mappings.

Different ASIDs distinguish P's and Q's translations, so switching need not flush P's entries (A). Both ASID and virtual page number are needed to identify a particular translation, refuting B. Recycling an ASID may make old entries falsely match a new address space, so invalidation may be required (C). Changing a mapping can still make a tagged entry stale, refuting D.

**Common misconception:** Tags avoid unnecessary context-switch flushes but do not make stale entries correct.

## Q11

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Products of rank-one projections.

Since uᵀu=vᵀv=2 and uᵀv=1, PQ=uvᵀ/4. This is a nonzero outer product and has rank one (A). Its trace is vᵀu/4=1/4 (B). Its (1,2) entry is zero while its (2,1) entry is 1/4, refuting symmetry (C). The vector u is an eigenvector with eigenvalue 1/4; the two-dimensional kernel vᵀx=0 supplies two zero eigenvalues, proving D.

**Common misconception:** Two symmetric matrices need not have a symmetric product unless they commute.

## Q12

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Integer promotion and unsigned conversion.

The addition is performed after integer promotion and is representable; assignment converts the result back modulo 256. Starting at an even value and adding two modulo 256 always leaves i even. It never becomes 255, and every even eight-bit value is less than 255. The loop is infinite (B). A,C wrongly claim termination; D mistakes conversion wraparound for signed overflow.

**Common misconception:** Promotion does not prevent wraparound when a representable sum is assigned back to a narrower unsigned type.

## Q13

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Overlapping pattern occurrences.

The windows ending at positions 3 and 5 are both 101. The detector emits two pulses, so B holds. A disallows the overlap, C counts the three possible windows without testing them, and D counts bits rather than matches.

**Common misconception:** An overlapping detector may reuse the last bit of an earlier match.

## Q14

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Flow versus congestion control.

The advertised window is receiver-buffer flow control, so ordinary new data cannot exceed its zero allowance (B). It is not evidence of router loss (A), does not itself close the connection (C), and does not require the independent congestion window to be zero (D).

**Common misconception:** Receiver capacity and network congestion are different constraints on sending.

## Q15

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Structural versus data hazards.

IF and MEM require the same single port concurrently. Forwarding carries operand results but adds no memory port, so A holds and D fails. Neither arithmetic overflow nor a branch/control dependency follows, eliminating B and C.

**Common misconception:** Assuming complete forwarding removes every pipeline stall.

## Q16

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Quantifiers in the pumping lemma.

Regularity promises at least one pumpable valid decomposition. Showing that one chosen decomposition fails does not exclude another. For the selected word, every allowed y lies in the initial zeros and has positive length; pumping it down breaks equal counts. That universal step repairs the proof, as A says. B is not required, C incorrectly bans a permitted pumping exponent, and D reverses the length condition.

**Common misconception:** Choosing the adversary's decomposition in a nonregularity proof.

## Q17

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Contextual meaning and limited claims.

The passage explicitly uses “economical” for efficient use of components, making A correct. It does not establish low cost (B), no components (C), or necessarily higher cost (D).

**Common misconception:** Converting a statement about resource efficiency into an unsupported price claim.

## Q18

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** SLR actions from items and FOLLOW sets.

S→L·=R prescribes a shift on '='. The completed R→L· prescribes a reduction on every symbol in FOLLOW(R), including '='. Both actions enter the same cell, creating the shift–reduce conflict B. A ignores the reduction rule, C requires a second completed production, and D confuses ordinary completion with the augmented start acceptance item.

**Common misconception:** Using LR(1) item-specific lookahead reasoning in an SLR table built from FOLLOW sets.

## Q19

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Undo/redo recovery.

T1 committed, so recovery ensures its X=8 update is present through redo if necessary. T2 did not commit, so its Y=9 update must be undone to Y=4 if it reached disk. The final pair is (8,4), C. A loses committed work, B retains uncommitted work, and D does both.

**Common misconception:** Letting the accidental precrash disk state determine the final recovered values.

## Q20

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Range restriction and infinite-domain complements.

The result is every integer outside finite R, which is infinite. A correctly identifies the missing range restriction. B reverses the meaning of negation; C contradicts the infinite complement; D incorrectly treats negation itself as a safety guarantee.

**Common misconception:** Silently switching from the stated infinite domain to a finite active domain.

## Q21

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Ordered reflections.

The first reflection sends (x,y) to (x,−y); the second swaps the coordinates, producing (−y,x), A. B gives the reverse-order composition, C is a half-turn, and D gives only the first reflection.

**Common misconception:** Assuming transformations commute.

## Q22

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

## Q23

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

## Q24

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: recognizability versus decidability. The existing acceptance guarantee plus halting rejection for every nonmember gives a correct total decision procedure (B). A only describes tape symbols; C gives a single successful case; D holds for recognizers that may loop and therefore is insufficient. Deciders must halt on all inputs.

## Q25

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: agreement and past tense. In the neither/nor construction the nearer subject is singular supervisor, giving was. The decision occurred yesterday, requiring announced. B supplies both. A has the wrong second verb and plural agreement; C lacks a finite past-tense second verb; D uses present announce. Check both blanks, not just one.

## Q26

**Correct answer:** D

Candidates I, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) IV.
- **B: Incorrect.** It includes invalid candidate(s) II, III and omits valid candidate(s) I, IV.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: cube union and don't-care expansion. The cubes cover respectively {0000,0001,0100,0101} and {0000,0001,1000,1001}. Their union has six minterms, while −−0− has eight; the missing ones are 1100 and 1101. Hence B is false. These are explicitly don't-cares, so the larger cube contains no OFF minterm: C is false and D true. Ordinary pairwise Quine–McCluskey combination needs matching dash positions and one remaining bit difference; A correctly notes that these two original cubes do not meet that direct rule. A valid larger implicant can still be reached by using additional don't-care cubes.

## Q27

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: negative DNS caching. The cached absence result can remain valid at the resolver until its TTL expires, C. A falsely prohibits later creation, B confuses transport with record updates, and D incorrectly makes the lifetime infinite. An authoritative change does not instantly invalidate every cached answer.

## Q28

**Correct answer:** B

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **D: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: essential prime implicants. Every column is covered by two rows, so no row uniquely covers a required minterm; B is true and A false. Any two rows cover all three columns, proving C. D is false: a cover need not contain an essential row. Covering many columns alone does not establish essentiality.

## Q29

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Area ratios with a shared height.

Write the rectangle's dimensions as width w and height h. The triangle has base w/2 along the top edge and perpendicular height h, hence area wh/4. The quadrilateral occupies3wh/4. The ratio is1:3, option B. A, C and D would allocate respectively one-third, one-fifth and two-fifths of the rectangle to the triangle, inconsistent with its base and height.

**Misconception:** Taking the ratio of the top-edge lengths as the ratio of areas.

## Q30

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

q points to the pointer variable p, so(*q)++ changes p from a+1 to a+2. Then **q names a[2], while*(p−1) is a[1]=4. The update changes a[2] from6 to10; p−a is2. C is correct. A omits both updates, B fails to update p's position, and D adds the wrong array value. Parentheses distinguish incrementing a pointer through another pointer from incrementing an array element.

## Q31

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The empty string begins and ends with an empty stack, so A is true. Every accepted prefix avoids a pop from empty, establishing C. Equal totals are insufficient: '())(' has equal totals but its third character tries to pop an empty stack. Thus B and D are false. Global balance and prefix balance are separate requirements.

## Q32

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The lookup finds the new binding for the reused endpoint, so B describes a possible misdelivery. A assumes unavailable historical mapping information. UDP supplies no universal transport sequence-number protection, disproving C. Expiration is local state management and cannot guarantee absence of delayed datagrams, disproving D.

## Q33

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Both f(n)=2n and f(n)=2n+(n−1)(n−2)(n−3) fit all observations but give different values at4. Thus C is true and A,B unjustified. D is contradicted by either example. Finite observations do not specify an unrestricted function uniquely.

## Q34

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Left cancellation makes x↦ax injective. On a finite set it is then surjective, proving A and giving b with ab=e, proving B. Now a(ba)=(ab)a=a=ae, so cancellation yields ba=e, proving C. On an infinite set an injective map need not be surjective; nonnegative integers under addition supply a cancellative monoid with noninvertible positive elements, disproving D.

## Q35

**Correct answer:** A

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Q covers a superset of P's columns at lower cost. If a cover contains P but not Q, replacing P by Q preserves coverage and reduces cost; if it already contains Q, dropping P preserves coverage. Thus A,B hold. C ignores dominance, and D ignores the objective's cost comparison: a larger but more expensive row need not dominate.

## Q36

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Scores are(6+3)/3=3, (8+4)/4=3 and(5+1)/1=6. R has the largest, so C is correct; P,Q do not win and D incorrectly equates all scores. Waiting time is normalized by service demand.

## Q37

**Correct answer:** C

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The full sum is A+(2^w−1−B)+1=A−B+2^w, so its low bits give the modular difference, proving A. Its carry-out is1 precisely when A≥B, the no-borrow case, proving B. This does not diagnose signed overflow, making C false. Identical low differences can arise with and without borrow, disproving D.

## Q38

**Correct answer:** D

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A cycle supplies an alternate route between e's endpoints, so deleting e preserves connectivity, proving B. If a spanning tree used e, deleting e creates a cut; another edge on the cycle crosses that cut and is lighter, permitting a lower-weight tree. Thus C is true and A false. A still heavier edge may lie elsewhere, so D is false. The exclusion concerns its cycle, not a global maximum.

## Q39

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

If p is null, the first comparison is false and short-circuit evaluation bypasses the dereference, proving A,C. Eager evaluation in B could introduce an invalid null dereference. D reverses the required order. Correct intermediate code must preserve which expressions are evaluated, not just a truth-table identity on safe operands.

## Q40

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The subject immediately following the introductory participial phrase should be the person who performed the digitizing: the archivist. C supplies that subject and preserves the intended claim. A makes searching the apparent digitizer, B makes the facility the digitizer and changes the claim, and D makes the documents the digitizer. A passive main clause does not automatically repair a dangling introductory modifier.

## Q41

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Exchanging selected lower-ratio weight for available higher-ratio weight improves value, proving the ratio rule in A. It fills whole items before at most one fractional final item, proving C. Absolute value ignores weight, refuting B. Indivisible packing may require a lower-ratio combination to use capacity better, refuting D; for capacity4, items(3,5),(2,3),(2,3) give such a counterexample.

## Q42

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Context-free languages are closed under intersection with regular languages, proving A. A regular language is context-free, and context-free languages are closed under union and concatenation, proving B,D. They are not generally closed under complement, so C is not guaranteed. The regularity condition on R is essential for the intersection guarantee.

## Q43

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A finite derivative implies f(x)−f(0)=x times a quantity with finite limit, so continuity follows: A. The same argument on each side proves C. The function |x| is continuous but not differentiable at0, refuting B. Equal finite one-sided derivative limits give the common two-sided derivative, refuting D. Unequal derivatives can cause a corner without a discontinuity.

## Q44

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The rule gives (Project,Role)→Employee. Neither project nor role alone determines an assignment under the given constraints, so their pair is a candidate key (A). C describes a direct violation of that dependency. B fails because one employee can hold multiple roles on a project. D discards which roles the employee fills and therefore loses information. A ternary key constrains a combination of two participating entities, not either participant separately.

## Q45

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The last arrival resets count and publishes the phase's sense, allowing the waiter to leave: A. Publishing first could let the waiter enter the next phase and increment count before the old phase resets it, losing that arrival; hence B. Both local senses toggle per phase, distinguishing one release from the next (D). A fast thread can arrive at the next barrier but must wait for the other thread's increment, making C false. These claims use the stipulated atomic increment and sequential consistency; unsynchronized language-level data races are not being assumed away by ordinary C syntax.

## Q46

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Intersection of any two remaining subsets is still a remaining subset and is their greatest lower bound, giving A. The empty set remains below all, giving C. The pair {a,b},{c} has no upper bound in the reduced poset because its only possible upper bound was the removed full set. Hence B,D are false. Removing a top element can destroy joins while preserving all meets.

## Q47

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

With S empty, the implication in Q is true for every y, so every candidate qualifies. The conjunction in P is false for every y; the infinite domain is nonempty, so its universal statement is false and no candidate qualifies. Thus B; A,C,D each mis-handle one quantifier. Logical implication restricts the required witnesses; conjunction does not implement relational division.

## Q48

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Tabular combination requires identical dash positions and exactly one differing fixed bit. A combines {0,1} and {2,3}; its cube covers precisely four ON minterms. C combines {0,2} with {8,10}; allowing the don't-care 10 gives the valid cube {0,2,8,10}. B's inputs have different dash positions and different sizes. Its proposed cube also includes OFF minterm 11. D likewise combines unequal dash patterns, and its proposed cube includes 11. Thus A and C are valid; B and D are invalid. Don't-care minterms may assist grouping, but OFF minterms never may.

## Q49

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Unlink removes a directory entry and decrements the link count. The open reference still keeps the file accessible through d after the count reaches zero. Final reclamation occurs after that reference is closed, so B. A ignores the open reference; C invents a pathname; D confuses independent directory entries with their common target.

## Q50

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The clause requiring revisions explicitly limits the panel's support, so qualified means conditional or limited, B. A uses another meaning of the word that is not intended here. C contradicts the stated support, and D contradicts the stated conditions. Context distinguishes a qualified endorsement from an unqualified one.

