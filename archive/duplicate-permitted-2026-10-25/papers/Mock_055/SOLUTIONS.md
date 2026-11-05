# Worked Solutions — Mock Test 055

Review provenance is recorded in the structured bank; no human review is claimed.

## Q1

**Correct answer:** A

**Concept:** General Aptitude — Inductive reasoning and analogies

Valid pairs: {R, S}, {P, R} (violates iff), {P, S} (violates iff). Valid selections: {R, S}, {Q, R} (if S excluded? No, R iff S forces R and S together), or non-R/S pairs: {P}, {Q}. Thus only {R,S} and non-RS pairs {P,Q} (forbidden). Exhaustive analysis yields 3 valid combinations under relaxed parity.

- **A:** Correct combinatorial count.
- **B:** Underestimated cases.
- **C:** Overestimated non-independent pairs.
- **D:** Missed mutually exclusive condition.

**Common misconception:** Misinterpreting bi-conditional constraint 'if and only if'.

## Q2

**Correct answer:** A

**Concept:** General Aptitude — Two- and three-dimensional patterns

Valid pairs: {R, S}, {P, R} (violates iff), {P, S} (violates iff). Valid selections: {R, S}, {Q, R} (if S excluded? No, R iff S forces R and S together), or non-R/S pairs: {P}, {Q}. Thus only {R,S} and non-RS pairs {P,Q} (forbidden). Exhaustive analysis yields 3 valid combinations under relaxed parity.

- **A:** Correct combinatorial count.
- **B:** Underestimated cases.
- **C:** Overestimated non-independent pairs.
- **D:** Missed mutually exclusive condition.

**Common misconception:** Misinterpreting bi-conditional constraint 'if and only if'.

## Q3

**Correct answer:** A

**Concept:** General Aptitude — Numerical series

First differences are 5, 7, 9, 11. Second difference is constant 2. Next term is 47.

- **A:** Correct polynomial sequence progression.
- **B:** Underestimated next difference.
- **C:** Overestimated acceleration term.
- **D:** Linear extrapolation error.

**Common misconception:** Assuming purely linear arithmetic difference.

## Q4

**Correct answer:** A

**Concept:** General Aptitude — Geometry and mensuration

Valid pairs: {R, S}, {P, R} (violates iff), {P, S} (violates iff). Valid selections: {R, S}, {Q, R} (if S excluded? No, R iff S forces R and S together), or non-R/S pairs: {P}, {Q}. Thus only {R,S} and non-RS pairs {P,Q} (forbidden). Exhaustive analysis yields 3 valid combinations under relaxed parity.

- **A:** Correct combinatorial count.
- **B:** Underestimated cases.
- **C:** Overestimated non-independent pairs.
- **D:** Missed mutually exclusive condition.

**Common misconception:** Misinterpreting bi-conditional constraint 'if and only if'.

## Q5

**Correct answer:** A

**Concept:** General Aptitude — Verbal grammar

The subject 'each of the candidates' takes a singular verb form 'has' in formal standard English.

- **A:** Correct singular agreement.
- **B:** Incorrect plural verb.
- **C:** Grammatical number disagreement.
- **D:** Malformed auxiliary verb construction.

**Common misconception:** Attracted agreement with the plural noun inside the prepositional phrase.

## Q6

**Correct answer:** 57.1 (exact)

**Concept:** General Aptitude — Ratios and percentages

Component X initially has 80 litres. Adding 16 litres yields 96 litres out of total 168 litres = 57.1%.

**Common misconception:** Forgetting to update total mixture volume when adding new components.

## Q7

**Correct answer:** A

**Concept:** General Aptitude — Deductive logic

Valid pairs: {R, S}, {P, R} (violates iff), {P, S} (violates iff). Valid selections: {R, S}, {Q, R} (if S excluded? No, R iff S forces R and S together), or non-R/S pairs: {P}, {Q}. Thus only {R,S} and non-RS pairs {P,Q} (forbidden). Exhaustive analysis yields 3 valid combinations under relaxed parity.

- **A:** Correct combinatorial count.
- **B:** Underestimated cases.
- **C:** Overestimated non-independent pairs.
- **D:** Missed mutually exclusive condition.

**Common misconception:** Misinterpreting bi-conditional constraint 'if and only if'.

## Q8

**Correct answer:** A

**Concept:** General Aptitude — Spatial transformations

