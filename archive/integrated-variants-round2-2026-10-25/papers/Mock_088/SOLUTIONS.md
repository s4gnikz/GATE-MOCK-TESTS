# Worked Solutions — Mock Test 088

## Q1

**Correct answer:** 0.24

The qualifying delayed journeys are in the last two rows, totaling14+10=24. The sampling population is all40+35+25=100 journeys, so the probability is 24/100=0.24. Dividing by 60 would answer a different, conditional question given duration over20 minutes.

## Q2

**Correct answer:** A

A punch away from both folds unfolds to all four sign combinations of its nonzero coordinates. A is exactly such a reflection orbit. B violates reflection symmetry, while C,D contain only two of the four distinct images. Being away from folds prevents coincident mirrored centres.

## Q3

**Correct answer:** A

Q introduces the missing entries and the comparison. P supplies that comparison's result, S uses the result to restore the entries, and R verifies the completed restoration. Thus Q,P,S,R is coherent. B mentions the result before introducing the comparison, C restores using evidence not yet supplied, and D verifies restoration before it occurs. The explicit restrictions exclude an unstated earlier operation that might otherwise rescue a different order.

## Q4

**Correct answer:** 36
**Concept:** Net work rates.

The inlets together fill 1/6+1/9=5/18 tank per hour. The observed net rate is 1/4. The leak removes 5/18−1/4=1/36 tank per hour, so a full tank takes 36 hours to empty.

**Common misconception:** Filling times cannot be added; rates must be combined first.

## Q5

**Correct answer:** B

**Concept:** Contextual vocabulary.

A conclusion open to revision is tentative, B. Irrevocable means it cannot be reversed; unrelated concerns relevance; unanimous concerns agreement among people. None of A,C,D expresses the stated revisability.

**Common misconception:** Selecting a word associated with authority rather than with uncertainty.

## Q6

**Correct answer:** 4
**Concept:** Conditional sample space.

The ten qualifying ordered outcomes are (1,2),(2,1), …, (5,6),(6,5), all equally likely. Each possible maximum 2,3,4,5,6 occurs twice. Its conditional mean is (2+3+4+5+6)/5=4.

**Common misconception:** The conditioning event changes which dice outcomes are relevant; the unconditional expected maximum does not apply.

## Q7

**Correct answer:** A, C, D

Substitution gives3,7,13, establishing A; at4 the rule gives16+4+1=21, proving D. The extra product vanishes at1,2,3 but not at4, so C is true and B false. Finite observations can support a pattern without uniquely determining its continuation.

## Q8

**Correct answer:** 3.6
**Concept:** Expected payout.

Different colours occur with probability 2×(3/6)(3/5)=3/5. The payout is 6 on that event and zero otherwise, so expectation is 6×3/5=3.6.

**Common misconception:** The second draw uses a denominator of five, not six.

## Q9

**Correct answer:** 11

The flip counts are1,2,1,3,1,2,1 for000→001→010→011→100→101→110→111. Their sum is11. Binary carries can flip several positions at once; this is not a Gray-code listing.

## Q10

**Correct answer:** 8

Concept: chord geometry. The perpendicular from the centre to the chord has length 3 and bisects the chord. A right triangle gives half-length sqrt(5²−3²)=4, so the chord length is 8. The difference of radii is not half the chord.

## Q11

**Correct answer:** A, B

If both read0 before either writes, both write1, giving A. If one increment completes before the other's read, the result is2, giving B. Shared memory supplies visibility/storage, not atomic compound operations, so C is false. Each computed write is based on0 or1, and only two increments occur, so3 cannot arise; D is false. Lost updates are possible without mutual exclusion or atomic increment.

## Q12

**Correct answer:** 0.02

Main memory is reached only after an L1 miss and an L2 miss conditional on that event. Probability0.1×(1−0.8)=0.02. The conditional L2 hit fraction must not be subtracted directly from the unconditional L1 miss fraction.

## Q13

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Circular-list pointer updates.

The first update bypasses node 1, making node 2 the head. Inserting 5 after old tail 4 sets 4.next=5 and 5.next=2. Updating tail to 5 leaves head=2. Thus traversal is 2,3,4,5. A retains the deleted node; B starts at the tail; D inserts 5 before rather than after node 4.

