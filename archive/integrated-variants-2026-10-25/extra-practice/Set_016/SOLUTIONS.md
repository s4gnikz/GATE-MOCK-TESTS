# Worked Solutions — Additional Practice Set 016

## Q1

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

1. Key 10 occupies slot 3. Key 17 probes 3 then 6; key 24 probes 3 then 1. Deleting 10 leaves a tombstone at 3.
2. Search for 24 visits 3 and then 1; stopping at 3 would miss it.
3. Tombstones are reusable on insertion. Key 31 starts at 3, so that slot is a possible insertion location after confirming absence. Capacity is not permanently lost.
- Original option A: Its probe sequence reaches slot 1 only after slot 3.
- Original option B: A never-used marker would incorrectly terminate search for 24.
- Original option C: Tombstones retain search chains while remaining available for reuse.
- Original option D: The tombstone may hold a later key, restoring all seven slots as potential capacity.

## Q2

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Original needs are P0=(1,2), P1=(1,1), P2=(2,0). With available (1,1), P1 can finish, releasing (0,1), so work becomes (1,2). P0 can then finish, releasing (1,0), making (2,2); P2 then finishes. Thus the original state is safe. Tentatively grant (0,1) to P0: available becomes (1,0), and P0's need becomes (1,1). P1 still needs (1,1) and P2 needs (2,0). No process can finish with (1,0), so the tentative state is unsafe and the request must be deferred. Unsafe does not by itself assert that deadlock has already occurred.
- Original option A: False: after the grant P0 needs one B, but no B is available.
- Original option B: False: P2 needs two A, but only one A is available.
- Original option C: True: the original safe sequence exists, while no process can start the tentative safety reduction.
- Original option D: False: P1,P0,P2 is a safe sequence in the original state.

## Q3

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Engineering Mathematics — LU decomposition

1. Eliminate column 1 to obtain rows [1,2,1], [0,t-4,1], [0,1,0]. Expanding along column 1 gives determinant -1 for every t.
2. At t=4 the second pivot is zero while the entry below it is 1. In any unit-lower LU decomposition the forced leading U block would have U22=0, making the required A32 residual impossible. Row exchange fixes this, giving trailing block diag(1,1).
3. At t=5, the second pivot is 1 and eliminating the last row gives U33=-1, not 1.

- **A:** The trailing 2-by-2 determinant is (t-4)*0-1=-1.
- **B:** Nonsingularity does not ensure all unpivoted pivots exist; t=4 is a counterexample.
- **C:** The swapped trailing rows are [1,0] and [0,1].
- **D:** The last elimination subtracts the second trailing row and produces -1.

**Common misconception:** An invertible matrix may still require pivoting for a particular elimination order.

## Q4

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Databases — Concurrency control

Each upgrade needs an exclusive lock, which is incompatible with the other transaction's shared lock. Neither shared lock is released until commit, and neither transaction can progress to commit, so a deadlock is possible. Retaining exclusive locks until commit still prevents dirty reads by other properly locking transactions.

A correctly states both facts. B confuses compatibility of existing shared locks with compatibility of an exclusive upgrade. C is false: releasing the shared lock enters the shrinking phase, so later acquiring an exclusive lock violates two-phase locking. D is false: acquiring an exclusive lock before the read serializes the entire read-modify-write operation, preventing a lost update.

- **A:** True: deadlock is possible due to incompatible lock upgrades, but strict 2PL prevents dirty reads.
- **B:** False: confuses compatibility of existing shared locks with compatibility of exclusive lock upgrades.
- **C:** False: releasing a lock enters the shrinking phase, so later acquiring an exclusive lock violates two-phase locking.
- **D:** False: acquiring an exclusive lock before reading serializes transactions, preventing lost updates.

**Common misconception:** A serializability or recovery guarantee does not imply deadlock freedom.

## Q5

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Linear probing and deletion markers.

All inserted keys hash to 3, occupying indices 3,4,5. Deleting 17 leaves a tombstone at 4. Searching 24 examines 3,4,5: three probes. The known-absent 31 then occupies tombstone 4. A and D stop the search too early; C ignores the reusable tombstone.

