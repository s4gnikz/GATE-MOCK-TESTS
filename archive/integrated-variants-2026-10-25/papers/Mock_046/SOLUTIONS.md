# Worked Solutions — Mock Test 046

## Q1

**Correct answer:** A, C

An exempt design cannot use M. Since D does, it is not exempt, proving C. Approval requires tested or exempt, so it must be tested, proving A and refuting B. D reverses an implication: nothing states that tested designs all use M. Apply the restriction to D, not indiscriminately to all designs.

## Q2

**Correct answer:** B

The combined map is (x,y)→(y+2,x−1). Matching (5,3) gives y=3,x=4, so B. A maps to (6,2), C to (3,5), and D to (8,0). Reversing a composition requires undoing the translation before the reflection.

## Q3

**Correct answer:** C

The observed count can fall either because delays became less frequent or because people submitted fewer reports under the new procedure. With no independent arrival data, these explanations are not separated, so C. A,B assert a punctuality improvement not established by the evidence; D asserts the opposite causal effect without evidence. A change in reporting can change a measured indicator without the underlying service changing.

## Q4

**Correct answer:** 10

**Concept:** Choosing nonadjacent positions.

For reserved indices i<j<k, map them to i,j−1,k−2. Nonadjacency makes these three distinct increasing positions in {1,…,5}. Conversely each such triple reconstructs a valid reservation set. Thus the count is choose(5,3)=10.

**Common misconception:** Subtracting adjacent pairs independently when their overlaps matter.

## Q5

**Correct answer:** B

Overall rates are weighted departmental averages. For example, rates90%,50% with shares90%,10% give86%; later rates91%,51% with shares10%,90% give55%. Both rates rise but the overall rate falls, proving B possible and A false. C and D introduce changes not needed by the example. Comparing weighted averages requires checking the weights.

## Q6

**Correct answer:** A, C
**Concept:** Folding a cube net.

Take B as the front face. Its neighbours A,C,D,F fold to left,right,top,bottom, while E beyond D becomes the back. Opposite pairs are A/C, B/E and D/F. A/E and E/F therefore share edges, proving A,C. B and D list opposite pairs, not adjacent faces.

**Common misconception:** Squares separated in the flat net may become adjacent after folding.

## Q7

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

## Q8

**Correct answer:** 2.0000 (accepted range 1.99995–2.00005)

Let T be the draw on which the first blue appears. T can be1,2,3,4. The tail-sum identity gives E[T]=P(T>0)+P(T>1)+P(T>2)+P(T>3). These probabilities are1,3/5,(3/5)(2/4)=3/10, and(3/5)(2/4)(1/3)=1/10. Their sum is2. Drawing without replacement changes the probabilities after each red; a constant-probability geometric model is inappropriate.

## Q9

**Correct answer:** A

**Concept:** Distinguishing brevity from superficiality.

The sentence explicitly says that required issues remain covered despite removal of repetition, supporting A. B and D contradict this distinction. C claims a necessary length relation not stated or implied.

**Common misconception:** Treating concise and cursory as synonyms in this context.

## Q10

**Correct answer:** 4
**Concept:** Conditional sample space.

The ten qualifying ordered outcomes are (1,2),(2,1), …, (5,6),(6,5), all equally likely. Each possible maximum 2,3,4,5,6 occurs twice. Its conditional mean is (2+3+4+5+6)/5=4.

**Common misconception:** The conditioning event changes which dice outcomes are relevant; the unconditional expected maximum does not apply.

## Q11

**Correct answer:** 36

Four pairs and total participation of the four B entities imply that each B entity occurs exactly once. Each chooses an A endpoint, and all three A entities must occur. Count onto functions from a four-element labeled set to a three-element labeled set:3^4−3×2^4+3×1^4=81−48+3=36. Many-to-many permits these instances; it does not require every entity to have more than one partner.

## Q12

**Correct answer:** B

**Concept:** Computer Organization and Architecture — Interrupts and DMA

DMA reads main memory rather than the processor's dirty cache copies. Writing back the buffer lines and waiting makes main memory contain the updates before DMA reads them. Discarding dirty lines loses modifications. Interrupt control changes notification, not visibility of cached data, and a completion event cannot precede starting the transfer.

