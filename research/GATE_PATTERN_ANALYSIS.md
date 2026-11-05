# GATE CS historical pattern analysis

Research date: 12 October 2026. Status: **sample-based analysis, with explicitly incomplete older-year review**. No historical question is licensed here as a reusable mock question. This document describes design evidence, not a claim that all historical questions were solved.

## Evidence and scope

The official [IIT Guwahati archive](https://gate2026.iitg.ac.in/download.html) and [2026 master-paper page](https://gate2026.iitg.ac.in/QPs-answer-keys.html) were opened. Local PDFs and text extractions are retained under `historical/`; `HISTORICAL_SOURCES.md` records actual reading scope. Recent samples cover 2021–2026. Most of the 2015–2018 papers could not be read fully because the alternate official IIT Kanpur host failed DNS/HTTP retrieval. No exhaustive historical subject-weight calculation has been performed.

## Official rules versus series choices

The 2026 master-paper page specifies a single correct MCQ choice, penalties of one-third/two-thirds for incorrect one/two-mark MCQs, all-or-nothing MSQ scoring without negative marks, and NAT acceptance within the published range without negative marks. It warns that console question and option order can differ from the master paper. These are historical official rules; 2027 confirmation belongs to `SYLLABUS_2027.md` and the 2027 sources.

The requested fixed numbering, five one-mark plus four two-mark mathematics questions, 40/45/15 difficulty allocation, and minimum proportion of multi-step technical tasks are **mock-series design constraints**. They are not inferred official quotas. The stricter series requirement that an MSQ contain multiple correct choices is also a design restriction: actual 2026 CS1 MSQ keys include singleton correct sets.

## Measured type counts

Counts include all 10 GA questions. The six programmatically counted keys each contain 65 parsed rows summing to 100 marks; the script and outputs are `historical/count_types.py` and `historical/type_counts.json`. The 2025 CS1 count was read directly from its key because its PDF text ordering did not pass the same row parser.

| Official paper | MCQ | MSQ | NAT | Measurement |
|---|---:|---:|---:|---|
| 2022 CS | 32 | 15 | 18 | Complete key parsed |
| 2023 CS | 34 | 15 | 16 | Complete key parsed |
| 2024 CS1 | 29 | 20 | 16 | Complete key parsed |
| 2024 CS2 | 32 | 18 | 15 | Complete key parsed |
| 2025 CS1 | 30 | 13 | 22 | Complete key read and counted |
| 2026 CS1 | 28 | 24 | 13 | Complete key parsed |
| 2026 CS2 | 35 | 11 | 19 | Complete key parsed |

These are observations, not future predictions. In particular, variation between the two 2026 sessions argues against prescribing identical type counts in every mock. Source links for every key are in the companion source ledger.

## Qualitative style findings from inspected samples

### General Aptitude

The inspected 2025 CS1 opening section spans articles, vocabulary in context, corrected-average arithmetic, constrained family deductions, map directions, reading comprehension, plane geometry, elementary probability, paper folding, and combinations with repetition. This supports including all four aptitude areas without treating GA as advanced engineering mathematics. The 2024 CS1 folding and symmetry samples emphasize transformation rules and careful interpretation. The 2026 CS1 samples combine piecewise-function interpretation, ordering constraints, and finite sample-space probability. These observations are based on samples, not calibrated difficulty ratings. [2025 CS1](https://gate2026.iitg.ac.in/doc/download/2025/CS12025.pdf), [2024 CS1](https://gate2026.iitg.ac.in/doc/download/2024/CS124S5.pdf), [2026 CS1](https://gate2026.iitg.ac.in/doc/download/2026/QPs/CS1.pdf).

### One-mark depth

2025 CS1 mixes compact concept checks with reasoning about function composition, graph properties, grammar languages, and state transitions. A short stem does not imply recall alone. 2024 CS1 samples require distinguishing representable integer range, probabilistic independence, and I/O mechanisms. 2026 CS1 samples include conditional probability after state-changing draws and counting under parity constraints. Accordingly, one-mark mocks should often require one decisive inference, occasionally two short steps, with limited arithmetic. Some official one-mark items are easier than this project's requested medium-to-hard target; that target should be disclosed as a deliberate training choice.

### Two-mark depth

The inspected 2025 CS1 late questions combine execution tracing, insertion order, or a structural graph condition with a requested numerical result. In 2026 CS1, constrained BST insertion, bounded-length shortest-path assertions, tuple-calculus translation and communication timing require building an intermediate model before answering. Earlier samples show similar depth: 2019 technical Q32–35 combine dependency analysis, translation coverage, language-set cardinality and quantified statements; 2020 technical Q32–34 require language classification, attribute dependencies and semaphore behavior. These are qualitative observations, not a claim that every two-mark question is harder than every one-mark question. [2019 CS](https://gate2026.iitg.ac.in/doc/download/2019/cs_2019.pdf), [2020 CS](https://gate2026.iitg.ac.in/doc/download/2020/cs_2020.pdf).

### MCQ distractors

Distractors in the inspected samples distinguish necessary from sufficient conditions, an existential example from a universal claim, a layer's role from a neighboring layer's role, and a plausible intermediate result from the required final result. Mocks should use mathematically meaningful alternatives and state domain, conventions and boundary conditions. Merely changing the historical numbers or option order would not create a new reasoning task.

### MSQ design

2022 samples independently test language closure, write policies, relational division and deadlock conditions; 2023 samples distinguish per-thread context from per-process state, guaranteed kernel transitions from ordinary calls, and language-class closure. This is stronger than repeating four equivalent definitions. Each option requires its own proof or counterexample. Official MSQ keys can contain a single selected option; a mock restriction to two or more must be labelled internal. [2022 CS](https://gate2026.iitg.ac.in/doc/download/2022/cs_2022.pdf), [2023 CS](https://gate2026.iitg.ac.in/doc/download/2023/cs_2023.pdf).

### NAT design

NATs vary from integer state counts to decimal-valued calculations. Keys distinguish singleton ranges from tolerance intervals; presentation precision and acceptance bounds must be explicit. A numerical answer alone does not demonstrate computational depth. For mocks, retain an exact intermediate representation where possible, round only at the stated final step, and verify the acceptance interval independently. The [2023 official key](https://gate2026.iitg.ac.in/doc/download/Answer_keys2023/CS_ANS_GATE2023.pdf) also contains exceptional accepted alternatives and marks-to-all cases. These justify strong ambiguity checks, not reproducing such ambiguities in practice papers.

### Historical continuity and limits

The visually inspected 2021 Set1 samples include regular/context-free closure, comparison bounds, syntax-directed typing and DFA selection. They demonstrate the continuing importance of definitions used in context and of testing candidate constructions. [2021 combined CS PDF](https://gate2026.iitg.ac.in/doc/download/2021/cs_2021.pdf).

The 2015 indexed official excerpt confirms the familiar 65-question, 100-mark and 15-mark GA structure; its two visible verbal questions were only a small search excerpt, not a full-paper review. Indexed 2016/2018 key excerpts show NAT ranges but do not support subject-distribution conclusions. No 2017 CS questions were successfully read. These limitations remain open research work.

## Blueprint implications and review rubric

1. Vary type counts across papers while maintaining the requested marks and numbering.
2. Represent all nine core subjects; use a rotating topic plan rather than an unsupported claim about historical exact weights.
3. Make at least 28 of the 55 technical tasks require two meaningful steps. Record the steps in internal metadata; a difficulty label alone is insufficient evidence.
4. Assign provisional difficulty using operations and likely time: medium generally one central inference plus execution; medium-hard couples constraints or representations; hard demands a non-obvious invariant, counterexample, or extended derivation. This is an editorial rubric, not empirical candidate calibration.
5. Audit each choice independently, check edge cases, and separate model review from programmatic evidence. Never call automated review human review.
6. Track coverage at subtopic level. No numerical historical subject ranking is warranted by this partial sample.

## Remaining research work

Retrieve/read 2015–2018 full CS papers and all uninspected sessions; expand the 2021 visual review; inspect every diagram used for any specific inference; tag all historical questions consistently if quantitative subject-frequency estimates are desired. Current sample analysis must not be presented as a complete 2015–2026 census.


## Supplemental 2018 sample evidence

The follow-up retrieval obtained the official 2018 CS paper through the IIT Bombay archive; the access ledger records the precise sample. Inspected technical one-mark tasks include generating functions, C memory interpretation, a queue whose operations are deliberately assigned to different list ends, automata-size bounds, closure and compiler phases. Selected two-mark tasks combine nested integer reductions, representability constraints, cache-field algebra, language classification, undecidability and maximal-munch tokenization. This supports designing distractors around violated conditions and intermediate reasoning, while preserving exact units, integer conventions and model assumptions. This is qualitative evidence only, not a new subject-weight census. [Officially linked 2018 PDF](https://drive.google.com/file/d/1CboGjdOkvPzijQk8IXzsE6LdJst-xv9M/view).

The opening historical-status statement above refers to the initial pass. Following this update, 2018 full source is locally available and partially studied; 2015-2017 remain incompletely accessed. No claim of full review is made for 2018.
