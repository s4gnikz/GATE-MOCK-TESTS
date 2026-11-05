# Worked Solutions — Mock Test 038

## Q1

**Correct answer:** C

**Concept:** Contraposition.

Certified implies tested, so untested implies not certified, C. The rejected tested samples need not be certified, refuting A and D. B reverses the first implication without justification.

**Common misconception:** Taking the converse instead of the contrapositive.

## Q2

**Correct answer:** D

Concept: orthogonal projections of stacked cubes. The horizontal projection contains four unit squares. In one vertical view, projected heights are the column maxima 2 and 3, giving area five. In the other, row maxima are 3 and 2, also giving five. Sum=4+5+5=14, so D. A is the volume, not the projection sum; B and C undercount the projections. Occluded cubes do not add duplicate projected squares.

## Q3

**Correct answer:** A

**Concept:** Reconciling aggregate and subgroup changes.

If some existing visits move later, evening attendance rises while the daily total stays constant, so A is consistent. B directly contradicts the unchanged daily total. C contradicts the unchanged total when evening attendance rises. D asserts an error without evidence.

**Common misconception:** Interpreting growth in one time segment as growth in the whole day.

## Q4

**Correct answer:** D

The required numerical answer is **30**, so select **D**.

There are6!/(2!2!2!)=90 unrestricted arrangements. For each named adjacent duplicate pair, contraction gives5!/(2!2!)=30 arrangements. For each pair of such events, contraction gives4!/2!=12. All three events give3!=6. Inclusion–exclusion gives90−3·30+3·12−6=30. Duplicate letters are indistinguishable, including within contracted blocks.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 30 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -15 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q5

**Correct answer:** B
**Concept:** Concession in sentence structure.

The acceptance occurs despite a concern; “notwithstanding” supplies that concessive meaning and takes the following noun phrase. “Because” would require a different grammatical construction here and changes the intended relation. “Therefore” and “consequently” express consequence, not concession, and do not fit before this noun phrase. B is correct.

**Common misconception:** A word can signal a logical relation without fitting the grammatical structure of the blank.

## Q6

**Correct answer:** A

**Concept:** Opposite faces and vertex incidence after folding a cube net.

The four squares A,B,C,D wrap around the cube as a belt. Positions two apart in this belt are opposite: A opposite C, and B opposite D. The two remaining squares E,F close the top and bottom and are opposite. A,B,E take one face from each opposite pair and meet at a vertex. Thus A is correct. B incorrectly makes adjacent B,C opposite and its proposed triple includes opposite A,C. C has the correct opposite pair E,F, but its proposed triple includes opposite A,C. D gives a wrong opposite pair A,D and a triple containing opposite E,F.

**Misconception:** Using distance on the flat net instead of adjacency on the folded cube.

## Q7

**Correct answer:** B

The stated chain is closure < measurement < replacement < reopening. Measurement is forced between the two specified events, making B correct. A happens afterward, C is not mentioned, and D contradicts the explicit chain. Temporal precedence is transitive here.

## Q8

**Correct answer:** C
**Concept:** Conditional probability with a hidden box.

In Box I, both-red probability is 1/3 and at-least-one-red probability is 1. In Box II these probabilities are 0 and 2/3. Including the equal box priors gives P(both red)=1/6 and P(at least one red)=1/2+1/3=5/6. Their ratio is 1/5. A gives the unconditional numerator; B ignores the box information in the condition; D is twice the required ratio.

**Common misconception:** Conditioning changes the probability of the selected box as well as the probability of its ball outcomes.

## Q9

**Correct answer:** C

The statement explicitly allows withdrawal before inspection and forbids it afterward, exactly C. A ignores the post-inspection restriction. B invents an exception. D confuses ending a withdrawal right with cancellation. The timing qualifies the agreement's provisional nature.

## Q10

**Correct answer:** A

The required numerical answer is **45**, so select **A**.

The domain requires x>36/7. Since log4(x)=log2(x)/2, exponentiation gives x^(3/2)=7x−36. Put t=sqrt(x)>0: t³−7t²+36=0=(t−3)(t−6)(t+2). The positive roots3,6 give x=9,36, both within the logarithm domain. The root−2 is inadmissible because t is the positive square root. Sum9+36=45. The auxiliary variable's sign restriction prevents adding x=4 spuriously.