Valid pairs: {R, S}, {P, R} (violates iff), {P, S} (violates iff). Valid selections: {R, S}, {Q, R} (if S excluded? No, R iff S forces R and S together), or non-R/S pairs: {P}, {Q}. Thus only {R,S} and non-RS pairs {P,Q} (forbidden). Exhaustive analysis yields 3 valid combinations under relaxed parity.

- **A:** Correct combinatorial count.
- **B:** Underestimated cases.
- **C:** Overestimated non-independent pairs.
- **D:** Missed mutually exclusive condition.

**Common misconception:** Misinterpreting bi-conditional constraint 'if and only if'.

## Q9

**Correct answer:** A

**Concept:** General Aptitude — Reading comprehension

Valid pairs: {R, S}, {P, R} (violates iff), {P, S} (violates iff). Valid selections: {R, S}, {Q, R} (if S excluded? No, R iff S forces R and S together), or non-R/S pairs: {P}, {Q}. Thus only {R,S} and non-RS pairs {P,Q} (forbidden). Exhaustive analysis yields 3 valid combinations under relaxed parity.

- **A:** Correct combinatorial count.
- **B:** Underestimated cases.
- **C:** Overestimated non-independent pairs.
- **D:** Missed mutually exclusive condition.

**Common misconception:** Misinterpreting bi-conditional constraint 'if and only if'.

## Q10

**Correct answer:** A

**Concept:** General Aptitude — Permutations and combinations

First differences are 8, 10, 12, 14. Second difference is constant 2. Next term is 68.

- **A:** Correct polynomial sequence progression.
- **B:** Underestimated next difference.
- **C:** Overestimated acceleration term.
- **D:** Linear extrapolation error.

**Common misconception:** Assuming purely linear arithmetic difference.

## Q11

**Correct answer:** A

**Concept:** Programming and Data Structures — Binary search trees

Insert 7 at index 8 (child of index 4 = 15). 7 < 15, so swap 7 and 15 (7 now at index 4). Parent of index 4 is index 2 (value 9). 7 < 9, so swap 7 and 9 (7 now at index 2). Parent of index 2 is index 1 (value 4). 7 > 4, stop. Final index is 2.

- **A:** True: sifts up past 15 and 9, resting at index 2 under root 4.
- **B:** False: position before second percolation step.
- **C:** False: cannot replace root (4 < 7).
- **D:** False: initial insertion position before heapify.

**Common misconception:** Stopping sift-up before comparing against parent node.

## Q12

**Correct answer:** 21 (exact)

**Concept:** Computer Organization and Architecture — Memory hierarchy and performance

Total blocks = 16384//64 = 256. Number of sets = 32 (5 bits). Offset = log2(64) = 6 bits. Tag bits = 32 - 5 - 6 = 21 bits.

**Common misconception:** Dividing total cache capacity by associativity before computing line count.

## Q13

**Correct answer:** A

**Concept:** Theory of Computation — Regular expressions and finite automata

States represent longest prefix matched of `011`: q0 (empty), q1 (`0`), q2 (`01`), q3 (`011`, accepting). Exactly 4 pairwise distinguishable states by Myhill-Nerode theorem.

- **A:** True: exactly 4 states are necessary and sufficient.
- **B:** False: cannot distinguish prefixes `01` and `011`.
- **C:** False: non-minimal DFA.
- **D:** False: NFA powerset bound without minimization.

**Common misconception:** Assuming NFA state count equals minimal DFA state count.

## Q14

**Correct answer:** A

**Concept:** Engineering Mathematics — Extrema and mean value theorem

By Cayley's formula, the number of labelled spanning trees on n vertices is n^(n-2). For n=5, 5^(5-2) = 125.

- **A:** True by Cayley's tree enumeration theorem.
- **B:** False: counts edges, not spanning trees.
- **C:** False: wrong exponent (n-1).
- **D:** False: squared vertex count.

**Common misconception:** Confusing total edges in complete graph with spanning tree count.

## Q15

**Correct answer:** A

**Concept:** Theory of Computation — Context-free grammars

By Rice's Theorem and the Halting Problem, all nontrivial semantic properties of languages recognized by Turing machines (halting, emptiness, equivalence) are undecidable.

- **A:** True: all listed problems are undecidable by Rice's theorem.
- **B:** False: equivalent to the Halting problem (undecidable).
- **C:** False: emptiness problem for TMs is undecidable.
- **D:** False: equivalence problem for TMs is undecidable.

**Common misconception:** Confusing decidable properties of DFAs (emptiness, equivalence) with those of Turing machines.

## Q16

**Correct answer:** A

**Concept:** Databases — File organization

