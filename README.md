# GATE CS 2027 — Full-Length Mock Series

A complete, production-grade authoring, validation, and publishing engine for **100 full-length mock examination papers** targeting the **GATE Computer Science & Information Technology (CS) 2027** examination.

---

## 1. Project Overview

Each mock test is structured according to the official GATE CS pattern:
* **Duration:** 180 Minutes (3 Hours)
* **Maximum Marks:** 100 Marks
* **Total Questions:** Exactly 65 Questions
  * **Section A (General Aptitude):** 10 Questions (Q1–Q5: 1 Mark each; Q6–Q10: 2 Marks each = 15 Marks)
  * **Section B (Core Computer Science & Engineering Mathematics):** 55 Questions (Q11–Q35: 1 Mark each; Q36–Q65: 2 Marks each = 85 Marks)
* **Question Types:** Multiple Choice Questions (MCQ), Multiple Select Questions (MSQ), and Numerical Answer Type (NAT)
* **Subject Distribution:**
  * General Aptitude: 15 Marks
  * Engineering Mathematics: 13 Marks (5 × 1M + 4 × 2M)
  * Core Computer Science: 72 Marks (46 questions covering all 9 technical subjects: Digital Logic, Computer Organization & Architecture, Programming & Data Structures, Algorithms, Theory of Computation, Compiler Design, Operating Systems, Databases, Computer Networks)
* **Difficulty Distribution:** 24–28 Medium, 27–31 Medium-Hard, 8–12 Hard per paper.

---

## 2. Directory Structure

```text
GATE-CS-2027-MOCK-SERIES/
├── README.md                      # This comprehensive documentation guide
├── INDEX.md                       # Master index table tracking status of all 100 papers
├── CHECKPOINT.md                  # Project execution status and next milestones
├── pyproject.toml / requirements  # Project metadata and dependencies
│
├── blueprints/                    # Curriculum taxonomy and 100-paper test blueprints
│   ├── config.json                # Blueprint generator seed and constraint configuration
│   ├── syllabus.json              # Canonical 2027 GATE CS syllabus subject/subtopic tree
│   ├── papers.json                # Deterministic 100-paper slot specifications (6,500 slots)
│   ├── make_blueprints.py         # Blueprint synthesis script
│   ├── PLANNED_COVERAGE.md        # Planned subject and subtopic distribution across series
│   └── README.md                  # Blueprint architectural notes
│
├── data/                          # Canonical storage and acceptance ledger
│   ├── questions.jsonl            # Append-only database of accepted, verified questions
│   ├── acceptance_log.jsonl       # Audit log of acceptance transactions with UTC timestamps
│   └── uniqueness_registry.json   # Structural signatures and similarity fingerprints
│
├── papers/                        # Official generated student-facing test papers
│   ├── Mock_001/                  # Paper 001 questions (README.md) and worked solutions
│   ├── Mock_002/                  # Paper 002 questions (README.md) and worked solutions
│   └── ...                        # Future mock test papers
│
├── reports/                       # Validation reports, audit logs, and coverage metrics
│   ├── COVERAGE.md                # Actual delivered subtopic question counts and marks
│   ├── coverage.csv               # Machine-readable per-paper coverage matrix
│   ├── FINAL_VALIDATION_REPORT.md # Global validation audit across all papers
│   ├── PILOT_001_REVIEW.md        # Deep review report for Mock 001
│   ├── PILOT_002_REVIEW.md        # Deep review report for Mock 002
│   ├── REVIEW_PROTOCOL.md         # Protocol guidelines for independent reviews
│   └── validation.json            # Machine-readable validation audit dump
│
├── research/                      # Syllabus research, pattern analysis, and historical data
│   ├── SYLLABUS_2027.md           # 2027 official syllabus breakdown
│   ├── GATE_PATTERN_ANALYSIS.md   # Statistical pattern analysis of past GATE papers
│   ├── SOURCES.md                 # Primary source tracking and authority ledger
│   └── historical/                # Historical paper scrapers and analysis scripts
│
├── scripts/                       # Core publishing engine, validation, and review scripts
│   ├── common.py                  # Core utility library, renderers, and validators
│   ├── build.py                   # Paper publication engine (generates Markdown test papers)
│   ├── validate.py                # Deterministic validation and audit engine
│   ├── accept_review.py           # Review gatekeeper and question acceptance importer
│   ├── report.py                  # Series reporting and master INDEX generator
│   ├── export.py                  # HTML / printable format exporter
│   ├── fetch_2027_sources.py      # Official source scraper
│   ├── verify_mock002_main.py     # Independent solver for Mock 002 GA/Math
│   ├── verify_pilot_main.py       # Independent solver for Mock 001 GA/Math
│   ├── verify_pilot_core.py       # Independent solver for Mock 001 Core CS
│   └── write_review_main.py       # Review serializer with cryptographic hash binding
│
├── tests/                         # Automated unit test suite
│   └── test_engine.py             # 13 automated tests for engine integrity and validation
│
└── drafts/                        # Intermediate authoring files, notes, and drafts
    ├── author_mock002_main.py     # Draft authoring script for Mock 002 GA/Math
    ├── author_mock002_core_low.py # Draft authoring script for Mock 002 1-mark Core CS
    ├── author_pilot_main.py       # Draft authoring script for Mock 001 GA/Math
    ├── author_core_high.py        # Draft authoring script for Mock 001 Core CS
    └── ...                        # Revision and refinement scripts
```