**Option check**
- **A: Correct.** It matches the derived answer at the required precision.
- **B: Incorrect.** Its value differs from the required answer by 45 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by -22 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q11

**Correct answer:** A

The reversed result is(2,C),(1,B),(1,A). Its key order is descending, but the tied records A,B have reversed relative order, so A. B,D mistakenly assume stability survives whole-array reversal. C describes the correct descending key order, not the defect.

## Q12

**Correct answer:** A, C
**Concept:** Expression kills and a must-analysis join.

Changing c does not change either operand, so the first predecessor preserves availability (A). Assigning a invalidates the previously computed value of a+b on the second path, refuting B. The must join intersects predecessor facts and therefore omits the expression (C). Union could falsely reuse a value on the second path, so D is unsound.

**Common misconception:** Having evaluated an expression somewhere earlier is insufficient if an operand was subsequently assigned.

## Q13

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Pumping-lemma quantifiers and a forced pumping region.

The bound |xy|≤p confines nonempty y to the first zero block, proving A. Pumping up adds zeros only before the single 1, so the two sides no longer match: B is false. Pumping down removes at least one zero from only that side, proving C. A nonregularity proof must defeat every permitted decomposition for its chosen witness; D is false.

**Common misconception:** The adversary chooses the decomposition; a proof must control all of its permitted choices.

## Q14

**Correct answer:** A, B

A matching without cd cannot perfectly match either odd triangle. Thus any perfect matching must use cd, after which edges ab and ef complete one; A,B are true. Each triangle is an odd cycle, so C is false. Covering all edges inside each triangle requires at least two of its vertices, hence at least4 overall; choosing b,c,d,e achieves4, refuting D. Matching and vertex-cover sizes need not agree in a nonbipartite graph.

## Q15

**Correct answer:** A

**Concept:** Eliminating the changing K-map variable.

Only a differs, while b=c=0, leaving b′c′, A. B and C improperly retain a and drop a fixed variable; D does not describe the two minterms' union.

**Common misconception:** Dropping a fixed literal rather than the bit that changes within the group.

## Q16

**Correct answer:** B

**Concept:** Direct-mapped conflict tracing.

B gives misses on 0 and 1, a hit on the second 0, and a miss on 4, which replaces 0 at index zero. A alternates conflicting blocks and has no hits; C visits four new blocks and has no hits; D has three hits after its first miss.

**Common misconception:** Treating blocks with the same index as the same cached block.

## Q17

**Correct answer:** D

Concept: conflict graph. w1(X) precedes r2(X), producing T1→T2. w2(Y) precedes r1(Y), producing T2→T1. The cycle precludes conflict serializability, D. A and B each ignore one edge; C is false because read/write pairs on the same item conflict. Commit order cannot remove an existing precedence cycle.

## Q18

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** FIRST and FOLLOW in LL(1) parsing.

At S the alternatives begin with distinct a and b. At A and B, c selects the nonempty production and the end marker in FOLLOW selects ε. No table cell has two entries, proving B. A ignores separate nonterminals and lookaheads; C ignores the leading symbols; D claims nonexistent left recursion.

**Common misconception:** Declaring a conflict merely because terminal symbols occur in different productions.

## Q19

**Correct answer:** C

The required numerical answer is **3**, so select **C**.

1. Transmission times per link are 0.5, 1 and 0.5 ms. Packet 1 finishes the links at 0.5,1.5,2 ms.
2. Packet 2 finishes link 1 at 1 ms but waits until 1.5 ms for link 2. It finishes link 2 at 2.5 ms.
3. Link 3 is free by then, so its final transmission ends at 3 ms.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 3 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **C: Correct.** It matches the derived answer at the required precision.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q20

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Predictive-parser pending terminals.

Each of the two leading a symbols causes an S→aSb expansion that leaves one future b on the stack. After both a symbols are consumed, two b symbols are pending around the remaining S. S→ε then allows them to be consumed. Thus the maximum is two, B; the other counts do not match the two expansions.

**Common misconception:** Count pending stack terminals, not all input symbols already read or still unconsumed.

## Q21

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Local next-hop address resolution.

ARP resolves the gateway's IPv4 address to its Ethernet address on the local LAN, enabling a frame to be delivered to that next hop (A). It does not discover TCP sequence numbers (B), routing tables (C), or DNS names (D).

