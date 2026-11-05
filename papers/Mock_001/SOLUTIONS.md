# Worked Solutions — Mock Test 001

Review provenance is recorded in the structured bank; no human review is claimed.

## Q1

**Correct answer:** A

**Concept:** General Aptitude — Verbal grammar

1. The relative clause “that were damaged” modifies the plural noun instruments.
2. The main clause has the singular subject Each, so its verb is has.
The complete sentence therefore uses were; has.

- **A:** Both agreements are correct.
- **B:** Both verbs have the wrong number.
- **C:** The main verb must agree with Each, not instruments.
- **D:** The relative-clause verb must agree with instruments.

**Common misconception:** A noun near a verb need not be that verb's grammatical subject.

## Q2

**Correct answer:** 35.71 (exact)

**Concept:** General Aptitude — Ratios and percentages

1. Normalize the initial number of orders to 100. There are 40 X and 60 Y orders.
2. Completed X orders = 40(0.75) = 30; completed Y orders = 60(0.90) = 54.
3. The required percentage is 100(30/84) = 250/7 = 35.714285..., which rounds to 35.71.

**Common misconception:** The denominator is completed orders, not original orders.

## Q3

**Correct answer:** 2 (exact)

**Concept:** General Aptitude — Deductive logic

1. The biconditional requires exactly one of C and D to be selected.
2. The other selected person must be A or B. Selecting A would also require B, producing three people, which is forbidden.
3. Hence the possible pairs are {B,C} and {B,D}: two pairs.

**Common misconception:** An implication does not require its antecedent to be true.

## Q4

**Correct answer:** A

**Concept:** General Aptitude — Spatial transformations

1. Reflection maps (x,y) to (x,-y).
2. Clockwise quarter-turn maps (u,v) to (v,-u). The combined map is (x,y) to (-y,-x).
3. Applying it separately to the labelled vertices gives (-1,-1), (-1,-3), (-2,-1).

- **A:** All three vertices obey (-y,-x).
- **B:** This is the combined map for a counterclockwise rotation after reflection.
- **C:** This applies clockwise rotation without the preceding reflection.
- **D:** This applies counterclockwise rotation without reflection.

**Common misconception:** Reflection and rotation must be composed in the stated order.

## Q5

**Correct answer:** B

**Concept:** General Aptitude — Reading comprehension

1. The data establish increased evening visits and unchanged daily totals.
2. A shift in visit timing is compatible with those observations, but individual histories were not recorded.
3. Therefore the cautious possibility in B is supported; definitive claims about individual visitors are not.

- **A:** New visitors could have been offset by losses elsewhere.
- **B:** A timing shift is possible and fits both reported totals.
- **C:** No individual histories establish this universal claim.
- **D:** The passage explicitly says daily totals were unchanged.

**Common misconception:** Aggregate counts do not identify the behaviour of each individual.

## Q6

**Correct answer:** A

**Concept:** General Aptitude — Permutations and combinations

1. With A and B adjacent, treat them as a block with two orders. There are 2(5!)=240 circular arrangements.
2. If C and D are also adjacent, there are 4(4!)=96 arrangements. The same count applies when E and F are adjacent.
3. When both forbidden adjacencies occur, three two-person blocks and G form four circular units. There are 2^3(3!)=48 arrangements.
4. Inclusion-exclusion gives 240-96-96+48=96.

- **A:** This subtracts both forbidden events and restores their intersection.
- **B:** This is 5!: it fixes the A-B order and ignores both forbidden adjacencies.
- **C:** This enforces only one of the two forbidden adjacencies: 240-96.
- **D:** This ignores both forbidden adjacencies.

**Common misconception:** Circular blocks reduce the number of rotationally distinct units before factorial counting.

## Q7

**Correct answer:** A

**Concept:** General Aptitude — Data interpretation

1. Month 1 productivity is (400+900)/(40+60) = 13 items/hour.
2. Month 2 productivity is (660+640)/(60+40) = 13 items/hour.
3. The percentage change is zero, even though each team's own rate improved. More hours were allocated to the slower team.

- **A:** Both aggregate rates are 13.
- **B:** A simple or weighted average of team percentage gains cannot replace aggregation with the new hour mix.
- **C:** This is only A's rate improvement.
- **D:** Neither the total output nor the total hours implies this increase.

**Common misconception:** A changed mixture can offset improvements in every component rate.

## Q8

**Correct answer:** 2 (exact)

**Concept:** General Aptitude — Paper folding and cutting

1. Unfolding a point (x,y) produces (x,y), (8-x,y), (x,8-y), (8-x,8-y).
2. The first punch produces (5,6),(3,6),(5,2),(3,2). Only (5,6) lies on y=x+1.
3. The second produces (6,5),(2,5),(6,3),(2,3). Only (2,3) lies on that line. The sets are disjoint, so the answer is 2.

**Common misconception:** Both folds must be reversed; points from different punches need not lie on the same symmetry line.

## Q9

**Correct answer:** C

**Concept:** General Aptitude — Narrative sequencing

1. Calibration precedes the first trial: Q precedes R.
2. “This divergence” in S refers to R, and the successful repeat trial is the basis of P: R precedes S precedes P.
3. T follows receipt of the final report: P precedes T. Combining the constraints gives Q-R-S-P-T.

- **A:** P cannot precede the repeat trial on which it is based.
- **B:** Q explicitly precedes the first trial described in R.
- **C:** This satisfies all four precedence links.
- **D:** S cannot precede the divergence, and T cannot precede the report.

**Common misconception:** A grammatically plausible adjacent pair can still violate the account's causal order.

## Q10

**Correct answer:** B

**Concept:** General Aptitude — Elementary probability and statistics

1. In Bag I, P(RR)=6/15 and P(same)=7/15. In Bag II, P(RR)=1/10 and P(same)=4/10.
2. Before conditioning, P(RR)=(1/2)(6/15+1/10)=1/4, and P(same)=(1/2)(7/15+4/10)=13/30.
3. Since RR is a subset of same, P(RR | same)=(1/4)/(13/30)=15/26.

- **A:** Conditioning on same does not leave red and blue equally likely.
- **B:** The ratio of the mixture probabilities is 15/26.
- **C:** This is not the ratio P(RR)/P(same).
- **D:** Conditioning cannot be replaced by the initial proportion in a bag.

