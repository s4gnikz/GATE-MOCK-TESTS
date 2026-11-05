# Worked Solutions — Mock Test 035

## Q1

**Correct answer:** C

The observed count can fall either because delays became less frequent or because people submitted fewer reports under the new procedure. With no independent arrival data, these explanations are not separated, so C. A,B assert a punctuality improvement not established by the evidence; D asserts the opposite causal effect without evidence. A change in reporting can change a measured indicator without the underlying service changing.

## Q2

**Correct answer:** 8

Fix A at seat 0 to quotient out rotations; B must occupy seat 3. Among remaining seats 1,2,4,5, the only adjacent pairs are{1,2} and{4,5}. Choose one of those pairs for C,D in two ways, orient C,D in two ways, and place E,F in the two remaining seats in two ways. Total 2×2×2=8. Reflection is not identified, so the reversed orientations remain distinct.

## Q3

**Correct answer:** 0.24

The qualifying delayed journeys are in the last two rows, totaling14+10=24. The sampling population is all40+35+25=100 journeys, so the probability is 24/100=0.24. Dividing by 60 would answer a different, conditional question given duration over20 minutes.

## Q4

**Correct answer:** 3

Unfolding horizontally turns the cut into a full-width strip across the original sheet at 0.5<y<1. Undoing the y=2 fold produces its reflected strip at 3<y<3.5. These two full-width removals divide the sheet into three horizontal pieces. The x fold does not create separate side-by-side holes because the removed strip spans the entire folded width, including the fold.

## Q5

**Correct answer:** A, C, D

F must precede each of I,A, and both must precede P, so F is first and P last(A,C). The middle events can be ordered I,A or A,I, giving exactly two possibilities(D). B holds only in the first order, not necessarily. A partial order specifies constraints rather than one uniquely determined narrative.

## Q6

**Correct answer:** 0.75

Describe an outcome by its repeated value r and singleton s. The condition max=5 permits r=5,s∈{1,2,3,4}, or s=5,r∈{1,2,3,4}: eight choices. Each corresponds to three equally likely dice-position orders. The sum2r+s is odd exactly when s is odd. Two choices in the first group and all four in the second qualify, so probability6/8=3/4. Counting only which face values occur would be unsafe without checking their equal numbers of ordered outcomes.

## Q7

**Correct answer:** B

The assessor must attend carefully to evidence while lacking a financial stake, so the intended quality is impartiality(B). A contradicts careful examination; C concerns competence, which is not specified; D introduces a predetermined negative conclusion, contrary to impartiality. “Disinterested” in this context does not mean “uninterested.”

## Q8

**Correct answer:** 45

The domain requires x>36/7. Since log4(x)=log2(x)/2, exponentiation gives x^(3/2)=7x−36. Put t=sqrt(x)>0: t³−7t²+36=0=(t−3)(t−6)(t+2). The positive roots3,6 give x=9,36, both within the logarithm domain. The root−2 is inadmissible because t is the positive square root. Sum9+36=45. The auxiliary variable's sign restriction prevents adding x=4 spuriously.

## Q9

**Correct answer:** B, C

For a list of length n, final position i holds the negative of original entry n+1−i under either order, proving B for all entries and lengths. Reversal and negation each undo themselves, and they commute; applying the composition twice restores the input(C). One example does not prove a universal statement(A), and commutation does not mean either operation is the identity(D). The argument applies equally to repeated values and an empty list.

## Q10

**Correct answer:** 18

Four separate cubes contribute24 unit faces. Exactly three pairs share full faces: the first and second, the second and third, and the third and fourth. Each shared face removes two exposed faces, giving 24−2×3=18. Other contacts are at most along edges or vertices and remove zero surface area.

## Q11

**Correct answer:** C

For x>0 the expression is 0; for x<0 it is−2. The one-sided limits disagree, so no value assigned at 0 can give continuity(C). A,B select only one side's value, and differentiability in B would also require continuity. D ignores the unequal limits.

## Q12

**Correct answer:** 3

A length-three string containing k copies of b advances3+k modulo4. Acceptance requires 3+k=4 since0≤k≤3, so k=1. Choose the sole b position in three ways: baa,aba,aab. The automaton adds different increments rather than merely counting one letter's parity.

## Q13

**Correct answer:** 0