**Common misconception:** For a remote destination, the link-layer next hop can be the gateway rather than the remote IP endpoint.

## Q22

**Correct answer:** C

The required numerical answer is **9**, so select **C**.

There are C(6,2)=15 pairs of positions. Exactly six are adjacent pairs, including positions6 and1. Thus15−6=9. Rotational equivalence is not imposed.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 9 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -4 and is outside the source answer's accepted range.
- **C: Correct.** It matches the derived answer at the required precision.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q23

**Correct answer:** A

The required numerical answer is **0**, so select **A**.

Two distinct flips toggle parity twice and restore even parity. Every one of the six pairs therefore escapes the check. An error-detecting parity bit detects odd-weight errors, not all nonzero errors.

**Option check**
- **A: Correct.** It matches the derived answer at the required precision.
- **B: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 2 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 3 and is outside the source answer's accepted range.


## Q24

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The link's stored path may stop resolving after deletion, so A is true. Pathnames can cross mounted file systems, making C true. Symbolic links do not increment the target's hard-link count or inherently retain its inode, so B,D are false. Name resolution and inode reference counting are separate.

## Q25

**Correct answer:** A

Concept: asynchronous I/O notification. Completion can raise an interrupt for the CPU (A). B destroys processor state; C corrupts addressing; D prevents useful transfer activity. None is a completion-notification mechanism. DMA transfers data independently but can still notify software when done.

## Q26

**Correct answer:** C

The required numerical answer is **11**, so select **C**.

Rearranging gives a(n)−a(n−1)=a(n−1)−a(n−2), so every first difference is 2. Therefore a(n)=1+2n and a5=11. By the definition of the ordinary generating function, the requested coefficient is precisely a5. The recurrence's repeated root leads to linear, not exponential, growth.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 11 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -5 and is outside the source answer's accepted range.
- **C: Correct.** It matches the derived answer at the required precision.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q27

**Correct answer:** A

A's inherited information cannot depend on a right sibling C under the left-to-right restriction, so A violates it. B,C use information from a left sibling; D uses the parent's inherited information. Those are permitted dependency directions, subject to the rest of the definition being consistent.

## Q28

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

A tombstone makes lookup continue through5 to6, so B is correct. A would stop lookup prematurely. C destroys another live key. D cannot repair the probe chain for the remaining key and is not a coherent deletion operation. Deleted and never-used slots have different search meanings.

## Q29

**Correct answer:** C

**Concept:** Computer Organization and Architecture — Pipelining and hazards

If the first ADD is fetched in cycle1, it writes R1 in cycle5. The second ADD's ID must be no earlier than5, so its IF must be4: two NOPs are needed between them. The second then writes R2 in cycle8, so the third's ID must be8 and IF7: two more NOPs. Four total suffice and fewer cannot meet both dependencies.

- **A:** False: two NOPs repair only one of the two immediate dependencies.
- **B:** False: at least two separations of two NOPs each are required.
- **C:** True: both consumer ID stages coincide with the corresponding producer WB stages.
- **D:** False: same-cycle write-before-read permits two, not three, NOPs per dependency.

**Common misconception:** A producer's EX completion does not make its result available without forwarding.

## Q30

**Correct answer:** C

The owner key distinguishes loans; the partial key distinguishes installments of a given loan. Their pair identifies each installment, so C. A collides across owners; B collides among installments of one owner. Amount need not be unique at either level, so D fails. A weak entity's partial key is interpreted within its owner.

## Q31

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Negating the universal yields an existential counterexample x. The implication fails when P(x) holds and its consequent ∃yR(x,y) fails; the latter negates to ∀y¬R(x,y). This is C. A retains a universal x; B negates the antecedent incorrectly; D requires only one failed witness instead of absence of every witness.

## Q32

**Correct answer:** D

Successful exec replaces the executing program within the same process. A is false because it is not fork. B is false because descriptors without close-on-exec can survive. C is false because only a failed exec returns to the old program. D states the preserved process identity correctly.

## Q33

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: recognizability versus decidability. The existing acceptance guarantee plus halting rejection for every nonmember gives a correct total decision procedure (B). A only describes tape symbols; C gives a single successful case; D holds for recognizers that may loop and therefore is insufficient. Deciders must halt on all inputs.