A non-root internal node in a B+ tree of order m must have at least ⌈m/2⌉ child pointers. For m=5, ⌈5/2⌉ = 3 children, which corresponds to 3 - 1 = 2 keys.

- **A:** True: ⌈5/2⌉ - 1 = 3 - 1 = 2 keys minimum.
- **B:** False: maximum number of keys for 3 children.
- **C:** False: maximum capacity (m-1 = 4).
- **D:** False: root minimum keys, not general internal node.

**Common misconception:** Confusing child pointer minimum ⌈m/2⌉ with key count minimum (⌈m/2⌉ - 1).

## Q17

**Correct answer:** A

**Concept:** Engineering Mathematics — Conditional probability and Bayes theorem

By Cayley's formula, the number of labelled spanning trees on n vertices is n^(n-2). For n=5, 5^(5-2) = 125.

- **A:** True by Cayley's tree enumeration theorem.
- **B:** False: counts edges, not spanning trees.
- **C:** False: wrong exponent (n-1).
- **D:** False: squared vertex count.

**Common misconception:** Confusing total edges in complete graph with spanning tree count.

## Q18

**Correct answer:** A

**Concept:** Programming and Data Structures — Binary heaps

Insert 7 at index 8 (child of index 4 = 15). 7 < 15, so swap 7 and 15 (7 now at index 4). Parent of index 4 is index 2 (value 9). 7 < 9, so swap 7 and 9 (7 now at index 2). Parent of index 2 is index 1 (value 4). 7 > 4, stop. Final index is 2.

- **A:** True: sifts up past 15 and 9, resting at index 2 under root 4.
- **B:** False: position before second percolation step.
- **C:** False: cannot replace root (4 < 7).
- **D:** False: initial insertion position before heapify.

**Common misconception:** Stopping sift-up before comparing against parent node.

## Q19

**Correct answer:** 16 (exact)

**Concept:** Engineering Mathematics — Partial orders and lattices

By Cayley's formula, the number of labelled spanning trees on n vertices is n^(n-2). For n=4, 4^(4-2) = 16.

**Common misconception:** Confusing total edges in complete graph with spanning tree count.

## Q20

**Correct answer:** A

**Concept:** Operating Systems — I/O scheduling

By definition, a state is safe if there exists a safe sequence of processes <P1, P2, ..., Pn> such that for each Pi, the resources Pi can still request can be satisfied by current available resources plus resources held by all preceding processes Pj (j < i).

- **A:** True: standard formal definition of safe state in Banker's algorithm.
- **B:** False: fully allocated resources often lead to unsafe states.
- **C:** False: irrelevant single-resource restriction.
- **D:** False: Banker's algorithm is proactive avoidance, not recovery.

**Common misconception:** Confusing an unsafe state with an active deadlock (all deadlocks are unsafe, but not all unsafe states are deadlocked).

## Q21

**Correct answer:** A

**Concept:** Theory of Computation — Pushdown automata

{ a^n b^n c^n | n ≥ 0 } requires simultaneous comparison of three independent block counts, which cannot be tracked by a single pushdown stack; proven non-CFL via Ogden's/pumping lemma.

- **A:** True: canonical non-context-free language.
- **B:** False: deterministic context-free language.
- **C:** False: context-free palindromic language.
- **D:** False: context-free language with unequal counts.

**Common misconception:** Assuming pushdown automata can count three distinct symbol groups simultaneously.

## Q22

**Correct answer:** A

**Concept:** Algorithms — Graph traversals

Merge Sort divides the array into halves in Θ(1), recursively sorts them in 2T(n/2), and merges in at most n-1 comparisons. By Master Theorem, T(n) = 2T(n/2) + Θ(n) = Θ(n log n) in all cases (best, average, and worst).

- **A:** True: worst-case comparison complexity is strictly Θ(n log n).
- **B:** False: quadratic time applies to Quick Sort worst-case, not Merge Sort.
- **C:** False: lower bound for comparison sort is Ω(n log n).
- **D:** False: sublinear sorting is impossible.

**Common misconception:** Confusing Merge Sort's invariant worst-case with Quicksort's unbalanced partition worst-case.

## Q23

**Correct answer:** A

**Concept:** Digital Logic — Combinational circuits

Critical path delay = t_ff + 2*t_and = 12 + 8 = 20 ns. Maximum clock frequency f = 1 / 20 ns = 50 MHz.

- **A:** True: critical path 20 ns gives 50 MHz.
- **B:** False: overestimates ripple propagation path.
- **C:** False: ignores gate propagation delay.
- **D:** False: double counts setup time.

