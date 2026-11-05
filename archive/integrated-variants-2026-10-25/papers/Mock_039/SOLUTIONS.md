# Worked Solutions — Mock Test 039

## Q1

**Correct answer:** 9

The domain starts with3,5,7, all prime. The next odd integer9=3×3 is composite, so it is the smallest counterexample. The integer1 is excluded by the conjecture's domain and cannot serve as a counterexample to this statement.

## Q2

**Correct answer:** 1

**Concept:** Fixed cells under a half-turn.

A cell at row r,column c maps to row 4−r,column 6−c, numbering from one. Equality requires r=2,c=3, the unique central cell.

**Common misconception:** Counting the full central row or column rather than the cell satisfying both coordinate conditions.

## Q3

**Correct answer:** A, C
**Concept:** Weighted means with positive weights.

The combined mean is a convex combination of 40,60,80 with all weights positive, so it lies strictly between 40 and 80 (A). Equal sizes give 60 (C). Sizes 2,1,1 give mean 55, refuting B and D.

**Common misconception:** An unweighted mean of group means is valid only with suitable group weights.

## Q4

**Correct answer:** B

**Concept:** Area ratios with a shared height.

Write the rectangle's dimensions as width w and height h. The triangle has base w/2 along the top edge and perpendicular height h, hence area wh/4. The quadrilateral occupies3wh/4. The ratio is1:3, option B. A, C and D would allocate respectively one-third, one-fifth and two-fifths of the rectangle to the triangle, inconsistent with its base and height.

**Misconception:** Taking the ratio of the top-edge lengths as the ratio of areas.

## Q5

**Correct answer:** B

**Concept:** Negating a universal statement.

“Not every” means that at least one submitted report lacks a diagram. Thus B is equivalent. A and C both say none has a diagram, which is stronger; D concerns a report outside the submitted set and need not hold.

**Common misconception:** Negating “all” produces “none” rather than “at least one not”.

## Q6

**Correct answer:** B

**Concept:** General Aptitude — Ratios and percentages

1. Initially milk=72 and water=48 litres. The first withdrawal removes one-quarter of each, leaving 54 milk and 36 water; the refill makes water 66.
2. The next withdrawal removes one-sixth of each: the remaining amounts are milk=45 and water=55.
3. Adding 20 litres of milk gives 65:55=13:11.

- **A:** This reverses the final milk and water quantities.
- **B:** The final quantities are 65 and 55 litres.
- **C:** The two different replacement fluids do not preserve the starting ratio.
- **D:** This would require 70 litres milk rather than 65.

**Common misconception:** Each withdrawal uses the composition after the preceding mixing step.

## Q7

**Correct answer:** D

If A is absent, the three statements are true,false,true. If B is absent, they are false,false,false. If C is absent, they are true,true,false. The counts of true statements are2,0,2, never1. Thus none of A,B,C can be the absent person under all conditions and D is correct. The task requires checking consistency, not assuming the conditions have a solution.

## Q8

**Correct answer:** C
**Concept:** Composition of plane transformations.

R maps (x,y) to (−y,x), and F swaps coordinates. R then F gives (2,−1); F then R gives (−2,1). C is correct. A reverses the requested order; B gives intermediate-style transformations; D assumes the two transformations commute.

**Common misconception:** A rotation and a reflection generally depend on composition order.

## Q9

**Correct answer:** B

**Concept:** Self-selection and causal direction.

People already inclined to exercise might choose locations near parks. This is the alternative causal direction described by B. Different measurement units (A) do not invalidate association; C reverses the reported association without justification; D denies the very selection mechanism identified.

**Common misconception:** Assuming location was assigned independently of residents' preferences.

## Q10

**Correct answer:** 32

There are5!=120 circular arrangements. For each specified pair forced adjacent, contract it to a block with2 internal orders:2·4!=48. For two designated adjacent pairs there are2²·3!=24 arrangements; for all three,2³·2!=16. Inclusion–exclusion gives120−3·48+3·24−16=32. Reflections remain distinct, so no additional division by2 is allowed.

## Q11

**Correct answer:** A

**Concept:** Aligned prefix aggregation.

The adjacent third octets 4 and 5 differ only in the last bit and form an aligned pair. Their common prefix yields 10.0.4.0/23, A. B and D include additional /24 blocks. C has host bits set and is not the aligned network-address notation of the requested block.

**Common misconception:** Aggregating by adjacency without checking prefix alignment.

## Q12

**Correct answer:** 16384

