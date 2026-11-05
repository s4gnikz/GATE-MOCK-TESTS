# Worked Solutions — GATE CS 2027 Mock Test 022

## Q1

**Correct answer:** C

A's and B's statements are logical opposites, so exactly one of them is true regardless of the coin's location. To have exactly one true label overall, C's statement must be false: the coin is in C. Thus C is correct; locations A and B each make two labels true, and D incorrectly denies the valid location.

## Q2

**Correct answer:** 20

The first half-turn maps(3,4) to(−1,−4), and the second maps that to(1,8). The displacement is(−2,4), with squared length4+16=20. Half-turns about different centres do not cancel: their composition is a translation.

## Q3

**Correct answer:** B

Selection rewards either of two attributes, so among selected applicants one attribute can compensate for the other. This can induce the reported association, supporting B as a possibility. A asserts causation and population generality without evidence. C contradicts the stated selection rule. D rules out a combination that the rule permits. A selected subgroup need not preserve population associations.

## Q4

**Correct answer:** 2

Fix one specified person to remove rotations. The other specified person must sit opposite. The two remaining distinct people can occupy the remaining seats in2! ways. Reflections are distinct, so these two are not identified.

## Q5

**Correct answer:** B

Overall rates are weighted departmental averages. For example, rates90%,50% with shares90%,10% give86%; later rates91%,51% with shares10%,90% give55%. Both rates rise but the overall rate falls, proving B possible and A false. C and D introduce changes not needed by the example. Comparing weighted averages requires checking the weights.

## Q6

**Correct answer:** 8

The cut rectangle has area2. Its preimages under the folds have x intervals[1,3] or[5,7] and y intervals[0,1] or[7,8]. These four rectangles have disjoint interiors and area2 each, for total8. The cut touches the folded sheet's boundary but not a fold line; no reflected areas overlap.

## Q7

**Correct answer:** 4

Chronological order is S,Q,P,R. In the current order, the inverted pairs are(P,Q),(P,S),(Q,S),(R,S): four. Each adjacent exchange can remove at most one inversion, giving a lower bound of four. Move S left three places to obtain S,P,Q,R, then exchange P,Q; four operations attain the bound. Rearranging arbitrary distant paragraphs in one step is not allowed.
## Q8

**Correct answer:** 4.5

Card3 always contributes3. Each of cards1 and2 precedes card3 with probability1/2 and then contributes its label. By linearity, the expected sum is3+1/2+2/2=4.5. Independence between the inclusion events is unnecessary.

## Q9

**Correct answer:** C

The statement explicitly allows withdrawal before inspection and forbids it afterward, exactly C. A ignores the post-inspection restriction. B invents an exception. D confuses ending a withdrawal right with cancellation. The timing qualifies the agreement's provisional nature.

## Q10

**Correct answer:** 6

After n days the first-to-second ratio is(3/2)^n/8. At n=5, (3/2)^5=243/32<8; at n=6 it is729/64>8. The ratio increases strictly, so day6 is the first crossing. Compare end-of-day values and require strict inequality.

## Q11

**Correct answer:** 1

All four inputs with a=0 are on-set or don't-care, so cube NOT a covers them and contains one literal. Any expansion to a literal-free cube would include off-set inputs with a=1. Thus this is the largest permissible prime cube that covers the on-set. Don't-care inputs may assist expansion but cannot override specified zeros.

## Q12

**Correct answer:** A, B, C

In a bipartition, each vertex needs three opposite-side neighbours, forcing each side to have at least three vertices. Six vertices therefore split3+3, and every vertex connects to all three opposite vertices. This is connected K3,3, proving A,B,C. A bipartite graph has no odd cycle, so D is false. The degree constraint forces the complete bipartite structure here.

## Q13

**Correct answer:** 2

Neither one-letter word resets: b is the identity and a maps the state set to{1,2}. Reading aa maps every state to2. Therefore the minimum length is2. Resetting concerns all starting states, not only a designated initial state.

