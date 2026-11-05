# Worked Solutions — Mock Test 003

These solutions accompany the rebuilt paper. Verification methods and unresolved review items are recorded separately in the paper's review report. No human review is claimed.

## Q1

**Correct answer:** B  
**Concept:** Reading comprehension and inference.

Weekly visits may be redistributed across times without increasing their total. In addition, one visitor can make several visits, so distinct visitors cannot be inferred from visit totals. B identifies both gaps. A wrongly excludes redistribution; C asserts an unsupported decrease; D replaces a possibility with an assertion about every visitor.

**Common misconception:** Treating counts of events as counts of distinct people, or a before/after association as proof of recruitment.

## Q2

**Correct answer:** 36  
**Concept:** Permutations with adjacency and order restrictions.

There are 5!=120 arrangements. Adjacent C,D can be treated as a block with two internal orders, giving 2×4!=48. Thus 72 avoid adjacency. Exchanging labels A and B pairs these arrangements without changing C,D adjacency; exactly half have A before B. Answer: 72/2=36.

**Common misconception:** Requiring A before B does not require them to be adjacent.

## Q3

**Correct answer:** A, C  
**Concept:** Weighted averages and composition effects.

P improves from 80% to 90%; Q improves from 20% to 30%, so A is true. Combined success falls from 100/200=50% to 36/100=36%, making B false. Q's application share rises from 100/200=50% to 90/100=90%, so C is true. D is false: the table neither follows comparable individuals nor identifies a causal policy effect.

**Common misconception:** An aggregate percentage can fall while each group's percentage rises, because the group weights change.

## Q4

**Correct answer:** B  
**Concept:** Reflection under folding.

Undoing the folds gives x coordinates 1 and 7 and y coordinates 3 and 5. The four holes are (1,3),(1,5),(7,3),(7,5). Opposite corners have distance √(6²+2²)=√40=2√10. A counts only the horizontal separation; C is the side length of the original sheet; D corresponds to a different diagonal.

**Common misconception:** A fold reflects a coordinate about its crease; it does not simply translate a hole by half the sheet width.

## Q5

**Correct answer:** C  
**Concept:** Narrative reference and causal order.

R initiates the first inspection. S refers to that inspection and identifies the defect. Q repairs the identified defect and starts the second inspection. P gives that second inspection's result. Thus R,S,Q,P is coherent. A repairs before identifying the crack; B uses the inspection reference before its introduction; D places repair and retesting before the initiating event.

**Common misconception:** Pronoun references and causal dependencies constrain order even when each sentence is grammatical alone.

## Q6

**Correct answer:** C  
**Concept:** Conditional probability with a hidden box.

In Box I, both-red probability is 1/3 and at-least-one-red probability is 1. In Box II these probabilities are 0 and 2/3. Including the equal box priors gives P(both red)=1/6 and P(at least one red)=1/2+1/3=5/6. Their ratio is 1/5. A gives the unconditional numerator; B ignores the box information in the condition; D is twice the required ratio.

**Common misconception:** Conditioning changes the probability of the selected box as well as the probability of its ball outcomes.

## Q7

**Correct answer:** B  
**Concept:** Necessary conditions and separate permissions.

No renewal implies stopping Monday. Because the policy is obeyed and the pilot continues Tuesday, renewal occurred before Monday. Expansion has the additional review requirement, whose satisfaction is not stated. B follows. A and C infer expansion permission without evidence; D treats review as a substitute despite the word “also.”

**Common misconception:** Satisfying a necessary condition for one action does not satisfy all conditions for a different action.

## Q8

**Correct answer:** A, B  
**Concept:** Logarithm bases and domain constraints.

Put y=log₂x. The domain requires x>0 and x≠1, hence y≠0. Change of base gives log_x16=4/y, so 4/y=y and y²=4. Therefore x=2²=4 or x=2⁻²=1/4. A and B satisfy the original equation. C has a negative base and argument for real logarithms; D uses the invalid base 1.

**Common misconception:** A logarithm base may lie between zero and one; only positivity and exclusion of one are required.

## Q9

**Correct answer:** 16  
**Concept:** Counting orders satisfying cyclic inequalities.