**Common misconception:** Conditional probabilities from different bags cannot be averaged without updating their weights.

## Q11

**Correct answer:** A

**Concept:** Digital Logic — Boolean algebra

1. If x=0, the original expression reduces to y. If x=1, it reduces to z.
2. A selects exactly these two cofactors. Equivalently, expansion gives xz + x'y + yz, and the consensus term yz is redundant.

- **A:** Its x=0 and x=1 cofactors are y and z.
- **B:** This swaps the selected cofactors; x=0,y=1,z=0 is a counterexample.
- **C:** For x=1,y=1,z=0 it gives 1, whereas F=0.
- **D:** For x=y=z=0 it agrees, but x=1,y=z=0 gives 1 while F=0.

**Common misconception:** The consensus term need not appear in a minimal equivalent expression.

## Q12

**Correct answer:** 2 (exact)

**Concept:** Operating Systems — System calls

1. dup creates a second descriptor referring to the same open-file description, so the offset is shared.
2. The two reads move the offset to 2 and then 5.
3. The absolute seek resets it to 1. The final one-byte read moves it to 2.

**Common misconception:** Duplicated descriptors share an offset; reopening the path would create an independent offset.

## Q13

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

## Q14

**Correct answer:** A

**Concept:** Engineering Mathematics — Propositional and predicate logic

1. Negating the outer quantifiers changes forall x exists y into exists x forall y.
2. Negating the conjunction gives NOT R(x,y) OR NOT forall z (R(x,z) -> z=y).
3. The inner negation is exists z [R(x,z) AND z!=y]. Substitution gives A. The original formula says each x has exactly one R-successor; its negation allows an x with none or more than one.

- **A:** It follows all three quantifier and connective changes.
- **B:** For a two-element identity relation the original is true, but this option is also true by choosing x!=y.
- **C:** For a singleton empty relation the original is false, but this conjunction is false.
- **D:** For a universal relation on two elements the original is false; this option is false because z=y defeats its universal conjunct.

**Common misconception:** Negating unique existence requires accounting for both zero and multiple witnesses.

## Q15

**Correct answer:** 120 (exact)

**Concept:** Computer Organization and Architecture — Instruction sets and addressing modes

1. The displacement is -6, not 250. The post-instruction PC is 104.
2. The intermediate address is 104+4(-6)=80.
3. Indirection reads M[80]=120, so the operand address is 120. M[120]=7 is the value loaded, not the address asked for.

**Common misconception:** PC base, scale, indirection and loaded value are distinct stages.

## Q16

**Correct answer:** D

**Concept:** Computer Organization and Architecture — ALU design

1. With s=1, invert B to 0101 and add 1: 0111+0101+1=1101, with no fifth bit. Thus C=0.
2. Signed interpretation gives 7-(-6)=13, outside [-8,7], so V=1 even though the unsigned carry-out is zero.

- **A:** Carry-out is zero and signed overflow is present.
- **B:** It gets result and carry right but misses signed overflow.
- **C:** The stated bit addition does not yield 0011.
- **D:** Both the bit arithmetic and signed range test agree.

**Common misconception:** Carry-out and signed overflow are different conditions.

## Q17

**Correct answer:** 3 (exact)

**Concept:** Databases — ER model

1. Project is identified by (dept_id, project_code), because project_code alone may repeat.
2. Task adds its own partial key, giving (dept_id, project_code, task_no).
3. Dropping any attribute can merge allowed distinct tasks, so all three are necessary.

**Common misconception:** A weak owner can itself have a composite identifying key.

## Q18

**Correct answer:** B

**Concept:** Compiler Design — Lexical analysis

1. The longest identifier prefix is ifx; a keyword prefix does not split it.
2. Maximal munch chooses == rather than two = operators.
3. The next identifier is exactly if, followed by ++ and +, because +++ is not a token. The final token is x.

- **A:** A keyword prefix cannot split the longer valid identifier ifx.
- **B:** Every boundary follows maximal munch.
- **C:** It splits == and fails to take ++ at the first plus.
- **D:** +++ is not among the recognized operators.

**Common misconception:** Token priority breaks equal-length ties; it does not override longest match.

## Q19

**Correct answer:** A, C

**Concept:** Computer Networks — Layering

1. Ordinary routing keeps the end-to-end IPv4 destination and TCP port unchanged.
2. Forwarding decrements TTL and constructs an Ethernet frame for the outgoing LAN's next hop.
3. Therefore A and C hold; the incoming and outgoing link-layer destinations need not match.

- **A:** No address translation occurs.
- **B:** The outgoing frame addresses the next hop on a different LAN, not necessarily the incoming destination MAC.
- **C:** The stated assumptions ensure ordinary forwarding with a one-hop decrement.
- **D:** TCP ports identify endpoints; a transit router does not replace them.

**Common misconception:** Link-layer next-hop addressing must be distinguished from end-to-end addressing.

## Q20

**Correct answer:** 3 (exact)

**Concept:** Algorithms — Searching and sorting

1. Strictly unequal inversions cause the same shifts in both versions: 3a past 1 and 2, and 3b past 2.
2. Only the modified version also shifts equal preceding records: one when inserting 3b and two when inserting 3c.
3. The additional count is 1+2=3; totals are 3 and 6 respectively.

**Common misconception:** Equality in the comparison changes stability and adds one shift per equal-key pair.

## Q21

**Correct answer:** A, B, D

**Concept:** Databases — Relational algebra

1. The product creates every candidate A paired with every required B. Subtracting R identifies a missing required pair; its A is excluded.
2. Originally only A=2 misses y, leaving 1. With empty S there are no missing pairs, so all candidate A values remain.
3. Adding (2,y) makes both candidates qualify. Adding z to S makes both fail because neither has a z pair.

- **A:** Only 1 is paired with every B in S.
- **B:** Universal coverage of an empty required set is vacuously true.
- **C:** The result becomes {(1),(2)}, not {(1)}.
- **D:** Both candidates lack z.

**Common misconception:** Division-like expressions include vacuous truth and candidate-domain restrictions.

## Q22

**Correct answer:** 2 (exact)

**Concept:** Compiler Design — Parsing

