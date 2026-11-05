# Worked Solutions — Additional Practice Set 007

## Q1

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

1. In Bag I, P(RR)=6/15 and P(same)=7/15. In Bag II, P(RR)=1/10 and P(same)=4/10.
2. Before conditioning, P(RR)=(1/2)(6/15+1/10)=1/4, and P(same)=(1/2)(7/15+4/10)=13/30.
3. Since RR is a subset of same, P(RR | same)=(1/4)/(13/30)=15/26.
- Original option A: Conditioning on same does not leave red and blue equally likely.
- Original option B: The ratio of the mixture probabilities is 15/26.
- Original option C: This is not the ratio P(RR)/P(same).
- Original option D: Conditioning cannot be replaced by the initial proportion in a bag.

## Q2

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Q cannot observe EOF on X while R keeps its writer open, even though R never writes. Hence Q cannot close Y, P cannot finish its read on Y, and R cannot finish waiting for P. Closing R's X writer before its wait breaks this cycle: P closes the remaining X writer; Q consumes X and sees EOF, writes/closes Y and terminates; P consumes Y and sees EOF and terminates; R's wait returns and R terminates. Buffer capacity cannot repair the original dependency cycle.
- Original option A: False: descriptor ownership, not capacity, prevents EOF.
- Original option B: False: it introduces or preserves a wait cycle.
- Original option C: True: closing the otherwise unused writer permits Q to see EOF, after which Q, P, and finally R can terminate.
- Original option D: False: it adds a termination dependency.

## Q3

**Correct answer:** B, D

The underlying question is correctly answered by A, C. This variant asks for its invalid answers, so select the complementary set: B, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** General Aptitude — Deductive logic

1. Since C is fifth, the positions of B and D must be {1,3} or {2,4}.
2. With B,D in {1,3}, A,E occupy {2,4} in either order; hence A can be fourth and need not precede E.
3. With B,D in {2,4}, E must be third and A first. Thus C is possible and D's claim of odd positions is false.

- **A:** For example B,E,D,A,C is valid.
- **B:** The same schedule places E before A.
- **C:** For example A,B,E,D,C is valid.
- **D:** The latter schedule has both B and D in even positions.

**Common misconception:** A claim of possibility needs one witness; a claim of necessity must survive every valid schedule.

## Q4

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Computer Networks — Network address translation

The NAT distinguishes the simultaneous connections using its assigned public ports. Its reverse mapping for 41002 restores destination address 10.0.0.2 and destination port 5000.

- **A:** is true by the stated mapping.
- **B:** is false: the server sees public source address 198.51.100.6 for both connections, with distinct source ports.
- **C:** is true: the source address is part of the IPv4 header covered by its header checksum.
- **D:** is true: the TCP checksum covers the TCP header, including the source port, and an IPv4 pseudoheader that includes the source and destination addresses.

**Common misconception:** A transport checksum can depend on network-layer addresses even though those addresses are not in the TCP header itself.

## Q5

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Reflection under folding.

Undoing the folds gives x coordinates 1 and 7 and y coordinates 3 and 5. The four holes are (1,3),(1,5),(7,3),(7,5). Opposite corners have distance √(6²+2²)=√40=2√10. A counts only the horizontal separation; C is the side length of the original sheet; D corresponds to a different diagonal.

**Common misconception:** A fold reflects a coordinate about its crease; it does not simply translate a hole by half the sheet width.

## Q6

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Pipe endpoint lifetime.

End-of-file requires the pipe buffer to be empty and every write-end reference to be closed. Child II still owns one, so the read blocks. A ignores that inherited reference. C is not stream-read behavior. D concerns writing to a pipe with no reader, not this read operation.

**Common misconception:** The process that supplied the data is not necessarily the only process keeping the pipe open.

## Q7

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Mean, median, mode and range.