All four assertions cannot be true, since they form a strict cycle; all four cannot be false for the same reason in reverse. Exactly three true assertions occur in four orders: choose which assertion is false, and the other three force a single chain. Reversing each order gives four orders with exactly one true assertion. The remaining 4!−4−4=16 have exactly two true assertions.

**Common misconception:** The four pairwise comparisons are constrained by transitivity, so their truth values are not independent coin tosses.

## Q10

**Correct answer:** 78  
**Concept:** Surface area after removing cubes.

The original exposed area is 6×3²=54. Each removed face-centre cube previously exposed one face. Its removal loses that face and exposes its five neighbouring cubes' faces, a net increase of four. The six removed cubes are not face-adjacent, so these changes do not double-count a shared removed interface. Total: 54+6×4=78.

An independent count is eight corner cubes with three exposed faces, twelve edge-centre cubes with four, and the core cube with six: 24+48+6=78.

**Common misconception:** Newly exposed inward faces count even though they are not on the original outer planes.

## Q11

**Correct answer:** A, C  
**Concept:** Bounded simulation and decidability.

A is decidable by simulating at most 100 transitions. C is decidable by checking whether any rejecting state is reachable from the DFA's start state. B is the general halting problem. D is undecidable: given machine M and input w, construct a machine that ignores its own input and simulates M on w; it halts on all inputs exactly when M halts on w.

**Common misconception:** A finite description does not imply a computable bound on an arbitrary computation's duration.

## Q12

**Correct answer:** D  
**Concept:** Chip selection and local addressing.

Each chip covers 0x1000 bytes. Chip bases are 0x8000,0x9000,0xA000,0xB000. Address 0x9ABC lies in chip 1 at offset 0xABC. A fails both the range and local-offset requirement; B chooses the next chip; C exceeds the maximum local offset 0xFFF.

**Common misconception:** Local chip addresses exclude the bits used to select the chip.

## Q13

**Correct answer:** A  
**Concept:** Continuity and matching one-sided derivatives.

Near zero, eˣ=1+x+x²/2+O(x³), so the left branch is 1+x/2+O(x²). Continuity requires a=1, and matching derivatives requires b=1/2. B and D fail continuity; C preserves continuity but has right derivative 1 instead of 1/2.

**Common misconception:** Matching function limits ensures continuity, not differentiability.

## Q14

**Correct answer:** 0.21  
**Concept:** Bernoulli variance and affine transformation.

X+2Y=2−X. If p=P(X=1), its expectation is 2−p=1.7, so p=0.3. Translation and a sign change preserve variance: Var(2−X)=p(1−p)=0.3×0.7=0.21.

**Common misconception:** X and Y are dependent; adding their variances as if independent is invalid.

## Q15

**Correct answer:** B  
**Concept:** Recursive execution order.

visit(1) prints 1. visit(2) calls visit(1), prints 2, then calls visit(0), yielding 1,2. visit(4) therefore prints 1,2 from its first call, then 4, then 1 from visit(1). B is correct. A moves the right subtree before the root; C is preorder; D assumes every value from 1 through 4 is visited.

**Common misconception:** The recursive arguments determine the visited values; they are not necessarily all integers below the initial argument.

## Q16

**Correct answer:** 6  
**Concept:** Process creation and inherited control flow.

The first fork creates two processes. Only its child has p=0, so the conditional fork increases the population to three. Every one of these three executes the unconditional final fork, giving six processes reaching work().

**Common misconception:** Not every fork in source code is executed by the same set of processes.

## Q17

**Correct answer:** B  
**Concept:** Linear probing and deletion markers.

All inserted keys hash to 3, occupying indices 3,4,5. Deleting 17 leaves a tombstone at 4. Searching 24 examines 3,4,5: three probes. The known-absent 31 then occupies tombstone 4. A and D stop the search too early; C ignores the reusable tombstone.

**Common misconception:** A tombstone may be reused by insertion but cannot terminate a lookup chain.

## Q18

**Correct answer:** B, C, D  
**Concept:** Interleaving and lost updates.