Each chip stores2048 bytes. Eight chips total16384 bytes. Equivalently each parallel pair stores2048 two-byte words, or4096 bytes; four pairs give16384. Widening the data path increases capacity per selected row, not the number of local rows.

## Q13

**Correct answer:** B
**Concept:** Parity composition.

The first gate computes a XOR b and the second computes (a XOR b) XOR c. This is 1 for one or three input ones, exactly odd parity. B holds. A excludes three ones incorrectly; C is a majority function; D includes 000 even though XOR there is 0.

**Common misconception:** Three-input XOR is not “exactly one input is 1.”

## Q14

**Correct answer:** B

Concept: constant propagation. All feasible incoming paths establish x=4, so 3x−2=12−2=10. B is correct. A omits the subtraction; C is not the expression's value; D denies the justified substitution. A value known on only one incoming path would not suffice.

## Q15

**Correct answer:** B

Concept: mean value theorem bounds. The increase f(3)−f(0) lies between 2·3 and 5·3, so 7≤f(3)≤16. B's value ten is achieved by f(x)=1+3x. A is below seven, C and D exceed sixteen. Bounding derivatives constrains endpoint differences, not just local slopes.

## Q16

**Correct answer:** 0.75

**Concept:** Total probability followed by Bayes.

P(A)=0.6×0.5+0.2×0.5=0.4. The intersection P(A∩B)=0.3, giving P(B|A)=0.3/0.4=0.75.

**Common misconception:** Reversing a conditional probability without incorporating the marginal probabilities.

## Q17

**Correct answer:** B

**Concept:** IPv4 subnet boundaries.

A /27 leaves five host bits and covers addresses 96 through 127. The last address is broadcast, so the highest host is 126. A is broadcast, C lies outside the subnet, and D is valid but not highest.

**Common misconception:** Assigning the all-one host field to a host.

## Q18

**Correct answer:** A

**Concept:** Context-free closure properties.

A new start symbol choosing either grammar proves closure under union, A. General CFL intersection, complement and set difference are not closed, so B,C,D lack the claimed guarantee. Closure under complement combined with union would also imply intersection by De Morgan, contradicting known nonclosure.

**Common misconception:** Assuming CFLs have every Boolean closure property of regular languages.

## Q19

**Correct answer:** A

Concept: preorder subtree ranges. A first lists root 40, then its valid left subtree 20,10,30, then its valid right subtree 60,50,70. B enters the right subtree at 50 and later returns to 10<40. C similarly puts 20<40 after entering the right subtree. D visits 30 in 20's right subtree then incorrectly places 10 there. Bounds from all ancestors matter.

## Q20

**Correct answer:** C
**Concept:** Structural invariants of recursive productions.

Each step adds complementary symbols to opposite ends. The base is empty. Induction therefore gives strings w followed by complement(reverse(w)), and any such string can be reduced by repeatedly stripping its complementary end pair. C is exact. A is too broad: abba has equal counts but equal end symbols and cannot be generated. B is wrong because nonempty generated strings have unequal end symbols. D omits ba, which is generated.

**Common misconception:** Equal symbol counts are necessary here but do not characterize the ordering constraint.

## Q21

**Correct answer:** A, C

The set is the divisor lattice of 6, with meet gcd and join lcm; all results remain in the set. Complements are 1↔6 and 2↔3, so A,C hold. B is false because 1 and 6 are a lower and upper bound of 2,3. D is false because neither 2 divides 3 nor 3 divides 2.

## Q22

**Correct answer:** A

**Concept:** Ties-to-even binary rounding.

The value 1.101₂ lies halfway between 1.10₂ and 1.11₂. The retained least significant bit in 1.10 is zero, so ties-to-even selects A. B chooses the odd last bit; C and D are not the adjacent nearest values.

**Common misconception:** Always rounding an exact halfway case upward.

## Q23

**Correct answer:** D

Q can progress and release S; P can then proceed. No request from Q leads back to P, so there is no cycle. D is correct. A equates waiting with deadlock, B invents a missing circular edge, and C invents a request not stated. A blocked process need not belong to a deadlock.

## Q24

**Correct answer:** C

After fewer than n−1 inspections all returning1, at least two uninspected positions remain possible locations of0, each consistent with the rotation promise. Thus n−1 inspections can be necessary, and a linear scan suffices. C is correct; A,B are too small and D exceeds the tight bound. Duplicates can remove the information needed for logarithmic rotated-array search.

## Q25

**Correct answer:** 10

