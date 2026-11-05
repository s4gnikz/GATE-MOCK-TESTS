# Worked Solutions — Mock Test 079

## Q1

**Correct answer:** B

**Concept:** Induction versus universal deduction.

The observations support a tentative pattern restricted to the observed circumstances, as B says. A generalizes across every route and bus; C makes an unsupported dry-weather claim; D treats association as proof of a unique cause. None of those stronger claims follows.

**Common misconception:** Turning repeated observations into a logically necessary universal statement.

## Q2

**Correct answer:** C

**Concept:** General Aptitude — Two- and three-dimensional patterns

1. With A on top, the clockwise side-face order consistent with front B and right C begins B,C. The other view with the same top places D immediately before E in that order.
2. The four side labels are distinct, so their cyclic order is B,C,D,E. Opposite side pairs are B-D and C-E.
3. The third view is consistent with F opposite A and confirms the orientation without changing B's opposite.

- **A:** A is adjacent to B in the first view.
- **B:** C is adjacent to B in the first view.
- **C:** D lies two positions from B around the four side faces.
- **D:** E is adjacent to B in the third view.

**Common misconception:** Face adjacency and cyclic orientation together determine opposite faces.

## Q3

**Correct answer:** 27

**Concept:** Constant second differences with an erroneous observation.

The first three terms give differences5 and8. Continuing with difference increment3 gives the sequence3,8,16,27,41, which changes only the fourth observation. This repair is unique: any two quadratic sequences agreeing at three distinct positions are identical, whereas two proposed one-position repairs would agree at at least three of the five positions. Thus no different constant-second-difference repair exists.

**Misconception:** Extending a pattern without checking the remaining observations or uniqueness.

## Q4

**Correct answer:** 48

The midpoint quadrilateral has perpendicular diagonals equal to the rectangle's sides12 and8. Its area is(1/2)·12·8=48. Equivalently, the four removed corner triangles total half the original area96. Joining midpoints does not leave a rectangle with sides6 and4.

## Q5

**Correct answer:** C

**Concept:** Agreement with the head of a subject phrase.

“Neither” is singular here and correctly takes “is”, C. A needs “has”, B's singular “list” needs “is”, and D's plural “results” needs “indicate”.

**Common misconception:** Matching the verb to the nearest noun rather than the subject's grammatical head.

## Q6

**Correct answer:** 38.89 (range 38.885–38.895)

Concept: compound revenue factors. Let the sticker-price multiplier be r. Revenue relative to last month is 0.8·0.9·r. Setting this to one gives r=1/0.72=25/18. Increase=100(r−1)=38.888…%, rounded to 38.89; accepted range 38.885–38.895. Adding the two losses as 30% would use the wrong compound factor.

## Q7

**Correct answer:** B

Let a,b,c,d denote the truth statuses. The statements impose a=NOT b, b=NOT c, c=NOT d, d=a AND b. Since a and b are opposites, a AND b=0, so d=0, c=1, b=0, a=1. Exactly A,C tell the truth, option B. Options A,C,D list pairs inconsistent with these statuses. A liar's statement must be false, not merely unproved.

## Q8

**Correct answer:** A

**Concept:** Ordered three-dimensional transformations.

The first transformation gives (−2,1,3). Applying the second to these updated coordinates gives (−2,−3,1), A. B interchanges axes differently, C loses the required signs, and D reverses the second rotation's signs.

**Common misconception:** Applying both transformations to the original coordinates rather than composing them.

## Q9

**Correct answer:** D

The qualification explicitly denies inferring impossibility from zero observed failures. D asserts exactly that inference and conflicts. A restates the observation; B and C acknowledge untested possibilities and future revision. Empirical absence is not a universal logical proof.

## Q10

**Correct answer:** 1488

Concept: circular permutations and inclusion–exclusion. Total circular arrangements are 7!=5040. For a specified set of k adjacent couples, contract each into one block, giving 2ᵏ(7−k)! circular arrangements. Apply inclusion–exclusion over the four couples:

5040−C(4,1)·2·6!+C(4,2)·4·5!−C(4,3)·8·4!+16·3!
=5040−5760+2880−768+96=1488.

Each contracted couple has two internal orders. Reflections remain distinct, so no additional division by two is allowed.

## Q11

**Correct answer:** 78

**Concept:** Inclusion–exclusion for forbidden fixed points.

