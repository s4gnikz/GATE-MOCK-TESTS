# Worked Solutions — Mock Test 098

## Q1

**Correct answer:** B

**Concept:** General Aptitude — Vocabulary in context

1. The reviewer supports the objective, so the endorsement is not withdrawn.
2. The requirement of a smaller pilot places a condition on that support. Here “qualified” means limited by reservations, rather than describing professional credentials.

- **A:** This contradicts the explicit condition.
- **B:** This captures support with a limitation.
- **C:** The context gives no information about credentials.
- **D:** Support remains; it has not been withdrawn.

**Common misconception:** A familiar word can have a contextual meaning unrelated to its usual professional use.

## Q2

**Correct answer:** 64

**Concept:** Changing logarithm bases.

Put y=log₂x. Then log₄x=y/2, so 3y/2=9 and y=6. Therefore x=2⁶=64.

**Common misconception:** Treating logarithms with different bases as equal terms.

## Q3

**Correct answer:** A, C

(3k+1)²=3(3k²+2k)+1, proving A. A finite list alone does not prove the rule for all integers, so B is false. For n=2, n²=4 has remainder1, proving C and giving a counterexample to the converse in D. A true implication need not have a true converse.

## Q4

**Correct answer:** 1

**Concept:** Fixed cells under a half-turn.

A cell at row r,column c maps to row 4−r,column 6−c, numbering from one. Equality requires r=2,c=3, the unique central cell.

**Common misconception:** Counting the full central row or column rather than the cell satisfying both coordinate conditions.

## Q5

**Correct answer:** 4

16!=16·15!, so the ratio contributes exactly the four factors of2 in16=2^4. Thus the exponent increases by4. Computing the entire factorial is unnecessary.

## Q6

**Correct answer:** 4.5

BC is horizontal, so the altitude from A is x=0. Side AC has slope(0−8)/(6−0)=−4/3; the perpendicular altitude from B has slope3/4 and equation y=(3/4)(x+6). At x=0 it gives y=4.5. Altitudes are perpendicular to opposite sides and are not generally angle bisectors or medians.

## Q7

**Correct answer:** B

B attaches both participial actions to the engineer, who also recommends closure. A makes “cracks” the grammatical subject of having inspected. C incorrectly attributes the recommendation to cracks and misattaches inspection. D explicitly reverses the inspector and inspected object. The introductory modifier must attach to the intended actor.

## Q8

**Correct answer:** 25

A 12.5% profit on cost ₹80 requires an average selling price of ₹90. If the discounted price is s, (3/5)×100+(2/5)s=90, giving s=75. Relative to the listed ₹100, that is a 25% discount. Profit percentage is measured against cost, whereas the requested discount is measured against the listed selling price.

## Q9

**Correct answer:** A, C

Concept: exhaustive constraint satisfaction. For prize pairs AB,AC,AD,BC,BD,CD, the numbers of true labels are respectively 2,4,2,3,1,1. Thus only AB and AD are feasible. Both include A and exclude C, making A and C necessary. B fails for AD; D fails for AD as well. Necessary conclusions must hold in every feasible placement.

## Q10

**Correct answer:** 16

The quarter-turn about the square's centre permutes its vertices, leaving their x-coordinate sum4. Translation adds3 to each of four x-coordinates, adding12. Total16. Tracking the invariant set avoids computing four individual rotated coordinates.

## Q11

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

## Q12

**Correct answer:** -24

**Concept:** Determinant from triangular factors.

det(L)=1 and det(U)=2×(−3)×4=−24. With no permutation sign to include, det(A)=−24.

**Common misconception:** Adding pivots rather than multiplying them.

## Q13

**Correct answer:** 3288

**Concept:** Final-page internal fragmentation.

Three 4096-byte pages are needed, allocating 12288 bytes. Unused bytes in the last page are 12288−9000=3288. Earlier pages are full because the region begins on a boundary.

**Common misconception:** Counting whole unused pages as part of this allocation.

## Q14

**Correct answer:** 3

Integrating the identity gives integral(f(x))+integral(f(1−x))=6. Substitution u=1−x makes the two integrals equal, so each is3. No pointwise symmetry of f itself is required.

## Q15

**Correct answer:** 1000

Each1100-bit packet occupies one millisecond and carries1000 payload bits. Hence payload throughput is1000 bits/ms. The link's raw rate includes headers and is not all useful payload.

## Q16

**Correct answer:** 7