The original sum is 2+9+7=18. Mean four after adding two x values gives 18+2x=32, hence x=7. The sorted data are 1,1,3,3,3,7,7,7. The middle pair is 3,3, so the median is 3; both 3 and 7 occur three times, so there is no unique mode. Range is 7−1=6. Thus A,B,D hold and C fails.

**Common misconception:** A mean change need not change the median, and a mode need not be unique.

## Q8

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Page replacement histories and the stack property.

FIFO fills 1,2,3; hits 1; replaces 1 by 4; hits 2; replaces 2 by 5: five faults. LRU's hit on 1 makes 2 least recent; 4 evicts 2, the next 2 evicts 3, and 5 evicts 1: six faults. A,B hold. One example cannot establish C. LRU's resident sets are nested as frame capacity grows, proving D.

**Common misconception:** A replacement policy with the stack property need not beat every other policy on every individual trace.

## Q9

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Local structure imposed by a regular expression.

Each 1 is introduced in a block 11; adjacent blocks may merge, but each resulting run has even length. Conversely, every even-length run can be partitioned into such blocks, separated by zeros. Thus A holds and 110011 is accepted (C). The string 101 has two 1s overall but two odd runs, refuting B and D.

**Common misconception:** Even parity over the entire string differs from even parity in every run.

## Q10

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Dovetailing and enumeration of recognizable languages.

Dovetailing eventually performs every finite number of steps of every started simulation, so each accepting computation is eventually found (A). If L is finite, other simulations may loop forever and there is no general way to detect that no further member will be found; B is false. With L empty no simulation accepts, so an infinite silent run is possible (C). Waiting for a nonmember to print never terminates, refuting D.

**Common misconception:** An enumeration is evidence of membership when an item appears, not evidence of nonmembership when it has not yet appeared.

## Q11

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Substitution into a sequential characteristic equation.

For J=K=0, Q′=Q, proving A. For J=K=1, Q′=NOT Q, proving B. For J=1,K=0, Q′=(NOT Q)+Q=1, so C is false. For J=0,K=1, both terms vanish, so D is true.

**Common misconception:** Force-set and force-reset inputs must be checked against the specified characteristic equation.

## Q12

**Correct answer:** B, D

The underlying question is correctly answered by A, C. This variant asks for its invalid answers, so select the complementary set: B, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Truth-value consistency.

If ON, the truth values are true,false,false: only one statement is true. If OFF, they are false,true,true: exactly two are true. Hence OFF is forced and B,C are truthful, proving A,C. B incorrectly includes A; D overlooks the consistent OFF assignment.

**Common misconception:** Evaluate a statement about another statement using the same candidate state.

## Q13

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Tail-call position.

In C, argument evaluation acc*n happens before the call, and the returned value is passed straight to the caller with no subsequent work. In A and B the caller must still add or multiply after f returns. In D, g must be called after f returns, so f is not the tail call being considered. Only C satisfies the stated eligibility condition for its recursive call.

**Common misconception:** An expression occurring after the word return is not necessarily a tail call.

## Q14

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Blocking versus busy waiting.

A blocked reader can be descheduled, requiring no polling CPU work (A). A writer's successful operation may enable it to resume (C). The writer's ability to make progress refutes necessary system deadlock (B), and it does not require the reader to be executing (D).

**Common misconception:** A blocked process is not synonymous with a deadlocked system.

## Q15

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Array size versus string termination.

The stored bytes are 'a', an explicit null, 'b', 'c', and the implicit terminating null: five bytes. strlen stops at the first null and returns one. A gets both values wrong; C counts through the embedded null; D omits the implicit terminator from the array size.

**Common misconception:** Treating every byte of a character array as part of its C string.

## Q16

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Isolation anomalies and locking.

Observing different committed values of the same row is a nonrepeatable read, establishing A. It need not involve uncommitted data, so B is false. A continuously held shared lock prevents a conflicting exclusive lock, establishing C under the given locking rules. Updating an existing row suffices; insertion is not required, so D is false.

**Common misconception:** Conflating a dirty read, a nonrepeatable read, and a phantom.

## Q17

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Precedence cycles and observed reads.