**Common misconception:** Neglecting intermediate enable steering gate delays in synchronous counters.

## Q24

**Correct answer:** A

**Concept:** Computer Organization and Architecture — Cache mapping

Total blocks = 16384//64 = 256. Number of sets = 128 (7 bits). Offset = log2(64) = 6 bits. Tag bits = 32 - 7 - 6 = 19 bits.

- **A:** True: 32 - set_bits - offset_bits gives exact tag size.
- **B:** False: miscalculated number of sets.
- **C:** False: forgot associativity factor.
- **D:** False: inverted index/tag field partitioning.

**Common misconception:** Dividing total cache capacity by associativity before computing line count.

## Q25

**Correct answer:** A

**Concept:** Operating Systems — Memory management

By definition, a state is safe if there exists a safe sequence of processes <P1, P2, ..., Pn> such that for each Pi, the resources Pi can still request can be satisfied by current available resources plus resources held by all preceding processes Pj (j < i).

- **A:** True: standard formal definition of safe state in Banker's algorithm.
- **B:** False: fully allocated resources often lead to unsafe states.
- **C:** False: irrelevant single-resource restriction.
- **D:** False: Banker's algorithm is proactive avoidance, not recovery.

**Common misconception:** Confusing an unsafe state with an active deadlock (all deadlocks are unsafe, but not all unsafe states are deadlocked).

## Q26

**Correct answer:** A

**Concept:** Engineering Mathematics — LU decomposition

By Cayley's formula, the number of labelled spanning trees on n vertices is n^(n-2). For n=6, 6^(6-2) = 1296.

- **A:** True by Cayley's tree enumeration theorem.
- **B:** False: counts edges, not spanning trees.
- **C:** False: wrong exponent (n-1).
- **D:** False: squared vertex count.

**Common misconception:** Confusing total edges in complete graph with spanning tree count.

## Q27

**Correct answer:** A

**Concept:** Databases — B-trees and B+ trees

A non-root internal node in a B+ tree of order m must have at least ⌈m/2⌉ child pointers. For m=5, ⌈5/2⌉ = 3 children, which corresponds to 3 - 1 = 2 keys.

- **A:** True: ⌈5/2⌉ - 1 = 3 - 1 = 2 keys minimum.
- **B:** False: maximum number of keys for 3 children.
- **C:** False: maximum capacity (m-1 = 4).
- **D:** False: root minimum keys, not general internal node.

**Common misconception:** Confusing child pointer minimum ⌈m/2⌉ with key count minimum (⌈m/2⌉ - 1).

## Q28

**Correct answer:** A

**Concept:** Compiler Design — Constant propagation

Local common subexpression elimination operates strictly within the boundaries of a single basic block and requires no control-flow or interprocedural information.

- **A:** True: intra-basic-block optimization requires only local value numbering.
- **B:** False: requires global interprocedural call-graph analysis.
- **C:** False: requires link-time whole-program analysis.
- **D:** False: requires closed-world object hierarchy analysis.

**Common misconception:** Assuming basic block optimizations require knowledge of entire program control flow.

## Q29

**Correct answer:** A

**Concept:** Computer Networks — Switching and performance

The degree of the generator polynomial G(x) is 3 (highest power of x is 3). The appended CRC checksum length is always equal to the degree of G(x), which is 3 bits.

- **A:** True: FCS length equals degree of generator polynomial (degree 3 = 3 bits).
- **B:** False: counts polynomial coefficients (4 bits), not appended remainder degree.
- **C:** False: underestimated remainder size.
- **D:** False: parity bit confusion.

**Common misconception:** Confusing number of polynomial coefficients (which is degree + 1) with remainder length.

## Q30

**Correct answer:** A (exact)

**Concept:** Compiler Design — Liveness analysis

Local common subexpression elimination operates strictly within the boundaries of a single basic block and requires no control-flow or interprocedural information.

**Common misconception:** Assuming basic block optimizations require knowledge of entire program control flow.

## Q31

**Correct answer:** A

**Concept:** Digital Logic — Sequential circuits

Critical path delay = t_ff + 2*t_and = 12 + 8 = 20 ns. Maximum clock frequency f = 1 / 20 ns = 50 MHz.

- **A:** True: critical path 20 ns gives 50 MHz.
- **B:** False: overestimates ripple propagation path.
- **C:** False: ignores gate propagation delay.
- **D:** False: double counts setup time.

**Common misconception:** Neglecting intermediate enable steering gate delays in synchronous counters.

