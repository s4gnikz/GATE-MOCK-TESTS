# Mock 002 — front-section difficulty and reasoning audit

Reviewed 2026-10-13. Scope: finalized `mock002_front_questions.md` (Q1–Q35), plus mathematics Q39, Q40, Q44 and Q54 as assessed in `mock002_main_review.md`. This is a model judgment, not measured candidate performance or human review. Questions were not edited. The revised Q13, Q25 and Q31 are used here, not their superseded JSON drafts.

M = Medium; MH = Medium-Hard; H = Hard. Labels assess conceptual depth and expected effort for a prepared GATE candidate, taking the stated mark value into account. Multiple arithmetic operations alone do not establish two meaningful reasoning steps. “Yes” in the technical-step column requires at least two connected inferences, or a state trace followed by a distinct conceptual inference/calculation. “No” means that criterion is not demonstrated; it does not mean the question is invalid. GA entries are N/A because the 50% requirement applies to technical questions.

Q1, Q2 and Q6 lie at the easier end of M and could be classified Easy-Medium under a wider scale. They should not be counted as evidence of a challenging paper. Other M items include conventional short one-mark applications; M does not certify that every candidate will find them difficult.

| Q | Subject | Difficulty | Two meaningful technical steps? | Justification |
|---|---|---|---|---|
| 1 | General Aptitude | M | N/A | Context directly supplies the vocabulary meaning; lower edge of M. |
| 2 | General Aptitude | M | N/A | Infer a doubling time and scale to five doublings; routine, lower edge of M. |
| 3 | General Aptitude | M | N/A | Test candidate logical rules against counterexamples and confirm the survivor. |
| 4 | General Aptitude | M | N/A | Combine adjacent-face information to identify the only opposite face. |
| 5 | General Aptitude | M | N/A | Short recurrence trace or first-difference transformation. |
| 6 | General Aptitude | M | N/A | Form the inner-area equation and reject the inadmissible root; familiar geometry. |
| 7 | General Aptitude | M | N/A | Recognize the past counterfactual and repair a dangling modifier. |
| 8 | General Aptitude | M | N/A | Track two withdrawals with different replacement fluids. |
| 9 | General Aptitude | MH | N/A | Split placement cases and distinguish possible from necessary statements. |
| 10 | General Aptitude | MH | N/A | Derive both extremal bounds from projections and construct arrangements attaining them. |
| 11 | Computer Organization and Architecture | M | Yes | Map all references into one set, then track LRU state to distinguish conflicts from capacity. |
| 12 | Programming and Data Structures | M | Yes | Infer subtree partitions from traversal closure, then count independent unary-child orientations. |
| 13 | Algorithms | MH | Yes | Rule out early exhaustion in both directions using inversion bounds, then give an attaining merge. |
| 14 | Computer Organization and Architecture | M | No | One cache-visibility principle selects completed write-back; distractors require little additional inference. |
| 15 | Algorithms | M | Yes | Infer ancestry from intervals, then combine a tree path with the reverse edge to form a cycle. |
| 16 | Programming and Data Structures | M | No | All claims are immediate consequences of the standard right-subtree minimum characterization. |
| 17 | Theory of Computation | M | Yes | Propagate the active set through input symbols, then compute the final transitive epsilon closure. |
| 18 | Compiler Design | M | Yes | Track successive versions symbolically, then compare complete final states against replacements. |
| 19 | Theory of Computation | M | Yes | Infer which productions a yield requires and show that their nesting orders give different trees. |
| 20 | Computer Networks | MH | Yes | Establish converged metrics and separately propagate synchronous stale advertisements after failure. |
| 21 | Digital Logic | M | Yes | Derive binade spacing, apply midpoint parity, and check exact representability across exponents. |
| 22 | Engineering Mathematics | MH | Yes | Eliminate symbolically, distinguish invertibility from unpivoted LU existence, then assess a row swap. |
| 23 | Compiler Design | MH | Yes | Contrast concrete path sums with abstract joins, then assess whether branch-local evaluation restores a constant. |
| 24 | Engineering Mathematics | M | Yes | Find the crossover of the upper envelope, then integrate the appropriate expression on each interval. |
| 25 | Compiler Design | M | Yes | Track kills and uses across the back edge, then exclude values overwritten before all future uses. |
| 26 | Digital Logic | M | No | A short XOR cancellation and gating identity; conservatively treated as one Boolean simplification. |
| 27 | Operating Systems | M | Yes | Simulate preemptions using remaining bursts, then recover waiting times from completion times. |
| 28 | Databases | MH | Yes | Find both composite candidate keys, classify prime attributes, then distinguish 3NF from BCNF. |
| 29 | Engineering Mathematics | MH | Yes | Recover the combined mean and aggregate squared deviations or second moments before computing variance. |
| 30 | Computer Networks | M | Yes | Derive aligned payload capacity, then convert and add displacement to the original fragment offset. |
| 31 | Operating Systems | M | Yes | Infer the head's position/direction at the arrival event, then preserve the sweep and compute total movement. |
| 32 | Computer Organization and Architecture | M | Yes | Translate write/read timing into the minimum dependency gap, then construct a consistent schedule for both dependencies. |
| 33 | Engineering Mathematics | MH | Yes | Compute modular inverse composition, identify the resulting translation, then determine its order. |
| 34 | Databases | M | No | One page-alignment bound plus a stated fixed cost; adding the two index reads is not a separate meaningful inference. |
| 35 | Engineering Mathematics | MH | Yes | Apply degree/Euler conditions and construct a compatible bridge-and-triangles counterexample for the other universal claims. |
| 39 | Engineering Mathematics | H | Yes | Constrained colouring enumeration and rotational fixed-point analysis establish the orbit count. |
| 40 | Engineering Mathematics | H | Yes | Build a bivariate generating function for adjacency restrictions, extract even parity, and simplify. |
| 44 | Engineering Mathematics | H | Yes | Prove a finite serial transitive irreflexive relation impossible, then build witnesses for feasible property combinations. |
| 54 | Engineering Mathematics | H | Yes | Derive the symmetric circulant form, decompose invariant subspaces, and count idempotent eigenvalue assignments. |