For 2, both threads read 0 before either first write, then both read 1 before either second write. For 4, run the threads serially. For 3, let the first pair of increments lose one update, reaching 1, then execute the two remaining increments serially.

Value 1 cannot be final: the final write is a thread's second write. Its preceding read occurs after its first write, which wrote at least 1; no operation writes 0, so that final read is at least 1 and the final write at least 2. Thus A is false and B,C,D are true.

**Common misconception:** Atomic individual accesses do not make a read-modify-write increment atomic.

## Q19

**Correct answer:** 3  
**Concept:** Functions commuting with a permutation.

Choose f(1)=a. Commutation forces f(2)=g(a) and f(3)=g²(a). The final condition f(g(3))=g(f(3)) holds because g³(a)=a. Every one of the three choices for a therefore gives exactly one valid function. These are the identity, g, and g².

**Common misconception:** The three function values cannot be chosen independently once commutation is imposed.

## Q20

**Correct answer:** A, B, C  
**Concept:** Annihilating polynomial and eigenvalue multiplicities.

The minimal polynomial divides (t−1)(t+1), whose roots are real and distinct. Thus M is diagonalizable with eigenvalues ±1. Trace zero and dimension four force two of each. The determinant is 1 and rank(M−I)=2, proving A,B,C. D need not hold: the block [[1,1],[0,−1]] squares to I but is not symmetric; combine it with diagonal entries 1,−1 for a four-dimensional counterexample.

**Common misconception:** Real diagonalizability does not imply orthogonal diagonalizability or symmetry.

## Q21

**Correct answer:** A, D  
**Concept:** Cardinality and total participation.

Each employee has exactly one department, so E→D and every employee appears in the E projection. Many employees may share one department, refuting B. A department may have none, refuting C. Thus A,D hold.

**Common misconception:** Total participation on one side of a relationship does not imply total participation on the other.

## Q22

**Correct answer:** B  
**Concept:** Multiplexer truth-table construction.

For AB=00 output C is true only at minterm 1. For AB=01 output NOT C is true at 2. AB=10 gives 4 and 5. AB=11 gives none. Therefore the on-set is {1,2,4,5}. A reverses the first two data inputs, C exchanges select groups 10 and 11, and D does not match the prescribed data inputs.

**Common misconception:** A select bit is not another data input; first identify the selected function, then evaluate C.

## Q23

**Correct answer:** C  
**Concept:** Syntax-directed postfix translation.

The grammar groups the input as (8−3)−2. The first subtraction emits 8 3 −; the outer one appends 2 −. C is correct. A encodes 8−(3−2), B is prefix, and D is infix.

**Common misconception:** Postfix output follows the parse tree's grouping rather than the textual placement of operator symbols.

## Q24

**Correct answer:** A, B  
**Concept:** TCP byte-stream delivery.

TCP preserves byte order, but not send-call boundaries. Buffering and arrival timing permit a single five-byte return or a one-byte return followed by four, proving A and B. With a blocking socket and no closure, lack of data causes waiting, not a zero return; C is false. Ordered delivery excludes D.

**Common misconception:** TCP provides a byte stream, not an application-message boundary for every send call.

## Q25

**Correct answer:** A, C  
**Concept:** Sequential state evolution.

Starting at 01: 01→11→10→01. Its period is three, and the second state after reset is 10. A,C are true. State 00 is a separate fixed point, never reached from reset, so B is false. At 11 the bits are equal, refuting D.

**Common misconception:** Reset selects one state-cycle component; not every representable state is reachable from it.

## Q26

**Correct answer:** 0  
**Concept:** Relational composition and set difference.

The only joinable chain is 1→2→3, producing T={(1,3)}. The renamed R already contains (1,3), so T−R is empty. Its cardinality is zero.

**Common misconception:** Projecting a join can produce a pair that is already present in the original relation.

## Q27

**Correct answer:** D  
**Concept:** Static and dynamic activation links.

R's lexical parent is P, so one static link reaches P. Its caller is Q, whose caller is P, so two dynamic links are required. A reverses the link roles, B assumes caller and lexical parent coincide, and C incorrectly follows a sibling in the static chain.

**Common misconception:** Lexical nesting and call nesting are different structures.

## Q28