**Common misconception:** In a tail-only circular-list representation the head is defined indirectly as tail.next.

## Q14

**Correct answer:** 1

For n≥1, the coefficient of x^n in(1−2x)A(x) is an−2a(n−1)=1. In particular the coefficient at degree4 is1. Equivalently,(1−2x)A(x)=1/(1−x). Formal power-series manipulation does not require a numerical convergence radius.

## Q15

**Correct answer:** 5

Concept: write-allocate and dirty eviction. Store to block 0 fetches one line and dirties it. Store to block 1 writes back block 0 and fetches block 1. Load from block 0 writes back dirty block 1 and fetches block 0. Total=3 reads+2 write-backs=5. No final flush is requested, and the final load leaves a clean line.

## Q16

**Correct answer:** A, B, D

A new row did not exist when T1 acquired its row locks and need not conflict with them, so A holds. The newly qualifying row can appear in the repeated predicate query, producing a phantom(B). A suitable predicate/range lock can protect against that insertion(D). C incorrectly equates locking a current result set with locking the predicate's future membership. These statements do not assume an additional snapshot-isolation mechanism beyond the given locking behavior.

## Q17

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

1. Negating the outer quantifiers changes forall x exists y into exists x forall y.
2. Negating the conjunction gives NOT R(x,y) OR NOT forall z (R(x,z) -> z=y).
3. The inner negation is exists z [R(x,z) AND z!=y]. Substitution gives A. The original formula says each x has exactly one R-successor; its negation allows an x with none or more than one.
- Original option A: It follows all three quantifier and connective changes.
- Original option B: For a two-element identity relation the original is true, but this option is also true by choosing x!=y.
- Original option C: For a singleton empty relation the original is false, but this conjunction is false.
- Original option D: For a universal relation on two elements the original is false; this option is false because z=y defeats its universal conjunct.

## Q18

**Correct answer:** A

**Concept:** Compiler Design — Local optimization

Write initial values b0,c0. The first statement sets a=b0+c0. The second sets b=(b0+c0)-c0=b0. The third reads this restored b and sets c=(b0+c0)-b0=c0. Thus b and c end unchanged, and only a=b+c is required.

- **A:** True: a becomes the sum and b,c retain their original values.
- **B:** False: it changes b whenever b0 differs from c0.
- **C:** False: it changes c to b0+c0 rather than preserving c0.
- **D:** False: it generally changes both b and c.

**Common misconception:** Algebraic simplification must track which version of each variable an expression uses.

## Q19

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Asynchronous reset priority.

Asserting an asynchronous reset changes Q independently of a clock edge, so A holds even while the clock remains low. B describes synchronous reset, C incorrectly substitutes toggling, and D is unrelated to reset behaviour.

**Common misconception:** Applying the normal data-sampling edge condition to an asynchronous control.

## Q20

**Correct answer:** 6 (exact)
**Concept:** Index probes with cached data-page reuse.

Read the three index pages, then distinct data pages {4,7,9}. Repeated records on already read pages cause no additional read. Total 3+3=6.

**Common misconception:** Record count and distinct data-page count are different I/O measures.

## Q21

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Computer Organization and Architecture — Interrupts and DMA

DMA reads main memory rather than the processor's dirty cache copies. Writing back the buffer lines and waiting makes main memory contain the updates before DMA reads them. Discarding dirty lines loses modifications. Interrupt control changes notification, not visibility of cached data, and a completion event cannot precede starting the transfer.

- **A:** False: discarding dirty lines without write-back loses the updated data.
- **B:** True: completed write-back makes the DMA source in main memory current.
- **C:** False: interrupt masking does not update memory.
- **D:** False: this ordering cannot start the required transfer and does not flush the cache.

**Common misconception:** DMA bypassing the CPU does not automatically observe its dirty cache contents.

## Q22

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Characterizing a recursive grammar.

Each a is prepended and each b appended around the remaining S. Thus all generated words are a^n b^m, with counts independently chosen; every such word is obtainable. A is correct. B and C impose unjustified equal counts or alternation; D includes ba, which cannot be generated.

**Common misconception:** Assuming grammar ambiguity changes the generated language into all strings.

## Q23

**Correct answer:** B
**Concept:** Integer promotion and unsigned conversion.

