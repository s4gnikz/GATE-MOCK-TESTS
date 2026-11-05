# Worked Solutions — Mock Test 082

## Q1

**Correct answer:** C

**Concept:** Vocabulary in context.

The following clause explicitly attaches a condition to the endorsement, establishing C. A is a different meaning of “qualified” and is not supported here. B removes the condition, while D denies the support that the sentence explicitly reports.

**Common misconception:** Choosing a familiar dictionary meaning without checking its context.

## Q2

**Correct answer:** 10

Concept: powers dividing a factorial. Multiples of two contribute six factors, multiples of four contribute three additional factors, and the multiple of eight contributes one more. Thus the exponent is floor(12/2)+floor(12/4)+floor(12/8)=6+3+1=10. Counting just the even factors misses their extra powers of two.

## Q3

**Correct answer:** A, C

The base2 and increments of2 reach every even integer, proving A. They never reach an odd integer, so B,D do not follow. A separate odd base3 starts the odd chain; together the two chains cover every n≥2, proving C. The induction step's stride determines which base cases are needed.

## Q4

**Correct answer:** 72

The original outside surface has6×9=54 unit faces. Removing the six face-centre cubes removes six old exposed squares, leaving48 exterior squares. Each removed face-centre cube exposes four side faces of neighboring remaining cubes; its inward neighbor is the removed central cube. These six disjoint sets add24 faces. The central removed cube has only removed face-centre cubes as neighbors, so it adds no further boundary against the remaining solid. Total48+24=72. Counting six new faces for every removed cube would count contacts between two removed cubes.

## Q5

**Correct answer:** 15 (exact)

**Concept:** General Aptitude — Numerical series

1. Let d_n=a_n-a_(n-1). Subtracting a_(n-1) from the recurrence gives d_n=d_(n-1)+n.
2. Starting from d2=3, obtain d3=6, d4=10 and d5=15.
3. Therefore a5-a4=15. Direct terms 2,5,11,21,36 give the same result.

**Common misconception:** A second-order sequence can become a simpler first-difference pattern.

## Q6

**Correct answer:** 2

Each square has area16. An area28 union implies overlap32−28=4. The overlap is a square of side4−t, so(4−t)²=4. Because0≤t≤4, 4−t=2 and t=2. The other algebraic root lies outside the allowed displacement range.

## Q7

**Correct answer:** C

The subject immediately following the introductory participial phrase should be the person who performed the digitizing: the archivist. C supplies that subject and preserves the intended claim. A makes searching the apparent digitizer, B makes the facility the digitizer and changes the claim, and D makes the documents the digitizer. A passive main clause does not automatically repair a dangling introductory modifier.

## Q8

**Correct answer:** 24
**Concept:** Adjacency exclusion.

Choose C's end seat in two ways. For each choice, the four remaining people have 4!=24 orders, of which 2×3!=12 place AB or BA together as a block. Therefore 2(24−12)=24 valid orders remain.

**Common misconception:** Exclude both internal orders of an adjacent pair.

## Q9

**Correct answer:** A, B, D

If p were true, the implication would force q true, contradicting exactly one true proposition. Thus A holds. The sole true proposition must be q or r, giving B and D. Either can be the true one, so C is not forced.

## Q10

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Composition of a rotation and an offset reflection.

R sends(x,y) to(-y,x). Reflection about x=1 sends(u,v) to(2-u,v), so one pair T sends(x,y) to(2+y,x). Applying the pair twice gives T²(x,y)=(x+2,y+2), and four times gives T⁴(x,y)=(x+4,y+4). The final point is(6,5), option B. A incorrectly assumes the composition has order four. C is the result of a half-turn about the origin, which is not the specified composite. D is not obtained by the specified sequence; the intermediate points are(3,2),(4,3),(5,4),(6,5).

**Misconception:** Treating a rotation followed by an offset reflection as a rotation about the origin.

