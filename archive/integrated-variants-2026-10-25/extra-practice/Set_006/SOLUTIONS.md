# Worked Solutions — Additional Practice Set 006

## Q1

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

1. Calibration precedes the first trial: Q precedes R.
2. “This divergence” in S refers to R, and the successful repeat trial is the basis of P: R precedes S precedes P.
3. T follows receipt of the final report: P precedes T. Combining the constraints gives Q-R-S-P-T.
- Original option A: P cannot precede the repeat trial on which it is based.
- Original option B: Q explicitly precedes the first trial described in R.
- Original option C: This satisfies all four precedence links.
- Original option D: S cannot precede the divergence, and T cannot precede the report.

## Q2

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Using only old-state values, the sequence is 00 → 01 → 11 → 00, a period-three cycle. Thus the state after t edges depends on t modulo 3. Since 2027 = 3×675+2, the state is 11. The unused state 10 maps to 10, but is unreachable from the specified initial state.
- Original option A: False: 00 occurs only at edge counts divisible by 3.
- Original option B: False: 01 occurs when the edge count is 1 modulo 3.
- Original option C: True: 2027 is 2 modulo 3, giving 11.
- Original option D: False: 10 is a separate fixed point and is never reached from 00.

## Q3

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** General Aptitude — Ratios and percentages

1. Initially milk=72 and water=48 litres. The first withdrawal removes one-quarter of each, leaving 54 milk and 36 water; the refill makes water 66.
2. The next withdrawal removes one-sixth of each: the remaining amounts are milk=45 and water=55.
3. Adding 20 litres of milk gives 65:55=13:11.

- **A:** This reverses the final milk and water quantities.
- **B:** The final quantities are 65 and 55 litres.
- **C:** The two different replacement fluids do not preserve the starting ratio.
- **D:** This would require 70 litres milk rather than 65.

**Common misconception:** Each withdrawal uses the composition after the preceding mixing step.

## Q4

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Computer Networks — CIDR

One optimal cover is 10.4.1.0/24, 10.4.2.0/23, 10.4.4.0/23 and 10.4.6.0/24. The first /24 cannot be enlarged without including third octet 0. The last /24 cannot be enlarged without including third octet 7. The intervening four /24 blocks, third octets 2 through 5, are not one aligned /22, and therefore require at least two prefixes. Thus at least four prefixes are necessary, and the displayed four suffice.

A and B underestimate the alignment constraints. C attains the lower bound. D is feasible using six /24 prefixes but is not minimum.

- **A:** False: two prefixes cannot cover the six required /24 subnets due to power-of-two alignment constraints.
- **B:** False: three prefixes cannot cover the range without either including unallocated subnets or missing subnets.
- **C:** True: exactly four prefixes (10.4.1.0/24, 10.4.2.0/23, 10.4.4.0/23, and 10.4.6.0/24) minimally cover the entire range.
- **D:** False: six /24 prefixes can cover the range, but four prefixes suffice, so six is not minimal.

**Common misconception:** A power-of-two number of addresses forms a CIDR block only when the starting address has the required alignment.

## Q5

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Weighted averages and composition effects.

P improves from 80% to 90%; Q improves from 20% to 30%, so A is true. Combined success falls from 100/200=50% to 36/100=36%, making B false. Q's application share rises from 100/200=50% to 90/100=90%, so C is true. D is false: the table neither follows comparable individuals nor identifies a causal policy effect.

**Common misconception:** An aggregate percentage can fall while each group's percentage rises, because the group weights change.

## Q6

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Harmonic running-time sum.

For a fixed i there are floor(n/i) calls. Their sum is Θ(nH_n)=Θ(n log n): replacing each floor by n/i changes the sum by less than n. A and C underestimate the harmonic accumulation; B treats the inner loop as n iterations for every i.

**Common misconception:** A nested loop need not be quadratic when its step size depends on the outer index.

## Q7

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Survey evidence and causality.