## Q34

**Correct answer:** D

The required numerical answer is **3**, so select **D**.

No singleton satisfies every factor: P misses(Q+R), Q misses(P+R), and R misses(P+Q). Each two-element subset satisfies all factors, giving covers{P,Q},{P,R},{Q,R}. Thus minimum cardinality is2 and three minimum covers exist. The three-element cover is valid but not minimum; repeated selections do not add new covers.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 3 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q35

**Correct answer:** 2

For a2×2 matrix, det(A−I)=det(A)−trace(A)+1=6−5+1=2. This follows by expanding the two-by-two determinant or evaluating its characteristic polynomial at1. No assumption of diagonal form is required.

## Q36

**Correct answer:** B

**Concept:** Many-to-one threading and blocking calls.

Every user thread needs the single kernel-scheduled execution context. When it blocks, none of those threads can execute through it, establishing B. A and C invent additional kernel contexts; D imagines execution without a runnable scheduled context.

**Common misconception:** Assuming the number of user threads equals the number of independently schedulable kernel threads.

## Q37

**Correct answer:** A, C

Later by-reference accesses need live storage, proving A. Lifetime-preserving allocation or another valid mechanism can supply it, proving C. A dangling pointer to reused stack storage does not suffice, refuting B. Lexical visibility is not a storage-lifetime guarantee, refuting D.

## Q38

**Correct answer:** 432

Concept: collision detection timing. Frame transmission time is 512/10⁸ seconds=5.12 microseconds, allowing one-way delay 2.56 microseconds. Subtract device delay 0.4 to get cable propagation budget 2.16 microseconds. Distance=2.16·10⁻⁶·2·10⁸=432 metres. Both device delays must be included in the round trip, not added only once to it.

## Q39

**Correct answer:** A, C
**Concept:** Continuity and oscillating difference quotients.

|f(x)|≤|x| proves continuity. Its difference quotient at zero is sin(1/x), which has no limit, so B is false. For g, the quotient x sin(1/x) tends to zero, proving C. For x≠0, g′(x)=2x sin(1/x)−cos(1/x), which fails to approach g′(0)=0, so D is false.

**Common misconception:** Existence of a derivative at a point does not imply continuity of the derivative there.

## Q40

**Correct answer:** B

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **D: Incorrect.** It includes invalid candidate(s) I, IV and omits valid candidate(s) II, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

If an A value occurs in R but not in S, any corresponding R tuple survives R−S, proving B. A fails for R={(1,x)}, S={(1,y)} with x≠y: the left side is{1}, the right empty. Every tuple in R∩S supplies an A value present in both projections, proving C. The same counterexample has empty intersection but common projected value1, refuting D. Projection can erase the distinctions on which intersection and difference depend.

## Q41

**Correct answer:** A, B, C

For s=0, T=a and F=T=a. For s=1, T=b and F=NOT T=NOT b. This proves A. When a=b, these two outputs are complements, proving B. When a≠b, a=NOT b and they agree, proving C. With s=a=b=0, F=0, but with s=0,a=b=1, F=1 whereas s XOR a XOR b=0, refuting D. Evaluate the two selection levels in their stated order.

## Q42

**Correct answer:** B

Let m=floor(log2 n). At outer iteration i=2^k, the inner values are2^(2^r), so there are floor(log2 k)+1 iterations. Summing for k=1..m givesΘ(m log m)=Θ(log n log log n). B is correct. A omits the growing inner count, C treats the outer loop as linear in n, and D treats the inner squaring loop as ordinary doubling.

## Q43

**Correct answer:** B

The required numerical answer is **3**, so select **B**.

B combines its link cost1 to A with A's stale distance2, adopting3. A's advertised route actually depended on the failed path through B, but ordinary distance-vector information does not reveal that dependency. This is the beginning of a count-to-infinity problem.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 3 and is outside the source answer's accepted range.
- **B: Correct.** It matches the derived answer at the required precision.
- **C: Incorrect.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q44

**Correct answer:** D

The required numerical answer is **3**, so select **D**.

**Concept:** Suffix-tracking DFA minimality.

Track three cases: no relevant suffix, suffix 0, and suffix 01 (accepting). These suffice with ordinary suffix updates. They are distinguishable: the accepting state differs from either other state on ε; states reached by ε and 0 differ on suffix 1. Thus three is both an upper and lower bound.

