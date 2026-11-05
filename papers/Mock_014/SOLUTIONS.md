# GATE CS 2027 — Mock 014: Worked Solutions

## Q1

**Correct answer:** C

**Concept:** Contraposition.

Certified implies tested, so untested implies not certified, C. The rejected tested samples need not be certified, refuting A and D. B reverses the first implication without justification.

**Common misconception:** Taking the converse instead of the contrapositive.

## Q2

**Correct answer:** A

**Concept:** Ordered reflections.

The first reflection sends (x,y) to (x,−y); the second swaps the coordinates, producing (−y,x), A. B gives the reverse-order composition, C is a half-turn, and D gives only the first reflection.

**Common misconception:** Assuming transformations commute.

## Q3

**Correct answer:** B

**Concept:** Different statistics describe different features.

The average improved while the largest delay increased, precisely B. A need not hold because a worse maximum exists. Such changes can coexist, refuting C, and they do not determine the median, refuting D.

**Common misconception:** Assuming a smaller mean forces every observation or every other statistic to decrease.

## Q4

**Correct answer:** 36

**Concept:** Positional constraints on permutations.

The specified books occupy one of three position pairs: (1,3),(2,4),(3,5). Orient the two books in two ways, then arrange the other three in 3! ways. Total 3×2×6=36.

**Common misconception:** Treating the specified books as adjacent when exactly one intervening book is required.

## Q5

**Correct answer:** 4.8

**Concept:** Aggregate rate.

Combined revenue is 240 and combined items 50. The rate is 240/50=4.8. Averaging the separate daily rates 4 and 6 without their item weights would be incorrect.

**Common misconception:** Averaging ratios with unequal denominators.

## Q6

**Correct answer:** 4

**Concept:** Reflecting a notch across two folds.

The triangular removal occupies one quadrant around the original centre. Unfolding reflects its diagonal cut into the other three quadrants. The four reflected diagonal segments form a square rotated relative to the paper's edges, with four sides.

**Common misconception:** Counting the fold edges as exposed hole edges after unfolding.

## Q7

**Correct answer:** A

**Concept:** Diagnosis before intervention and verification.

Record the symptom, isolate its cause, replace that component, then test the result: S,Q,R,P. B verifies before replacement, C replaces before diagnosis, and D verifies before the original fault is even recorded. A is the coherent order.

**Common misconception:** Treating replacement itself as proof that the original fault was corrected.

## Q8

**Correct answer:** 0.75

**Concept:** Conditional sampling without replacement.

There are choose(6,3)=20 equally likely selections. Four contain only red balls, leaving 16 with at least one blue. Exactly one blue occurs in choose(2,1)choose(4,2)=12 selections. The conditional probability is 12/16=0.75.

**Common misconception:** Using all twenty selections as the denominator after conditioning.

## Q9

**Correct answer:** A

**Concept:** Distinguishing brevity from superficiality.

The sentence explicitly says that required issues remain covered despite removal of repetition, supporting A. B and D contradict this distinction. C claims a necessary length relation not stated or implied.

**Common misconception:** Treating concise and cursory as synonyms in this context.

## Q10

**Correct answer:** 20

**Concept:** Combining logarithmic ratio and product.

The logarithm difference gives log₂(x/y)=2, so x=4y. From xy=64, 4y²=64 and positivity gives y=4,x=16. Their sum is 20.

**Common misconception:** Replacing a difference of logarithms by the logarithm of a difference.

## Q11

**Correct answer:** C

**Concept:** Segment-bound checking before translation.

Valid offsets are 0–99, but 120 is outside that interval, so C holds. A adds the base before disregarding the bounds violation; B clamps the address without authorization; D ignores both base and validity.

**Common misconception:** Assuming every base-plus-offset calculation is a valid address.

## Q12

**Correct answer:** 4

**Concept:** Terminal contributions per grammar expansion.

Each nonempty production adds one a and two b symbols. After n such steps the total length is 3n. Thus 3n=12 gives n=4 a symbols.

**Common misconception:** Counting nonterminals as part of the final terminal length.

## Q13

**Correct answer:** A

**Concept:** DNS record types.

AAAA records associate names with IPv6 addresses, A. Ethernet addresses, TCP sequence information and HTTP bodies belong to different mechanisms, eliminating B,C,D.

**Common misconception:** Confusing address resolution at different network layers.

## Q14

**Correct answer:** A, B

**Concept:** Reliability above a datagram service.

Transport can track missing bytes, retransmit and reorder received bytes, giving A and B. It cannot prevent every physical error (C), and simultaneous application endpoints still need identification (D).

