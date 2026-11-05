# GATE CS 2027 — Mock 005: Worked Solutions

NAT rounding and accepted ranges are specified in the paper's final answer key. All integer and exact finite-decimal answers are exact.

## Q1

**Correct answer:** C  
**Concept:** Modifier attachment and grammatical parallelism.

The person examining the records must be the subject immediately following the introductory phrase. In C that subject is Mira, and the three coordinated verbs are corrected, recalculated, and reorganized. A and B attach the introductory phrase to errors and totals, respectively, and mix incompatible list forms. D has no coherent parallel structure and also makes totals the subject of examining. Only C meets both conditions.

**Common misconception:** A sentence can contain individually grammatical phrases while linking them incorrectly.

## Q2

**Correct answer:** 36  
**Concept:** Net work rates.

The inlets together fill 1/6+1/9=5/18 tank per hour. The observed net rate is 1/4. The leak removes 5/18−1/4=1/36 tank per hour, so a full tank takes 36 hours to empty.

**Common misconception:** Filling times cannot be added; rates must be combined first.

## Q3

**Correct answer:** A, C  
**Concept:** Exhaustive consistency of statements.

If the prize is in A, the three truth values are false,false,true: valid. If it is in B, they are true,false,true: invalid. If it is in C, they are false,true,false: valid. Hence A and C are possible locations, B is impossible, and label A is false in every valid case. Options A,C hold; B,D do not.

**Common misconception:** Exactly one true statement need not determine a unique location.

## Q4

**Correct answer:** B  
**Concept:** Composition of spatial transformations.

Track the direction vector (1,0). Reflection in y=x sends it to (0,1); a clockwise quarter-turn sends that to (1,0); reflection in the y-axis gives (−1,0). Thus B is correct. A omits the last reflection; C stops after the first operation; D is not the final vector.

**Common misconception:** Reflections and rotations must be applied in the stated order.

## Q5

**Correct answer:** D  
**Concept:** Necessary versus sufficient conditions.

Approval implies timely receipt, so timely receipt is necessary. The explicitly mentioned timely rejections show it is insufficient. A reverses the implication; B contradicts those timely rejections. C is not implied: the report is compatible with some approvals or none. D precisely states the implication and its failed converse.

**Common misconception:** “Every approved application was timely” does not mean every timely application was approved.

## Q6

**Correct answer:** 3.125  
**Concept:** Cost-weighted profit.

Take one item of each kind, since their quantities are equal. Total cost is 160. Selling prices are 60×1.25=75 and 100×0.90=90. Profit is 165−160=5; percentage profit is 100×5/160=3.125%.

**Common misconception:** Averaging 25% and −10% ignores the unequal cost bases.

## Q7

**Correct answer:** B  
**Concept:** Recovering subgroup totals.

The original total is 20×30=600. The retained total is 15×34=510. The removed five therefore average (600−510)/5=18. The new total is 510+5×28=650, giving mean 32.5. The required difference is 32.5−18=14.5, option B. A,C,D disagree with these totals.

**Common misconception:** The incoming workers' mean is not the new group's mean.

## Q8

**Correct answer:** 8  
**Concept:** Constrained lattice paths.

There are 2 paths to (1,1) and C(5,2)=10 paths from there to (4,3), for 20 paths through the required point. Forbidden paths additionally pass through (3,2): their count is 2×C(3,1)×C(2,1)=12. Subtracting gives 8. The monotone directions ensure these visits have the indicated order and no path is counted twice.

**Common misconception:** Count forbidden paths subject to the required visit, rather than all paths through the forbidden point.

## Q9

**Correct answer:** B  
**Concept:** Adjacency blocks with relative-order constraints.

Treat PQ as one block. Among R,PQ,S their order is fixed. Insert unrestricted T into one of the four gaps before, between, or after those three objects. Each insertion produces a distinct valid schedule, giving 4. A,C,D miscount the available positions.

**Common misconception:** The PQ block has a fixed internal order and must not be multiplied by 2!.

