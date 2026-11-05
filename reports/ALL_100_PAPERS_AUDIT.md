# Review of all 100 mock papers

Audit date: 13 October 2026. **The series is not ready for use as 100 original, medium-to-hard GATE examinations.** All 100 README papers and 100 solution documents exist, but Mocks 003–100 have systematic content failures. The papers have been preserved unchanged. No Python files were created or executed for this audit.

## Scope and method

All 6,500 question slots, all answer tables, and all corresponding solution sections were extracted from the current Markdown files. Questions were compared after removing headings, options, answer-format instructions, separators and whitespace differences. This produces 205 distinct stems across the series: 130 in Mocks 001–002 and 75 in Mocks 003–100.

For Mocks 003–100, all 75 distinct stems, numeric variants, options, and corresponding solution variants were examined as 35 reasoning families. Their findings were mapped back to every one of the 6,370 occurrences. This is an exhaustive occurrence inventory with family-based model review, **not 6,500 separate blind solves, human review, or proof of internet-wide originality**. Identical questions need not be solved hundreds of times to establish the same defect. Difficulty is an editorial assessment for a prepared candidate, not a measured student-performance statistic.

Supporting documents:

- [Aptitude and mathematics: 1,862 occurrences](AUDIT_APTITUDE_MATHEMATICS.md).
- [Systems subjects: 2,505 occurrences](AUDIT_TECHNICAL_SYSTEMS.md).
- [Theory, algorithms, programming and compilers: 2,003 occurrences](AUDIT_TECHNICAL_THEORY.md), with [exact reference appendix](AUDIT_TECHNICAL_THEORY_REFERENCES.md).
- [Question-by-question findings for Mock 003–100](AUDIT_QUESTION_FINDINGS.csv): question ID, marks, type, key, actual family, difficulty and issue codes.
- [All 100 structural results](AUDIT_STRUCTURE.csv), [duplicate groups and every occurrence](AUDIT_DUPLICATES.csv), [full extracted inventory](AUDIT_QUESTION_INVENTORY.json), and [file hashes](AUDIT_FILE_HASHES.csv).

## What passes

All 100 papers have 65 sequentially numbered questions, 65 answer-key rows, and 65 solution headings. Each totals 100 marks with 30 one-mark and 35 two-mark questions. GA occupies Q1–Q10 and contributes 15 marks. The solution labels allocate 13 marks to mathematics using five one-mark and four two-mark slots. Each final answer table follows Q65.

These checks establish the document skeleton, not correctness. In particular, many topic labels describe skills that the associated question does not test.

## Critical findings

| Finding in Mock 003–100 | Verified count | Consequence |
|---|---:|---|
| Question occurrences | 6,370 | Only 75 distinct stems and 35 actual reasoning families |
| Duplicate occurrences beyond one of each exact stem | 6,295 | 98.82% of this batch repeats an already present stem |
| Within-paper duplicate excess | 24–34 per paper | Even individual papers repeatedly ask the same stem |
| MCQ keys equal A | 3,408 of 3,408 | Option-position pattern makes scores meaningless |
| MSQs keyed only A | 1,182 of 1,182 | Fails the project's multiple-correct MSQ design requirement |
| NAT keys that are not numbers | 963 of 1,780 | Includes A and ['A']; cannot be graded as numerical answers |
| Wrong four-person-selection answers | 613 | Correct count is 1; supplied count is 3 |
| Duplicate option sets | 163 | 153 K4 items repeat the correct answer; 10 cache items repeat a distractor |
| Grammar questions with no grammatical option | 37 | No defensible correct MCQ answer |
| Counter timing questions missing essential assumptions | 215 | Different permitted circuits imply different frequencies |
| Reno fast-recovery questions with unsupported key | 45 | Missing MSS/FlightSize and confusion between recovery entry and exit |
| Non-CFL questions with inconsistent alphabet | 166 | Stem specifies {a,b}; intended choice contains c |

Counts overlap. Do not add the rows to claim a total number of defective questions. The question-level findings file contains 3,348 distinct occurrences with at least one listed format/content/solution concern; this excludes the universal originality failure and is not a claim that the remaining occurrences satisfy all requirements.

### Examples with corrected reasoning