**Common misconception:** Equating recovery from lower-layer errors with prevention of those errors.

## Q15

**Correct answer:** 1

**Concept:** Eigenvalues of a rank-one matrix.

Au=u(vᵀu) and vᵀu=2−3=−1, so −1 is an eigenvalue. The two-dimensional kernel of vᵀ is annihilated by A, yielding two zero eigenvalues. The sum of squares is (−1)²=1.

**Common misconception:** Summing squared matrix entries instead of squared eigenvalues.

## Q16

**Correct answer:** 9

**Concept:** Address width versus word width.

Selecting among 512=2⁹ microinstructions requires nine bits. The 40-bit microinstruction width determines storage per entry, not the number of address bits.

**Common misconception:** Using microinstruction width as its address width.

## Q17

**Correct answer:** A

**Concept:** Definitions along branch paths.

Each feasible branch defines the value consumed at the join, establishing A. B would make x=b even when p is true, while C and D disregard the source condition and selected values.

**Common misconception:** Treating a branch join as permission to execute both mutually exclusive assignments.

## Q18

**Correct answer:** 5

**Concept:** Decoder indexing.

101₂ is decimal five, so D5 is asserted. The one-hot output index is five, rather than the number of asserted outputs, which is one.

**Common misconception:** Confusing decoded position with Hamming weight.

## Q19

**Correct answer:** A

**Concept:** Doubly linked neighbour repair.

Bypassing X requires P's forward pointer to reach N and N's backward pointer to reach P, A. B changes the wrong directions; C retains X; D creates self-links rather than preserving the remaining chain.

**Common misconception:** Updating only the forward chain or reversing the pointer directions.

## Q20

**Correct answer:** 1

**Concept:** Edit-distance lower and upper bounds.

Substituting u for a changes cat into cut in one step. Zero edits cannot work because the strings differ. Therefore the optimum is one.

**Common misconception:** Using one deletion plus one insertion when a cheaper substitution is permitted.

## Q21

**Correct answer:** 4

**Concept:** Width expansion of memory chips.

Each chip supplies eight bits at the shared word address. Four in parallel supply 32 bits while retaining the 1024-word depth.

**Common misconception:** Expanding depth instead of width.

## Q22

**Correct answer:** A, B

**Concept:** B+ tree structural invariants.

Separators may copy leaf key values, so A holds. Balance keeps all leaves at one depth, giving B. Data entries are at leaves, refuting C; root occupancy has special exceptions, refuting D.

**Common misconception:** Importing ordinary B-tree data-placement rules unchanged into B+ trees.

## Q23

**Correct answer:** 4

**Concept:** Serialization delay.

A 1000-byte packet contains 8000 bits. At 2×10⁶ bits/s it takes 0.004 seconds, or four ms.

**Common misconception:** Dividing bytes by a bit rate without multiplying by eight.

## Q24

**Correct answer:** B

**Concept:** Translation caching versus page residency.

A TLB miss lacks a cached translation, not necessarily the data page. The resident accessible page-table entry supplies that translation without a page fault, B. A,C,D incorrectly turn a translation-cache miss into a residency or protection failure.

**Common misconception:** Equating TLB misses with page faults.

## Q25

**Correct answer:** 2

**Concept:** Global maximum from derivative sign.

f′(x)=1/x−1/2 is positive below two and negative above two. Thus x=2 gives the global maximum on x>0; f tends to −∞ at both ends of the domain.

**Common misconception:** Solving f′=0 without checking whether the stationary point is a maximum.

## Q26

**Correct answer:** 0.75

**Concept:** Total probability followed by Bayes.

P(A)=0.6×0.5+0.2×0.5=0.4. The intersection P(A∩B)=0.3, giving P(B|A)=0.3/0.4=0.75.

**Common misconception:** Reversing a conditional probability without incorporating the marginal probabilities.

## Q27

**Correct answer:** 5

**Concept:** Complement in a divisor lattice.

Since 30 has prime factors 2,3,5, a complement of 6=2×3 must supply 5 but neither 2 nor 3. Thus y=5, with gcd one and lcm thirty.

**Common misconception:** Using arithmetic subtraction instead of the lattice's meet and join.

## Q28

**Correct answer:** -24

**Concept:** Determinant from triangular factors.

det(L)=1 and det(U)=2×(−3)×4=−24. With no permutation sign to include, det(A)=−24.

**Common misconception:** Adding pivots rather than multiplying them.

## Q29

**Correct answer:** A

**Concept:** Prefix balance as well as total balance.

A closing parenthesis cannot precede its matching opening parenthesis, so every prefix must have nonnegative unmatched-open count, A. Balanced words have even length, contradicting B; nesting refutes C and can require unbounded stack height, refuting D.