E[X]=1,E[Y]=1/2, and XY equals1 only when X=1, giving E[XY]=1/2. Cov(X,Y)=1/2−1×1/2=0. This does not imply independence: Y is a nonconstant deterministic function of X. Zero covariance can coexist with dependence.

## Q14

**Correct answer:** A, C

If f(a1)=f(a2), applying g gives a1=a2, proving injectivity(A). Every a equals g(f(a)), so g reaches all of A(C). For a counterexample to B,D, take A={0},B={0,1},f(0)=0,and g(0)=g(1)=0. The stated identity holds, but f misses1 and f(g(1))=0≠1. A left inverse does not force a two-sided inverse.

## Q15

**Correct answer:** 5

In[1,2), the spacing is 1/8, giving 1.75 and1.875 in the requested interval. In[2,4), spacing doubles to 1/4, giving 2,2.25,2.5. There are five values. The exponent boundary changes the spacing; neither uniform1/8 nor uniform1/4 counting works throughout.

## Q16

**Correct answer:** A, D

Both A,D use unused primary keys and non-NULL code values. Reusing code 'X' is permitted because no uniqueness constraint applies to it. B duplicates id2 and C violates code's NOT NULL constraint. Constraints must be applied to the declared columns rather than inferred from the sample rows.

## Q17

**Correct answer:** B

The candidate keys are AB and AC: A must be present, and either B or C supplies the other via the dependencies. All attributes are prime. Thus C→B satisfies3NF through its prime right-hand attribute, but C is not a superkey, violating BCNF. B is correct; A confuses primeness with determinant superkey status. C mistakes determinant size for a partial dependency of a nonprime attribute, and D omits needed B or C.

## Q18

**Correct answer:** 3

The assignments fill B[2]=0, B[0]=1, B[4]=2, B[1]=3, and B[3]=4. Thus B=[1,3,0,4,2] is the inverse permutation. The nested lookup gives B[B[0]]=B[1]=3. The two arrays are distinct, so constructing the inverse does not overwrite A. Applying the inverse twice is different from composing A with its inverse.

## Q19

**Correct answer:** 0

The advertised right edge is 4200+600=4800, below the next unsent sequence5000. Therefore no new bytes fit in the current receiver window. Window shrinkage does not produce a negative allowance; the usable new-data allowance is clamped to zero. Already sent data and retransmission policy are separate issues.

## Q20

**Correct answer:** 13

For a2×2 matrix, trace(A²)=trace(A)²−2det(A). Thus25−12=13. Equivalently, eigenvalues sum to 5 and multiply to 6, so their squared sum is 13. This identity does not require choosing eigenvectors or assuming symmetry.

## Q21

**Correct answer:** A, B

Substituting x=0 leaves y AND1=y, proving A; x=1 leaves 1 AND z=z, proving B. With x=0,y=1,z=0, F=1 but yz=0, refuting C. With x=1,y=0,z=0, F=0 while x XOR y XOR z=1, refuting D. The expression implements a selector, not a three-way parity operation.

## Q22

**Correct answer:** A

The device continues asserting the interrupt level while its status remains1, permitting redelivery(A). Acknowledging the controller does not inherently acknowledge or clear the device's own condition, so B is false. Neither transfer rollback(C) nor a change in electrical trigger semantics(D) follows. The handler must address the source condition as required by the device interface.

## Q23

**Correct answer:** 3

The first assignment changes A.next to D. The second changes C.next to A. Starting from q=C, the reachable chain is C→A→D→NULL, containing three nodes. B still exists but is not reachable from q; changing a pointer does not delete a node or automatically reconnect every old predecessor.

## Q24

**Correct answer:** A, C

Every aS production adds one a; every aSb adds one a and a matching trailing b. Consequently the language is a^n b^m with n≥m≥0. A has counts2,1 and C has3,2, both allowed. B has fewer a's than b's, and D violates the block order, so neither is generated. Different productions may contribute unmatched a's, but never unmatched b's.

## Q25

**Correct answer:** 10

A runs0–2, leaving5. B runs2–4: at 3 its remaining 1 ties C's burst1, so B continues. C runs4–5, then A runs5–10. Thus A completes at 10. The explicit tie rule resolves scheduling at time3 without altering total work.

## Q26

**Correct answer:** C

