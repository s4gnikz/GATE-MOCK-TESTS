# Worked Solutions — Mock Test 057

## Q1

**Correct answer:** B

“Had the survey included” is inversion of a past counterfactual condition. Its unreal past consequence is “would have been,” B. A uses an incompatible future perfect; C describes an awkward progressive state rather than the completed past consequence; D does not supply the required conditional consequence.

## Q2

**Correct answer:** 19

**Concept:** Weighted subgroup percentages.

Remote part-timers form 0.60×0.25=0.15 of all employees. Other part-timers form 0.40×0.10=0.04. Together they are 0.19, or 19%.

**Common misconception:** Adding subgroup percentages without weighting their group sizes.

## Q3

**Correct answer:** C

**Concept:** Exclusive truth conditions.

If the key is in drawer 1, both P and Q are true. In drawer 2, both are false. In drawer 3, P is false and Q true, so exactly one holds. C alone satisfies the premises; A,B fail and D incorrectly includes them.

**Common misconception:** Reading “exactly one” as “at least one”.

## Q4

**Correct answer:** 20

The first half-turn maps(3,4) to(−1,−4), and the second maps that to(1,8). The displacement is(−2,4), with squared length4+16=20. Half-turns about different centres do not cancel: their composition is a translation.

## Q5

**Correct answer:** C

Concept: scope of survey evidence. The volunteers reported a result, but self-selection can affect representativeness; C preserves that distinction. A generalizes to every resident, B assumes away selection bias, and D asserts dishonesty without evidence. A limitation on generalization does not invalidate the observations themselves.

## Q6

**Correct answer:** 18

Arrange B,B,C in three distinct orders. Each has four gaps around/between its letters. Put the two identical A's in two distinct gaps to avoid adjacency: choose(4,2)=6 choices. Total3×6=18. Selecting distinct gaps prevents AA without distinguishing the two A copies.

## Q7

**Correct answer:** 47.73 (range 47.725–47.735)

Concept: changing mixture weights. Old combined percentage=100·91/110=82.72727…. New combined percentage=100·35/100=35. Difference=47.72727… percentage points, rounded to 47.73; range 47.725–47.735. A improves from 90% to 95%, B from 10% to 20%, yet the new mix gives much greater weight to B. Averaging the two centre percentages would ignore candidate counts.

## Q8

**Correct answer:** 16.8284 (accepted range 16.82835–16.82845)

Reflection of the removed triangle produces one triangular notch with base from(1,0) to(3,0) and apex(2,1). The original perimeter16 loses the base length2 and gains two sides of length sqrt2. Thus P=14+2sqrt2≈16.828427. The shared fold line inside the removed notch does not become an exposed edge.

## Q9

**Correct answer:** C

Concept: inconsistent cyclic evidence and an independent constraint. If each cyclic log entry in turn is the sole false one, the possible chronological orders are R,S,P,Q; S,P,Q,R; P,Q,R,S; Q,R,S,P. The reliable R-before-P record retains only R,S,P,Q and Q,R,S,P. Both place S before P, making C necessary. A and B hold only in the second retained order, not the first. D contradicts the reliable record. One cannot discard an arbitrary log entry without checking the other three together.

## Q10

**Correct answer:** 0.4286 (accepted range 0.42855–0.42865)

There are4²−3²=7 ordered outcomes with maximum4. An even sum requires both entries even; among even values{2,4}, the pairs with at least one4 are(2,4),(4,2),(4,4), three outcomes. Conditional probability3/7≈0.4286. Do not count only unordered pairs because doubles and unequal pairs have different multiplicities.

## Q11

**Correct answer:** 8

**Concept:** Complements in an interval of a subset lattice.

Both X and Y must contain 1 and 2. Each of 3,4,5 must be in exactly one of X,Y: neither would violate the union requirement, while both would violate the intersection requirement. The independent choices give 2³=8 ordered pairs.

**Common misconception:** Dividing by two even though pairs are ordered.

## Q12

**Correct answer:** B, C

A store through q may modify the object read through p. If p=q and its old value is4, x=5 while y=10, proving C and disproving A. Proven distinct objects prevent this store from changing *p, so B is true. D ignores aliasing and is false. Availability of an expression depends on memory effects, not just matching source text.