r1(X) before w2(X) gives T1→T2. r2(Y) before w1(Y) gives T2→T1. The cycle refutes both serial orders in A and B. In serial T1,T2, T2 reads Y=1; in serial T2,T1, T1 reads X=1, so neither reproduces both zero reads. Thus C holds. D overlooks read–write conflicts across transactions.

**Common misconception:** Checking only write–write conflicts.

## Q18

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Truth-table synthesis.

The possible values are 0,1,2,3. Exactly 2 and 3 are prime, and both have a=1, so A realizes the required function. B includes 1 and excludes 2; C includes 1 and excludes 3; D excludes prime 2.

**Common misconception:** Treating 1 as prime.

## Q19

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Pointer offsets and postfix increment.

p points to a[1]=4. Therefore *(p+1) is a[2]=6, giving B. A yields the old pointed-to value 4 before advancing p; C is 4+1=5; D is a[0]=2. Each option is evaluated independently from the stated declaration.

**Common misconception:** Confusing addition to the pointed-to value with addition to the pointer.

## Q20

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Mux selection and dependency.

Select 00 gives constant zero and select 11 constant one, both independent of x. Select 01 gives x and 10 gives its complement, both dependent. C lists exactly the correct settings. A and B omit one; D lists the dependent settings.

**Common misconception:** Treating inversion of an input as independence from that input.

## Q21

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Bounded pumping window across three symbol blocks.

A substring of length at most p cannot touch both an a and a c while also crossing the entire intervening block of p b symbols. Thus at least one symbol count is unaffected by pumping; some count changes because |vy|>0. Pumping can also disrupt order when a repeated mixed segment crosses a boundary. In either case the language condition fails, supporting B. A violates the nonempty pumped-part condition; C contradicts the chosen length 3p; D is unrelated.

**Common misconception:** Claiming the pumped parts necessarily lie inside one block, when they may straddle a boundary.

## Q22

**Correct answer:** B

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** B+ tree structural invariants.

Separators may copy leaf key values, so A holds. Balance keeps all leaves at one depth, giving B. Data entries are at leaves, refuting C; root occupancy has special exceptions, refuting D.

**Common misconception:** Importing ordinary B-tree data-placement rules unchanged into B+ trees.

## Q23

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Output dependencies under out-of-order completion.

Two writes to one register create a write-after-write hazard: the program-order younger value must remain final even if completion order differs. A names it. B involves no writes, C is unrelated to register naming, and D falsely classifies every write as a control transfer.

**Common misconception:** Considering only read-after-write dependencies.

## Q24

**Correct answer:** D

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Starvation under strict priority.

Persistent higher-priority work can always be selected first, establishing A. An aging policy that eventually raises a waiting job sufficiently can address that risk, B. Readiness alone gives no time bound under strict priority, refuting C; preemption does not create fairness, refuting D.

**Common misconception:** Equating eligibility to run with a guarantee of timely scheduling.

## Q25

**Correct answer:** A

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: CFG language and ambiguity. Productions create only a symbols, and repeated concatenation generates any number, including zero, so A holds. A tree for a can be wrapped as S→SS with one child deriving ε, repeatedly, producing infinitely many distinct trees; B holds. That also disproves C. An LL(1) grammar is unambiguous, and this grammar additionally has immediate left recursion, so D fails. Infinitely many derivations here correspond to genuinely different trees, not merely different expansion orders.

## Q26

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: quantifier order. For every x choose y=x, making ∀x∃y true. No single y equals both 0 and 1, so ∃y∀x is false. B gives this pair. A and C incorrectly reject the per-x choice; C and D incorrectly permit one common witness. A witness may depend on the preceding universal variable.

## Q27

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: vocabulary in context. Reversing a tentative preference is wavering, so A fits. B means working together, C means approaching agreement and D means vanishing; none captures indecision. The sentence's second clause supplies the intended meaning.

## Q28

**Correct answer:** D

