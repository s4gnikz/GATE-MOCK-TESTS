# Technical systems audit — Mock 003 through Mock 100

Audit date: 2026-10-13. **Result: FAIL; these papers cannot be described as technically validated.** This audit made no paper changes and created no Python files. It covers actual Operating Systems, Computer Organization and Architecture, Digital Logic, Databases and Computer Networks content in the 98 specified papers. It does not certify Mock 001 or Mock 002.

Read-only PowerShell extraction inspected all 98 question papers and solution documents, grouped their stems and solution bodies, and compared every distinct systems-content variant. The parent's question inventory was subsequently used to cross-check the selection by actual stem rather than trusting concept labels. Counts below cover **2,505 question occurrences, 22 distinct stems, and 14 reasoning families** (nine cache-capacity/associativity combinations are one family). All corresponding distinct solution variants were inspected. This is a model-based family review plus systematic extraction, not 2,505 blinded independent solves or human review. Series-wide duplicate counting is handled separately.

## Verified scope and response-format failures

| Type | Occurrences |
|---|---:|
| MCQ | 1,281 |
| MSQ | 470 |
| NAT | 754 |
| Total | 2,505 |

**445 NAT entries have the literal answer `A (exact)` rather than a number.** All 470 systems MSQs have the singleton key A. A single correct MSQ is not inherently forbidden by every examination convention, but it violates this project's explicit requirement for multiple correct choices when designated MSQ; these are effectively MCQs with a different label. Several are also technically unsound independently of that format failure.

| NAT family with alphabetic key | Count | Correct response or reason no numeric response exists | Example |
|---|---:|---|---|
| Banker's safe-state definition | 115 | A verbal safe-sequence criterion; the stem ends at “if and only if” and supplies no choices | Mock 003 Q16 |
| B+ tree minimum keys | 100 | 2 under the usual half-full internal-node convention | Mock 003 Q21 |
| DMA duty fraction | 118 | 0.1, or 10 if explicitly requesting percentage; assume one stolen cycle per transfer | Mock 004 Q13 |
| IEEE single-precision decoding | 43 | −4 | Mock 003 Q55 |
| Single-level page-table size | 22 | 4 MiB = 4,194,304 bytes; a NAT must specify the requested unit | Mock 006 Q37 |
| Relational operation noncommutativity | 31 | A named operation, with missing choices; not a numeric task | Mock 007 Q41 |
| Candidate key plus normal form | 16 | {A}, 2NF; a pair of nonnumeric answers, not NAT | Mock 004 Q19 |
| Total | 445 | | |

Examples are directly visible in [Mock 003 Q16](<C:/Users/Sandhit/Downloads/GATE Prep/GATE-CS-2027-MOCK-SERIES/papers/Mock_003/README.md:157>), [Q21](<C:/Users/Sandhit/Downloads/GATE Prep/GATE-CS-2027-MOCK-SERIES/papers/Mock_003/README.md:193>), [Q55](<C:/Users/Sandhit/Downloads/GATE Prep/GATE-CS-2027-MOCK-SERIES/papers/Mock_003/README.md:463>) and [Mock 007 Q41](<C:/Users/Sandhit/Downloads/GATE Prep/GATE-CS-2027-MOCK-SERIES/papers/Mock_007/README.md:351>). Their final answer tables and corresponding solutions retain the alphabetic NAT keys. This is a substantive unusable-answer-format failure, not a cosmetic issue.

## Incorrect or under-specified technical families

### TCP Reno: 45 occurrences; immediate fast-recovery answer not determined

Example: [Mock 005 Q18](<C:/Users/Sandhit/Downloads/GATE Prep/GATE-CS-2027-MOCK-SERIES/papers/Mock_005/README.md:168>) is NAT with key 16; [Mock 007 Q20](<C:/Users/Sandhit/Downloads/GATE Prep/GATE-CS-2027-MOCK-SERIES/papers/Mock_007/README.md:180>) offers 16, 1, 32 and 8 KB, keyed A. Eleven copies are NAT.