The addition is performed after integer promotion and is representable; assignment converts the result back modulo 256. Starting at an even value and adding two modulo 256 always leaves i even. It never becomes 255, and every even eight-bit value is less than 255. The loop is infinite (B). A,C wrongly claim termination; D mistakes conversion wraparound for signed overflow.

**Common misconception:** Promotion does not prevent wraparound when a representable sum is assigned back to a narrower unsigned type.

## Q24

**Correct answer:** B

**Concept:** A counterexample to greedy coin selection.

Greedy chooses 4, then 1, then 1, using three coins. The feasible choice 3+3 uses two, and one coin cannot make six. Thus B is correct. A gives the wrong greedy count; C ignores denomination one; D ignores 3+3.

**Common misconception:** Assuming the familiar greedy rule works for every denomination system.

## Q25

**Correct answer:** 702
**Concept:** TCP sequence space.

SYN uses 400, data use 401 through 700, and FIN uses 701. Acknowledgment names the next expected sequence number, 702. Equivalently, compute 400+1+300+1.

**Common misconception:** SYN and FIN consume sequence numbers despite not being ordinary application data bytes.

## Q26

**Correct answer:** 130

**Concept:** Recomputing shortest-seek choices.

The initial tie between 45 and 55 chooses 45. The full order is 50→45→55→90→10, with distances 5,10,35,80. Their sum is 130. Each choice uses the head's current position, not its original position.

**Common misconception:** Sorting requests once by initial distance instead of making successive local choices.

## Q27

**Correct answer:** B

Concept: constant propagation. All feasible incoming paths establish x=4, so 3x−2=12−2=10. B is correct. A omits the subtraction; C is not the expression's value; D denies the justified substitution. A value known on only one incoming path would not suffice.

## Q28

**Correct answer:** 1

**Concept:** Edit-distance lower and upper bounds.

Substituting u for a changes cat into cut in one step. Zero edits cannot work because the strings differ. Therefore the optimum is one.

**Common misconception:** Using one deletion plus one insertion when a cheaper substitution is permitted.

## Q29

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Segment-bound checking before translation.

Valid offsets are 0–99, but 120 is outside that interval, so C holds. A adds the base before disregarding the bounds violation; B clamps the address without authorization; D ignores both base and validity.

**Common misconception:** Assuming every base-plus-offset calculation is a valid address.

## Q30

**Correct answer:** 839

The fragment starts at75·8=600 bytes. Its240-byte payload occupies offsets600 through600+240−1=839. The final byte has an inclusive offset, one less than the next byte's position.

## Q31

**Correct answer:** 28

The real sum is1.75, represented by integer1.75·16=28. Its positive eight-bit code also has unsigned interpretation28. The requested answer is the code, not the real sum.

## Q32

**Correct answer:** 10

The row swap multiplies the determinant by−1, and scaling a column by−2 multiplies it by−2. Thus det(B)=5×(−1)×(−2)=10. Apply both operations, including their signs.

## Q33

**Correct answer:** C

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Both one-sided function limits are0, matching f(0), proving A. Difference quotients are−1 from the left and1 from the right, proving B and disproving C. This same example disproves D. An extremum need not have zero derivative when differentiability fails.

## Q34

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Epsilon specifies no consumed input, not no state or stack action, so A,C are true. B overrestricts stack behavior, and D misinterprets epsilon as an actual character. Several internal moves may occur without advancing the input head.

## Q35

**Correct answer:** 5

Concept: conditional sample spaces. The eligible equally likely outcomes are (4,3),(5,2),(6,1). Their X values average to (4+5+6)/3=5. Conditioning on the sum alone would instead give 3.5.

## Q36

**Correct answer:** 10

An idempotent function fixes every point in its image. Choose its nonempty image of size k, then send each remaining point to any image point. Count sum C(3,k)k^(3−k) for k=1,2,3:3+6+1=10. The image choices and fixed-point requirements are linked, not independent arbitrary mappings.

## Q37

**Correct answer:** 1

Concept: subnormal spacing and rounding to zero. Minimum normal is 2⁻²=1/4; with two stored fraction bits, subnormal spacing is 2⁻⁴=1/16. The first product 1/16 is exactly representable. Multiplying by 1/2 gives 1/32, midway between zero and 1/16. Ties-to-even chooses zero. Relative error=|0−1/32|/(1/32)=1. Normal-range relative-error bounds need not hold at underflow.