## Q10

**Correct answer:** 2.333  
**Concept:** A stopping-time expectation on a small sample space.

The first red occurs on draws 1,2,3 with probabilities 1/2, (2/4)(2/3)=1/3, and (2/4)(1/3)=1/6. Expected draws are 1/2+2/3+3/6=5/3. Expected balls remaining are 4−5/3=7/3=2.333… . Round to three decimals.

**Common misconception:** The red probability changes after a blue is removed.

## Q11

**Correct answer:** A, C  
**Concept:** Local structure imposed by a regular expression.

Each 1 is introduced in a block 11; adjacent blocks may merge, but each resulting run has even length. Conversely, every even-length run can be partitioned into such blocks, separated by zeros. Thus A holds and 110011 is accepted (C). The string 101 has two 1s overall but two odd runs, refuting B and D.

**Common misconception:** Even parity over the entire string differs from even parity in every run.

## Q12

**Correct answer:** C  
**Concept:** Stable multi-key sorting.

The first pass gives (a,2),(a,1),(b,1),(b,2). The second pass moves both number-1 records ahead of both number-2 records while preserving letter order within each equal-number group. The result is (a,1),(b,1),(a,2),(b,2). C matches. A instead gives letter priority; B,D violate preserved ordering within a numeric group.

**Common misconception:** With successive stable sorts, the final sort key has highest priority.

## Q13

**Correct answer:** 3  
**Concept:** Lexical binding under nested scopes.

The first print references the middle-scope x. The second references that same x and the innermost y. The third occurs outside the innermost block and references the outer y. Thus three distinct variables are read; the outer x is shadowed at every print.

**Common misconception:** Repeated occurrences of a name need not refer to the same declaration.

## Q14

**Correct answer:** A  
**Concept:** Intersection and equivalence closure.

No pair of distinct elements shares a block in both partitions, so R∩S consists of the six reflexive pairs. In R∪S, the links 1–2–3–4–5–6 connect every element. Transitivity therefore puts all six into one class in T, giving 6²=36 ordered pairs. Only A has both counts. B omits reflexivity; C incorrectly retains nonreflexive intersection pairs; D does not complete transitivity.

**Common misconception:** The union of equivalence relations need not itself be transitive.

## Q15

**Correct answer:** 86  
**Concept:** Endianness versus numeric bit shifts.

The loaded word is 0x78563412. Shifting right by 16 yields 0x00007856. The stored halfword 0x7856 places 0x56 at the lower address 102 and 0x78 at 103. Hexadecimal 56 equals 5×16+6=86.

**Common misconception:** Endianness determines byte order in memory, not which bits a numeric right shift discards.

## Q16

**Correct answer:** 1  
**Concept:** Matrix polynomial reduction.

Multiplication gives A²=−I. Hence I+A+A²=A, whose determinant is 0×0−(−1)×1=1. Reducing the polynomial before evaluating its determinant avoids unnecessary arithmetic.

**Common misconception:** Determinants do not distribute over matrix addition.

## Q17

**Correct answer:** -0.0833  
**Concept:** Covariance of dependent indicator variables.

Both marginals have mean 1/2 by symmetry. E[XY] is the probability of two reds: (2/4)(1/3)=1/6. Cov(X,Y)=1/6−1/4=−1/12=−0.083333… . The negative sign reflects depletion of red balls.

**Common misconception:** Equal marginal probabilities do not imply independence.

## Q18

**Correct answer:** 65534  
**Concept:** End-around carry in one's-complement checksums.

The ordinary sum is 0x10000. Fold the carry into the low word to obtain 0x0001. Its 16-bit complement is 0xFFFE, decimal 65534. Discarding the carry would instead yield the wrong checksum 65535.

**Common misconception:** One's-complement addition is not ordinary addition modulo 2¹⁶.

## Q19

**Correct answer:** 5  
**Concept:** Copy-on-write allocation.