## Q11

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: pivoting in LU decomposition. det(A)=−1, so A is nonsingular (A true). Write L=[[1,0],[l,1]] and U=[[u,v],[0,w]]. From the first row u=0,v=1, but then (LU)21=lu=0, contradicting A21=1; B is false. Swapping rows gives the identity, factored as I·I, so C is true. This nonsingular matrix itself disproves D. Invertibility does not guarantee a nonzero first pivot.

## Q12

**Correct answer:** 0.3333 (accepted range 0.33325–0.33335)

The fundamental theorem gives F'(x)=2x+1, while direct integration gives F(x)=x²+x. Hence xF'(x)−F(x)=2x²+x−x²−x=x². Its integral on [0,1] is 1/3≈0.3333. Differentiating F and evaluating F are distinct steps; the integration variable t is a dummy variable.

## Q13

**Correct answer:** 2

One resource remains free. It can satisfy either process's outstanding request; that process then finishes and releases its two resources. Both processes are possible first finishers, so the answer is2. Holding one resource each does not imply deadlock while a suitable resource is still free.

## Q14

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The lookup finds the new binding for the reused endpoint, so B describes a possible misdelivery. A assumes unavailable historical mapping information. UDP supplies no universal transport sequence-number protection, disproving C. Expiration is local state management and cannot guarantee absence of delayed datagrams, disproving D.

## Q15

**Correct answer:** 1

Any b sends the machine to the rejecting sink permanently. Only aaaa is accepted at length4, giving one string. The accepting initial state also accepts ε, but that string has length0 and is excluded here.

## Q16

**Correct answer:** 12

Concept: pointer and pointee increments. `*p++` means `*(p++)`: x receives 2 and p advances to a[1]. `++*p` increments that element from 4 to 5 and gives y=5. The sum is 2+5+5=12. Incrementing a pointer and incrementing the pointed value are different operations.

## Q17

**Correct answer:** 10

The burst2 job starts at0. After it ends at2, one switch delays the burst3 job to3. That job ends at6, and the next switch delays the burst5 job to7. Waiting times are0,3,7, totaling10. Context-switch time is waiting time for jobs still ready.

## Q18

**Correct answer:** A
**Concept:** SQL aggregate treatment of NULL and duplicates.

COUNT(*) counts four rows. COUNT(x) excludes the one NULL but retains both rows with value 2, giving three. A is correct. B excludes NULL from COUNT(*); C,D mistakenly apply DISTINCT.

**Common misconception:** COUNT(column) is not COUNT(DISTINCT column).

## Q19

**Correct answer:** 40

The transformed mean is10−2×4=2 and variance is(−2)²×9=36. Therefore E[Y²]=Var(Y)+(E[Y])²=36+4=40. Translation changes the mean but not variance; negative scaling still squares in the variance.

## Q20

**Correct answer:** 6

The four nonbase invocations add4+3+2+1=10 and each subtracts1 on return, for four subtractions. Final g=10−4=6. The base invocation contributes neither an addition nor a subtraction.

## Q21

**Correct answer:** B

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Right inverses throughout a monoid.

For a, choose b with ab=e. Choose c with bc=e. Associativity gives a=a(bc)=(ab)c=c, hence ba=bc=e. Thus every a has a two-sided inverse, establishing A and the group property B. Groups need not commute (C false), and inverses must satisfy the equations rather than being arbitrary (D false, as any nontrivial group illustrates).

**Common misconception:** Assuming one-sided inverses remain one-sided when the inverse-existence condition applies to every element.

## Q22

**Correct answer:** A, C, D

The nullable foreign key permits NULL, proving A. A non-null value must match an existing id, proving D; its own id is a possible match, proving C. Mutual references between two existing rows also satisfy the foreign key, disproving B. Referential integrity does not impose an acyclic hierarchy.

## Q23

**Correct answer:** C

Candidates I, IV are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) IV.
- **B: Incorrect.** It includes invalid candidate(s) II, III and omits valid candidate(s) I, IV.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

1. The separator deterministically identifies the midpoint. Push each pre-separator bit, then match each later bit to the stack top and pop; accept only after the input ends with the data stack empty.
2. LIFO order compares against reverse(w), not w in its original order.
3. Choosing w=epsilon gives #, which is accepted with an empty data stack.
- Original option A: The separator removes the need to guess when to switch phases.
- Original option B: Remaining symbols mean the second half was too short.
- Original option C: For w=01, input 01#01 fails this test, while 01#10 passes it.
- Original option D: The definition allows the empty string for w.