**Correct answer:** 20  
**Concept:** Array views and address strides.

C[1][2] is B[2][1], at 1000+4(2×4+1)=1036. C[0][1] is B[1][0], at 1000+4(1×4)=1016. Difference: 20 bytes. A transposed view changes index interpretation, not physical storage.

**Common misconception:** A transpose view is not necessarily a contiguous row-major array in its own index order.

## Q29

**Correct answer:** C  
**Concept:** Circular-list pointer updates.

The first update bypasses node 1, making node 2 the head. Inserting 5 after old tail 4 sets 4.next=5 and 5.next=2. Updating tail to 5 leaves head=2. Thus traversal is 2,3,4,5. A retains the deleted node; B starts at the tail; D inserts 5 before rather than after node 4.

**Common misconception:** In a tail-only circular-list representation the head is defined indirectly as tail.next.

## Q30

**Correct answer:** A, B, C  
**Concept:** Conditional cache hit rates.

L1 misses with probability 0.2. Half hit L2 and half reach memory, each with probability 0.1. Expected time is 1+0.2×9+0.1×90=11.8 ns. A,B,C hold. D confuses a conditional 50% with an unconditional 10%.

**Common misconception:** Additional miss penalties must be weighted by the probability of reaching their level.

## Q31

**Correct answer:** D  
**Concept:** Harmonic running-time sum.

For a fixed i there are floor(n/i) calls. Their sum is Θ(nH_n)=Θ(n log n): replacing each floor by n/i changes the sum by less than n. A and C underestimate the harmonic accumulation; B treats the inner loop as n iterations for every i.

**Common misconception:** A nested loop need not be quadratic when its step size depends on the outer index.

## Q32

**Correct answer:** B  
**Concept:** Pipe endpoint lifetime.

End-of-file requires the pipe buffer to be empty and every write-end reference to be closed. Child II still owns one, so the read blocks. A ignores that inherited reference. C is not stream-read behavior. D concerns writing to a pipe with no reader, not this read operation.

**Common misconception:** The process that supplied the data is not necessarily the only process keeping the pipe open.

## Q33

**Correct answer:** 200  
**Concept:** HTTP connection reuse and parallel rounds.

The HTML costs one handshake plus one request-response: 80 ms. Each of three parallel image connections then costs 80 ms for its first image. Their second images need only another request-response, 40 ms. Total 80+80+40=200 ms.

**Common misconception:** Persistent connections save the second handshake, but non-pipelined dependent requests still consume another RTT.

## Q34

**Correct answer:** 3  
**Concept:** Derivative criterion for monotonicity.

f′(x)=3x²−6x+c=3(x−1)²+c−3. Its minimum over [0,2] occurs at 1 and equals c−3. Nonnegative derivative throughout is equivalent to c≥3. For c<3 the derivative is negative near 1, so monotonicity fails.

**Common misconception:** Checking only the endpoints of a derivative can miss its interior minimum.

## Q35

**Correct answer:** 4  
**Concept:** DFA residual states and the empty string.

Use the three remainder states with transition r→(2r+b) mod 3, accepting remainder 0. Add a separate nonaccepting initial state whose transitions on 0,1 go to remainders 0,1. All four are reachable.

Remainder 0 is distinguished from the others by the empty suffix. Remainders 1 and 2 are distinguished by suffix 1: only remainder 1 reaches zero. The initial state differs from remainders 1 and 2 by suffix 0, which it accepts but they reject. Thus four states are necessary as well as sufficient.

**Common misconception:** Rejecting the empty representation can require separating the initial state from numeric remainder zero.

## Q36

**Correct answer:** 208  
**Concept:** Write allocation, conflict misses and dirty eviction.

The A and B blocks both map to cache line 0. The first iteration misses on A, B and A: three block fills. Each later iteration begins with an A hit, then misses on B and A: two fills each. Total fills are 3+3×2=9, transferring 144 bytes. Every B write dirties its block, and the following A read evicts it: four write-backs, transferring 64 bytes. Total 144+64=208.

**Common misconception:** A store miss with write allocation reads the block before modifying it; a dirty eviction adds a separate transfer.

## Q37