Begin with three physical pages. The parent's first write to logical page 0 adds one copy, and the child's write to page 1 adds another. The parent's second write to its already private page 0 adds none. Total physical pages: 3+1+1=5; logical page 2 remains shared.

**Common misconception:** A repeated write does not copy a page that is already exclusively owned.

## Q20

**Correct answer:** C  
**Concept:** CPU execution-time comparison.

Ignoring the common factor N/10⁹, P's time is 1.5/3=0.5 and Q's time is 0.8×2/4=0.4. Speedup is old time divided by new time: 0.5/0.4=1.25. C is correct; A is its reciprocal, while B,D omit or miscombine factors.

**Common misconception:** Clock rate or CPI alone does not determine performance when instruction counts differ.

## Q21

**Correct answer:** 2  
**Concept:** CIDR alignment and exact coverage.

The blocks 192.0.2.32/27 and 192.0.2.64/27 cover 32–63 and 64–95. A single 64-address /26 block must begin at a multiple of 64, so it cannot begin at 32. Larger blocks include extra addresses. Therefore two are necessary and sufficient.

**Common misconception:** A power-of-two address count is insufficient for a single CIDR block without boundary alignment.

## Q22

**Correct answer:** A, B  
**Concept:** NULL in anti-membership queries.

For x=1, NOT IN compares against both 2 and NULL, yielding UNKNOWN; x=2 yields FALSE; x=NULL yields UNKNOWN. WHERE retains none, proving A. NOT EXISTS instead asks whether an equality is TRUE for some inner row. It finds a match only for x=2, returning 1 and NULL (B). Removing the inner NULL permits x=1 through NOT IN but leaves outer x=NULL UNKNOWN, refuting C. IN returns only 2, not three rows, refuting D.

**Common misconception:** NOT IN and correlated NOT EXISTS need not agree in the presence of NULL.

## Q23

**Correct answer:** A, C  
**Concept:** Circular wait and lock ordering.

P may acquire A while Q acquires B; each then waits for the other's mutex, so A holds. If P finishes before Q begins, no deadlock occurs, disproving B. Acquiring A before B in both threads prevents this cycle, proving C. Releasing locks immediately does not protect an operation that needs both held together, so D is false.

**Common misconception:** Avoiding deadlock does not by itself preserve the required mutual exclusion.

## Q24

**Correct answer:** D  
**Concept:** Asymmetric signed range.

The eight-bit signed range is −128 to 127. Negating 10000000 wraps back to 10000000, although mathematical +128 is outside that range. Zero (A) also negates to itself but its negation is representable. 127 and −1 (B,C) have representable, different negatives. Only D satisfies both conditions.

**Common misconception:** Two's-complement ranges have one more negative value than positive values.

## Q25

**Correct answer:** A, C  
**Concept:** Closures and minimal keys.

AB determines C and hence all attributes; neither A nor B alone does, so AB is a candidate key. BC determines A through C→A, and neither B nor C alone determines all attributes, so BC is also a candidate key. AC lacks B, and C's closure is only AC. Thus A,C are correct and B,D are not.

**Common misconception:** A determinant of one dependency need not be a key for the entire relation.

## Q26

**Correct answer:** B  
**Concept:** Array parameters and local pointer reassignment.

The parameter a is a pointer to x[0]; p saves that pointer. Advancing local a makes it point to x[1], without changing the caller's array or p. With n=3, a[n−2]=a[1] refers to x[2], which becomes p[0]+a[0]=4+7=11. x[0] stays 4. Only B matches; A treats pointer advancement as shifting array contents, and C,D miss the actual target.

**Common misconception:** Reassigning a pointer parameter and modifying its pointed-to object are different operations.

## Q27

**Correct answer:** 2  
**Concept:** Quantifier order and countermodels.

On a one-element domain, a witness for the sole x is necessarily a common witness, so the requested combination is impossible. On {0,1}, take R to be equality. Each x has its own witness y=x, but neither y is related to both x values. Size two is achievable and minimal.