## Q24

**Correct answer:** A, C

A strict greater-than shift never moves an equal predecessor past the key, so A holds. On sorted input no predecessor exceeds its key, proving C. A non-strict comparison can move equal records past each other, disproving B. Shifts correspond to strict inversions; distinct descending records already disprove D. Equality is crucial to stability but not to the shift count claimed in D.

## Q25

**Correct answer:** B

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Correct.** It includes both valid candidates and no invalid candidate.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Error-detection parity.

Each flipped bit toggles total parity. Any odd number of flips changes even to odd and is detected, proving A,C. Two flips restore the original parity, refuting B; the same counterexample refutes D.

**Common misconception:** A parity bit detects every odd-weight error, not every nonzero error.

## Q26

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Databases — Functional dependencies and normal forms

Neither A nor B determines C, so candidate keys are AC and BC. Every attribute is prime because each occurs in a candidate key. Each nontrivial dependency has a prime right-side attribute, satisfying 3NF. A→B violates BCNF since A is not a superkey, and similarly for B→A. Thus 3NF but not BCNF.

- **A:** False: every attribute is prime, so there is no nonprime partial dependency violating 2NF.
- **B:** False: prime right-side attributes satisfy 3NF.
- **C:** True:3NF holds while A and B are non-superkey determinants.
- **D:** False: A→B is nontrivial and A does not determine C.

**Common misconception:** Third normal form allows a prime dependent attribute even when the determinant is not a superkey.

## Q27

**Correct answer:** C
**Concept:** Static hazards and the consensus term.

Before and after A changes, F is 1. Unequal direct and complemented path delays can temporarily make both original products 0. BC remains 1 throughout, bridging the transition. It is redundant: when BC=1, either AB or (NOT A)C already makes the steady-state output 1. AC and A(NOT C) still depend on A; the latter is also 0 here and changes the function elsewhere. (NOT B)C is 0 during this transition and changes the function, for example at A=1,B=0,C=1. Thus A,B,D fail.

**Common misconception:** Boolean equivalence alone does not ensure glitch-free behaviour under unequal delays.

## Q28

**Correct answer:** A

The device continues asserting the interrupt level while its status remains1, permitting redelivery(A). Acknowledging the controller does not inherently acknowledge or clear the device's own condition, so B is false. Neither transfer rollback(C) nor a change in electrical trigger semantics(D) follows. The handler must address the source condition as required by the device interface.

## Q29

**Correct answer:** 3

**Concept:** Matching bottlenecks and a construction.

The three vertices a,b,c together have only two neighbours, so at most two of them can be matched. Vertex d adds at most one match, giving an upper bound three. The matching a–1,b–2,d–3 attains it.

**Common misconception:** Inferring a perfect matching just because the two bipartition sides have equal size.

## Q30

**Correct answer:** A, C

Don't-cares may be used to enlarge useful cubes, proving A, but they need not be covered, refuting B. OFF inputs must remain0, so C is true. Covering only don't-cares cannot satisfy an additional required ON input and is not mandatory, refuting D. Optimization freedom is not an additional output requirement.

## Q31

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

## Q32

**Correct answer:** B
**Concept:** Linear probing and deletion markers.

All inserted keys hash to 3, occupying indices 3,4,5. Deleting 17 leaves a tombstone at 4. Searching 24 examines 3,4,5: three probes. The known-absent 31 then occupies tombstone 4. A and D stop the search too early; C ignores the reusable tombstone.

**Common misconception:** A tombstone may be reused by insertion but cannot terminate a lookup chain.

## Q33

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Expression kills and a must-analysis join.

Changing c does not change either operand, so the first predecessor preserves availability (A). Assigning a invalidates the previously computed value of a+b on the second path, refuting B. The must join intersects predecessor facts and therefore omits the expression (C). Union could falsely reuse a value on the second path, so D is unsound.