## Q13

**Correct answer:** A, B

The two zeros compare equal but have distinct signs; reciprocal division can yield positive versus negative infinity, proving A,B and disproving C. Infinity is outside the finite representable values, so D is false. Numeric equality need not imply bitwise equality.

## Q14

**Correct answer:** 1
**Concept:** Cache expiry rather than sliding expiration.

The initial entry expires at 120. Requests at 50 and 119 hit and do not change this. The request at 121 refreshes it until 241; the request at 200 then hits. Exactly one of these requests causes an upstream fetch.

**Common misconception:** A TTL is not automatically restarted on each cache hit.

## Q15

**Correct answer:** D

Substitute z=y: F=xy+(NOT x)y=y(x+NOT x)=y. Thus D is correct. A depends on an unrelated selector, B complements the required value, and C changes with x. When a multiplexer's two data inputs agree, its selector cannot affect its output.

## Q16

**Correct answer:** 2

At the first character, >> matches two characters; >>= does not match because the third character is >. The remaining >= is one token. Total2. Maximal munch is applied anew at each current position.

## Q17

**Correct answer:** A, C

Each spanning tree has n−1 edges, so its new weight is three times its old weight plus 7(n−1). Strict comparisons and uniqueness are preserved: A,C. Paths can have different edge counts, so B need not hold. D ignores both scaling and the number of edges. The shortcut is to identify equal cardinality of all candidate trees.

## Q18

**Correct answer:** 1.2
**Concept:** Conditioning independent Poisson counts on their sum.

The conditional distribution is Binomial(3,2/(2+3)). This follows directly by dividing P(X=k,Y=3−k) by P(X+Y=3), producing C(3,k)(2/5)^k(3/5)^(3−k). The conditional mean is 3×2/5=1.2.

**Common misconception:** Conditioning on the total changes X's Poisson distribution to a binomial distribution.

## Q19

**Correct answer:** 12
**Concept:** Aliased physical mappings.

The distinct frame numbers are 7,2,9, only three frames. Their total physical storage is 3×4=12 KiB. Two virtual mappings of frame 7 do not allocate two copies of it.

**Common misconception:** Virtual-page count can exceed distinct mapped physical-frame count.

## Q20

**Correct answer:** B, D

Concept: true versus name dependences. Renaming separates an earlier reader from a later writer using the same architectural name (WAR), and separates different writers (WAW), so B and D. A's consumer still needs its producer's actual value, and C depends on the branch outcome, so neither is removed merely by register names. Renaming is not value prediction.

## Q21

**Correct answer:** A, B

**Concept:** Reliability above a datagram service.

Transport can track missing bytes, retransmit and reorder received bytes, giving A and B. It cannot prevent every physical error (C), and simultaneous application endpoints still need identification (D).

**Common misconception:** Equating recovery from lower-layer errors with prevention of those errors.

## Q22

**Correct answer:** A, C

**Concept:** Recognizability of complementary languages.

Interleave one step of each recognizer. Exactly one language contains the input, so one simulation eventually accepts; that determines membership and yields a decider. Thus A and C hold. A decidable language need not be regular, refuting B. A recognizer can still loop on nonmembers even when another decider exists, refuting D.

**Common misconception:** Confusing existence of a decider with termination of every recognizer.

## Q23

**Correct answer:** 50 (exact)
**Concept:** B+ deletion and separator removal.

Deleting 40 leaves [30], below the two-key minimum. Merge it into left sibling [10,20] to form [10,20,30]. The remaining right leaf is [50,60], so the root now separates these two leaves with 50. Separator 30 is removed, not retained as a third leaf boundary.

**Common misconception:** Leaf merging changes parent separators even when the root itself remains valid.

## Q24

**Correct answer:** 64

**Concept:** Bit patterns versus maximum value.

Six unsigned bits encode 2⁶=64 values, from zero to 63 inclusive. The question asks the count, not the greatest value.

**Common misconception:** Answering 63 by confusing maximum value with number of values.

## Q25

