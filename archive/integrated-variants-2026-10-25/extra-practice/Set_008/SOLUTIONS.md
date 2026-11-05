# Worked Solutions — Additional Practice Set 008

## Q1

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

1. If x=0, the original expression reduces to y. If x=1, it reduces to z.
2. A selects exactly these two cofactors. Equivalently, expansion gives xz + x'y + yz, and the consensus term yz is redundant.
- Original option A: Its x=0 and x=1 cofactors are y and z.
- Original option B: This swaps the selected cofactors; x=0,y=1,z=0 is a counterexample.
- Original option C: For x=1,y=1,z=0 it gives 1, whereas F=0.
- Original option D: For x=y=z=0 it agrees, but x=1,y=z=0 gives 1 while F=0.

## Q2

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Because g has nonzero constant term and degree 3, it cannot divide a monomial, establishing A. A burst of length at most 3 has the form x^k b(x), with nonzero constant term and degree(b)≤2. Since gcd(g,x)=1 and degree(b)<3, it cannot be divisible by g, establishing B. Polynomial division gives x^7+1 = (x^3+x+1)(x^4+x²+x+1), so a two-bit error seven positions apart is undetected, establishing C. The polynomial g itself is an undetected three-bit error, refuting D. Equivalently g(1)=1, so x+1 is not a factor and the universal odd-error guarantee does not hold.
- Original option A: True: a generator with constant term 1 and positive degree cannot divide a single monomial.
- Original option B: True: after removing the x^k shift, a burst of length ≤3 has degree below that of g.
- Original option C: True: g divides x^7+1, and multiplying by x^k only shifts the same error.
- Original option D: False: e(x)=g(x) has three nonzero coefficients and is undetected.

## Q3

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** General Aptitude — Two- and three-dimensional patterns

1. Each stack at row i, column j is at most min(row maximum i, column maximum j). The componentwise largest arrangement is rows [2,3,1] and [2,2,1], with 11 cubes; it meets every projection.
2. Each column must attain its maximum, so at least 2+3+1=6 cubes are needed.
3. Rows [0,3,1] and [2,0,0] attain all required row and column maxima with exactly 6 cubes. Thus both bounds are achievable.

- **A:** The displayed 6-cube construction disproves a minimum of 7.
- **B:** It gives the two attainable bounds.
- **C:** The per-stack upper bounds sum to only 11.
- **D:** Both numbers exceed attainable tight bounds.

**Common misconception:** Projection heights are maxima, not sums; each visible peak can serve both a row and a column constraint.

## Q4

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Operating Systems — Contiguous allocation and coalescing

1. First-fit allocates A at [0,50). B cannot fit the remaining [50,60), so it occupies [100,135).
2. Freeing A and X joins [0,50), [50,60), and [60,100) into [0,100). B prevents further merging. The other holes have sizes 45 and 40. The largest is 100.
3. Best-fit also puts A at [0,50), since the 60-unit hole is the smallest that fits 50. It puts B in the 40-unit hole at [200,235).
4. When A and X are freed, the entire interval [0,180) becomes free: the original [100,180) hole was never occupied. Y prevents merging beyond 180. The largest hole is 180.

- **A:** Correct: the maxima are 100 and 180.
- **B:** Incorrect: best-fit leaves [100,180) available for coalescing.
- **C:** Incorrect: first-fit's B blocks the interval at address 100.
- **D:** Incorrect: it reverses the two outcomes.

**Common misconception:** A choice that leaves a smaller immediate remainder can improve a later allocation by preserving holes that will coalesce after deallocation.

## Q5

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Narrative reference and causal order.

R initiates the first inspection. S refers to that inspection and identifies the defect. Q repairs the identified defect and starts the second inspection. P gives that second inspection's result. Thus R,S,Q,P is coherent. A repairs before identifying the crack; B uses the inspection reference before its introduction; D places repair and retesting before the initiating event.

**Common misconception:** Pronoun references and causal dependencies constrain order even when each sentence is grammatical alone.

## Q6

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Division, candidate domains and vacuous truth.

With no required courses, every Student identifier satisfies QI's universal condition, giving {1,2}. QII considers only identifiers appearing in Enrollment, namely {1}; each vacuously covers all required courses. D is correct. A treats a universal over an empty set as false; B incorrectly narrows QI's domain; C adds identifier 2 to the division's specified candidate domain.

**Common misconception:** Equivalent-looking universal queries can differ because their candidate tuple domains differ.

## Q7

**Correct answer:** B, D

The underlying question is correctly answered by A, C. This variant asks for its invalid answers, so select the complementary set: B, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Folding a cube net.

