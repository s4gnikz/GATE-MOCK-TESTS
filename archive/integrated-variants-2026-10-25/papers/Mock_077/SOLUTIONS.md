# Worked Solutions — Mock Test 077

## Q1

**Correct answer:** A

**Concept:** Experimental sequencing.

A hypothesis must be formulated before designing its test; the test is then conducted and its result recorded. A follows Q,R,S,P. B designs before formulating, C reverses the process, and D records a result before testing.

**Common misconception:** Ignoring the dependency expressed by “that hypothesis” and “that test”.

## Q2

**Correct answer:** 0.6667 (accepted range 0.66665–0.66675)

P(A and boy)=1/2, whereas P(B and boy)=(1/2)(1/2)=1/4. The posterior is (1/2)/(3/4)=2/3, rounding to 0.6667. Sampling a household first does not make the five children equally likely; counting three of four boys would use a different experiment.

## Q3

**Correct answer:** B

Discrete means distinct or separate; discreet means tactful or careful about confidential matters. B assigns both meanings correctly. A reverses them; C misuses the second word; D misuses the first.

## Q4

**Correct answer:** B
**Concept:** Composition of spatial transformations.

Track the direction vector (1,0). Reflection in y=x sends it to (0,1); a clockwise quarter-turn sends that to (1,0); reflection in the y-axis gives (−1,0). Thus B is correct. A omits the last reflection; C stops after the first operation; D is not the final vector.

**Common misconception:** Reflections and rotations must be applied in the stated order.

## Q5

**Correct answer:** B

**Concept:** General Aptitude — Inductive reasoning and analogies

1. The rejected red, circular, filled card excludes rules that accept both properties together: A and D.
2. The rejected blue, circular, hollow card excludes a colour-independent exclusive-or rule C.
3. B accepts precisely the two listed red cards with one of the two properties and rejects all three other rows. This selects among the stated candidates; it does not claim uniqueness among all imaginable rules.

- **A:** It would accept the first row.
- **B:** It matches all five rows.
- **C:** It would accept the final blue card.
- **D:** It would accept the first, fourth and fifth rows.

**Common misconception:** Observed examples select a rule only relative to a specified candidate set.

## Q6

**Correct answer:** 72

The original exterior area is54. Removing the six face-centre cubes removes six outward faces, leaving48. Each of those removed cubes exposes four faces on retained adjacent cubes, adding24. Its inward neighbour is the removed central cube, so there is no additional retained face in that direction. The central cube's six neighbours are all removed. Total48+24=72. Count retained-to-empty interfaces, not the surfaces of removed cubes.

## Q7

**Correct answer:** B
**Concept:** Precedence-constrained parallel tasks.

Run A and B from time zero on the two workers. They finish at 4 and 3; C then runs from 4 to 6. The chain A→C requires at least 4+2=6 hours, so this schedule is optimal. B is correct; A violates that lower bound, while C,D fail to use available concurrency optimally.

**Common misconception:** Worker capacity cannot remove a precedence constraint.

## Q8

**Correct answer:** B

**Concept:** General Aptitude — Geometry and mensuration

1. If the width is x, the planted dimensions are 16-2x and 10-2x. The planted area is 160-88=72.
2. Expanding (16-2x)(10-2x)=72 gives x^2-13x+22=0, with roots 2 and 11.
3. Geometry requires 0<x<5, so only x=2 is admissible.

- **A:** Width 1 leaves 14*8=112 square metres planted, so the path area is 48.
- **B:** Width 2 leaves 12*6=72, giving path area 88.
- **C:** Width 3 leaves 10*4=40, giving path area 120.
- **D:** Width 4 leaves 8*2=16, giving path area 144.

**Common misconception:** A border removes its width from both ends of each dimension, and algebraic roots must meet geometric bounds.

## Q9

**Correct answer:** C

**Concept:** Reference and causal sequencing.

R introduces the result and competing explanations. P's “these explanations” refers back to them and introduces the repeat. Q describes that repeat's outcome; S states the ensuing conclusion. Thus R–P–Q–S is required. A uses an unresolved reference, B reports the repeat before introducing it, and D places the conclusion before its grounds.

