# Technical content audit — Algorithms, Programming, TOC and Compiler Design

Audit date: 2026-10-13. Scope: Mock 003–100. This report audits current paper and solution Markdown, not the earlier generation claims. No papers were changed and no Python files were created. This is a model-based audit with independently derived answers, not human review. Inline PowerShell was used to extract and count records; correctness conclusions below come from reasoning about the actual questions.

## Verdict

**The audited content fails the requested originality, question-type, coverage and difficulty requirements.** Across these four subjects, 2,003 question placements reduce to only **12 distinct stems/reasoning tasks**, with **1,991 repeated placements beyond one instance per task**. These are exact stem repeats, not merely questions about the same concepts. Changing MCQ/MSQ/NAT or the question number does not create a distinct problem.

All 98 audited papers contain repeated families. In particular, the stack, DFA, local-optimization, merge-sort, TM-decidability and non-CFL families each occur in all 98 papers. All 1,000 MCQs and 415 MSQs in this scope have answer A. The 415 MSQs have only one intended correct option; that violates this project's requirement for multiple correct choices, without asserting that official GATE universally forbids a singleton MSQ answer set.

Of 588 NAT placements, **504 have nonnumeric keys**: 473 say `A (exact)` and 31 say `['A'] (exact)`. The other 84 have appropriate numerical keys: 56 DFA counts, 14 token counts, and 14 C outputs. Many defective NATs ask “which of the following” while omitting every option. A valid question cannot be recovered merely by replacing an answer letter with a number when the requested object is a language, set, asymptotic class, or optimization.

The 166 non-CFL placements have an additional defect: they specify alphabet {a,b}, but their intended answer uses c. The 110 MST solutions give a counterexample that violates their own distinct-weight premise. The 168 TM solutions incorrectly describe halting on the empty tape as a property of the accepted language covered by Rice's theorem.

## Inventory and honest difficulty assessment

Counts include malformed NAT variants; difficulty describes the underlying intended task **when correctly presented**, not an endorsement of malformed questions. “Easy” means recall or a very short mechanical trace, below the requested Medium floor. “Medium” is a conservative upper assessment for the routine constructions below; none justifies Medium-Hard or Hard. Repeating these same tasks across tests makes practice substantially less demanding after first exposure.

| Family | Actual task | Total | MCQ | MSQ | NAT | Papers | Intended-task difficulty |
|---|---|---:|---:|---:|---:|---:|---|
| T01 | One min-heap insertion | 167 | 68 | 33 | 66 | 78 | Easy |
| T02 | Tokenize x===y | 55 | 28 | 13 | 14 | 55 | Easy |
| T03 | Four-key stack permutation | 279 | 149 | 52 | 78 | 98 | Medium, lower end |
| T04 | Two C pointer offsets | 55 | 29 | 12 | 14 | 55 | Easy |
| T05 | FIRST set with indirect recursion | 55 | 29 | 15 | 11 | 55 | Medium, lower end |
| T06 | Named Master Theorem case | 56 | 24 | 16 | 16 | 56 | Medium, lower end |
| T07 | Suffix-011 DFA count | 167 | 80 | 31 | 56 | 98 | Medium |
| T08 | Name a local optimization | 390 | 182 | 89 | 119 | 98 | Easy |
| T09 | Distinct-weight MST versus shortest path | 110 | 58 | 21 | 31 | 66 | Medium |
| T10 | Recall merge-sort complexity | 335 | 178 | 69 | 88 | 98 | Easy |
| T11 | Recall TM undecidability | 168 | 92 | 33 | 43 | 98 | Easy |
| T12 | Recognize standard non-CFL | 166 | 83 | 31 | 52 | 98 | Invalid as stated; intended recall is Easy |
| Total | 12 tasks | 2003 | 1000 | 415 | 588 | 98 | No genuinely hard task identified |

There are 501 Algorithms, 500 Compiler Design, 501 Programming/Data Structures and 501 TOC placements according to the solution subject headings. Actual stems were also checked against all unique stems in Mock 003–100 to ensure another technical family was not hidden by a misleading subtopic label. Trailing Markdown separators were excluded from stem identity.

## Independent family reviews

### T01 — Min-heap insertion

Example: Mock 003 Q50 (NAT), Q52 (MCQ); Mock 007 Q58 (MSQ). Insert 7 at position 8 of [4,9,12,15,20,16,25]. It swaps with position 4's 15, then position 2's 9, and stops below root 4. **Answer 2**, option A. B=4 stops too soon; C=1 violates the comparison with 4; D=8 skips all sifting. No undefined convention affects this result. All **66 NAT keys incorrectly say A**, although the worked trace reaches 2. A two-swap textbook trace is not a hard two-mark problem. Counts: 69 one-mark, 98 two-mark placements.

### T02 — Lexical maximal munch