- **A:** False: discarding dirty lines without write-back loses the updated data.
- **B:** True: completed write-back makes the DMA source in main memory current.
- **C:** False: interrupt masking does not update memory.
- **D:** False: this ordering cannot start the required transfer and does not flush the cache.

**Common misconception:** DMA bypassing the CPU does not automatically observe its dirty cache contents.

## Q13

**Correct answer:** B, C

A blocking operation can suspend the caller, making the core available to another runnable process; B and C hold. The caller need not busy-wait, so A is false. An empty pipe with a writer still open may later receive data; emptiness alone does not establish EOF, refuting D.

## Q14

**Correct answer:** 0.5

**Concept:** Floating-point spacing within one exponent bin.

Values in [8,16) have exponent three. Four fractional significand bits give spacing 2^(3−4)=1/2.

**Common misconception:** Using precision as the exponent or counting the leading bit twice.

## Q15

**Correct answer:** A

**Concept:** Output dependencies under out-of-order completion.

Two writes to one register create a write-after-write hazard: the program-order younger value must remain final even if completion order differs. A names it. B involves no writes, C is unrelated to register naming, and D falsely classifies every write as a control transfer.

**Common misconception:** Considering only read-after-write dependencies.

## Q16

**Correct answer:** A

**Concept:** Prefix balance as well as total balance.

A closing parenthesis cannot precede its matching opening parenthesis, so every prefix must have nonnegative unmatched-open count, A. Balanced words have even length, contradicting B; nesting refutes C and can require unbounded stack height, refuting D.

**Common misconception:** Checking only equal total numbers of opening and closing parentheses.

## Q17

**Correct answer:** B
**Concept:** Language of a left-recursive grammar.

Each recursive step appends either a or b to the right of the remaining A, and the terminating production replaces A by c. The result is c followed by any string over {a,b}, namely B. A,C place c at the wrong end; D unnecessarily forces alternating pairs.

**Common misconception:** Left recursion describes a derivation mechanism, not the position of the terminal base symbol in the final word.

## Q18

**Correct answer:** A, C

**Concept:** Finite configuration-space reachability.

Determinism makes a repeated nonhalting configuration repeat its entire future, proving A. Record configurations and stop on acceptance, rejecting halt, or repetition; finiteness ensures one occurs, proving C. Plain simulation can loop forever, refuting B and D.

**Common misconception:** Confusing finitely many possible states with finitely many execution steps.

## Q19

**Correct answer:** A, C

Concept: divide-and-conquer tree sums. Level j has 3ʲ calls of size n/2ʲ, costing Θ(n²(3/4)ʲ). Summing this decreasing geometric series gives Θ(n²), A; B incorrectly adds a logarithmic factor. The depth is log₂n and the number of leaves 3^(log₂n)=n^(log₂3), C. D confuses logarithmic depth with n levels.

## Q20

**Correct answer:** A, B, C
**Concept:** Annihilating polynomial and eigenvalue multiplicities.

The minimal polynomial divides (t−1)(t+1), whose roots are real and distinct. Thus M is diagonalizable with eigenvalues ±1. Trace zero and dimension four force two of each. The determinant is 1 and rank(M−I)=2, proving A,B,C. D need not hold: the block [[1,1],[0,−1]] squares to I but is not symmetric; combine it with diagonal entries 1,−1 for a four-dimensional counterexample.

**Common misconception:** Real diagonalizability does not imply orthogonal diagonalizability or symmetry.

## Q21

**Correct answer:** A, B

A selects at least one true input but excludes both true, while B explicitly selects the two unequal-input cases. Both are XOR. C also accepts11; D complements XOR and accepts equal inputs. A truth table verifies all four cases.

## Q22

**Correct answer:** C

**Concept:** Programming and Data Structures — Trees

A is the root. Its first subtree must contain B,C because B closes at the second postorder position; its other subtree contains D,E. Thus A has two children, B and D. B has only child C and D has only child E. Either only child may independently be placed left or right, giving 2*2=4 trees.

- **A:** False: traversals do not specify which side holds an only child.
- **B:** False: there are two independent only-child choices, not one.
- **C:** True: two independent left/right choices give four.
- **D:** False: A must have two children; it does not contribute a third binary choice.

**Common misconception:** Preorder and postorder can fix subtree membership without fixing the side of an only child.