The survey establishes only what respondents reported. Voluntary selection may bias their composition, and no comparison separates the app's effect from other causes. B preserves those limits. A overgeneralizes and asserts causality; C treats self-selection as representativeness; D mistakes absence of causal evidence for proof of no benefit.

**Common misconception:** Failure to establish a causal claim does not establish its negation.

## Q8

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Read timestamps in timestamp ordering.

After the read, RTS(x)=10 while WTS(x)=0. T5's write has timestamp 5<RTS(x), meaning a later transaction already read a value that would have preceded this write in timestamp order. T5 must abort. A ignores that read; B misuses the obsolete-write exception; D destroys the recorded ordering information.

**Common misconception:** Thomas's rule does not authorize ignoring a violation of the read-timestamp check.

## Q9

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Adjacency blocks with relative-order constraints.

Treat PQ as one block. Among R,PQ,S their order is fixed. Insert unrestricted T into one of the four gaps before, between, or after those three objects. Each insertion produces a distinct valid schedule, giving 4. A,C,D miscount the available positions.

**Common misconception:** The PQ block has a fixed internal order and must not be multiplied by 2!.

## Q10

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Join multiplicities under set semantics and functional dependencies.

Each of two R rows matches both S rows on B=x. J contains (1,x,p),(1,x,q),(2,x,p),(2,x,q), so A holds. Each A value has two C values, refuting B. Projecting away C yields exactly the two original R rows, proving C. B=x occurs in four tuples, so it is not a key, refuting D.

**Common misconception:** Set semantics eliminate duplicate complete tuples, not distinct matching combinations.

## Q11

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Parity composition.

The first gate computes a XOR b and the second computes (a XOR b) XOR c. This is 1 for one or three input ones, exactly odd parity. B holds. A excludes three ones incorrectly; C is a majority function; D includes 000 even though XOR there is 0.

**Common misconception:** Three-input XOR is not “exactly one input is 1.”

## Q12

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Dependency ordering.

Locating the fault precedes restoring the backup; restoration precedes testing; successful testing precedes reopening. Thus R,P,Q,S is forced. A restores before diagnosis, B reopens before testing, and D tests before restoration.

**Common misconception:** A plausible narrative order still has to satisfy every explicit prerequisite.

## Q13

**Correct answer:** C

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Reachability of and from negative cycles.

The reachable a→b→a cycle has weight −1; it can be repeated arbitrarily before continuing from b to c, so s-to-c walk weights are unbounded below (A). No edge from that component reaches t; the only s-to-t route has weight 5 (B). Thus C is false. c has no outgoing edges and cannot reach the cycle, refuting D.

**Common misconception:** A negative cycle affects destinations reachable from it, not every reachable vertex indiscriminately.

## Q14

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Precedence-preserving intermediate code.

Multiplication must compute b*c before the addition to a, as in B. A groups (a+b)*c; C changes the products; D computes separate values without combining a with b*c as required.

**Common misconception:** Three-address temporaries must preserve the original expression tree's dependencies.

## Q15

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Synchronous binary counting.

All right-hand sides use the old state. The trajectory is 011→100→101→110→111→000. B is therefore correct. A is the state after four edges, C after six, and D after two.

**Common misconception:** Updating bits sequentially within a single clock edge.

## Q16

**Correct answer:** B

Candidates I, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) IV.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II, III and omits valid candidate(s) I, IV.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Decidability under a totality promise.

Enumerate strings by length and simulate M on each. Every simulation halts by the promise; if any string is accepted it will eventually be found, proving A. D tests only finitely many strings, so it terminates with either answer.

For B and C, given an arbitrary machine N and input w, construct M that on input x simulates N(w) for |x| steps and accepts exactly if N halts within that bound. M always halts. Its language is nonempty exactly when N(w) halts. A decider for emptiness, or equivalence to the empty language, would therefore decide the halting problem, which is impossible. B and C are false.

**Common misconception:** Confusing termination of each individual test with termination of an infinite search for a negative answer.

## Q17

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Recoverability and cascading aborts.