**Correct answer:** B

B rechecks the predicate while holding the mutex after every wakeup. A fails on a spurious wakeup or when another thread consumes the condition first. C races with changes to ready. D can prevent another process from acquiring the mutex to make ready true. A wakeup is a reason to recheck, not proof of the predicate.

## Q26

**Correct answer:** 2

**Concept:** Heap insertion path.

The new 1 occupies index 7, whose parent at index 3 contains 3. Swap once, then compare with the root 2 and swap again. Two exchanges suffice and produce root 1.

**Common misconception:** Comparing with adjacent array entries rather than parent indices.

## Q27

**Correct answer:** 0.3466 (range 0.34655–0.34665)

Concept: substitution in integration. Let u=1+x², du=2x dx. The integral is (1/2)∫₁² du/u=(ln 2)/2=0.34657359…. Round to 0.3466; accepted range 0.34655–0.34665. The factor 1/2 comes from differentiating x².

## Q28

**Correct answer:** C

**Concept:** Segment-bound checking before translation.

Valid offsets are 0–99, but 120 is outside that interval, so C holds. A adds the base before disregarding the bounds violation; B clamps the address without authorization; D ignores both base and validity.

**Common misconception:** Assuming every base-plus-offset calculation is a valid address.

## Q29

**Correct answer:** B

Concept: TLB address-space separation. Without tags, a matching virtual page can retrieve the previous process's frame. Flushing the relevant entries prevents this, B. A ignores different page tables; C destroys data unnecessarily; D denies the point of a cached translation, since a hit does not necessarily walk the page table. A virtual page number is meaningful within an address space.

## Q30

**Correct answer:** A, B, D
**Concept:** Regular-language closure.

Reverse a finite automaton's edges and exchange start/final roles using nondeterminism for reversal (A). Complement a complete DFA's accepting set for B. Concatenation can be implemented by an ε-NFA connecting copies, proving D. C fails with L=Σ* and a nonregular CFL: their intersection is that nonregular CFL.

**Common misconception:** Intersection with a language from a larger class need not remain regular.

## Q31

**Correct answer:** 15
**Concept:** Static storage across recursive and successive calls.

During f(2), the three local a values are 1,2,3, yielding x=6. The static k remains 3. During f(1), the values are 4,5, yielding y=9. The printed sum is 15. Each invocation's local a retains its own value while k is shared across calls.

**Common misconception:** A static local is initialized once, not once per invocation or once per top-level call.

## Q32

**Correct answer:** 5

**Concept:** Reconstructing raw second moments when removing an observation.

The original sum is50. Population variance8 implies the sum of squares is5(8+10²)=540. Removing14 leaves sum36 and sum of squares344 for four observations, with mean9. The new variance is344/4−9²=86−81=5.

**Misconception:** Subtracting the removed squared deviation while retaining the old mean.

## Q33

**Correct answer:** A, B

**Concept:** Right inverses throughout a monoid.

For a, choose b with ab=e. Choose c with bc=e. Associativity gives a=a(bc)=(ab)c=c, hence ba=bc=e. Thus every a has a two-sided inverse, establishing A and the group property B. Groups need not commute (C false), and inverses must satisfy the equations rather than being arbitrary (D false, as any nontrivial group illustrates).

**Common misconception:** Assuming one-sided inverses remain one-sided when the inverse-existence condition applies to every element.

## Q34

**Correct answer:** 7

Concept: B+ internal-node separators. Six ordered separators partition the search domain into seven child intervals, so k+1=7 pointers. This is an internal node, not a leaf's record-pointer count.

## Q35

**Correct answer:** B

**Concept:** One-past pointers versus dereferencing.

p=a+3 may be formed, but not dereferenced. Moving back one gives a+2, whose value is seven, so B is valid. A and D access one-past storage; C goes farther out of the permitted array-pointer range and dereferences it.

**Common misconception:** Treating permission to form a one-past pointer as permission to access an element there.

## Q36

**Correct answer:** A, C

Base strings a,b are odd palindromes, and recursive productions add the same symbol at both ends, preserving that property, proving A. No production removes the central base symbol, refuting B. A palindrome equals its reversal, proving C. Both a and b are generated but their concatenation ab is not, refuting D. Recursive symmetry does not imply closure under concatenation.