## Q23

**Correct answer:** A

**Concept:** Gray-code adjacency in Karnaugh maps.

The order makes each adjacent pair differ in one variable, including 10 next to 00 at wraparound. Such pairs can combine while eliminating one literal. A holds. B wrongly universalizes a display convention; C confuses reordering with changing function values; D states the opposite adjacency condition.

**Common misconception:** Ignoring edge wraparound when reasoning about adjacent map cells.

## Q24

**Correct answer:** A, C
**Concept:** Local structure imposed by a regular expression.

Each 1 is introduced in a block 11; adjacent blocks may merge, but each resulting run has even length. Conversely, every even-length run can be partitioned into such blocks, separated by zeros. Thus A holds and 110011 is accepted (C). The string 101 has two 1s overall but two odd runs, refuting B and D.

**Common misconception:** Even parity over the entire string differs from even parity in every run.

## Q25

**Correct answer:** A, C

The successor is the leftmost node in v's right subtree, so it cannot have a left child, proving A and refuting D. It may lie several edges below v, refuting B. Its possible right child can replace it at its original parent link, proving C. If s is v's immediate right child, that former parent is v itself.

## Q26

**Correct answer:** D

Concept: negating the pumping condition. The regular-language statement has order ∃p ∀w ∃split ∀i with membership preserved. Negation gives ∀p ∃w ∀split ∃i with membership failing, exactly D. A only exhibits one bad split; B chooses the split and even requires failure at i=1, which reproduces w; C uses the wrong initial quantifier and still allows a bad chosen split. The adversary chooses the decomposition.

## Q27

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

## Q28

**Correct answer:** 3

Rolle's theorem gives at least four distinct roots of f' between consecutive roots of f, and then at least three roots of f''. A degree-five polynomial with five distinct real roots has a cubic second derivative, showing three is attainable. Repeated application supplies a lower bound, while degree supplies attainability.

## Q29

**Correct answer:** 0 (exact)
**Concept:** Relational composition and set difference.

The only joinable chain is 1→2→3, producing T={(1,3)}. The renamed R already contains (1,3), so T−R is empty. Its cardinality is zero.

**Common misconception:** Projecting a join can produce a pair that is already present in the original relation.

## Q30

**Correct answer:** 0.4

Inclusion–exclusion gives P(A∩B)=0.4+0.5−0.7=0.2. Divide by P(B)=0.5 to get P(A|B)=0.4. Conditional probability uses the intersection as numerator, not the union.

## Q31

**Correct answer:** 2

Concept: antichains and chain bounds. Partition the divisors into chains 1|2|4|12 and 3|6. An antichain contains at most one element from each, hence size at most two. The incomparable pair {3,4} attains two. The number of divisors is not the width.

## Q32

**Correct answer:** B

**Concept:** Algorithms — Graph traversals

Nested intervals show that u is a proper ancestor of v in the DFS forest. The tree path from u to v consists of directed edges. Adding v→u closes a directed cycle; v→u is a back edge. Thus only B follows.

- **A:** False: a tree edge runs from an ancestor to a newly discovered descendant, not back to an ancestor.
- **B:** True: the tree path u to v together with v→u is a directed cycle.
- **C:** False: the nested intervals identify an ancestor relationship, not separate branches.
- **D:** False: this return edge closes a cycle.

**Common misconception:** Nested DFS intervals alone do not imply acyclicity; edge direction matters.

## Q33

**Correct answer:** -6

Taking determinants gives det(P)det(A)=det(L)det(U)=1×6. One row interchange has det(P)=−1, hence det(A)=−6. The permutation sign must be retained when reconstructing the determinant from pivoted factors.

## Q34

**Correct answer:** B

Following alpha reaches beta, which immediately leads back to alpha. No address record is supplied, so B. A,C,D invent an address unsupported by this configuration. Cycle detection can stop the futile traversal but cannot derive missing address data.

## Q35

**Correct answer:** A, C

Each link supplies its own framing, so A,C are true. Its checksum must correspond to its own frame rather than blindly copying the incoming one, refuting B. Changing encapsulation does not require changing the application message, refuting D.

## Q36

**Correct answer:** 1

**Concept:** Don't-care expansion.