Begin with 5!=120. Subtract 4!=24 for each of the forbidden events π(1)=1 and π(2)=2, then add 3!=6 for their intersection. The result is 120−24−24+6=78.

**Common misconception:** Subtracting the overlap twice without restoring it.

## Q12

**Correct answer:** A, C, D

An odd number of bit flips toggles parity and is detected, proving A and D. An even number leaves total parity unchanged, disproving B. Flipping one data bit and the parity bit is an example of two undetected flips, proving C. Include the parity bit itself when counting errors.

## Q13

**Correct answer:** A

**Concept:** Digital Logic — Boolean algebra

1. If x=0, the original expression reduces to y. If x=1, it reduces to z.
2. A selects exactly these two cofactors. Equivalently, expansion gives xz + x'y + yz, and the consensus term yz is redundant.

- **A:** Its x=0 and x=1 cofactors are y and z.
- **B:** This swaps the selected cofactors; x=0,y=1,z=0 is a counterexample.
- **C:** For x=1,y=1,z=0 it gives 1, whereas F=0.
- **D:** For x=y=z=0 it agrees, but x=1,y=z=0 gives 1 while F=0.

**Common misconception:** The consensus term need not appear in a minimal equivalent expression.

## Q14

**Correct answer:** D
**Concept:** Generating function with initial conditions.

For F=Σa_nx^n, summing the recurrence for n≥2 gives F−x=3xF−2x²F. Thus F=x/(1−3x+2x²)=x/((1−x)(1−2x)). A has the wrong constant coefficient; B has the wrong recurrence sign; C also has nonzero constant coefficient.

**Common misconception:** A recurrence denominator alone does not determine a generating function; initial conditions determine its numerator.

## Q15

**Correct answer:** 0

Unlink removes the final directory reference, but an open reference remains. The stated reclamation condition is therefore false and none of the eight blocks is freed yet. Namespace removal and storage reclamation can occur at different times.

## Q16

**Correct answer:** B, C

A blocking operation can suspend the caller, making the core available to another runnable process; B and C hold. The caller need not busy-wait, so A is false. An empty pipe with a writer still open may later receive data; emptiness alone does not establish EOF, refuting D.

## Q17

**Correct answer:** C

Negating the universal yields an existential counterexample x. The implication fails when P(x) holds and its consequent ∃yR(x,y) fails; the latter negates to ∀y¬R(x,y). This is C. A retains a universal x; B negates the antecedent incorrectly; D requires only one failed witness instead of absence of every witness.

## Q18

**Correct answer:** A, B

The wait-for edges T1→T2 and T2→T1 form a cycle, so A is true. Aborting either and releasing its locks breaks the cycle, proving B. Two-phase locking ensures a serializability property, not deadlock freedom, so C is false. Simultaneous commit is neither possible while blocked nor necessary for recovery, making D false.

## Q19

**Correct answer:** B
**Concept:** Priority aging.

Waiting gradually improves a job's urgency, counteracting indefinite postponement by newly arriving high-priority jobs. This is B. It does not change mutex acquisition order (A), page allocation (C), or cache/DMA coherence (D).

**Common misconception:** Scheduling starvation and resource deadlock require different remedies.

## Q20

**Correct answer:** B
**Concept:** An epsilon production selected by FOLLOW.

b belongs to FOLLOW(A), since S→Ab. With lookahead b, the predictive table selects A→ε: remove A from the stack and do not advance input. B is correct. A consumes a token too early; C requires lookahead a; D ignores the epsilon/FOLLOW rule.

**Common misconception:** A table entry for an epsilon alternative is determined by FOLLOW, not by a literal input epsilon.

## Q21

**Correct answer:** 10
**Concept:** Tree degree sum.

Let l be the leaf count. There are l+13 vertices and l+12 edges. Summing degrees gives l+8×3+5×2=2(l+12), so l+34=2l+24 and l=10.

**Common misconception:** Degree-two vertices add edges and vertices without changing the leaf count implied by branching vertices.

## Q22

**Correct answer:** 3

The assignments fill B[2]=0, B[0]=1, B[4]=2, B[1]=3, and B[3]=4. Thus B=[1,3,0,4,2] is the inverse permutation. The nested lookup gives B[B[0]]=B[1]=3. The two arrays are distinct, so constructing the inverse does not overwrite A. Applying the inverse twice is different from composing A with its inverse.