## Q38

**Correct answer:** 8 (exact)

**Concept:** Databases — B-trees and B+ trees

Inserting 35 splits the middle leaf into [20,25] and [30,35]. The root now has four children and separators 20,30,40. Split it into two internal nodes, with separator 30 in a new root. The two child internal nodes have separators 20 and 40. At this point there are four leaves, two internal children and one root: seven nodes.

Inserting 55 splits [40,45,50,55] into [40,45] and [50,55]. Its parent acquires separator 50 and has three children, so it does not overflow. The final tree has five leaves and three internal nodes, for eight nodes.

**Common misconception:** A leaf split can trigger an internal split and creation of a root; later splits need not propagate to the root.

## Q39

**Correct answer:** 1

Three distinct eigenvalues imply a basis of eigenvectors. Applying polynomial p(t)=t²−3t+2=(t−1)(t−2) gives eigenvalues0,0,6 for B in that basis. Exactly one is nonzero, so rank B=1. Without diagonalizability, simply counting nonzero eigenvalues would not generally determine rank; it is justified here by distinct eigenvalues of A.

## Q40

**Correct answer:** 8

The subtree rooted at2 contains2,4,5,6, four vertices. Vertex7 originally has depth2. After attaching2 below7, its depth changes from1 to3, an increase2; every descendant of2 increases by the same2. The other vertices do not move, so total increase is4·2=8. Reattaching a subtree changes all its descendant depths, not just its root's.

## Q41

**Correct answer:** 78

The clock period is maximum stage delay5 plus overhead1, or6 ns. Four cycles produce the first result and nine more produce the next nine, totaling13 cycles. Time13×6=78 ns. Sum of unpipelined stage delays is not the pipeline clock period.

## Q42

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Recursion-tree cost with a nonuniform nested loop.

For each i, there are i iterations of j and Θ(log i+1) iterations of k. Summing gives Θ(n² log n), using the i values from n/2 through n for a matching lower bound. The recurrence is T(n)=2T(n/2)+Θ(n² log n). At successive recursion depths the quadratic factor drops geometrically after accounting for the number of subproblems, so total cost remains Θ(n² log n). A loses a loop factor; B loses the k loop's logarithm; D adds an unnecessary logarithm for recursion depth despite the geometric decrease.

**Common misconception:** Multiplying root work by recursion depth is incorrect when per-level work decreases geometrically.

## Q43

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** CFL closure with a regular constraint.

A PDA for L can be combined with a DFA for R by storing their finite control states together and retaining the PDA stack, proving A. CFLs are not closed under complement or arbitrary CFL intersection, so B and C are not guaranteed. D would include the complement of L by taking R to be the full language, so it too is not guaranteed.

**Common misconception:** Extending intersection closure with regular languages to arbitrary context-free languages.

## Q44

**Correct answer:** C

The pumping lemma is a necessary condition for regularity, not a characterization. Its conclusion alone therefore does not establish regularity, so C is correct. A incorrectly reverses the implication; B and D assert additional classifications not supplied by the condition. A failed attempt to contradict pumping is not a regularity proof.

## Q45

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Concept: ordered auto-increment addressing. Source read uses 100 and gives three, then R becomes 104. Destination read uses 104 and gives five, then R becomes 108. The sum eight is written to captured destination 104. C=(108,8). A and D omit an increment; B reads the wrong destination value. The explicitly stated evaluation order resolves reuse of the same address register.

## Q46

**Correct answer:** A, B

There are finitely many strings in each bounded-length set. Run M on every candidate; the promise guarantees every run finishes, allowing A,B to be decided. The promise does not bound the number of inputs. For undecidability, construct a total machine that simulates a chosen machine on a fixed input for |w| steps. Accepting iff it has halted makes emptiness equivalent to nonhalting; accepting iff it has not halted makes universality equivalent to nonhalting. Thus C,D remain undecidable even on promised total machines. A per-input termination guarantee is not a bound on all inputs collectively.

## Q47

**Correct answer:** 62