1. FIRST(B)={b,epsilon} and FIRST(A)={a,b,epsilon}. FOLLOW(A)={a}, propagated to FOLLOW(B)={a}. FOLLOW(S)={$}.
2. S -> A a enters columns a and b, while S -> b enters b. Thus M[S,b] conflicts. A -> a A enters a; A -> B enters b and, because B is nullable, FOLLOW(A)'s a. Thus M[A,a] conflicts.
3. B -> b B enters b; B -> epsilon enters a. These do not conflict. Exactly two table cells conflict.

**Common misconception:** Nullable productions can create conflicts through FOLLOW, separately from overlapping FIRST sets.

## Q23

**Correct answer:** 2 (exact)

**Concept:** Engineering Mathematics — Matrices determinants and linear systems

1. Subtract row 1 from rows 2 and 3. The determinant becomes (t-1)^2-1=t(t-2).
2. A real homogeneous square system has infinitely many solutions precisely when it is singular.
3. The distinct singular values are t=0 and t=2, whose sum is 2.

**Common misconception:** A homogeneous singular system is always consistent and has a nontrivial null space.

## Q24

**Correct answer:** C

**Concept:** Engineering Mathematics — Limits continuity and differentiability

1. Set r=|x|. Then f(x)=2 for r<=1 and f(x)=2r for r>1; equivalently f(x)=2 max(1,r).
2. When r<=1, the outer argument is -1 and g=2. When 1<r<=2, the outer argument 2r-3 lies in (-1,1], so g remains 2. When r>2, that argument exceeds 1 and g=4r-6.
3. Thus g is constant on [-2,2], linear with slope -4 on x<-2 and slope 4 on x>2. Only -2 and 2 have unequal one-sided derivatives. The original corners at +/-1 disappear under the composition.

- **A:** The outer function is constant across the relevant images around +/-1, so g has no corners there.
- **B:** This retains the original f corners incorrectly; g is constant around +/-1.
- **C:** At each of +/-2, the slope changes between zero and a nonzero value.
- **D:** The slopes on the two sides of +/-2 differ.

**Common misconception:** A composition can remove a corner of the inner function; the chain rule cannot simply be applied at nondifferentiable points.

## Q25

**Correct answer:** 2 (exact)

**Concept:** Engineering Mathematics — Random variables and distributions

1. P(X=0)=exp(-lambda) and P(X=1)=lambda exp(-lambda), so lambda=1.
2. A Poisson variable has variance lambda and mean lambda. Thus E[X^2]=Var(X)+(E[X])^2=lambda+lambda^2=2.

**Common misconception:** The second moment is not the variance alone.

## Q26

**Correct answer:** 2 (exact)

**Concept:** Digital Logic — Tabular minimization

1. No four-cell cube avoids both zero minterms 3 and 4. The prime implicants therefore cover the six adjacent pairs (0,1),(0,2),(1,5),(2,6),(5,7),(6,7).
2. Each covers two minterms, so at least three are necessary. These pairs form a cycle on six vertices: 0-1-5-7-6-2-0.
3. A three-edge cover of six vertices must be a perfect matching. The cycle has exactly two alternating perfect matchings, giving two minimum covers.

**Common misconception:** Finding the minimum number of terms is different from counting all minimum covers.

## Q27

**Correct answer:** B

**Concept:** Programming and Data Structures — C programming and pointers

1. p points to the first row, and q points to the start of row 1. The addition changes a[0][2] from 6 to 9.
2. r initially points to a[0][1]. Because postfix ++ binds before unary *, *r++ stores q[0]=1 at that element, then advances r to a[0][2].
3. q[2]=*r sets a[1][2]=9. The printed sum is 1+9=10. All pointer arithmetic stays inside its row array, and side effects are sequenced across statements.

- **A:** This misses the earlier update of a[0][2].
- **B:** The final values are 1 and 9.
- **C:** This retains the old value 4 in a[0][1].
- **D:** No access is out of bounds and no scalar has unsequenced conflicting accesses.

**Common misconception:** Post-increment advances the pointer, not the pointed-to value.

## Q28

**Correct answer:** A, C

**Concept:** Algorithms — Hashing

1. Key 10 occupies slot 3. Key 17 probes 3 then 6; key 24 probes 3 then 1. Deleting 10 leaves a tombstone at 3.
2. Search for 24 visits 3 and then 1; stopping at 3 would miss it.
3. Tombstones are reusable on insertion. Key 31 starts at 3, so that slot is a possible insertion location after confirming absence. Capacity is not permanently lost.

- **A:** Its probe sequence reaches slot 1 only after slot 3.
- **B:** A never-used marker would incorrectly terminate search for 24.
- **C:** Tombstones retain search chains while remaining available for reuse.
- **D:** The tombstone may hold a later key, restoring all seven slots as potential capacity.

**Common misconception:** A tombstone is neither an occupied record nor an ordinary empty stopping point.

## Q29

**Correct answer:** A

**Concept:** Operating Systems — Processes and threads

1. At i=0, the first child breaks and prints 0; only the parent increments and continues.
2. The continuing parent similarly creates children that print 1 and 2.
3. The original parent increments to 3 and exits the loop. Thus exactly four values, 0,1,2,3, are printed.

- **A:** One child stops in each iteration and the original parent finishes.
- **B:** Children break; they do not take part in later forks.
- **C:** A child preserves its copied value of i when it breaks.
- **D:** Later children inherit i=1 and i=2, not the initial value.

**Common misconception:** A fork inside a loop is not automatically exponential when children stop iterating.

## Q30

**Correct answer:** 3 (exact)

**Concept:** Theory of Computation — Regular expressions and finite automata

1. Track E0: even b count but not currently accepting; E1: even b count and last symbol a; O: odd b count. In O the last symbol does not affect future acceptance, so one state suffices.
2. Transitions are E0 --a--> E1, E1 --a--> E1, both E states --b--> O; O --a--> O and O --b--> E0. E0 is initial and E1 alone accepts.
3. E1 is distinguished from the others by the empty suffix; E0 and O are distinguished by suffix a. All three are reachable, proving minimality.

**Common misconception:** The naive product construction can contain equivalent states.

## Q31

**Correct answer:** 3 (exact)

**Concept:** Computer Networks — Switching and performance

