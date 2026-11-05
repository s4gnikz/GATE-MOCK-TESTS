# Resumable project checkpoint

Saved 25 October 2026. Latest request completed: 800 additional adapted variants replaced repetitive occurrences inside the existing papers.

## Current counts
- 100 populated papers, each 65 questions and 100 marks; 6,500 records and unique IDs.
- Round 1: 1,000 complementary-answer/pair variants.
- Round 2: 1,000 NAT-to-MCQ variants.
- Round 3: 1,000 NAT-to-invalid-answer-MSQ variants.
- Round 4: 800 candidate-validity-audit variants; 350 excess exact occurrences remain across papers.
- 3,800 replacements total, in disjoint positions.
- 6,150 distinct normalized versions based on 2,350 underlying source problems.
- All 100 papers passed the current structural audit. All 4,000 third-round numerical options and 1,000 answer sets passed interval checks.
- 65 prior ACCEPTED records; 6,435 REVIEW_REQUIRED.
- No extra standalone questions, Python files or old template generation.

## Provenance and recovery
Current papers and solutions are linked in INDEX.md. The canonical bank, assembly manifest and uniqueness registry reflect all three rounds.

Round reports: reports/INTEGRATED_1000_REPLACEMENTS.md, reports/INTEGRATED_1000_ROUND2_REPLACEMENTS.md and reports/INTEGRATED_1000_ROUND3_REPLACEMENTS.md; corresponding JSON mappings identify every destination.

Provenance: data/extra_questions.jsonl, data/adapted_variants_round2.jsonl and data/adapted_variants_round3.jsonl. These are historical adaptation records, not extra active assignments.

Backups are under archive/integrated-variants-2026-10-25/, archive/integrated-variants-round2-2026-10-25/ and archive/integrated-variants-round3-2026-10-25/.

Frozen original source bank: archive/integrated-variants-2026-10-25/data/questions.jsonl. Source IDs refer to that snapshot, not necessarily current content at that ID.

## Remaining review
User permits lightweight tweaks and repetitions. Do not claim semantic uniqueness or entirely new reasoning families. Independent correctness, difficulty, multistep quota and rendered export review remain pending. No human review is claimed.

Review original sources once and propagate corrections: ordinary copies keep source answers; round 1 uses complementary/pair mappings; round 2 selects the valid numeric answer; round 3 selects all invalid numeric answers. Recheck distractors if source answers change.

The six-hour continuation should follow this checkpoint for economical quality review, without restarting generation, and notify only on meaningful changes or required action.

## Latest within-paper uniqueness check 100 actual paper files checked: each contains 65 questions, no exact normalized repeat and no repeated tracked original source within the same paper. See reports/WITHIN_PAPER_UNIQUENESS_AUDIT.md. No paper changes needed for this scope. Across-paper exact repeats and semantic similarity remain; do not claim global originality.

## Round 4 completed
User requested reducing 1,150 exact repeated occurrences to a few hundred. Completed: 800 replacements, leaving 350. All 100 papers and all 800 answer mappings passed consistency checks. These are adapted versions, not new reasoning families. See reports/ROUND4_REPLACEMENTS.md and .json; data/adapted_variants_round4.jsonl; archive/integrated-variants-round4-2026-10-25/.

When propagating source corrections, round 4 audit options classify each original candidate as valid or invalid. Recompute the truth vector and ensure exactly one audit option remains correct; regenerate alternative classifications if needed. All prior review limitations remain.

## Technical review checkpoint — 26 October 2026
Persisted targeted model review of Mock 002 Q38,39,40,42,43,44,45,48,51,53,54,61 in reports/MOCK_002_TARGETED_REVIEW_2026-10-26.md. No corrections found; acceptance counts unchanged. Q39 and Q40 received fresh exhaustive small-instance checks; earlier Q45/Q53 enumeration results are recorded. Next scope is listed in the report. Full technical and difficulty review remains pending.

## Continued review — 26 October 2026
Completed model-based targeted review of remaining Mock 002 technical two-mark questions; all Q36–Q65 now covered across the two dated reports. Corrected Q63 option explanations and Q58's stopping trace in all matching live copies and structured records. Keys unchanged. See reports/MOCK_002_SECOND_REVIEW_2026-10-26.md. Next: Q1–Q35 version/evidence reconciliation and whole-paper difficulty assessment. Acceptance counts remain unchanged.

## Continued model review — Mock 002 and Mock 003
Mock 002 Q1–Q35 reviewed; combined with earlier reports, all 65 questions have current targeted model-review coverage. Mock 003 all 65 questions and solutions reviewed, with eight fresh exhaustive/simulation checks. No further answer corrections identified. See reports/MOCK_002_REVIEW_COMPLETE_MODEL_2026-10-26.md and reports/MOCK_003_MODEL_REVIEW_2026-10-26.md. No promotion to ACCEPTED: difficulty, independent review and final rendering gates remain. Next source paper: Mock 004.

## Mock 004 reviewed
All 65 stems/options and solutions re-derived; no answer mismatch. Fresh enumerations checked Q8,Q28,Q41,Q63. See reports/MOCK_004_MODEL_REVIEW_2026-10-26.md for evidence and weak two-mark candidates. Next source paper: Mock 005. Do not repeat completed source checks unless changed.