## Q32

**Correct answer:** A

**Concept:** Computer Networks — Error detection

The degree of the generator polynomial G(x) is 3 (highest power of x is 3). The appended CRC checksum length is always equal to the degree of G(x), which is 3 bits.

- **A:** True: FCS length equals degree of generator polynomial (degree 3 = 3 bits).
- **B:** False: counts polynomial coefficients (4 bits), not appended remainder degree.
- **C:** False: underestimated remainder size.
- **D:** False: parity bit confusion.

**Common misconception:** Confusing number of polynomial coefficients (which is degree + 1) with remainder length.

## Q33

**Correct answer:** A

**Concept:** Algorithms — Minimum spanning trees

Distinct edge weights guarantee a unique MST (Statement I is true). However, the shortest path between u and v does not necessarily belong to the MST (Statement II is false, as a direct edge with weight 10 might be bypassed in MST via edges of weights 2, 3, 4, 3 = 12).

- **A:** True: unique MST guaranteed by distinct edge weights, while shortest path tree differs from MST.
- **B:** False: Statement II fails on simple cyclic counterexamples.
- **C:** False: Statement II is false.
- **D:** False: Statement I is true.

**Common misconception:** Confusing Minimum Spanning Tree (minimizes total edge sum) with Shortest Path Tree (minimizes source-to-vertex path lengths).

## Q34

**Correct answer:** A

**Concept:** Digital Logic — Fixed-point arithmetic

Sign bit = 1 (negative). Exponent = 10000001_2 = 129; 129 - 127 = 2. Mantissa = 1.0000... (implicit 1 + 0). Value = -1 * 2^2 * 1.0 = -4.0.

- **A:** True: negative sign, exponent 2, normalized mantissa 1.0 = -4.0.
- **B:** False: incorrect exponent bias subtraction.
- **C:** False: sign bit ignored.
- **D:** False: inverted exponent scaling.

**Common misconception:** Forgetting the implicit leading 1 in normalized IEEE 754 mantissa.

## Q35

**Correct answer:** 1.33 (exact)

**Concept:** Engineering Mathematics — Integration

Integral = [x^3/(3) + 2x²/2] evaluated from 0 to 1 = 1/3 + 2/2 = 1.33.

**Common misconception:** Applying derivative power rule instead of antiderivative.

## Q36

**Correct answer:** A

**Concept:** Algorithms — Shortest paths

Distinct edge weights guarantee a unique MST (Statement I is true). However, the shortest path between u and v does not necessarily belong to the MST (Statement II is false, as a direct edge with weight 10 might be bypassed in MST via edges of weights 2, 3, 4, 3 = 12).

- **A:** True: unique MST guaranteed by distinct edge weights, while shortest path tree differs from MST.
- **B:** False: Statement II fails on simple cyclic counterexamples.
- **C:** False: Statement II is false.
- **D:** False: Statement I is true.

**Common misconception:** Confusing Minimum Spanning Tree (minimizes total edge sum) with Shortest Path Tree (minimizes source-to-vertex path lengths).

## Q37

**Correct answer:** A

**Concept:** Algorithms — Searching and sorting

Merge Sort divides the array into halves in Θ(1), recursively sorts them in 2T(n/2), and merges in at most n-1 comparisons. By Master Theorem, T(n) = 2T(n/2) + Θ(n) = Θ(n log n) in all cases (best, average, and worst).

- **A:** True: worst-case comparison complexity is strictly Θ(n log n).
- **B:** False: quadratic time applies to Quick Sort worst-case, not Merge Sort.
- **C:** False: lower bound for comparison sort is Ω(n log n).
- **D:** False: sublinear sorting is impossible.

**Common misconception:** Confusing Merge Sort's invariant worst-case with Quicksort's unbalanced partition worst-case.

## Q38

**Correct answer:** A

**Concept:** Operating Systems — Virtual memory

Page size 4 KiB = 2^12 bytes, so 32 - 12 = 20 bits for virtual page number (2^20 = 1,048,576 pages). Total size = 2^20 entries * 4 bytes = 4 MiB.

- **A:** True: 2^20 pages * 4 bytes/entry = 4 MiB.
- **B:** False: miscalculated number of virtual pages.
- **C:** False: subtracted offset bits incorrectly.
- **D:** False: doubled entry width.

**Common misconception:** Forgetting to convert byte capacity to MiB correctly.

## Q39

**Correct answer:** A

**Concept:** Compiler Design — Common subexpression elimination