The pumped block consists only of a's and its length k is1,2,or3. Pumping with exponent i changes the a-count to3+(i−1)k. Equating this to9 gives i=1+6/k, respectively7,4,3. The largest required exponent is7. The exponent may depend on the decomposition; one need not use the same exponent for every legal block. This finite instance illustrates the pumping contradiction mechanism rather than constituting a full proof for every pumping length.

## Q17

**Correct answer:** A

Concept: transaction atomicity. Atomicity requires the transfer's updates to take effect together or not at all. Persisting only the debit violates A. B and C are not transaction requirements. D mistakes partial success for an atomic outcome. Merely retaining a durable partial update is not sufficient.

## Q18

**Correct answer:** 5

**Concept:** Recovering a missing observation before sorting.

The total must be 5×6=30. Known observations sum to 25, so x=5. The sorted list is 2,4,5,8,11, whose middle entry is 5.

**Common misconception:** Using the mean as the median without reconstructing the data.

## Q19

**Correct answer:** 4

**Concept:** Binary-search decision depth.

The balanced successful-search tree for fifteen entries has levels with 1,2,4,8 entries. A deepest entry needs four comparisons. The midpoint choice yields these exact sizes.

**Common misconception:** Using floor(log₂15)=3 without accounting for the first comparison level.

## Q20

**Correct answer:** 120 (exact)

**Concept:** Computer Organization and Architecture — Instruction sets and addressing modes

1. The displacement is -6, not 250. The post-instruction PC is 104.
2. The intermediate address is 104+4(-6)=80.
3. Indirection reads M[80]=120, so the operand address is 120. M[120]=7 is the value loaded, not the address asked for.

**Common misconception:** PC base, scale, indirection and loaded value are distinct stages.

## Q21

**Correct answer:** 12
**Concept:** An inessential Boolean variable.

Each of the six qualifying four-variable assignments permits either value of the fifth variable. The count doubles to 12.

**Common misconception:** Independence from an input means both values replicate each output-table entry.

## Q22

**Correct answer:** 8

p++ advances by one entire three-int row. Thus (*p)[1]=5 and p[-1][2]=3, summing to8. Pointer arithmetic scales by the pointed-to row type.

## Q23

**Correct answer:** B
**Concept:** Recursive execution order.

visit(1) prints 1. visit(2) calls visit(1), prints 2, then calls visit(0), yielding 1,2. visit(4) therefore prints 1,2 from its first call, then 4, then 1 from visit(1). B is correct. A moves the right subtree before the root; C is preorder; D assumes every value from 1 through 4 is visited.

**Common misconception:** The recursive arguments determine the visited values; they are not necessarily all integers below the initial argument.

## Q24

**Correct answer:** 6

**Concept:** Homomorphisms from cyclic groups.

The image a of the generator 1 determines the homomorphism. It must satisfy 12a=0 mod 18, equivalently a=0 mod 3. The six images 0,3,6,9,12,15 all work. In general the count is gcd(12,18)=6.

**Common misconception:** Allowing arbitrary generator images without respecting its order.

## Q25

**Correct answer:** B

**Concept:** B+ leaf splitting and separator copies.

The stipulated leaves are [4,7,9] and [12,15]. The right leaf's smallest key is 12, so B is correct. A is the left leaf's largest key, C is internal to the left leaf, and D is the right leaf's largest key. None matches the given separator policy.

**Common misconception:** Applying a different split convention despite an explicit rule.

## Q26

**Correct answer:** A, C

Simulating at most k transitions decides both bounded questions, with the initial-state acceptance test included for C. The computation is finite even when M would run forever. B is the unrestricted halting problem; D is the general Turing-machine language-emptiness problem. Both are undecidable. A finite bound changes the decision problem fundamentally.

## Q27

**Correct answer:** A, C

T2 reads T1's uncommitted write, so A is true; it commits before that writer aborts, proving C. Recoverability requires a reader to commit only after the writer it depends on commits, so B is false. Strictness disallows reading the uncommitted written value, refuting D. Commit order matters in addition to the read/write order.

## Q28

**Correct answer:** B

**Concept:** Synchronous binary counting.

All right-hand sides use the old state. The trajectory is 011→100→101→110→111→000. B is therefore correct. A is the state after four edges, C after six, and D after two.

**Common misconception:** Updating bits sequentially within a single clock edge.

## Q29

**Correct answer:** 4
**Concept:** Cartesian product and selection.

Initially there are 3×2=6 tuples. The A=2 condition removes its two pairings with x,y. Four remain, corresponding to the two remaining A values times two B values.

**Common misconception:** Removing one value from a component domain may remove multiple tuples.

## Q30

**Correct answer:** D