r2(X) reads the uncommitted w1(X), proving A. Recoverability would require T1 to commit before T2 commits; instead T1 aborts after c2, so B is false. T2's dependence requires aborting it when T1 aborts, but T2 has already committed, establishing C's problem. Strict schedules prohibit this read of an uncommitted write, so D is false.

**Common misconception:** Treating a completed commit as evidence that a schedule satisfies recovery constraints.

## Q18

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Joining constant-propagation facts.

Both 4 and 7 can reach B, so no single constant describes all executions at entry. C holds. A or B would exclude a feasible path; D is false because each path assigns x.

**Common misconception:** Selecting one predecessor's fact instead of merging all feasible predecessors.

## Q19

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Encapsulation across routed hops.

The router removes the incoming link framing and constructs an outgoing frame appropriate to the next hop, proving A. IP and link addresses address different scopes, proving C. The next-hop frame address generally differs, refuting B; routed IP delivery still needs the destination IP address, refuting D.

**Common misconception:** Treating hop-local addresses as unchanged end-to-end identifiers.

## Q20

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Structural description of a grammar's language.

Each S expansion adds a at the front and b at the end; T generates an arbitrary central block of c symbols. Thus the language is {aⁿcᵐbⁿ:n,m≥0}. A and B follow. abcc puts c symbols after b and cannot be generated, so C is false. aacbb has n=2,m=1, proving D.

**Common misconception:** Tracking symbol counts without tracking their ordering restrictions.

## Q21

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Reverse translation of multiplexed connections.

The public translated ports distinguish the clients' connections, and the translator needs the corresponding mapping back to internal endpoints. B provides that information. A ignores the distinguishing field; link broadcast addressing (C) and payload length (D) cannot identify the internal connection.

**Common misconception:** Assuming the server endpoint alone uniquely identifies a connection through a shared public address.

## Q22

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Doubly linked neighbour repair.

Bypassing X requires P's forward pointer to reach N and N's backward pointer to reach P, A. B changes the wrong directions; C retains X; D creates self-links rather than preserving the remaining chain.

**Common misconception:** Updating only the forward chain or reversing the pointer directions.

## Q23

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Refragmentation retains original offsets and identity.

The first child starts at the parent's original offset 100. The second begins 200 bytes later, adding 200/8=25 to give 125, so A holds. The original MF=1 means later original-datagram data still exists after this parent; even its final child therefore keeps MF=1, proving B. The identification remains common to the original datagram, C. D incorrectly restarts the reference frame for offsets.

**Common misconception:** Clearing MF on the last child of a nonfinal parent fragment.

## Q24

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Datagram truncation semantics.

The first receive copies eight bytes from the twelve-byte datagram and discards its four-byte excess. The second receives the separate five-byte datagram. Thus B gives 8,5. A combines datagrams improperly, C exceeds the buffer, and D retains excess bytes explicitly specified to be discarded.

**Common misconception:** Applying byte-stream receive semantics to a datagram interface.

## Q25

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: regular-expression membership. baab=(ba)(ab), and it begins with b so cannot lie in (ab)*; B is correct. A=(ab)(ab) belongs to both languages. C's first pair aa is neither allowed block. D has odd length and cannot be concatenated two-letter blocks. Splitting into the specified blocks is the relevant test.

## Q26

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: address aliasing. Ignoring A11 makes addresses differing by hexadecimal 800 identical at the chip. 134+800=934, so D. A, B and C change one or more of the connected low eleven bits. A larger decoded window need not imply more physical storage.

## Q27

**Correct answer:** A

Candidates II, IV are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) IV.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: dead values versus observable effects. The first stored value is overwritten before print, but evaluating 1/x may raise an observable exception (B). Thus A is false when x=0. C leaves print dependent on an unrelated old value and also removes the possible exception. If x is known nonzero, the division has no observable effect under the stated exact-arithmetic model, and the second assignment fixes the printed value to two; D is correct. Dead-store elimination does not automatically justify deleting a potentially trapping right-hand side.