## Q14

**Correct answer:** A, C

The only walk from s to t uses s→t and costs5. Vertex a cannot reach t, so its negative loop cannot affect this destination. A and C are true; D is false. Walk costs from s to a decrease without bound through repeated self-loops, disproving B. A negative cycle matters to a destination only if it can also reach that destination.

## Q15

**Correct answer:** 3

The midpoints are3,1,0. The first two comparisons move r to3 then1; the third sees1<2 and moves l to1. The interval is then empty. Total3 comparisons. The equal values require searching toward the left boundary, not returning at the first equality.

## Q16

**Correct answer:** 5

The initial root-to-leaf path costs three reads. Each of the two leaf-link advances costs one additional leaf read. Total5. Repeating a root search for every leaf would overcount under the specified linked traversal.

## Q17

**Correct answer:** 5

Classify by the unique occurrence's starting position. At position1, avoiding another occurrence forces the third bit to1, giving0010 and0011. At position2, both exterior bits must be1, giving1001. At position3, the second bit must be1, giving0100 and1100. Thus there are five. Treating occurrences as disjoint would mishandle strings containing000.
## Q18

**Correct answer:** A, C

The forced old value permits restoration if the uncommitted update reaches disk; A and C are true. Reversing the order creates a crash interval with changed data but no durable undo information, making B false. The rule orders logging before a particular write; it does not force all committed values to disk, so D is false. Recovery information and commit durability require distinct arguments.

## Q19

**Correct answer:** B

The lookup finds the new binding for the reused endpoint, so B describes a possible misdelivery. A assumes unavailable historical mapping information. UDP supplies no universal transport sequence-number protection, disproving C. Expiration is local state management and cannot guarantee absence of delayed datagrams, disproving D.

## Q20

**Correct answer:** 4

A finite parse consists of k unary S→S expansions followed by S→a. For k=0,1,2,3 this gives four distinct trees. Restricting the number of unary expansions makes the count finite even though the unrestricted grammar has infinitely many parse trees for a.

## Q21

**Correct answer:** 1500

The active window limit is min(6000,4500)=4500 outstanding bytes. Subtract3000 already outstanding to get1500 additional bytes. Congestion and receiver limits constrain the same flight size rather than adding together.

## Q22

**Correct answer:** 5

Three faults require three page reads. The two dirty victims also require writes; the clean victim does not. Total3+2=5 page transfers. A page fault is not necessarily exactly one disk transfer.

## Q23

**Correct answer:** B

The stated token classes give identifier x, two separate minus operators and unsigned integer12. B is correct. A invents a signed integer token, C violates identifier boundaries, and D introduces an explicitly excluded operator. Unary-versus-binary classification is deferred to parsing.

## Q24

**Correct answer:** 4

The visited bank numbers are3,1,7,5, then3. Equivalently the period is8/gcd(8,6)=4. The starting address shifts the visited residue class but does not change this period.

## Q25

**Correct answer:** A, B

Both forms derive only ab and ac, proving A. FIRST(A)={b} and FIRST(B)={c}, so one lookahead selects an X alternative, proving B. The original S alternatives both start with a, making C false. Left factoring changes common-prefix decision structure but does not generally eliminate ambiguity, making D false.

## Q26

**Correct answer:** 1

After both unlinks, the link count is zero but one open reference remains. Closing its descriptor removes that final reference, allowing reclamation. One further operation is needed. Unlinking names is not the same as closing open-file references.

## Q27

**Correct answer:** B

A tombstone makes lookup continue through5 to6, so B is correct. A would stop lookup prematurely. C destroys another live key. D cannot repair the probe chain for the remaining key and is not a coherent deletion operation. Deleted and never-used slots have different search meanings.

## Q28

**Correct answer:** A, B