**Common misconception:** Having evaluated an expression somewhere earlier is insufficient if an operand was subsequently assigned.

## Q34

**Correct answer:** B

**Concept:** FIRST and FOLLOW in LL(1) parsing.

At S the alternatives begin with distinct a and b. At A and B, c selects the nonempty production and the end marker in FOLLOW selects ε. No table cell has two entries, proving B. A ignores separate nonterminals and lookaheads; C ignores the leading symbols; D claims nonexistent left recursion.

**Common misconception:** Declaring a conflict merely because terminal symbols occur in different productions.

## Q35

**Correct answer:** 5

**Concept:** Decoder indexing.

101₂ is decimal five, so D5 is asserted. The one-hot output index is five, rather than the number of asserted outputs, which is one.

**Common misconception:** Confusing decoded position with Hamming weight.

## Q36

**Correct answer:** 7

There are four distinct referenced data pages:7,19,44,80. Buffer retention permits one read of each despite multiple qualifying records. Adding3 index reads gives7. Charging one data-page read per record would overcount repeated pages; a noncovering index still requires fetching the distinct data pages.

## Q37

**Correct answer:** C

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

After locating the lower bound, linked leaves permit ordered scanning, proving A and disproving B. Separator values can also appear among leaf keys, so C is true. The links still require a starting leaf to be located, disproving D. Search navigation and sequential continuation are complementary.

## Q38

**Correct answer:** A, D

Concept: SSTF starvation under arrivals. The head alternates between tracks 0 and 1, each new nearby request being closer than track 100. Thus the far request can wait forever, A, disproving B. A finite request set decreases by one per completed service and cannot sustain this infinite pattern, so C is false and D true. Low immediate seek cost is not a waiting-time guarantee.

## Q39

**Correct answer:** A, B, D

If the complement were regular, complementing it again would make L regular, a contradiction; A is true. The union in B equalsΣ*, which is regular. C is false: for L={a^n b^n}, intersection with the infinite regular language a* is just{ε}. For D, if deleting a finite set made L regular, adding back the finitely many removed words would make L regular by closure under finite union; this is impossible. Nonregularity is not preserved under every intersection.

## Q40

**Correct answer:** 2

The cycles are0→1→3→0 and2→5→4→2. They partition all six indices, so there are2 cycles. The omitted residue6 maps to itself in the full modulo7 mapping but is not an array index here.

## Q41

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Pumping twice adds k=|v|, with1≤k≤p. Since(p+1)²−p²=2p+1>p, the new length lies strictly between consecutive squares, proving A. Primality is irrelevant and not guaranteed(B); the next square is too far away(C); pumping twice increases rather than decreases length(D). The interval argument covers every legal block length, not one selected decomposition.

## Q42

**Correct answer:** A, C

Reusing the same tag can match an old virtual-page entry and produce an obsolete frame, making A true. Invalidating the tag's entries removes those stale hits, so C is true. ASIDs distinguish concurrently assigned address spaces only when reuse is managed; B is false. The lookup key in the question omits the page-table base, so changing that base alone does not guarantee a miss, making D false.

## Q43

**Correct answer:** 0.8
**Concept:** Polling versus interrupt CPU overhead.

Polling occurs 1,000,000/50=20,000 times per second and costs 40,000 microseconds, or 4.0% CPU time. Interrupts cost 4000×8=32,000 microseconds, or 3.2%. The saved fraction is 4.0−3.2=0.8 percentage points.

**Common misconception:** The relative reduction is 20%, but the requested difference in percentage points is 0.8.

## Q44

**Correct answer:** 0.75

**Concept:** Recovery-path lengths and expected first-entry time.

The five valid initial states contribute zero. Invalid 6 reaches 2 in one edge; 5 follows 5→6→2 in two; 7 follows 7→5→6→2 in three. The uniform expectation is (1+2+3)/8=0.75 edges.

**Common misconception:** Averaging only over invalid initial states despite the specified distribution over all states.

## Q45

**Correct answer:** A, C

