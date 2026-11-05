# GATE CS 2027 — Mock 013: Worked Solutions

## Q1

**Correct answer:** A

**Concept:** Experimental sequencing.

A hypothesis must be formulated before designing its test; the test is then conducted and its result recorded. A follows Q,R,S,P. B designs before formulating, C reverses the process, and D records a result before testing.

**Common misconception:** Ignoring the dependency expressed by “that hypothesis” and “that test”.

## Q2

**Correct answer:** 0.5

**Concept:** Conditioning on an event independent of a remaining trial.

The first two differing tosses contribute exactly one head. Exactly two total heads then requires the third toss to be heads. The third fair toss remains independent of the condition, giving 1/2.

**Common misconception:** Treating the condition on earlier tosses as changing the last toss's probability.

## Q3

**Correct answer:** B

**Concept:** Contextual vocabulary.

A conclusion open to revision is tentative, B. Irrevocable means it cannot be reversed; unrelated concerns relevance; unanimous concerns agreement among people. None of A,C,D expresses the stated revisability.

**Common misconception:** Selecting a word associated with authority rather than with uncertainty.

## Q4

**Correct answer:** 2

**Concept:** Exponential equations with a common base.

The right side is 3³×3^(2x−4)=3^(2x−1). Equality of powers of three gives x+1=2x−1, hence x=2, which is positive.

**Common misconception:** Forgetting to multiply the entire exponent by two when replacing 9 by 3².

## Q5

**Correct answer:** B

**Concept:** Testing a proposed predictor with comparison data.

B supplies observations where the suspected condition is present and absent, allowing comparison. A and D claim certainty without the missing evidence; C deliberately keeps the comparison condition unobserved.

**Common misconception:** Counting only instances consistent with a hypothesis instead of testing alternatives.

## Q6

**Correct answer:** 9

**Concept:** Counting local patterns in a grid.

Every adjacent 2×2 chessboard block has two squares of each colour. Its top-left square can occupy three rows and three columns, giving 3×3=9 subgrids.

**Common misconception:** Counting only disjoint 2×2 blocks when overlapping subgrids are allowed.

## Q7

**Correct answer:** 41

**Concept:** Recurrence evaluation and summation.

The first four terms are 2,5,11,23. Their sum is 41. Alternatively a_n+1 doubles at each step, so a_n=3×2^(n−1)−1, and the four-term sum is 3(2⁴−1)−4=41.

**Common misconception:** Reporting the fourth term instead of the requested sum.

## Q8

**Correct answer:** 0.5

**Concept:** Displacement volume.

The immersed sphere displaces (4/3)π(1.5)³=4.5π cubic metres. The tank's horizontal area is 9π, so the rise is 4.5π/(9π)=0.5 m. The assumptions exclude spilling and partial immersion.

**Common misconception:** Using the sphere's surface area rather than its volume.

## Q9

**Correct answer:** B

**Concept:** A necessary prerequisite.

B forbids restarting before closure, exactly expressing the prerequisite. A reverses the time order, C removes the prerequisite, and D converts a necessary condition into a sufficient automatic trigger.

**Common misconception:** Equating “only after” with “whenever”.

## Q10

**Correct answer:** 8

**Concept:** Conservation of mixture content.

Let x kg be the 70% alloy. Copper mass is 0.7x+0.4(20−x)=0.52×20. Thus 0.3x=2.4 and x=8 kg.

**Common misconception:** Averaging concentrations without weighting their masses.

## Q11

**Correct answer:** 4

**Concept:** Element order in a multiplicative group.

Powers of 3 modulo 10 are 3,9,7,1. The first return to the identity is the fourth power, so the order is four.

**Common misconception:** Using the additive order instead of the multiplicative group operation.

## Q12

**Correct answer:** 8

**Concept:** Handshaking with loops and parallel edges.

There are four edges counted with multiplicity. Every edge contributes two to the total degree, including the loop, so the sum is eight. Directly, the degrees are 2,3,3.

**Common misconception:** Counting a self-loop only once in its vertex's degree.

## Q13

**Correct answer:** B

**Concept:** Direct-mapped conflict tracing.