**Common misconception:** Checking only equal total numbers of opening and closing parentheses.

## Q30

**Correct answer:** 4

**Concept:** Ring-counter period.

The single 1 visits four distinct positions before returning to its starting position. Therefore the first return occurs after four edges.

**Common misconception:** Assuming every four-flip-flop counter has period sixteen regardless of its transition function.

## Q31

**Correct answer:** A, B, D

**Concept:** Algebraic identities under explicit exact semantics.

Zero is the additive identity, one the multiplicative identity, and subtracting a value from itself yields zero. These establish A,B,D. C fails for any nonzero x because x×0 equals zero, not x.

**Common misconception:** Confusing a multiplicative annihilator with an identity.

## Q32

**Correct answer:** A

**Concept:** Persistence of acknowledged commits.

Durability requires committed effects to survive the specified crash model, so A is the direct violation. Atomicity concerns all-or-nothing behaviour and need not be violated if all effects are lost together, refuting B's necessity. C names the wrong property; D excludes the very failure scenario durability addresses.

**Common misconception:** Treating every recovery error as necessarily an atomicity violation.

## Q33

**Correct answer:** 16

**Concept:** Leaf partition of the original input.

Every leaf holds one input element and the recursive halves partition all sixteen elements without duplication. Thus there are sixteen leaves.

**Common misconception:** Counting levels or all calls when only leaves are requested.

## Q34

**Correct answer:** A

**Concept:** Context-free closure properties.

A new start symbol choosing either grammar proves closure under union, A. General CFL intersection, complement and set difference are not closed, so B,C,D lack the claimed guarantee. Closure under complement combined with union would also imply intersection by De Morgan, contradicting known nonclosure.

**Common misconception:** Assuming CFLs have every Boolean closure property of regular languages.

## Q35

**Correct answer:** 9

**Concept:** Postfix operand order.

Push 5 and 2, then subtraction computes left 5 minus right 2, giving 3. Push the next 3 and multiply to get 9.

**Common misconception:** Reversing the two popped operands for subtraction.

## Q36

**Correct answer:** A

**Concept:** Gaps between successive squares.

Pumping once extra gives length p²+d. It exceeds p² because d≥1, but d≤p<2p+1, so it is below (p+1)². Thus it is not a square and leaves the language, A. B reverses the inequality; C is false; D invents an alphabet restriction.

**Common misconception:** Failing to bound the pumped length between consecutive allowed lengths.

## Q37

**Correct answer:** A, C

**Concept:** Loop joins and fixed-point facts.

The initial edge carries zero while iterations can carry one,two,…, so C holds and no single constant generally describes all header visits, A. B ignores the back edge. Constant propagation does not generally determine arbitrary input-dependent loop counts, so D is false.

**Common misconception:** Propagating an initialization through a modifying loop as an invariant.

## Q38

**Correct answer:** 15.875

**Concept:** Saturating fixed-point conversion.

The largest signed eight-bit integer code is 127, and three fractional bits give real maximum 127/8=15.875. Exact 17 exceeds that range, so saturation stores 15.875.

**Common misconception:** Wrapping modulo 256 instead of applying the specified saturation rule.

## Q39

**Correct answer:** 1.5476

**Concept:** CPI improvement versus instruction-count expansion.

Old CPI is 1+0.04×40=2.6. New CPI is 1+0.01×40=1.4, but new instruction count is 1.2 times old. The time ratio is 2.6/(1.2×1.4)=65/42=1.547619…. Accepted range: 1.54755–1.54765.

**Common misconception:** Comparing CPIs without accounting for changed instruction count.

## Q40

**Correct answer:** A, B, D

**Concept:** Finite execution traces versus unbounded halting.

Simulating at most k steps decides acceptance and halting within that bound, establishing A,B. Recording the finite sequence of complete configurations permits exact repetition testing, establishing D. Unbounded halting for arbitrary M,x is undecidable, so C is false.

**Common misconception:** Treating bounded and unbounded execution questions as equally undecidable.

## Q41

**Correct answer:** 5

**Concept:** Wait-for edges for lock conflicts and upgrades.

T1's X(B) waits for T2 and T3, giving two edges. T3's X(A) waits for T1 and T2, giving two more. T2's upgrade to X(A) waits for T1, not for its own shared lock, giving one more. Total five edges; no self-edge is added.

**Common misconception:** Treating a lock-upgrade request as waiting on the transaction's own compatible existing ownership.

## Q42

**Correct answer:** B

**Concept:** Liveness kill and use sets.