The question asks for cwnd **immediately after entering fast recovery**, given only a previous cwnd of 32 KB. Standard Reno inflates the new window by three segment sizes on entry; it deflates to the threshold after a subsequent advancing ACK. The threshold calculation also depends on FlightSize. MSS and FlightSize are not specified, so 16 KB is not the uniquely implied entry value. Even with the simplifying assumptions FlightSize=32 KB and MSS=1 KB, the usual entry value would be 19 KB, absent from the choices. The solution itself mentions the additional three MSS as a parenthetical alternative while nevertheless marking 16 as exact. [RFC 5681, section 3.2, steps 2, 3 and 6](https://www.rfc-editor.org/rfc/rfc5681#section-3.2) establishes this timing distinction.

### Synchronous counter: 215 occurrences; missing circuit and timing assumptions

Examples: [Mock 003 Q22](<C:/Users/Sandhit/Downloads/GATE Prep/GATE-CS-2027-MOCK-SERIES/papers/Mock_003/README.md:199>), Q25 and [Mock 004 Q31](<C:/Users/Sandhit/Downloads/GATE Prep/GATE-CS-2027-MOCK-SERIES/papers/Mock_004/README.md:264>). Sixty-three copies are NAT with key 50.

The stem gives four JK flip-flops with 12 ns propagation delay and AND gates with 4 ns delay. The solution silently chooses two AND levels and zero setup/skew, producing 1/(12+8) ns = 50 MHz. The counter's highest-bit enable is Q0 AND Q1 AND Q2: one three-input AND gives one gate level, whereas cascaded two-input AND gates give two. Both satisfy the written gate-delay description. Even ignoring setup/skew, these yield 62.5 MHz versus 50 MHz. Setup time is also unspecified. A circuit diagram or explicit two-input gate topology and timing assumptions are necessary. Missing assumptions are not legitimate difficulty.

### Relational Cartesian product: 100 occurrences; tuple convention not stated

Example: [Mock 003 Q26](<C:/Users/Sandhit/Downloads/GATE Prep/GATE-CS-2027-MOCK-SERIES/papers/Mock_003/README.md:232>). Set difference is certainly noncommutative. Under ordered tuple concatenation, Cartesian product is also noncommutative: {(1)} × {(2)} = {(1,2)}, whereas reversing operands gives {(2,1)}. Under named-attribute relational equality disregarding column order, the intended answer A alone can be valid. The solution introduces “up to tuple component ordering” although the stem does not. This is a convention ambiguity, not an unconditional claim that the answer must always include C. Restore the convention explicitly before using a single-answer key. Thirty-one NAT versions additionally omit the required choices entirely.

## Independently derived answers for every family

Difficulty below is an editorial estimate for a prepared GATE candidate. E = easy/routine, M = medium, U = ungradable as written. These are not empirical timing measurements and are not adjusted to meet blueprint quotas.

| Actual family | Occurrences | Independent derivation and answer | Difficulty / caveat |
|---|---:|---|---|
| Cache tag fields | 126 | Sets = capacity/(64 × ways); tag = 32−6−log2(sets). All nine answer values are shown below. | E–M; a short standard address partition, never hard |
| DMA cycle stealing | 374 | One 200 ns stolen cycle per 2,000 ns gives duty fraction 0.1 = 10%. Options B=5%, C=20%, D=2.5% disagree. | E; explicitly state one bus cycle per word and required NAT scale |
| JK synchronous counter | 215 | 50 MHz only with two AND levels and ignored setup/skew; other permitted implementations differ. | U |
| IEEE 0xC0800000 | 144 | Sign=1, exponent=129, fraction=0: −1 × 2^(129−127) = −4. Options −2,+4,−0.5 are wrong. | E–M; NAT alphabetic key invalid |
| Essential prime implicants | 143 | Minterms satisfy B=D independently of A,C, so F=B'D'+BD. These two disjoint maximal cubes are both essential; answer 2. | M; standard small K-map |
| Banker's safe-state definition | 401 | A safe sequence exists such that each process's remaining claim can be met after predecessors release allocations. Fully allocated resources, one-resource-type requests, and an existing deadlock are not equivalent criteria. | E; definitional MCQ, incomplete NAT |
| SJF average waiting | 50 | Execute the two 3 ms jobs before the 24 ms job. Waits are 0,3,6; mean 3 ms. The tie between short jobs does not change the mean. | E |
| Single-level page table | 50 | 2^(32−12) entries × 4 bytes = 2^22 bytes = 4 MiB. Options 2,1,8 MiB are wrong. | E–M; specify numeric output unit |
| B+ internal occupancy | 351 | Under the conventional minimum ceil(m/2) children, ceil(5/2)−1 = 2 keys. Options 3,4,1 are not the non-root minimum. | E; state minimum occupancy for full explicitness |
| Relational noncommutativity | 100 | Difference is noncommutative; union is commutative; natural join and Cartesian product require named-schema/column-order convention as discussed. | E conceptual content, U where convention affects key |
| Dependency chain normal form | 50 | A determines A,B,C,D; no dependency derives A, so sole candidate key {A}. No partial key dependency; B→C violates 3NF. Highest form 2NF, assuming 1NF and the stated dependency closure. | M; unsuitable unchanged as NAT |
| CRC checksum length | 366 | Generator degree 3 implies a three-bit appended remainder. Four counts generator coefficients, two undercounts degree, one is simple parity. | E; direct fact recall |
| /20 split into /24 | 90 | Four additional prefix bits yield 2^4 =16 subnets; 192.168.16.0 is a valid /20 boundary. | E; one formula application |
| Reno immediate recovery | 45 | Needs threshold/FlightSize and SMSS; generic entry cwnd is threshold plus 3 SMSS. Not fixed by old cwnd alone. | U |

### All nine cache variants

| Capacity | Ways | Occurrences | Sets | Tag bits | Example |
|---|---:|---:|---:|---:|---|
| 16 KiB | 2 | 13 | 128 | 19 | Mock 019 Q12 |
| 16 KiB | 4 | 10 | 64 | 20 | Mock 003 Q30 |
| 16 KiB | 8 | 21 | 32 | 21 | Mock 009 Q51 |
| 32 KiB | 2 | 15 | 256 | 18 | Mock 008 Q26 |
| 32 KiB | 4 | 14 | 128 | 19 | Mock 005 Q15 |
| 32 KiB | 8 | 14 | 64 | 20 | Mock 005 Q20 |
| 64 KiB | 2 | 11 | 512 | 17 | Mock 006 Q51 |
| 64 KiB | 4 | 16 | 256 | 18 | Mock 003 Q36 |
| 64 KiB | 8 | 12 | 128 | 19 | Mock 008 Q31 |

The arithmetic in the cache solutions matches these values. Parameter changes do not create nine meaningfully different reasoning tasks.

## Solution explanations contain additional errors

- [Mock 003 Q63 solution](<C:/Users/Sandhit/Downloads/GATE Prep/GATE-CS-2027-MOCK-SERIES/papers/Mock_003/SOLUTIONS.md:840>) correctly gives mean waiting 3 ms, but describes option B=6 as average turnaround and option C=9 as FCFS waiting. Actual SJF mean turnaround is (3+6+30)/3=13 ms. FCFS in P1,P2,P3 order has mean waiting (0+24+27)/3=17 ms. Thus both distractor explanations are false. The same choice-bearing explanation appears 36 times.
- [Mock 003 Q37 solution](<C:/Users/Sandhit/Downloads/GATE Prep/GATE-CS-2027-MOCK-SERIES/papers/Mock_003/SOLUTIONS.md:485>) calls option B=3 “maximum number of keys for 3 children.” Three child pointers correspond to two separator keys, not three. The main answer 2 is correct, but the explanation is not. This choice-bearing solution appears 251 times.
- [Mock 003 Q30 solution](<C:/Users/Sandhit/Downloads/GATE Prep/GATE-CS-2027-MOCK-SERIES/papers/Mock_003/SOLUTIONS.md:400>) labels dividing cache capacity by associativity before computing line count a misconception. That calculation is a perfectly valid route to the number of lines per way, equal to the number of sets. The text should distinguish total lines from sets rather than implying that this order of division is inherently wrong. This misleading note appears in all 126 cache occurrences.

## Claimed topic coverage does not match tested content

Actual broad subject labels remained in the relevant five subjects in this scope, but subtopic labels repeatedly claim unrelated coverage. Examples from Mock 003's solutions are sufficient to establish the problem:

| Question | Published concept label | What is actually tested |
|---|---|---|
| Q16 | Operating Systems — System calls | Safe-sequence definition |
| Q18 | Operating Systems — Processes and threads | Same safe-sequence definition |
| Q32 | Operating Systems — Interprocess communication | Same safe-sequence definition |
| Q21 | Databases — ER model | B+ tree minimum occupancy |
| Q37 | Databases — Tuple calculus | Same B+ tree occupancy |
| Q49 | Databases — Integrity constraints | Same B+ tree occupancy |
| Q24 | Computer Networks — Socket API | CRC generator degree |
| Q33 | Computer Networks — DNS and HTTP | Same CRC degree |
| Q54 | Computer Networks — Switching and performance | Same CRC degree |
| Q38 | Databases — SQL | Relational algebra operator property; no SQL |
| Q44 | Digital Logic — Fixed-point arithmetic | IEEE floating-point decoding |

Across all 98 papers, the B+ occupancy stem is assigned seven database subtopics; the Banker's definition eight OS subtopics; the CRC-degree stem eight networking subtopics; and DMA duty fraction six architecture subtopics, including ALU design, instruction addressing, and pipelining. These labels cannot serve as a valid coverage matrix. Counter timing is also labelled tabular minimization in some records, and subnet counting is labelled fragmentation.

## Release consequence

There are at least **705 distinct affected question occurrences in this scope** from three disjoint groups alone: 445 nonnumeric NAT keys, 215 under-specified counter questions, and 45 incorrect/under-specified Reno questions. Of the 754 NAT occurrences, 519 fall in those three groups (445 + 63 + 11). This lower bound excludes the Cartesian-product convention ambiguity, deficient distractor explanations, misleading labels, repetition, and difficulty failures.

The 470 singleton MSQs fail the series' own multi-answer requirement. Most technically coherent families are direct definitions or short formula substitution, including many two-mark copies. They do not substantiate the claimed medium-to-hard distribution, and none of these families warrants a Hard classification merely because its metadata says so.

Do not repair this corpus merely by changing `A` into a number. Some stems require substantive redesign, missing assumptions, different response types, and newly constructed questions to meet originality and syllabus coverage. Recheck answers independently after redesign. This audit recommends withholding the affected papers' validated/released status; it does not alter files or silently approve unaffected occurrences.