j doubles monotonically across the entire program and is not reset per i, so the while body runs only floor(log2 n)+1 times in total. The outer loop still performs n iterations and tests, giving Theta(n). A omits those iterations, B incorrectly multiplies the total doubling count by n, and D assumes a linear inner loop each time.

## Q27

**Correct answer:** A, C

After buffered data is drained, orderly end-of-stream is reported by a zero return on a positive-length receive(A). TCP supports independent directional shutdown, so continued sending can remain valid(C). Zero here is a count, not a delivered data byte(B), and TCP supplies a byte stream without a separate application shutdown record(D).

## Q28

**Correct answer:** 5

The first three pushes store(5,5),(2,2),(2,2). Popping one duplicate minimum leaves the other minimum2. Pushing and popping4 does not remove that2. The final pop removes the remaining 2, leaving(5,5), so the minimum is 5. Per-entry minimum metadata restores the previous minimum correctly even with duplicates.

## Q29

**Correct answer:** 3

Each block holds floor(512/90)=5 unspanned records. Twelve records require three blocks, with capacity 15. Therefore three additional records fit without another block. The unused62 bytes per full block cannot combine across boundaries to hold a record because spanning is prohibited.

## Q30

**Correct answer:** B

Greedy chooses6,1,1, using three coins. The optimal choice4,4 uses two; a one-coin solution is unavailable. Greedy exceeds optimum by one(B). A assumes greedy is always optimal, C overstates the difference, and D reports greedy's count rather than the excess. Arbitrary denomination systems need not support greedy optimality.

## Q31

**Correct answer:** 4

By the mean value theorem on[0,1], f(1)−1≤3, hence f(1)≤4. Applied on[1,2], 7−f(1)≤3, hence f(1)≥4. Together f(1)=4. The endpoint increase already attains the maximum permitted slope over the full interval; a lower intermediate value would force a later slope above3.

## Q32

**Correct answer:** A, C

The returned function must retain the captured variable for later use(A), and an environment with a sufficiently long lifetime can do so(C). A pointer into reclaimed storage does not preserve a valid variable(B). Lexical capture refers to outer's binding, not an unrelated caller's variable(D). The lifetime of an escaping environment can exceed the dynamic lifetime of its original call.

## Q33

**Correct answer:** 3

The successive depths are 1 after a,2 after b,1 after +,2 after c,3 after d,2 after −,and1 after *. The maximum is 3. An operator reduces the depth by one because it consumes two values and produces one, not because it simply pops both without replacement.

## Q34

**Correct answer:** A

A younger result waits in the reorder buffer until all preceding instructions can commit, allowing precise architectural state at an older exception(A). Early issue and additional execution units(B,C) affect execution timing but do not enforce visibility ordering. Branch-direction prediction(D) does not establish exception ordering.

## Q35

**Correct answer:** 42

From50, request45 is closer than80, costing5 movement. The newly arrived44 is then closer to 45 than80 is, costing1. Finally44→80 costs 36. Total 5+1+36=42. A fixed batch order chosen only at time0 would miss the scheduler's reconsideration after the new arrival.

## Q36

**Correct answer:** 0.3333 (accepted range 0.33325–0.33335)

The joint probability of blue then red is(1/2)(1/3)=1/6. Red then red has probability(1/2)(2/3)=1/3. Thus P(second red)=1/2 and the requested posterior is(1/6)/(1/2)=1/3. Replacement plus reinforcement makes the two draws dependent.

## Q37

**Correct answer:** 512

A and B each occupy256-byte buddies; C occupies the remaining 512-byte block. Freeing A,B coalesces their adjacent aligned buddies into one512-byte block. It cannot merge with C because C remains allocated. Thus a512-byte request fits, while a larger request rounds up to 1024 and cannot fit.

## Q38

**Correct answer:** 1

The four minterms0,2,4,6 form the cube C=0. Using the don't-care permits the single-literal implementation NOT C. A constant cannot match both specified1 and0 entries, so one literal is minimal. That implementation assigns1 to minterm 4. Don't-care means freedom during synthesis, not that the implemented output remains undefined.

## Q39

**Correct answer:** 513

The effective address is 100+12−8=104. Little-endian order places byte01 in bits 7..0 and02 in bits 15..8. The low16 bits are 0x0201=2×256+1=513. Computing the address and interpreting the byte order are separate steps.