## Counts

| Scope | Questions | M | MH | H | Technical two-step Yes | Technical No |
|---|---:|---:|---:|---:|---:|---:|
| Q1–Q10: GA | 10 | 8 | 2 | 0 | N/A | N/A |
| Q11–Q35: technical | 25 | 17 | 8 | 0 | 21 | 4 |
| Q1–Q35 combined | 35 | 25 | 10 | 0 | 21 | 4 |
| Mathematics Q39,Q40,Q44,Q54 | 4 | 0 | 0 | 4 | 4 | 0 |
| All questions in this audit | 39 | 25 | 10 | 4 | 25 | 4 |

The front 35 questions therefore contain 71.4% M, 28.6% MH and no H. The 39-question audited scope contains 64.1% M, 25.6% MH and 10.3% H. Neither percentage is a full-paper distribution.

Technical two-step coverage is 21/25 = 84% in the front technical section and 25/29 = 86.2% including the four hard mathematics questions. For the whole paper's 55 technical questions, at least 28 must qualify. These reviewed items supply 25; at least three of the remaining 26 core two-mark questions must qualify before the full-paper requirement can be confirmed.

## Whole-paper implications

A natural 65-question rounding of the requested 40%/45%/15% target is 26 M, 29 MH and 10 H. Given the assessed 25 M, 10 MH and 4 H here, exact attainment would require the remaining 26 questions to be 1 M, 19 MH and 6 H. That is a demanding distribution for the remaining core section; it must be established by its independent content audit, not achieved by changing labels. Small configured variation may be acceptable, but the actual final distribution and any deviation must be disclosed.

This audit confirms that the redesigned front technical questions meet the intended short reasoning standard overall. It does not alone establish the full paper's target difficulty distribution. The front section remains predominantly medium, with a few routine GA questions at its lower edge.