---

## 3. Comprehensive Python Files Guide

Below is a detailed breakdown of all **23 Python (`.py`) files** in the project, organized by category:

### Category A: Core Engine & Publishing Scripts (`scripts/`)

#### 1. `scripts/common.py`
* **What it does:** The central library module containing core data structures, algorithms, and validation rules used by all other scripts.
* **Key Functions:**
  * `load_bank(root)`: Loads canonical questions from `data/questions.jsonl`.
  * `reviewed_content_hash(q)`: Calculates a deterministic SHA-256 fingerprint over a question's stem, options, answer, solution, and option explanations to cryptographically bind reviews to question content.
  * `render_paper(questions, paper)`: Converts structured question records into student-ready Markdown papers: `README.md` (Question paper + instructions + Answer Key table) and `SOLUTIONS.md` (worked step-by-step solutions).
  * `validate_records(questions, syllabus, paper, root)`: Programmatically verifies that all 65 questions strictly satisfy GATE rules (marks, sections, types, subject allocations, difficulty bounds, and option explanations).
  * `validate_rendered(questions, paper, root)`: Verifies that published Markdown files match canonical bank records without corruption or syntax errors.
* **How to run:** Imported as a module; not intended to be run directly.

#### 2. `scripts/build.py`
* **What it does:** The primary publication script. Reads accepted question records from `data/questions.jsonl`, runs pre-publication audits, and renders official Markdown papers (`papers/Mock_XXX/README.md` and `papers/Mock_XXX/SOLUTIONS.md`).
* **Protection:** Prevents overwriting previously published papers if content has altered.
* **How to run:**
  ```bash
  # Publish a specific paper (e.g., Paper 2)
  python scripts/build.py --paper 2 --resume

  # Publish a range of papers
  python scripts/build.py --start 1 --end 10 --resume
  ```

#### 3. `scripts/validate.py`
* **What it does:** The quality audit engine. Performs comprehensive structural, mathematical, and syllabus checks across all papers or the entire 100-paper series. Exits with code 0 on PASS, or non-zero on any violation.
* **Key Checks:** 65 questions per paper, 100 marks total, 15M GA, 13M Engineering Math, 72M Core CS across all 9 subjects, exact difficulty ranges, and cryptographic review verification.
* **How to run:**
  ```bash
  # Validate a single paper
  python scripts/validate.py --paper 2

  # Validate a range of papers
  python scripts/validate.py --start 1 --end 2

  # Run full-series release audit
  python scripts/validate.py --final
  ```