The wait-for edges T1→T2 and T2→T1 form a cycle, so A is true. Aborting either and releasing its locks breaks the cycle, proving B. Two-phase locking ensures a serializability property, not deadlock freedom, so C is false. Simultaneous commit is neither possible while blocked nor necessary for recovery, making D false.

## Q29

**Correct answer:** 8

The first four coefficients of A are1,1,2,2. The product coefficient at degree3 is a0a3+a1a2+a2a1+a3a0=2+2+2+2=8. Equivalently,(1+2x²+x⁴)/(1−x)² contributes4 from degree3 of the denominator expansion and4 from the shifted term. Coefficients of a product require convolution, not squaring a single coefficient.
## Q30

**Correct answer:** 1

Both operands of the addition are unsigned int. The result is65537 modulo65536, which is1. The %u conversion matches the type. This is defined unsigned wraparound, not signed-overflow reasoning.

## Q31

**Correct answer:** 200

Old time=100×2+10×60=800 ns. New time=100×3+5×60=600 ns. Reduction200 ns. Saving five misses saves300 ns, but slower hits/lookups cost100 ns across the entire stream.

## Q32

**Correct answer:** 1

Exactly one decoder is enabled, and that decoder raises exactly one output. The other raises none. Therefore one of sixteen outputs is high. Sharing address inputs does not imply both enabled outputs are active.

## Q33

**Correct answer:** A, C, D

If either predicate holds universally, their pointwise disjunction does too, so A is true. On a two-element domain, let P hold only at the first element and Q only at the second. Then F is true but G false, proving C and disproving B. On a singleton, both reduce to the same P-or-Q statement, proving D. Universal quantification does not generally distribute over disjunction.

## Q34

**Correct answer:** 10

The row swap multiplies the determinant by−1, and scaling a column by−2 multiplies it by−2. Thus det(B)=5×(−1)×(−2)=10. Apply both operations, including their signs.

## Q35

**Correct answer:** 6

The four nonbase invocations add4+3+2+1=10 and each subtracts1 on return, for four subtractions. Final g=10−4=6. The base invocation contributes neither an addition nor a subtraction.

## Q36

**Correct answer:** A, C, D

The owner key together with the partial key distinguishes every room, proving A. Equal room numbers in different buildings disprove B and explain D. A required, non-null foreign key checks existence of the owner; combined with the composite Room key it implements this mapping, so C is true. A partial key is unique only relative to its owner.

## Q37

**Correct answer:** B

For fixed i, the inner work is1+2+4+...+2^floor(log2 i), which lies between i and2i. Summing over i=1..n givesΘ(n²), so B is correct. A counts doubling iterations but ignores their growing work; C multiplies by a spurious log factor; D ignores the outer linear range. Geometric inner workloads must be summed, not bounded by their maximum at every iteration.

## Q38

**Correct answer:** 5.625

Each101 part has length3 and value5 by the concatenation rule. The returned value is5+5/8=5.625. The fractional part is scaled by its digit length, including any leading zeros, not by its numerical magnitude.

## Q39

**Correct answer:** A, B, D

R−S={(1,y),(2,x)}, so its A-projection is{1,2}, proving A. Separately the projections are{1,2} and{1}, whose difference is{2}, proving B. The surviving(1,y) gives D and directly disproves C's proposed distributivity. Projection can collapse tuples that difference distinguishes.

## Q40

**Correct answer:** A

Ratios are2,1.8,1.8. The heuristic takes the weight6 item, leaving4, so neither remaining item fits and its value is12. The two weight5 items fit together and yield18. A is correct; B reverses the values, C uses forbidden fractional items, and D ignores the initially fitting items. Fractional-knapsack exchange arguments do not automatically apply to indivisible items.

## Q41

**Correct answer:** 3

All first-sequence blocks map to set0; cycling through three blocks in two LRU ways makes every one of its six references miss. The second sequence maps0 and6 to set0 and3 to set1; all three fit, producing only the three compulsory misses. Difference6−3=3. Total cache capacity is insufficient to predict misses without set placement.