Candidates II, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) IV.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) IV.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: negative edges and premature finalization. True best route s→b→a→t costs 5−4+3=4, so B is true and A false. Other routes cost 5 and 6. The graph is acyclic, so C is false. Dijkstra first finalizes a at two, sets t to five, and then chooses t before b at the specified tie, returning five, so D is true. The negative edge permits later improvement of an already-finalized distance.

## Q29

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: oracle-assisted recognition versus ordinary computation. If the oracle says M does not halt on w, then w is not accepted; otherwise simulate to its halting accept/reject outcome. This decides membership with the oracle, proving A. Apply this decision to all words and output the nonmembers to enumerate the complement, C. B confuses recognizers with total deciders; D would imply an ordinary finite-time halting decision bound and is false. Oracle-assisted conclusions do not assert ordinary decidability.

## Q30

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Forced edges and alternative perfect matchings.

Vertex b has only neighbour2, so every perfect matching uses b–2. Then a must use1 and c must use3, giving exactly one perfect matching. A and C are true. Edge a–2 is unused in that matching, so removing it does not destroy the matching; B is false. Adding b–1 allows the additional matching a–2,b–1,c–3, so D is true.

**Misconception:** Assuming every edge incident to a matched vertex is essential to the matching.

## Q31

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The clause beginning “only if” imposes a condition on the endorsement. Thus B is the contextual meaning. A is the occupational sense of qualified, C wrongly asserts withdrawal, and D contradicts the stated reservation. Interpret vocabulary through its surrounding claim.

## Q32

**Correct answer:** B, D

The underlying question is correctly answered by A, C. This variant asks for its invalid answers, so select the complementary set: B, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The two unequal(a,b) assignments give the two products in A, independent of c,d. Each leaves two variables free and covers four inputs, proving C. Their eight inputs do not form one cube: spanning01 and10 while omitting a,b would also cover00 and11 zeros. Thus B and D are false. Power-of-two cardinality is necessary but not sufficient for a valid Karnaugh group.

## Q33

**Correct answer:** A

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **D: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A one-bit pending indicator merges events that occur before clearing, so B is true and A false. A properly synchronized counter can represent their multiplicity, proving C. Arbitrarily close events can still merge even with a fast handler, so D's universal timing guarantee is false. Counting delivered interrupts need not count underlying device events.

## Q34

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Meet and join in a subset lattice are intersection and union, giving{b} and{a,b,c}. Thus A,B are true. Neither set contains the other, so C is false. The empty set is contained in every subset, proving D. Lattice order is inclusion, not cardinality alone.

## Q35

**Correct answer:** C

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The IPv4 header checksum covers the source address, so A is true. TCP includes its ports and a pseudo-header containing IP addresses, making B true. C and D incorrectly omit checksum-covered fields. Rewriting at one protocol layer can affect integrity checks at another.

## Q36

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

B explicitly compares one cost with the other cost, using “that” to refer to cost. A compares an activity's cost with a machine rather than its replacement cost; C lacks parallel grammatical structures; D is malformed. Parallel comparison makes the intended quantities unambiguous.

## Q37

**Correct answer:** C, D

The underlying question is correctly answered by A, B. This variant asks for its invalid answers, so select the complementary set: C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The fixed bits yield a NOT c; b,d are absent because all their combinations are covered. Thus A,B are true and C false. Specified zeros cannot be included in a valid exact SOP group, making D false.

## Q38

**Correct answer:** B

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **D: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A conditional can avoid evaluating an unsafe expression. Unconditionally evaluating it can introduce invalid division even if the eventual selected arithmetic value seems unchanged. Hence B,C are true and A false. D is false precisely because branch removal can introduce extra evaluations. Safety and side effects must be checked in addition to value identities; the stated proof is relevant, not a universal sufficient condition for all transformations.

## Q39

**Correct answer:** A