**Common misconception:** Ordering sentences by vocabulary alone instead of their logical dependencies.

## Q10

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

## Q11

**Correct answer:** C

For t=7, the read-timestamp test7<5 is false, but7<9 is true, so ignore. For t=4, the first test4<5 already aborts. C is the pair. A,D incorrectly perform the obsolete write; B reverses the priority of the two checks. Each attempt starts from the specified same metadata.

## Q12

**Correct answer:** 24

**Concept:** Alignment and final padding.

c occupies offset 0. i starts at 4 and occupies 4–7. d starts at 8 and occupies 8–15. e occupies 16. The end offset is 17, rounded up to 24 for eight-byte total alignment.

**Common misconception:** Summing object sizes without accounting for internal and trailing padding.

## Q13

**Correct answer:** 31

Work counts are16,8,4,2,1 before i becomes0. Their sum is31. The geometric total is about twice n, not n times the number of halving steps.

## Q14

**Correct answer:** C
**Concept:** Syntax-directed postfix translation.

The grammar groups the input as (8−3)−2. The first subtraction emits 8 3 −; the outer one appends 2 −. C is correct. A encodes 8−(3−2), B is prefix, and D is infix.

**Common misconception:** Postfix output follows the parse tree's grouping rather than the textual placement of operator symbols.

## Q15

**Correct answer:** 1

Concept: weighted interval scheduling. Earliest finish first chooses [0,2), then [2,4), total weight eight. Choosing only [0,4) yields nine, which is optimal among the listed choices. Shortfall=1. The unweighted greedy rule does not generally maximize weights.

## Q16

**Correct answer:** 0

Every one-bit flip toggles total parity, including a flip of the parity bit itself. None of the five patterns passes the check. Detection is being asked, not localization or correction.

## Q17

**Correct answer:** B, C

A missing transition previously rejected the word, so its complement must accept it, proving C. Complete the original machine with a rejecting sink and then complement every state, including that sink: B. A leaves such words rejected; D wrongly leaves the new sink rejecting. Complementation requires total transition behaviour.

## Q18

**Correct answer:** D

**Concept:** Engineering Mathematics — Monoids and groups

1. The inverses are f-inverse(x)=3x mod 5 and g-inverse(x)=x-1 mod 5.
2. Apply the maps right to left: x becomes x-1, then 3x-3, then 3x-2, then 6x-4, which is x+1 modulo 5.
3. Thus h is a translation by 1; its k-fold application is x+k, equal to x for every residue exactly when k is a multiple of 5.

- **A:** h is not identity; it maps 0 to 1.
- **B:** Two applications map 0 to 2.
- **C:** The order of f alone is 4, but h is a different permutation.
- **D:** Five is the least positive translation count returning every residue.

**Common misconception:** Composition order matters when the permutations do not commute.

## Q19

**Correct answer:** A, C

Every aS production adds one a; every aSb adds one a and a matching trailing b. Consequently the language is a^n b^m with n≥m≥0. A has counts2,1 and C has3,2, both allowed. B has fewer a's than b's, and D violates the block order, so neither is generated. Different productions may contribute unmatched a's, but never unmatched b's.

## Q20

**Correct answer:** A, B

An open descriptor refers to the opened file object rather than repeatedly resolving its pathname. Thus R retains F(A), while the replaced directory entry sends a later open to G(B). C confuses the directory entry with the existing open-file reference. D is false because the open reference can keep F alive after its last name is removed. Atomic replacement affects pathname visibility, not the identity of already-open files.

## Q21

**Correct answer:** 3
**Concept:** Lexical binding under nested scopes.

The first print references the middle-scope x. The second references that same x and the innermost y. The third occurs outside the innermost block and references the outer y. Thus three distinct variables are read; the outer x is shadowed at every print.

**Common misconception:** Repeated occurrences of a name need not refer to the same declaration.

## Q22

**Correct answer:** A, B