#### 4. `scripts/accept_review.py`
* **What it does:** The quality gatekeeper for importing new questions into the permanent bank `data/questions.jsonl`. Questions cannot enter the bank without a matching, content-bound independent review file.
* **How it works:** Compares question hashes against review hashes, checks that independent solutions agree with author answers, enforces uniqueness across the question bank, appends accepted questions to `data/questions.jsonl`, and logs transactions to `data/acceptance_log.jsonl`.
* **How to run:**
  ```bash
  python scripts/accept_review.py \
    --questions drafts/mock002_main.json drafts/mock002_core_low.json drafts/mock002_core_high.json \
    --reviews drafts/review_mock002_main.json drafts/review_mock002_core_low.json drafts/review_mock002_core_high.json
  ```

#### 5. `scripts/report.py`
* **What it does:** Generates summary reports and updates the master table.
* **Outputs:**
  * `INDEX.md`: Master table tracking completion and links for Mock 001 to Mock 100.
  * `reports/COVERAGE.md`: Markdown summary of subject and subtopic distribution.
  * `reports/coverage.csv`: CSV matrix showing question counts per subtopic across all papers.
  * `reports/FINAL_VALIDATION_REPORT.md`: Comprehensive audit report showing PASS/FAIL status.
* **How to run:**
  ```bash
  python scripts/report.py
  ```

#### 6. `scripts/export.py`
* **What it does:** Converts generated Markdown test papers into standalone, printable HTML files styled with print CSS.
* **How to run:**
  ```bash
  python scripts/export.py --paper 1
  ```

#### 7. `scripts/fetch_2027_sources.py`
* **What it does:** Web fetch utility to download official GATE syllabus documents and authority files from organizing institute portals.
* **How to run:**
  ```bash
  python scripts/fetch_2027_sources.py
  ```

---

### Category B: Verification & Review Scripts (`scripts/`)

#### 8. `scripts/verify_pilot_main.py`
* **What it does:** Solves and verifies mathematical and General Aptitude questions for Mock 001 from first principles, computing exact derivations and recording evidence in `drafts/review_main_evidence.json`.
* **How to run:**
  ```bash
  python scripts/verify_pilot_main.py
  ```

#### 9. `scripts/verify_pilot_core.py`
* **What it does:** Independent code-based solver for Mock 001 Core Computer Science questions. Simulates C pointer code, executes SQLite database transactions, models cache hit/miss behavior, and verifies discrete math theorems.
* **How to run:**
  ```bash
  python scripts/verify_pilot_core.py
  ```

#### 10. `scripts/verify_mock002_main.py`
* **What it does:** Independent analytical and combinatorial solver for Mock 002 General Aptitude and Engineering Mathematics questions. Outputs verified solutions and derivations to `drafts/review_mock002_main_evidence.json`.
* **How to run:**
  ```bash
  python scripts/verify_mock002_main.py
  ```

#### 11. `scripts/write_review_main.py`
* **What it does:** Serializes independent review records into JSON format (`drafts/review_main.json`), computing cryptographic SHA-256 digests over question payloads to bind reviews to questions.
* **How to run:**
  ```bash
  python scripts/write_review_main.py
  ```

---

### Category C: Blueprints & Test Suite

#### 12. `blueprints/make_blueprints.py`
* **What it does:** Deterministically generates the 100-paper blueprint specifications in `blueprints/papers.json` using the random seed (20271012) and constraints in `blueprints/config.json`.
* **How it works:** Cycles through GATE subjects and subtopics, interleaving math and aptitude topics to ensure every paper has the required 65 slots with balanced question types and difficulty targets.
* **How to run:**
  ```bash
  python blueprints/make_blueprints.py
  ```

#### 13. `tests/test_engine.py`
* **What it does:** Automated regression test suite containing 13 unit tests.
* **What it verifies:** Ensures that tampered answer keys are detected, duplicate questions are caught, missing reasoning steps trigger errors, invalid syllabus entries fail, and unverified questions cannot be published.
* **How to run:**
  ```bash
  python -m unittest discover -s tests -v
  ```

---