A hit costs 2+50=52ns. A miss costs 2+3×50=152ns. The weighted mean is 0.9×52+0.1×152=62ns. Resident pages avoid disk faults, but a TLB miss still pays page-table memory accesses.

## Q48

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

The /25 covers addresses128–255 and is more specific, so200 uses Y and100 uses X: A,B are true. Lookup is based on prefix length, not installation order, making C false. Removing the /25 leaves the matching /24 for200, proving D.

## Q49

**Correct answer:** B

**Concept:** Reverse translation of multiplexed connections.

The public translated ports distinguish the clients' connections, and the translator needs the corresponding mapping back to internal endpoints. B provides that information. A ignores the distinguishing field; link broadcast addressing (C) and payload length (D) cannot identify the internal connection.

**Common misconception:** Assuming the server endpoint alone uniquely identifies a connection through a shared public address.

## Q50

**Correct answer:** A, C
**Concept:** Recovery conditions versus serializability.

T2 reads from T1 and commits after T1; T3 reads from T2 and commits after T2, so the schedule is recoverable. Both reads occur before the producing transaction commits, so it is neither cascadeless nor strict. Conflict edges are T1→T2→T3 with no cycle. Thus A,C hold and B,D fail.

**Common misconception:** Recoverability permits dirty reads if commit dependencies are respected; cascadelessness does not.

## Q51

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Aggregate analysis of parent-pointer traversal.

Across the entire traversal, each downward tree edge is followed once to visit its child, and each upward edge is followed at most once when a subtree is exhausted. All constant work over n successor operations plus at most n−1 downward and n−1 upward traversals is O(n). Visiting all n nodes also gives Ω(n), hence Θ(n). A cannot account for visiting n nodes. C,D incorrectly multiply the worst single-operation cost by n; even on a path, the final long ascent occurs only once.

**Common misconception:** A worst-case O(height) successor call does not imply O(n×height) total traversal time.

## Q52

**Correct answer:** 1.2308 (range 1.23075–1.23085)

**Concept:** CPI versus elapsed instruction time.

A's CPI is 1+0.30×0.10×20=1.6, giving 1.6 ns per instruction. B's CPI is 1+0.30×0.05×20=1.3. For period T, require 1.3T≤1.6, or T≤16/13=1.230769… ns. Rounded answer 1.2308; accepted range 1.23075–1.23085.

**Common misconception:** Comparing CPIs without accounting for different clock periods.

## Q53

**Correct answer:** 0.25

Absorption gives F=a OR (b AND c), whereas G=a AND (b OR c). If a=0, the outputs differ exactly at b=c=1. If a=1, they differ exactly at b=c=0. These are two of eight equally likely inputs, so the probability is 1/4. Distributing one expression does not make the two circuits identical.

## Q54

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Key 7 must be the root. Key 6 is already at index 3. If 5 were at index 4 or 5, its parent at index 2 would have to exceed 5; both available larger keys are already elsewhere. Index 2 is possible, and indices 6,7 have parent 6, so each is possible. Hence exactly {2,6,7}: C. A excludes feasible child positions; B includes impossible positions 4,5; D includes the root occupied by 7.

## Q55

**Correct answer:** 3

No four-cell cube avoids both000 and111: fixing any one variable still admits one of them. Thus a valid cube covers at most two of the six1-inputs, giving a lower bound of three terms. The cubes a'c, bc' and ab' cover disjoint pairs001/011,010/110,100/101, attaining three. A power-of-two group cannot cross a specified zero.

## Q56

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Rank of a composition.

The image of B has dimension three. A's one-dimensional kernel can remove at most one dimension from that image, so rank(AB)≥2, proving A and excluding C. Taking A=B=diag(1,1,1,0) gives rank three (B). Taking A=diag(1,1,1,0) and B=diag(1,1,0,1) gives AB=diag(1,1,0,0), rank two (D).

**Common misconception:** Knowing the two individual ranks does not uniquely determine the product rank; the kernel/image alignment matters.

## Q57

**Correct answer:** 5

Concept: sparse double-indirect allocation. Each pointer block holds 1024 pointers. Direct blocks cover 0–7; single-indirect covers 8–1031. Block 1032 is double-indirect offset zero, requiring a double-indirect root, one child pointer block and one data block. Block 2061 has double-indirect offset 1029=1024+5, requiring a different child pointer block and its data block but reusing the root. Total=3+2=5. Unwritten intervening file holes consume no blocks.

