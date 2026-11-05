# Mock 001 — current-content audit

Audit date: 2026-10-13. **No answer-key defect found in this audit. Mock 001 is materially stronger than Mock 003–100.** Its current content matches the previously accepted 65-question bank. Difficulty remains an editorial estimate: this reviewer assesses 28 Medium, 30 Medium-Hard and 7 Hard, rather than the stored 28/27/10 split. This report does not claim an empirical or human validation of the target distribution.

## Scope, provenance and integrity

Read all 65 current questions, options and worked solutions. Previously accepted review proofs were read and reused as evidence; targeted mathematical and systems derivations were independently reconsidered as detailed below. This was **not a fresh blind solve of all 65 questions** and not human review. Historical Python tests, C execution and other recorded computational checks were not rerun. No paper or solution files were edited, and no Python files were created.

Current content was compared with the 65 `paper=1` records in `data/questions.jsonl`, all of which have `validation_status=ACCEPTED`. For every question, a SHA-256 comparison was made over a projection containing the stem, ordered options, answer, marks and type. Only whitespace was normalized, along with the displayed NAT `(exact)` suffix and spaces between answer letters. **65/65 projections match.** This is an audit comparison hash, not a claim that the existing internal `reviewed_content_hash` algorithm was rerun. In addition, all 65 canonical solution bodies, all canonical option explanations and all misconception statements occur in the current solution document after whitespace normalization.

Full current file hashes, SHA-256:

- `papers/Mock_001/README.md`: `4DE4619AB9BC33DA5062A63E0D690C020429E7E0904DF46E7806341C2044E58C`
- `papers/Mock_001/SOLUTIONS.md`: `D4C53DD954230B4DA927B7A13F81E9F28295E496A13BCA2774B191CF24BF930A`

The current question/solution extraction was cross-checked against the parent's `reports/AUDIT_QUESTION_INVENTORY.json`. Thus reliance on the accepted proofs is tied to unchanged question content rather than merely the same paper number. These hashes describe this audit snapshot.

## Renewed mathematical and technical checks

The following are fresh reasoning checks in this audit, although the proposed answers and old solutions were visible. Other questions received a read-through, canonical-content comparison and inspection of their existing derivations; they were not all solved again from scratch.