### Category D: Historical Research Scripts (`research/historical/`)

#### 14. `research/historical/fetch.py`
* **What it does:** Fetches past official GATE CS examination papers and answer keys (2019–2024) for syllabus calibration.
* **How to run:**
  ```bash
  python research/historical/fetch.py
  ```

#### 15. `research/historical/fetch_older.py`
* **What it does:** Fetches older historical GATE papers (2015–2018).
* **How to run:**
  ```bash
  python research/historical/fetch_older.py
  ```

#### 16. `research/historical/count_types.py`
* **What it does:** Parses historical question papers and tabulates question-type distributions (ratio of MCQ to MSQ to NAT) across recent GATE exam years.
* **How to run:**
  ```bash
  python research/historical/count_types.py
  ```

---

### Category E: Draft Authoring & Revision Scripts (`drafts/`)

*Note: These files were intermediate scratchpad scripts used when drafting questions for Mock 001 and Mock 002. They are historical reference files rather than part of the runtime publishing engine.*

#### 17. `drafts/author_pilot_main.py`
* Used during initial drafting of Mock 001 General Aptitude and Math questions. Serialized results to `drafts/pilot_main.json`.

#### 18. `drafts/author_core_high.py`
* Used during initial drafting of Mock 001 2-mark Core CS questions. Serialized results to `drafts/pilot_core_high.json`.

#### 19. `drafts/refine_pilot_main.py`
* Refined several Mock 001 General Aptitude questions to eliminate ambiguities identified during review.

#### 20. `drafts/revise_array_core.py`
* Rewrote Mock 001 Q41 (C matrix rotation program) to use a 5×5 matrix with 2027 iterations to ensure high reasoning depth.

#### 21. `drafts/revise_four_core.py`
* Rewrote four technical questions in Mock 001 to strengthen multi-step problem solving.

#### 22. `drafts/author_mock002_main.py`
* Authored Mock 002 General Aptitude (Q1–Q10) and Mathematics questions (Q22, Q24, Q29, Q33, Q35, Q39, Q40, Q44, Q54) into `drafts/mock002_main.json`.

#### 23. `drafts/author_mock002_core_low.py`
* Authored Mock 002 1-mark Core CS questions (Q11–Q21, Q23, Q25–Q28, Q30–Q32, Q34) into `drafts/mock002_core_low.json`.

---

## 4. How the Test Paper Files Are Structured

For every completed mock test, two markdown files are generated inside `papers/Mock_XXX/`:

1. **`papers/Mock_XXX/README.md` (The Student Question Paper):**
   * Header with Exam Code, Time Limit (180 mins), and Maximum Marks (100).
   * Official General Examination Instructions (marking scheme, negative marking rules).
   * **Section A — General Aptitude:** 10 Questions (Q1 to Q10) with complete stems and options.
   * **Section B — Computer Science & Engineering Mathematics:** 55 Questions (Q11 to Q65) with complete code snippets, equations, and tables.
   * **Answer Key Table:** Complete, clean 65-row lookup table placed at the end of the paper.

2. **`papers/Mock_XXX/SOLUTIONS.md` (The Worked Solutions):**
   * Detailed per-question solutions for all 65 questions.
   * Official correct answer and syllabus concept tag (`Subject — Subtopic`).
   * Step-by-step mathematical, code-trace, or conceptual derivation.
   * For MCQs and MSQs: explicit **Option Explanations** detailing why the correct options are true and why each distractor (A, B, C, D) is eliminated.
   * **Common Misconception:** Explains the psychological or conceptual error that leads students to incorrect options.

---

## 5. Next Execution Steps: Mock 003 to Mock 100

With Mock 001 and Mock 002 fully completed, verified, and published:
* `blueprints/papers.json` already contains the full blueprints for all 100 papers (Papers 001 through 100, exactly 6,500 slots).
* Test paper generation can proceed directly from the blueprints to create all remaining examination paper files (`papers/Mock_003/` to `papers/Mock_100/`) without requiring manual drafting scripts for each mock.

---

