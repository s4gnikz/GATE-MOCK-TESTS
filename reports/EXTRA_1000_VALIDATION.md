# Additional 1,000 questions — validation

Status: all 1,000 adapted variants saved; structural and answer-transformation checks PASS. Full independent source-answer verification is not claimed.

- 20 sets × 50 questions; each has a final 50-row key and 50 worked solutions.
- 1,000 unique extra-bank IDs and normalized texts, based on 1,000 different source questions.
- The original 200 question-paper and solution files retain their SHA-256 hashes.
- Correctness of answer transformations was checked independently using truth-set bit masks and the rendered pair choices.
- Numbering, four distinct options, answer counts, saved key/solution agreement, final-key placement and code-fence balance passed.
- No new Python or generator script files were created. The main 6,500-record bank remains unchanged.

## What “unique” means for this addition

The user requested lightweight tweaks. These are adapted selection tasks, not 1,000 wholly original problems: the underlying situations, numerical inputs and reasoning are reused. Exact text and IDs differ, but semantic/problem-family uniqueness is deliberately not claimed. Existing source-answer and difficulty-review limitations apply. No human review occurred.

| Adaptation | Questions |
|---|---:|
| correct-pair | 354 |
| incorrect-answer-selection | 646 |

| Subject | Questions |
|---|---:|
| Algorithms | 89 |
| Compiler Design | 113 |
| Computer Networks | 75 |
| Computer Organization and Architecture | 51 |
| Databases | 99 |
| Digital Logic | 69 |
| Engineering Mathematics | 78 |
| General Aptitude | 152 |
| Operating Systems | 89 |
| Programming and Data Structures | 57 |
| Theory of Computation | 128 |

Canonical extra records and source mappings: data/extra_questions.jsonl. Machine-readable results: reports/EXTRA_1000_VALIDATION.json. When correcting a source answer, update its extra variant using the recorded adaptation rule; do not blindly copy the original answer letters into the new key.
 note: these standalone-set checks predate integration. All 1,000 variants now replace repeated occurrences inside the main papers; see INTEGRATED_1000_REPLACEMENTS.md for current status.
