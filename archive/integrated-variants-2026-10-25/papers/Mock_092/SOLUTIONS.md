# Worked Solutions — Mock Test 092

## Q1

**Correct answer:** 17

**Concept:** Applying an alternating recurrence.

The terms are 3,6,5,10,9,18,17. Six updates produce the seventh term, 17.

**Common misconception:** Repeating only one operation or counting the initial term as an update.

## Q2

**Correct answer:** 50

**Concept:** Side sum, squared length and area.

For sides a,b, a+b=15 and a²+b²=125. Hence 2ab=(a+b)²−(a²+b²)=225−125=100, so area ab=50.

**Common misconception:** Treating the diagonal as the sum of the sides.

## Q3

**Correct answer:** D

The relative clause “that were discussed” modifies plural proposals, while the main clause's subject is singular “One,” requiring has. D supplies both. A is wrong in both positions; B gets the relative clause right but not the main clause; C gets the main clause right but not the relative clause.

## Q4

**Correct answer:** 9

**Concept:** Work-rate conservation.

The job requires 6×8=48 worker-days. The first two days complete 12 worker-days, leaving 36. Four workers require 36/4=9 additional days.

**Common misconception:** Applying the reduced workforce to work already completed.

## Q5

**Correct answer:** A, B, D

**Concept:** Combining implication with a cardinality constraint.

If P were ON, Q would be ON, forcing R and S OFF because exactly two switches are ON. But R OFF would require S ON, a contradiction. Hence A is true. The implication R OFF implies S ON forbids R and S both OFF, so B is true. Q need not be ON: R,S ON with P,Q OFF is valid, making C false. If Q is OFF, P must also be OFF, and the two ON switches must be R and S; D is true. The complete valid ON pairs are QR, QS and RS.

**Misconception:** Applying implications separately while ignoring the exact-count constraint.

## Q6

**Correct answer:** 0.25
**Concept:** Conditional counting with parity.

Of C(6,2)=15 pairs, C(3,2)=3 are odd-odd and have odd product. Twelve pairs satisfy the condition. Within them, an even sum requires even-even, giving C(3,2)=3 favourable pairs. The probability is 3/12=1/4.

**Common misconception:** Odd-odd pairs have even sum but must be removed by the conditioning event.

## Q7

**Correct answer:** B
**Concept:** Survey evidence and causality.

The survey establishes only what respondents reported. Voluntary selection may bias their composition, and no comparison separates the app's effect from other causes. B preserves those limits. A overgeneralizes and asserts causality; C treats self-selection as representativeness; D mistakes absence of causal evidence for proof of no benefit.

**Common misconception:** Failure to establish a causal claim does not establish its negation.

## Q8

**Correct answer:** 15

Separate cases according to C's group. If C is with A, choose their third member from D,E,F in three ways; C is that group's leader and the other group has two eligible leaders because B is excluded, giving 6 assignments. If C is with B, choose their third member in three ways; C leads that group and any of the three members of A's group may lead it, giving 9. Total 6+9=15. Distinguishing the groups by whether they contain A or B counts every unlabelled partition once, so no further division by two is needed.

## Q9

**Correct answer:** 47.73 (range 47.725–47.735)

Concept: changing mixture weights. Old combined percentage=100·91/110=82.72727…. New combined percentage=100·35/100=35. Difference=47.72727… percentage points, rounded to 47.73; range 47.725–47.735. A improves from 90% to 95%, B from 10% to 20%, yet the new mix gives much greater weight to B. Averaging the two centre percentages would ignore candidate counts.

## Q10

**Correct answer:** 32

The cut unfolds into a diamond with vertices(3,4),(4,3),(5,4),(4,5). Each side has length sqrt2, so its perimeter is4sqrt2 and its square is32. The fold boundaries become interior symmetry axes, not extra hole-boundary segments.

## Q11

**Correct answer:** 3

Rotation makes10 the root,20 its right child, and15 the left child of20;30 remains20's right child. Searching30 visits10,20,30: three nodes. Rotation preserves inorder order but changes search depths.

## Q12

**Correct answer:** B

**Concept:** CRC detection using a polynomial factor.

