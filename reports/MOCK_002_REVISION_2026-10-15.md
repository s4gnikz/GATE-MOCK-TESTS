# Mock 002 — Markdown revision checkpoint

Updated 15 October 2026. All 65 questions, the final answer key and all 65 worked solutions are present. **Markdown structure and answer consistency pass; full-series release and renewed independent review of the new questions remain pending.** No Python files were created or executed.

## Changes now in the actual paper

| Q | Revision | Answer |
|---|---|---|
| 13 | Infer merge comparisons from a cross-inversion constraint | 6 |
| 16 | Clarify universal versus possible BST-successor statements | A,C,D |
| 25 | Analyze liveness across a loop back edge | A |
| 31 | Handle a disk request arriving during a LOOK sweep | 205 |
| 32 | Require correctness for arbitrary initial registers | C |
| 38 | Count minimum and next-weight spanning trees | A,B,C |
| 42 | Explicit NAT port-to-host mapping | A,C,D |
| 43 | Compare allocation after freeing and coalescing regions | A: (100,180) |
| 45 | Count byte pairs satisfying overflow and carry conditions | B: 8128 |
| 48 | Conflict versus view serializability with blind writes | B,C,D |
| 51 | Regular restrictions and context-free closure | A,C |
| 53 | Closed edge-distinct walks in a directed multigraph | B: 12 |
| 61 | Successive ACK-relative receive/congestion windows | 5000 |

The pre-revision paper and solutions are preserved in `archive/pre-revision-2026-10-15/Mock_002/`. The incorrect solution-preamble claim that this paper's review provenance resides in the canonical bank was removed. That bank still contains only Mock 001. Do not run the old generator over these Markdown revisions.

## Verification evidence

Unchanged questions retain separate-model evidence in `drafts/mock002_main_review.md`, `drafts/mock002_low_review.md` and `drafts/mock002_high_independent_review.md`, applicable only to matching versions. Q13/Q16/Q25/Q31/Q32 were separately reviewed after revision. New 15 October changes have worked derivations and the following independent computational checks, but not yet fresh separate-model or human review.

Inline PowerShell verification, with no new script files:

| Q | Check | Observed result |
|---|---|---|
| 38 | All five-edge subsets of the ten-edge graph, rejecting cycles | Tree counts by weight: 6→27, 7→45, 8→36, 9→18, 10→4 |
| 43 | Address-by-address memory simulation under both policies | First-fit 100, best-fit 180 |
| 45 | All 65,536 ordered byte pairs | 8,128 qualifying pairs |
| 48 | All 24 serial orders, tracking read source and final writers | Only (2,3,4,1) and (3,2,4,1) |
| 53 | All four-edge sequences over seven distinct directed edges | 12 closed walks without edge reuse |
| 61 | ACK-relative right edges with persistent next sequence number | 2000 + 0 + 3000 = 5000 |

Q51 has general closure proofs, a finite regular union, a nonregular slice and a pumping argument; finite enumeration alone would not establish its infinite-language claims. Q48's deletion claim follows from the forced conflict chain T3→T2→T4→T1. Unchanged Q56 was previously compiled with GCC C11, warnings-as-errors and pedantic checking, producing `8 13 0`; execution supplements the semantic reasoning.

## Structural checks and remaining work

Exactly 65 sequential questions, 65 solutions and 65 final key rows. Total 100 marks, with 30 one-mark and 35 two-mark questions. GA remains 15 marks; mathematics remains Q22,24,29,33,35 and Q39,40,44,54, totaling 13; core CS totals 72. Option counts, question/key marks and types, and all key-versus-solution answers were checked: zero discrepancies. Q48 is MSQ in both its heading and key.

A provisional editorial difficulty split is 27 Medium, 29 Medium-Hard and 9 Hard. This is not calibrated student performance or fresh independent approval. Obtain renewed review of the rewritten questions before claiming full validation.

Next: rebuild Mock 003's repetitive and invalid content with genuinely new questions, backing up its existing version first. Mocks 003–100 remain unchanged and still fail the substantive audit.