B gives misses on 0 and 1, a hit on the second 0, and a miss on 4, which replaces 0 at index zero. A alternates conflicting blocks and has no hits; C visits four new blocks and has no hits; D has three hits after its first miss.

**Common misconception:** Treating blocks with the same index as the same cached block.

## Q14

**Correct answer:** A, C

**Concept:** Scope and cost of interrupt masking.

A is the specified masking effect. An interrupt arriving during a longer masked interval may wait longer, proving C. Masking on one CPU does not stop other CPUs, refuting B, and it does not change ordinary memory operations into atomic multi-CPU operations, refuting D.

**Common misconception:** Treating local interrupt exclusion as a complete multiprocessor lock.

## Q15

**Correct answer:** 7.75

**Concept:** Signed fixed-point maximum.

The greatest signed six-bit encoded integer is 2⁵−1=31. Two fractional bits divide it by four, giving 31/4=7.75.

**Common misconception:** Allocating all six bits to magnitude despite the sign bit.

## Q16

**Correct answer:** A

**Concept:** Preserving expression availability across unrelated assignments.

Neither a nor b changes between t and u, so t is the correct replacement, A. c=d+e need not equal a+b, refuting B and C. D leaves a use of an undefined replacement value.

**Common misconception:** Assuming every intervening assignment invalidates every available expression.

## Q17

**Correct answer:** 4

**Concept:** Projection duplicate elimination and Cartesian product.

π_A(R)={1,2} and π_B(R)={2,3}, each of size two. Their product contains four ordered pairs. Projected duplicates are eliminated under set semantics.

**Common misconception:** Retaining all three original occurrences in each projected relation.

## Q18

**Correct answer:** B

**Concept:** One-past pointers versus dereferencing.

p=a+3 may be formed, but not dereferenced. Moving back one gives a+2, whose value is seven, so B is valid. A and D access one-past storage; C goes farther out of the permitted array-pointer range and dereferences it.

**Common misconception:** Treating permission to form a one-past pointer as permission to access an element there.

## Q19

**Correct answer:** A, B, D

**Concept:** Unbounded stack height with a small alphabet.

Repeated X symbols can encode an unbounded unary count (A), which later pops can match (B). Stack height has no fixed bound, proving D. With exactly one X per prefix symbol and no alternative encoding, only the length is stored in the stack; finite control cannot distinguish every arbitrary binary prefix, so C is false.

**Common misconception:** Confusing finite stack alphabet with bounded stack capacity.

## Q20

**Correct answer:** 21

**Concept:** Equal-weight spanning trees.

Every spanning tree on four vertices has three edges. With every edge weighted seven, all spanning trees weigh 3×7=21 and are minimum.

**Common misconception:** Counting graph edges rather than the three edges selected by a tree.

## Q21

**Correct answer:** 3

**Concept:** Matching bottlenecks and a construction.

The three vertices a,b,c together have only two neighbours, so at most two of them can be matched. Vertex d adds at most one match, giving an upper bound three. The matching a–1,b–2,d–3 attains it.

**Common misconception:** Inferring a perfect matching just because the two bipartition sides have equal size.

## Q22

**Correct answer:** A

**Concept:** Range restriction and infinite-domain complements.

The result is every integer outside finite R, which is infinite. A correctly identifies the missing range restriction. B reverses the meaning of negation; C contradicts the infinite complement; D incorrectly treats negation itself as a safety guarantee.

**Common misconception:** Silently switching from the stated infinite domain to a finite active domain.

## Q23

**Correct answer:** B

**Concept:** Shared storage versus synchronization.

Shared memory provides access to common data but does not automatically order protocol steps or exclude conflicting operations, proving B. A and C are false restrictions; D incorrectly supplies automatic serialization.

**Common misconception:** Assuming communication visibility is sufficient for a race-free protocol.

## Q24

**Correct answer:** 12

**Concept:** Bounded positive compositions.

Without upper bounds there are choose(7,2)=21 positive triples. If x≥5, setting x′=x−4 leaves three positive entries summing to four, giving choose(3,2)=3 choices; similarly for y or z. Two entries cannot both be at least five. Therefore 21−3×3=12.