**Common misconception:** Adding a dead state although every prefix can still be extended to end in 01.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 3 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q45

**Correct answer:** 5

**Concept:** Round-robin scheduling with I/O.

The CPU schedule is P:[0,2), Q:[2,4), Q:[4,6), P:[6,8), Q:[8,9). P performs I/O on [2,5), then waits [5,6), giving waiting time 1. Q waits [0,2) and [6,8), giving 4. Their sum is 5. Q is not preempted at time 5 because the I/O completion only enqueues P.

**Common misconception:** Including blocked I/O time in ready-queue waiting time.

## Q46

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The first nested loop swaps each pair of entries on opposite sides of the main diagonal exactly once, so it transposes the matrix. The second nested loop reverses each row. The composition is a clockwise 90-degree rotation. Four iterations restore the original array, and 2027 has remainder 3 modulo 4, so the net transformation is a counterclockwise 90-degree rotation. Under that net transformation, new[r,c]=old[c,4−r]. Index 7 is (r,c)=(1,2), so its value is old[2,3]=5×2+3=13. Index 17 is (3,2), so its value is old[2,1]=11. Hence the program prints `13 11`. Every pointer is inside the single a array and every swap uses distinct entries.
- Original option A: True: three clockwise quarter-turns map the queried positions to original positions (2,3) and (2,1).
- Original option B: False: these are the values after one clockwise quarter-turn, not after 2027 iterations.
- Original option C: False: these are the unchanged initial values; 2027 is not divisible by four.
- Original option D: False: these are the values after two quarter-turns, not three.

## Q47

**Correct answer:** C

Concept: ordered auto-increment addressing. Source read uses 100 and gives three, then R becomes 104. Destination read uses 104 and gives five, then R becomes 108. The sum eight is written to captured destination 104. C=(108,8). A and D omit an increment; B reads the wrong destination value. The explicitly stated evaluation order resolves reuse of the same address register.

## Q48

**Correct answer:** D

**Concept:** Theory of Computation — Pushdown automata

The finite language L is regular, so a DFA recognizes it. A final-state DPDA can simulate that DFA without using its stack. A nondeterministic empty-stack PDA can choose whether to finish after a or to wait for b and then finish.

A deterministic empty-stack PDA accepting a has a unique computation on that prefix. On input ab it must follow the same computation until the prefix a has been consumed. If it then empties its stack through epsilon transitions, determinism prevents choosing a b-consuming alternative, and no transition can consume b after the stack is empty. Hence it cannot also accept ab. This is the prefix-free obstruction under the stated conventions.

A, B and C can recognize L by the constructions above. D cannot.

- **A:** False: a DFA recognizes the regular language {a, ab}, so a final-state PDA can also recognize it.
- **B:** False: an NPDA can nondeterministically guess whether to accept after a or after ab.
- **C:** False: a DPDA accepting by final state easily recognizes {a, ab}.
- **D:** True: a DPDA accepting by empty stack cannot recognize {a, ab} because it is not prefix-free and no end marker is provided.

**Common misconception:** Final-state and empty-stack acceptance have equivalent power for nondeterministic PDAs, but not automatically for deterministic PDAs without an end marker.

## Q49

**Correct answer:** B

The required numerical answer is **0**, so select **B**.

After the first read the pipe is empty. The second read blocks while any writer descriptor remains open; closing only P's copy does not signal end-of-file. When Q closes the final writer descriptor, an empty pipe yields EOF, represented by a zero-byte return. This differs from an error and from a short positive read.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **B: Correct.** It matches the derived answer at the required precision.
- **C: Incorrect.** Its value differs from the required answer by 2 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 3 and is outside the source answer's accepted range.


## Q50

**Correct answer:** B

The required numerical answer is **1.6667**, so select **B**.

P(N=2k+1)=2^{−(2k+1)} for k≥0. The odd probability is(1/2)/(1−1/4)=2/3. Conditional on being odd, K=(N−1)/2 has probabilities(3/4)(1/4)^k and mean(1/4)/(3/4)=1/3. Therefore E[N|odd]=1+2/3=5/3≈1.6667. Conditioning on parity changes the distribution and cannot be handled by rounding the unconditional mean.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 1.6667 and is outside the source answer's accepted range.
- **B: Correct.** It matches the derived answer at the required precision.
- **C: Incorrect.** Its value differs from the required answer by -0.8333 and is outside the source answer's accepted range.
- **D: Incorrect.** Its value differs from the required answer by 1.0000 and is outside the source answer's accepted range.