Example: Mock 004 Q38 (MCQ), Mock 006 Q21 (NAT). `x===y` tokenizes as `x`, `==`, `=`, `y`, giving **4**, option A. C and Java both have == and = but no === token. Whether this sequence is a syntactically valid expression is irrelevant to lexical tokenization. B=3 incorrectly merges ===; C=5 splits ==; D=6 is not even the number of characters. The 14 NAT paper keys and solution headers correctly say 4. The 13 MSQ variants still have a single correct answer. Counts: 24 one-mark, 31 two-mark placements.

### T03 — Stack permutation

Example: Mock 003 Q15 (MSQ), Q28 (NAT), Q29 (MCQ). After pushing 1,2,3 and popping 3, the stack has 2 above 1. Therefore 3,1,2,4 is impossible, **option A**. B is obtained by push 1,2; pop 2; push 3,4; pop 4,3,1. C follows immediate push-pop pairs; D pushes all then drains. All 78 NATs lose the output-permutation options and retain a nonnumeric A key, so they are unsolvable as numerical questions. The same task is falsely labelled Arrays, Graph representations, Linked lists, Recursion and Stacks and queues. Counts: 125 one-mark, 154 two-mark placements.

### T04 — C pointer arithmetic

Example: Mock 004 Q36 (MCQ), Mock 006 Q40 (NAT). p=arr+1, so p+2=arr+3; q=arr+4, so q-1=arr+3. Each dereference is 40 and the output is **80**, option A. Options 70,90,60 do not equal that sum. Both pointers and dereferences remain within the array, no object is modified, and argument evaluation order does not affect the result. This reasoning checks correctness without treating a successful run as proof of defined semantics. The 14 NAT keys and solution headers correctly say 80. Counts: 24 one-mark, 31 two-mark placements.

### T05 — FIRST set

Example: Mock 004 Q58 (MCQ), Mock 010 Q26 (NAT). S->Aa|b and A->c|Sd. No nonterminal is nullable. The least fixed point is FIRST(S)=FIRST(A)={b,c}. Direct derivations S=>b and S=>Aa=>ca witness both terminals; no rule can introduce a or d first. **A is correct**, B wrongly includes a, C wrongly includes d and loses b, D omits c. The 11 NATs ask for a set but prescribe a numerical response and key A: malformed. Counts: 25 one-mark, 30 two-mark placements.

### T06 — Recurrence

Example: Mock 003 Q31 (MCQ), Mock 013 Q59 (NAT). For n=2^k let U(k)=T(2^k)/4^k. The recurrence becomes U(k)=U(k-1)+k up to the fixed logarithm base. Summing gives U(k)=Theta(k^2), hence **Theta(n^2 log^2 n)**, option A. B loses a logarithm; C=n^3 and D=n^(5/2) both grow faster. The prompt itself names the applicable extended Master Theorem case, reducing the required inference. Its 16 NATs require a symbolic asymptotic class but supply a numeric format and key A. Counts: 24 one-mark, 32 two-mark placements.

### T07 — Minimal suffix DFA

Example: Mock 003 Q35/Q61 (NAT), Mock 004 Q46 (MCQ). A four-state DFA tracks longest suffix equal to one of epsilon,0,01,011. Its transitions on 0,1 are respectively (q1,q0), (q1,q2), (q1,q3), (q1,q0), with q3 accepting. Minimality: q3 is distinguished from the others by epsilon; q2 from q0/q1 by suffix 1; q1 from q0 by suffix 11. **4 states**, option A, so 3 is insufficient and 5 or 8 are not minimal. All 56 NAT answers are correct. This is a standard short DFA construction, not a hard problem. Counts: 72 one-mark, 95 two-mark placements.

### T08 — Local common-subexpression elimination

Example: Mock 003 Q23 (MCQ), Q27/Q40/Q46 (NAT), Q65 (MSQ). Intended answer **A**, local CSE: available pure expressions and intervening local definitions can be tracked within a basic block. The cross-unit recursive inlining, externally observed global elimination and polymorphic dispatch elimination in B,C,D require additional nonlocal information to justify their general application. The question is a classification recall item, not an actual dataflow calculation. Its solution should not imply that all expressions are safe to eliminate solely because they are in one block: aliasing, writes, calls and side effects still require sound treatment. All **119 NATs omit the choices and retain A**. Counts: 168 one-mark, 222 two-mark placements.

Coverage mislabelling is substantial: this one question is tagged Common subexpression elimination, Constant propagation, Intermediate code generation, Liveness analysis, Local optimization, Runtime environments, and Syntax-directed translation. It computes no liveness, performs no propagation, generates no intermediate code and traces no runtime environment.

### T09 — MST and shortest path

Example: Mock 004 Q23/Q34 (MCQ), Mock 006 Q15 (NAT), Mock 011 Q31 (MSQ). Distinct edge weights ensure a unique MST by the exchange argument. They do not make every shortest path part of it. A correct counterexample is a triangle with AB=2, BC=3, AC=4: the MST is AB+BC with total 5, while the shortest A-to-C path is the excluded direct edge of weight 4. Thus **only I, option A**; B,C,D are false.