**Common misconception:** Applying a nonnegative-composition formula without adjusting positivity.

## Q25

**Correct answer:** 400

**Concept:** Summing odd increments.

T(n)=Σ_(i=1)^n(2i−1)=2n(n+1)/2−n=n². Therefore T(20)=400.

**Common misconception:** Treating the recurrence's incremental cost as the total.

## Q26

**Correct answer:** B

**Concept:** Lexical recognition versus semantic binding.

A lexer can identify a spelling as an identifier without resolving its declaration, which may require scope information. B is correct. A asserts an unnecessary implementation rule; C leaps from lexical validity to type correctness; D misclassifies whitespace.

**Common misconception:** Treating tokenization, name resolution and type checking as the same analysis.

## Q27

**Correct answer:** 1200

**Concept:** Offset units and payload length.

The starting payload offset is 100×8=800 bytes. The fragment carries 420−20=400 payload bytes. Its exclusive end offset is 800+400=1200.

**Common misconception:** Including the header in the original-payload byte range or using the offset field directly as bytes.

## Q28

**Correct answer:** A, B, C

**Concept:** Closure under finite changes.

Finite F is regular. Union and difference of regular languages are regular, establishing A and B. F−L is finite, establishing C directly. D fails by taking L empty and a nonregular superset, such as {aⁿbⁿ}.

**Common misconception:** Assuming an arbitrary superset inherits a subset's language class.

## Q29

**Correct answer:** 20

**Concept:** Prefix-range membership before longest matching.

The /20 beginning at third octet 32 covers third octets 32 through 47, so 41 matches it. The /24 route covers only third octet 40 and does not match. The /16 and default match but are less specific. Selected length: 20.

**Common misconception:** Choosing the most specific table entry without first checking that it matches.

## Q30

**Correct answer:** 2

**Concept:** DISTINCT combined with NULL exclusion in COUNT.

The distinct non-NULL values are 2 and 5. NULL is not counted by COUNT(expression), so the result is two.

**Common misconception:** Counting NULL as another distinct numeric value.

## Q31

**Correct answer:** B

**Concept:** Reachability limits on negative-cycle effects.

A source-to-destination walk cannot exploit a cycle unreachable from the source. Thus that cycle alone does not make source-reachable distances undefined, proving B. A overgeneralizes; C unnecessarily blocks reachability analysis; D imposes no justified restriction on other edges.

**Common misconception:** Declaring all graph distances undefined whenever any negative cycle exists anywhere.

## Q32

**Correct answer:** 0.5

**Concept:** Floating-point spacing within one exponent bin.

Values in [8,16) have exponent three. Four fractional significand bits give spacing 2^(3−4)=1/2.

**Common misconception:** Using precision as the exponent or counting the leading bit twice.

## Q33

**Correct answer:** A, C

**Concept:** Negating implication under universal quantification.

P→Q is ¬P∨Q, giving C by direct substitution. Negating the universal and then the disjunction gives ∃x(P∧¬Q), A. B requires all objects to be counterexamples rather than one; D describes the opposite truth pattern.

**Common misconception:** Negating the consequent without also handling the implication and quantifier.

## Q34

**Correct answer:** A

**Concept:** Counting-semaphore permits.

Three initial permits allow at most three simultaneous unreleased successful waits, so A holds. No simultaneous arrival requirement exists (B); one wait consumes one permit (C false); later processes can block once all permits are held (D false).

**Common misconception:** Interpreting the initial count as a required batch size rather than available capacity.

## Q35

**Correct answer:** 4

**Concept:** Binary-search decision depth.

The balanced successful-search tree for fifteen entries has levels with 1,2,4,8 entries. A deepest entry needs four comparisons. The midpoint choice yields these exact sizes.

**Common misconception:** Using floor(log₂15)=3 without accounting for the first comparison level.

## Q36

**Correct answer:** 7

**Concept:** A worst-case resource deadlock bound.

With six resources, each process can hold two and wait for its third, producing deadlock. With seven, if all three are unfinished, at most six can be held while each remains short of its maximum; a free instance then permits some waiting process to reach three and finish. After it releases resources, the remaining processes can similarly progress. Equivalently the sufficient bound is Σ(max_i−1)+1=3×2+1=7, and the six-instance construction proves minimality.