**Common misconception:** A tombstone may be reused by insertion but cannot terminate a lookup chain.

## Q6

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Repeated rounding and grouping.

In [8,16), four significant binary bits give spacing 1. Thus 8.5 is a midpoint between 8 and 9 and rounds to even significand 8. Every sequential addition returns to 8, proving A and disproving C. Real arithmetic gives 8+16×0.5=16, proving B. Adding 2 four times gives exactly representable 10,12,14,16, proving D.

**Common misconception:** A small representable addend can disappear when added to a larger representable number.

## Q7

**Correct answer:** B, D

The underlying question is correctly answered by A, C. This variant asks for its invalid answers, so select the complementary set: B, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Availability of expressions across calls.

If neither operand can change, the expression value is preserved. A guarantees inaccessible unchanged locals; C supplies a direct effect proof. Unknown effects on mutable globals make B insufficient. D ignores definitions and side effects. Thus A,C hold.

**Common misconception:** Textual equality is only part of common-subexpression eligibility; intervening modifications matter.

## Q8

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Lossy decomposition of ternary relationships.

All three original tuples survive. Their projections additionally support (s1,p1,j2): each of its three pairs appears somewhere. No other new tuple is possible: s2 has only p1 and j2, and pair (p2,j1) is absent. The join therefore has four tuples. Each original SP pair appears once and determines J. A,B,D hold; the spurious tuple itself refutes C.

**Common misconception:** Pairwise compatibility does not prove that a three-way combination occurred in the original relation.

## Q9

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Cut property of minimum spanning trees.

If a spanning tree omitted a uniquely lightest cut edge e, adding e creates a cycle containing another cut-crossing edge of strictly greater weight. Exchanging them lowers total weight, contradicting minimality. Thus C holds. Tied weights do not necessarily create alternative MSTs (A); a maximum-weight bridge must be included (B); Kruskal can break ties arbitrarily and remains correct (D).

**Common misconception:** Global distinctness of all weights is stronger than the local uniqueness needed by this cut argument.

## Q10

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Concession in sentence structure.

The acceptance occurs despite a concern; “notwithstanding” supplies that concessive meaning and takes the following noun phrase. “Because” would require a different grammatical construction here and changes the intended relation. “Therefore” and “consequently” express consequence, not concession, and do not fit before this noun phrase. B is correct.

**Common misconception:** A word can signal a logical relation without fitting the grammatical structure of the blank.

## Q11

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** A reduction must preserve a distinguishing yes/no condition.

If M halts on w, N accepts every input, so L(N)=Σ*. Otherwise N accepts none, so L(N)=∅. Both are regular, and a regularity test answers yes in either case; B identifies the failure. The construction merely simulates M and needs no advance halting knowledge, refuting A. C is the opposite of the actual outcomes, and D incorrectly forbids standard simulation.

**Common misconception:** Encoding halting into a machine's behaviour is not enough; the target property must distinguish the two cases.

## Q12

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** CHECK and SQL UNKNOWN.

A CHECK rejects FALSE, but accepts TRUE or UNKNOWN. Positive integers make x>0 TRUE; NULL makes it UNKNOWN. Zero and negative integers make it FALSE. Thus B is correct, A incorrectly rejects NULL, and C,D incorrectly admit FALSE cases.

**Common misconception:** A CHECK predicate alone is not a NOT NULL constraint.

## Q13

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Quadratic scaling.

Both areas are proportional to the square of the changed linear dimension. Multiplying that dimension by 1.1 multiplies area by 1.21, a 21% increase. C is correct. A,D confuse linear and area scaling; B omits the additional 0.1² term.

**Common misconception:** Percentage changes in length and area are not equal.

## Q14

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Uses before overwrites.

The first x value is used immediately in y=x*c before being overwritten, and y is then returned. Neither definition is dead, so C holds. A,D ignore the intervening use of x; B ignores return y. The later x=0 may itself be dead under the stated observability assumption, but that is not one of the two assignments asked about.

**Common misconception:** A later overwrite does not kill earlier uses that already consumed the previous value.

## Q15

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** TCP connection demultiplexing.