## Q23

**Correct answer:** A

Concept: asynchronous I/O notification. Completion can raise an interrupt for the CPU (A). B destroys processor state; C corrupts addressing; D prevents useful transfer activity. None is a completion-notification mechanism. DMA transfers data independently but can still notify software when done.

## Q24

**Correct answer:** A
**Concept:** Continuity and matching one-sided derivatives.

Near zero, eˣ=1+x+x²/2+O(x³), so the left branch is 1+x/2+O(x²). Continuity requires a=1, and matching derivatives requires b=1/2. B and D fail continuity; C preserves continuity but has right derivative 1 instead of 1/2.

**Common misconception:** Matching function limits ensures continuity, not differentiability.

## Q25

**Correct answer:** A, C, D
**Concept:** Reachability and residual-language equivalence.

The strings ε,a,b,ab reach p,q,r,s, respectively, proving A. From either p or q, acceptance occurs exactly when a future suffix contains b; they are equivalent, so B is false. r and s accept every suffix and are equivalent (C). Before the first b the machine alternates between p and q; after a b it stays in an accepting sink, proving D.

**Common misconception:** Distinct reachable states need not remain distinct after minimization.

## Q26

**Correct answer:** 2

A's next field and C's prev field must each change, giving two surviving-node pointer updates. Fields inside the removed node are not included in the question's count.

## Q27

**Correct answer:** A, C

Concept: amortized geometric copying. Copies occur at sizes 1,2,4,... below n. Their sum is less than 2n, so A holds and B fails. An append at a full capacity proportional to n copies Θ(n) elements, making C true and D false. Amortized constant time does not mean worst-case constant time per operation.

## Q28

**Correct answer:** A

A younger result waits in the reorder buffer until all preceding instructions can commit, allowing precise architectural state at an older exception(A). Early issue and additional execution units(B,C) affect execution timing but do not enforce visibility ordering. Branch-direction prediction(D) does not establish exception ordering.

## Q29

**Correct answer:** B
**Concept:** Language of a left-recursive grammar.

Each recursive step appends either a or b to the right of the remaining A, and the terminating production replaces A by c. The result is c followed by any string over {a,b}, namely B. A,C place c at the wrong end; D unnecessarily forces alternating pairs.

**Common misconception:** Left recursion describes a derivation mechanism, not the position of the terminal base symbol in the final word.

## Q30

**Correct answer:** 988

The eight-bit signed displacement11111100 represents−4. Scaling gives−16 bytes; the PC base is1000+4=1004. The target is1004−16=988. Both sign extension and the specified next-instruction PC convention affect the answer.

## Q31

**Correct answer:** 1

Greedy chooses4,1,1, using three coins. An optimum is3,3, using two; one coin cannot make6. The difference is1. A denomination system need not support the greedy-choice property.

## Q32

**Correct answer:** A

The first p symbols are all a, so every permitted nonempty v consists solely of a's. Pumping down reduces only their count and leaves all p b's, proving A. B contradicts this location; C reverses the universal quantification required to refute the lemma; D violates |v|≥1. One convenient split is insufficient: the argument must cover all legal splits.

## Q33

**Correct answer:** A, C

The rule gives (Project,Role)→Employee. Neither project nor role alone determines an assignment under the given constraints, so their pair is a candidate key (A). C describes a direct violation of that dependency. B fails because one employee can hold multiple roles on a project. D discards which roles the employee fills and therefore loses information. A ternary key constrains a combination of two participating entities, not either participant separately.

## Q34

**Correct answer:** A

**Concept:** Digital Logic — Karnaugh maps

1. The required ones and don't-cares together are exactly the eight inputs with B=0.
2. Assign those don't-cares to 1 and group all eight cells. This yields NOT B with one literal.
3. A zero-literal constant is impossible because both required zeros and required ones exist.

- **A:** It covers all required ones and no required zero with one literal.
- **B:** It misses every required one, each of which has D=1.
- **C:** For A=B=1,C=0,D=0 it produces a forbidden 1.
- **D:** It is valid but has two literals, so it is not minimum-literal.

**Common misconception:** A valid implementation may still be nonminimal when don't-cares are available.

## Q35

**Correct answer:** 0.25