## Q42

**Correct answer:** B, C

A one-bit pending indicator merges events that occur before clearing, so B is true and A false. A properly synchronized counter can represent their multiplicity, proving C. Arbitrarily close events can still merge even with a fast handler, so D's universal timing guarantee is false. Counting delivered interrupts need not count underlying device events.

## Q43

**Correct answer:** A, B, C

Choose x_n=1/(π/2+2πn) for value1 and y_n=1/(3π/2+2πn) for value−1; both approach0 positively. A and B are true and their different limits disprove D. Since |x sin(1/x)|≤|x|, the squeeze theorem proves C. Bounded oscillation can disappear after multiplication by a vanishing factor.

## Q44

**Correct answer:** 2

Bytes0,3 specify a three-byte payload65,66,67. The first read ends after66 and is incomplete. The second supplies67, then length0,2 and payload68,69, completing two messages. Reads and protocol boundaries differ; a buffer must retain partial header/payload data across reads.

## Q45

**Correct answer:** 3

The state cycle is01→10→11→01. Old states equal10 before edges2,5,8, so three pulses occur in eight edges. Outputs use the old state, and the initial state is examined on edge1 rather than after a preliminary transition.
## Q46

**Correct answer:** A, C, D

E[X]=0, E[Y]=2/3, and E[XY]=E[X³]=0, so covariance is0, proving A and C. Y=0 forces X=0, proving D and disproving independence B: P(X=0,Y=0)=1/3 differs from(1/3)(1/3). Zero covariance does not imply independence.

## Q47

**Correct answer:** 0.5

First round11/16=0.6875 to the nearest quarter:0.75. Rounding0.75 to halves is a tie between0.5 (raw coefficient1, odd) and1 (coefficient2, even), so it becomes1. Direct rounding of0.6875 to halves gives0.5. Difference1−0.5=0.5. Intermediate rounding can move a value onto a tie.

## Q48

**Correct answer:** 3

The lookup at0 remains valid at4 and9 but expires at10. The refreshed answer at10 is valid at19 but expires at20. Therefore misses occur at0,10,20: three upstream lookups. Cache hits do not extend the fixed expiry time under the stated rule.

## Q49

**Correct answer:** 820

(AB)C costs10×2×20+10×20×3=1000. A(BC) costs2×20×3+10×2×3=180. The saving is820. Parenthesization changes intermediate matrix dimensions while preserving the final product.

## Q50

**Correct answer:** A, B

On abab, the stack empties twice without underflow, so the machine accepts despite the forbidden alternation: A is true and C false. A separate post-b phase can reject any subsequent a, proving B. aabb pushes twice then pops twice and is accepted, disproving D. Stack balance alone does not enforce block order.

## Q51

**Correct answer:** 16

Choose f(1) arbitrarily in four ways; commutation forces f(2)=τ(f(1)). Since3 and4 are fixed by τ, their images must also be fixed by τ, giving two choices each from{3,4}. These choices satisfy every equation independently, so there are4×2×2=16 functions. Images of fixed points are constrained, while the swapped pair's image is determined by one free choice.

## Q52

**Correct answer:** B, D

A checksum can reject corrupt frames but does not restore lost data, disproving A. End-to-end acknowledgment/retransmission can recover losses across the path under the stated eventual-communication condition, proving B and D. A checksum validates one received frame under its error model, not complete arrival of all message data, so C is false.

## Q53

**Correct answer:** 13

Separate open calls create separate open-file descriptions and offsets. p advances to4 then6; q is independently set to7. Their sum is13. This differs from dup, which shares an open-file description and offset.

## Q54

**Correct answer:** A, B, D