**Common misconception:** A witness that depends on x need not be a single witness for all x.

## Q28

**Correct answer:** 1.718  
**Concept:** Mean value theorem.

The secant slope is (1−0)/(e−1). Since f′(c)=1/c, equality gives c=e−1=1.7182818… . This lies strictly between 1 and e and rounds to 1.718.

**Common misconception:** The mean value theorem point need not be the midpoint of the interval.

## Q29

**Correct answer:** 3  
**Concept:** Cycle detection trace.

After iterations 1,2,3, the (slow,fast) node pairs are (1,2),(2,4),(3,3). The first equality is therefore at node 3. The initial equality at node 0 is explicitly not tested before movement.

**Common misconception:** The test location in the loop affects whether an initial equality is mistakenly counted.

## Q30

**Correct answer:** C  
**Concept:** Structural invariants of recursive productions.

Each step adds complementary symbols to opposite ends. The base is empty. Induction therefore gives strings w followed by complement(reverse(w)), and any such string can be reduced by repeatedly stripping its complementary end pair. C is exact. A is too broad: abba has equal counts but equal end symbols and cannot be generated. B is wrong because nonempty generated strings have unequal end symbols. D omits ba, which is generated.

**Common misconception:** Equal symbol counts are necessary here but do not characterize the ordering constraint.

## Q31

**Correct answer:** 2  
**Concept:** Carry propagation in a binary increment.

All three bits flip precisely when the two low bits are 11. The inputs 011 and 111 become 100 and 000, respectively. Any other input stops carry propagation before the most significant bit, so only two qualify.

**Common misconception:** Wraparound from 111 to 000 still flips all bits and must be counted.

## Q32

**Correct answer:** C  
**Concept:** Cut property of minimum spanning trees.

If a spanning tree omitted a uniquely lightest cut edge e, adding e creates a cycle containing another cut-crossing edge of strictly greater weight. Exchanging them lowers total weight, contradicting minimality. Thus C holds. Tied weights do not necessarily create alternative MSTs (A); a maximum-weight bridge must be included (B); Kruskal can break ties arbitrarily and remains correct (D).

**Common misconception:** Global distinctness of all weights is stronger than the local uniqueness needed by this cut argument.

## Q33

**Correct answer:** 1  
**Concept:** Cache expiry rather than sliding expiration.

The initial entry expires at 120. Requests at 50 and 119 hit and do not change this. The request at 121 refreshes it until 241; the request at 200 then hits. Exactly one of these requests causes an upstream fetch.

**Common misconception:** A TTL is not automatically restarted on each cache hit.

## Q34

**Correct answer:** A, B  
**Concept:** Recognizability and decidability.

If both U and its complement were recognizable, dovetailing their recognizers would decide U, a contradiction; A holds. Every finite language is decidable by a finite lookup, so U is infinite (B). An infinite countable U has uncountably many subsets but only countably many machines, refuting C. D is also not forced: for a recognizable undecidable K, the language {0w:w arbitrary}∪{1w:w∈K} is recognizable and undecidable while containing the decidable infinite subset of strings starting with 0.

**Common misconception:** Closure properties of recognizable languages do not extend to arbitrary subsets.

## Q35

**Correct answer:** B  
**Concept:** An epsilon production selected by FOLLOW.

b belongs to FOLLOW(A), since S→Ab. With lookahead b, the predictive table selects A→ε: remove A from the stack and do not advance input. B is correct. A consumes a token too early; C requires lookahead a; D ignores the epsilon/FOLLOW rule.

**Common misconception:** A table entry for an epsilon alternative is determined by FOLLOW, not by a literal input epsilon.

## Q36

**Correct answer:** 5.375  
**Concept:** Synthesized attributes for positional notation.

The integer part evaluates as ((1×2)+0)×2+1=5. For the fraction, process the right recursion from its epsilon base: the final 1 gives 1/2; the preceding 1 gives (1+1/2)/2=3/4; the initial 0 gives (0+3/4)/2=3/8. The complete value is 5+3/8=5.375.