Take B as the front face. Its neighbours A,C,D,F fold to left,right,top,bottom, while E beyond D becomes the back. Opposite pairs are A/C, B/E and D/F. A/E and E/F therefore share edges, proving A,C. B and D list opposite pairs, not adjacent faces.

**Common misconception:** Squares separated in the flat net may become adjacent after folding.

## Q8

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Comparison lower bounds with partial order information.

There are C(6,3)=20 possible interleavings preserving both run orders. A binary comparison tree needs depth at least ceil(log₂20)=5. Standard merging compares until one run empties and uses at most five comparisons, attaining the bound. A and B cannot distinguish twenty orders; D is not minimal.

**Common misconception:** Known sorted runs reduce the possibilities from 6!, but do not eliminate uncertainty about their interleaving.

## Q9

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Intersection and equivalence closure.

No pair of distinct elements shares a block in both partitions, so R∩S consists of the six reflexive pairs. In R∪S, the links 1–2–3–4–5–6 connect every element. Transitivity therefore puts all six into one class in T, giving 6²=36 ordered pairs. Only A has both counts. B omits reflexivity; C incorrectly retains nonreflexive intersection pairs; D does not complete transitivity.

**Common misconception:** The union of equivalence relations need not itself be transitive.

## Q10

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

## Q11

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Process creation versus image replacement.

fork creates the child. Its successful exec replaces the child's current program image while retaining its process identity, so B holds. A confuses exec with process creation; C changes the wrong process; D describes a return to the old program, which does not occur after a successful exec.

**Common misconception:** Launching a new program image need not create a new process.

## Q12

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Lower and upper bounds with duplicate keys.

The first 4 is at index 4, while the first value greater than 4 is 7 at index 6. Thus C gives (4,6). A begins before any 4; B stops at the last equal value rather than after it; D starts at the second equal value.

**Common misconception:** Upper bound is the first strictly greater element, not the final matching element.

## Q13

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Cumulative acknowledgments with reordering.

Until bytes 1000–1099 arrive, byte 1000 remains the first missing byte, so each of the first three ACKs is 1000. Once that segment arrives, buffered data make all bytes through 1399 contiguous, so the ACK advances to 1400. B matches; A,C,D incorrectly acknowledge across a gap or ignore buffered data.

**Common misconception:** Duplicate ACKs can result from reordering without actual packet loss.

## Q14

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

## Q15

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Regular-expression union.

A belongs to a*b, using two a symbols. B belongs to ab*, using two b symbols. C belongs to both branches. D starts with b and ends with a, matching neither branch.

**Common misconception:** Applying the star to the entire alternative instead of the preceding symbol.

## Q16

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** State-cycle analysis and input counting.

Input 1 cycles 01→10→11→01, while input 0 resets to 01. Acceptance therefore requires the trailing run of ones to have length divisible by three. At length five, a string containing a zero is accepted with trailing run length 0 or 3: respectively 16 strings ending in 0 and two ending in 0111 (one free prefix bit). The all-one string has five trailing ones and is rejected. Total 18, option C. A omits the trailing-three case; B includes only one of its two prefixes; D exceeds the exhaustive count.

**Common misconception:** Counting all ones rather than only those after the last reset.

## Q17

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

## Q18

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Dead assignments and liveness.

A states precisely that the assigned value cannot be observed on any outgoing path. With a pure, nontrapping right-hand side, the assignment can be removed. C is the corresponding liveness criterion. B provides a path that may need the value; D has no semantic relevance.

**Common misconception:** Removing an assignment that is unused on only some paths.

## Q19

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Control links versus lexical links.

The dynamic link identifies the caller's activation for return-time restoration. A holds. A static link follows lexical enclosure and need not identify the caller, refuting B. Symbol-table and heap-object pointers in C,D do not restore the caller's activation.

**Common misconception:** Assuming caller and lexical parent always coincide.

## Q20

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Many-to-one threading and blocking calls.

Every user thread needs the single kernel-scheduled execution context. When it blocks, none of those threads can execute through it, establishing B. A and C invent additional kernel contexts; D imagines execution without a runnable scheduled context.

**Common misconception:** Assuming the number of user threads equals the number of independently schedulable kernel threads.

## Q21

**Correct answer:** C

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** SQL CHECK and three-valued logic.

For B=3, the predicate is TRUE and passes. For NULL it is UNKNOWN, which is not FALSE and therefore passes under the specified semantics. Zero and −2 make the predicate FALSE and are rejected. The fresh primary keys remove key collisions from consideration.

**Common misconception:** Assuming CHECK(B>0) also imposes NOT NULL.

## Q22

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Translation caching versus page residency.

A TLB miss lacks a cached translation, not necessarily the data page. The resident accessible page-table entry supplies that translation without a page fault, B. A,C,D incorrectly turn a translation-cache miss into a residency or protection failure.