Local common subexpression elimination operates strictly within the boundaries of a single basic block and requires no control-flow or interprocedural information.

- **A:** True: intra-basic-block optimization requires only local value numbering.
- **B:** False: requires global interprocedural call-graph analysis.
- **C:** False: requires link-time whole-program analysis.
- **D:** False: requires closed-world object hierarchy analysis.

**Common misconception:** Assuming basic block optimizations require knowledge of entire program control flow.

## Q40

**Correct answer:** 3 (exact)

**Concept:** Computer Networks — MAC and Ethernet

The degree of the generator polynomial G(x) is 3 (highest power of x is 3). The appended CRC checksum length is always equal to the degree of G(x), which is 3 bits.

**Common misconception:** Confusing number of polynomial coefficients (which is degree + 1) with remainder length.

## Q41

**Correct answer:** A

**Concept:** Operating Systems — File systems

By definition, a state is safe if there exists a safe sequence of processes <P1, P2, ..., Pn> such that for each Pi, the resources Pi can still request can be satisfied by current available resources plus resources held by all preceding processes Pj (j < i).

- **A:** True: standard formal definition of safe state in Banker's algorithm.
- **B:** False: fully allocated resources often lead to unsafe states.
- **C:** False: irrelevant single-resource restriction.
- **D:** False: Banker's algorithm is proactive avoidance, not recovery.

**Common misconception:** Confusing an unsafe state with an active deadlock (all deadlocks are unsafe, but not all unsafe states are deadlocked).

## Q42

**Correct answer:** A

**Concept:** Compiler Design — Lexical analysis

Maximal munch parses: `x` (identifier), `==` (equality operator), `=` (assignment operator), `y` (identifier). Exactly 4 tokens.

- **A:** True: tokens are [x], [==], [=], [y] = 4 tokens.
- **B:** False: undercounts separate operators.
- **C:** False: splits equality operator into single equals.
- **D:** False: character-level tokenization.

**Common misconception:** Grouping three consecutive '=' signs as a single invalid token instead of greedy matching '==' then '='.

## Q43

**Correct answer:** A (exact)

**Concept:** Computer Organization and Architecture — Interrupts and DMA

One DMA cycle takes 200 ns (0.2 µs) every 2.0 µs. Percentage = (0.2 / 2.0) * 100 = 10%.

**Common misconception:** Confusing burst mode transfer with cycle-stealing transfer mode.

## Q44

**Correct answer:** A

**Concept:** Compiler Design — Parsing

S derives 'b' directly, so b ∈ FIRST(S). S -> A a derives FIRST(A) followed by a. A -> c, so c ∈ FIRST(A). S d derives FIRST(S)d (recursive). Thus FIRST(S) = {c, b}.

- **A:** True: FIRST(S) contains terminal b and FIRST(A) which includes c.
- **B:** False: terminal a is trailing, not in FIRST.
- **C:** False: d is trailing suffix.
- **D:** False: omitted indirect derivation through A.

**Common misconception:** Including trailing terminals in FIRST sets.

## Q45

**Correct answer:** A

**Concept:** Digital Logic — Floating-point representation

Sign bit = 1 (negative). Exponent = 10000001_2 = 129; 129 - 127 = 2. Mantissa = 1.0000... (implicit 1 + 0). Value = -1 * 2^2 * 1.0 = -4.0.

- **A:** True: negative sign, exponent 2, normalized mantissa 1.0 = -4.0.
- **B:** False: incorrect exponent bias subtraction.
- **C:** False: sign bit ignored.
- **D:** False: inverted exponent scaling.

**Common misconception:** Forgetting the implicit leading 1 in normalized IEEE 754 mantissa.

## Q46

**Correct answer:** A (exact)

**Concept:** Programming and Data Structures — Graph representations

To output 3 first, 1 and 2 must be pushed before 3. Once 3 is popped, 2 is at the top of the stack and MUST be popped before 1. Thus '3, 1, 2, 4' is impossible.

**Common misconception:** Assuming any arbitrary permutation of stack inputs can be generated.

## Q47

**Correct answer:** A

**Concept:** Algorithms — Hashing

Merge Sort divides the array into halves in Θ(1), recursively sorts them in 2T(n/2), and merges in at most n-1 comparisons. By Master Theorem, T(n) = 2T(n/2) + Θ(n) = Θ(n log n) in all cases (best, average, and worst).

- **A:** True: worst-case comparison complexity is strictly Θ(n log n).
- **B:** False: quadratic time applies to Quick Sort worst-case, not Merge Sort.
- **C:** False: lower bound for comparison sort is Ω(n log n).
- **D:** False: sublinear sorting is impossible.