1. **Mock 050 Q3, Q4, Q6 and Q9:** R iff S forces them to be selected together or not at all. {P,Q} is forbidden. Only {R,S} works, so the answer is 1. The solution contradicts itself and then invents an unstated “relaxed parity.” The same task is labelled as several unrelated GA topics.
2. **Mock 050 Q20:** a NAT asks when a Banker's-algorithm state is safe, ending with “if and only if,” but gives no alternatives or numerical task. Its key is A.
3. **Mock 050 Q30:** K4 has 16 spanning trees, but both A and D say 16. A single-answer key is invalid.
4. **Mock 004 Q3:** the keyed option says “has announced its acceptable to the board.” It is not a grammatical sentence.
5. **Mock 005 Q18:** Reno entry to fast recovery uses the threshold plus three segment sizes, not simply half the old congestion window. The missing segment size and flight-size assumptions prevent a unique numerical answer. See [RFC 5681 section 3.2](https://www.rfc-editor.org/rfc/rfc5681#section-3.2).

## Actual question level

Mocks 003–100 are **predominantly easy or routine medium, with many ungradable items**. The “Medium to Hard” heading is not supported by their content. No genuine medium-hard or hard family was identified in this batch.

The conservative family classification maps 4,599 occurrences to an Easy intended task, 1,345 to Medium, and 426 to inherently ungradable families (counter timing, Reno and the inconsistent-alphabet language question). This does **not** mean the first two groups are all valid: wrong keys, missing options, ambiguous conventions and other defects are recorded separately. Invalidity is not a level of difficulty.

Examples of low demand include recalling CRC degree, recalling merge-sort complexity, substituting into a formula supplied in the question, preserving a mixture ratio by adding the same ratio, and doing two pointer offsets. Awarding two marks or assigning a “Hard” label does not add reasoning depth. Numerical substitutions across many papers do not create new problems.

The target of approximately 40% Medium, 45% Medium-Hard and 15% Hard is therefore not met. The repeated tasks would also become easier after first exposure, further reducing their value as separate mocks.

## Coverage and verification records

Actual mathematics in the 98-paper batch consists of only four families: complete-graph spanning-tree counting, a matrix-polynomial determinant, a short polynomial integral, and a standard quantified-logic question. GA has only five families. There is no genuine spatial reasoning in this batch despite spatial labels. Technical labels similarly claim system calls, processes, ER modelling, tuple calculus, sockets and other topics while repeating safe-state definitions, B+ occupancy and CRC degree.

The structured bank still has **65 records, all belonging to Mock 001**. The 99 later Markdown papers are not represented by 6,435 accepted verified canonical records. The existing INDEX, CHECKPOINT and FINAL_VALIDATION_REPORT predate the newly populated papers and must not be used as evidence that the new content passed validation. Likewise, the solution preamble referring to review provenance in the structured bank is unsupported for papers absent from that bank.

## Recommended disposition

- Preserve Mock 001 and its prior review evidence; see its separate current-file audit when available.
- Treat Mock 002 separately: it contains varied authored work, but review concerns and draft/current-file differences must be resolved. Do not apply unpublished draft corrections silently.
- Classify Mock 003–100 as **FAIL — substantial redesign required**. Fixing answer letters alone cannot repair their repetition, difficulty or topic coverage.
- Reuse only sound individual questions, once each, after fixing their specific format and solution issues. Rebuild the remaining slots around genuinely distinct reasoning tasks and actual syllabus coverage.

This audit does not generate replacement papers or alter the examination content. Detailed per-paper counts follow below.

## Paper-by-paper results

The Easy/Medium/U columns apply to the intended task families in Mock 003–100; U means the family itself is ungradable. Additional invalid instances are counted in the findings column. Duplicate excess counts repeated stems within that paper. Mathematics marks are verified from solution subject labels only, not from the accuracy of their subtopic claims.

| Mock | Questions / marks | Duplicate excess | Nonnumeric NAT | Flagged occurrences | Easy / Medium / U | Disposition |
|---|---|---:|---:|---:|---|---|
| 001 | 65 / 100 | 0 | 0 | Separate review | Separate review | Prior accepted; see current audit |
| 002 | 65 / 100 | 0 | 0 | Separate review | Separate review | REVIEW REQUIRED |
| 003 | 65 / 100 | 30 | 12 | 34 | 49 / 13 / 3 | FAIL |
| 004 | 65 / 100 | 27 | 13 | 37 | 47 / 13 / 5 | FAIL |
| 005 | 65 / 100 | 31 | 11 | 37 | 48 / 12 / 5 | FAIL |
| 006 | 65 / 100 | 26 | 13 | 33 | 43 / 19 / 3 | FAIL |
| 007 | 65 / 100 | 34 | 16 | 43 | 52 / 8 / 5 | FAIL |
| 008 | 65 / 100 | 25 | 12 | 33 | 42 / 18 / 5 | FAIL |
| 009 | 65 / 100 | 27 | 13 | 39 | 49 / 12 / 4 | FAIL |
| 010 | 65 / 100 | 32 | 13 | 35 | 46 / 15 / 4 | FAIL |
| 011 | 65 / 100 | 25 | 10 | 35 | 47 / 13 / 5 | FAIL |
| 012 | 65 / 100 | 34 | 11 | 30 | 50 / 11 / 4 | FAIL |
| 013 | 65 / 100 | 25 | 14 | 30 | 44 / 17 / 4 | FAIL |
| 014 | 65 / 100 | 31 | 15 | 36 | 49 / 12 / 4 | FAIL |
| 015 | 65 / 100 | 25 | 8 | 32 | 44 / 15 / 6 | FAIL |
| 016 | 65 / 100 | 32 | 6 | 34 | 50 / 11 / 4 | FAIL |
| 017 | 65 / 100 | 25 | 13 | 36 | 44 / 17 / 4 | FAIL |
| 018 | 65 / 100 | 29 | 12 | 34 | 49 / 13 / 3 | FAIL |
| 019 | 65 / 100 | 28 | 6 | 31 | 47 / 13 / 5 | FAIL |
| 020 | 65 / 100 | 27 | 10 | 29 | 44 / 16 / 5 | FAIL |
| 021 | 65 / 100 | 31 | 9 | 31 | 51 / 11 / 3 | FAIL |
| 022 | 65 / 100 | 26 | 10 | 33 | 43 / 16 / 6 | FAIL |
| 023 | 65 / 100 | 32 | 7 | 35 | 50 / 10 / 5 | FAIL |
| 024 | 65 / 100 | 28 | 11 | 32 | 45 / 16 / 4 | FAIL |
| 025 | 65 / 100 | 25 | 9 | 35 | 48 / 15 / 2 | FAIL |
| 026 | 65 / 100 | 31 | 9 | 35 | 47 / 12 / 6 | FAIL |
| 027 | 65 / 100 | 26 | 10 | 35 | 46 / 14 / 5 | FAIL |
| 028 | 65 / 100 | 29 | 4 | 34 | 47 / 13 / 5 | FAIL |
| 029 | 65 / 100 | 27 | 6 | 30 | 46 / 16 / 3 | FAIL |
| 030 | 65 / 100 | 28 | 9 | 36 | 49 / 11 / 5 | FAIL |
| 031 | 65 / 100 | 29 | 5 | 32 | 44 / 17 / 4 | FAIL |
| 032 | 65 / 100 | 30 | 8 | 32 | 51 / 10 / 4 | FAIL |
| 033 | 65 / 100 | 29 | 6 | 26 | 44 / 17 / 4 | FAIL |
| 034 | 65 / 100 | 29 | 12 | 37 | 48 / 12 / 5 | FAIL |
| 035 | 65 / 100 | 31 | 15 | 40 | 48 / 12 / 5 | FAIL |
| 036 | 65 / 100 | 29 | 9 | 32 | 45 / 18 / 2 | FAIL |
| 037 | 65 / 100 | 30 | 7 | 30 | 46 / 13 / 6 | FAIL |
| 038 | 65 / 100 | 31 | 3 | 26 | 48 / 12 / 5 | FAIL |
| 039 | 65 / 100 | 26 | 9 | 29 | 47 / 15 / 3 | FAIL |
| 040 | 65 / 100 | 34 | 11 | 37 | 49 / 12 / 4 | FAIL |
| 041 | 65 / 100 | 26 | 9 | 33 | 45 / 14 / 6 | FAIL |
| 042 | 65 / 100 | 32 | 7 | 31 | 48 / 12 / 5 | FAIL |
| 043 | 65 / 100 | 25 | 14 | 37 | 45 / 17 / 3 | FAIL |
| 044 | 65 / 100 | 31 | 13 | 40 | 49 / 12 / 4 | FAIL |
| 045 | 65 / 100 | 25 | 11 | 35 | 44 / 16 / 5 | FAIL |
| 046 | 65 / 100 | 32 | 7 | 33 | 51 / 9 / 5 | FAIL |
| 047 | 65 / 100 | 28 | 9 | 33 | 44 / 19 / 2 | FAIL |
| 048 | 65 / 100 | 30 | 11 | 37 | 49 / 10 / 6 | FAIL |
| 049 | 65 / 100 | 30 | 9 | 31 | 46 / 14 / 5 | FAIL |
| 050 | 65 / 100 | 24 | 11 | 35 | 44 / 17 / 4 | FAIL |
| 051 | 65 / 100 | 31 | 5 | 30 | 52 / 10 / 3 | FAIL |
| 052 | 65 / 100 | 27 | 10 | 43 | 44 / 16 / 5 | FAIL |
| 053 | 65 / 100 | 30 | 10 | 30 | 48 / 12 / 5 | FAIL |
| 054 | 65 / 100 | 28 | 15 | 39 | 46 / 15 / 4 | FAIL |
| 055 | 65 / 100 | 30 | 7 | 34 | 47 / 14 / 4 | FAIL |
| 056 | 65 / 100 | 27 | 12 | 38 | 46 / 13 / 6 | FAIL |
| 057 | 65 / 100 | 30 | 9 | 36 | 47 / 15 / 3 | FAIL |
| 058 | 65 / 100 | 28 | 8 | 34 | 48 / 13 / 4 | FAIL |
| 059 | 65 / 100 | 29 | 11 | 37 | 46 / 14 / 5 | FAIL |
| 060 | 65 / 100 | 28 | 7 | 35 | 47 / 13 / 5 | FAIL |
| 061 | 65 / 100 | 30 | 10 | 29 | 47 / 14 / 4 | FAIL |
| 062 | 65 / 100 | 27 | 12 | 33 | 48 / 14 / 3 | FAIL |
| 063 | 65 / 100 | 32 | 10 | 35 | 47 / 13 / 5 | FAIL |
| 064 | 65 / 100 | 26 | 7 | 35 | 45 / 15 / 5 | FAIL |
| 065 | 65 / 100 | 30 | 10 | 32 | 49 / 12 / 4 | FAIL |
| 066 | 65 / 100 | 26 | 14 | 39 | 45 / 17 / 3 | FAIL |
| 067 | 65 / 100 | 27 | 10 | 37 | 48 / 11 / 6 | FAIL |
| 068 | 65 / 100 | 30 | 9 | 32 | 47 / 14 / 4 | FAIL |
| 069 | 65 / 100 | 26 | 12 | 45 | 47 / 13 / 5 | FAIL |
| 070 | 65 / 100 | 27 | 12 | 34 | 45 / 17 / 3 | FAIL |
| 071 | 65 / 100 | 30 | 10 | 34 | 50 / 9 / 6 | FAIL |
| 072 | 65 / 100 | 29 | 7 | 26 | 47 / 15 / 3 | FAIL |
| 073 | 65 / 100 | 27 | 8 | 37 | 44 / 16 / 5 | FAIL |
| 074 | 65 / 100 | 30 | 13 | 34 | 49 / 12 / 4 | FAIL |
| 075 | 65 / 100 | 29 | 7 | 36 | 46 / 14 / 5 | FAIL |
| 076 | 65 / 100 | 27 | 14 | 37 | 48 / 13 / 4 | FAIL |
| 077 | 65 / 100 | 30 | 14 | 38 | 47 / 14 / 4 | FAIL |
| 078 | 65 / 100 | 26 | 8 | 30 | 46 / 14 / 5 | FAIL |
| 079 | 65 / 100 | 34 | 7 | 35 | 50 / 11 / 4 | FAIL |
| 080 | 65 / 100 | 26 | 12 | 34 | 43 / 18 / 4 | FAIL |
| 081 | 65 / 100 | 29 | 10 | 34 | 48 / 13 / 4 | FAIL |
| 082 | 65 / 100 | 28 | 7 | 36 | 44 / 15 / 6 | FAIL |
| 083 | 65 / 100 | 29 | 9 | 35 | 50 / 11 / 4 | FAIL |
| 084 | 65 / 100 | 28 | 10 | 29 | 46 / 16 / 3 | FAIL |
| 085 | 65 / 100 | 30 | 8 | 35 | 49 / 11 / 5 | FAIL |
| 086 | 65 / 100 | 29 | 5 | 35 | 45 / 14 / 6 | FAIL |
| 087 | 65 / 100 | 31 | 13 | 34 | 49 / 13 / 3 | FAIL |
| 088 | 65 / 100 | 27 | 6 | 28 | 46 / 15 / 4 | FAIL |
| 089 | 65 / 100 | 29 | 9 | 38 | 44 / 16 / 5 | FAIL |
| 090 | 65 / 100 | 29 | 9 | 33 | 50 / 10 / 5 | FAIL |
| 091 | 65 / 100 | 29 | 10 | 36 | 45 / 16 / 4 | FAIL |
| 092 | 65 / 100 | 26 | 12 | 36 | 48 / 14 / 3 | FAIL |
| 093 | 65 / 100 | 31 | 7 | 30 | 50 / 10 / 5 | FAIL |
| 094 | 65 / 100 | 27 | 6 | 33 | 44 / 17 / 4 | FAIL |
| 095 | 65 / 100 | 29 | 13 | 38 | 47 / 14 / 4 | FAIL |
| 096 | 65 / 100 | 30 | 9 | 41 | 47 / 13 / 5 | FAIL |
| 097 | 65 / 100 | 27 | 11 | 36 | 46 / 14 / 5 | FAIL |
| 098 | 65 / 100 | 30 | 9 | 29 | 47 / 14 / 4 | FAIL |
| 099 | 65 / 100 | 27 | 9 | 30 | 48 / 14 / 3 | FAIL |
| 100 | 65 / 100 | 32 | 13 | 34 | 46 / 14 / 5 | FAIL |
