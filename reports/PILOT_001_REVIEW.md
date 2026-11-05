# Mock 001 pilot review

Status: **complete paper; accepted after separate model review and applicable programmatic checks**. No human review is claimed. This does not constitute completion of the 100-paper series.

| Check | Result |
|---|---|
| Questions / marks / duration | 65 / 100 / 180 minutes |
| GA | 10 questions, 15 marks |
| Engineering Mathematics | 5 one-mark + 4 two-mark questions, 13 marks |
| Core CS | 20 one-mark + 26 two-mark questions, 72 marks; all nine subjects represented |
| Type distribution | 30 MCQ, 13 MSQ, 22 NAT |
| Difficulty | 28 Medium, 27 Medium-Hard, 10 Hard; within configured bounds |
| Worked solutions and option explanations | Present for every question; every selection option addressed |
| Independent reviewer records | 65, bound to current content hashes |
| Duplicate candidates within accepted bank | 0 unresolved |
| Answer key | 65 entries, after Q65, generated from accepted records |
| Human review | None |

## Review changes

The first draft was not released. A malformed C string escape was repaired and the corrected program compiled. A network timing question gained an explicit immediate-transmission assumption. A distractor explanation was corrected. Several difficulty labels were lowered; deeper, distinct tasks replaced straightforward or overly familiar drafts. Revisions include predictive-parser conflicts, removal of corners under function composition, eigenstructure under a rank-one update, probability under a stopping rule, and a lattice with a missing union. Five core questions were also rewritten to improve reasoning depth.

All revised content was re-reviewed before import. `drafts/review_main.json` and `drafts/review_core_high.json` retain answer derivations, evidence, content digests, and honest review provenance. Some initial reviews saw the proposed answer; they are accurately described as separate reviewer re-derivations, not uniformly blinded reviews. The executable checks are `scripts/verify_pilot_main.py` and `scripts/verify_pilot_core.py`. They include exact arithmetic, finite enumeration, native GCC execution and SQLite tests where applicable. General statements also require the recorded mathematical proofs; finite tests alone do not prove them.

Difficulty remains an editorial estimate, without candidate timing trials. The 55 technical items were reviewed as multi-step tasks, although not every written solution line is itself a separate reasoning step. The configured minimum is 28.

## Rendering

Both Markdown documents were exported using a CommonMark parser with table support to local HTML. Headless Edge checks found 65 question/solution headings in each and no horizontal overflow at viewport widths 1000 and 420 pixels. No image resources are missing. Images of the opening paper, C question, answer-key transition and opening solutions were visually inspected: text, code indentation and tables are readable.

Evidence is in `reports/rendered/Mock_001/`. This is sampled visual inspection plus full DOM overflow/resource checks, not a claim that every possible Markdown viewer or PDF pagination has been tested. No PDF was produced. The HTML includes print styles and can be printed locally.

## Limits and next work

The bank currently has 65 accepted questions, so cross-paper uniqueness has not yet been tested against future content. Structural signatures and lexical checks do not prove originality against every external question bank. Embeddings are unavailable. Historical research covers samples from 2019–2026; full official 2015–2018 retrieval remains unresolved. The global final release is intentionally failed while those research requirements and the other 99 papers remain unfinished.