## Q58

**Correct answer:** B, C

The original components are{a,b,c},{d,e},{f}, linked in that order. There is no path back from d to c, refuting A, and f has no outgoing edge, refuting D. Adding f→b closes a directed cycle among all components, proving B. Reversing all edges reverses mutual paths but preserves their existence in both directions, proving C. One-way reachability between components is insufficient for strong connectivity.

## Q59

**Correct answer:** 3

The edge AD of weight2 is uniquely cheapest across the cut isolating D, so every MST includes it. Connecting A,B,C then requires two of the three unit triangle edges, with three choices. All have total weight4; using BD of weight3 would increase the weight. Thus there are3 MSTs. Equal edge weights allow distinct optimal trees without changing their common cost.

## Q60

**Correct answer:** 64

**Concept:** Counting signed overflow pairs.

Overflow occurs for two nonnegative operands summing to at least eight, or two negative operands summing below −8. For values 0–7, the first count is 1+2+…+7=28. Write negative magnitudes as 1–8; sums greater than eight occur in 1+2+…+8=36 ordered pairs. Opposite signs cannot overflow. Total 28+36=64.

**Common misconception:** Counting unordered pairs or excluding the asymmetric endpoint −8.

## Q61

**Correct answer:** A, C, D

**Concept:** Engineering Mathematics — Conditional probability and Bayes theorem

1. P(N>=2)=P(first positive)=11/40. Reaching test 3 requires the first two positives, whose probability is (1/4)(4/5)^2+(3/4)(1/10)^2=67/400. Thus E[N]=1+11/40+67/400=577/400.
2. N=3 does not disclose the third result. P(faulty | N=3)=[(1/4)(4/5)^2]/(67/400)=64/67. The value 512/515 would instead condition on three positives.
3. Exactly two positives before a negative is the path ++-. Faulty and sound weights are (1/4)(4/5)^2(1/5)=128/4000 and (3/4)(1/10)^2(9/10)=27/4000, giving posterior 128/155.
4. Positive first and negative stopping includes paths +- and ++-. With conditional positive probability p, their total probability is p(1-p)+p^2(1-p)=p-p^3. Faulty and sound weighted probabilities are 288/4000 and 297/4000. Their posterior ratio is 288/585=32/65.

- **A:** The tail-sum formula uses the probabilities of reaching the second and third tests.
- **B:** Reaching three tests means only that the first two were positive; the third may be negative.
- **C:** This conditions on the specific path ++-, with weights 128 and 27.
- **D:** The two possible terminating paths give weights 288 and 297, whose normalized faulty weight is 32/65.

**Common misconception:** The number of tests performed and the number of positives are different observations under a stopping rule.

## Q62

**Correct answer:** A, D

Let the original operands be a0,b0, so t=a0+b0. Path P makes the sum a0+1+b0=t+1, proving A. Path Q leaves it t, making the path-dependent selection in D valid. Global reuse of t in B misses the increment. Assigning a does not mutate the already computed scalar t, refuting C. Dependency of a value at computation time is not an ongoing reference link.

## Q63

**Correct answer:** 5

dup creates another descriptor referring to the same open-file description, including its shared offset. The first read sets it to6; the seek sets it to2; the final read advances it to5. Descriptor4 therefore observes5. Separate descriptor numbers do not imply separate file offsets.

## Q64

**Correct answer:** 3

Concept: outstanding data versus two window limits. First allowance=min(10,12)−8=2, making flight size ten. ACK of five leaves five outstanding. The new limit is min(8,6)=6, so only one more segment can be sent. Total new segments=2+1=3. An ACK frees space relative to both the remaining flight size and the updated limiting window.

## Q65

**Correct answer:** 5

**Concept:** Wait-for edges for lock conflicts and upgrades.

T1's X(B) waits for T2 and T3, giving two edges. T3's X(A) waits for T1 and T2, giving two more. T2's upgrade to X(A) waits for T1, not for its own shared lock, giving one more. Total five edges; no self-edge is added.

**Common misconception:** Treating a lock-upgrade request as waiting on the transaction's own compatible existing ownership.