**Common misconception:** Fractional digits are weighted by decreasing powers of two; their recurrence differs from the integer-part recurrence.

## Q37

**Correct answer:** A, C, D  
**Concept:** Safe loop-invariant code motion.

n never changes, so 100/n is invariant on iterations where it is evaluated (A). But when n=0 the original loop executes no iterations and does not divide; unconditional hoisting introduces a trap, refuting B. Guarding the hoisted evaluation with n>0 evaluates it exactly when the loop has at least one iteration, where n is nonzero and the same quotient is used throughout (C). This demonstrates D: invariance does not ensure safety on newly executed paths.

**Common misconception:** Removing repeated computation may introduce an exception even when the expression's inputs are unchanged.

## Q38

**Correct answer:** 51  
**Concept:** Bounded compositions and generating functions.

The answer is the coefficient of x⁵ in (1+x+x²)⁵. Without upper bounds there are C(9,4)=126 solutions. For a chosen bin holding at least three tokens, remove three tokens: C(6,4)=15 remaining solutions. Subtract 5×15=75. Two bins cannot each hold three when the total is five, so no intersection correction is needed. The result is 126−75=51.

**Common misconception:** Identical tokens do not make the distinguishable bins interchangeable.

## Q39

**Correct answer:** B  
**Concept:** DISTINCT aggregates and NULL exclusion.

Department A has two distinct non-NULL salaries {10,20} and sum 40; both predicates hold. Department B has one distinct non-NULL salary {20} and sum 20; neither predicate holds. Therefore only A is returned, option B. A omits a qualifying group, C selects the failing group, and D includes both.

**Common misconception:** COUNT(DISTINCT salary) ignores NULL, and SUM still counts repeated non-NULL rows.

## Q40

**Correct answer:** 4  
**Concept:** Selective-repeat buffering and contiguous delivery.

Receiving 0 delivers it and moves the lower edge to 1. Packets 2 and 3 are buffered while 1 is missing; the lower edge stays 1. Arrival of 1 enables delivery of 1,2,3 in order, moving the lower edge to 4. Sequence-space wraparound is not reached in these four arrivals.

**Common misconception:** Receiving a higher sequence number alone does not move the lower edge past a missing packet.

## Q41

**Correct answer:** A, B, D  
**Concept:** A nilpotent chain and a finite matrix inverse series.

Choose v with A²v≠0. The vectors v,Av,A²v are linearly independent: applying A² to a supposed relation first makes the v coefficient zero; applying A then makes the Av coefficient zero; the last coefficient follows. They form a basis. A maps that basis to Av,A²v,0, so rank(A)=2 and rank(A²)=1 (A,B). Every eigenvalue λ obeys λ³=0, hence C is false. Multiplication gives (I−A)(I+A+A²)=I−A³=I, proving D.

**Common misconception:** A zero eigenvalue for every eigenvector does not mean the matrix itself is zero.

## Q42

**Correct answer:** B  
**Concept:** Array-index intervals of a complete-tree subtree.

At successive depths below node 6 the indices are {6},12–13,24–27,48–55,96–111. Only 96–100 exist at the final level. Counts are 1+2+4+8+5=20. B is correct. A omits the partial final level, D treats it as full, and C adds one nonexistent node.

**Common misconception:** A complete tree may have a partially populated last level inside a subtree.

## Q43

**Correct answer:** A, C  
**Concept:** Eliminating nongenerating and unreachable grammar symbols.

B has no terminating alternative: every derivation from B retains a B. Thus S→AB cannot produce a terminal string. All successful derivations use S→C, which generates exactly c*, proving A. Only S and C occur in successful derivations, proving C. Although A is separately reachable and generating, its only reachable context includes the nonterminating B; it is not useful, refuting B. D generates a terminal string but is unreachable from S, refuting D.

**Common misconception:** Reachability and generation tested in the unpruned grammar are not independently sufficient; remove nongenerating productions before recomputing reachability.