The ON and don't-care minterms together are exactly the assignments with b=0. The term b′ covers all ON minterms and no OFF minterm, using one literal. A zero-literal term would be constant one and cover every OFF minterm, so one is minimal.

**Common misconception:** Treating don't-care values as required zeros or as required ones in the final function.

## Q37

**Correct answer:** 0.0833 (accepted range 0.08325–0.08335)

Integrate the identity on[0,1]. By substitution u=1−x, both integrals on the left equal I=∫f. Therefore2I=∫0¹(x−x²)dx=1/2−1/3=1/6, giving I=1/12≈0.083333. The individual function need not be uniquely specified for its integral to be determined.

## Q38

**Correct answer:** 7

The unique minimum tree uses weights1,2,3 and totals6. The tree AB,BC,DA has weight7. Since all edge weights are integers, no spanning-tree weight lies strictly between6 and7, so7 is the next possible optimum. Constructing a tree attains the lower bound.

## Q39

**Correct answer:** 64

The two high-bit pairs must match. Choose their common value in4 ways, and choose each input's low-bit pair independently in4 ways. Total 4×4×4=64 ordered pairs require the second comparison. Equality of the high halves does not imply equality of the full inputs.

## Q40

**Correct answer:** 123

The saved source is 7. R changes 100→104→100 before the destination fetch, so the destination is the same word and becomes 14. The word at 104 stays 9, and R ends at 100. Their sum is 100+14+9=123. Evaluating both addresses from an imagined simultaneous operand fetch would violate the given instruction semantics.

## Q41

**Correct answer:** 3

The first three sends fill the three slots. The fourth finds no capacity and blocks before completing, so three have completed. Counting attempted sends would give four, which is not the requested quantity.

## Q42

**Correct answer:** B, C, D

If both threads read the same value before either writes at each round, updates are lost and the final value is 2. Serial execution gives 4. For 3, let both first reads see 0, let both write 1, then execute each second increment serially. These establish B,C,D. Every second write is based on a read after that thread's first write; all first writes are at least 1 and no later write can be 0. Hence every second write is at least 2. A final value 1 is impossible because the last write belongs to a thread's second increment. Atomic individual accesses do not make the increment atomic.

## Q43

**Correct answer:** A, C

Simulate the machine on00 and accept its encoding if it accepts00; this recognizes S, so A is true. Membership depends only on the recognized language and holds for some languages but not others, so C is true. By the undecidability of nontrivial semantic language properties, S is undecidable, disproving B. Equivalently one can reduce arbitrary machine acceptance to acceptance on the fixed string by embedding the original machine and input in a new machine. If both S and its complement were recognizable, dovetailing their recognizers would decide S, so D is false. A fixed input length does not bound computation time.

## Q44

**Correct answer:** B

**Concept:** Longest-path dynamic programming in a DAG.

Initialize the source distance to zero and unreachable distances to negative infinity; process reachable edges in topological order. Every predecessor distance is final before a vertex is processed, so maximizing over incoming paths is correct regardless of negative weights. This proves B and refutes A. Path lengths in edges may differ (C false), and converting to an undirected graph destroys the acyclic dependency structure (D false).

**Common misconception:** Transferring restrictions of greedy shortest-path algorithms to topological dynamic programming.

## Q45

**Correct answer:** C
**Concept:** Tail-call position.

In C, argument evaluation acc*n happens before the call, and the returned value is passed straight to the caller with no subsequent work. In A and B the caller must still add or multiply after f returns. In D, g must be called after f returns, so f is not the tail call being considered. Only C satisfies the stated eligibility condition for its recursive call.

**Common misconception:** An expression occurring after the word return is not necessarily a tail call.

## Q46

**Correct answer:** A, C

Concept: alias-sensitive optimization. When i≠j, the store does not modify A[i], so reuse p (A). When i=j, the last load reads 7 (C). Without a proven relation, the i=j case with old value not 7 defeats B. The same case defeats D. Equal expression text does not ensure an unchanged memory value across a store.

## Q47

**Correct answer:** C

Key 7 must be the root. Key 6 is already at index 3. If 5 were at index 4 or 5, its parent at index 2 would have to exceed 5; both available larger keys are already elsewhere. Index 2 is possible, and indices 6,7 have parent 6, so each is possible. Hence exactly {2,6,7}: C. A excludes feasible child positions; B includes impossible positions 4,5; D includes the root occupied by 7.