## Q51

**Correct answer:** C

The required numerical answer is **7**, so select **C**.

**Concept:** Equivalence relations as set partitions.

Choose a nonempty proper subset as one block: 2⁴−2=14 choices. Each two-block partition is counted twice, once for each complementary block. Therefore there are 14/2=7 relations.

**Common misconception:** Treating the two classes as labelled or ordered.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 7 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -3 and is outside the source answer's accepted range.
- **C: Correct.** It matches the derived answer at the required precision.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q52

**Correct answer:** C

Candidates II, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I, IV and omits valid candidate(s) II, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: induction-variable strength reduction. At iteration i=s+r, B's running address is base+4s+4r=base+4i; retaining i preserves its other uses. The now-unused address multiplication can be removed, so C also holds. A starts at the wrong element unless s=0. D corrupts statements that still depend on i. A derived induction variable need not replace the original variable everywhere.

## Q53

**Correct answer:** C
**Concept:** Common subexpressions with changing variable versions.

Share x*y with y*x, and share their identical sums with z. After x=x+1, x has a new value, so the later multiplication and sum cannot be shared with the earlier ones. Required operations: two multiplications, one initial sum with z, one increment, one final sum with z. Thus (2,3). A incorrectly shares across the definition of x; B omits the increment; D fails to merge the initial commutative products.

**Common misconception:** Equal variable names do not guarantee equal expression values across assignments.

## Q54

**Correct answer:** C

The required numerical answer is **275**, so select **C**.

The first MTU permits1000 payload bytes, already divisible by8, giving payload lengths1000,1000,400 and offsets0,125,250. The final400-byte payload is split into200 and200 bytes for MTU220. Their offsets remain relative to the original payload:250 and250+200/8=275. Refragmentation does not reset offsets to zero.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 275 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -137 and is outside the source answer's accepted range.
- **C: Correct.** It matches the derived answer at the required precision.
- **D: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.


## Q55

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** MST exchange arguments independent of weight signs.

Kruskal's cut-based choices remain correct with negative weights, proving A and C. A spanning tree cannot contain a cycle even if every edge on it is negative, refuting B. Adding c to each edge adds exactly (n−1)c to every spanning tree, preserving all comparisons and ties, so D is false.

**Common misconception:** Transferring shortest-path restrictions on negative weights to minimum spanning trees.

## Q56

**Correct answer:** B
**Concept:** Decidability from two recognizers.

Every input belongs to exactly one of L and its complement, so exactly the corresponding recognizer is guaranteed eventually to accept. Dovetailing reaches that event in finite time and yields a decision (B). A has no valid universal timeout, C discards the complementary recognizer's guarantee, and D is not a construction for complementation of arbitrary machines.

**Common misconception:** The two recognizers need not halt on their nonmembers for the combined decider to halt.

## Q57

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

With S empty, the implication in Q is true for every y, so every candidate qualifies. The conjunction in P is false for every y; the infinite domain is nonempty, so its universal statement is false and no candidate qualifies. Thus B; A,C,D each mis-handle one quantifier. Logical implication restricts the required witnesses; conjunction does not implement relational division.

## Q58

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Resource-count deadlock guarantee.

With six instances, each of three processes can hold two and wait for a third, giving a deadlock. With seven, if every unfinished process holds at most two, at most six are held and at least one remains available. Some waiting process can therefore receive another instance and complete once it reaches its requirement, releasing resources. The worst-case requirement is three for each process, so seven suffice and six do not. B is the minimum; A is unsafe, and C,D are sufficient but not minimal.

**Common misconception:** Preventing deadlock does not require satisfying every process's maximum demand simultaneously.

## Q59

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Computer Organization and Architecture — Signed overflow and unsigned comparison