## Mock 005 reviewed
All 65 questions and solutions received model review; no answer discrepancy. Fresh computational checks: bounded bins, LRU access trace and matrix-chain DP. Evidence and difficulty caveats: reports/MOCK_005_MODEL_REVIEW_2026-10-26.md. Next source: Mock 006. Acceptance unchanged.

## Mock 006 reviewed
All 65 stems/options and solutions model-reviewed with fresh spanning-tree, bit-string and knapsack enumerations. No correction identified. Evidence: reports/MOCK_006_MODEL_REVIEW_2026-10-26.md. Next source: Mock 007. Full-series technical acceptance and difficulty strengthening remain unfinished.

## Mock 007 reviewed and clarified
All 65 questions/solutions reviewed. Fixed C17 loop ambiguity in Mock007 Q32 and its Mock044 Q21 / Mock088 Q23 adaptations; keys unchanged, live hashes updated. See reports/MOCK_007_MODEL_REVIEW_2026-10-26.md and its backup reference. Future use of historical source snapshots must apply the volatile/C17 clarification. Next source: Mock 008.

## Mocks 008 and 009 reviewed
All 130 questions and solutions received model review; no answer mismatch identified. Fresh exhaustive/state-recurrence checks cover three questions per paper. See reports/MOCK_008_MODEL_REVIEW_2026-10-26.md and reports/MOCK_009_MODEL_REVIEW_2026-10-26.md for evidence and difficulty limitations. Next source: Mock 010. Acceptance remains unchanged; short two-mark questions require strengthening before difficulty certification.

## Mock 010 reviewed
All 65 questions and solutions model-reviewed; no answer mismatch found. Three fresh computational checks saved in reports/MOCK_010_MODEL_REVIEW_2026-10-26.md. Next source: Mock 011. Review coverage through Mock 010 is not full technical acceptance; difficulty strengthening remains necessary.

## Mock 011 and whole-series structural recheck
Model review now covers source Mocks 002–011 in the dated reports, alongside prior accepted Mock 001. Mock 011 has no answer discrepancy and three new enumeration checks. Next source: Mock 012. Do not restart Mock 002 or obsolete paper-generation tasks.

A fresh 100-paper structural recheck after the C-loop clarification found zero errors: 6,500 records/unique IDs, 6,150 distinct normalized bodies, 350 excess exact occurrences, no within-paper exact duplicate. See reports/STRUCTURAL_RECHECK_2026-10-26.md for the precise scope. This does not replace remaining correctness, difficulty, syllabus and rendering gates. Accepted record count remains 65.

## Mock 012 reviewed
All 65 questions and solutions were re-derived; no answer discrepancy found. New computational checks cover Q8, Q39, Q50 and Q52. See reports/MOCK_012_MODEL_REVIEW_2026-10-26.md. Next source: Mock 013. Difficulty calibration and broader technical gates remain open; acceptance count unchanged.

## Mock 013 reviewed
All questions, answer choices and worked solutions received model review; no answer discrepancy found. Targeted computation checked the recursion tree and matrix entry. See reports/MOCK_013_MODEL_REVIEW_2026-10-26.md. Next source: Mock 014. Difficulty and full technical acceptance remain pending.

## Mock 014 reviewed
All 65 questions and solutions received model review; no answer discrepancy found. Targeted computations and limitations are documented in reports/MOCK_014_MODEL_REVIEW_2026-10-27.md. Next source: Mock 015. Full technical and difficulty acceptance remain pending.

## Mock 015 reviewed
All 65 questions and solutions were re-derived; no answer mismatch found. Q43 was exhaustively counted across all 256 operand pairs. See reports/MOCK_015_MODEL_REVIEW_2026-10-28.md for evidence and limits. Next source: Mock 016. Full technical and difficulty acceptance remain pending.

## Mock 016 reviewed
All 65 stems, options, keys and worked solutions received model review; no answer mismatch identified. Targeted derivations and limitations are recorded in reports/MOCK_016_MODEL_REVIEW_2026-10-28.md. Next source: Mock 017. Full technical and difficulty acceptance remain pending.

## Mock 017 reviewed
All 65 question stems, options, answer keys and solutions received model review; no answer mismatch identified. Targeted derivations and review limits are in reports/MOCK_017_MODEL_REVIEW_2026-10-28.md. Next source: Mock 018. Full technical and difficulty acceptance remain pending.

## Mock 018 reviewed
All 65 question stems, options, answer keys and solutions received model review; no answer mismatch identified. Targeted derivations and limits are in reports/MOCK_018_MODEL_REVIEW_2026-10-30.md. Next source: Mock 019. Full technical and difficulty acceptance remain pending.

## Mock 019 reviewed
All 65 question stems, options, answer keys and solutions received model review; no answer mismatch identified. Targeted derivations and limitations are recorded in reports/MOCK_019_MODEL_REVIEW_2026-10-30.md. Next source: Mock 020. Full technical and difficulty acceptance remain pending.
