# Resumable project checkpoint

Saved 25 October 2026. Latest request completed: another 1,000 adapted variants replaced repetitive occurrences inside the existing papers.

## Current counts
- 100 populated papers, each 65 questions and 100 marks; 6,500 records and unique IDs.
- Round 1: 1,000 complementary-answer/pair variants.
- Round 2: 1,000 NAT-to-MCQ variants.
- Round 3: 1,000 NAT-to-invalid-answer-MSQ variants.
- 3,000 replacements total, in disjoint positions.
- 5,350 distinct normalized versions based on 2,350 underlying source problems.
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