For these IPv4 TCP connections, both endpoint addresses and ports identify the connection, so C holds and distinct remote endpoints can distinguish them, as A states. A listening service routinely retains the same local endpoint for many established connections, refuting B and D.

**Common misconception:** Treating the server's port as the entire connection identity.

## Q16

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Probe-cycle length.

The visited slots are 1,5,9,3,7, then 1 again. The period is 10/gcd(10,4)=5. Hence B holds: empty even slots cannot be reached. A and C give incorrect period lengths. D is false because the arithmetic sequence is independent of table contents.

**Common misconception:** Assuming every nonzero step visits the entire table.

## Q17

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Unfolding as reflection.

Folding superposes a point and its reflection across the crease, so the punch produces that reflected pair. A holds. The punch is away from the fold, refuting B. Separation depends on distance from the fold, refuting C. A general reflected pair is not a quarter-turn pair, refuting D.

**Common misconception:** Replacing reflection by rotation.

## Q18

**Correct answer:** D

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Removing necessary deadlock conditions.

A imposes one resource order and rules out a circular wait. B prevents hold-and-wait because an unsuccessful acquisition holds neither resource. C changes scheduling priority but cannot supply the blocked resource. D explicitly allows the original hold-and-wait cycle. Thus only A and B guarantee prevention here.

**Common misconception:** Expecting CPU scheduling changes to resolve a resource cycle.

## Q19

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Universal decomposition requirement in a CFL pumping proof.

For a claimed pumping length, choose an appropriate long word, then show that every valid decomposition has some pumping exponent leaving the language. B states the needed decomposition range. A restricts it incorrectly, C violates |vy|>0, and D omits the central proof obligation.

**Common misconception:** Choosing a convenient decomposition that the pumping property never promised would work.

## Q20

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** One-past pointers versus dereferencing.

p=a+3 may be formed, but not dereferenced. Moving back one gives a+2, whose value is seven, so B is valid. A and D access one-past storage; C goes farther out of the permitted array-pointer range and dereferences it.

**Common misconception:** Treating permission to form a one-past pointer as permission to access an element there.

## Q21

**Correct answer:** C

Candidates I, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) IV.
- **B: Incorrect.** It includes invalid candidate(s) II, III and omits valid candidate(s) I, IV.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Tabular combination conditions.

A has identical dash positions and differs only in the final bit, combining to 01-1-. D differs only in its first bit with matching dashes, combining to ---10. B has different dash positions. C differs in two nondash bits, first and last. Therefore only A and D qualify in one step.

**Common misconception:** Comparing only numbers of dashes instead of their positions and all remaining bits.

## Q22

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Boolean absorption and redundancy.

Expanding gives x+xy+xz+yz=x+yz, proving A. Whenever F=1, either x=1 or y=z=1, so x+y+z=1; multiplying by that redundant factor preserves F, proving C. At x=0,y=z=1, F=1 while B and D are zero, refuting both.

**Common misconception:** Distributing without applying absorption, or forgetting the yz term.

## Q23

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Atomicity of an invariant-preserving update sequence.

The pair may be inconsistent after the first update and before the second. If that interval is unprotected, another thread can observe it, giving A. B,C,D make false claims about mutex capabilities or implicit atomicity.

**Common misconception:** Protecting individual assignments while leaving the multi-field invariant temporarily exposed.

## Q24

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: pivoting in LU decomposition. det(A)=−1, so A is nonsingular (A true). Write L=[[1,0],[l,1]] and U=[[u,v],[0,w]]. From the first row u=0,v=1, but then (LU)21=lu=0, contradicting A21=1; B is false. Swapping rows gives the identity, factored as I·I, so C is true. This nonsingular matrix itself disproves D. Invertibility does not guarantee a nonzero first pivot.

## Q25

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: semaphore acquisition order. Consumer can hold mutex while waiting on initially zero full; producer then waits for that mutex and cannot insert/signall full (A). Code containing signal operations does not make them reachable, so B is false. Waiting for an available item before acquiring mutex removes this circular acquisition order (C). full must initially count zero available items; setting it to N misrepresents the empty buffer (D false). A resource should not be held while waiting for the condition that needs another process to acquire it.