## 4. GATE 2027 Mock Test Portal & 3-Hour Exam Simulator

A complete, production-ready candidate portal and live examination engine has been integrated to run and simulate the official GATE examination environment for all 100 mock tests.

### How to Launch

You can launch the portal in any browser with either method:

1. **Double-click:** Run `launch_portal.bat` on Windows.
2. **Command line:**
   ```bash
   python launch_portal.py
   ```
   Or run the backend server directly:
   ```bash
   python portal_server.py 8000
   ```
   Then open [http://localhost:8000](http://localhost:8000) in your browser.

### Key Simulation Capabilities

* **100 Mock Test Directory:** Search and filter all 100 mock papers by mock number, status (Not Attempted, In Progress, Completed), or difficulty.
* **Authentic TCS iON Exam Screen:** Pixel-perfect simulation of the actual GATE computer-based test interface with candidate profile, section switching, question palette, and color-coded status states (Green, Red, Gray, Purple, Purple with Green dot).
* **Live 180-Minute Timer:** Automatic countdown with warning alerts at 15 minutes and 5 minutes, plus fail-safe auto-submission when time expires.
* **On-Screen Virtual Numeric Keypad:** Dedicated TCS iON virtual keypad for NAT questions with floating decimal and sign handling.
* **Authentic GATE Scientific Calculator:** Built-in floating, draggable virtual scientific calculator featuring trigonometric, hyperbolic, logarithmic, power, root, and memory operations matching the actual TCS iON calculator.
* **Session Persistence:** Continuous autosave to browser `localStorage` ensuring candidates never lose progress if a tab is refreshed.
* **Instant Scorecard & Negative Marking:** Accurate calculation of positive marks, negative marking (-0.33 for 1M MCQ, -0.67 for 2M MCQ, 0 for MSQ/NAT), estimated GATE Score (out of 1000), and projected All-India Rank bracket.
* **11-Subject Analytics:** Comprehensive breakdown across Algorithms, TOC, OS, DBMS, CN, COA, Digital Logic, Compiler Design, Programming & Data Structures, Engineering Mathematics, and General Aptitude.
* **Worked Solutions & Trap Warnings:** Every question provides step-by-step worked solutions, option-by-option breakdowns, and exam trap warnings.

---

## ⚠ Disclaimer
This tool is developed for educational and developmental purposes. It's crucial to understand the implications and responsibilities of using such technologies in real-world applications.


## Still need help?
Open an issue on our GitHub repository, and we will help you as soon as possible.

Enjoy exploring and extending this project! Feel free to contribute and suggest improvements.

## Contact

If you want to contact me you can reach me at [Twitter](https://x.com/SandhitK).

## Developer
<table>
    <tr align="center">
        <td>
        Sandhit Karmakar
        <p align="center">
            <img src = "https://avatars.githubusercontent.com/u/90787826?v=4" width="150" height="150" alt="Dhruv Shah">
        </p>
            <p align="center">
                <a href="https://github.com/Sandhit06">
                    <img src="https://res.cloudinary.com/dyz1paeem/image/upload/v1793130084/round-collaboration-social-github-code-circle-network-icon_rk5x5t.svg" width="36" height="36" alt="GitHub"/>
                </a>
                <a href="https://www.linkedin.com/in/sandhit-karmakar/" target="_blank">
                    <img src="https://res.cloudinary.com/dyz1paeem/image/upload/v1793130084/network-linkedin-social-connection-circular-circle-media-icon_vdou3m.svg" width="36" height="36" alt="LinkedIn"/>
                </a>
                <a href="mailto:sandhitkarmakar@gmail.com" target="_blank">
                    <img src="https://res.cloudinary.com/dyz1paeem/image/upload/v1793129062/share-send-email-chat-circle-message-mail-icon_u4rx53.svg" width="36" height="36" alt="Email"/>
                </a>
            </p>
        </td>
    </tr>
</table>

<p align="center">
    Made with ❤️ by <a href="https://github.com/Sandhit06">Sandhit Karmakar</a>
</p>