A matching without cd cannot perfectly match either odd triangle. Thus any perfect matching must use cd, after which edges ab and ef complete one; A,B are true. Each triangle is an odd cycle, so C is false. Covering all edges inside each triangle requires at least two of its vertices, hence at least4 overall; choosing b,c,d,e achieves4, refuting D. Matching and vertex-cover sizes need not agree in a nonbipartite graph.

## Q23

**Correct answer:** 13

There are24 child-pointer positions at12 non-null vertices. Exactly11 point to other vertices because a tree has11 edges. The remaining24−11=13 are null, each producing one null call. Counting only missing leaves would miss null child pointers at one-child vertices.

## Q24

**Correct answer:** A

**Concept:** Truth-table synthesis.

The possible values are 0,1,2,3. Exactly 2 and 3 are prime, and both have a=1, so A realizes the required function. B includes 1 and excludes 2; C includes 1 and excludes 3; D excludes prime 2.

**Common misconception:** Treating 1 as prime.

## Q25

**Correct answer:** 2 (exact)

**Concept:** Operating Systems — System calls

1. dup creates a second descriptor referring to the same open-file description, so the offset is shared.
2. The two reads move the offset to 2 and then 5.
3. The absolute seek resets it to 1. The final one-byte read moves it to 2.

**Common misconception:** Duplicated descriptors share an offset; reopening the path would create an independent offset.

## Q26

**Correct answer:** 3

Simultaneous transitions are 00→01→10→00. Thus the first return takes three edges. The next-state equations use the old bits; updating one bit first and then using its new value would model a different circuit.

## Q27

**Correct answer:** B
**Concept:** Array parameters and local pointer reassignment.

The parameter a is a pointer to x[0]; p saves that pointer. Advancing local a makes it point to x[1], without changing the caller's array or p. With n=3, a[n−2]=a[1] refers to x[2], which becomes p[0]+a[0]=4+7=11. x[0] stays 4. Only B matches; A treats pointer advancement as shifting array contents, and C,D miss the actual target.

**Common misconception:** Reassigning a pointer parameter and modifying its pointed-to object are different operations.

## Q28

**Correct answer:** B

The source address establishes A's location on incoming port 1. B's destination location is unknown, so the frame floods out the other two ports. B is correct. A learns the destination from the wrong evidence; C assigns the wrong source port; D assumes the destination's physical location can be learned merely from its address in this frame.

## Q29

**Correct answer:** C

The owner key distinguishes loans; the partial key distinguishes installments of a given loan. Their pair identifies each installment, so C. A collides across owners; B collides among installments of one owner. Amount need not be unique at either level, so D fails. A weak entity's partial key is interpreted within its owner.

## Q30

**Correct answer:** 12
**Concept:** Minimizing a quadratic under linear constraints.

Let x=y=t, so z=6−2t. Then x²+y²+z²=2t²+(6−2t)²=6(t−2)²+12. The minimum is 12, achieved at (2,2,2).

**Common misconception:** Satisfying the linear equations leaves a family of solutions; the quadratic objective selects one.

## Q31

**Correct answer:** 9

The coefficients of(1−x)^(−2) are n+1. Multiplying by1+x makes the x4 coefficient5+4=9. Equivalently, convolve the two contributions at powers4 and3. Formal power-series arithmetic needs no numerical convergence assumption.

## Q32

**Correct answer:** 7

Concept: duplicate-suppressed flooding. Source S sends on its two incident links. Routers A and B each have degree three and each forwards on two links after its first arrival. C has degree two and forwards on one. Total=2+2+2+1=7 transmissions. Arrival order can choose which link is excluded but does not change these counts; later duplicates never trigger further sends.

## Q33

**Correct answer:** 2

**Concept:** Cyclic implication.

If any variable is true, the implications force the other two true. If none is true, all implications also hold. Therefore only FFF and TTT satisfy the formula.

**Common misconception:** Treating the three implications as independent clauses without propagating their consequences.

## Q34

**Correct answer:** 200

Old time=100×2+10×60=800 ns. New time=100×3+5×60=600 ns. Reduction200 ns. Saving five misses saves300 ns, but slower hits/lookups cost100 ns across the entire stream.

## Q35

**Correct answer:** 64

Concept: cache geometry. The cache contains 16384/64=256 lines. Four lines per set give 256/4=64 sets. Associativity counts lines per set, not bytes per set.