The shift yields floor(−3.5)=−4, while division truncates to−3. Difference−4−(−3)=−1, option D. A treats both rounding directions as identical; B reverses subtraction; C is unrelated to the two resulting integers.

## Q31

**Correct answer:** D

Concept: preserving probe-chain semantics. A tombstone can be remembered as a potential insertion location, but searching must continue for an existing equal key. D does this. A creates a duplicate; B and C confuse a formerly occupied slot with a never-used stopping slot. Deletion must not break searches for displaced entries.

## Q32

**Correct answer:** 3
**Concept:** Antichains and a chain-cover upper bound.

The set {4,5,6} is an antichain, establishing a lower bound of three. Partition the entire poset into chains {1,2,4}, {3,6}, and {5}. Any antichain contains at most one member of each chain, giving an upper bound of three. The maximum is exactly three.

**Common misconception:** Exhibiting a large antichain alone does not prove it is largest; an upper bound is also needed.

## Q33

**Correct answer:** 20 (exact)
**Concept:** Array views and address strides.

C[1][2] is B[2][1], at 1000+4(2×4+1)=1036. C[0][1] is B[1][0], at 1000+4(1×4)=1016. Difference: 20 bytes. A transposed view changes index interpretation, not physical storage.

**Common misconception:** A transpose view is not necessarily a contiguous row-major array in its own index order.

## Q34

**Correct answer:** 2

**Concept:** Boolean dependence on a variable.

The two product terms cannot both be1. At a=1, f=b; at a=0, f=c. Flipping a changes the output precisely when b differs from c: assignments(0,1) and(1,0). Thus there are2 assignments.

**Misconception:** Counting both initial values of a even though the question asks for assignments to(b,c).

## Q35

**Correct answer:** A

A's inherited information cannot depend on a right sibling C under the left-to-right restriction, so A violates it. B,C use information from a left sibling; D uses the parent's inherited information. Those are permitted dependency directions, subject to the rest of the definition being consistent.

## Q36

**Correct answer:** 35
**Concept:** Microinstruction field widths.

There are 16 control bits, log₂8=3 condition-selection bits, and two log₂256=8-bit addresses. Total width is 16+3+8+8=35. Both outcomes have explicit address fields, so no fall-through address saving applies.

**Common misconception:** Encoding one branch condition does not also encode its target addresses.

## Q37

**Correct answer:** A, C

Concept: locking conditions. Unlock-S(A) starts the shrinking phase; later lock-S(C) violates basic 2PL (A true, B false). X(B) is released after commit, meeting the specifically defined exclusive-lock retention condition (C true). Retaining X(B) does not remove the new shared-lock acquisition, so D is false. The question separates strictness of release from the full strict-2PL protocol.

## Q38

**Correct answer:** A, C
**Concept:** Directory links versus open-file references.

An open descriptor keeps the unlinked file available until the reference is released, proving A and refuting B. Removed pathnames no longer resolve to it, proving C. Open descriptors are not directory hard links; the hard-link count is zero, refuting D.

**Common misconception:** Removing a name is not necessarily the same as immediately destroying the referenced data.

## Q39

**Correct answer:** A

**Concept:** Compiler Design — Runtime environments

C is declared directly inside A, so every C activation reaches the same active A through its static link. Its references to x therefore name A's x, initially 4, even when a B activation containing its own x is C's caller. B(2) first calls B(1), which first calls B(0). B(0) calls C: A.x becomes 5 and 5 is returned. B(1) next calls C, obtaining 6, and returns 5+6=11. B(2) next calls C, obtaining 7, and returns 11+7=18. Main prints 18. The recursive B locals would matter under dynamic lookup, but not under the specified lexical lookup.

- **A:** True: the calls to C update the single enclosing A.x to 5,6,7 and their returned values sum to 18.
- **B:** False: 101+102+103=306 uses each calling B activation as the variable environment, which would be dynamic rather than static scoping.
- **C:** False: 15 assumes all three C calls start from a fresh copy of A.x=4; the enclosing activation persists and is modified.
- **D:** False: 21+22+23=66 uses Main.x, but the nearer enclosing declaration in A shadows it.

**Common misconception:** A static link follows lexical nesting, so recursion in a sibling procedure does not create fresh copies of the sibling's enclosing variables.

## Q40

**Correct answer:** 7
**Concept:** State transition tracing of a feedback shift register.

Applying all next-state equations simultaneously gives 001→011→111→110→101→010→100→001. No earlier state equals the initial state. The first return is after seven edges.

**Common misconception:** Next-state equations all use the old bits; updating bits sequentially computes a different machine.