**Correct answer:** D  
**Concept:** Division, candidate domains and vacuous truth.

With no required courses, every Student identifier satisfies QI's universal condition, giving {1,2}. QII considers only identifiers appearing in Enrollment, namely {1}; each vacuously covers all required courses. D is correct. A treats a universal over an empty set as false; B incorrectly narrows QI's domain; C adds identifier 2 to the division's specified candidate domain.

**Common misconception:** Equivalent-looking universal queries can differ because their candidate tuple domains differ.

## Q38

**Correct answer:** A, B, D  
**Concept:** SQL aggregate and NULL semantics.

A has COUNT(*)=3, COUNT(amount)=2 and SUM=30, satisfying both predicates. B has counts 2 and 0, but SUM is NULL and NULL>10 is UNKNOWN, so it is excluded. C has equal counts and is excluded. Thus one row (A,30) remains: A,B true and C false. Replacing COUNT(amount) with COUNT(*) makes the strict inequality false in every group, proving D.

**Common misconception:** SUM of an all-NULL group is NULL, not zero, and HAVING retains only TRUE.

## Q39

**Correct answer:** B  
**Concept:** Bayesian updating of a hidden Bernoulli source.

The likelihoods of exactly two successes are 3(1/4)²(3/4)=9/64 and 3(1/2)³=24/64. Multiplying by priors gives relative weights 9 and 48, so posterior probabilities are 3/19 and 16/19. The predictive success probability is (3/19)(1/4)+(16/19)(1/2)=35/76. A ignores the posterior mixture; C is the posterior probability of source I rather than a trial success; D is not the posterior-weighted value.

**Common misconception:** Trials are independent conditional on the hidden source, not necessarily unconditionally.

## Q40

**Correct answer:** 1.75  
**Concept:** Short-circuit control flow and expected work.

P is always evaluated. Q is evaluated only if P is true, probability 1/2. R is evaluated only if P is true and Q false, probability 1/4. By adding indicator expectations, the mean is 1+1/2+1/4=1.75.

**Common misconception:** The last predicate is not reached merely because one of the earlier predicates is false; its exact path condition matters.

## Q41

**Correct answer:** 38  
**Concept:** Two-stack queue operation accounting.

There are ten enqueue pushes and eight dequeue pops. The first dequeue transfers six items from I to O. After six total dequeues O is empty. Before the seventh dequeue, I contains 7,8,9,10, so four more items transfer. Ten transfers each require one pop and one push, contributing twenty operations. Total 10+8+20=38.

**Common misconception:** Transfers occur only when the output stack is empty, not on every dequeue or enqueue.

## Q42

**Correct answer:** A, C, D  
**Concept:** Divisor lattices as products of chains.

Write 60=2²×3×5. Divisors correspond to exponent vectors in {0,1,2}×{0,1}×{0,1}, with meet and join given by coordinatewise minimum and maximum. This is a lattice and is distributive, proving A,D. A complemented vector must choose either zero or the full exponent in each coordinate, giving 2³=8: C is true. A divisor with 2-exponent one, such as 2, has no complement, so B is false.

**Common misconception:** Distributive does not imply that every element is complemented; a three-element chain is not Boolean.

## Q43

**Correct answer:** C  
**Concept:** Limits of the unweighted interval greedy rule.

Earliest finish chooses A then C, then E rather than F because E starts earlier in the finish-time tie. Its weight is 12. For the optimum, the best compatible predecessor totals at A,B,C,D,E,F are 4,5,8,10,12,13. In particular B,D,F attain 13. Thus C gives (12,13). A misses the better weighted solution; B attributes it to the greedy rule; D miscounts the greedy choices.

**Common misconception:** Maximizing the number of compatible intervals does not maximize their total weight.

## Q44

**Correct answer:** B  
**Concept:** Signed fixed-point multiplication and ties-to-even.

0xE6 represents −26/16=−1.625, and 0x1C represents 28/16=1.75. Their product is −2.84375, exactly halfway between −45/16 and −46/16. The even retained integer is −46, giving −2.875 and byte 256−46=210=0xD2. A is the odd tie neighbour; C loses the sign; D rounds to an unrelated representable value.