## Q44

**Correct answer:** 1  
**Concept:** Scheduling by earliest deadline and a lower bound.

Earliest-deadline order is C,A,B,D, with completion times 1,3,6,8 and latenesses −2,−1,0,1. Its maximum lateness is 1. No schedule can do better: total processing time is 8, so the last job finishes at 8, while every deadline is at most 7. The last job's lateness is at least 1. The exhibited schedule attains the lower bound.

**Common misconception:** Lateness can be negative; it is not the same as tardiness, which truncates negative values to zero.

## Q45

**Correct answer:** B  
**Concept:** Outstanding bytes and the updated send window.

After the ACK, outstanding data are bytes 23000 through 24999, totaling 2000. The effective window is min(10000,4000)=4000 bytes. Thus 4000−2000=2000 additional bytes can be sent. B is correct. A uses an obsolete window edge, C ignores outstanding data, and D exceeds the receive window.

**Common misconception:** A window advertises total allowed unacknowledged data, not an allowance entirely additional to data already in flight.

## Q46

**Correct answer:** 256  
**Concept:** Reuse distance and capacity misses.

Each row occupies one aligned cache line, so a column scan visits 16 different lines. Between successive accesses to one row's line, 15 other distinct lines are accessed, exceeding the capacity of eight. LRU therefore evicts every line before its next use. All 16×16=256 element reads miss, despite each row's elements sharing one line.

**Common misconception:** Spatial locality helps only when the line remains resident until the nearby element is accessed.

## Q47

**Correct answer:** B  
**Concept:** Prediction penalties and clock-period tradeoffs.

Old CPI is 1+0.20×0.60×3=1.36, giving 1.36 ns per instruction. New CPI is 1+0.20×0.10×3=1.06, with time 1.06×1.1=1.166 ns. Speedup is 1.36/1.166≈1.166. B is closest. A reverses the comparison; C ignores the longer clock; D treats the new execution time as 1 ns per instruction.

**Common misconception:** Improving CPI can be partly offset by a longer clock period.

## Q48

**Correct answer:** 24  
**Concept:** Full binary recursion trees.

Every internal invocation has exactly two children; there are 13 unit-segment leaves. A full binary tree with L leaves has L−1 internal nodes, so there are 13+12=25 invocations and markers. In postorder the root emits last. Immediately before that final emission, the other 24 have been emitted.

**Common misconception:** Unequal split sizes change the shape but not the full-binary-tree leaf/internal-node identity.

## Q49

**Correct answer:** 0.5  
**Concept:** Conditional expectation over a triangular region.

The conditioning region x+y>1 occupies area 1/2 in the unit square. By symmetry about x=y, integrate min(x,y)=x over the half where x≤y and double. For 0≤x≤1/2, y ranges from 1−x to 1; for 1/2≤x≤1, y ranges from x to 1. The unnormalized integral is 2[∫₀¹ᐟ² x² dx + ∫₁ᐟ²¹ x(1−x) dx]=2[1/24+1/12]=1/4. Dividing by probability 1/2 gives 1/2.

**Common misconception:** Conditioning destroys the original independence and changes the integration region.

## Q50

**Correct answer:** C  
**Concept:** Context-free union and intersection limitations.

L is the union of {aⁿbⁿcᵏ} and {aⁱbⁿcⁿ}; both are context-free, so L is context-free. It contains every aⁿbⁿcⁿ, making its intersection with that language exactly the non-context-free language {aⁿbⁿcⁿ}. C is correct. A incorrectly infers complexity from containing a subset. B is false: intersecting L with the regular language a*b* (no c) gives {aⁿbⁿ}∪a*, which is nonregular; alternatively a standard regular pumping argument on aᵖbᵖ disproves regularity of L itself. D is false because cᵏ is in L for every k.

**Common misconception:** Context-free languages are closed under union, but not arbitrary intersection.

## Q51