1. Transmission times per link are 0.5, 1 and 0.5 ms. Packet 1 finishes the links at 0.5,1.5,2 ms.
2. Packet 2 finishes link 1 at 1 ms but waits until 1.5 ms for link 2. It finishes link 2 at 2.5 ms.
3. Link 3 is free by then, so its final transmission ends at 3 ms.

**Common misconception:** Pipeline overlap does not remove serialization at the slowest link.

## Q32

**Correct answer:** D

**Concept:** Theory of Computation — Context-free grammars

1. A base tree uses S -> aSb with the inner S -> epsilon.
2. Replace the root with S -> SS, placing the previous tree on one child and S -> epsilon on the other. The yield remains ab.
3. Repeating this operation creates arbitrarily large finite trees with the same yield, so their count is infinite.

- **A:** The base tree is not unique; an empty sibling adds a second shape.
- **B:** The construction can be repeated after two trees have been obtained.
- **C:** There is no finite size bound on added empty siblings.
- **D:** The unbounded family consists of distinct finite trees.

**Common misconception:** A fixed finite string can have infinitely many parse trees in an epsilon-generating recursive grammar.

## Q33

**Correct answer:** A

**Concept:** Programming and Data Structures — Recursion

1. Induction gives f(n)=n: the even case restores 2(n/2), and the odd case restores 2 floor(n/2)+1.
2. The call chain is 45,22,11,5,2,1, which contains six active calls at its deepest point.

- **A:** Both the induction and explicit chain give this pair.
- **B:** It counts five recursive edges instead of six calls.
- **C:** The odd branches preserve the discarded low-order bits.
- **D:** The branches do not append 1 at even n.

**Common misconception:** Recursion depth counts frames, which is one greater than the number of recursive edges.

## Q34

**Correct answer:** A, D

**Concept:** Theory of Computation — Pushdown automata

1. The separator deterministically identifies the midpoint. Push each pre-separator bit, then match each later bit to the stack top and pop; accept only after the input ends with the data stack empty.
2. LIFO order compares against reverse(w), not w in its original order.
3. Choosing w=epsilon gives #, which is accepted with an empty data stack.

- **A:** The separator removes the need to guess when to switch phases.
- **B:** Remaining symbols mean the second half was too short.
- **C:** For w=01, input 01#01 fails this test, while 01#10 passes it.
- **D:** The definition allows the empty string for w.

**Common misconception:** A stack reverses order; the separator solves midpoint detection, not copying in forward order.

## Q35

**Correct answer:** 6 (exact)

**Concept:** Engineering Mathematics — Sets relations and functions

1. Idempotence implies every value in the image is fixed: if y=f(x), then f(y)=y.
2. Choose the two fixed elements in 3 ways. The remaining element must map to one of them, in 2 ways.
3. Each of these 3*2=6 functions satisfies idempotence and has exactly two fixed points.

**Common misconception:** The nonfixed element cannot map to itself or to another nonfixed image under idempotence.

## Q36

**Correct answer:** 448 (exact)

**Concept:** Algorithms — Asymptotic time and space complexity

At a fixed width w, the base loop has n/(2w) iterations because w is a power of two smaller than n. Each iteration calls touch w times, so each width contributes n/2 = 64 calls. The widths are 1, 2, 4, 8, 16, 32, 64: seven levels. Hence the exact count is 64 × 7 = 448. The work is Θ(n log n), even though individual inner-loop lengths vary.

**Common misconception:** Multiplying the largest bounds of all loops ignores the inverse relationship between the number of blocks and block width.

## Q37

**Correct answer:** B

**Concept:** Theory of Computation — Regular and context-free languages

A deterministic pushdown automaton can push a stack symbol on a and pop one on b, rejecting underflow. Its finite control also remembers the preceding symbol and whether its current run has length one or two; it rejects a third repetition. It accepts at end of input exactly when the stack is empty. Thus L is deterministic context-free.

To show nonregularity, consider the prefixes u_n=(aab)^n for n≥0. For distinct m,n, append v_n=(abb)^n. The string u_n v_n has no triple repetition, never underflows, and has net stack change n−n=0, so it lies in L. But u_m v_n has net stack change m−n≠0, so it cannot lie in L. Hence infinitely many prefixes are pairwise distinguishable by suffixes, and no finite automaton recognizes L. In particular, banning long runs does not bound stack depth: repeated aab blocks keep increasing it.

- **A:** False: (aab)^n raises the stack height without creating aaa or bbb; suffixes distinguish infinitely many such prefixes.
- **B:** True: finite control checks the run restriction while the deterministic stack checks balanced legal operations; the suffix argument proves nonregularity.
- **C:** False: the explicit deterministic push/pop construction handles both restrictions without guessing.
- **D:** False: a pushdown stack together with finite control can impose both restrictions simultaneously.

**Common misconception:** Bounding consecutive pushes does not bound total nesting depth when pushes can be interspersed with fewer pops.

## Q38

**Correct answer:** 4 (exact)

**Concept:** Compiler Design — Syntax-directed translation

The postfix code is `a b + c d e * + *`. Stack depths after successive tokens are 1, 2, 1, 2, 3, 4, 3, 2, 1. The maximum is 4. Equivalently assign a leaf peak 1 and a binary node peak max(left.peak, 1 + right.peak): the left result must remain on the stack throughout evaluation of the right subtree.

**Common misconception:** Expression-tree height alone does not give stack depth without the operand evaluation order.

## Q39

**Correct answer:** A, B, D

**Concept:** Engineering Mathematics — Eigenvalues and eigenvectors

1. Bu=Au+u(v^T u)=2u-2u=0, so zero is an eigenvalue.
2. Choose a basis (u,w1,w4) in which Aw1=w1 and Aw4=4w4. Distinct eigenvalues ensure this is a basis. In this basis A is diag(2,1,4), and u v^T has nonzero entries only in its first row, whose first entry is -2.
3. Therefore B is upper triangular with diagonal (0,1,4). These distinct real eigenvalues make B diagonalizable, and exactly two are nonzero, so rank(B)=2.
4. Commutation need not hold. In this basis choose v^T=(-2,1,0). Then B has first row (0,1,0); AB has entry (1,2)=2, whereas BA has that entry 1. A and B do not commute.