**Common misconception:** Equating TLB misses with page faults.

## Q23

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Existential range-restricted assignment.

The existential requires some listed department to which e is assigned, A. It does not require all departments (B), forbid assignments (C), or universally restrict the domain (D).

**Common misconception:** Reading EXISTS as a universal condition.

## Q24

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Summing coupled loop costs.

For each i, work runs i floor(n/i) times, at most n, giving O(n²). For i>n/2, floor(n/i)=1, and the sum of these i values alone is Θ(n²), giving a matching lower bound. Thus B is tight. A omits the innermost factor, C treats all three bounds as independent n, and D ignores the outer iterations.

**Common misconception:** Multiplying maximum loop bounds without using their dependence on i.

## Q25

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: DFS interval nesting. v's entire interval lies inside u's, so v is a descendant of u. An edge from ancestor to descendant that is not a tree edge is forward (B). A would point to an ancestor; C connects unrelated DFS subtrees and requires disjoint intervals; D denies ordinary descendant nesting. Edge direction is crucial.

## Q26

**Correct answer:** D

Candidates II, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) I, III and omits valid candidate(s) II, IV.
- **B: Incorrect.** It includes invalid candidate(s) I and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) IV.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: stable multi-key sorting. Sorting secondary department first and then stably sorting primary name preserves department order among equal names, so B works. A gives department primary priority. C can scramble equal-name records' department order. D compares the desired tuple directly and works regardless of how equal complete tuples are ordered. The final stable pass sets the primary key.

## Q27

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: induction versus proof. The observation establishes correctness only on the tested executions, which is B. A extrapolates to all programs, C invents universal failure outside the suite, and D denies the possibility of a revealing new test. Finite testing alone is not a universal correctness proof.

## Q28

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: universal conditions over an empty set. Every candidate passes the “for every B in S” condition vacuously. Division's candidates are {1,2}, giving A and disproving B. The second query's candidates are U={1,2,3}, giving C. D mistakes an empty requirement set for a failed requirement. The candidate universe still matters when the condition is vacuous.

## Q29

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: subset simulation and accepting suffixes. Starting at {p}, input 0 gives {p,q}, then 1 gives {p,r}, then 0 gives {p,q}; A holds and B fails because final acceptance requires r after the whole word, not an earlier prefix. Reachable subsets are {p},{p,q},{p,r},{p,q,r}, proving C. A zero creates q, and exactly one more symbol reaches r; r has no outgoing transitions. Thus final acceptance records a zero exactly two positions from the end, proving D.

## Q30

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Consensus term and static hazards.

When b=c=1, the function should stay1 while a changes. Unequal delays can briefly make both original product outputs0. The term bc is continuously1 during the transition and covers that gap. It is logically redundant: whenever bc=1, either a=1 makes ab=1 or a=0 makes(NOT a)c=1. Thus C removes this hazard without changing the function. A and D incorrectly turn the function on at a=b=c=0. B incorrectly turns it on at a=1,b=c=0. They also do not provide the required stable cover during the specified transition.

**Misconception:** Equating Boolean equivalence with identical transient circuit behaviour.

## Q31

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

For digit string ab, both RS and SR produce(9−b)(9−a): digitwise replacement commutes with reversal. A is true. R² and S² each restore the original string, so B and C are false in general. D fails, for example, on12, which becomes78. A transformation being its own inverse does not make the composite the identity.

## Q32

**Correct answer:** B

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

For1≤k≤p, p²<p²+k≤p²+p<(p+1)² because the gap to the next square is2p+1. Pumping y twice therefore produces a nonsquare length for every legal decomposition. A and B are true. No particular k needs to be chosen, so C is false. The contradiction disproves regularity, making D false. The uniform inequality is what handles the pumping lemma's existential decomposition.

## Q33

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Choose x_n=1/(π/2+2πn) for value1 and y_n=1/(3π/2+2πn) for value−1; both approach0 positively. A and B are true and their different limits disprove D. Since |x sin(1/x)|≤|x|, the squeeze theorem proves C. Bounded oscillation can disappear after multiplication by a vanishing factor.

## Q34

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Linearity gives H(c+e)=Hc+He=He for a codeword c. Thus C is true. If e is a nonzero codeword, He=0 and the change is undetected, proving A and disproving B,D. A zero syndrome means code membership, not absence of error.

## Q35

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

A separate slot in every active activation record preserves each call's local value, making B correct. A overwrites older calls' values, C cannot represent arbitrary evolving locals, and D confuses control information with variable storage.

## Q36

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

An existing auditor is a reviewer and therefore not an intern, proving A. The same containment/exclusion argument applies to all auditors, proving C. Non-interns need not be auditors, so B is not implied. Nothing requires interns to exist, so D is not implied. Existential information must be carried only through justified set inclusions.