**Correct answer:** 405  
**Concept:** Matrix-chain dynamic programming.

For adjacent pairs, costs are m12=150,m23=360,m34=180. For triples, m13=min(360+600,150+180)=330 and m24=min(180+150,360+600)=330. Splitting the four-matrix chain after positions 1,2,3 gives costs 330+250=580, 150+180+75=405, and 330+300=630. The minimum is 405, achieved by (A1A2)(A3A4).

**Common misconception:** Multiplication is associative algebraically, but the intermediate dimensions determine computational cost.

## Q52

**Correct answer:** A, C  
**Concept:** Join multiplicities under set semantics and functional dependencies.

Each of two R rows matches both S rows on B=x. J contains (1,x,p),(1,x,q),(2,x,p),(2,x,q), so A holds. Each A value has two C values, refuting B. Projecting away C yields exactly the two original R rows, proving C. B=x occurs in four tuples, so it is not a key, refuting D.

**Common misconception:** Set semantics eliminate duplicate complete tuples, not distinct matching combinations.

## Q53

**Correct answer:** 3  
**Concept:** Register requirements for expression-tree evaluation.

A leaf needs one register, and each sum of two leaves needs two. The right subtree adds two such sums: whichever is evaluated first occupies one retained register while the second needs two, giving three registers. The left subtree needs two. Evaluate the right subtree first, retaining its result in one register while evaluating the left in the other two; then multiply. Three suffice and are necessary because the right subtree alone requires three.

**Common misconception:** Evaluating the left child first everywhere can use more registers than choosing the larger-demand subtree first.

## Q54

**Correct answer:** A, C  
**Concept:** Dovetailing and enumeration of recognizable languages.

Dovetailing eventually performs every finite number of steps of every started simulation, so each accepting computation is eventually found (A). If L is finite, other simulations may loop forever and there is no general way to detect that no further member will be found; B is false. With L empty no simulation accepts, so an infinite silent run is possible (C). Waiting for a nonmember to print never terminates, refuting D.

**Common misconception:** An enumeration is evidence of membership when an item appears, not evidence of nonmembership when it has not yet appeared.

## Q55

**Correct answer:** B  
**Concept:** Resource-count deadlock guarantee.

With six instances, each of three processes can hold two and wait for a third, giving a deadlock. With seven, if every unfinished process holds at most two, at most six are held and at least one remains available. Some waiting process can therefore receive another instance and complete once it reaches its requirement, releasing resources. The worst-case requirement is three for each process, so seven suffice and six do not. B is the minimum; A is unsafe, and C,D are sufficient but not minimal.

**Common misconception:** Preventing deadlock does not require satisfying every process's maximum demand simultaneously.

## Q56

**Correct answer:** 7  
**Concept:** State transition tracing of a feedback shift register.

Applying all next-state equations simultaneously gives 001→011→111→110→101→010→100→001. No earlier state equals the initial state. The first return is after seven edges.

**Common misconception:** Next-state equations all use the old bits; updating bits sequentially computes a different machine.

## Q57

**Correct answer:** B  
**Concept:** Aggregate analysis of parent-pointer traversal.

Across the entire traversal, each downward tree edge is followed once to visit its child, and each upward edge is followed at most once when a subtree is exhausted. All constant work over n successor operations plus at most n−1 downward and n−1 upward traversals is O(n). Visiting all n nodes also gives Ω(n), hence Θ(n). A cannot account for visiting n nodes. C,D incorrectly multiply the worst single-operation cost by n; even on a path, the final long ascent occurs only once.

**Common misconception:** A worst-case O(height) successor call does not imply O(n×height) total traversal time.

## Q58

**Correct answer:** 0.8  
**Concept:** Polling versus interrupt CPU overhead.

Polling occurs 1,000,000/50=20,000 times per second and costs 40,000 microseconds, or 4.0% CPU time. Interrupts cost 4000×8=32,000 microseconds, or 3.2%. The saved fraction is 4.0−3.2=0.8 percentage points.