An undetected error polynomial must be divisible by the generator, hence by x+1. Over GF(2), this implies E(1)=0, meaning an even number of nonzero coefficients. Any odd-weight error has E(1)=1 and is detected. B is correct. Even-weight errors may be undetected, so A and C are not universal guarantees; a nonzero multiple of the generator refutes D.

**Common misconception:** Treating a CRC as detecting every nonzero corruption.

## Q13

**Correct answer:** C
**Concept:** Gray/binary conversion.

Decode by prefix XOR: b2=1,b1=1 XOR 0=1,b0=1 XOR 1=0, giving binary 110=6. The next integer is 111=7, whose Gray code is 100. C is correct. A is the decoded current binary word; B is next binary rather than Gray; D is neither conversion result.

**Common misconception:** Incrementing a Gray word as an ordinary binary number does not generally advance its decoded integer by one.

## Q14

**Correct answer:** 0

E[X]=1,E[Y]=1/2, and XY equals1 only when X=1, giving E[XY]=1/2. Cov(X,Y)=1/2−1×1/2=0. This does not imply independence: Y is a nonconstant deterministic function of X. Zero covariance can coexist with dependence.

## Q15

**Correct answer:** B, C

R∩S contains only the three diagonal pairs, proving B. R∪S includes(1,2) and(2,3) but not(1,3), so A and D are false. Transitive equivalence closure connects all three elements, making C true. A union of equivalence relations need not itself be an equivalence relation.

## Q16

**Correct answer:** 14

From low to high:1+0 gives c1=0;1+1+0 gives c2=1;0+1+1 gives c3=1;1+0+1 gives c4=1. Thus c4c3c2c1=1110, unsigned14. This asks for the internal carry pattern, not the retained four-bit sum0001 or the full five-bit sum10001.

## Q17

**Correct answer:** A, D

**Concept:** Compiler Design — Constant propagation

Both concrete paths give x+y=5, proving A. At the join, x has values2 or3 and y has3 or2; each independently becomes not constant. This abstraction loses the relation x+y=5 and cannot evaluate the sum as a constant there. Evaluating within each branch first produces the same constant 5 for z on both incoming paths, which survives the join. Thus D holds, B,C do not.

- **A:** True: the two concrete branch sums both equal5.
- **B:** False: x differs between the incoming paths.
- **C:** False: independent unknown values do not retain their correlation.
- **D:** True: equal incoming constants for z survive the join.

**Common misconception:** A property true on every path may be lost by an abstraction that forgets correlations.

## Q18

**Correct answer:** B, D

Concept: backward liveness. After `x=d`, only y is needed by return. Immediately before that assignment, d is needed as its source and y remains needed, so B and D are live after statement two. The old x is overwritten before any further use, making A false; c has already had its last use, making C false. Syntactic liveness precedes any deletion of the dead assignment.

## Q19

**Correct answer:** 3456

Concept: control-store capacity. Address width=2+3+2=7 bits, giving 128 words. Word width=20+7=27 bits, so total=128·27=3456 bits. The next-address field contributes to word width as well as the physical store having an address input.

## Q20

**Correct answer:** 0.5

There are 16 equally likely ordered pairs and 12 unequal ones. Six unequal pairs have minimum zero: (0,j),(j,0) for j=1,2,3. The conditional probability is 6/12. Equal backoffs, including (0,0), are excluded by the condition.

## Q21

**Correct answer:** 5

**Concept:** Relationship cardinalities and integer bounds.

With d departments, 3d≤17, so d≤5. Five are achievable with department sizes 3,3,3,3,5.

**Common misconception:** Rounding a maximum feasible count upward.

## Q22

**Correct answer:** A

**Concept:** Necessary versus sufficient conditions.

The pumping property is necessary for regularity, so its failure implies nonregularity, proving A. Its converse is not supplied by the lemma, refuting B. Infinite regular languages such as a* refute C. Every sufficiently large bound also works once a pumping length works, refuting D.

**Common misconception:** Reversing a one-way implication.

## Q23

**Correct answer:** A, C