F can only output values satisfying R, so A and D are true. G includes the infinite complement of finite S, making B true. Range-restricted negation is not inherently unsafe; F illustrates this, disproving C. Safety depends on how variables are bounded, not merely on the presence of negation.

## Q55

**Correct answer:** A, B, D

The byte offset of B[i,j] is4(5j+i). Its i-stride is4 and j-stride20, proving A and B. A row-major traversal of B advances j first, so consecutive elements generally lie20 bytes apart; C is false. The defined index mapping gives B[2,1]=A[1,2] as aliases, proving D. A transpose view changes strides and index interpretation without rearranging the underlying storage.
## Q56

**Correct answer:** A, C

The escaped function must still access valid storage for its captured variable, so A is true. A retained environment referenced by a closure supplies such storage, proving C. A reclaimed frame offers no such lifetime guarantee, making B and D false. Lexical visibility and storage lifetime are related but distinct requirements.

## Q57

**Correct answer:** A, B, D

Context-free languages are closed under intersection with a regular language, proving A. Since the complement of R is regular, C−R=C∩complement(R) is context-free, proving B. Union closure, with regular languages also context-free, proves D. C is false: taking R=Σ* would assert closure of all context-free languages under complement, which does not hold. For a concrete counterexample, the complement of{a^n b^n c^n} is context-free (union of malformed block order and unequal adjacent block-count cases), while its complement is not. Difference is asymmetric here.

## Q58

**Correct answer:** 4

The shared a+b node is one. Multiplying it by itself adds one. b+a is a distinct ordered-child addition node, adding one; the outer sum adds one. Total4. Sharing identical syntax does not automatically use commutativity to identify reversed operands.

## Q59

**Correct answer:** C

The pumping lemma is a necessary condition for regularity, not a characterization. Its conclusion alone therefore does not establish regularity, so C is correct. A incorrectly reverses the implication; B and D assert additional classifications not supplied by the condition. A failed attempt to contradict pumping is not a regularity proof.

## Q60

**Correct answer:** 4

Once slow has reached the cycle after three steps, equality requires the distance difference t between fast and slow to be a multiple of the cycle length4. The first t≥3 satisfying this is4. No earlier equality occurs in the noncyclic tail. The initial equality before either moves is explicitly excluded by the comparison rule.

## Q61

**Correct answer:** 8

Three instructions through five stages need3+5−1=7 cycles without stalls. The immediate load consumer requires one bubble because the value is available only after MEM. The second add's dependency is satisfied by EX forwarding with no extra bubble. Total8 cycles. Full forwarding does not remove this load-use timing gap.

## Q62

**Correct answer:** 0.125

The smallest normal is1.00×2^−2=1/4. With p=3, adjacent significands differ by1/4 of that binade's scale, so subnormal spacing is2^−4=1/16. The target3/32 lies halfway between1/16 and2/16. Ties-to-even chooses coefficient2, giving1/8=0.125. Gradual underflow keeps this spacing below the minimum normal.

## Q63

**Correct answer:** A, C, D

Threads in one process share its virtual address space and conventional descriptor table, so A and C are true and B false. Each thread still needs a separate execution context and ordinarily a separate stack, making D true. Shared resources require synchronization; sharing does not imply identical instruction pointers or stack contents.

## Q64

**Correct answer:** 1

The polynomial p(t)=t²−5t+7 maps both eigenvalues2 and3 to1. Eigenvalues of p(A) are consequently1,1, and its determinant is their product1. Equivalently Cayley–Hamilton gives A²−5A+6I=0, so the target matrix is I. Matrix entries need not be reconstructed.

## Q65

**Correct answer:** A, B, D

The consumer takes mutex then blocks on full=0, proving A. A producer can take an empty slot token but cannot take mutex, so it cannot insert and signal full, proving B. Any initially empty finite buffer still starts full=0, so merely increasing capacity does not fix the ordering, disproving C. Waiting for an item before taking mutex avoids holding that mutex while waiting on full, proving D.