## Q37

**Correct answer:** A, C

**Concept:** Compiler Design — Parsing

FIRST(aSbS)={a} and FOLLOW(S)={b,$}. Therefore the epsilon alternative occupies lookaheads b and $, while the other alternative occupies a. There is no LL(1) conflict, proving A and also establishing unambiguity, so B is false.

The LR(0) initial state contains S->.aSbS and S->. (the completed epsilon item). LR(0) would reduce by epsilon on every lookahead while also shifting a, causing a shift/reduce conflict; D is false. In the SLR construction, epsilon reductions occur only on FOLLOW(S)={b,$}. States where an S is expected have the same a-shift versus epsilon-reduce distinction; their reductions do not conflict. The state with S->aS.bS only shifts b, and the completed nonempty production occupies a separate state. Thus the SLR table is conflict-free and C is true.

- **A:** True: FIRST and FOLLOW sets have disjoint lookahead sets, so the grammar is LL(1).
- **B:** False: every LL(1) grammar is unambiguous.
- **C:** True: in the SLR parser, reductions are restricted to FOLLOW(S), eliminating the shift/reduce conflict on terminal a.
- **D:** False: LR(0) produces a shift/reduce conflict in the initial state between shifting on a and reducing S -> epsilon.

**Common misconception:** An LR(0) conflict caused by an epsilon reduction may disappear when reductions are restricted by FOLLOW sets.

## Q38

**Correct answer:** B
**Concept:** Expected distinct blocks via indicators.

For each of ten blocks, a random record request misses that block with probability 9/10. All ten requests miss it with probability (9/10)¹⁰, so its probability of being read at least once is 1−(9/10)¹⁰. Sum ten such indicators to obtain B. A ignores repeated blocks. C counts distinct records rather than blocks. D is only the probability that one specified block is never requested.

**Common misconception:** Linearity of expectation does not require the block-hit indicators to be independent.

## Q39

**Correct answer:** C
**Concept:** Shared open-file offsets after dup.

fd1 and fd2 share an open-file description and offset; fd3 does not. The first reads advance the shared offset to 3 and fd3's offset to 1. Seeking fd2 to 1 also sets fd1's offset to 1. Its final two-byte read returns bc. A ignores the seek; B resets to zero; D starts at offset two.

**Common misconception:** Descriptor identity is different from the identity of the underlying open-file description.

## Q40

**Correct answer:** B

**Concept:** Databases — Tuple calculus

The biconditional requires the employee's completed-project set to equal, rather than merely contain, the department's required-project set. Department A requires {p,q}. Employee u has an extra r and fails; v has exactly {p,q} and passes. Department B requires {q}, exactly w's set, so w passes. Department C requires the empty set, but z has completed r, so z fails. Thus E={v,w}. The universal statement for C does not become automatically true: Required(C,t) is always false, so Done(z,t) must also always be false.

- **A:** False: u has an extra completed project r and violates the reverse implication.
- **B:** True: v and w alone have exactly the required sets.
- **C:** False: z has a nonempty completion set for a department with no required projects.
- **D:** False: both u and z violate set equality.

**Common misconception:** Relational division tests containment; a universal biconditional tests exact set equality, including the empty-set case.

## Q41

**Correct answer:** A, B, D
**Concept:** A decreasing distance as a loop-prevention invariant.

With w(v,u)>0, d(u)=d(v)−w(v,u)<d(v), proving D; strict decrease around a directed cycle is impossible, proving A. With a zero-cost A–B link and unit-cost links from both A and B to t, both distances are 1. Each may choose the other as an equal-cost next hop, producing a cycle despite exact distances (B). This example refutes C.

**Common misconception:** Nonnegative costs suffice for shortest-distance algorithms, but strict decrease of chosen forwarding distances needs positive costs or an additional tie rule.

## Q42

**Correct answer:** 32

Descent increments the shared x three times, from 1 to 4. The base call returns 4. Each returning frame receives the current x as a and adds it to the same shared x, doubling it: 4→8→16→32. The final return is also 32. Treating x as a separate local copy per call would ignore reference semantics.