- **A:** u is a nonzero vector in the null space of B.
- **B:** The three eigenvalues are 0,1,4, all distinct and real.
- **C:** The explicit choice A=diag(2,1,4), u=(1,0,0)^T, v=(-2,1,0)^T is a counterexample.
- **D:** Similarity to a diagonal matrix with exactly two nonzero entries gives rank two.

**Common misconception:** A rank-one change need not commute with the original matrix, even when its image is an eigenspace.

## Q40

**Correct answer:** 2 (exact)

**Concept:** Engineering Mathematics — Extrema and mean value theorem

1. f_a'(x)=4g(x), where g(x)=x^3-a*x+1. Two strict minima of this quartic require three distinct real roots of g, with alternating derivative signs -,+,-,+.
2. For a<=0, g is increasing and has only one root. For a>0 its turning points are at +/-sqrt(a/3). Its local maximum is 1+2(a/3)^(3/2)>0, and its local minimum is 1-2(a/3)^(3/2).
3. Three distinct roots exist exactly when 1-2(a/3)^(3/2)<0, equivalently a^3>27/4. The threshold is approximately 1.88988, so the smallest integer is 2. At equality a repeated stationary point does not give a second strict minimum.

**Common misconception:** Stationary points must be classified; a repeated derivative root need not be an extremum.

## Q41

**Correct answer:** A

**Concept:** Programming and Data Structures — Arrays

The first nested loop swaps each pair of entries on opposite sides of the main diagonal exactly once, so it transposes the matrix. The second nested loop reverses each row. The composition is a clockwise 90-degree rotation. Four iterations restore the original array, and 2027 has remainder 3 modulo 4, so the net transformation is a counterclockwise 90-degree rotation. Under that net transformation, new[r,c]=old[c,4−r]. Index 7 is (r,c)=(1,2), so its value is old[2,3]=5×2+3=13. Index 17 is (3,2), so its value is old[2,1]=11. Hence the program prints `13 11`. Every pointer is inside the single a array and every swap uses distinct entries.

- **A:** True: three clockwise quarter-turns map the queried positions to original positions (2,3) and (2,1).
- **B:** False: these are the values after one clockwise quarter-turn, not after 2027 iterations.
- **C:** False: these are the unchanged initial values; 2027 is not divisible by four.
- **D:** False: these are the values after two quarter-turns, not three.

**Common misconception:** The order of transpose and row reversal determines the rotation direction; repeated index permutations should be reduced by their period.

## Q42

**Correct answer:** A

**Concept:** Digital Logic — Combinational circuits

Fixing bc=00 leaves at most two ones, so I0=0. Fixing bc=01 or 10 supplies one one, so both a and d must be one: I1=I2=ad. Fixing bc=11 supplies two ones, so either a or d suffices: I3=a+d. This is Shannon decomposition with respect to the select variables.

- **A:** True: the four cofactors are 0, ad, ad, a+d.
- **B:** False: for bc=01, a=1,d=0 it outputs 1 with only two ones; for bc=11,a=1,d=0 it also misses a required 1.
- **C:** False: for bc=00,a=d=1 it outputs 1 despite only two ones; bc=11,a=d=0 is another false positive.
- **D:** False: bc=01,a=d=1 has three ones and must yield 1.

**Common misconception:** MUX data inputs are cofactors, not the select variables themselves.

## Q43

**Correct answer:** A

**Concept:** Compiler Design — Runtime environments

C is declared directly inside A, so every C activation reaches the same active A through its static link. Its references to x therefore name A's x, initially 4, even when a B activation containing its own x is C's caller. B(2) first calls B(1), which first calls B(0). B(0) calls C: A.x becomes 5 and 5 is returned. B(1) next calls C, obtaining 6, and returns 5+6=11. B(2) next calls C, obtaining 7, and returns 11+7=18. Main prints 18. The recursive B locals would matter under dynamic lookup, but not under the specified lexical lookup.

- **A:** True: the calls to C update the single enclosing A.x to 5,6,7 and their returned values sum to 18.
- **B:** False: 101+102+103=306 uses each calling B activation as the variable environment, which would be dynamic rather than static scoping.
- **C:** False: 15 assumes all three C calls start from a fresh copy of A.x=4; the enclosing activation persists and is modified.
- **D:** False: 21+22+23=66 uses Main.x, but the nearer enclosing declaration in A shadows it.

**Common misconception:** A static link follows lexical nesting, so recursion in a sibling procedure does not create fresh copies of the sibling's enclosing variables.

## Q44

**Correct answer:** C

**Concept:** Digital Logic — Sequential circuits

Using only old-state values, the sequence is 00 → 01 → 11 → 00, a period-three cycle. Thus the state after t edges depends on t modulo 3. Since 2027 = 3×675+2, the state is 11. The unused state 10 maps to 10, but is unreachable from the specified initial state.

- **A:** False: 00 occurs only at edge counts divisible by 3.
- **B:** False: 01 occurs when the edge count is 1 modulo 3.
- **C:** True: 2027 is 2 modulo 3, giving 11.
- **D:** False: 10 is a separate fixed point and is never reached from 00.

**Common misconception:** Flip-flops update simultaneously; substituting an already updated bit gives a wrong transition graph.

## Q45

**Correct answer:** C

**Concept:** Operating Systems — Interprocess communication

Q cannot observe EOF on X while R keeps its writer open, even though R never writes. Hence Q cannot close Y, P cannot finish its read on Y, and R cannot finish waiting for P. Closing R's X writer before its wait breaks this cycle: P closes the remaining X writer; Q consumes X and sees EOF, writes/closes Y and terminates; P consumes Y and sees EOF and terminates; R's wait returns and R terminates. Buffer capacity cannot repair the original dependency cycle.

- **A:** False: descriptor ownership, not capacity, prevents EOF.
- **B:** False: it introduces or preserves a wait cycle.
- **C:** True: closing the otherwise unused writer permits Q to see EOF, after which Q, P, and finally R can terminate.
- **D:** False: it adds a termination dependency.

**Common misconception:** EOF depends on all open writers, including writers held by processes that never send data.

## Q46

**Correct answer:** 12 (exact)

**Concept:** Operating Systems — Concurrency and synchronization