## Q26

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: sparse expensive iterations. The inner loop runs only at i=1,2,4,...,2^m where 2^m≤n<2^(m+1). Its total work is 1+2+...+2^m=2^(m+1)−1, between n and 2n. The outer loop also costs Θ(n), so C. A counts only trigger events, B charges an average logarithmic inner cost to every iteration, and D treats the expensive loop as running for every i. Sum actual executed lengths rather than multiplying syntactic bounds.

## Q27

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: stream EOF versus datagram length. TCP zero after draining input denotes orderly incoming EOF, so A. A valid UDP datagram can have empty payload and yield zero without stream-style EOF, so C. TCP is a byte stream: B and D incorrectly assert preservation of application message/write boundaries. Interpret a return value with the socket's transport semantics.

## Q28

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: contextual meanings and qualification. D uses impartial for disinterested, approved for sanctioned, and retains criticism of cost. A changes both meanings; B reverses approval and criticism; C incorrectly treats impartiality as loss of interest. Approval of a procedure need not endorse every aspect of it.

## Q29

**Correct answer:** C

Candidates II, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) IV.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) I, III and omits valid candidate(s) II, IV.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: sortable floating-point bit keys. Positive encodings grow with magnitude, so B. Negative raw encodings also grow with magnitude but that makes their numerical values smaller, disproving C. Raw unsigned ordering puts positive encodings before negative ones, disproving A. Complementing negatives reverses their magnitude order and places them below 0x80; flipping the sign bit of positives places them above. Thus D preserves increasing numeric order for the specified finite nonzero values. Excluding NaNs and signed-zero ties is important to the stated strict comparison.

## Q30

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Stable least-significant-key-first sorting preserves the year order within each city and retains arrival order for exact ties, so A is true. Explicitly restoring arrival order before the same two stable passes also works, so C is true. B makes year the primary key and can interleave cities incorrectly. D can destroy arrival order for equal keys, and a later stable city sort will preserve that damage. Stability matters for ties, not just for the primary ordering.

## Q31

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

B rechecks the predicate while holding the mutex after every wakeup. A fails on a spurious wakeup or when another thread consumes the condition first. C races with changes to ready. D can prevent another process from acquiring the mutex to make ready true. A wakeup is a reason to recheck, not proof of the predicate.

## Q32

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The only walk from s to t uses s→t and costs5. Vertex a cannot reach t, so its negative loop cannot affect this destination. A and C are true; D is false. Walk costs from s to a decrease without bound through repeated self-loops, disproving B. A negative cycle matters to a destination only if it can also reach that destination.

## Q33

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Threads in one process share its virtual address space and conventional descriptor table, so A and C are true and B false. Each thread still needs a separate execution context and ordinarily a separate stack, making D true. Shared resources require synchronization; sharing does not imply identical instruction pointers or stack contents.

## Q34

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Different source addresses make the supplied context keys different, proving A and disproving B. Once the context is identified, offset locates a payload piece within it, so C is true. Fragments may be interleaved and reordered; arrival order does not replace the supplied key, making D false. Identification values are not globally unique across senders.

## Q35

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The aS production adds an unmatched leading a; aSbS adds a matched enclosing pair around the first S and then a valid suffix. Structural induction shows no generated prefix has more b's than a's, proving B and hence A. ba violates that prefix condition, disproving C. Derive aab via S→aS→aaSbS→aab using epsilon subderivations, proving D.

## Q36

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

One A is free, so Q can obtain it, finish and release B; P then obtains B. B is correct and C,D false. With multiple instances, a resource-allocation cycle alone need not establish deadlock, disproving A.

## Q37

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

If f mapped two distinct A elements together, their compositions would coincide, contradicting injectivity; A follows. Distinct points of f(A) also cannot be identified by g, proving C. g may identify points outside that image without affecting the composition, so B is not necessary. For example, embedding a smaller set in B need not be onto, disproving D.

## Q38

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Substitute z=y: F=xy+(NOT x)y=y(x+NOT x)=y. Thus D is correct. A depends on an unrelated selector, B complements the required value, and C changes with x. When a multiplexer's two data inputs agree, its selector cannot affect its output.