The burst2 job starts at0. After it ends at2, one switch delays the burst3 job to3. That job ends at6, and the next switch delays the burst5 job to7. Waiting times are0,3,7, totaling10. Context-switch time is waiting time for jobs still ready.

## Q26

**Correct answer:** C

When a is processed before b, both c and d are enqueued before b can enqueue e. C puts e between c and d and is impossible. A,D are possible with a's neighbors ordered c,d or d,c. B results when b is processed first, discovering e before a discovers c,d. Equal BFS distance does not make every within-level ordering attainable.

## Q27

**Correct answer:** 6

Concept: cascading referential actions. Delete the parent, its two children, and their three grandchildren. Total=1+2+3=6. A cascade follows both declared levels rather than stopping after direct references.

## Q28

**Correct answer:** 5

Concept: Gaussian elimination and LU. Eliminate the lower entry using multiplier 6/2=3, giving L21=3. The remaining lower-right pivot is 5−3·1=2, so U22=2. Sum=5. The multiplier belongs to L, while the updated pivot belongs to U.

## Q29

**Correct answer:** 200

Old time=100×2+10×60=800 ns. New time=100×3+5×60=600 ns. Reduction200 ns. Saving five misses saves300 ns, but slower hits/lookups cost100 ns across the entire stream.

## Q30

**Correct answer:** A
**Concept:** Reconstructing a binary tree from traversals.

Preorder selects A as root; inorder splits its left labels D,B,E and right labels C,F. The left subtree has root B with children D,E; the right has root C with right child F. Postorder is D,E,B,F,C,A. Only A matches; B visits B before completing its left subtree, and C,D misorder or mix the two subtrees.

**Common misconception:** Preorder identifies each subtree's root, while inorder determines which labels belong to each side.

## Q31

**Correct answer:** 16

There are eight inclusive ports per address and two addresses, giving16 distinct endpoint pairs. Distinguish the inclusive port count from4007−4000=7.

## Q32

**Correct answer:** A

Concept: dead stores. No operation reads the first stored value before the second assignment overwrites it; removing that store preserves behavior (A). B invents an invalidity rule; C contradicts print's use of x; D would remove the value that print requires. The side-effect assumption is essential.

## Q33

**Correct answer:** C

Both tuples share B=2 but differ in A, directly violating B→A, so C. A→B holds in this instance because A values are distinct. B,D are trivial dependencies from the combined attribute set. An instance satisfying a dependency does not establish it as a constraint on all future instances.

## Q34

**Correct answer:** 42

From50, request45 is closer than80, costing5 movement. The newly arrived44 is then closer to 45 than80 is, costing1. Finally44→80 costs 36. Total 5+1+36=42. A fixed batch order chosen only at time0 would miss the scheduler's reconsideration after the new arrival.

## Q35

**Correct answer:** 1

Split at the sign change x=1. On[0,1], the integrand is x−x², whose integral is1/6. On[1,2], it is x²−x, whose integral is5/6. Their sum is1. Dropping the absolute value would subtract rather than add the first region's area.

## Q36

**Correct answer:** 2 (exact)

**Concept:** Theory of Computation — Turing machines and undecidability

Set 1 is recognizable by simulating M on 01 and accepting if M accepts. Set 4 is recognizable by dovetailing simulations of M on all binary strings and accepting as soon as one enters q.

Set 2 is not recognizable: given a machine N and input w, construct M which, on any input other than 01, simulates N(w) and accepts exactly if that simulation halts; on 01 it rejects. Then M belongs to set 2 exactly when N(w) does not halt. A recognizer for set 2 would recognize the complement of the halting problem, which is impossible.

Set 3 is also not recognizable. Given N,w, let M on input x simulate N(w) for |x| steps. If that bounded simulation has not halted, M halts; if it has halted, M loops forever. If N(w) never halts, M halts on every input. If N(w) halts after t steps, M loops on every sufficiently long input. Thus membership again recognizes nonhalting if set 3 were recognizable. Exactly sets 1 and 4 are recognizable, giving 2. The designated-state construction uses a computably inserted fresh q, so no accidental visit is required.

**Common misconception:** A finite existential witness can be dovetailed; universal termination and absence of accepted counterexamples cannot in general be recognized.

## Q37

**Correct answer:** 3 (exact)

**Concept:** Compiler Design — Common subexpression elimination

The initial *p and *q must each be read: in the allowed case where the pointers differ, their original values are independent and both are returned. After *p=7, the old value b cannot always replace c: if p=q, the store changes *q to 7; otherwise *q retains its old value. Without the prohibited runtime pointer test, a third load is needed for c. No subsequent store occurs, so e=c. The store itself establishes d=7, even if p and q alias. Three loads therefore suffice and are necessary under the allowed transformations.