There are 6!/(2×2×2) = 90 interleavings preserving each read-before-write order. Enumerate them while retaining a private register for each thread; the final values are [1, 3, 4, 5, 6, 7, 8, 9, 11, 12, 14, 17], giving 12 distinct outcomes. A direct derivation partitions by the last writer: if A is last, its read can see 0,3,5,8, giving 1,7,11,17; if B is last, its read can see 0,1,5,6,11, giving 3,4,8,9,14; if C is last, its read can see 0,1,3,4,7, giving 5,6,8,9,12. The union of these sets gives the stated answer. The values before a last writer's read come only from the other two threads, which may themselves overlap.

**Common misconception:** Atomic reads and writes do not make a read-modify-write pair atomic.

## Q47

**Correct answer:** A, B, C

**Concept:** Computer Networks — Error detection

Because g has nonzero constant term and degree 3, it cannot divide a monomial, establishing A. A burst of length at most 3 has the form x^k b(x), with nonzero constant term and degree(b)≤2. Since gcd(g,x)=1 and degree(b)<3, it cannot be divisible by g, establishing B. Polynomial division gives x^7+1 = (x^3+x+1)(x^4+x²+x+1), so a two-bit error seven positions apart is undetected, establishing C. The polynomial g itself is an undetected three-bit error, refuting D. Equivalently g(1)=1, so x+1 is not a factor and the universal odd-error guarantee does not hold.

- **A:** True: a generator with constant term 1 and positive degree cannot divide a single monomial.
- **B:** True: after removing the x^k shift, a burst of length ≤3 has degree below that of g.
- **C:** True: g divides x^7+1, and multiplying by x^k only shifts the same error.
- **D:** False: e(x)=g(x) has three nonzero coefficients and is undetected.

**Common misconception:** The degree guarantee for short bursts does not imply the odd-number-of-errors guarantee.

## Q48

**Correct answer:** B

**Concept:** Databases — Tuple calculus

The biconditional requires the employee's completed-project set to equal, rather than merely contain, the department's required-project set. Department A requires {p,q}. Employee u has an extra r and fails; v has exactly {p,q} and passes. Department B requires {q}, exactly w's set, so w passes. Department C requires the empty set, but z has completed r, so z fails. Thus E={v,w}. The universal statement for C does not become automatically true: Required(C,t) is always false, so Done(z,t) must also always be false.

- **A:** False: u has an extra completed project r and violates the reverse implication.
- **B:** True: v and w alone have exactly the required sets.
- **C:** False: z has a nonempty completion set for a department with no required projects.
- **D:** False: both u and z violate set equality.

**Common misconception:** Relational division tests containment; a universal biconditional tests exact set equality, including the empty-set case.

## Q49

**Correct answer:** A, D

**Concept:** Compiler Design — Intermediate code generation

The OR evaluates its right operand exactly when its left operand is false. The left operand is false when x=0 or when x is nonzero and the quotient is at most 2, so A holds. For B use x=2,y=5,z=0: the original quotient is 2, so the original evaluates z++ and returns false, leaving z=1; the proposed comparison 5>4 is true, so it returns true without incrementing z. C is unsafe because x=0 would cause division by zero, an operation the original never evaluates. If x=0 the AND is false without division, so the right operand is evaluated and D follows. Side-effect freedom alone never justifies speculating an operation that can fail.

- **A:** True: these are precisely the paths on which the left side of OR is false.
- **B:** False: x=2,y=5,z=0 is a counterexample due to integer truncation and short-circuit effects.
- **C:** False: the transformation introduces division by zero when x=0.
- **D:** True: no division occurs, and the postfix increment is evaluated once.

**Common misconception:** Boolean algebra transformations must preserve evaluation order, exceptions and side effects, not only real-number algebra.

## Q50

**Correct answer:** A, B

**Concept:** Theory of Computation — Pumping lemma

A substring containing an a and a c must include all p b's between them, plus at least one a and one c, requiring length at least p+2. This contradicts |vxy|≤p, proving A. Consequently deletion of v and y changes the counts of at most two symbol types. At least one symbol is deleted since |vy|>0, while at least one type retains count p. Thus all three counts cannot remain equal; deletions preserve block order, and i=0 is outside L for every legal decomposition. This proves B. To contradict the pumping lemma, every permitted decomposition must fail for some pumping index; choosing only a convenient one, or assuming where its pieces lie, is invalid.

- **A:** True: spanning an a and a c needs at least p+2 symbols.
- **B:** True: at least one count decreases and at least one remains p.
- **C:** False: the lemma asserts existence of a successful decomposition, so every legal choice must be ruled out.
- **D:** False: v and y may lie in other blocks or cross a boundary; the proof must cover those choices.

**Common misconception:** Pumping-lemma proofs require the right quantifier order; the prover does not choose the decomposition.

## Q51

**Correct answer:** B

**Concept:** Programming and Data Structures — Linked lists

The first iteration detaches node 2 and prepends it to q, leaving head 1→3→4→5→6, q 2, and p at 3. The second detaches 4, leaving head 1→3→5→6, q 4→2, p at 5. The third detaches 6, leaving head 1→3→5, q 6→4→2, p NULL. Every detached successor is prepended, so its list is reversed. All terminal next pointers are NULL.

- **A:** False: prepending each removed node reverses their order.
- **B:** True: odd-position nodes remain, and removed even-position nodes are reversed.
- **C:** False: p advances to the next surviving node, so node 3 is never detached.
- **D:** False: removal is based on alternating successors, not splitting the original list in half.

**Common misconception:** Updating next links changes what the subsequent advance follows; removed nodes are prepended rather than appended.

## Q52

**Correct answer:** 167 (exact)

**Concept:** Digital Logic — Fixed-point arithmetic

E7 has unsigned value 231 and signed raw value 231−256=−25, representing −25/16. Hexadecimal 39 is 57, representing 57/16. Their product is −1425/256. To encode with four fractional bits, multiply by 16, obtaining raw value −1425/16 = −89.0625. The nearest integer is −89; there is no tie. Its 8-bit two's-complement encoding is 256−89=167. The represented rounded value is −89/16.

**Common misconception:** Multiplication doubles the fractional-bit count; rounding must follow rescaling before two's-complement encoding.

## Q53