The underlying question is correctly answered by B, C, D. This variant asks for its invalid answers, so select the complementary set: A.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Au=u−u(vᵀu)=0, so A is singular and A is false. If Ax=0 then x=u(vᵀx), putting x in span(u); conversely every such multiple is killed, proving B. Also vᵀA=0, so solvability requires vᵀb=0; when that holds, Ab=b and x=b works, proving C. Expanding A²=I−2uvᵀ+u(vᵀu)vᵀ=I−uvᵀ proves D. This is a projection, not necessarily an orthogonal projection because u and v need not coincide.

## Q40

**Correct answer:** D

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The regular pumping lemma requires0<|y| and |xy|≤p, so1≤d≤p, proving A. Pumping to two copies adds d to p², and0<d≤p<2p+1 is smaller than the next-square gap. Thus B is true and the pumped word is outside L for every permitted decomposition. C violates the nonempty requirement. D is false since p²≥p for p≥1. The gap argument handles all decompositions, not one chosen substring.

## Q41

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Both instances are held and neither holder can release under the given rule, so A. An allowed release would supply the outstanding request of one process, proving C. B ignores exhaustion of all instances. D counts an already allocated instance as an additional available one.

## Q42

**Correct answer:** B

Candidates I, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, III and omits valid candidate(s) I, IV.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The four minterms are0000,0010,1000,1010. A and C vary independently, while B=D=0 throughout. Thus they form a four-cell cube represented by (NOT B)(NOT D), proving A,D and refuting B,C. Karnaugh-map grouping follows Gray-code adjacency, including wraparound, rather than ordinary consecutive decimal labels.

## Q43

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The lemma's requirement concerns language words at least as long as the pumping length. None exist at length≥21, so the implication is vacuously satisfied, giving C. A,B invent long words or substrings. D incorrectly excludes finite regular languages from the condition.

## Q44

**Correct answer:** D

Candidates I, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) IV.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) IV.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Inclusion would be violated if an evicted L2 block remained in L1, so a corresponding L1 invalidation can be needed, proving A. L2 can contain blocks absent from L1, refuting B. Exclusivity forbids simultaneous copies, refuting C. Inclusive replication consumes slots without adding distinct blocks, proving D. The policies constrain contents, not merely replacement order.

## Q45

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The updated alternatives have costs 2+9=11 through Y and 5+1=6 through Z. X advertises their minimum, 6. A omits link costs; C ignores the still-valid Z route; D combines unrelated quantities. An increased metric must trigger reconsideration of other neighbors.

## Q46

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Static links implement lexical scope, so R refers to its lexical parent P. Dynamic links implement return/unwinding along actual calls, so R's caller Q is identified. Thus B; A confuses lexical and dynamic parents, C swaps them, and D ignores the actual caller. Sibling procedures share a lexical parent without calling through it.

## Q47

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Gray v is an ancestor of active u; the tree path v→…→u together with u→v forms a directed cycle, proving A. Directed DFS detects a back edge on every directed cycle, proving C for a complete forest. A black vertex may simply have finished in another branch, with no return path to u, so B is false. A white vertex is undiscovered and cannot already be an ancestor, so D is false. The undirected parent-edge exception does not apply to this directed setting.

## Q48

**Correct answer:** D

Candidates I, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) IV.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Both A,D use unused primary keys and non-NULL code values. Reusing code 'X' is permitted because no uniqueness constraint applies to it. B duplicates id2 and C violates code's NOT NULL constraint. Constraints must be applied to the declared columns rather than inferred from the sample rows.

## Q49

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Signed implies archived, which implies not editable, proving A. An editable form exists and cannot be signed, proving C. Unsigned forms need not be editable: an unsigned archived form is consistent with all premises, refuting B. Nothing requires any signed form, so D is not entailed. Universal statements alone do not establish existence.

## Q50

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The unrestricted complement contains domain elements absent from R. It is {3} in the first domain, proving A, and {3,4} in the second, refuting B. Changing the ambient domain changes the answer without changing R, proving C. The contradictory bounded formula in D returns nothing over any domain, so D holds. Negation without a suitable range restriction can introduce domain dependence.