## Q37

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Subsequent fragment starts must be expressible in eight-byte offset units, so nonfinal payload lengths are multiples of eight: A. The final payload need not be padded to that boundary, proving B. The offset requires multiplication by eight, disproving C, and refers to original payload positions rather than counting each fragment's new header, proving D. Length and offset use different units.

## Q38

**Correct answer:** D

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Ascending insertion gives a right-child chain with n−1 edges, so A is true. The BST invariant ensures that inorder traversal returns sorted keys, proving B. For keys1,2,3, inserting2 first can give a balanced root, whereas inserting1,2,3 gives a chain; C is false. The chain has sorted inorder output but linear worst-case search, refuting D. Traversal order does not certify balance.

## Q39

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Swapping q[0] and q[1] swaps the pointers only: they now point to v[0] and u[0]. Incrementing q[0] makes it point to v[1]. The assignment adds u[0]=1 to v[1]=4, leaving v[1]=5 and u[0]=1. B follows. A,D incorrectly change u[0]; C misses the final addition. Moving pointers does not move array elements.

## Q40

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

For false flag both blocks end with x=0,y=1, proving A. For true flag the original produces x=1,y=2 while the proposal produces x=1,y=1, refuting B. The conditional assignment invalidates an unconditional x=0 assumption, proving C. If y is unobservable and only the stated operations occur, both blocks leave the same x for either flag, proving D. Correct optimization depends on both control flow and which results are observable.

## Q41

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

A uniform truth of either predicate guarantees their pointwise disjunction, proving A. One common witness proves both existential claims, proving C. On domain{1,2}, let P hold only at1 and Q only at2: this refutes both B and D. Separate witnesses need not coincide.

## Q42

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Transposition reverses product order, giving Aᵀ=UᵀLᵀ, so A is true. Set y=Lᵀx; solve Uᵀy=b first, then Lᵀx=y, proving C. Reversing those solves in B generally solves the wrong product because the factors need not commute. Transposing a unit lower-triangular matrix gives unit upper triangular, proving D.

## Q43

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The first receive discards DE under the given truncation rule. The next queued datagram is FG, which fits, so A is correct. B,C,D all incorrectly retain discarded bytes or combine separate datagrams. Datagram boundaries differ from stream byte buffering.

## Q44

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

XOR cancellation gives u XOR v=x XOR z=w, proving A and refuting D: only four parity triples occur. Complementing all three inputs preserves u,v,w, so B is false. Those outputs identify a pair of complementary input triples; with three inputs, their majority bits are opposite. Adding t selects exactly one member, proving C. A nonlinear extra output can resolve information lost by the parity outputs.

## Q45

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The first x value feeds y=x+2, so A is true. The last x value is never used, so B is false. y must survive the intervening x assignment to the return, giving C. The assignment to y kills its previous value; that old value is not used on its right-hand side, so D is false. Liveness concerns values needed in the future, not merely variables appearing somewhere later.

## Q46

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The outputs encode the count of true inputs: s is its low bit and k its high bit, proving A. Complementing three inputs changes count m to3−m, complementing both bits, proving C. k is1 for counts2 and3, so B is false. Several triples share a count, so D is false. These are full-adder outputs, not an injective code for the input triple.

## Q47

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

A new row did not exist when T1 acquired its row locks and need not conflict with them, so A holds. The newly qualifying row can appear in the repeated predicate query, producing a phantom(B). A suitable predicate/range lock can protect against that insertion(D). C incorrectly equates locking a current result set with locking the predicate's future membership. These statements do not assume an additional snapshot-isolation mechanism beyond the given locking behavior.

## Q48

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The candidate keys are AB and AC: A must be present, and either B or C supplies the other via the dependencies. All attributes are prime. Thus C→B satisfies3NF through its prime right-hand attribute, but C is not a superkey, violating BCNF. B is correct; A confuses primeness with determinant superkey status. C mistakes determinant size for a partial dependency of a nonprime attribute, and D omits needed B or C.

## Q49

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Reflection sends (x,y) to (y,x); clockwise rotation sends (u,v) to (v,−u). The composition is (x,−y), reflection in the x-axis. Thus A works for every point. B sends Q to (−2,0), C also sends Q to (−2,0), and D moves the origin; all conflict with the actual final positions. The order of transformations matters.

## Q50

**Correct answer:** D

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **C: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

For any w of length n, h(ww)=0^(2n), and every n≥0 occurs. Thus h(L)=(00)*, proving A and B. The image has only even lengths, so D is false. C is disproved by this very regular image: a many-to-one homomorphism can erase the distinguishing information responsible for non-context-freeness.