**Common misconception:** Ties-to-even uses the retained integer's low bit, including for negative values; it is not simply rounding toward zero.

## Q45

**Correct answer:** 1096  
**Concept:** Layer-specific headers and IPv4 fragmentation.

The IP payload is 1020 bytes, including the TCP header. The first fragment can carry floor((600−20)/8)×8=576 bytes; the second carries 444. Their IP lengths are 596 and 464. Each adds 18 link bytes, so total transmission is 596+464+36=1096. TCP's header is not duplicated in each fragment.

**Common misconception:** IP fragmentation copies IP headers, not the transport header contained inside the fragmented payload.

## Q46

**Correct answer:** C  
**Concept:** Common subexpressions with changing variable versions.

Share x*y with y*x, and share their identical sums with z. After x=x+1, x has a new value, so the later multiplication and sum cannot be shared with the earlier ones. Required operations: two multiplications, one initial sum with z, one increment, one final sum with z. Thus (2,3). A incorrectly shares across the definition of x; B omits the increment; D fails to merge the initial commutative products.

**Common misconception:** Equal variable names do not guarantee equal expression values across assignments.

## Q47

**Correct answer:** -2  
**Concept:** LU elimination and back substitution.

Eliminate using multipliers 2 and 4 in column one, then multiplier 3 in column two. U has rows (2,1,1),(0,1,1),(0,0,2). The transformed right side is (4,2,8). Back substitution gives x3=4, x2=2−4=−2, and x1=(4−x2−x3)/2=1. Direct substitution gives (4,10,30), checking the result.

**Common misconception:** Row operations must be applied to the right-hand side as well as the coefficient matrix.

## Q48

**Correct answer:** A, B, D  
**Concept:** Ordered parse trees and language versus grammar ambiguity.

Let c_n count trees with n a-leaves. c_1=1 and c_n=Σ(c_i c_(n−i)), giving c_2=1,c_3=2,c_4=5,c_5=14. Every tree has exactly one leftmost derivation, so A,B hold. A tree also has a rightmost derivation, but that is not a new tree; C is false. The generated language is a+, a regular language, so D is true.

**Common misconception:** An ambiguous context-free grammar can generate a regular language.

## Q49

**Correct answer:** A, D  
**Concept:** Composite foreign keys and three-valued CHECK evaluation.

A skips the foreign-key check because one component is NULL, and qty=5 satisfies CHECK. B skips the foreign-key check but fails qty>0. C has both key components non-NULL, so the missing parent (9,9) rejects it despite the UNKNOWN check. D finds parent (1,2), and NULL qty produces UNKNOWN rather than FALSE, so it succeeds.

**Common misconception:** A nullable CHECK is not equivalent to requiring its expression to be TRUE; NOT NULL is a separate constraint.

## Q50

**Correct answer:** 5  
**Concept:** Height bounds for full binary trees.

Height h allows at most 2^h leaves, so h≥3. A longest path of h edges in a full tree requires at least h+1 leaves, so h≤7. All intermediate values occur. Heights 3,4,5,6,7 can use root child subtrees with leaf counts (4,4),(1,7),(1,7),(1,7),(1,7), choosing the seven-leaf subtree heights 3,4,5,6 for the last four cases. More generally a full tree of height h can attain every leaf count from h+1 through 2^h by expanding leaves below its height bound. Therefore all five integers 3–7 are possible.

**Common misconception:** Full means zero or two children; it does not require all leaves at the same depth.

## Q51

**Correct answer:** 19  
**Concept:** Counting constrained compositions.

If there are k two-unit moves, there are 8−2k one-unit moves. The two-unit moves must occupy distinct gaps before, between or after those one-unit moves. Their number is C(9−2k,k). For k=0,1,2,3 the counts are 1,7,10,1; k=4 is impossible. Total 19. This also follows from a two-state dynamic program tracking whether the previous move was two units.

**Common misconception:** Ordered moves cannot be counted by merely choosing how many moves of each size occur; adjacency also restricts placement.

## Q52

**Correct answer:** 40  
**Concept:** BST insertion partial orders.