Assignment defines a new x and does not use old x; its right-hand side uses y and z. Thus the transfer removes x from live-out and adds y,z, B. A conflates old and new values; C reverses uses and definitions; D treats liveness as preventing assignment.

**Common misconception:** Keeping a variable's old value live merely because its newly assigned value is needed later.

## Q43

**Correct answer:** 4

**Concept:** Spurious tuples from decomposing a ternary relationship.

Each binary projection contains all four binary pairs. Their natural join therefore contains all eight triples in {0,1}³. Only four were originally in R; the other four are spurious. The binary associations do not preserve the original parity restriction.

**Common misconception:** Assuming all pairwise projections uniquely determine an arbitrary ternary relationship.

## Q44

**Correct answer:** 0.5

**Concept:** Rounding across an exponent boundary.

With three significant bits, 7 and 8 are adjacent representable values surrounding 7.5. The exact value is halfway. Ties-to-even selects 8 (1.00₂×2³), whose retained final bit is even; either nearest endpoint has absolute error 0.5, which is the requested quantity.

**Common misconception:** Assuming fixed spacing continues unchanged beyond the exponent boundary or reporting signed rather than absolute error.

## Q45

**Correct answer:** 4

**Concept:** BFS queue constraints on discovery order.

If s enqueues a before b, a discovers c,d in either order before b discovers e. Orders are s,a,b,c,d,e and s,a,b,d,c,e. If b comes first, b discovers d,e in either order before a discovers c, giving s,b,a,d,e,c and s,b,a,e,d,c. Marking on enqueue prevents rediscovering d. Thus four distinct orders exist.

**Common misconception:** Permuting each distance layer freely despite restrictions imposed by the parent queue order.

## Q46

**Correct answer:** 0.2402

**Concept:** Substitution in a logarithmic integral.

Let u=ln(1+x), so du=dx/(1+x). The integral becomes ∫ from 0 to ln2 of u du=(ln2)²/2=0.2402265…. Accepted range: 0.24015–0.24025.

**Common misconception:** Treating the numerator logarithm and denominator independently instead of recognizing a derivative pair.

## Q47

**Correct answer:** A, C

**Concept:** Boolean absorption and redundancy.

Expanding gives x+xy+xz+yz=x+yz, proving A. Whenever F=1, either x=1 or y=z=1, so x+y+z=1; multiplying by that redundant factor preserves F, proving C. At x=0,y=z=1, F=1 while B and D are zero, refuting both.

**Common misconception:** Distributing without applying absorption, or forgetting the yz term.

## Q48

**Correct answer:** -1

**Concept:** Edge counting in a full ternary tree.

A tree with fifteen vertices has fourteen edges. If every internal node has three children, the edge count must equal three times the number of internal nodes. Fourteen is not divisible by three, so no such tree exists. The specified impossibility response is −1.

**Common misconception:** Applying a leaf formula without checking the required internal-node count is integral.

## Q49

**Correct answer:** 5

**Concept:** Linked-allocation payload capacity.

Each block provides 512−4=508 data bytes. Four blocks hold 2032 bytes, one byte short of the requested 2033. A fifth block is therefore required.

**Common misconception:** Using raw block size and overlooking per-block pointer overhead.

## Q50

**Correct answer:** 0

**Concept:** Persistent direct-mapped thrashing.

All three block numbers map to line zero. Every reference replaces the immediately preceding block, including across iteration boundaries, so none of the thirty accesses hits.

**Common misconception:** Assuming repetition across loop iterations guarantees temporal-locality hits despite mapping conflicts.

## Q51

**Correct answer:** A

**Concept:** Forked private state.

Each process starts with its own logical copy of counter=5 and increments it to six. Copy-on-write implementation details do not turn the ordinary global into shared writable state. Thus A holds; B assumes sharing, while C,D contradict the executed increment and inherited value.

**Common misconception:** Confusing initially identical contents with a shared variable.

## Q52

**Correct answer:** 1.25

**Concept:** Updating sufficient statistics.

After removal the sum is 14 and sum of squares 54. Mean is 14/4=3.5; population variance is 54/4−3.5²=13.5−12.25=1.25.

**Common misconception:** Removing six from the sum of squares instead of removing 6².

## Q53

**Correct answer:** 4

**Concept:** Orders in a direct-product group.

An element (a,b) has order lcm(ord(a),ord(b)). In Z8, exactly a=2,6 have order four. Either b=0 or b=1 in Z2 keeps the least common multiple four, giving 2×2=4. Components of order eight give order eight, and lower-order components cannot yield four here.

**Common misconception:** Multiplying component orders instead of taking their least common multiple.

## Q54

