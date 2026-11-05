# Aptitude and mathematics content audit

Reviewed 13 October 2026. Scope: every GA/math occurrence in Mocks 003–100, grouped by actual task and numeric variant, rather than by the often incorrect concept labels. This is model-based review, not human review. Papers were not edited. No Python files were created or executed for this audit.

## Findings by task family

| Actual task | Occurrences | Assessment of intended difficulty | Main finding |
|---|---:|---|---|
| Four-person selection with biconditional | 613 | Easy | Every supplied answer is wrong; correct count is 1 |
| Subject–verb agreement | 61 | Easy when well formed | 37 items have no grammatical option; 24 have A correct |
| Same-ratio liquid additions | 122 | Easy | Ratio never changes; 16 NATs demand an unstated rounded value as exact |
| Meaning of ephemeral | 61 | Easy | A correct; identical repeated vocabulary item |
| Constant-second-difference sequence | 123 | Easy | Arithmetic consistent with intended rule; only constants vary |
| Complete-graph spanning-tree count | 606 | Easy | Formula supplied; 153 option sets contain duplicate correct choices |
| Determinant of a matrix polynomial | 110 | Medium | Values correct; same reasoning repeated with four eigenvalue lists |
| Polynomial integration on [0,1] | 111 | Easy | Values correct at requested precision; three numerical variants |
| Validity of quantified formulas | 55 | Medium in option form | 14 NAT versions omit the formulas and use a nonnumeric key |

These nine families cover 1,862 question occurrences: all 980 GA slots and all 882 mathematics slots in Mocks 003–100. The intended difficulty assessment does not rehabilitate an invalid question: an incomplete NAT or an MCQ with no correct choice is ungradable, not hard.

## 1. Four-person selection: 613 wrong answers

Example: [Mock 050 Q3](../papers/Mock_050/README.md), repeated as Q4, Q6 and Q9 in that paper. In each instance P implies not Q, R if and only if S, and exactly two people must be selected.

There are six possible pairs. {P,Q} violates the first condition. {P,R}, {P,S}, {Q,R}, and {Q,S} each violate R iff S. Only {R,S} remains. Therefore the answer is **1**, or **D** for the supplied options [3,2,4,1]. All 445 MCQ and 72 MSQ occurrences are keyed A; all 96 NAT occurrences are keyed 3.

The worked solution notices that several pairs violate the condition, then asserts 3 under an undefined “relaxed parity.” Relaxing a stated constraint changes the problem and cannot justify its key. This defect affects every paper from 003 through 100.

Changing the introductory label to “reading comprehension,” “paper folding,” “geometry,” “data interpretation,” or “spatial transformations” does not change the underlying selection task or provide coverage of those topics. There are no genuine spatial reasoning tasks in these 980 GA slots.

## 2. Grammar: 37 questions with no correct option

The 17 “each of the candidates” variants offer “Neither of the options has acceptable to the board” as A. This lacks the required verb construction: “is acceptable” or “has been acceptable” would work. The subject in the options also differs from the supplied original.

The 20 “the committee” variants offer “Neither of the options has announced its acceptable to the board.” This too is malformed, and none of the other choices repairs it. Example: [Mock 004 Q3](../papers/Mock_004/README.md).

The remaining 24 “neither of the options” variants correctly use “Neither of the options was acceptable to the board.” All are elementary agreement questions, not two-mark medium-hard reasoning tasks.

## 3. Mixture: unchanged ratios and unjustified exact keys

The added components have the same ratio as the original mixture, so the percentage stays constant. The four variants yield 60%, 400/7%, 500/7%, and 70% for ratios 3:2, 4:3, 5:2, and 7:3, respectively.

For 4:3 and 5:2, 57.1% and 71.4% are rounded approximations, not exact values. Sixteen NAT versions insist on these exact entries without asking for one decimal place or providing a tolerance. Example: [Mock 010 Q8](../papers/Mock_010/README.md). Repair the precision requirement before grading. In option form, the intended rounded choice is apparent, but the stem should still specify rounding.

The solution label “Powers and logarithms” does not match a percentage-mixture calculation.

## 4. Numerical sequences and vocabulary

All 12 sequence variants follow the intended constant second difference of 2. The next terms are:

| First term | Initial first difference 4 | Difference 5 | Difference 6 | Difference 8 |
|---|---:|---:|---:|---:|
| 2 | 42 | 47 | 52 | 62 |
| 5 | 45 | 50 | 55 | 65 |
| 8 | 48 | 53 | 58 | 68 |

The arithmetic in each displayed variant agrees. A finite list alone does not mathematically determine its continuation; specifying the second-difference rule would make the NAT uniquely determined. At ordinary aptitude-test level the intended pattern is straightforward. These are numerical changes to one family, not 123 original reasoning tasks. Labels claiming permutations and combinations are inaccurate.

“Ephemeral” means short-lived, so A is correct in all 61 copies. Option B is not logically the opposite of ephemeral: a large or monumental structure could also be temporary. The solution's rationale for B should say that it does not give the word's meaning.

## 5. Mathematics

### Complete graphs

The supplied formula gives K4: 4² = 16, K5: 5³ = 125, and K6: 6⁴ = 1296. The formula is printed in the question, reducing the task to exponentiation. All 153 option-based K4 variants repeat 16 in A and D, so an MCQ lacks a unique correct option; an MSQ requires both A and D. Example: [Mock 050 Q30](../papers/Mock_050/README.md).

These questions are repeatedly tagged as probability distributions, sets and functions, calculus extrema, statistics, and other topics. Those tags do not establish coverage. The actual concept is graph enumeration.

### Matrix polynomial

For each eigenvalue λ of M, λ²+2 is an eigenvalue of M²+2I; the determinant is their product. The four lists give:

- (-1,2,3): 3×6×11 = 198.
- (1,1,3): 3×3×11 = 99.
- (1,2,4): 3×6×18 = 324.
- (2,3,5): 6×11×27 = 1782.

The conclusion does not require M to be diagonalizable. These are reasonable medium-level questions individually, but their numerical variants fail the project's uniqueness requirement.

### Integrals

For n = 2,3,4, the integral of xⁿ+nx over [0,1] is 1/(n+1)+n/2, giving 1.33, 1.75, and 2.20 when rounded to two decimal places. The keys are arithmetically correct; 2.2 and 2.20 represent the same numeric entry. Each is basic integration, not a difficult application. A label saying “limits continuity and differentiability” does not alter the task.

### Predicate logic

In the option-based version A is valid: if every P implies Q and every object satisfies P, every object satisfies Q. For B use a two-element domain with P true only at the first object and Q false everywhere: the outer antecedent is vacuously true but ∀x(P→Q) is false. For C and D use a two-element domain with P true only at one object and Q only at the other; witnesses cannot be combined for C, and the disjunction cannot be moved outside the universal for D.

Fourteen NAT versions retain “Which of the following formulas” but remove all formulas, and print ['A'] as an exact numerical key. Those versions cannot be answered as written.

## Required action

Mocks 003–100 should not be used to measure GATE readiness. Correcting these keys would still leave the global repetition, shallow reasoning, missing topic coverage, and malformed question types. Replace the repeated families with distinct reasoning tasks; preserve only individual sound items where they fit an independently designed paper.

The accompanying question inventory and occurrence reports identify all paper/question references. The review does not claim that existing metadata or a repeated worked solution constitutes independent verification.