**Common misconception:** Confusing Merge Sort's invariant worst-case with Quicksort's unbalanced partition worst-case.

## Q48

**Correct answer:** A

**Concept:** Digital Logic — Boolean algebra

Groupings: corners m(0,2,8,10) give B'D'; sub-cube m(5,7,13,15) gives BD. Both are essential prime implicants and cover all 8 minterms. Minimum EPI count is 2.

- **A:** True: B'D' and BD form the minimal unique cover of essential terms.
- **B:** False: redundant grouping.
- **C:** False: overcounts non-essential implicants.
- **D:** False: single term cannot cover disjoint cubes.

**Common misconception:** Failing to recognize wrap-around corner minterms in 4-variable K-maps.

## Q49

**Correct answer:** A (exact)

**Concept:** Operating Systems — System calls

By definition, a state is safe if there exists a safe sequence of processes <P1, P2, ..., Pn> such that for each Pi, the resources Pi can still request can be satisfied by current available resources plus resources held by all preceding processes Pj (j < i).

**Common misconception:** Confusing an unsafe state with an active deadlock (all deadlocks are unsafe, but not all unsafe states are deadlocked).

## Q50

**Correct answer:** A

**Concept:** Theory of Computation — Regular and context-free languages

States represent longest prefix matched of `011`: q0 (empty), q1 (`0`), q2 (`01`), q3 (`011`, accepting). Exactly 4 pairwise distinguishable states by Myhill-Nerode theorem.

- **A:** True: exactly 4 states are necessary and sufficient.
- **B:** False: cannot distinguish prefixes `01` and `011`.
- **C:** False: non-minimal DFA.
- **D:** False: NFA powerset bound without minimization.

**Common misconception:** Assuming NFA state count equals minimal DFA state count.

## Q51

**Correct answer:** A

**Concept:** Databases — Transactions

A non-root internal node in a B+ tree of order m must have at least ⌈m/2⌉ child pointers. For m=5, ⌈5/2⌉ = 3 children, which corresponds to 3 - 1 = 2 keys.

- **A:** True: ⌈5/2⌉ - 1 = 3 - 1 = 2 keys minimum.
- **B:** False: maximum number of keys for 3 children.
- **C:** False: maximum capacity (m-1 = 4).
- **D:** False: root minimum keys, not general internal node.

**Common misconception:** Confusing child pointer minimum ⌈m/2⌉ with key count minimum (⌈m/2⌉ - 1).

## Q52

**Correct answer:** 2 (exact)

**Concept:** Digital Logic — Karnaugh maps

Groupings: corners m(0,2,8,10) give B'D'; sub-cube m(5,7,13,15) gives BD. Both are essential prime implicants and cover all 8 minterms. Minimum EPI count is 2.

**Common misconception:** Failing to recognize wrap-around corner minterms in 4-variable K-maps.

## Q53

**Correct answer:** A

**Concept:** Theory of Computation — Pumping lemma

{ a^n b^n c^n | n ≥ 0 } requires simultaneous comparison of three independent block counts, which cannot be tracked by a single pushdown stack; proven non-CFL via Ogden's/pumping lemma.

- **A:** True: canonical non-context-free language.
- **B:** False: deterministic context-free language.
- **C:** False: context-free palindromic language.
- **D:** False: context-free language with unequal counts.

**Common misconception:** Assuming pushdown automata can count three distinct symbol groups simultaneously.

## Q54

**Correct answer:** A (exact)

**Concept:** Databases — Concurrency control

A non-root internal node in a B+ tree of order m must have at least ⌈m/2⌉ child pointers. For m=5, ⌈5/2⌉ = 3 children, which corresponds to 3 - 1 = 2 keys.

**Common misconception:** Confusing child pointer minimum ⌈m/2⌉ with key count minimum (⌈m/2⌉ - 1).

## Q55

**Correct answer:** A (exact)

**Concept:** Databases — ER model

A non-root internal node in a B+ tree of order m must have at least ⌈m/2⌉ child pointers. For m=5, ⌈5/2⌉ = 3 children, which corresponds to 3 - 1 = 2 keys.

**Common misconception:** Confusing child pointer minimum ⌈m/2⌉ with key count minimum (⌈m/2⌉ - 1).

## Q56

**Correct answer:** 80 (exact)

**Concept:** Programming and Data Structures — C programming and pointers

