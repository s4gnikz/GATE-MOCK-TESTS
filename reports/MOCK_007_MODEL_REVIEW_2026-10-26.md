# Mock 007 model review — 26 October 2026

All 65 stems/options, answers and solutions read and re-derived. Model review, not human or separate-model certification.

## Material clarification
Q32's plain unsigned-char loop was unsuitable as a portable guaranteed-infinite C example: C17 permits assuming termination for certain loops without observable operations. Changed the variable to volatile unsigned char, specified C17 and no external modification, and explained why the termination permission no longer applies. Answer B is unchanged; the complementary and candidate-audit answers remain unchanged as well.

Corrected all three occurrences: Mock007 Q32, Mock044 Q21, Mock088 Q23. Canonical records, adaptation provenance, manifest and registry hashes updated. Backups: archive/mock007-loop-fix-2026-10-26/. Frozen source snapshots remain historical; future reuse must apply this clarification.

Primary reference: [WG14 issue 0436, C11/C17 iteration semantics](https://open-std.org/JTC1/SC22/WG14/issues/c11c17/issue0436.html).

## Fresh computations
- Q45: enumerated all 120 permutations. Of 96 with first position not fixed, 36 have exactly one fixed point, ratio 0.375.
- Q61: propagated survival probabilities for 1000 alternating-coin steps; sum of survival probabilities = 11.272727272727264, agreeing with exact first-step value 124/11.

Other re-derivations checked finite cancellation inverses (Q13), VIPT index limit (Q18), recurrence regularity (Q36), exact product-difference range ±32640 (Q39), injective per-A relation bound 12 (Q41), minimax quadratic lower bound and construction (Q46), multiplier schedule lower bound seven (Q48), negative-cycle reachability (Q51), optimal BST roots (Q53), CFL closure counterexample (Q56), epsilon-cycle runs versus words (Q59), isolated-weight-two minterms (Q60), and strict distance decrease/zero-link counterexample (Q65). All retained keys agree.

Several two-mark questions remain short rule applications (Q38,Q44,Q49,Q50,Q54,Q55,Q57,Q58,Q62). Difficulty strengthening and calibration remain open. No canonical ACCEPTED count change. Next source: Mock 008.