| Q | Independent check | Outcome |
|---|---|---|
| 6 | Treat AB as one circular block: 2×5! total. Subtract two 4×4! forbidden-pair events and restore 8×3! for their intersection. | 240−96−96+48=96; A |
| 10 | Weighted RR probability is 1/4; weighted same-colour probability is 13/30. Ratio is 15/26, not a simple average of bag-conditioned ratios. | B |
| 16 | 7+5+1=13 gives raw 1101 with no carry; signed 7−(−6) exceeds the four-bit range. | D: 1101,0,1 |
| 22 | FIRST(A) contains a,b,epsilon; FOLLOW(A)=FOLLOW(B)={a}. Only cells (S,b) and (A,a) receive two productions. | 2 |
| 24 | Inner f=2 for abs(x)≤1 and 2abs(x) otherwise. The outer plateau extends the composition's flat region to abs(x)≤2. | Only ±2 are corners; C |
| 26 | The six permitted minterms induce the six-cycle 0–1–5–7–6–2–0. No four-cell implicant is permitted. A three-term optimum is a perfect matching of that cycle. | Two alternating matchings; 2 |
| 30 | Merge the two odd-b product states because last-symbol status does not affect their future acceptance. The even accepting/nonaccepting states remain distinguishable, as does odd parity. | Smallest complete DFA has 3 states |
| 37 | Prefix (aab)^n followed by (abb)^n is a legal balanced log without triples. For m≠n, the same suffix appended to (aab)^m fails balance. A stack plus finite run-memory is deterministic. | Nonregular deterministic context-free; B |
| 39 | In an eigenbasis beginning with u, the update affects only the first row; the diagonal changes from (2,1,4) to (0,1,4). Distinct eigenvalues give diagonalizability and rank two. An off-diagonal first-row update disproves universal commutation. | A,B,D |
| 40 | Derivative is 4(x³−ax+1). Three simple roots require a³>27/4. Their alternating signs give two strict minima; equality does not. | Least integer a is 2 |
| 41 | Transpose followed by row reversal is a clockwise quarter-turn. 2027 mod 4=3, giving new[r,c]=old[c,4−r]. | a[7]=13 and a[17]=11; A |
| 43 | Every C call reaches A's persistent lexical x, so successive returns are 5,6,7. Recursive B calls accumulate these rather than rebinding C's x. | 18; A |
| 45 | Q waits for X EOF, P for Y EOF, R for P. Closing R's unused X writer before its wait removes the cycle and permits Q then P then R to finish. | C |
| 46 | Partition by last writer. A-last outcomes {1,7,11,17}; B-last {3,4,8,9,14}; C-last {5,6,8,9,12}. Union has 12 values. This is an analytic rederivation; the old 90-interleaving program was not rerun. | 12 |
| 47 | Degree and nonzero constant term give the single-bit and short-burst guarantees. Multiplication confirms (x³+x+1)(x⁴+x²+x+1)=x⁷+1 over GF(2). The generator itself is an undetected odd-weight error. | A,B,C |
| 49 | With x=2,y=5,z=0, integer y/x>2 is false but y>2x is true, changing both truth and increment. Speculation also introduces division by zero at x=0. | A,D |
| 50 | A window of length at most p cannot include both a and c in a^p b^p c^p. Deleting nonempty v,y changes at least one count while leaving at least one count p. | A,B |
| 52 | Signed raw operands −25 and 57 give rescaled result −1425/16=−89.0625, rounded to −89. | Unsigned byte encoding 167 |
| 53 | Prefix 3,2 forces residual stack [1] and unread 4,5,6. Four-label stack permutations number 14; only pushing all four before popping violates capacity three. | 13 |
| 54 | Joint bus field has 1+8(2^5−1)=249 choices, hence eight bits. Remaining independent fields need 3+7+2 bits. | 20; B |
| 55 | Tail-sum mean is 1+11/40+67/400. N=3 reveals two positives, giving posterior 64/67 rather than the three-positive posterior. The ++− weights are 128:27; (+− or ++−) weights are 288:297. | A,C,D |
| 56 | Acceptance on a fixed input and reaching a designated state on some input have finite discoverable witnesses. The universal-language restriction and total-halting property each admit a reduction from nonhalting, as shown in the saved solution. The bounded-simulation construction for totality has the correct direction. | Exactly sets 1 and 4; 2 |
| 57 | Upper bits 10 select 0x8000–0xBFFF; A13:A12 select chip and low 12 bits offset. Ignoring A14 makes two aliases; ignoring A0 in the alternate wiring destroys uniqueness. | A,B,C |
| 58 | Only group k=1 has counts (3,2), sum 20 and both HAVING conditions true. The all-NULL sum for k=2 is UNKNOWN in the comparison. | A |
| 59 | Original work (1,1) permits P1 then P0 then P2. Granting P0 one B leaves work (1,0), insufficient for any remaining need. | C |
| 61 | Five maximum sets are ADFH, BCEG, BCEH, BCFH, BDFH. Earliest-finish scheduling proves four is optimal. | (4,5); C |
| 64 | The missing {a,b} forces join({a},{b})=top. Meet with {c} disproves distributivity. Only {c} lacks a complement; its unique two-cover structure fixes it under automorphisms, leaving only the a/b swap. | B,C,D |
| 65 | One-way propagation 12 μs; inclusive round trip plus detection 26 μs. At 100 Mb/s this is 2,600 bits. | 325 bytes |

These checks support the previously accepted answers. No answer change is recommended from this audit. Technical qualifiers supplied in the pilot—such as atomicity and sequential consistency, same-cycle semantics where relevant, set/SQL NULL semantics, pipeline timing, pointer bounds, and idealized network units—are materially better specified than the repeated questions in Mock 003–100.

## All-question answer and difficulty assessment

M=Medium, MH=Medium-Hard, H=Hard. This is an independent editorial assessment based on the actual task, not a claim that marks or metadata establish difficulty. Some M questions are at the easier end. Answers are reconciled with the unchanged canonical record; the table does not imply all 65 were freshly blind-solved.