Conditional on any allowed choice2,3 or4 by A, independent B matches that choice with probability1/4. Averaging the same probability over those three choices leaves1/4. Restricting A's choices does not restrict B's independent choices.

## Q36

**Correct answer:** 1

Rear advances for six successful enqueues in total, ending at6 modulo5=1. Front advances twice to2; the queue then holds four elements, the maximum allowed with one reserved slot. Dequeues do not move rear.

## Q37

**Correct answer:** A, C

EOF requires no write descriptors remain open and all buffered bytes are consumed. The child itself retains an open write end, so it can block after reading the message, proving A and refuting B. Closing that unused end removes the obstacle; after the parent's close and buffer drain, EOF can occur, proving C. Waiting does not close another process's descriptors, refuting D. The parent's wait can therefore participate in a hang caused by inherited descriptor ownership.

## Q38

**Correct answer:** D

Concept: signed comparison after overflow. A represents −128 and B represents one. Exact difference −129 wraps to 127=0x7F, giving N=0 and V=1. Signed less-than is N XOR V=1. Thus D. A wrongly uses the unrepresentable exact difference's sign as the stored sign; B misses overflow; C gives the wrong stored sign and comparison. A subtraction's sign alone is insufficient when it overflows.

## Q39

**Correct answer:** A, C
**Concept:** Pumping-lemma quantifiers.

The first p symbols are all a, and y is a nonempty part of that prefix, proving A. Pumping down removes positive a count while leaving p b symbols, so the result is outside L (C). Pumping twice also unbalances counts, refuting B. D violates the lemma's required decomposition constraints.

**Common misconception:** A contradiction must work for every allowed decomposition of the selected witness.

## Q40

**Correct answer:** A, C

**Concept:** Ancestor bounds during BST search.

After 50,20,40, the next node must lie strictly between 40 and 50, so 48 is possible (A). After 20 the upper bound 50 still applies, excluding 55 (B false). After 47 the interval becomes (40,47), proving C. Successive left and right choices are allowed when all ancestor bounds remain satisfied, so D is false.

**Common misconception:** Checking only the immediately previous comparison and forgetting older bounds.

## Q41

**Correct answer:** C

**Concept:** Mux selection and dependency.

Select 00 gives constant zero and select 11 constant one, both independent of x. Select 01 gives x and 10 gives its complement, both dependent. C lists exactly the correct settings. A and B omit one; D lists the dependent settings.

**Common misconception:** Treating inversion of an input as independence from that input.

## Q42

**Correct answer:** A, C, D

E[X]=0, E[Y]=2/3, and E[XY]=E[X³]=0, so covariance is0, proving A and C. Y=0 forces X=0, proving D and disproving independence B: P(X=0,Y=0)=1/3 differs from(1/3)(1/3). Zero covariance does not imply independence.

## Q43

**Correct answer:** 4

**Concept:** Comparing multi-hop routes.

A–B–C–D costs 1+2+1=4. The alternatives A–C–D and A–B–D cost five and six; positive-weight extra detours cannot improve them. The shortest distance is four.

**Common misconception:** Choosing the route with fewer hops rather than lower total weight.

## Q44

**Correct answer:** 6

On MTU620 the maximum aligned payload is600, so the original payload becomes three600-byte fragments. On MTU420 the maximum aligned payload is400. Each existing600-byte fragment splits into400 and200 bytes; both are multiples of8, so the original-fragment more-fragments status is consistent even for a final piece of a nonfinal original fragment. Six fragments reach the destination. Recombining payload across first-hop fragment boundaries to obtain five fragments is not allowed without reassembly.

## Q45

**Correct answer:** 13

**Concept:** Encoded control fields with idle choices.

The groups need 6,4 and 10 distinct encodings after including “none”. Their widths are ceil(log₂6)=3, log₂4=2 and ceil(log₂10)=4. Add the four independent bits: 3+2+4+4=13.

**Common misconception:** Omitting the “none” code or encoding independent signals as mutually exclusive.

## Q46

**Correct answer:** A, B, D
**Concept:** Products of rank-one projections.

Since uᵀu=vᵀv=2 and uᵀv=1, PQ=uvᵀ/4. This is a nonzero outer product and has rank one (A). Its trace is vᵀu/4=1/4 (B). Its (1,2) entry is zero while its (2,1) entry is 1/4, refuting symmetry (C). The vector u is an eigenvector with eigenvalue 1/4; the two-dimensional kernel vᵀx=0 supplies two zero eigenvalues, proving D.