## Q40

**Correct answer:** A, B

The usable DNS cache can supply the address without a new query(A). An entity-tag conditional request can receive a not-modified response and reuse the body(B). DNS freshness concerns name-to-address information, not resource freshness(C). HTTP receipt does not reset DNS TTL(D). The two caches have independent validity rules.

## Q41

**Correct answer:** 684

The IP payload has600+8=608 bytes. Each fragment can carry at most 380 payload bytes, but a nonfinal payload must be a multiple of 8, so the first carries376 and the second232. Payload remains608 in total; two IP headers add40 and two link overheads add36. Total 608+40+36=684. The UDP header is included once, not repeated per IP fragment.

## Q42

**Correct answer:** A, C

Tabular combination requires identical dash positions and exactly one differing fixed bit. A combines {0,1} and {2,3}; its cube covers precisely four ON minterms. C combines {0,2} with {8,10}; allowing the don't-care 10 gives the valid cube {0,2,8,10}. B's inputs have different dash positions and different sizes. Its proposed cube also includes OFF minterm 11. D likewise combines unequal dash patterns, and its proposed cube includes 11. Thus A and C are valid; B and D are invalid. Don't-care minterms may assist grouping, but OFF minterms never may.

## Q43

**Correct answer:** 2

Insert 6 into the left leaf, producing[2,5,6]. Inserting 7 produces[2,5,6,7], split into[2,5] and[6,7]; separator 6 is added alongside the existing separator 8. The root now has three leaf children and two keys, within its capacity. Leaf promotion copies rather than removes the separator key from the new leaf.

## Q44

**Correct answer:** 1

Optimal prefix weights are 4,7,9,13,13. For the fifth vertex, taking it gives9+3=12, below omitting it at 13. For the fourth, taking it gives7+6=13, above omitting at 9. The second vertex's7 beats the first vertex's4. Thus the unique optimal set is positions 2,4, with weight13; the count is 1. Ties between consecutive prefix optimum values need not imply multiple optimal sets for the same prefix.

## Q45

**Correct answer:** A, C

Commit can be durable while data remains only buffered, so redo may be needed(A). Forcing a position in a sequential log can make all earlier records durable(C). WAL requires the update's log record to be durable before its data page is flushed, contradicting B. Missing flushed data for a committed transaction calls for redo, not automatic undo(D).

## Q46

**Correct answer:** 6

Since30=2×3×5 with distinct prime factors, a maximal divisor chain introduces exactly one previously absent prime at each step. The orders of these three introductions yield3!=6 chains. Skipping a multiplication would leave an intermediate divisor that could be inserted, making that chain nonmaximal.

## Q47

**Correct answer:** 4

From r, depths are 0,1,1,2,2,2, summing8. From c, depths of c,a,d,r,b,e are 0,1,2,2,3,4, summing12. The increase is 4. Rerooting changes every distance to the chosen root, not merely the old root's depth.

## Q48

**Correct answer:** C

On()), the stack becomes empty after the prefix(), so the modified machine accepts before processing the remaining unmatched ')'. The original rejects that remaining pop. A,B are valid balanced strings accepted by both; D never empties after consuming a symbol and is rejected by both. Acceptance must account for the entire input.

## Q49

**Correct answer:** 64

The two high-bit pairs must match. Choose their common value in4 ways, and choose each input's low-bit pair independently in4 ways. Total 4×4×4=64 ordered pairs require the second comparison. Equality of the high halves does not imply equality of the full inputs.

## Q50

**Correct answer:** A, C

Short-circuit semantics already skip f() in A,C, so replacing those expressions removes no executed side effect and preserves the constant result. In B,D, f() is evaluated first even though the final value is predetermined; replacing the whole expression would suppress its effects. Boolean algebra alone is insufficient for effectful expressions.

## Q51

**Correct answer:** 300

The exact sum300 leaves low byte44 and carry1. The retained byte has its sign bit clear, so signed R=44. Therefore R+256C=44+256=300. Carry is computed from the unsigned addition; it is not the same as the signed-overflow flag.

## Q52

**Correct answer:** A, B

After reading u, its DFA state can reach an original accepting state iff some suffix v completes uv into L. Marking precisely these reachable-to-accept states therefore recognizes Pref(L), proving B and regularity(A). For L={ab}, prefix a is not in L, disproving C. If L is empty, no suffix completes even epsilon, disproving D.

