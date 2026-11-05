# Mock-series design plan

The 100 plans in `papers.json` contain 6,500 **planned slots**, not questions. `make_blueprints.py` deterministically reconstructs the initial plan using the seed and settings in `config.json`. It does not create, permute or reuse question content.

Every plan has five 1-mark and five 2-mark GA slots, five 1-mark and four 2-mark mathematics slots, and twenty 1-mark and twenty-six 2-mark core slots. Technical subjects are shuffled only within their mark groups. Each core subject begins with two slots of each mark value; the remaining two one-mark and eight two-mark slots rotate across subjects. These weights are deliberate design choices, not estimated official subject quotas.

Mathematics cycles interleave discrete mathematics, linear algebra, calculus and probability. GA cycles interleave all four aptitude areas. Core subtopics rotate over the entire series. `PLANNED_COVERAGE.md` records the resulting planned topic totals; `reports/COVERAGE.md` must be used for actual content delivered.

Question type and difficulty at slot level are provisional editorial targets. Types may change when a sound question requires it. Final difficulty is assigned after solving, using the rubric in the research analysis; labels must not be forced to match quotas. A paper outside the configured bounds must be revised before release. Exact subject/marks counts remain mandatory.

Before generating a new batch, inspect the accepted bank's reasoning patterns and actual coverage, then choose genuinely distinct tasks for its slots. Replacing a question with new numerical constants is not an acceptable implementation of this plan. A revised paper may adjust subtopics within its subject to repair coverage, with the difference recorded in its review report.