## Q36

**Correct answer:** B

The first phase stores a prefix; the second must match its reverse, consuming one stack symbol per input symbol. A successful branch therefore divides an even-length palindrome equally. B is true. NPDA acceptance requires some successful branch, not every guess, disproving A. One stack is sufficient, disproving C. End-of-input remains mandatory, disproving D.

## Q37

**Correct answer:** 15

Concept: aliasing in linked structures. Reversal makes 4→3→2→1→null. B still points to node 9, whose next pointer is still node 3; node 3's next has changed to 2. Thus B now visits 9,3,2,1, sum 15. The nodes are shared objects, not independent copies of their labels.

## Q38

**Correct answer:** B

The parent retains its three threads. Only the calling thread is replicated into the child, which therefore starts with one thread. B is correct; A,C,D have incorrect thread counts. A copied address space can contain synchronization objects representing the old multithreaded state, but this does not recreate the other threads.

## Q39

**Correct answer:** 3

To pop3 first,1,2,3 must all be pushed before any pop, requiring capacity at least3. Pop3, push and pop4, pop2 and1, then push and pop5. This never exceeds three entries, proving capacity3 sufficient. The lower bound follows from the first demanded output, not the total number of inputs.

## Q40

**Correct answer:** 3

p is always evaluated. If p is false, q is skipped and r is evaluated: subset{p,r}. If p and q are true, r is skipped: {p,q}. If p is true and q false, all three are evaluated. These are three distinct subsets. Truth assignments sharing a control path need not create new subsets.

## Q41

**Correct answer:** 2

**Concept:** Ties among optimal compatible subsets.

Before time 4, either A and B together or C alone gives value eight, and no compatible selection exceeds eight. D is compatible with both and adds one, giving optimal value nine. The two maximizing subsets are {A,B,D} and {C,D}.

**Common misconception:** Returning one optimal solution without counting another with the same value.

## Q42

**Correct answer:** A, C

With a full buffer and no consumer progress, a further blocking write can wait indefinitely, proving A. An open read endpoint is merely a reference, not an action consuming data, so B is false. Closing all readers changes the endpoint condition, rather than leaving an ordinary full pipe with a potential reader, proving C. A finite buffer cannot absorb unlimited data without draining, so D is false. Capacity can postpone blocking but cannot replace consumer progress.

## Q43

**Correct answer:** A, B, C
**Concept:** Row dependence, null space, and consistency.

Row 1 minus twice row 2 plus row 3 is zero, so rank is at most 2. The upper-left 2×2 minor has determinant 1, making rank exactly 2 (A). Direct multiplication sends (1,−2,1)ᵀ to zero; nullity is one, so this vector spans the null space (B). The same dependence requires b1−2b2+b3=0. It is sufficient because the first two independent equations can be solved and the third is then their combination (C). Adding any multiple of the nonzero null vector to a solution gives another solution, disproving D.

**Common misconception:** Consistency and uniqueness are separate conditions; a nontrivial null space rules out uniqueness.

## Q44

**Correct answer:** A, C

Concept: universal conditions over an empty set. Every candidate passes the “for every B in S” condition vacuously. Division's candidates are {1,2}, giving A and disproving B. The second query's candidates are U={1,2,3}, giving C. D mistakes an empty requirement set for a failed requirement. The candidate universe still matters when the condition is vacuous.

## Q45

**Correct answer:** B

**Concept:** Databases — Tuple calculus

The biconditional requires the employee's completed-project set to equal, rather than merely contain, the department's required-project set. Department A requires {p,q}. Employee u has an extra r and fails; v has exactly {p,q} and passes. Department B requires {q}, exactly w's set, so w passes. Department C requires the empty set, but z has completed r, so z fails. Thus E={v,w}. The universal statement for C does not become automatically true: Required(C,t) is always false, so Done(z,t) must also always be false.

- **A:** False: u has an extra completed project r and violates the reverse implication.
- **B:** True: v and w alone have exactly the required sets.
- **C:** False: z has a nonempty completion set for a department with no required projects.
- **D:** False: both u and z violate set equality.