## Q53

**Correct answer:** 496

Every unordered pair of distinct array positions is compared exactly once: at the first recursive split that separates its members. Thus total comparisons are C(32,2)=496. Equivalently, T(n)=2T(n/2)+n²/4 with T(1)=0 yields n(n−1)/2. This merge phase is quadratic pair enumeration, not the usual linear merge of sorted arrays.

## Q54

**Correct answer:** 5

The executed addresses are 0,4,8,5,1. CALL0 saves1; CALL4 saves5; RETURN8 restores5; RETURN5 restores1; then HALT executes. Five cycles elapse and stack depth never exceeds two. A call stores its return address, not its own address.

## Q55

**Correct answer:** 3

The successor of 8 is 10. It replaces the root's key, and its original leaf under12 is removed. The left subtree is unchanged, so the path to 5 is 10→4→6→5, three edges. Replacing the root key does not transplant the entire right subtree into the left path.

## Q56

**Correct answer:** A, C

Concrete execution increments x,y together from zero, so x=y=n and z=0(A). The stated per-variable abstraction joins0 with 1 at the loop header, making each nonconstant(C). It does not store the relational invariant x=y, so B is false; D is contradicted by the concrete invariant. An imprecise analysis does not make an impossible program result possible.

## Q57

**Correct answer:** 4

Before r=d+a, a,d are live. Across a=f, replace old a by f, giving d,f. Across d=a+e, replace d by a,e, giving a,e,f. Across a=b+c, replace a by b,c, giving b,c,e,f. Four variables are live at entry. The two definitions of a are different values whose liveness must be traced backward through kills.

## Q58

**Correct answer:** 2

After replacement,9 first swaps with smaller child2 at index 3. It then swaps with smaller child4 at index 6 and reaches a leaf. The final heap is[2,3,4,8,7,9,5]. Two swaps occur. The smaller child must be chosen to preserve heap order with both children.

## Q59

**Correct answer:** B

T3 is younger than holder T2, so wait-die aborts T3. T1 is older than T2 and is permitted to wait. This is B; A,D apply one rule indiscriminately, while C reverses the age comparison. The scenario specifies wait-die, not wound-wait.

## Q60

**Correct answer:** 2.5

The first link delivers packet1 at 1s and packet2 at 2s. The second link sends packet1 during1–1.5s, then waits for packet2, which it sends during2–2.5s. Completion is 2.5s. Different link rates prevent treating both links as sharing a single packet transmission time.

## Q61

**Correct answer:** −2.5

Apply the row permutation to the right-hand side: Pb=(2,7)ᵀ. Solve Ly=Pb: y1=2,y2=7−4=3. Then2x2=3 gives x2=1.5, and x1+3x2=2 gives x1=−2.5. Using b without its row swap would solve a different system.

## Q62

**Correct answer:** C, D

All legal pumped blocks have the form a^k with 1≤k≤p. After pumping, the counts are m=p+(i−1)k and n=p. For C, m=p+k>p, so positive m cannot divide p. For D, m=p+(p+1)k>p, with the same consequence. B leaves the original string, whose two counts are equal, inside L. A is not guaranteed to leave L: choose k=p−1, giving m=1 and n=p, and 1 divides p. This legal decomposition exists for every p≥2. A decomposition that fails for some exponent is not enough; here the successful choices force failure for every legal decomposition.

## Q63

**Correct answer:** 62

A hit costs 2+50=52ns. A miss costs 2+3×50=152ns. The weighted mean is 0.9×52+0.1×152=62ns. Resident pages avoid disk faults, but a TLB miss still pays page-table memory accesses.

## Q64

**Correct answer:** 0.5

Combine the integrands before integrating: (x+x³)/(1+x²)=x on the interval. Thus I+J=integral0..1 x dx=1/2. Computing the two logarithmic antiderivatives separately is unnecessary; their logarithmic terms cancel.

## Q65

**Correct answer:** 1

BFS gives distance1 to a,b and distance2 to c,d. Vertex d's only predecessor at distance1 is a, so the sole shortest route is s→a→d. Although c has two shortest paths, extending either through c→d takes three edges and does not contribute to shortest paths to d. Count only predecessors one level earlier.