## Q28

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: nullable productions and FOLLOW propagation. FOLLOW(S)={$}; B ends S's production and occurs before c in its own recursive production, so FOLLOW(B)={c,$}, C. A is followed by nullable B, whose nonempty FIRST is {b}; hence FOLLOW(A)={b,$}, not c, disproving B. A's alternatives use lookahead a versus {b,$}; B's use b versus {c,$}, with no conflicts, proving A. D chooses ε on the lookahead reserved for A→aA and is false.

## Q29

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: pending-bit coalescence. Events at 1,2,3 collapse into one pending bit. At time 5 the handler clears it and runs to 7. The event at 6 sets it again, causing a second handler from 7 to 9. Hence B=(2,9). A counts every masked event separately; C loses the event during the handler; D has one extra invocation. A pending bit is not an event counter.

## Q30

**Correct answer:** D

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) I, IV and omits valid candidate(s) II, III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Physical sharing versus metadata representation.

A frame may have several virtual aliases, making B true. A single stored pair can equal only one of the two distinct(process, virtual-page) pairs, so A is false. Retaining a list of aliases permits lookup of both and resolves this particular representation problem, so C is true. Different virtual page numbers can map to the same physical frame; D is false.

**Misconception:** Treating a limitation of a simplified page-table format as a hardware prohibition on sharing.

## Q31

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Q establishes the discrepant readings; S explains the diagnosis; P describes the repair; R gives the subsequent test. Thus Q,S,P,R is required. B uses “this discrepancy” before its referent and puts the second trial before repair. C diagnoses the defect after the repair and trial. D introduces repair before the problem. Follow explicit references and causal dependencies, not just grammatical possibility.

## Q32

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

After line2 there exists a path through line3 that uses x before redefining it, so may-liveness includes x and A is true. On the path beginning at line5, x is never used, making B false. Line6 uses y, so C is true. The existence of a path using line1's definition prevents deleting it as dead; D is false. May-liveness takes a union over possible successors, not an intersection.

## Q33

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Ratios are2,1.8,1.8. The heuristic takes the weight6 item, leaving4, so neither remaining item fits and its value is12. The two weight5 items fit together and yield18. A is correct; B reverses the values, C uses forbidden fractional items, and D ignores the initially fitting items. Fractional-knapsack exchange arguments do not automatically apply to indivisible items.

## Q34

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Both a and b are at level1; a discovers c at level2 before any level2 node can create a level3 discovery. b discovers d at level2. Thus A,C are true and B false. Other graphs can have several shortest predecessors and order-dependent parents, disproving D. BFS distance uniqueness does not imply parent uniqueness.

## Q35

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A write fault can allocate and copy a private page, preserving the other process's contents, so A and C are true. Deferred copying is the point of copy-on-write, disproving B. Initial physical sharing does not force permanent shared-write semantics, disproving D.

## Q36

**Correct answer:** B

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) I, IV and omits valid candidate(s) II, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

P(both positive)=0.1×0.9²+0.9×0.2²=0.081+0.036=0.117, proving B. Bayes gives0.081/0.117=9/13, proving C. Each marginal positive probability is0.27, whose square0.0729 differs from0.117, so A is false. After one positive the posterior is0.09/0.27=1/3; the second raises it to9/13, disproving D. Conditional independence does not imply unconditional independence.

## Q37

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The device's memory update need not replace a noncoherent CPU cache entry, so A is possible and C can be necessary. DMA completion does not supply the excluded coherence guarantee, disproving B. Physical sharing and coherence are distinct properties, making D false.

## Q38

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A is realized by a root whose left child is a leaf and whose right subtree has a left leaf and a right pair of leaves. C is the complete depth-two tree. B is impossible: a first leaf at depth2 lies in the root's left subtree, which must supply at least one more leaf before the root's right depth-one leaf can appear; the second leaf cannot already have depth1. In D the depth-one leaf is third, so it would have to be the root's right leaf and therefore last, a contradiction. All four lists satisfy the numerical sum of 2^(−depth)=1, but that condition alone does not enforce the specified left-to-right order. Ignoring order would incorrectly accept B and D.