Root 3 must be first. The left subtree contains 1,2 and either insertion order gives height one. The right subtree contains 4,5,6; to fit within total height two, its root must be 5, followed by 4,6 in either order. Interleave the two left-subtree insertions with the three right-subtree insertions in C(5,2)=10 ways. Count 2×2×10=40.

**Common misconception:** Interleaving operations on opposite BST subtrees does not change either subtree's shape.

## Q53

**Correct answer:** 9  
**Concept:** Stack nondeterminism with prefix feasibility.

Seven a symbols push seven Xs. Five b symbols must pop seven, so exactly two b transitions must pop two symbols and three must pop one. Without prefix restrictions there are C(5,2)=10 choices. Before the first two b symbols, only three pushes have occurred; choosing both those b transitions as double pops is impossible. Every other choice is feasible: the first pop has at least two available symbols, the first two together use at most three, and the four later pushes supply all remaining demand. Answer 10−1=9.

**Common misconception:** Final push/pop balance is necessary but insufficient; every prefix must have enough stack symbols.

## Q54

**Correct answer:** 8  
**Concept:** Store-and-forward pipelining and packet-size optimization.

Let s=8(4000/n+100)/10⁶ seconds be transmission time on either slow link. The middle link takes s/2. The first packet arrives after 2.5s. Subsequent packets arrive every s because the slow links are the bottlenecks, giving T=(n+1.5)s.

Ignoring a positive constant factor, minimize (n+1.5)(4000/n+100)=4150+100n+6000/n. The continuous minimum is at n=√60, between 7 and 8. The function decreases before that point and increases after. Comparing 7 and 8 gives 100(8−7)+6000(1/8−1/7)<0, so 8 is the integer optimum. It divides 4000 and is therefore permitted. Its total time is 45.6 ms.

**Common misconception:** Smaller packets improve pipelining but increase total header overhead; neither one huge packet nor arbitrarily many small packets is automatically optimal.

## Q55

**Correct answer:** A, B, D  
**Concept:** Repeated rounding and grouping.

In [8,16), four significant binary bits give spacing 1. Thus 8.5 is a midpoint between 8 and 9 and rounds to even significand 8. Every sequential addition returns to 8, proving A and disproving C. Real arithmetic gives 8+16×0.5=16, proving B. Adding 2 four times gives exactly representable 10,12,14,16, proving D.

**Common misconception:** A small representable addend can disappear when added to a larger representable number.

## Q56

**Correct answer:** A, B, C  
**Concept:** Counting versus binary semaphore event accumulation.

Counting V calls create two permits, and fair scheduling lets both P calls complete: A true, D false. With the binary version, if both V calls occur before a P, their effect collapses to value 1; the consumer prints once then blocks, proving B. Interleaving V,P,V,P preserves both wakeups and prints twice, proving C.

**Common misconception:** A binary semaphore cannot necessarily count multiple notifications that arrive before they are consumed.

## Q57

**Correct answer:** 4  
**Concept:** Interrupt batching throughput and latency.

Complete batches arrive every 2k microseconds. To avoid increasing backlog, processing time 8+k must not exceed 2k, giving k≥8. From the first word to the kth word takes 2(k−1) microseconds; add processing time to obtain latency 2(k−1)+8+k=3k+6. Requiring at most 40 gives k≤11 for integer k. The choices are 8,9,10,11: four.

**Common misconception:** Throughput compares batch intervals, while the first word's latency includes waiting for the rest of its batch.

## Q58

**Correct answer:** A, C, D  
**Concept:** CRC error-polynomial divisibility.

Modulo G, x³=x+1. Successive reductions give x⁴=x²+x, x⁵=x²+x+1, x⁶=x²+1 and x⁷=1. Thus x⁷+1 has zero remainder (A), while x⁶+1 has remainder x² (B false). A single-bit error is x^k; a polynomial with nonzero constant term and degree three cannot divide a monomial, proving C. A burst of length at most three is x^kB(x) with nonzero B of degree at most two. Since G is coprime to x, divisibility would require G to divide B, impossible by degree; D holds.

**Common misconception:** CRC guarantees depend on error structure, not just the number of flipped bits.

## Q59