## Q48

**Correct answer:** B, D

Concept: negative edges and premature finalization. True best route s→b→a→t costs 5−4+3=4, so B is true and A false. Other routes cost 5 and 6. The graph is acyclic, so C is false. Dijkstra first finalizes a at two, sets t to five, and then chooses t before b at the specified tie, returning five, so D is true. The negative edge permits later improvement of an already-finalized distance.

## Q49

**Correct answer:** A, C

The outer R(x,y) requires membership. The negated existential rules out another y value for that same x, so A,C are true. Other x values are irrelevant to this test, making B false. The membership conjunct excludes pairs outside R, making D false. Uniqueness is per x, not a requirement that the whole relation contain one tuple.

## Q50

**Correct answer:** 13.75

**Concept:** Within-group and between-group population variance.

The weights are 1/4 and 3/4, and the combined mean is 6.5. Variance is (1/4)[1+(2−6.5)²]+(3/4)[9+(8−6.5)²]=13.75. Equivalently, within-group variance 7 plus between-group variance (1/4)(3/4)(8−2)²=6.75 gives 13.75.

**Common misconception:** Averaging only subgroup variances and ignoring differences in means.

## Q51

**Correct answer:** A, C

Stable least-significant-key-first sorting preserves the year order within each city and retains arrival order for exact ties, so A is true. Explicitly restoring arrival order before the same two stable passes also works, so C is true. B makes year the primary key and can interleave cities incorrectly. D can destroy arrival order for equal keys, and a later stable city sort will preserve that damage. Stability matters for ties, not just for the primary ordering.

## Q52

**Correct answer:** A, B, C

Left cancellation makes x↦ax injective. On a finite set it is then surjective, proving A and giving b with ab=e, proving B. Now a(ba)=(ab)a=a=ae, so cancellation yields ba=e, proving C. On an infinite set an injective map need not be surjective; nonnegative integers under addition supply a cancellative monoid with noninvertible positive elements, disproving D.

## Q53

**Correct answer:** A, C, D

Concept: subset simulation and accepting suffixes. Starting at {p}, input 0 gives {p,q}, then 1 gives {p,r}, then 0 gives {p,q}; A holds and B fails because final acceptance requires r after the whole word, not an earlier prefix. Reachable subsets are {p},{p,q},{p,r},{p,q,r}, proving C. A zero creates q, and exactly one more symbol reaches r; r has no outgoing transitions. Thus final acceptance records a zero exactly two positions from the end, proving D.

## Q54

**Correct answer:** B
**Concept:** Outstanding bytes and the updated send window.

After the ACK, outstanding data are bytes 23000 through 24999, totaling 2000. The effective window is min(10000,4000)=4000 bytes. Thus 4000−2000=2000 additional bytes can be sent. B is correct. A uses an obsolete window edge, C ignores outstanding data, and D exceeds the receive window.

**Common misconception:** A window advertises total allowed unacknowledged data, not an allowance entirely additional to data already in flight.

## Q55

**Correct answer:** 7 (exact)
**Concept:** Balanced parentheses with a depth bound.

A nonempty primitive balanced block of maximum depth at most two has the form '(' followed by k copies of '()' then ')', contributing k+1 pairs. Every depth-at-most-two string decomposes uniquely into such blocks. Thus strings with four pairs correspond to compositions of 4, of which there are 2³=8. Exactly one, ()()()(), has maximum depth one. Subtract it to obtain seven with depth exactly two.

**Common misconception:** Counting all balanced strings ignores the nesting-depth restriction; counting depth at most two still includes depth one.

## Q56

**Correct answer:** B
**Concept:** Saturation versus modular overflow.

S saturates 7+3 to 7, then adds −5 to obtain 2. W represents 10 as signed −6, then wraps −6−5=−11 to signed 5. Thus (2,5). A delays saturation until the end; C fails to wrap the second W addition; D reports intermediate values.

**Common misconception:** Applying overflow rules after each operation differs from applying them only to the final exact result.

## Q57

**Correct answer:** 0.21484375