An equivalent sequence retains the loads for a,b,c and replaces d by 7 and e by c.

**Common misconception:** Syntactically identical loads are not common subexpressions across a potentially aliasing store; a load from the exact stored address can, however, use the stored value.

## Q38

**Correct answer:** 3

Each block stores floor((4096−96)/100)=40 records. Ranks39 and40 are in block1, ranks41–80 in block2 and ranks81–83 in block3. Thus three data blocks must be read. The in-memory directory costs no disk read and does not remove the need to read each block containing selected records.

## Q39

**Correct answer:** 1.36

Mean=(6+t)/5 and mean square=(14+t²)/5. Variance=(4t²−12t+34)/25. Its derivative(8t−12)/25 is positive for t≥3, so the minimum occurs at t=3 and is34/25=1.36. An unconstrained minimum at1.5 would violate the allowed range.

## Q40

**Correct answer:** B

**Concept:** Cumulative acknowledgment across holes.

The third segment leaves byte 1000 missing, so ACK=1000. The first fills 1000–1099 but leaves 1100 missing, so ACK=1100. The fourth still leaves that hole, so ACK stays 1100. The second finally fills the hole and joins all buffered data through 1399, so ACK=1400. B is correct; A follows arrival ends, while C,D advance past missing bytes too early.

**Common misconception:** Treating cumulative ACKs as acknowledgments of the most recently arriving segment alone.

## Q41

**Correct answer:** 200

First-fit takes250 from the500-byte hole, leaving200,250,300; its next200 consumes the first hole, leaving a largest hole300. Best-fit takes250 from300, leaving200,500,50; then consumes200 exactly, leaving largest hole500. Difference500−300=200. Both policies allocate successfully, but their remaining hole distributions differ.

## Q42

**Correct answer:** B

**Concept:** Programming and Data Structures — Directed multigraph representation and edge-distinct walks

1. Every closed walk without a repeated edge decomposes into directed cycles using disjoint edges. Here a four-edge walk can be either two two-edge cycles or one three-edge cycle plus the self-loop at vertex 3. There is no four-vertex simple cycle and only one loop.
2. The first case combines 1→2→1 with 2→3→2. The 1→2 edge has two choices. For either choice, the resulting four-edge circuit has four distinct cyclic starting positions, including two distinct edge orders starting at vertex 2. Contribution: 2×4=8.
3. The only directed three-vertex cycle is 1→3→2→1. Insert the loop 3→3 at vertex 3. This circuit has four distinct cyclic starting positions. Contribution: 4.
4. Repeating the 1↔2 cycle would reuse the sole 2→1 edge; repeating the 2↔3 cycle would also reuse edges. Neither is allowed. The total is 8+4=12.

- **A:** Incorrect: 7 is the ordinary closed-walk count for length two, not this task.
- **B:** Correct: the two permissible cycle decompositions give 12.
- **C:** Incorrect: it does not follow from the permitted disjoint-edge decompositions.
- **D:** Incorrect: reversing a directed circuit is not automatically permitted; doubling 12 counts nonexistent reversals.

**Common misconception:** Powers of an adjacency matrix count unrestricted walks, including edge reuse. An edge-distinct restriction requires additional state or a structural counting argument.

## Q43

**Correct answer:** 9

Concept: B+ splitting and root growth. Leaf splits occur on inserting 4,6,8,10,12, leaving six leaves [1,2],[3,4],[5,6],[7,8],[9,10],[11,12]. At insertion 10 the root first reaches five children and splits into two internal nodes with two and three children, under a new root. Insertion 12 increases the right internal node to four children without overflowing it. Total=6 leaves+2 internal children+1 root=9. A leaf split does not always create another root level.

## Q44

**Correct answer:** A, C
**Concept:** C sequencing and side effects.

A reads the old i to calculate i+1 and then assigns it, which is defined. In C, B reads i for the left index without sequencing that read relative to the increment on the right, so behaviour is undefined. The left operand of && is sequenced before the right, so C is defined. D has two unsequenced modifications of i in function arguments, so is undefined.

**Common misconception:** Function arguments are not evaluated in a guaranteed left-to-right order in C; short-circuit operators have different sequencing rules.

## Q45

**Correct answer:** 8