Every family solution instead invokes a bypass of weights **2,3,4,3**, repeating weight 3 despite the distinct-weight condition. That is not a valid counterexample to the stated claim. The intended conclusion remains correct; the supporting example must be repaired. All **31 NATs key the literal list `['A']`** and omit the choice encoding, rather than asking a numerical question. Counts: 50 one-mark, 60 two-mark placements.

### T10 — Merge-sort recall

Example: Mock 003 Q17/Q43/Q51/Q64 (MCQ), Mock 004 Q42 (NAT). Ordinary merge sort has worst-case recurrence C(n)=2C(n/2)+(n-1) for powers of two. Solving gives n log2(n)-n+1 comparisons in that case and asymptotic **Theta(n log n)** generally, selecting A. Quadratic, linear and logarithmic alternatives B,C,D are not tight worst-case bounds. The stem asks a “number” but offers asymptotic classes; it should explicitly ask the tight asymptotic bound. The 88 NATs provide neither n nor any numeric quantity to compute and key A.

This is exactly the sort of definition-by-algorithm-name question the original brief asked to avoid. Labelling it Hashing, Greedy algorithms, Dynamic programming or Graph traversals provides no coverage of those topics. The solution's general comparison-sorting lower bound is a **worst-case** lower bound, not a lower bound on every input; its wording should not suggest otherwise. Counts: 144 one-mark, 191 two-mark placements.

### T11 — TM decidability

Example: Mock 003 Q11 (MSQ), Q48 (MCQ), Mock 004 Q25 (NAT). B, halting on blank input, is undecidable by reducing arbitrary-input halting: construct a machine that writes the chosen input and simulates the chosen machine. C, emptiness of the accepted language, is an undecidable nontrivial language property. D, language equivalence, is undecidable because deciding equivalence with a fixed empty-language machine would decide emptiness. Thus the intended answer is **A, none**; B,C,D are false.

The solution states that all are language properties covered by Rice's theorem. **Halting is not determined by the accepted language:** two machines can both accept the empty language while one rejects immediately and the other loops forever on blank input. The halting reduction is required instead. Also A is a meta-answer, not itself a “decision problem” of the kind requested; wording can be improved. All **43 NATs omit the problem options and key A**. Merely recalling three familiar undecidability results is not a multi-step GATE challenge. Counts: 72 one-mark, 96 two-mark placements.

### T12 — Non-context-free language

Example: Mock 004 Q15 (MCQ), Q64 (MSQ), Mock 003 Q53 (NAT). The stem specifies languages over **{a,b}**, but A is {a^n b^n c^n:n>=0}. That is not a language over the specified alphabet. Therefore **all 166 placements need repair**; do not certify them as technically unambiguous merely because the intended textbook answer is recognizable.

If the alphabet is corrected to {a,b,c}, the intended answer is A. A pumping-lemma proof uses a^p b^p c^p: a length-at-most-p pumping window cannot meet both the a and c blocks, so pumping down changes at least one count while leaving another p unchanged. B={a^n b^n} has the standard stack grammar; C={ww^R} is the even palindrome CFL; D={a^n b^m:n!=m} is the union of the n>m and n<m CFLs (unequal block counts). Thus B,C,D are context-free. The solution's phrase “cannot be tracked by a single stack” is intuition rather than a substitute for the necessary proof. All 52 NATs additionally omit every language option and key A. Counts: 74 one-mark, 92 two-mark placements.

## Consequences and repair priority

1. Treat Mock 003–100 as unvalidated drafts, not completed medium-to-hard examinations. Structural counts cannot override the content failures.
2. Replace the repeated tasks with independently authored problems. Retaining 98 copies and changing constants, option order, labels or type cannot satisfy the original uniqueness requirement.
3. Repair the 504 nonnumeric NAT placements by redesigning what is asked, not automatically substituting an option number. Convert the 415 single-answer MSQs or develop meaningful multi-answer alternatives.
4. Correct the alphabet error, false proof attributions, and invalid distinct-weight counterexample before any question from those families is reused.
5. Build topic coverage from actual reasoning performed. Current subtopic tags substantially overstate coverage. Add real liveness/propagation, code generation, recursive program analysis, searching/hashing, graph algorithms and language-proof tasks.
6. Reassess difficulty from the new questions. No solution here provides evidence that these four-subject placements meet the target 40/45/15 difficulty mix.

Exact affected references are listed by family and paper in the companion [reference appendix](AUDIT_TECHNICAL_THEORY_REFERENCES.md). Each listed NAT/MSQ can be located by its type; all members of a family inherit the substantive family findings described above. Findings overlap and must not be summed as if they were disjoint question counts.