## Q39

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Lexical scope identifies Outer regardless of which procedure calls Inner, so the static link in B locates the intended activation. A follows call history to Caller. C follows recency without lexical meaning. D cannot by itself locate a non-global activation's local x. Dynamic and static nesting need not coincide.

## Q40

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Adding e to a spanning tree creates a cycle. Because e crosses the cut, the cycle must cross back via another edge, proving C. If an MST omitted e, replacing that other crossing edge by the uniquely lighter e would reduce total weight, proving A. Lighter edges may exist within one side of the cut, refuting B. Equal-weight alternatives elsewhere may give multiple MSTs, refuting D. A forced edge does not force every other edge.

## Q41

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

C cannot be derived, so keys must contain it. A or B then determines the other, giving candidate keys AC,BC; A true and B false. Every attribute is prime, so the dependencies satisfy3NF, proving C. A and B individually are not superkeys, violating BCNF, refuting D. Prime right-hand attributes can permit3NF without BCNF.

## Q42

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

On an input-consuming PDA step, update the DFA with the same symbol, proving A. A PDA epsilon step changes only the PDA component and leaves the DFA state unchanged, refuting B. The finite DFA state is stored in the finite product control; the original stack suffices, proving C and refuting D. Acceptance must require the PDA's acceptance condition and an accepting DFA state after the input is consumed.

## Q43

**Correct answer:** A

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

For NULL, x>0 is UNKNOWN, which this CHECK accepts, proving A and refuting C. A non-NULL integer passes exactly when it is positive, proving B. NOT NULL would exclude the previously permitted NULL, refuting D. SQL CHECK acceptance differs from WHERE filtering of UNKNOWN.

## Q44

**Correct answer:** B

Candidates III, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) I, II and omits valid candidate(s) III, IV.
- **D: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) IV.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Equality2a+b=2a+c gives b=c, proving C. Both sides of D equal2a+b+c. In A, the two sides are4a+2b+c and2a+2b+c, not equal for arbitrary a. In B,2a+b and2b+a need not agree. A familiar-looking operator need not inherit addition's algebraic properties.

## Q45

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A selects a subset of finite R. C is exactly membership in R because its witness must equal x, so it too is finite. B is the complement of the finite union R∪S and is infinite. D is true for every x when S is empty, hence need not be finite. Quantifying over an empty relation can turn a universal condition into an unbounded result.

## Q46

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

x−x is always exactly zero within range, and x*0 likewise, so A,C preserve value and do not remove possible traps. B removes the divide-by-zero trap when x=0. D removes a possible overflow trap in x+1 at the maximum integer, even though the algebraic result would be x. Algebraic identities require attention to the stated arithmetic semantics.

## Q47

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The Boolean matrix merges all parallel edges into one true entry, losing multiplicities(A,D). Therefore its row sum can undercount outdegree, disproving B. Parallel-edge multiplicity does not change whether a path exists, so collapsing them preserves reachability(C). Multiplicity matters for degrees and edge counts even when it does not matter for reachability.

## Q48

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

A younger result waits in the reorder buffer until all preceding instructions can commit, allowing precise architectural state at an older exception(A). Early issue and additional execution units(B,C) affect execution timing but do not enforce visibility ordering. Branch-direction prediction(D) does not establish exception ordering.

## Q49

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Simulating at most k transitions decides both bounded questions, with the initial-state acceptance test included for C. The computation is finite even when M would run forever. B is the unrestricted halting problem; D is the general Turing-machine language-emptiness problem. Both are undecidable. A finite bound changes the decision problem fundamentally.

## Q50

**Correct answer:** A

The underlying question is correctly answered by B, C, D. This variant asks for its invalid answers, so select the complementary set: A.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

If both threads read the same value before either writes at each round, updates are lost and the final value is 2. Serial execution gives 4. For 3, let both first reads see 0, let both write 1, then execute each second increment serially. These establish B,C,D. Every second write is based on a read after that thread's first write; all first writes are at least 1 and no later write can be 0. Hence every second write is at least 2. A final value 1 is impossible because the last write belongs to a thread's second increment. Atomic individual accesses do not make the increment atomic.