A valid even-parity word remains valid exactly when an even number of bits flips. Excluding no change, the possibilities are two or four flips. Their total probability is C(4,2)(1/4)²(3/4)²+(1/4)^4=54/256+1/256=55/256=0.21484375. The undetected-error probability excludes the zero-error event.

## Q58

**Correct answer:** C

**Concept:** Compiler Design — Lexical analysis

After reading a, the lexer has an accepting position for token a, but ab*c is still possible. It must continue across all n b symbols because a subsequent c would make them part of the longer token. The following d rules out that longer token. No position after the first a was accepting for a token beginning there, so the lexer returns to the position after a. It has inspected n+1 characters beyond that accepting position. This amount is unbounded as n grows.

A and B propose fixed bounds disproved by large n. C is correct. D would violate longest match on inputs that end the prefix with c instead of d.

- **A:** False: proposes a fixed bound of at most one character, disproved by inputs with large n.
- **B:** False: proposes a fixed bound of at most two characters, disproved by inputs with large n.
- **C:** True: before returning token a, the lexer must inspect all n occurrences of b plus character d, requiring n+1 lookahead characters, which is unbounded as n grows.
- **D:** False: violates longest match; token a cannot be emitted immediately because longer candidate ab*c may follow.

**Common misconception:** Recognition by a finite automaton does not guarantee a fixed bound on longest-match backup.

## Q59

**Correct answer:** C

**Concept:** Digital Logic — Sequential circuits

Using only old-state values, the sequence is 00 → 01 → 11 → 00, a period-three cycle. Thus the state after t edges depends on t modulo 3. Since 2027 = 3×675+2, the state is 11. The unused state 10 maps to 10, but is unreachable from the specified initial state.

- **A:** False: 00 occurs only at edge counts divisible by 3.
- **B:** False: 01 occurs when the edge count is 1 modulo 3.
- **C:** True: 2027 is 2 modulo 3, giving 11.
- **D:** False: 10 is a separate fixed point and is never reached from 00.

**Common misconception:** Flip-flops update simultaneously; substituting an already updated bit gives a wrong transition graph.

## Q60

**Correct answer:** 1

Deleting e leaves six edges and retains connectivity on six vertices. A spanning tree needs five edges and exists in every connected graph, so one further appropriate edge removal suffices. Arbitrarily deleting a bridge would not be an appropriate choice.

## Q61

**Correct answer:** A, B, D
**Concept:** SQL aggregate and NULL semantics.

A has COUNT(*)=3, COUNT(amount)=2 and SUM=30, satisfying both predicates. B has counts 2 and 0, but SUM is NULL and NULL>10 is UNKNOWN, so it is excluded. C has equal counts and is excluded. Thus one row (A,30) remains: A,B true and C false. Replacing COUNT(amount) with COUNT(*) makes the strict inequality false in every group, proving D.

**Common misconception:** SUM of an all-NULL group is NULL, not zero, and HAVING retains only TRUE.

## Q62

**Correct answer:** A, C, D

The Boolean matrix merges all parallel edges into one true entry, losing multiplicities(A,D). Therefore its row sum can undercount outdegree, disproving B. Parallel-edge multiplicity does not change whether a path exists, so collapsing them preserves reachability(C). Multiplicity matters for degrees and edge counts even when it does not matter for reachability.

## Q63

**Correct answer:** B

p−1=a+3 points to the last actual element and may be dereferenced. p itself is one-past, so A,D dereference outside the array. p+1 goes beyond even the permitted one-past pointer, making C invalid. Forming a boundary pointer does not authorize reading at it.

## Q64

**Correct answer:** 4

**Concept:** Register requirements for expression trees.

Each leaf needs one register. Each two-leaf sum needs two. At each multiplication, after one sum is retained in a register, evaluating its sibling sum needs two additional registers, so each product needs three. At the root, retaining one product while evaluating the other requires 1+3=4 registers. This ordering attains four. Whichever product is evaluated first, the other still requires three while the first remains live, proving four is minimal under the stated restrictions.

**Common misconception:** Taking the maximum child requirement without counting a retained sibling result.

## Q65

**Correct answer:** 22

**Concept:** Microinstruction field allocation.

The next-address field needs log₂256=8 bits. Add twelve control bits and two sequencing bits: 12+8+2=22.

**Common misconception:** Confusing the number of control-store words with the address-field bit count.