1. N=0 with V=1 means the mathematical signed subtraction was less than −128, wrapping into a nonnegative result. Positive overflow would instead produce N=1.
2. Therefore A represents a negative signed number and B a nonnegative signed number. Write the unsigned value of A as 128+r, where 0≤r≤127, and the value of B as b, where 0≤b≤127. Their signed difference is r−128−b.
3. Overflow requires r−128−b<−128, hence b>r. Every such pair automatically has unsigned A>B, so C=1.
4. For r=0 there are 127 choices of b, for r=1 there are 126, and so on down to zero. The count is 127+126+⋯+1=127×128/2=8128.

- **A:** Incorrect: 8192 treats the boundary as exactly half of all opposite-sign pairs without excluding the equality diagonal.
- **B:** Correct: the strict triangular inequality gives 8128.
- **C:** Incorrect: 8256 includes b=r, whose signed result is exactly −128 and does not overflow.
- **D:** Incorrect: 16384 counts all opposite-sign pairs, including those with no overflow.

**Common misconception:** Unsigned carry and signed overflow describe different properties; endpoint pairs must be checked against the signed representable range.

## Q60

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Aligning distances to shared suffixes.

If two acyclic lists share a node, all successors of that node are shared. After discarding the length difference from the longer prefix, the two pointers have equal distances to the end. Advancing together therefore reaches the first shared node together, or reaches null if disjoint. B uses linear time and constant extra storage. A and C confuse equal values with identity; D supplies no intersection test and mutates links.

**Common misconception:** Inferring physical node sharing from equal stored data.

## Q61

**Correct answer:** B
**Concept:** Array-index intervals of a complete-tree subtree.

At successive depths below node 6 the indices are {6},12–13,24–27,48–55,96–111. Only 96–100 exist at the final level. Counts are 1+2+4+8+5=20. B is correct. A omits the partial final level, D treats it as full, and C adds one nonexistent node.

**Common misconception:** A complete tree may have a partially populated last level inside a subtree.

## Q62

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

In a downward scan, j−wi<j has not yet been updated for the current item. Thus the right-hand side combines the previous-item optimum with at most one copy of the new item, preserving the 0/1 recurrence. This proves A and D. In an upward scan, the lower entry may already contain this item: for the single item (2,3), update D[2]=3 and then D[4]=D[2]+3=6, although the true 0/1 optimum is 3. Hence C is true and B is false. The descending order is a dependency discipline that allows two DP rows to share storage.
- Original option A: True: descending capacity order preserves the previous-row dependency for every item.
- Original option B: False: upward order can reuse the current item repeatedly.
- Original option C: True: the update at capacity 4 reads the newly changed D[2]=3.
- Original option D: True: positive weight makes j−wi smaller than j, so the downward scan has not visited it yet.

## Q63

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** DISTINCT aggregates and NULL exclusion.

Department A has two distinct non-NULL salaries {10,20} and sum 40; both predicates hold. Department B has one distinct non-NULL salary {20} and sum 20; neither predicate holds. Therefore only A is returned, option B. A omits a qualifying group, C selects the failing group, and D includes both.

**Common misconception:** COUNT(DISTINCT salary) ignores NULL, and SUM still counts repeated non-NULL rows.

## Q64

**Correct answer:** D

The required numerical answer is **35**, so select **D**.

**Concept:** Microinstruction field widths.

There are 16 control bits, log₂8=3 condition-selection bits, and two log₂256=8-bit addresses. Total width is 16+3+8+8=35. Both outcomes have explicit address fields, so no fall-through address saving applies.

**Common misconception:** Encoding one branch condition does not also encode its target addresses.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 35 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -17 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


## Q65

**Correct answer:** D

The required numerical answer is **1**, so select **D**.

Three distinct eigenvalues imply a basis of eigenvectors. Applying polynomial p(t)=t²−3t+2=(t−1)(t−2) gives eigenvalues0,0,6 for B in that basis. Exactly one is nonzero, so rank B=1. Without diagonalizability, simply counting nonzero eigenvalues would not generally determine rank; it is justified here by distinct eigenvalues of A.

**Option check**
- **A: Incorrect.** Its value differs from the required answer by 1 and is outside the source answer's accepted range.
- **B: Incorrect.** Its value differs from the required answer by -1 and is outside the source answer's accepted range.
- **C: Incorrect.** Its value differs from the required answer by 2 and is outside the source answer's accepted range.
- **D: Correct.** It matches the derived answer at the required precision.