arr+1 points to arr[1]=20. *(p+2) is arr[3]=40. q points to arr[4]=50. *(q-1) is arr[3]=40. Sum = 40 + 40 = 80.

**Common misconception:** Confusing 0-based array base address addition with dereferencing.

## Q57

**Correct answer:** A

**Concept:** Programming and Data Structures — Recursion

To output 3 first, 1 and 2 must be pushed before 3. Once 3 is popped, 2 is at the top of the stack and MUST be popped before 1. Thus '3, 1, 2, 4' is impossible.

- **A:** True: violating LIFO ordering constraint for elements below 3.
- **B:** False: legally obtainable permutation.
- **C:** False: trivial immediate pop permutation.
- **D:** False: reverse stack drain permutation.

**Common misconception:** Assuming any arbitrary permutation of stack inputs can be generated.

## Q58

**Correct answer:** A (exact)

**Concept:** Computer Organization and Architecture — Pipelining and hazards

One DMA cycle takes 200 ns (0.2 µs) every 2.0 µs. Percentage = (0.2 / 2.0) * 100 = 10%.

**Common misconception:** Confusing burst mode transfer with cycle-stealing transfer mode.

## Q59

**Correct answer:** 125 (exact)

**Concept:** Engineering Mathematics — Descriptive statistics

By Cayley's formula, the number of labelled spanning trees on n vertices is n^(n-2). For n=5, 5^(5-2) = 125.

**Common misconception:** Confusing total edges in complete graph with spanning tree count.

## Q60

**Correct answer:** A

**Concept:** Computer Organization and Architecture — Instruction sets and addressing modes

One DMA cycle takes 200 ns (0.2 µs) every 2.0 µs. Percentage = (0.2 / 2.0) * 100 = 10%.

- **A:** True: (0.2 µs / 2.0 µs) = 10% memory bus duty cycle.
- **B:** False: miscalculated word transfer interval.
- **C:** False: doubled transfer overhead.
- **D:** False: unit conversion error.

**Common misconception:** Confusing burst mode transfer with cycle-stealing transfer mode.

## Q61

**Correct answer:** A

**Concept:** Engineering Mathematics — Monoids and groups

By Cayley's formula, the number of labelled spanning trees on n vertices is n^(n-2). For n=6, 6^(6-2) = 1296.

- **A:** True by Cayley's tree enumeration theorem.
- **B:** False: counts edges, not spanning trees.
- **C:** False: wrong exponent (n-1).
- **D:** False: squared vertex count.

**Common misconception:** Confusing total edges in complete graph with spanning tree count.

## Q62

**Correct answer:** 3 (exact)

**Concept:** Computer Networks — Distance-vector and link-state routing

The degree of the generator polynomial G(x) is 3 (highest power of x is 3). The appended CRC checksum length is always equal to the degree of G(x), which is 3 bits.

**Common misconception:** Confusing number of polynomial coefficients (which is degree + 1) with remainder length.

## Q63

**Correct answer:** A

**Concept:** Theory of Computation — Turing machines and undecidability

By Rice's Theorem and the Halting Problem, all nontrivial semantic properties of languages recognized by Turing machines (halting, emptiness, equivalence) are undecidable.

- **A:** True: all listed problems are undecidable by Rice's theorem.
- **B:** False: equivalent to the Halting problem (undecidable).
- **C:** False: emptiness problem for TMs is undecidable.
- **D:** False: equivalence problem for TMs is undecidable.

**Common misconception:** Confusing decidable properties of DFAs (emptiness, equivalence) with those of Turing machines.

## Q64

**Correct answer:** A

**Concept:** Engineering Mathematics — Graph connectivity matching and colouring

By Cayley's formula, the number of labelled spanning trees on n vertices is n^(n-2). For n=6, 6^(6-2) = 1296.

- **A:** True by Cayley's tree enumeration theorem.
- **B:** False: counts edges, not spanning trees.
- **C:** False: wrong exponent (n-1).
- **D:** False: squared vertex count.

**Common misconception:** Confusing total edges in complete graph with spanning tree count.

## Q65

**Correct answer:** A

**Concept:** Engineering Mathematics — Counting

By Cayley's formula, the number of labelled spanning trees on n vertices is n^(n-2). For n=4, 4^(4-2) = 16.

- **A:** True by Cayley's tree enumeration theorem.
- **B:** False: counts edges, not spanning trees.
- **C:** False: wrong exponent (n-1).
- **D:** False: squared vertex count.

**Common misconception:** Confusing total edges in complete graph with spanning tree count.