**Common misconception:** Requiring all maximum demands simultaneously, or counting scheduling starvation as resource deadlock.

## Q37

**Correct answer:** A, B

**Concept:** Inessential variables through equal cofactors.

The given equality makes both z-cofactors identical, proving A. Set z=0 to obtain a function of x,y that equals F everywhere, proving B. F=x is a nonconstant counterexample to C and can be written without z, refuting D.

**Common misconception:** Interpreting independence of one variable as independence of every variable.

## Q38

**Correct answer:** 13

**Concept:** Nilpotent finite polynomial expansions.

Write A=I+N, where N has ones immediately above the diagonal. N³=0 and (N²)13=1. Therefore A⁵=I+5N+10N². Also (I+N)⁻²=I−2N+3N², obtained by squaring I−N+N². The requested entry is 10+3=13.

**Common misconception:** Expanding as a scalar formula without checking which powers vanish or which entry each contributes to.

## Q39

**Correct answer:** 142

**Concept:** Nonoverlapping stall accounting.

Base issue time is 100 cycles. Branch stalls add 3×4=12. Only six of the eight cache misses add time outside those intervals, contributing 6×5=30. Total 142.

**Common misconception:** Double-counting penalties explicitly stated to overlap completely.

## Q40

**Correct answer:** 1020

**Concept:** Scaled index and signed displacement.

11111000₂ represents −8 in eight-bit two's complement. The target is 1000+4×7−8=1020. Only the index is scaled by four.

**Common misconception:** Scaling the displacement too or reading it as unsigned 248.

## Q41

**Correct answer:** A, B, D

**Concept:** Subtraction flags and signed range.

The full unsigned sum is A+(2ⁿ−1−B)+1=2ⁿ+A−B. A carry exists exactly when A≥B, meaning no unsigned borrow, proving A. Retained bits give the modulo result, proving B. Opposite signed operands can produce a sign inconsistent with A when their difference exceeds range, establishing D. Borrow and signed overflow are different: for four bits, 0−1 borrows but has valid signed result −1, refuting C.

**Common misconception:** Using one flag interpretation for both signed and unsigned arithmetic.

## Q42

**Correct answer:** 5.3333

**Concept:** Nonpreemptive scheduling with later arrivals.

J1 starts at zero and runs to five. Both others are then ready, so J3 runs 5–6 and J2 runs 6–8. Turnaround times are 5,7,4 respectively, averaging 16/3=5.333333…. Accepted range: 5.33325–5.33335.

**Common misconception:** Preempting J1 when a shorter job arrives despite the nonpreemptive policy.

## Q43

**Correct answer:** 4

**Concept:** Recursion-tree argument sizes.

The root 10 splits equally into 5,5. Each 5 splits unequally into 2,3. Each 2 splits equally into 1,1; each 3 splits unequally into 1,2. Thus the two size-5 calls and two size-3 calls are exactly the unequal splits, totalling four.

**Common misconception:** Counting only distinct odd lengths instead of separate calls with those lengths.

## Q44

**Correct answer:** 1.6667

**Concept:** Key-weighted successful hashing cost.

Comparison costs within the chains are [1], [1,2], [1,2,3]. All keys are equally likely, so the average is (1+1+2+1+2+3)/6=10/6=1.666666…. Accepted range: 1.66665–1.66675.

**Common misconception:** Giving every bucket equal probability when keys, not buckets, are sampled uniformly.

## Q45

**Correct answer:** B

**Concept:** Reverse translation of multiplexed connections.

The public translated ports distinguish the clients' connections, and the translator needs the corresponding mapping back to internal endpoints. B provides that information. A ignores the distinguishing field; link broadcast addressing (C) and payload length (D) cannot identify the internal connection.

**Common misconception:** Assuming the server endpoint alone uniquely identifies a connection through a shared public address.

## Q46

**Correct answer:** B

**Concept:** Bounded pumping window across three symbol blocks.