| Q | Answer | Assessment | Main task |
|---|---|---|---|
| 1 | A | M | Relative versus main-clause agreement |
| 2 | 35.71 | M | Conditional percentage after cancellation |
| 3 | 2 | M | Implication and exclusive selection constraints |
| 4 | A | M | Ordered reflection/rotation composition |
| 5 | B | M | Supported conclusion from aggregate counts |
| 6 | A | MH | Circular blocks and inclusion-exclusion |
| 7 | A | M | Weighted productivity with changing mixture |
| 8 | 2 | MH | Reverse two folds and filter punch images |
| 9 | C | M | Explicit chronological ordering; relatively easy for two marks |
| 10 | B | MH | Conditional probability in a bag mixture |
| 11 | A | M | Boolean cofactors/consensus |
| 12 | 2 | M | Shared descriptor offset trace |
| 13 | A | M | Don't-care minimization |
| 14 | A | MH | Negation of nested unique-existence statement |
| 15 | 120 | MH | Signed, scaled, indirect PC-relative addressing |
| 16 | D | MH | Separate signed overflow from carry |
| 17 | 3 | M | Nested weak-entity identifying keys |
| 18 | B | M | Maximal munch and keyword boundary |
| 19 | A,C | M | Router changes across protocol layers |
| 20 | 3 | M | Equality shifts and sorting stability |
| 21 | A,B,D | MH | Division-like algebra and empty-set behavior |
| 22 | 2 | MH | FIRST/FOLLOW conflict counting |
| 23 | 2 | M | Parametric singular homogeneous system |
| 24 | C | MH | Composition eliminates inner-function corners |
| 25 | 2 | M | Infer Poisson rate then second moment |
| 26 | 2 | MH | Count all minimum prime-implicant covers |
| 27 | B | M | Legal C pointer and assignment trace |
| 28 | A,C | MH | Double hashing and tombstone semantics |
| 29 | A | M | Fork loop with early child exit |
| 30 | 3 | MH | Merge equivalent DFA product states |
| 31 | 3 | M | Store-and-forward serialization |
| 32 | D | MH | Unbounded finite parse-tree family |
| 33 | A | M | Recursive identity and activation depth |
| 34 | A,D | M | Deterministic delimiter-based stack comparison |
| 35 | 6 | MH | Idempotent-function image characterization |
| 36 | 448 | MH | Coupled nested-loop bounds |
| 37 | B | H | Nonregularity proof despite bounded runs |
| 38 | 4 | M | Postfix evaluation-stack trace; short for two marks |
| 39 | A,B,D | H | Rank-one update in an eigenbasis |
| 40 | 2 | H | Cubic critical-point threshold for two minima |
| 41 | A | MH | Matrix permutation composition and period |
| 42 | A | M | Multiplexer cofactors |
| 43 | A | MH | Lexical environments across sibling recursion |
| 44 | C | M | Simultaneous state update and cycle |
| 45 | C | MH | Pipe EOF ownership and wait dependencies |
| 46 | 12 | H | Exhaustive interleaving outcomes by last writer |
| 47 | A,B,C | MH | Multiple CRC guarantees and counterexample |
| 48 | B | M | Universal biconditional means exact set equality |
| 49 | A,D | MH | Integer truncation plus short-circuit side effects |
| 50 | A,B | MH | Pumping-lemma quantifiers and count preservation |
| 51 | B | M | Linked-list detachment and reversed accumulation |
| 52 | 167 | MH | Signed fixed-point multiplication and re-encoding |
| 53 | 13 | MH | Constrained residual stack-permutation count |
| 54 | B | MH | Joint command encoding and independent fields |
| 55 | A,C,D | H | Stopping-rule events and Bayesian conditioning |
| 56 | 2 | H | Recognizability versus universal properties |
| 57 | A,B,C | MH | Chip decoding and address aliases |
| 58 | A | M | Duplicate and NULL aggregate semantics |
| 59 | C | MH | Safety before and after a tentative grant |
| 60 | A | M | Conditional miss rates and break-even inequality |
| 61 | C | MH | Prove and enumerate optimal activity sets |
| 62 | A,C,D | MH | In-place DP dependency discipline |
| 63 | A,B,D | MH | Referential actions versus uniqueness/NULL |
| 64 | B,C,D | H | Non-Boolean lattice complements and automorphisms |
| 65 | 325 | MH | Propagation, detection latency and frame units |

Counts: **28 M (43.1%), 30 MH (46.2%), 7 H (10.8%)**. Stored canonical labels give 28 M, 27 MH, 10 H. The paper is credibly medium-to-hard overall, but the exact 15% Hard target is not independently confirmed by this review. Neither estimate is empirically calibrated; do not hide that uncertainty by treating stored labels as measurements.

## Disposition

Retain the prior scoped technical acceptance of Mock 001: the current content is unchanged, all solutions remain present, and the renewed checks found no substantive answer failure. This is not a fresh full-series uniqueness or historical-research certification. Difficulty calibration could be improved, especially the comparatively direct two-mark Q9 and Q38. Any further claim that the paper exactly achieves the difficulty target should distinguish stored design labels from an independent estimate and, ideally, candidate timing/error data.