**Correct answer:** A, B, D  
**Concept:** Safety test after tentative allocation.

Initially only P2's need fits (1,1). Its completion releases (1,1), giving (2,2), after which P0 and P1 can finish in either order: exactly two sequences, proving A.

Granting P0 (1,0) leaves available (0,1) and needs (0,2),(2,0),(1,1). None fits, so B is true. Granting P1 (1,0) leaves available (0,1) and needs (1,2),(1,0),(1,1); none fits, so C is false. Granting P2 (1,0) leaves its need (0,1), which fits. It then releases its enlarged allocation (2,1), yielding (2,2), and both other processes can finish. D is true.

**Common misconception:** A request fitting currently available resources need not preserve a safe completion order.

## Q60

**Correct answer:** A, B, D  
**Concept:** Absolute-value integration and parameter inequalities.

Split at x=t: I(t)=t²/2+(1−t)²/2=(t−1/2)²+1/4. The minimum and its unique location prove A. Symmetry gives I(1−t)=I(t), so their sum is at least 1/2, proving B. Integration gives ∫(t²−t+1/2)dt=1/3, not 1/2, refuting C. The last inequality becomes (t−1/2)²≤1/16, hence t∈[1/4,3/4], proving D.

**Common misconception:** Integrating an absolute value requires determining where the inner expression changes sign.

## Q61

**Correct answer:** B  
**Concept:** Right quotient of a language.

Appending k zeros changes counts from (n0,n1) to (n0+k,n1). Equality requires k=n1−n0, which exists as a nonnegative integer exactly when n0≤n1. B is correct. A excludes strings fixable by appending zeros; C reverses the inequality; D wrongly includes w=0, which cannot be balanced by more zeros.

**Common misconception:** The suffix alphabet restricts which count imbalances can be repaired.

## Q62

**Correct answer:** 4  
**Concept:** Monotone self-dual Boolean functions.

Monotonicity and self-duality force f(000)=0 and f(111)=1. Let the values at singleton inputs 100,010,001 be a,b,c. Self-duality fixes the complementary doubleton values as 1−a,1−b,1−c. If two singleton values were 1, monotonicity into a doubleton complementary to the other singleton would contradict self-duality. Thus at most one of a,b,c is 1. All four choices (none or exactly one) satisfy the remaining monotonicity constraints. They give majority and the three coordinate functions x,y,z.

**Common misconception:** Choosing arbitrary values for complementary input pairs enforces self-duality but not monotonicity.

## Q63

**Correct answer:** 4.33  
**Concept:** Round-robin queue order and waiting time.

The CPU intervals are A:0–2, B:2–4, C:4–6, A:6–8, B:8–10, A:10–11. At time 2, C joins before A is requeued, so the order is B,C,A. Completion times are A=11,B=10,C=6. Waiting times are completion−arrival−burst: 6,5,2. Mean 13/3=4.333…, rounded to 4.33.

**Common misconception:** Arrival ordering at a quantum boundary can change later response and completion times.

## Q64

**Correct answer:** C  
**Concept:** Recursion-tree cost with a nonuniform nested loop.

For each i, there are i iterations of j and Θ(log i+1) iterations of k. Summing gives Θ(n² log n), using the i values from n/2 through n for a matching lower bound. The recurrence is T(n)=2T(n/2)+Θ(n² log n). At successive recursion depths the quadratic factor drops geometrically after accounting for the number of subproblems, so total cost remains Θ(n² log n). A loses a loop factor; B loses the k loop's logarithm; D adds an unnecessary logarithm for recursion depth despite the geometric decrease.

**Common misconception:** Multiplying root work by recursion depth is incorrect when per-level work decreases geometrically.

## Q65

**Correct answer:** B, D  
**Concept:** Loop fixed points and zero-iteration paths.

At the header, the entry edge carries x=1 and the back edge x=2; the analysis joins them as not constant, so A is false. The assignment establishes x=2 immediately after itself, proving B. The loop may execute zero times, leaving final y=1, so C is false. A do-while executes the assignment at least once and never changes x afterwards, eliminating y=1 and proving D.

**Common misconception:** A fact established by a loop body need not hold after a loop that can execute zero times.