**Correct answer:** 18

**Concept:** Undetected patterns under row and column parity.

Every affected row and column must contain an even number of flipped bits. With four distinct data-bit errors, this forces the four corners of a rectangle: two chosen rows and two chosen columns. There are choose(3,2)choose(4,2)=3×6=18 such patterns. Each rectangle flips two bits in every affected row and column, so all pass parity checks.

**Common misconception:** Assuming two-dimensional parity detects every four-bit error.

## Q55

**Correct answer:** B, C

**Concept:** Lost updates under atomic individual accesses.

If both loads read zero before either store, both later store one, yielding B. If one complete increment precedes the other's load, the result is two, C. A store always writes at least one, so final zero is impossible; with only two increments no load can see two before a third increment, so three is impossible.

**Common misconception:** Treating a source-level increment as atomic despite its specified separate steps.

## Q56

**Correct answer:** 800

**Concept:** Cycle stealing as lost issue opportunities.

There are 1000/5=200 stolen cycles. Each removes exactly one otherwise productive cycle, leaving 1000−200=800 completed instructions.

**Common misconception:** Adding a second penalty beyond the one opportunity loss explicitly specified.

## Q57

**Correct answer:** A, B, D

**Concept:** Path-sensitive expression availability.

On the false branch no operand changes, so t can replace the final expression, B. On the true branch a is reset to zero and the old t may differ, so unconditional replacement is unsound, A, and C is false. This is why availability must track definitions along paths, D.

**Common misconception:** Reusing an expression because it is available on one predecessor rather than all relevant predecessors.

## Q58

**Correct answer:** 2

**Concept:** Relational division as a universal requirement.

A values 1 and 3 each pair with both x and y. Value 2 pairs only with x and fails the requirement. The division result has two tuples.

**Common misconception:** Counting any matching B value rather than requiring all values in S.

## Q59

**Correct answer:** -5

**Concept:** Depth changes under rotation.

After the left rotation, x moves down one level and y up one, cancelling their contributions. Every node in A moves down one (+4 total), every node in C moves up one (−9), and B's nodes remain at the same depth. Nodes outside the rotated subtree are unchanged. Net comparison-count change is 4−9=−5.

**Common misconception:** Moving B's nodes with y even though the rotation reattaches B beneath x at their original depth.

## Q60

**Correct answer:** 8

**Concept:** Counting spanning trees with a distinguished edge.

Without diagonal a–c, a spanning tree is obtained by deleting one of four cycle edges, giving four. With the diagonal present, b must attach through either ab or bc, and d through either ad or cd, giving 2×2=4. All trees have three unit-weight edges and are minimum. Total eight.

**Common misconception:** Counting all three-edge subsets without excluding triangles and disconnected subsets.

## Q61

**Correct answer:** 0.25

**Concept:** Exactly one transmitter.

Choose the transmitting station in four ways. Each specified one-transmitter outcome has probability (1/2)^4=1/16. Thus success probability is 4/16=1/4.

**Common misconception:** Counting a slot with two transmissions as two successes instead of a collision.

## Q62

**Correct answer:** A

**Concept:** Direction of heap-order repair.

Decreasing a key cannot make it exceed a child that was previously at least its old value. It can become smaller than its parent, requiring upward repair, A. B reverses the direction; C exaggerates the local violation; D ignores the parent relation.

**Common misconception:** Applying the same repair direction to both increasing and decreasing keys.

## Q63

**Correct answer:** 4

**Concept:** Comparing multi-hop routes.

A–B–C–D costs 1+2+1=4. The alternatives A–C–D and A–B–D cost five and six; positive-weight extra detours cannot improve them. The shortest distance is four.

**Common misconception:** Choosing the route with fewer hops rather than lower total weight.

## Q64

**Correct answer:** A, C

**Concept:** Regular-expression identities and counterexamples.

A holds because concatenating arbitrary strings of a symbols gives another string of a symbols, and every such string is already in a*. C is the identity property of ε for concatenation. B fails on ba, which is in the left language but not a*b*. D fails on a, which belongs to a*b* but not (ab)*.

**Common misconception:** Moving a star through union or concatenation as though it were an ordinary arithmetic operation.

## Q65

**Correct answer:** 12

**Concept:** Degree counts in labelled-tree encodings.

In the Prüfer correspondence for six labelled vertices, the code has length four and label i appears di−1 times. The required multiset is {1,1,2,3}. Its distinct orderings number 4!/2!=12, each corresponding to exactly one labelled tree. The degree sum is ten, as required for a six-vertex tree.

**Common misconception:** Using degree rather than degree minus one as the code multiplicity.