## Q41

**Correct answer:** 1

**Concept:** Polynomial long division over GF(2).

Starting with 1101000, XOR shifted 1011 successively to eliminate leading ones:

```text
1101000 XOR 1011000 = 0110000
0110000 XOR 0101100 = 0011100
0011100 XOR 0010110 = 0001010
0001010 XOR 0001011 = 0000001
```

The remainder is 001, unsigned value one. Subtraction is XOR, without borrows.

**Common misconception:** Performing ordinary integer division instead of polynomial division.

## Q42

**Correct answer:** A, C
**Concept:** Eliminating nongenerating and unreachable grammar symbols.

B has no terminating alternative: every derivation from B retains a B. Thus S→AB cannot produce a terminal string. All successful derivations use S→C, which generates exactly c*, proving A. Only S and C occur in successful derivations, proving C. Although A is separately reachable and generating, its only reachable context includes the nonterminating B; it is not useful, refuting B. D generates a terminal string but is unreachable from S, refuting D.

**Common misconception:** Reachability and generation tested in the unpruned grammar are not independently sufficient; remove nongenerating productions before recomputing reachability.

## Q43

**Correct answer:** 13

Separate open calls create separate open-file descriptions and offsets. p advances to4 then6; q is independently set to7. Their sum is13. This differs from dup, which shares an open-file description and offset.

## Q44

**Correct answer:** A, C, D

The original successor's value occupies p's position and its node is bypassed, giving the value sequence in A. A successor is needed to perform that operation, proving C. The actual removed node is the successor, not p; external references can distinguish this, so D is true and B false. Value-sequence equivalence is weaker than identity preservation.

## Q45

**Correct answer:** 20

Among all5!=120 permutations, the six relative orders of1,2,3 occur equally often by relabelling those three elements. Exactly one is allowed, giving120/6=20. Equivalently choose their three positions in10 ways, fill them in increasing order, and arrange4,5 in two ways.

## Q46

**Correct answer:** 4

R covers0,3 and S covers1,2, so together they cover all minterms at cost2+2=4. No single implicant covers all four minterms. Since every implicant costs at least2, every cover using at least two costs at least4. Thus the exhibited cover is optimal. Selecting the largest coverage row P first would lead to a cost5 cover and miss the lower literal cost.

## Q47

**Correct answer:** 4096 (exact)
**Concept:** Partial address decoding and aliases.

Only twelve address bits reach the chip, so it contains 2¹²=4096 physical bytes. Within the selected 16 KiB window, varying the ignored two bits creates four aliases per byte, not four independent copies. For example 0x8123,0x9123,0xA123,0xB123 select the same physical byte.

**Common misconception:** The address window's size can exceed actual device storage when decoding is incomplete.

## Q48

**Correct answer:** A, B, C

For s=0, T=a and F=T=a. For s=1, T=b and F=NOT T=NOT b. This proves A. When a=b, these two outputs are complements, proving B. When a≠b, a=NOT b and they agree, proving C. With s=a=b=0, F=0, but with s=0,a=b=1, F=1 whereas s XOR a XOR b=0, refuting D. Evaluate the two selection levels in their stated order.

## Q49

**Correct answer:** 12

Three enqueues give3 pushes. Each element transfers from I to O exactly once, giving3 pops and3 pushes. Each of the three dequeues gives one pop from O. Total3+6+3=12. The second dequeue does not transfer c because b is still in O; this preserves FIFO order.

## Q50

**Correct answer:** 9
**Concept:** Exact insertion-sort comparison counting.

Inserting 1 compares against 5 once. Inserting 4 compares against 5 then 1: two comparisons. Inserting 2 compares against 5,4,1: three. Inserting 3 compares against 5,4,2: three. Total 1+2+3+3=9. Successful shifts and the final failed key comparison are both comparisons, but reaching the boundary adds no key comparison.

**Common misconception:** The number of key comparisons can exceed the number of shifts.

## Q51

**Correct answer:** A, C

An earliest-finishing interval ends no later than the first chosen interval in an optimum, leaving at least as much remaining scheduling time, proving A. Half-open endpoints allow back-to-back compatibility, proving C. Weighted objectives can prefer a later-finishing higher-value interval, so B is false. A long interval can block many short intervals, disproving D. The exchange proof relies on the equal-value cardinality objective.

## Q52

**Correct answer:** 16

At total 10, the even number of 3-parts can be zero or two. Zero gives the single all-1 composition. Two consume 6 units, leaving four 1-parts; arranging these six parts gives C(6,2)=15. Total e10=16. More generally E(x) is one half of [1/(1−x−x³)+1/(1−x+x³)], since averaging cancels compositions with an odd number of 3-parts. Ordered compositions count arrangements, not merely partitions.