**Common misconception:** Two symmetric matrices need not have a symmetric product unless they commute.

## Q47

**Correct answer:** 12

The root's three distinct child subtrees can be ordered in3!=6 ways. Vertex a's two leaves can be ordered in2!=2 ways. Vertex b has only one child, contributing one choice. Distinct labels make these choices give distinct preorder strings, so6×2=12. Permutations within a subtree cannot interleave its preorder block with another subtree.

## Q48

**Correct answer:** A, C, D

**Concept:** Algorithms — Dynamic programming

In a downward scan, j−wi<j has not yet been updated for the current item. Thus the right-hand side combines the previous-item optimum with at most one copy of the new item, preserving the 0/1 recurrence. This proves A and D. In an upward scan, the lower entry may already contain this item: for the single item (2,3), update D[2]=3 and then D[4]=D[2]+3=6, although the true 0/1 optimum is 3. Hence C is true and B is false. The descending order is a dependency discipline that allows two DP rows to share storage.

- **A:** True: descending capacity order preserves the previous-row dependency for every item.
- **B:** False: upward order can reuse the current item repeatedly.
- **C:** True: the update at capacity 4 reads the newly changed D[2]=3.
- **D:** True: positive weight makes j−wi smaller than j, so the downward scan has not visited it yet.

**Common misconception:** A correct recurrence can become a different optimization problem when in-place update order changes.

## Q49

**Correct answer:** B

**Concept:** Precision limits of an abstract domain.

At the merge, x can be 2 or 3 and is not a known constant, so A is false. A constant-only evaluator may treat both operands as unknown and fail to retain their equality, whereas algebra proves x−x=0. B captures that distinction. Each execution uses the same x twice, so C is impossible; unknown p does not invalidate the identity, refuting D.

**Common misconception:** Treating separate occurrences of the same variable as independently chosen values.

## Q50

**Correct answer:** B

**Concept:** Mutual exclusion versus progress.

Both can set their flag before either checks the other's flag, leaving both spinning forever. Progress therefore fails. Mutual exclusion still holds: a thread entering has its own flag true, preventing the other from passing its test until that flag is cleared after the critical section. B captures both facts. A overlooks the preceding writes, C overlooks the deadlocking interleaving, and D invents a turn variable.

**Common misconception:** Treating absence of simultaneous entry as a complete synchronization proof.

## Q51

**Correct answer:** 3

A has eigenvalues1 and2, with eigenvectors(1,1)ᵀ and(1,2)ᵀ. Write v=α(1,1)ᵀ+β(1,2)ᵀ. Then A^n v=α(1,1)ᵀ+2^nβ(1,2)ᵀ. Boundedness forces β=0, and x+y=2α=6 gives α=3, so x=3. A component along the expanding eigenvector cannot remain bounded.

## Q52

**Correct answer:** C

**Concept:** Digital Logic — Sequential circuits

Using only old-state values, the sequence is 00 → 01 → 11 → 00, a period-three cycle. Thus the state after t edges depends on t modulo 3. Since 2027 = 3×675+2, the state is 11. The unused state 10 maps to 10, but is unreachable from the specified initial state.

- **A:** False: 00 occurs only at edge counts divisible by 3.
- **B:** False: 01 occurs when the edge count is 1 modulo 3.
- **C:** True: 2027 is 2 modulo 3, giving 11.
- **D:** False: 10 is a separate fixed point and is never reached from 00.

**Common misconception:** Flip-flops update simultaneously; substituting an already updated bit gives a wrong transition graph.

## Q53

**Correct answer:** B

Concept: BST deletion and successor. The original root's successor is 45, the leftmost node in its right subtree. Copy 45 to the root and replace node 45's original link from 50 by its child 47. Thus 47's parent is 50. With no right subtree, its next inorder node is its ancestor 50. B gives (50,50). A and D leave the old parent relation; C and D skip the closer successor 50. Copying the successor key does not move its entire subtree to the root.

## Q54

**Correct answer:** A, B, C

N behaves identically on every input. It accepts every string if the embedded simulation accepts, and no strings otherwise, proving A,B. An emptiness decider could therefore distinguish arbitrary acceptance by negating its result, proving C. Producing N requires only embedding the simulation instructions, not resolving their outcome, so D is false.