The state, head position and contents of the bounded tape range form a finite configuration space, proving C. Determinism means a repeated complete configuration repeats the future forever. Simulating until halt or repetition therefore decides halting, proving A. A machine may loop within one cell, refuting B. The finite bound is essential and does not apply to unrestricted machines, refuting D.

## Q24

**Correct answer:** A

Concept: contiguous allocation. Free space is split into separate holes, neither large enough, which is external fragmentation (A). B concerns waste inside allocated blocks and no such block was allocated; C is unnecessary; D has no connection to the allocation failure. Total free capacity is not the maximum contiguous capacity.

## Q25

**Correct answer:** A, C

**Concept:** Unique-light-edge cut property.

If an MST omitted e, adding e creates a cycle containing another crossing edge. That crossing edge is heavier because e is uniquely minimum; replacing it gives a lighter spanning tree, contradiction. Thus A and C hold. An MST may cross the cut through several edges, refuting B. A triangle with distinct edge weights supplies a cut-minimum edge that is not a bridge, refuting D.

**Common misconception:** Assuming an MST must cross every cut exactly once.

## Q26

**Correct answer:** 4

The visited bank numbers are3,1,7,5, then3. Equivalently the period is8/gcd(8,6)=4. The starting address shifts the visited residue class but does not change this period.

## Q27

**Correct answer:** 1

**Concept:** Eigenvalues of a rank-one matrix.

Au=u(vᵀu) and vᵀu=2−3=−1, so −1 is an eigenvalue. The two-dimensional kernel of vᵀ is annihilated by A, yielding two zero eigenvalues. The sum of squares is (−1)²=1.

**Common misconception:** Summing squared matrix entries instead of squared eigenvalues.

## Q28

**Correct answer:** 1

Concept: NULL-aware aggregate conditions. Group A has zero distinct non-null x values and fails. B has one distinct non-null value and counts COUNT(*)=2, COUNT(x)=1, passing both tests. C has one distinct value but both counts equal two, failing the second test. Only B remains. COUNT(DISTINCT x) and COUNT(x) both ignore NULL, unlike COUNT(*).

## Q29

**Correct answer:** -0.0833 (range -0.08335–-0.08325)
**Concept:** Covariance of dependent indicator variables.

Both marginals have mean 1/2 by symmetry. E[XY] is the probability of two reds: (2/4)(1/3)=1/6. Cov(X,Y)=1/6−1/4=−1/12=−0.083333… . The negative sign reflects depletion of red balls.

**Common misconception:** Equal marginal probabilities do not imply independence.

## Q30

**Correct answer:** B, D

Let q=P(A∩B). The feasible interval is max(0,0.8+0.7−1)≤q≤min(0.8,0.7), or0.5≤q≤0.7. B chooses0.6 and D implies q=0.5, both feasible. A is below the lower bound. C would give q=0.5·0.7=0.35, also impossible. A conditional probability must be compatible with the other supplied probabilities.

## Q31

**Correct answer:** A

**Concept:** Preserving expression availability across unrelated assignments.

Neither a nor b changes between t and u, so t is the correct replacement, A. c=d+e need not equal a+b, refuting B and C. D leaves a use of an undefined replacement value.

**Common misconception:** Assuming every intervening assignment invalidates every available expression.

## Q32

**Correct answer:** A, C
**Concept:** Tagged translations and stale mappings.

Different ASIDs distinguish P's and Q's translations, so switching need not flush P's entries (A). Both ASID and virtual page number are needed to identify a particular translation, refuting B. Recycling an ASID may make old entries falsely match a new address space, so invalidation may be required (C). Changing a mapping can still make a tagged entry stale, refuting D.

**Common misconception:** Tags avoid unnecessary context-switch flushes but do not make stale entries correct.

## Q33

**Correct answer:** 1.25

The stored integers are 46 and 28. Their sum 74 wraps modulo 64 to 10, which decodes as 10/8=1.25. The exact numerical sum is 9.25, outside the format's maximum 63/8. Wraparound is neither saturation nor rounding.

## Q34

**Correct answer:** 3

Each block holds floor(512/90)=5 unspanned records. Twelve records require three blocks, with capacity 15. Therefore three additional records fit without another block. The unused62 bytes per full block cannot combine across boundaries to hold a record because spanning is prohibited.