State1 records that the latest symbol was a without any aa yet. State2 records that aa has occurred and is absorbing. Count strings avoiding aa: if F(n) is their count, F(n)=F(n−1)+F(n−2), with F(0)=1,F(1)=2. Hence F(2)=3,F(3)=5,F(4)=8. Subtract from all16 length-four strings to get8 accepted strings. Counting occurrences instead of strings can double-count words such as aaaa.

## Q46

**Correct answer:** 2

Bytes0,3 specify a three-byte payload65,66,67. The first read ends after66 and is incomplete. The second supplies67, then length0,2 and payload68,69, completing two messages. Reads and protocol boundaries differ; a buffer must retain partial header/payload data across reads.

## Q47

**Correct answer:** 0

FIFO faults on A,B,C and D. The intervening A hit does not change insertion order; D evicts A. The final B is still resident, so FIFO has4 faults. The optimal policy also needs the four distinct pages at least once and can keep B when D arrives, attaining4. The difference is zero. A familiar trace need not exhibit a strict advantage for an optimal policy.

## Q48

**Correct answer:** A, C

The order of x divides both4 and6, hence divides2, proving x²=e and C. It also divides the odd group order, so it cannot be2; its order is1, giving x=e and A. B,D contradict that order. The two exponent equations alone would allow order2; the odd-order hypothesis eliminates it.

## Q49

**Correct answer:** 4 (exact)
**Concept:** Monotone self-dual Boolean functions.

Monotonicity and self-duality force f(000)=0 and f(111)=1. Let the values at singleton inputs 100,010,001 be a,b,c. Self-duality fixes the complementary doubleton values as 1−a,1−b,1−c. If two singleton values were 1, monotonicity into a doubleton complementary to the other singleton would contradict self-duality. Thus at most one of a,b,c is 1. All four choices (none or exactly one) satisfy the remaining monotonicity constraints. They give majority and the three coordinate functions x,y,z.

**Common misconception:** Choosing arbitrary values for complementary input pairs enforces self-duality but not monotonicity.

## Q50

**Correct answer:** 370
**Concept:** Fragment offsets.

Maximum payload is 1500−20=1480, already divisible by eight. The payloads are 1480,1480,1040. The final fragment starts after 2960 payload bytes, so its offset field is 2960/8=370.

**Common misconception:** Fragment offsets measure original payload position, excluding all IPv4 headers.

## Q51

**Correct answer:** A, C

**Concept:** Recoverability and cascading aborts.

r2(X) reads the uncommitted w1(X), proving A. Recoverability would require T1 to commit before T2 commits; instead T1 aborts after c2, so B is false. T2's dependence requires aborting it when T1 aborts, but T2 has already committed, establishing C's problem. Strict schedules prohibit this read of an uncommitted write, so D is false.

**Common misconception:** Treating a completed commit as evidence that a schedule satisfies recovery constraints.

## Q52

**Correct answer:** B

**Concept:** Copy propagation and killed facts.

Before the assignment y=5, x and y have the same value, so the use in z may be replaced. Afterwards x still has the original y while y has 5, so a direct replacement in w is generally wrong. B is correct. A ignores the redefinition; C assumes every initial y equals 5; D forbids the valid first substitution.

**Common misconception:** Treating a copy assignment as a permanent alias relationship.

## Q53

**Correct answer:** D
**Concept:** Lexer states and longest match.

The tokens are string literal "if", keyword if, and identifier if2. The comment is discarded. The string's content is not tokenized as source code, and longest match keeps if2 as one identifier. Thus one keyword and three total tokens. A counts comment/string text as keywords; B counts if2 as a keyword; C retains an extra token from discarded or split text.

**Common misconception:** Keyword recognition depends on lexical context and full token boundaries.

## Q54

**Correct answer:** 5000

The full response sends5200 bytes; the revalidation response sends200. Saving=5000 bytes. The cached body is reused locally and is not retransmitted as part of the specified304 response.

## Q55

**Correct answer:** 1.5
**Concept:** Optimal BST comparison cost.

With b at the root, cost is 0.5×1+(0.2+0.3)×2=1.5. With a at the root, the best right subtree puts b above c, costing 0.2+2×0.5+3×0.3=2.1. With c at the root, the best left subtree puts b above a, costing 0.3+2×0.5+3×0.2=1.9. The remaining shapes are worse within those root choices, so 1.5 is optimal.

**Common misconception:** Minimizing height alone does not account for nonuniform search probabilities.

## Q56

**Correct answer:** A
**Concept:** Circular-array indices and occupancy.