**Correct answer:** 13 (exact)

**Concept:** Programming and Data Structures — Stacks and queues

The prefix forces pushes 1,2,3 followed by pops 3,2. The remaining situation has 1 on the stack and unread inputs 4,5,6. If capacity were unrestricted, completions correspond to all stack permutations of four ordered items [1,4,5,6], with the first push already done; there are Catalan(4)=14. Exactly one of those operation patterns reaches depth 4: pushing all four before any pop, whose output is 6,5,4,1. It is prohibited by capacity three. Therefore there are 14−1=13 completions. Distinct input labels make the push/pop pattern recoverable from the output, so this counts output sequences, not merely schedules. One can also compute F(k,h)=F(k−1,h+1)+F(k,h−1) where the push term is allowed for k>0,h<3 and the pop term for h>0, with F(0,h)=1; the desired F(3,1)=13.

**Common misconception:** After a fixed output prefix, the residual stack contents and capacity still constrain completions.

## Q54

**Correct answer:** B

**Concept:** Computer Organization and Architecture — Hardwired and microprogrammed control

Five destinations have 2^5−1=31 nonempty subsets. There are 8×31=248 non-idle bus commands and one idle command, giving 249 commands. Since 128<249≤256, the joint bus field needs 8 bits. Independently, six ALU choices need 3 bits, 128 addresses need 7 bits, and four sequencing conditions need 2 bits. The total is 8+3+7+2=20 bits. A separate source field plus five literal destination-enable bits would consume more bits, but the question explicitly permits a joint binary command encoding.

- **A:** False: the other fields need 12 bits, leaving only seven bus-command bits, which cannot encode 249 commands.
- **B:** True: 8 bits for the 249 bus commands plus 3+7+2 bits for the other fields gives 20.
- **C:** False: 21 bits suffice but are not minimal; joint encoding uses eight bus bits instead of separately encoding source and destination enables.
- **D:** False: the command choices can be binary encoded; 20 bits already suffice.

**Common misconception:** When controls may be encoded jointly, count legal combined commands rather than blindly adding separate control-signal widths.

## Q55

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

## Q56

**Correct answer:** 2 (exact)

**Concept:** Theory of Computation — Turing machines and undecidability

Set 1 is recognizable by simulating M on 01 and accepting if M accepts. Set 4 is recognizable by dovetailing simulations of M on all binary strings and accepting as soon as one enters q.

Set 2 is not recognizable: given a machine N and input w, construct M which, on any input other than 01, simulates N(w) and accepts exactly if that simulation halts; on 01 it rejects. Then M belongs to set 2 exactly when N(w) does not halt. A recognizer for set 2 would recognize the complement of the halting problem, which is impossible.

Set 3 is also not recognizable. Given N,w, let M on input x simulate N(w) for |x| steps. If that bounded simulation has not halted, M halts; if it has halted, M loops forever. If N(w) never halts, M halts on every input. If N(w) halts after t steps, M loops on every sufficiently long input. Thus membership again recognizes nonhalting if set 3 were recognizable. Exactly sets 1 and 4 are recognizable, giving 2. The designated-state construction uses a computably inserted fresh q, so no accidental visit is required.

**Common misconception:** A finite existential witness can be dovetailed; universal termination and absence of accepted counterexamples cannot in general be recognized.

## Q57

**Correct answer:** A, B, C

**Concept:** Computer Organization and Architecture — Memory interfacing

The region is 0x8000–0xBFFF, so its upper two address bits are 10. A13:A12 enumerate the four 4 KiB subregions, and A11:A0 choose one of 4096 bytes in each chip. Hence A and B hold. Ignoring A14 enables both 0x8000–0xBFFF and 0xC000–0xFFFF; the chip and offset bits are unchanged when A14 flips, so each byte has two aliases, establishing C. In D, A0 is unused, so adjacent byte addresses have the same chip and local address. A12 also redundantly enters the chip's address and decoder, leaving parts inaccessible; one-to-one addressing fails.

- **A:** True: the upper bits 10 identify the 16 KiB window and the next two choose its four chips.
- **B:** True: B123−8000=3123 hexadecimal, giving bank 3 and offset 123.
- **C:** True: toggling the ignored A14 yields another enabled address for the same storage cell.
- **D:** False: ignoring A0 aliases every adjacent address pair.

**Common misconception:** Partial address decoding causes aliasing; chip capacity alone does not guarantee unique processor addresses.

## Q58

**Correct answer:** A

**Concept:** Databases — SQL

For k=1, COUNT(*)=3, COUNT(v)=2 and SUM(v)=20, so both predicates are true. For k=2, counts are 2 and 0, but SUM(v) is NULL; NULL>=10 evaluates UNKNOWN and HAVING does not retain the group. For k=3, both counts are 1 and SUM(v)=5, so the group fails. SQL aggregates retain duplicate non-null values unless DISTINCT is requested. The single output row is (1,3,2).

- **A:** True: only group 1 satisfies both HAVING conditions.
- **B:** False: group 2 has an unknown second predicate and is discarded.
- **C:** False: COUNT does not deduplicate rows or values without DISTINCT.
- **D:** False: group 1 has counts 3 and 2 and sum 20, and therefore passes.

**Common misconception:** SUM over an all-null group is NULL rather than zero, and HAVING keeps only TRUE.

## Q59

**Correct answer:** C

**Concept:** Operating Systems — Deadlock

Original needs are P0=(1,2), P1=(1,1), P2=(2,0). With available (1,1), P1 can finish, releasing (0,1), so work becomes (1,2). P0 can then finish, releasing (1,0), making (2,2); P2 then finishes. Thus the original state is safe. Tentatively grant (0,1) to P0: available becomes (1,0), and P0's need becomes (1,1). P1 still needs (1,1) and P2 needs (2,0). No process can finish with (1,0), so the tentative state is unsafe and the request must be deferred. Unsafe does not by itself assert that deadlock has already occurred.

- **A:** False: after the grant P0 needs one B, but no B is available.
- **B:** False: P2 needs two A, but only one A is available.
- **C:** True: the original safe sequence exists, while no process can start the tentative safety reduction.
- **D:** False: P1,P0,P2 is a safe sequence in the original state.

**Common misconception:** A request within availability and maximum claim can still destroy safety.