## Q43

**Correct answer:** 4

**Concept:** Cycles of a modular rotation permutation.

Repeatedly adding eight modulo twelve returns after 12/gcd(12,8)=3 positions. Each cycle has length three, so the twelve positions form four cycles. For example one is 0,8,4.

**Common misconception:** Equating the rotation amount with the number of permutation cycles.

## Q44

**Correct answer:** 5

**Concept:** Wait-for edges for lock conflicts and upgrades.

T1's X(B) waits for T2 and T3, giving two edges. T3's X(A) waits for T1 and T2, giving two more. T2's upgrade to X(A) waits for T1, not for its own shared lock, giving one more. Total five edges; no self-edge is added.

**Common misconception:** Treating a lock-upgrade request as waiting on the transaction's own compatible existing ownership.

## Q45

**Correct answer:** A, C

The only child thread is T1, while the copied mutex records a lock whose owner has no surviving child thread. With no repair or possible releaser, a wait can persist indefinitely: A,C are true. B contradicts the specified fork model. D confuses a private copied mutex with shared synchronization storage; changing the parent's copy does not unlock the child's. The conclusion depends on the explicit model, not on assuming arbitrary library calls are safe after fork.

## Q46

**Correct answer:** 9

Insertion-sort shifts count inversions. Every one of4,5,6 exceeds each later1,2,3, creating3×3=9 inversions. No inversion lies within an ascending block or involves the final7,8. Thus nine shifts occur. Counting key placements would add operations outside the requested metric.

## Q47

**Correct answer:** A, C, D
**Concept:** CRC error-polynomial divisibility.

Modulo G, x³=x+1. Successive reductions give x⁴=x²+x, x⁵=x²+x+1, x⁶=x²+1 and x⁷=1. Thus x⁷+1 has zero remainder (A), while x⁶+1 has remainder x² (B false). A single-bit error is x^k; a polynomial with nonzero constant term and degree three cannot divide a monomial, proving C. A burst of length at most three is x^kB(x) with nonzero B of degree at most two. Since G is coprime to x, divisibility would require G to divide B, impossible by degree; D holds.

**Common misconception:** CRC guarantees depend on error structure, not just the number of flipped bits.

## Q48

**Correct answer:** A, C

On an input-consuming PDA step, update the DFA with the same symbol, proving A. A PDA epsilon step changes only the PDA component and leaves the DFA state unchanged, refuting B. The finite DFA state is stored in the finite product control; the original stack suffices, proving C and refuting D. Acceptance must require the PDA's acceptance condition and an accepting DFA state after the input is consumed.

## Q49

**Correct answer:** A, C, D

The identifier is the pair, permitting the same room number under different owners, proving A and refuting B. BuildingID contributes to identification, proving C. Replacing it with another owner's identifier can duplicate an existing pair, proving D. A partial key is not a global key.

## Q50

**Correct answer:** 0.6875

For Y=10, Y.val=1/2+0/4=1/2 and Y.len=2. For Z=11, Z.val=1/2+1/4=3/4. Concatenation shifts Z's fraction right by Y.len places: X.val=1/2+(3/4)/4=11/16=0.6875. Using Z.len in this shift happens to match here but is not the stated general rule; the preceding prefix length determines placement.

## Q51

**Correct answer:** A, B

The fixed bits yield a NOT c; b,d are absent because all their combinations are covered. Thus A,B are true and C false. Specified zeros cannot be included in a valid exact SOP group, making D false.

## Q52

**Correct answer:** 300

The exact sum300 leaves low byte44 and carry1. The retained byte has its sign bit clear, so signed R=44. Therefore R+256C=44+256=300. Carry is computed from the unsigned addition; it is not the same as the signed-overflow flag.

## Q53

**Correct answer:** 4

After successive iterations, (slow,fast) is(1,2),(2,4),(3,2),(4,4). The first tested equality is at node4. Initial equality is deliberately not tested, and the meeting point need not be the cycle entrance node2.

## Q54

**Correct answer:** 4