## Q35

**Correct answer:** 0

Index2 has children at indices4,5 in a seven-element heap. Both must have larger keys than their parent in a distinct-key min-heap, but7 is the largest available key. The stipulated position is impossible, so there are zero such heaps. A heap's largest key must be at a leaf, though a particular leaf is not prescribed.

## Q36

**Correct answer:** 24

There are2·3=6 leaves, each with4 data entries, so24. Internal separator copies are routing metadata and are excluded from the data count.

## Q37

**Correct answer:** 3

Without the edge-count constraint, s→a→b→t costs3. Among routes with at most two edges, direct s→t costs10, s→a→t costs9, and s→b→t costs6. The permitted optimum is6, exceeding3 by3. Keeping only one unrestricted distance per vertex does not encode a remaining hop budget.

## Q38

**Correct answer:** 2

Entry(1,1) of A³ counts directed walks of length3 from1 back to1. They are1→2→4→1 and1→3→4→1, giving2. Matrix powers count walks of an exact length, not arbitrary reachability or only simple paths in general.

## Q39

**Correct answer:** 3

**Concept:** Shortest paths after an edge failure.

Originally A–B–C–D costs 2+1+2=5. After deleting BC, A–B–D costs 8 and A–C–D costs 9, with positive-weight detours unable to improve either. The new optimum is 8, an increase of 3.

**Common misconception:** Keeping a path that still contains the failed edge in the recomputation.

## Q40

**Correct answer:** 203

The first four issues occur at0,1,2,3 and complete at100,101,102,103. Each completion frees a slot for another issue in that same cycle. Those four new requests finish at200,201,202,203. The last completion is203. Unlimited parallelism would wrongly allow all eight misses to issue by7; fully serial service would ignore the four outstanding slots.

## Q41

**Correct answer:** 3
**Concept:** Value-based DAG sharing.

Let original operands be a0,b0,c0. t1 and t2 share node N1=a0+b0. The assignment to a creates N2=N1+c0. t3 creates N3=N2+b0, because a's value has changed. t4=N1+c0 shares N2. Exactly three addition nodes suffice.

**Common misconception:** Expression identity depends on operand values and versions, not only textual variable names.

## Q42

**Correct answer:** B, C

A small addend can round away at a large magnitude, proving B. Subtracting nearby rounded quantities can expose their prior approximation errors, proving C. Rounding at intermediate operations can break associativity, making A false. Finite precision and exponent range cannot represent all arbitrarily large integers exactly, disproving D.

## Q43

**Correct answer:** 4

Words0,4 conflict in line0 and words1,5 in line1. Alternation makes all eight direct-mapped accesses miss. The fully associative cache holds all four distinct words after four compulsory misses; the second round is entirely hits. The miss reduction is8−4=4. Equal capacity does not imply equal conflict behavior.

## Q44

**Correct answer:** A, C, D
**Concept:** Divisor lattices as products of chains.

Write 60=2²×3×5. Divisors correspond to exponent vectors in {0,1,2}×{0,1}×{0,1}, with meet and join given by coordinatewise minimum and maximum. This is a lattice and is distributive, proving A,D. A complemented vector must choose either zero or the full exponent in each coordinate, giving 2³=8: C is true. A divisor with 2-exponent one, such as 2, has no complement, so B is false.

**Common misconception:** Distributive does not imply that every element is complemented; a three-element chain is not Boolean.

## Q45

**Correct answer:** 208

Begin with all 256 addresses assigned A. The /26 removes 64. The more specific /27 restores 32 of them to A, but the /28 removes 16 from that restored block. Thus 256−64+32−16=208. Counting the /24 and /27 separately without subtracting overridden subranges would double count.

## Q46

**Correct answer:** 26

Concept: pointer-to-pointer updates. Initially *p points to x; the first change raises x from 4 to 6. Assigning *p=q changes main's p to point to y. The last change raises y from 7 to 10. Printed value is x+y+*p=6+10+10=26. Updating the caller's pointer requires, and here uses, its address.

## Q47

**Correct answer:** 12668