Pinning prevents eviction/reuse until the physical-address transfer finishes, proving A. If the frame is reused, the device still targets that same physical address and may corrupt the new allocation, proving C. A stable virtual name does not prevent physical reuse, refuting B, and D contradicts the stated DMA addressing model. Page-table remapping and device address state require coordination.

## Q46

**Correct answer:** A, C

Both calls pass the same starting buffer address. The first places A,B at positions0,1; the second places C,D,E at0,1,2, overwriting earlier bytes. A is true and B false. Using buf+n retains the first n bytes and writes subsequent bytes after them, proving C. D is false because network order does not prevent an application from choosing an incorrect destination address. Successful total byte counts alone do not prove correct assembly.

## Q47

**Correct answer:** 21

**Concept:** Floyd meeting time and reset phase.

Once both pointers are in the cycle, their positions agree when the slow step count is a multiple of five. The first such count at least the prefix length three is five, so phase one has five iterations and 15 traversals. Resetting one pointer to the head makes them meet at the entry after three paired steps, adding six traversals. Total 21.

**Common misconception:** Counting iterations as traversals or counting the pointer reset as walking the prefix.

## Q48

**Correct answer:** 3

Concept: primitive cyclic arrangements. There are C(6,3)=20 labelled words. A smaller least period divides six. Period one cannot give three ones; period three repeats twice and has an even total number of ones. Period two gives only 010101 and 101010. Excluding these leaves 18 words, each in an orbit of six distinct rotations. Therefore 18/6=3 classes. Division by six is valid only after removing shorter-period words.

## Q49

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Register coloring and an odd cycle.

A five-cycle has edges but no triangle, so its largest clique has size two. Alternating two colors around the cycle forces equal colors at the closing edge, making two registers insufficient. Three suffice, for example a=1,b=2,c=1,d=2,e=3. B is correct. A misses the odd-cycle obstruction; C,D invent a triangle, and D also overallocates registers.

**Common misconception:** The maximum clique gives a lower bound on required colors, not always an exact answer.

## Q50

**Correct answer:** B

For fixed i, the loop executes floor(n/i) times. Summing gives sum from1 to n of floor(n/i). This lies between nHn−n and nHn, where Hn=Θ(log n), so the total isΘ(n log n). B is correct. A ignores the harmonic factor; C and D exceed the tight growth rate. Varying strides prevent multiplication of two uniform loop bounds.

## Q51

**Correct answer:** A, C

Commit can be durable while data remains only buffered, so redo may be needed(A). Forcing a position in a sequential log can make all earlier records durable(C). WAL requires the update's log record to be durable before its data page is flushed, contradicting B. Missing flushed data for a committed transaction calls for redo, not automatic undo(D).

## Q52

**Correct answer:** 0.5333 (range 0.53325–0.53335)

**Concept:** Exponential races and memorylessness.

The first event time min(X,Y) is exponential with rate 5, with mean 1/5. Conditional on X winning the race, the first-event time retains this distribution: its conditional density is 5e^(−5t). By memorylessness, Y's remaining time then has mean 1/3. Under X<Y, the maximum is Y, so its conditional mean is 1/5+1/3=8/15=0.533333…. Accepted range: 0.53325–0.53335.

**Common misconception:** Using the unconditional mean of Y after conditioning on Y being the later event.

## Q53

**Correct answer:** 5.75

The six-bit signed scaled range is−32..31, or−8..7.75 after dividing by4. The first sum is4.5, the second exact sum9 saturates to7.75, and the final subtraction2 yields5.75. Summing first and saturating only once would incorrectly give7. Saturation is applied after each operation as specified.

## Q54

**Correct answer:** A, B

Concept: Huffman tie choices. Merge the two ones to make 2; then merge any two of the three weight-two nodes to make 4. Remaining weights are 2,4,4, one four being the original symbol. If the next merge uses the other four, the original four is a child of the final root and has length one (A). If it uses the original four, that symbol has length two (B). Its first possible merge is this penultimate merge, so depths three or four cannot occur; C and D fail. Equal-weight choices can change individual lengths while preserving optimal weighted cost.

## Q55

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Finite execution traces versus unbounded halting.