A substring of length at most p cannot touch both an a and a c while also crossing the entire intervening block of p b symbols. Thus at least one symbol count is unaffected by pumping; some count changes because |vy|>0. Pumping can also disrupt order when a repeated mixed segment crosses a boundary. In either case the language condition fails, supporting B. A violates the nonempty pumped-part condition; C contradicts the chosen length 3p; D is unrelated.

**Common misconception:** Claiming the pumped parts necessarily lie inside one block, when they may straddle a boundary.

## Q47

**Correct answer:** A, B

**Concept:** SQL CHECK and three-valued logic.

For B=3, the predicate is TRUE and passes. For NULL it is UNKNOWN, which is not FALSE and therefore passes under the specified semantics. Zero and −2 make the predicate FALSE and are rejected. The fresh primary keys remove key collisions from consideration.

**Common misconception:** Assuming CHECK(B>0) also imposes NOT NULL.

## Q48

**Correct answer:** 8

**Concept:** Pointer-to-row indexing.

p+1 points to the second three-element row; *(*(p+1)+2) is its third element, 6. (*p)[1] is the second element of the first row, 2. Their sum is eight.

**Common misconception:** Advancing a pointer-to-array by one integer instead of by one full row.

## Q49

**Correct answer:** A, B, D

**Concept:** Differentiability without a continuous derivative.

|f(x)|≤x² gives continuity. The difference quotient x sin(1/x) tends to zero, proving f′(0)=0. For x≠0, f′(x)=2x sin(1/x)−cos(1/x), which oscillates and has no limit at zero, refuting C. Yet |f′(x)|≤2|x|+1, so it is bounded near zero, proving D along with A,B.

**Common misconception:** Assuming existence of a derivative implies continuity of that derivative.

## Q50

**Correct answer:** 22

**Concept:** Congestion-window timing within rounds.

The first four rounds transmit windows 4,5,6,7 MSS, increasing only after each round. Total 4+5+6+7=22 MSS.

**Common misconception:** Applying the first increase before transmitting the first window.

## Q51

**Correct answer:** 0.36

**Concept:** Hypergeometric variance.

Among choose(5,3)=10 equally likely samples, X=0 occurs once, X=1 occurs choose(2,1)choose(3,2)=6 times, and X=2 occurs three times. Hence E[X]=(6+6)/10=1.2 and E[X²]=(6+12)/10=1.8. Variance is 1.8−1.2²=0.36.

**Common misconception:** Using independent Bernoulli variance for sampling without replacement.

## Q52

**Correct answer:** A, C

**Concept:** Bounded simulation.

The allowed simulation horizon is computable and finite for every input. Test acceptance initially and after each permitted step, stopping no later than |x| steps; this decides membership, proving A and C. It requires no unbounded halting decision, so B is false. Behaviour on another input cannot invalidate acceptance within this input's finite bound, refuting D.

**Common misconception:** Treating every question about a Turing machine's behaviour as an undecidable halting question.

## Q53

**Correct answer:** 15

**Concept:** Involutions with a prescribed fixed-point count.

f²=id implies f is a permutation and every cycle has length one or two. Choose the sole fixed point in five ways; pair the remaining four elements into two unordered pairs in three ways. Each pair forms a transposition. Total 5×3=15.

**Common misconception:** Counting pair orders or orientations as distinct functions.

## Q54

**Correct answer:** B

**Concept:** Prime attributes and 3NF versus BCNF.

A is never derived and must be in every key. AB determines C; AC determines B via C→B. Both are minimal keys, and all attributes are prime. Thus every nontrivial dependency has either a superkey determinant or prime right-hand attribute, satisfying 3NF. But C is not a superkey while C→B holds, violating BCNF. B is correct. A misses AC and the BCNF violation; C overstates individual closures; D misclassifies B as nonprime.

**Common misconception:** Treating the 3NF exception for a prime right-hand attribute as valid in BCNF too.

## Q55

**Correct answer:** 298

**Concept:** SCAN travel to a physical endpoint.

The head travels from 80 to 199, passing 90 and 150, for 119 cylinders. It then returns to 20, travelling 179. Total 119+179=298; measurement stops there. Reversing at 150 would instead be LOOK, not the stated SCAN rule.