**Common misconception:** The relative reduction is 20%, but the requested difference in percentage points is 0.8.

## Q59

**Correct answer:** A, B, D  
**Concept:** Rounding-induced nonassociativity.

In [16,32), the spacing is 2. The exact 16+1=17 is midway between 16 and 18, and ties-to-even selects 16, so (a+b)+c=0 (A). For the other grouping, 1−16=−15 is exactly representable with four significant bits (1111₂), and 16−15=1 is exact (B). Real arithmetic gives 1 (D). The unequal computed results refute C without any overflow.

**Common misconception:** Finite-precision rounding alone breaks associativity, even with unbounded exponents.

## Q60

**Correct answer:** A, B, D  
**Concept:** Ordering resource and mutex waits in a bounded buffer.

The consumer can lock M and block on F=0. The producer can obtain E but then blocks on M, so it cannot insert and signal F; A,D describe this cycle. Waiting for F before acquiring M means an empty-buffer consumer holds no mutex, allowing the producer to fill and signal; B holds for this specific deadlock. Extra capacity changes E but not the blocked consumer's need for F or the producer's need for M, refuting C.

**Common misconception:** More buffer space cannot fix an ordering cycle involving a mutex and an empty-item semaphore.

## Q61

**Correct answer:** -1  
**Concept:** Convexity after subtracting a quadratic.

Let g(x)=f(x)−x(x−2). Then g″=f″−2≥0, so g is convex, and g(0)=g(2)=0. A convex function lies below the chord joining two endpoints, hence g(1)≤0. Therefore f(1)≤1(1−2)=−1. Equality is attained by f(x)=x(x−2), which satisfies every condition. The greatest possible value is −1.

**Common misconception:** Positive curvature with zero endpoint values bounds the interior from above by a negative quadratic; it does not force positive interior values.

## Q62

**Correct answer:** C  
**Concept:** Conditional HTTP validation.

A matching entity tag permits the server to report that the cached representation may be reused without transferring the full representation body. The client still sends the request and receives the validation response, so a network round trip remains (C). A confuses validation with a fresh local-cache hit. B incorrectly assigns a representation body to 304. D makes an unsupported claim about unrelated caches.

**Common misconception:** Saving transferred bytes and eliminating network latency are different benefits.

## Q63

**Correct answer:** 3  
**Concept:** Fan-in bounds and balanced XOR trees.

An output depending on eight distinct inputs requires at least seven two-input gates: merging eight independent input contributions into one output takes at least seven merges. A balanced tree uses four XORs in layer one, two in layer two, and one in layer three, achieving seven gates and delay three. A depth-d two-input circuit can depend on at most 2ᵈ inputs, so depth less than three cannot cover all eight. The minimum delay among minimum-gate circuits is therefore three.

**Common misconception:** A serial seven-gate chain has minimum gate count but not minimum delay.

## Q64

**Correct answer:** A  
**Concept:** Conflict versus view serializability with blind writes.

On x, the first two writes create T1→T2, while the second and third create T2→T1. This cycle rules out conflict serializability. For view equivalence, x's final writer T1 forces T2 before T1. The read of y by T3 reads T2's write, forcing T2 before T3. No constraint orders T1 versus T3. Thus the two serial orders are T2,T1,T3 and T2,T3,T1. A is correct. B,D incorrectly ignore the conflict cycle; C incorrectly treats it as proof against view serializability.

**Common misconception:** Blind writes allow some view-serializable schedules to fail conflict serializability.

## Q65

**Correct answer:** 16  
**Concept:** Sparse allocation of multilevel page tables.

Each leaf covers 1024 virtual pages. Pages 0 and 1023 use leaf index 0; page 1024 uses index 1; pages 2048 and 3071 use index 2. Thus three leaf pages plus the root occupy four pages, each 4 KiB, for 16 KiB. Data pages are explicitly excluded.

**Common misconception:** Count allocated leaf-table regions, not one leaf table per mapped data page.