**Common misconception:** Relational division tests containment; a universal biconditional tests exact set equality, including the empty-set case.

## Q46

**Correct answer:** A, C

Different source addresses make the supplied context keys different, proving A and disproving B. Once the context is identified, offset locates a payload piece within it, so C is true. Fragments may be interleaved and reordered; arrival order does not replace the supplied key, making D false. Identification values are not globally unique across senders.

## Q47

**Correct answer:** A, C
**Concept:** Stack permutations.

A is produced by pushing 1,2,3, popping all three, then pushing 4,5 and popping both. C is produced by push 1,2/pop 2; push 3,4/pop 4,3; push 5/pop 5,1. In B, after popping 3 the top is 2, blocking 1. In D, after popping 4 the top is 3, blocking 2. Thus A,C are possible and B,D are not.

**Common misconception:** Unread input cannot remove an already stacked obstruction to the next requested output.

## Q48

**Correct answer:** B
**Concept:** Right quotient of a language.

Appending k zeros changes counts from (n0,n1) to (n0+k,n1). Equality requires k=n1−n0, which exists as a nonnegative integer exactly when n0≤n1. B is correct. A excludes strings fixable by appending zeros; C reverses the inequality; D wrongly includes w=0, which cannot be balanced by more zeros.

**Common misconception:** The suffix alphabet restricts which count imbalances can be repaired.

## Q49

**Correct answer:** 1

The semaphore serializes both complete read-modify-write operations. Each increments x exactly once, and the third critical section changes no data. Every completed execution ends with x=2, so there is exactly one distinct final value. The requested count of possible results is1, not the result2 itself.

## Q50

**Correct answer:** 15.875

**Concept:** Saturating fixed-point conversion.

The largest signed eight-bit integer code is 127, and three fractional bits give real maximum 127/8=15.875. Exact 17 exceeds that range, so saturation stores 15.875.

**Common misconception:** Wrapping modulo 256 instead of applying the specified saturation rule.

## Q51

**Correct answer:** 300

Base computation costs1000×2=2000 cycles. DMA adds100 stall cycles, total2100. Programmed I/O adds400 cycles, total2400. DMA saves300 cycles. The baseline CPI must be combined with the respective transfer overhead, not multiplied by it.

## Q52

**Correct answer:** C, D

All legal pumped blocks have the form a^k with 1≤k≤p. After pumping, the counts are m=p+(i−1)k and n=p. For C, m=p+k>p, so positive m cannot divide p. For D, m=p+(p+1)k>p, with the same consequence. B leaves the original string, whose two counts are equal, inside L. A is not guaranteed to leave L: choose k=p−1, giving m=1 and n=p, and 1 divides p. This legal decomposition exists for every p≥2. A decomposition that fails for some exponent is not enough; here the successful choices force failure for every legal decomposition.

## Q53

**Correct answer:** A

**Concept:** Databases — SQL

For k=1, COUNT(*)=3, COUNT(v)=2 and SUM(v)=20, so both predicates are true. For k=2, counts are 2 and 0, but SUM(v) is NULL; NULL>=10 evaluates UNKNOWN and HAVING does not retain the group. For k=3, both counts are 1 and SUM(v)=5, so the group fails. SQL aggregates retain duplicate non-null values unless DISTINCT is requested. The single output row is (1,3,2).

- **A:** True: only group 1 satisfies both HAVING conditions.
- **B:** False: group 2 has an unknown second predicate and is discarded.
- **C:** False: COUNT does not deduplicate rows or values without DISTINCT.
- **D:** False: group 1 has counts 3 and 2 and sum 20, and therefore passes.

**Common misconception:** SUM over an all-null group is NULL rather than zero, and HAVING keeps only TRUE.

## Q54

**Correct answer:** B, D

Concept: dead values versus observable effects. The first stored value is overwritten before print, but evaluating 1/x may raise an observable exception (B). Thus A is false when x=0. C leaves print dependent on an unrelated old value and also removes the possible exception. If x is known nonzero, the division has no observable effect under the stated exact-arithmetic model, and the second assignment fixes the printed value to two; D is correct. Dead-store elimination does not automatically justify deleting a potentially trapping right-hand side.