Initially occupancy is (2−6) mod 8=4. The operations change head/tail as follows: dequeue (7,2), enqueue (7,3), enqueue (7,4), dequeue (0,4), enqueue (0,5). Occupancy is 4−1+1+1−1+1=5, agreeing with (5−0) mod 8. A is correct; B has the right indices but inconsistent occupancy, and C,D miscount index advances.

**Common misconception:** Index wraparound does not reset queue occupancy to zero.

## Q57

**Correct answer:** 8

A perfect matching must use newly added edges to both initially isolated right vertices3 and4. The pair a,b also needs an escape from its single neighbour1, and c,d needs an escape from2. With only two new edges, choose one endpoint from{a,b}, one from{c,d}, and assign them bijectively to3,4. There are2·2·2=8 choices, each completing a matching with the remaining original edges. Any other two-edge choice leaves a deficient pair or isolated right vertex.

## Q58

**Correct answer:** A, B, C

With b=c=0 the expression is a AND NOT a, always 0, proving A. During a transition, the direct and inverted paths can temporarily make both OR outputs 1, proving B. By the consensus theorem, (a+b)(NOT a+c) already implies (b+c), so adding that factor preserves the truth table. When b=c=0 the added factor remains 0 and blocks the glitch, proving C and refuting D. A redundant Boolean factor can be physically useful for hazard suppression.

## Q59

**Correct answer:** 3

Without the edge-count constraint, s→a→b→t costs3. Among routes with at most two edges, direct s→t costs10, s→a→t costs9, and s→b→t costs6. The permitted optimum is6, exceeding3 by3. Keeping only one unrestricted distance per vertex does not encode a remaining hop budget.

## Q60

**Correct answer:** 6

**Concept:** Strict inversions in stable insertion sort.

The leading 4 forms inversions with all four later elements. The 3 forms two more with the later 1 and 2. No other inversions exist; equal 1 values are not shifted past one another. Each strict inversion causes one shift, for six shifts.

**Common misconception:** Counting equal-valued pairs as inversions in a stable implementation.

## Q61

**Correct answer:** A, B

**Concept:** Precedence and associativity encoded in grammar levels.

Multiplication is built inside T before addition combines T terms, establishing A. Left-recursive addition groups chains on the left, establishing B. Immediate left recursion causes naive recursive descent to recurse without consuming input, refuting C. The separated precedence levels give the unique parse id+(id*id), refuting D.

**Common misconception:** Assuming left recursion implies ambiguity rather than an implementation issue for naive top-down parsing.

## Q62

**Correct answer:** 48

Choose the unordered pair of positions for A,B at distance 2: (1,3),(2,4),(3,5),(4,6). The remaining positions admit respectively 2,1,1,2 adjacent position pairs for C,D. For each such selection, orient A,B in two ways, orient C,D in two ways, and arrange the two other books in two ways. The total is (2+1+1+2)×2×2×2=48. Therefore the required count is 48.

## Q63

**Correct answer:** 45

Without coalescing20 interrupts cost20·3=60 microseconds. Groups of four give5 interrupts and15 microseconds. Savings are60−15=45. The computation concerns CPU handling time, not device completion latency or the waiting delay introduced by batching.

## Q64

**Correct answer:** C

**Concept:** Digital Logic — Tabular minimization

Every pair of rows misses one column: P1P2 misses m6; P1P3 misses m5; P1P4 misses m4; P2P3 misses m3; P2P4 misses m2; P3P4 misses m1. Therefore at least three product terms are necessary. Every triple covers all columns. Their literal totals are 8 for P1P2P3, 9 for P1P2P4, 9 for P1P3P4 and 10 for P2P3P4. The unique preferred set is P1P2P3.

A is not a cover. B is a cover with nine literals. C is the minimum-literal three-term cover. D is a cover with ten literals.

- **A:** False: pair P1P4 misses minterm m4 and does not cover all required minterms.
- **B:** False: P1P2P4 covers all minterms but has total literal cost 9.
- **C:** True: P1P2P3 covers all minterms with the minimum total literal cost of 8.
- **D:** False: P2P3P4 covers all minterms but has total literal cost 10.

**Common misconception:** A chart with no essential prime implicant can still have a unique optimum once literal costs are considered.

## Q65

**Correct answer:** A, B, D

The aS production adds an unmatched leading a; aSbS adds a matched enclosing pair around the first S and then a valid suffix. Structural induction shows no generated prefix has more b's than a's, proving B and hence A. ba violates that prefix condition, disproving C. Derive aab via S→aS→aaSbS→aab using epsilon subderivations, proving D.