## Q55

**Correct answer:** 3

**Concept:** Suffix-tracking DFA minimality.

Track three cases: no relevant suffix, suffix 0, and suffix 01 (accepting). These suffice with ordinary suffix updates. They are distinguishable: the accepting state differs from either other state on ε; states reached by ε and 0 differ on suffix 1. Thus three is both an upper and lower bound.

**Common misconception:** Adding a dead state although every prefix can still be extended to end in 01.

## Q56

**Correct answer:** B

With S empty, the implication in Q is true for every y, so every candidate qualifies. The conjunction in P is false for every y; the infinite domain is nonempty, so its universal statement is false and no candidate qualifies. Thus B; A,C,D each mis-handle one quantifier. Logical implication restricts the required witnesses; conjunction does not implement relational division.

## Q57

**Correct answer:** A, C, D

Concept: mean value theorem and continuity of f′. On [0,1/2] the secant slope is 2/(1/2)=4, proving A. On [1/2,1] it is (1−2)/(1/2)=−2, proving C and disproving B. The derivative is continuous and takes both signs, so it equals zero between those two interior points, proving D. The whole-interval secant slope alone would hide both the rise and the fall.

## Q58

**Correct answer:** D
**Concept:** Longest-prefix fallback after withdrawal.

160 lies in the withdrawn /17 but outside the surviving /18, so it falls back to the /16 via B. 200 remains inside the /18, so uses D. A skips valid more-specific routes; B retains the withdrawn route; C ignores the surviving /18.

**Common misconception:** Withdrawing a prefix does not withdraw its more-specific routes.

## Q59

**Correct answer:** A, C

After line2 there exists a path through line3 that uses x before redefining it, so may-liveness includes x and A is true. On the path beginning at line5, x is never used, making B false. Line6 uses y, so C is true. The existence of a path using line1's definition prevents deleting it as dead; D is false. May-liveness takes a union over possible successors, not an intersection.

## Q60

**Correct answer:** 16

Bits15–12 are fixed and bits7–0 must equal0x35. Four ignored bits11–8 can take any of16 patterns, yielding16 aliases. These do not represent additional device storage.

## Q61

**Correct answer:** 7

Concept: tournament certificates for second maximum. Only keys directly defeated by the overall winner can be second largest; every other key lost to another nonmaximum key. Here there are exactly two such candidates. One further comparison determines the larger, and in the worst case that comparison is necessary because their mutual order is not fixed by the separate winning subtrees. Total=6+1=7. The winner's path length, not just total input size, controls the final selection cost.

## Q62

**Correct answer:** B

Concept: DFS interval nesting. v's entire interval lies inside u's, so v is a descendant of u. An edge from ancestor to descendant that is not a tree edge is forward (B). A would point to an ancestor; C connects unrelated DFS subtrees and requires disjoint intervals; D denies ordinary descendant nesting. Edge direction is crucial.

## Q63

**Correct answer:** B

**Concept:** Longest-path dynamic programming in a DAG.

Initialize the source distance to zero and unreachable distances to negative infinity; process reachable edges in topological order. Every predecessor distance is final before a vertex is processed, so maximizing over incoming paths is correct regardless of negative weights. This proves B and refutes A. Path lengths in edges may differ (C false), and converting to an undirected graph destroys the acyclic dependency structure (D false).

**Common misconception:** Transferring restrictions of greedy shortest-path algorithms to topological dynamic programming.

## Q64

**Correct answer:** A, B, D
**Concept:** SQL aggregate and NULL semantics.

A has COUNT(*)=3, COUNT(amount)=2 and SUM=30, satisfying both predicates. B has counts 2 and 0, but SUM is NULL and NULL>10 is UNKNOWN, so it is excluded. C has equal counts and is excluded. Thus one row (A,30) remains: A,B true and C false. Replacing COUNT(amount) with COUNT(*) makes the strict inequality false in every group, proving D.

**Common misconception:** SUM of an all-NULL group is NULL, not zero, and HAVING retains only TRUE.

## Q65

**Correct answer:** 6

The distinct nonempty subsequences of nullable occurrences in ABA are ABA,AB,BA,AA,A,B. Retaining only the first A and retaining only the final A produce the same right-hand side A and are counted once. Thus6. There are eight omission patterns, but one is empty and two collapse to the same A.