## Q55

**Correct answer:** A, C

Concept: aggregation with longest-prefix exceptions. The two /25s exactly partition the /24 and share H. Keeping the more-specific /26 retains J for its destinations, so A. No address outside the /24 gains a matching nondefault route, so C. Longest-prefix matching selects by prefix length, not insertion time, disproving B. Removing the /26 would send its destinations to H instead of J, disproving D.

## Q56

**Correct answer:** 142

**Concept:** Nonoverlapping stall accounting.

Base issue time is 100 cycles. Branch stalls add 3×4=12. Only six of the eight cache misses add time outside those intervals, contributing 6×5=30. Total 142.

**Common misconception:** Double-counting penalties explicitly stated to overlap completely.

## Q57

**Correct answer:** A, B, C

Choose x_n=1/(π/2+2πn) for value1 and y_n=1/(3π/2+2πn) for value−1; both approach0 positively. A and B are true and their different limits disprove D. Since |x sin(1/x)|≤|x|, the squeeze theorem proves C. Bounded oscillation can disappear after multiplication by a vanishing factor.

## Q58

**Correct answer:** 24

There are three merge levels for eight elements. Every level writes all eight elements once across its buffers, so total writes are3·8=24. Equivalently W(n)=2W(n/2)+n with W(1)=0. This is cumulative work, not simultaneous buffer space.

## Q59

**Correct answer:** 1

Near8 the spacing is2. The exact sum9 is a tie between8 and10, rounded to8 because its significand low bit is even. The first expression is therefore0. The value1−8=−7 is exactly representable with three significant bits, so the second expression becomes8−7=1 exactly. The absolute difference is1. Reassociation changes intermediate rounding.

## Q60

**Correct answer:** B
**Concept:** Longest-prefix matching before metric comparison.

The destination lies in all three explicit blocks, including /25's range 172.16.5.128–255. The /25 is the longest match and therefore wins before metrics are compared. B is correct. A applies the tie-breaker across unequal prefix lengths; C prefers the broadest rather than narrowest match; D ignores the deterministic selection rule.

**Common misconception:** A better metric on a shorter prefix does not override longest-prefix matching under the stated policy.

## Q61

**Correct answer:** 2

Concept: reconstructing a Boolean function from differences. The x difference condition gives F=xy XOR g(y,z), where g=F(0,y,z). The z difference then forces g=z XOR h(y). The specified value at 000 imposes h(0)=0, while h(1) remains free. The two functions are xy XOR z and xy XOR y XOR z. Both directly satisfy all constraints. A Boolean difference determines dependence on one variable but leaves a function of the others to be constrained.

## Q62

**Correct answer:** 0.80 (two decimals)
**Concept:** Tail probabilities of an independent minimum.

For integer k≥1, P(X≥k)=(2/3)^k. Independence gives P(min(X,Y)≥k)=(4/9)^k. Summing the nonnegative integer variable's tails yields E[min]=Σ_(k≥1)(4/9)^k=(4/9)/(5/9)=4/5=0.80.

**Common misconception:** The expected minimum is not the minimum of the two expectations.

## Q63

**Correct answer:** A, B

The assignment x=0 proves the condition true. The other branch and input call are unreachable, and y=4 gives z=16. Thus A,B. C would execute dead code unnecessarily and alter behavior; D ignores feasibility and confuses syntactic assignment presence with possible execution. Reachability can increase the precision of constant propagation.

## Q64

**Correct answer:** 102

Concept: variable instruction lengths and branch base. Branch starts at 100+2+4=106; next-instruction address=108. Displacement is −3·2=−6 bytes. Target=108−6=102. Neither branch-start addressing nor treating the displacement as bytes matches the stated architecture.

## Q65

**Correct answer:** A, C

To have f(g(0))=0, g(0) may be a or b. To have f(g(1))=1, g(1) must be c. Hence two right inverses, proving A, and both are injective, proving C. A left inverse would have to send f(a)=f(b)=0 to both a and b, impossible, refuting B. f itself is not injective, refuting D.