## Q60

**Correct answer:** A

**Concept:** Computer Organization and Architecture — Memory hierarchy and performance

The expected additional cost of an L1 miss is 6+0.20×60=18 ns. The initial mean is 1+0.10×18=2.8 ns. The redesigned mean is t+0.05×18=t+0.9 ns. Strict improvement requires t+0.9<2.8, or t<1.9 ns. The L2 miss probability is local, so only the fraction 0.10×0.20 (or 0.05×0.20) of all accesses reaches memory.

- **A:** True: the redesign saves 0.9 ns of expected miss cost, so L1 can rise by less than that.
- **B:** False: it ignores the redesigned system's remaining 0.9 ns expected miss cost.
- **C:** False: this is sufficient but not necessary; for example t=1.8 ns also improves performance.
- **D:** False: values such as t=3 ns satisfy it but are slower than the original.

**Common misconception:** Local miss rates must be multiplied along the hierarchy, and a hit-time increase affects every access.

## Q61

**Correct answer:** C

**Concept:** Algorithms — Greedy algorithms

Earliest-finish selection gives B,C,E,G, a feasible four-activity schedule. The earliest-finish exchange argument guarantees that its cardinality is maximum, so m=4. To count all maximum subsets, partition by the first activity. Starting with A forces D,F,H to fit three more, yielding {A,D,F,H}. Starting with B, the next activity can be C or D. If it is C, the final pair can be (E,G), (E,H), or (F,H). If it is D, the final pair must be (F,H). Starting with C or any later activity permits at most three activities total, so adds no maximum subset. The five maximum subsets are {A,D,F,H}, {B,C,E,G}, {B,C,E,H}, {B,C,F,H}, and {B,D,F,H}. Hence (m,r)=(4,5).

- **A:** False: B,C,E,G is already a feasible set of four activities.
- **B:** False: it omits one of the five listed optimal subsets, often the one beginning with the later-finishing A.
- **C:** True: earliest-finish greedy establishes m=4, and partitioning by the first two choices gives five optimal subsets.
- **D:** False: earliest-finish greedy reaches four and is optimal; five compatible activities cannot be selected.

**Common misconception:** An earliest-finish greedy algorithm finds one optimum, but it does not enumerate every optimal schedule.

## Q62

**Correct answer:** A, C, D

**Concept:** Algorithms — Dynamic programming

In a downward scan, j−wi<j has not yet been updated for the current item. Thus the right-hand side combines the previous-item optimum with at most one copy of the new item, preserving the 0/1 recurrence. This proves A and D. In an upward scan, the lower entry may already contain this item: for the single item (2,3), update D[2]=3 and then D[4]=D[2]+3=6, although the true 0/1 optimum is 3. Hence C is true and B is false. The descending order is a dependency discipline that allows two DP rows to share storage.

- **A:** True: descending capacity order preserves the previous-row dependency for every item.
- **B:** False: upward order can reuse the current item repeatedly.
- **C:** True: the update at capacity 4 reads the newly changed D[2]=3.
- **D:** True: positive weight makes j−wi smaller than j, so the downward scan has not visited it yet.

**Common misconception:** A correct recurrence can become a different optimization problem when in-place update order changes.

## Q63

**Correct answer:** A, B, D

**Concept:** Databases — Integrity constraints

ON DELETE SET NULL changes each referencing pid to NULL, which is permitted because pid is nullable; so A holds. Updating 2 to the unused key 3 preserves the parent primary key and cascades the new value to Child, so B holds. A single-column foreign key with NULL does not require a matching referenced row, so the insertion in C succeeds. The update in D would duplicate existing parent primary key 2 and violates the primary-key constraint. Cascading describes changes to referencing rows; it does not waive uniqueness of referenced keys.

- **A:** True: nullable pid permits the specified SET NULL action.
- **B:** True: the new parent key is unused and the child reference follows the update.
- **C:** False: NULL in this nullable single-column foreign key does not require a parent match.
- **D:** True: primary-key uniqueness independently forbids changing 1 to the existing key 2.

**Common misconception:** Referential actions do not override primary-key uniqueness, and nullable foreign keys have special NULL semantics.

## Q64

**Correct answer:** B, C, D

**Concept:** Engineering Mathematics — Partial orders and lattices

1. Intersections remain in L, so they are meets. All unions are in L except {a} union {b}; for that pair the least available upper bound is {a,b,c}. Hence L is a lattice, but joins need not equal unions.
2. Distributivity fails: {c} meet ({a} join {b})={c}, whereas ({c} meet {a}) join ({c} meet {b})=empty set.
3. Bottom and top complement one another. {a} has complements {b} and {b,c}; {b} has complements {a} and {a,c}; {a,c} and {b,c} are consequently complemented too. The remaining element {c} has no complement: the only nonempty elements disjoint from it are {a} and {b}, and their individual joins with {c} are below top. Thus six elements have complements.
4. Among the three atoms, {c} uniquely has two immediate upper covers; {a} and {b} each have one. Any automorphism must fix {c} and may only fix or swap {a},{b}. The two choices determine all other images, and both are valid. Thus there are exactly two automorphisms.

- **A:** The explicit distributive-law calculation yields {c} on one side and empty set on the other.
- **B:** Only {c} lacks any complement.
- **C:** An automorphism fixes {c}; its only freedom is the swap of a and b.
- **D:** Because {a,b} is absent, the only common upper bound for the two atoms is top.

**Common misconception:** An inclusion-ordered family can have joins different from set union, so it need not inherit Boolean distributivity.

## Q65

**Correct answer:** 325 (exact)

**Concept:** Computer Networks — MAC and Ethernet

One-way propagation is 2400/(2×10^8)=12 microseconds. A far-end station can begin just before the first bit arrives, so the collision disturbance takes almost another 12 microseconds to return. The stated inclusive bound is 24 microseconds, and detector delay adds 2, giving 26 microseconds. At 100×10^6 bits/s the sender must transmit at least 2600 bits. Dividing by eight gives 325 bytes exactly. These are parameters of the idealized link, not a claim about a standard Ethernet minimum frame size.

**Common misconception:** Collision detection requires round-trip propagation plus the specified detector delay, not just one-way propagation or a memorized Ethernet frame size.