## Q39

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Appending b's can complete exactly strings a^i b^j with i≥j≥0, so K is that language. aaab has3≥1, proving A; abb has1<2 and cannot be repaired by more b's, refuting B. A grammar S→aSb | A, A→aA | ε generates K, proving C. For any i<j, the suffix b^j distinguishes prefixes a^i and a^j: only the latter completes a word in K. Infinitely many distinguishable prefixes imply nonregularity, refuting D. Right quotient by a regular language preserves context-freeness, but does not force regularity.

## Q40

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The ideals are empty,{a},{b},{a,b},{a,b,c},{a,b,c,d}, so A is true. Unions and intersections of downward-closed sets remain downward-closed and are respectively least upper and greatest lower bounds, proving B,C. These set operations satisfy the distributive laws, refuting D. Incomparability in the underlying poset does not destroy distributivity of its ideal lattice.

## Q41

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Two's-complement overflow is carry into the sign bit XOR carry out, proving A. Opposite-signed operands produce a sum between them, so C is true. For four bits,1111+0001 has carry but no signed overflow, refuting B. A valid negative result refutes D.

## Q42

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

For t=7, the read-timestamp test7<5 is false, but7<9 is true, so ignore. For t=4, the first test4<5 already aborts. C is the pair. A,D incorrectly perform the obsolete write; B reverses the priority of the two checks. Each attempt starts from the specified same metadata.

## Q43

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

SELECT DISTINCT x produces one row containing NULL. The outer COUNT(*) counts that row, giving1. COUNT(DISTINCT x), however, ignores NULL values and has no non-NULL distinct values to count, giving0. D is correct. A discards the surviving row, B fails to eliminate duplicates, and C treats the NULL as a counted value in Q2. A DISTINCT result row and a counted non-NULL aggregate input are different objects.

## Q44

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

To have f(g(0))=0, g(0) may be a or b. To have f(g(1))=1, g(1) must be c. Hence two right inverses, proving A, and both are injective, proving C. A left inverse would have to send f(a)=f(b)=0 to both a and b, impossible, refuting B. f itself is not injective, refuting D.

## Q45

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The set is the divisor lattice of 6, with meet gcd and join lcm; all results remain in the set. Complements are 1↔6 and 2↔3, so A,C hold. B is false because 1 and 6 are a lower and upper bound of 2,3. D is false because neither 2 divides 3 nor 3 divides 2.

## Q46

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

A is a valid implication: the union of two finite sets would be finite. Its antecedent cannot actually hold here because {a,b}* is infinite. B follows from regular complement closure and regular languages being context-free. D follows because finite languages are regular. C fails for nonregular context-free languages: if their complement were regular, complement closure would make the original regular too. A statement can be necessarily true because its premise is impossible.

## Q47

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Any adjacent map cells differ in exactly one input, which changes parity. Hence no two1-cells are adjacent, including wraparound neighbors. Each of the four1-cells requires a singleton implicant: C. A,B would include zeros; D is false because the four minterms themselves form an SOP. A compact XOR expression is not a two-level SOP of input literals.

## Q48

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

If f(a1)=f(a2), applying g gives a1=a2, proving injectivity(A). Every a equals g(f(a)), so g reaches all of A(C). For a counterexample to B,D, take A={0},B={0,1},f(0)=0,and g(0)=g(1)=0. The stated identity holds, but f misses1 and f(g(1))=0≠1. A left inverse does not force a two-sided inverse.

## Q49

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

In C, the introductory phrase modifies the subject technician, assigning the haste correctly. A grammatically attaches the introductory modifier to instrument; D explicitly describes the instrument as hurried. B's wording is unnatural and does not correctly express the intended modifier relationship. A human performer should be the subject governed by this introductory phrase.

## Q50

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

A has (i,j,k)=(2,2,3), so its first branch accepts. B has (2,3,3), so its second accepts. D has (1,1,1), so both accept. C has (3,1,2), satisfying neither equality, and is rejected. Nondeterministic choice gives a union, not an intersection of the branches' languages.