Simulating at most k steps decides acceptance and halting within that bound, establishing A,B. Recording the finite sequence of complete configurations permits exact repetition testing, establishing D. Unbounded halting for arbitrary M,x is undecidable, so C is false.

**Common misconception:** Treating bounded and unbounded execution questions as equally undecidable.

## Q56

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Implication transitivity gives p→r, proving A. Its contrapositive is NOT r→NOT p, proving B. The premises prohibit p true with r false, proving D. The converse r→p need not hold, so C is false. Implication chains do not reverse direction.

## Q57

**Correct answer:** A

The underlying question is correctly answered by B, C, D. This variant asks for its invalid answers, so select the complementary set: A.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Au=u−u(vᵀu)=0, so A is singular and A is false. If Ax=0 then x=u(vᵀx), putting x in span(u); conversely every such multiple is killed, proving B. Also vᵀA=0, so solvability requires vᵀb=0; when that holds, Ab=b and x=b works, proving C. Expanding A²=I−2uvᵀ+u(vᵀu)vᵀ=I−uvᵀ proves D. This is a projection, not necessarily an orthogonal projection because u and v need not coincide.

## Q58

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: duplicate minima. The two pushes of one store only one auxiliary minimum. Popping one removes that minimum even though the other one remains in the data stack, so A is true and B false. Storing equal minima as separate entries keeps their multiplicities synchronized, C. Never removing minima would retain values after their last occurrence was popped, so D fails. An auxiliary summary must represent duplicate occurrences or their counts.

## Q59

**Correct answer:** A, C
**Concept:** Combinational dependency depth.

The final carry can depend sequentially on all n propagation stages, taking n units (A). Extra lookahead/group logic can shorten that dependency chain (C). Physical simultaneous presence of gates does not remove signal dependencies, refuting B. The ripple bound grows with n, refuting D.

**Common misconception:** Gate parallelism and critical-path depth are different measures.

## Q60

**Correct answer:** D

The intended loads are2 and1, giving a[0]=3. The faulty first store sets a[0]=2; because k=0, the second statement then reads that changed2 for both terms, yielding4. Difference4−3=1, option D. A reverses the difference, B ignores aliasing, and C is not the difference between the two outcomes.

## Q61

**Correct answer:** 1

At magnitude 8, representable values immediately around 9 are 8 and 10. The midpoint rounds to 8 because its final significand bit is even. Thus fl(fl(8+1)−8)=0. On the other grouping, 1−8=−7 is exactly representable with three significant bits, and 8−7=1 is exact. The requested difference is 1−0=1. Rounding after intermediate operations breaks associativity.

## Q62

**Correct answer:** 11

Track K, the best nonempty subarray sum ending at each position with no deletion, and D, the best with exactly one deletion, allowing the last element to be the deleted one. Initialize K=4,D=−infinity. For each next x, set D'=max(D+x,K) and K'=max(x,K+x). The successive K values are4,3,5,−2,5,3,6; D values are −infinity,4,6,5,10,8,11. The maximum is11. It is attained by taking the full array and deleting −7. Removing an element anywhere in the array without respecting a contiguous enclosing interval is a different problem.

## Q63

**Correct answer:** 5

**Concept:** Persistent HTTP scheduling with a connection limit.

The initial handshake consumes RTT 1 and the HTML consumes RTT 2. During RTT 3 the existing connection fetches image 1 while the second connection opens. During RTT 4 both connections fetch images 2 and 3. RTT 5 fetches image 4. This is optimal: by time 4 only one image can complete on the first connection during RTT 3 and two during RTT 4, so at most three images could be done. The fourth requires a fifth RTT.

**Common misconception:** Treating the second connection as already available when the images are first discovered.

## Q64

**Correct answer:** B

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

## Q65

**Correct answer:** 14

Address 0 executes once. The outer loop runs for R=3,2,1, so address 1 executes three times and address 3 executes three times. Address 2 executes 3+2+1=6 times as S decreases to zero in each outer iteration. Address 4 executes once. Total clocks are 1+3+6+3+1=14. Counting branch targets without testing updated values can introduce an extra inner iteration.