## Q53

**Correct answer:** 7

Concept: basic blocks and control-flow edges. Leaders are lines 1,2,3,4,7,9, producing six blocks. Edges are 1→2; 2→3 and 2→9; 3→4 and 3→7; 4–6→2; 7–8→2. Total seven distinct block edges. Internal sequential statements within a block do not add inter-block edges.

## Q54

**Correct answer:** 5

When p=r=false, q is free: two choices. When at least one of p,r is true, q must be true: three choices for(p,r). In all cases s is uniquely their XOR. Hence2+3=5 assignments. The equivalence defining s does not double the number of choices.

## Q55

**Correct answer:** 432

Concept: collision detection timing. Frame transmission time is 512/10⁸ seconds=5.12 microseconds, allowing one-way delay 2.56 microseconds. Subtract device delay 0.4 to get cable propagation budget 2.16 microseconds. Distance=2.16·10⁻⁶·2·10⁸=432 metres. Both device delays must be included in the round trip, not added only once to it.

## Q56

**Correct answer:** 4

From r, depths are 0,1,1,2,2,2, summing8. From c, depths of c,a,d,r,b,e are 0,1,2,2,3,4, summing12. The increase is 4. Rerooting changes every distance to the chosen root, not merely the old root's depth.

## Q57

**Correct answer:** 8

The candidate distances are2+7=9 via A and5+3=8 via B. The router selects8. A neighbour's advertisement must be combined with the link cost to that neighbour.

## Q58

**Correct answer:** A, B, C

The third left-hand side is the sum of the first two, requiring t=3. The first two rows are independent, leaving one free variable when consistent. Subtracting twice the first equation from the second gives −x1+x3=0. Equivalently, solutions are (s,1−2s,s) for arbitrary real s. Thus A,B,C hold. Rank is 2, not 3, so D is false.

## Q59

**Correct answer:** 18

Bank indices are0,0,1,1,2,2,3,3. Issue cycles are respectively0,3,4,7,8,11,12,15: each consecutive same-bank pair incurs a wait until the bank is free, and switching banks still obeys one issue per cycle. The final request finishes at15+3=18. The controller cannot issue later independent requests early because requests must remain in order.

## Q60

**Correct answer:** 6

**Concept:** Grammar generation and distinct terminal strings.

Each nonempty production introduces one a and one b, so length-four strings must have two of each: there are at most choose(4,2)=6. All six are generated: aabb via a(S=ab)b(S=ε); abab via a(S=ε)b(S=ab); abba via a(S=ε)b(S=ba); and their symbol-swapped versions bbaa,baba,baab using the second production. Thus the count is six regardless of ambiguity.

**Common misconception:** Counting parse trees or assuming the balance condition alone proves all balanced strings are generated.

## Q61

**Correct answer:** A, C

Short-circuit semantics already skip f() in A,C, so replacing those expressions removes no executed side effect and preserves the constant result. In B,D, f() is evaluated first even though the final value is predetermined; replacing the whole expression would suppress its effects. Boolean algebra alone is insufficient for effectful expressions.

## Q62

**Correct answer:** A, C

Concept: nondeterministic midpoint matching. To consume abba and empty its pushed portion, push and matching lengths must both be two, proving A. The matched suffix ba is the reversal of prefix ab. A guess after one symbol cannot ignore a mismatch or extra input, so B is false. For abab the only possible balanced lengths are two and two, but suffix ab is not the reversal ba, so C is true. Nondeterministic acceptance needs one successful branch; incorrect guesses do not invalidate another accepting branch, so D fails.

## Q63

**Correct answer:** A, C, D

The owner key together with the partial key distinguishes every room, proving A. Equal room numbers in different buildings disprove B and explain D. A required, non-null foreign key checks existence of the owner; combined with the composite Room key it implements this mapping, so C is true. A partial key is unique only relative to its owner.

## Q64

**Correct answer:** 4

Two-step paths yield P={(a,c),(a,a),(b,a),(c,b),(c,c)}. Of these, only(a,c) is already in E. Therefore P−E has4 pairs. Set projection eliminates duplicate witnesses, and self-pairs are permitted when a two-edge cycle returns to the start.

## Q65

**Correct answer:** 820

(AB)C costs10×2×20+10×20×3=1000. A(BC) costs2×20×3+10×2×3=180. The saving is820. Parenthesization changes intermediate matrix dimensions while preserving the final product.