Virtual5500 has page number5 and offset5500−5×1024=380. Replace the page number by frame12 and preserve the offset:12×1024+380=12668. Translation changes the frame portion, not the within-page displacement.

## Q48

**Correct answer:** 5

Concept: maximal munch and priority. Tokens are identifier ifx, integer 12, keyword if, plus, integer 007. Longest match takes ifx rather than splitting keyword if and identifier x. The later exact if tie goes to the keyword. Leading zeroes do not split the integer under the given regex, so total five.

## Q49

**Correct answer:** 1

FIRST(B)={a,b}, so FOLLOW(A)={a,b}. A→aA enters cell(A,a); A→ε enters both(A,a) and(A,b), creating exactly one conflicting cell(A,a). The two B alternatives have disjoint FIRST sets{b} and{a}. S has only one production. The number of conflicted cells is1, even though the epsilon production populates two cells.

## Q50

**Correct answer:** 8

State1 records that the latest symbol was a without any aa yet. State2 records that aa has occurred and is absorbing. Count strings avoiding aa: if F(n) is their count, F(n)=F(n−1)+F(n−2), with F(0)=1,F(1)=2. Hence F(2)=3,F(3)=5,F(4)=8. Subtract from all16 length-four strings to get8 accepted strings. Counting occurrences instead of strings can double-count words such as aaaa.

## Q51

**Correct answer:** 7 (exact)
**Concept:** Balanced parentheses with a depth bound.

A nonempty primitive balanced block of maximum depth at most two has the form '(' followed by k copies of '()' then ')', contributing k+1 pairs. Every depth-at-most-two string decomposes uniquely into such blocks. Thus strings with four pairs correspond to compositions of 4, of which there are 2³=8. Exactly one, ()()()(), has maximum depth one. Subtract it to obtain seven with depth exactly two.

**Common misconception:** Counting all balanced strings ignores the nesting-depth restriction; counting depth at most two still includes depth one.

## Q52

**Correct answer:** 157

There are400/20=20 bursts, occupying100 cycles. Only19 gaps lie between them, taking57 cycles. Completion occurs after157 cycles. Adding a twentieth gap would count time after completion, contrary to the stated boundary condition.

## Q53

**Correct answer:** 1

**Concept:** Pivoting before LU elimination.

After the swap, rows are (2,1,0),(0,1,1),(4,3,2). The first-column multipliers are zero and two. Eliminating row three gives (0,1,2); dividing its second entry by the row-two pivot one gives L32=1. The final U33 is then one.

**Common misconception:** Reading elimination multipliers from the unswapped matrix.

## Q54

**Correct answer:** 4

**Concept:** Recursion-tree argument sizes.

The root 10 splits equally into 5,5. Each 5 splits unequally into 2,3. Each 2 splits equally into 1,1; each 3 splits unequally into 1,2. Thus the two size-5 calls and two size-3 calls are exactly the unequal splits, totalling four.

**Common misconception:** Counting only distinct odd lengths instead of separate calls with those lengths.

## Q55

**Correct answer:** 9 (exact)
**Concept:** Stack nondeterminism with prefix feasibility.

Seven a symbols push seven Xs. Five b symbols must pop seven, so exactly two b transitions must pop two symbols and three must pop one. Without prefix restrictions there are C(5,2)=10 choices. Before the first two b symbols, only three pushes have occurred; choosing both those b transitions as double pops is impossible. Every other choice is feasible: the first pop has at least two available symbols, the first two together use at most three, and the four later pushes supply all remaining demand. Answer 10−1=9.

**Common misconception:** Final push/pop balance is necessary but insufficient; every prefix must have enough stack symbols.

## Q56

**Correct answer:** A

**Concept:** Databases — Concurrency control

Each upgrade needs an exclusive lock, which is incompatible with the other transaction's shared lock. Neither shared lock is released until commit, and neither transaction can progress to commit, so a deadlock is possible. Retaining exclusive locks until commit still prevents dirty reads by other properly locking transactions.

A correctly states both facts. B confuses compatibility of existing shared locks with compatibility of an exclusive upgrade. C is false: releasing the shared lock enters the shrinking phase, so later acquiring an exclusive lock violates two-phase locking. D is false: acquiring an exclusive lock before the read serializes the entire read-modify-write operation, preventing a lost update.