**Common misconception:** Reversing at the highest request despite an explicit endpoint requirement.

## Q56

**Correct answer:** A, B

**Concept:** Precedence and associativity encoded in grammar levels.

Multiplication is built inside T before addition combines T terms, establishing A. Left-recursive addition groups chains on the left, establishing B. Immediate left recursion causes naive recursive descent to recurse without consuming input, refuting C. The separated precedence levels give the unique parse id+(id*id), refuting D.

**Common misconception:** Assuming left recursion implies ambiguity rather than an implementation issue for naive top-down parsing.

## Q57

**Correct answer:** B

**Concept:** TCP byte-stream reception.

A positive short read can return available data without indicating EOF. The application must use its own framing and accumulate as needed, B. A and C misinterpret a permitted short return; D invents message boundaries absent from TCP's stream interface.

**Common misconception:** Equating one send with one receive.

## Q58

**Correct answer:** 2

**Concept:** Covering zeros for product-of-sums minimization.

Zero minterms 0 and 2 form a pair with a=0,c=0, giving clause (a+c). Zero minterms 1 and 5 form a pair with b=0,c=1, giving clause (b+c′). Their product has exactly the required zeros. One clause's zero set would have to be a single Boolean subcube, but {0,1,2,5} is not one: four points would require one variable fixed across all, and none is fixed. Thus at least two clauses are necessary and two suffice.

**Common misconception:** Grouping ON minterms when deriving a product-of-sums form from zero groups.

## Q59

**Correct answer:** B

**Concept:** Aggregate resizing cost.

The n appends themselves cost n. Resizing copies 1,2,4,…,n/2 elements, summing to n−1. Total cost is 2n−1, B. A counts resize events rather than copied elements; C incorrectly charges logarithmic copying for each append; D exceeds the exact count.

**Common misconception:** Multiplying the largest single append cost by the number of appends.

## Q60

**Correct answer:** 28

**Concept:** Synthesized width attributes.

The inner array has width 2×4=8. The outer array has width 3×8=24. Adding the final int without padding yields 28 bytes.

**Common misconception:** Adding nested array dimensions instead of multiplying their extents.

## Q61

**Correct answer:** 3

**Concept:** Suffix-tracking DFA minimality.

Track three cases: no relevant suffix, suffix 0, and suffix 01 (accepting). These suffice with ordinary suffix updates. They are distinguishable: the accepting state differs from either other state on ε; states reached by ε and 0 differ on suffix 1. Thus three is both an upper and lower bound.

**Common misconception:** Adding a dead state although every prefix can still be extended to end in 01.

## Q62

**Correct answer:** 11

**Concept:** Unspanned blocking factor.

A block has 1000−40=960 usable bytes, fitting floor(960/120)=8 records. Thus ceil(81/8)=11 blocks are needed.

**Common misconception:** Dividing total record bytes by raw block size without accounting for headers and unspanned records.

## Q63

**Correct answer:** B

**Concept:** Per-activation storage.

Each active recursive call needs its own x, and stack activation records provide these separate slots with return-time reclamation, B. A overwrites older calls' values, C falsely forbids locals, and D ignores assignments to a variable.

**Common misconception:** Allocating one slot per function rather than one per active call.

## Q64

**Correct answer:** A, D

**Concept:** Tabular combination conditions.

A has identical dash positions and differs only in the final bit, combining to 01-1-. D differs only in its first bit with matching dashes, combining to ---10. B has different dash positions. C differs in two nondash bits, first and last. Therefore only A and D qualify in one step.

**Common misconception:** Comparing only numbers of dashes instead of their positions and all remaining bits.

## Q65

**Correct answer:** A, C

**Concept:** MST exchange arguments independent of weight signs.

Kruskal's cut-based choices remain correct with negative weights, proving A and C. A spanning tree cannot contain a cycle even if every edge on it is negative, refuting B. Adding c to each edge adds exactly (n−1)c to every spanning tree, preserving all comparisons and ties, so D is false.

**Common misconception:** Transferring shortest-path restrictions on negative weights to minimum spanning trees.

