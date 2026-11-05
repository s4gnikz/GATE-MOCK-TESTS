# Mock 002 second targeted review — 26 October 2026

Reviewed Q36,37,41,46,47,49,50,52,55,56,57,58,59,60,62,63,64,65. Model-based re-derivation, not human or separate-model review.

## Corrections
Q63's detailed option A note incorrectly named P1P4/m4; corrected to P1P2/m6. Option B incorrectly named P1P2P4; corrected to P1P3P4, with the same nine-literal cost. The correct answer remains C.

Q58's detailed option B note listed b after t even though the algorithm stops at t. Corrected to settling s,a,t and stopping. Answer remains A,B.

Propagated matching erroneous explanations to five SOLUTIONS documents (Mocks 002,039,055,076,099), the canonical bank and two adaptation provenance files. Backups are in archive/explanation-corrections-2026-10-26/. Frozen historical source snapshots are unchanged; apply these corrections when reusing their derivations.

## Re-derivation evidence
| Q | Retained result | Reason |
|---|---|---|
| 36 | 1536 | 65536−200×256−800×16, with feasible prefix allocation. |
| 37 | 8 | Middle leaf and root split yield seven nodes; final leaf split adds one. |
| 41 | C | Aligned /24,/23,/23,/24 cover; endpoints and middle alignment give matching lower bound. |
| 46 | 3 | Two independent initial values plus post-store potentially aliased load; d=7 and e=c. |
| 47 | A,B,D | Consensus BC is logically redundant and stable through A transitions; ABC is not stable. |
| 49 | 16 | Directory indices 0,0,1,1023 require three tables plus directory. |
| 50 | D | Empty-stack deterministic acceptance without end marker cannot accept a word and its proper extension. |
| 52 | C | Choose three of six subtree keys, then two orders for each child pair: 20×2×2. |
| 55 | A | Shared-to-exclusive upgrade cycle; releasing then acquiring violates two-phase locking. |
| 56 | B | Calls yield (7,6), then (8,13), with pointer offset zero; operations are sequenced. |
| 57 | C | Token beginning at a must scan all n b symbols and d before backing up. |
| 58 | A,B | Path weights 4,15,3; adding four per edge gives 12,23,15. Stopping trace s,a,t. |
| 59 | A,C | FIRST={a}, FOLLOW={b,$}; epsilon causes LR(0) conflict but not SLR conflict. |
| 60 | A,B,D | Direct 0–3, single 4–259, double 260–262; three metadata blocks and 269312 data bytes. |
| 62 | B | For every permitted split, p²< p²+length(y) <(p+1)². |
| 63 | C | Every pair misses one column; triple literal costs 8,9,9,10. |
| 64 | B | Start once, wait without side effects, then sample and increment once. |
| 65 | B | Twelve eliminations plus winner-path length minus one; path lengths range two to four. |

All 30 technical two-mark questions Q36–Q65 now have a saved targeted model review across this report and MOCK_002_TARGETED_REVIEW_2026-10-26.md. No answer-key changes identified. Individual difficulty judgments and whole-paper difficulty distribution remain pending; no records promoted to ACCEPTED.

Verification after edits: 6500 parseable canonical records; each of the five affected solution documents still has 65 sections, with 65 corresponding final-key entries. Question files were not edited.

Next: reconcile existing reviews and current versions for Mock 002 Q1–Q35; then assess overall difficulty and remaining verification gaps before declaring full-paper acceptance.