- **A:** True: deadlock is possible due to incompatible lock upgrades, but strict 2PL prevents dirty reads.
- **B:** False: confuses compatibility of existing shared locks with compatibility of exclusive lock upgrades.
- **C:** False: releasing a lock enters the shrinking phase, so later acquiring an exclusive lock violates two-phase locking.
- **D:** False: acquiring an exclusive lock before reading serializes transactions, preventing lost updates.

**Common misconception:** A serializability or recovery guarantee does not imply deadlock freedom.

## Q57

**Correct answer:** A

**Concept:** Forked private state.

Each process starts with its own logical copy of counter=5 and increments it to six. Copy-on-write implementation details do not turn the ordinary global into shared writable state. Thus A holds; B assumes sharing, while C,D contradict the executed increment and inherited value.

**Common misconception:** Confusing initially identical contents with a shared variable.

## Q58

**Correct answer:** A, C

A establishes descending score order first; the later stable department sort groups departments while retaining that score order and original tie order within each. C directly uses the desired composite key and stability, so both work. B makes score the primary final key and can intermix departments. D reverses the original order of equal-key records, which later stable sorts retain rather than restore. Stable multi-pass sorting processes the least significant key first.

## Q59

**Correct answer:** C

**Concept:** Precedence cycles and observed reads.

r1(X) before w2(X) gives T1→T2. r2(Y) before w1(Y) gives T2→T1. The cycle refutes both serial orders in A and B. In serial T1,T2, T2 reads Y=1; in serial T2,T1, T1 reads X=1, so neither reproduces both zero reads. Thus C holds. D overlooks read–write conflicts across transactions.

**Common misconception:** Checking only write–write conflicts.

## Q60

**Correct answer:** 2

Work modulo2. (u+v)(v+w)+uw simplifies to uv+v+vw=v(u+1+w). It is1 precisely when v=1 and u=w, giving(0,1,0) and(1,1,1). The duplicate uw terms cancel in parity arithmetic.

## Q61

**Correct answer:** A, B, D
**Concept:** A nilpotent chain and a finite matrix inverse series.

Choose v with A²v≠0. The vectors v,Av,A²v are linearly independent: applying A² to a supposed relation first makes the v coefficient zero; applying A then makes the Av coefficient zero; the last coefficient follows. They form a basis. A maps that basis to Av,A²v,0, so rank(A)=2 and rank(A²)=1 (A,B). Every eigenvalue λ obeys λ³=0, hence C is false. Multiplication gives (I−A)(I+A+A²)=I−A³=I, proving D.

**Common misconception:** A zero eigenvalue for every eigenvector does not mean the matrix itself is zero.

## Q62

**Correct answer:** 370
**Concept:** Fragment offsets.

Maximum payload is 1500−20=1480, already divisible by eight. The payloads are 1480,1480,1040. The final fragment starts after 2960 payload bytes, so its offset field is 2960/8=370.

**Common misconception:** Fragment offsets measure original payload position, excluding all IPv4 headers.

## Q63

**Correct answer:** A, C
**Concept:** Boolean substitution with dependent inputs.

Substitute s=a: F=(NOT a)a+ab=ab, proving A. With a=0, F is always zero, refuting B. NAND(a,b) followed by inversion computes ab, proving C. OR differs at (a,b)=(0,1), refuting D.

**Common misconception:** A selector tied to a data input is not an independent Boolean variable.

## Q64

**Correct answer:** A, C

The probes are 0,1,4,2,2,4,1. Four distinct slots are reachable, so the first four insertions succeed and the fifth fails despite three unused slots. This proves A and refutes B. Slot 3 is never probed, proving C. Linear probing visits all seven slots and permits seven insertions, so D is false. Table occupancy alone does not ensure a restricted probe sequence finds an empty slot.

## Q65

**Correct answer:** 14

The combined mean is5. The within-group variance average is(1+9)/2=5. Each group's mean is3 from the combined mean, so the between-group contribution is9. Total population variance is5+9=14. Averaging variances alone omits the spread of group means.