An odd five-cycle requires three colours. Each of p and q is adjacent to every cycle vertex, so neither may use any of those three colours, establishing a four-colour lower bound. Give p and q the same fourth colour because they are nonadjacent; this attains four. The two universal-to-cycle vertices do not require distinct extra colours.

## Q55

**Correct answer:** 3

h1(22)=0 and h2(22)=3. Probes visit0,3,6; the first two are occupied and6 is empty. Count includes that successful third probe. Occupied slots1 and5 are not on this prefix of the probe sequence.

## Q56

**Correct answer:** 42

All arrangements number6!/(2!2!2!)=90. With AA treated as a block there are5!/(2!2!)=30 arrangements; likewise30 with BB together. With both blocks, there are4!/2!=12. Inclusion–exclusion gives90−30−30+12=42. Each repeated-letter pair is indistinguishable internally; no extra factor2 is used for its block.

## Q57

**Correct answer:** A, B, D
**Concept:** Rounding-induced nonassociativity.

In [16,32), the spacing is 2. The exact 16+1=17 is midway between 16 and 18, and ties-to-even selects 16, so (a+b)+c=0 (A). For the other grouping, 1−16=−15 is exactly representable with four significant bits (1111₂), and 16−15=1 is exact (B). Real arithmetic gives 1 (D). The unequal computed results refute C without any overflow.

**Common misconception:** Finite-precision rounding alone breaks associativity, even with unbounded exponents.

## Q58

**Correct answer:** 9

If k length-two tiles are used, there are6−2k unit tiles. These unit tiles create7−2k gaps, including both ends; put at most one long tile in each gap. Thus k=0 gives1, k=1 gives C(5,1)=5, k=2 gives C(3,2)=3, and k=3 is impossible. Total1+5+3=9. Counting unrestricted tilings would wrongly allow adjacent length-two tiles.

## Q59

**Correct answer:** 2

Entering V, execution must remember both where V returns inside U and where U returns inside Main. These are two distinct live return addresses. Overwriting the sole link register on U's call to V loses the older one unless another location preserves it. The question asks the required simultaneous information, not the number of registers already supplied.

## Q60

**Correct answer:** 15

The selection tree has16 data leaves and every internal node is a two-input multiplexer. A full binary tree has one fewer internal node than leaves, giving15. Equivalently8+4+2+1=15 across the levels.

## Q61

**Correct answer:** 0.375

Six ordered pairs have absolute difference1: (0,1),(1,0),(1,2),(2,1),(2,3),(3,2). Out of16 equally likely pairs, probability6/16=0.375. Either station may have the larger counter.

## Q62

**Correct answer:** 7

f and g reference the same closure and captured x, so their first calls return1 and2. h has its own environment and returns1. The final f call advances the first environment to3. Sum1+2+1+3=7. Copying a closure reference is not creating a fresh capture environment.

## Q63

**Correct answer:** -0.3333 (range -0.33335–-0.33325)

**Concept:** Integral constraints and quadratic extrema.

The constraints give a+b+1=0 and a/3+b/2+1=0. Substitution gives a=3, b=−4. Therefore f(x)=3x²−4x+1 has its minimum at x=2/3 inside the interval, with value −1/3. The endpoints give 1 and 0, both larger. Rounded answer −0.3333; accepted range −0.33335–−0.33325.

**Common misconception:** Checking only endpoints or solving the integral equation without the endpoint condition.

## Q64

**Correct answer:** B

**Concept:** Aggregate resizing cost.

The n appends themselves cost n. Resizing copies 1,2,4,…,n/2 elements, summing to n−1. Total cost is 2n−1, B. A counts resize events rather than copied elements; C incorrectly charges logarithmic copying for each append; D exceeds the exact count.

**Common misconception:** Multiplying the largest single append cost by the number of appends.

## Q65

**Correct answer:** A, B

After reading u, its DFA state can reach an original accepting state iff some suffix v completes uv into L. Marking precisely these reachable-to-accept states therefore recognizes Pref(L), proving B and regularity(A). For L={ab}, prefix a is not in L, disproving C. If L is empty, no suffix completes even epsilon, disproving D.

