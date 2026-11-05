# Worked Solutions — Mock Test 028

## Q1

**Correct answer:** 8

Modulo2, the recurrence starts1,0 and cycles1,0,1 with period3. Each three-term group has two odd terms. Twelve terms contain four such groups, hence8 odd terms. Actual rapidly growing term values are unnecessary; parity obeys the same recurrence modulo2.

## Q2

**Correct answer:** 48

The midpoint quadrilateral has perpendicular diagonals equal to the rectangle's sides12 and8. Its area is(1/2)·12·8=48. Equivalently, the four removed corner triangles total half the original area96. Joining midpoints does not leave a rectangle with sides6 and4.

## Q3

**Correct answer:** B

With neither/nor joining unlike-number subjects, agreement follows the nearer subject, here the plural authors, so “are willing” is appropriate. A and D are singular. C is singular and also cannot combine as “has willing.” Read the complete predicate as well as the subject number.

## Q4

**Correct answer:** 10

If the mass is M, initial value is50M. Removal subtracts5·50=250 and replacement adds5·40=200. Thus45M=50M−50, giving M=10. The removed uniform mixture has its existing average cost, not the cost of just one constituent.

## Q5

**Correct answer:** 2

For x=1 the statements have truth pattern true,false,false. For2 it is true,true,false. For3 it is false,false,true, and for4 false,true,false. Exactly two are true only at2. Evaluating the conjunction of all three would answer a different condition.

## Q6

**Correct answer:** 5

Undo the90-degree counterclockwise rotation by mapping final coordinates(u,v) to(v,−u), obtaining(−2,3). Reflection across x=1 maps original(x,y) to(2−x,y), so2−x=−2 and y=3. The original point is(4,3), at distance sqrt(16+9)=5. Undo composed transformations in reverse order.

## Q7

**Correct answer:** A, B

The observed group difference establishes association in this sample, proving A. Optional enrolment and absent baseline information leave alternative explanations, so B is true. C claims individual causal improvements unsupported by the data. D invents equality of prior achievement. A group mean comparison alone cannot remove selection effects.

## Q8

**Correct answer:** 32

There are5!=120 circular arrangements. For each specified pair forced adjacent, contract it to a block with2 internal orders:2·4!=48. For two designated adjacent pairs there are2²·3!=24 arrangements; for all three,2³·2!=16. Inclusion–exclusion gives120−3·48+3·24−16=32. Reflections remain distinct, so no additional division by2 is allowed.

## Q9

**Correct answer:** 72

Let b be the number of B packages, from0 to5. For each, use a=floor((300−60b)/40). The resulting(a,b) and registration totals are(7,0):70,(6,1):72,(4,2):64,(3,3):66,(1,4):58,(0,5):60. The maximum72 uses six A and one B. Better registrations per unit cost for A alone does not remove the effect of the leftover budget.

## Q10

**Correct answer:** 16.8284 (accepted range 16.82835–16.82845)

Reflection of the removed triangle produces one triangular notch with base from(1,0) to(3,0) and apex(2,1). The original perimeter16 loses the base length2 and gains two sides of length sqrt2. Thus P=14+2sqrt2≈16.828427. The shared fold line inside the removed notch does not become an exposed edge.

## Q11

**Correct answer:** 3

A length-three word can consist of three a blocks, giving aaa, or one a block and one ba block in either order, giving aba and baa. These three are distinct and exhaust the length compositions. The expression has no lone b block.

## Q12

**Correct answer:** 4

Label nodes by first-visit indices0,1,2,3,4,5,6, with6 linking back to3. After iterations1,2,3,4 the slow pointer is at1,2,3,4 while the fast pointer is at2,4,6,4. The first equality after advancement is iteration4. Starting equality at the head is explicitly excluded, and cycle length alone does not in general determine the first meeting without considering the prefix.

## Q13

**Correct answer:** 96

The /25 route covers128 addresses, from.128 through.255. The more-specific /27 route removes32 addresses,.160 through.191, from B's traffic. Thus128−32=96 addresses go to B. These routing counts include network/broadcast-looking addresses because the question counts address matches, not assignable hosts.

## Q14

**Correct answer:** B

Lexical scope identifies Outer regardless of which procedure calls Inner, so the static link in B locates the intended activation. A follows call history to Caller. C follows recency without lexical meaning. D cannot by itself locate a non-global activation's local x. Dynamic and static nesting need not coincide.

## Q15

**Correct answer:** A, C

Both mappings translate to the same frame and offset, so writes alias shared storage, proving A,C. Different virtual page numbers can map to one frame, refuting B. Without copy-on-write there is no stated fresh-frame allocation, refuting D. Virtual address distinction does not imply physical storage distinction.

## Q16

**Correct answer:** 5

Let T(n) count ordered parse trees with n leaves. T(1)=1, and the root split gives T(n)=sum over i=1..n−1 of T(i)T(n−i). Hence T(2)=1,T(3)=2,T(4)=1·2+1·1+2·1=5. Different orders of expanding nodes in the same tree are not additional parse trees.

## Q17

**Correct answer:** 2

Blocks40 and41 form one contiguous extent;90 forms another. A single extent would include unrequested blocks42–89, contrary to the question. Logical consecutiveness does not guarantee physical consecutiveness.

## Q18

**Correct answer:** 0

For HH,HT,TH,TT the(X,Y) pairs are(2,0),(1,1),(1,1),(0,0), each with probability1/4. Thus E[X]=1,E[Y]=1/2,E[XY]=1/2 and covariance is1/2−1·1/2=0. These variables are nevertheless dependent: Y=1 forces X=1. Zero covariance does not establish independence.

## Q19

**Correct answer:** A, C

If p is null, the first comparison is false and short-circuit evaluation bypasses the dereference, proving A,C. Eager evaluation in B could introduce an invalid null dereference. D reverses the required order. Correct intermediate code must preserve which expressions are evaluated, not just a truth-table identity on safe operands.

## Q20

**Correct answer:** 1

Greedy chooses4,1,1, using three coins. An optimum is3,3, using two; one coin cannot make6. The difference is1. A denomination system need not support the greedy-choice property.

## Q21

**Correct answer:** A, C

T2 reads T1's uncommitted write, so A is true; it commits before that writer aborts, proving C. Recoverability requires a reader to commit only after the writer it depends on commits, so B is false. Strictness disallows reading the uncommitted written value, refuting D. Commit order matters in addition to the read/write order.

## Q22

**Correct answer:** 2

The old word has5+8=13 bits; the new one has3+8=11. Savings are2 bits. Six combinations fit in3 bits, but the unchanged address field must still be counted in both widths.

## Q23

**Correct answer:** -4

011111 represents stored integer31. Incrementing modulo64 gives100000, the six-bit signed value−32. Scaling by1/8 yields−4. The arithmetic is wrapping, not saturating at the largest positive representable value.

## Q24

**Correct answer:** 6

The floor values are0,1,1,2 for elements1,2,3,4. Equivalence classes therefore have sizes1,2,1. Each contributes its size squared in ordered related pairs, giving1+4+1=6. The middle class includes both off-diagonal orders as well as its two reflexive pairs.

## Q25

**Correct answer:** B, C

A finite format has only finitely many representable numbers, whereas a real interval contains infinitely many inputs; rounding maps many distinct inputs to the same value, proving B and refuting A. Finite precision and binary fractional representation matter even within exponent range, proving C and refuting D. Being in range avoids one problem, not every rounding error.

## Q26

**Correct answer:** 0

Associativity and y XOR y=0 give F=x XOR(y XOR y) XOR z=x XOR z. No assignment differs, so the count is0. The two uses of y are the same signal, not independent inputs.

## Q27

**Correct answer:** B, D

The specified acceptance rule asks for at least one accepting branch, so D is true. A rejecting or infinite alternative does not erase a finite accepting branch, proving B and refuting A. C ignores the explicit full-input-consumption requirement. Nondeterministic acceptance is not a requirement that every branch terminate successfully.

## Q28

**Correct answer:** 25

A rank-one matrix can be written uvᵀ. Its trace is vᵀu=5. Squaring gives A²=u(vᵀu)vᵀ=5A, so trace(A²)=5·5=25. The identity depends on rank one; squaring the trace is not valid for arbitrary matrices.

## Q29

**Correct answer:** 2

r1(x) before w2(x), and also w1(x) before w2(x), create edge T1→T2. r2(x) before w1(x) creates T2→T1. Repeated conflicts in one direction count only once, giving2 directed edges. The two reads alone do not conflict.

## Q30

**Correct answer:** B

The mean value theorem gives c1 in(0,1) with f'(c1)=2 and c2 in(1,2) with f'(c2)=−2. Apply it to f' on[c1,c2]: some point has f''=(−2−2)/(c2−c1)<0, proving B. A is stronger than this existence claim. To refute C,D, add t·x(x−1)(x−2) to the parabola−2x²+4x: it preserves all three function values but changes f'(1) when t≠0. To vary f''(1), add t·x(x−1)²(x−2), again preserving the values. Such perturbations can also make f'' positive elsewhere, refuting A. Pointwise values do not determine all derivatives.

## Q31

**Correct answer:** B, C

At w=2 the update sets dp[2]=3. At w=4 it reads that updated value and produces6, reusing the only item. Thus B is true and A,D false. Descending order reads the preceding item's states at smaller capacities, so no updated dp[w−2] is reused during this pass, proving C. Loop direction encodes whether repeated item use is permitted.

## Q32

**Correct answer:** 0.4

Inclusion–exclusion gives P(A∩B)=0.4+0.5−0.7=0.2. Divide by P(B)=0.5 to get P(A|B)=0.4. Conditional probability uses the intersection as numerator, not the union.

## Q33

**Correct answer:** 8

Two chips in parallel give each16-bit word. Four such banks provide1024/256=4 times the depth. Therefore2·4=8 chips are required. Expanding width alone would still leave only256 addresses.

## Q34

**Correct answer:** 4

To output4 first, push1,2,3,4 and pop4. The remaining older stack values must emerge as3,2,1. Value5 can be pushed and popped before any of these, between either consecutive pair, or after all three. This gives four outputs:45321,43521,43251,43215. Once5 is pushed it must pop before the older entries, so it has exactly four insertion positions rather than arbitrary freedom.

## Q35

**Correct answer:** A, C

With a common public address and common external endpoint, distinct public source ports distinguish the two active mappings, proving A. The stored mapping sends replies to the appropriate private endpoint, proving C. B incorrectly requires the private addresses to coincide. D confuses translation state with changing application payloads. Demultiplexing follows transport/address metadata under the stated model.

## Q36

**Correct answer:** 177.5

For sample140, S becomes75+35=110 and D becomes5+20=25, using old S=100. For sample100, S becomes82.5+25=107.5 and D becomes12.5+5=17.5, using old S=110. Timeout is107.5+4·17.5=177.5ms. Substituting the newly updated S inside the deviation formula would implement a different estimator.

## Q37

**Correct answer:** A, B, D

If the complement were regular, complementing it again would make L regular, a contradiction; A is true. The union in B equalsΣ*, which is regular. C is false: for L={a^n b^n}, intersection with the infinite regular language a* is just{ε}. For D, if deleting a finite set made L regular, adding back the finitely many removed words would make L regular by closure under finite union; this is impossible. Nonregularity is not preserved under every intersection.

## Q38

**Correct answer:** 4

Each binary projection contains every one of the four possible bit pairs. Their join therefore permits all2³=8 triples. Only four were originally present, giving4 spurious additional triples. Pairwise relationships cannot encode the original parity-like ternary restriction by themselves.

## Q39

**Correct answer:** A, C

Both calls pass the same starting buffer address. The first places A,B at positions0,1; the second places C,D,E at0,1,2, overwriting earlier bytes. A is true and B false. Using buf+n retains the first n bytes and writes subsequent bytes after them, proving C. D is false because network order does not prevent an application from choosing an incorrect destination address. Successful total byte counts alone do not prove correct assembly.

## Q40

**Correct answer:** A, B, C

The ideals are empty,{a},{b},{a,b},{a,b,c},{a,b,c,d}, so A is true. Unions and intersections of downward-closed sets remain downward-closed and are respectively least upper and greatest lower bounds, proving B,C. These set operations satisfy the distributive laws, refuting D. Incomparability in the underlying poset does not destroy distributivity of its ideal lattice.

## Q41

**Correct answer:** 1.25

Elimination gives pivots d1=2 and d(i)=2−1/d(i−1). Hence d2=3/2,d3=4/3,d4=5/4=1.25. The subdiagonal multiplier at each step is−1 divided by the preceding pivot; subtracting its product with the superdiagonal reduces the next diagonal. Using the original diagonal2 at every step would miss propagated elimination effects.

## Q42

**Correct answer:** A, B

The regular pumping lemma requires0<|y| and |xy|≤p, so1≤d≤p, proving A. Pumping to two copies adds d to p², and0<d≤p<2p+1 is smaller than the next-square gap. Thus B is true and the pumped word is outside L for every permitted decomposition. C violates the nonempty requirement. D is false since p²≥p for p≥1. The gap argument handles all decompositions, not one chosen substring.

## Q43

**Correct answer:** 6

The minimum value-equivalent cover ab+(NOT a)c has a potential static-1 hazard when a changes while b=c=1: one product may fall before the other rises. Adding the consensus product bc holds the output high during that transition. The three required adjacent one-pairs are covered by ab, (NOT a)c, and bc. None can be covered by a one-literal implicant because every single-literal cube includes a zero of F. Each of these pair-cover requirements forces its corresponding two-literal prime implicant; all three together use6 literals. Logical equivalence alone does not guarantee hazard freedom under unequal delays.

## Q44

**Correct answer:** A, C, D

For false flag both blocks end with x=0,y=1, proving A. For true flag the original produces x=1,y=2 while the proposal produces x=1,y=1, refuting B. The conditional assignment invalidates an unconditional x=0 assumption, proving C. If y is unobservable and only the stated operations occur, both blocks leave the same x for either flag, proving D. Correct optimization depends on both control flow and which results are observable.

## Q45

**Correct answer:** 203

The first four issues occur at0,1,2,3 and complete at100,101,102,103. Each completion frees a slot for another issue in that same cycle. Those four new requests finish at200,201,202,203. The last completion is203. Unlimited parallelism would wrongly allow all eight misses to issue by7; fully serial service would ignore the four outstanding slots.

## Q46

**Correct answer:** 8

The subtree rooted at2 contains2,4,5,6, four vertices. Vertex7 originally has depth2. After attaching2 below7, its depth changes from1 to3, an increase2; every descendant of2 increases by the same2. The other vertices do not move, so total increase is4·2=8. Reattaching a subtree changes all its descendant depths, not just its root's.

## Q47

**Correct answer:** B, C, D

Each column appears in two rows, so no row is essential; A is false. Each row omits one column, proving B. Every pair of rows covers all three columns, giving exactly the three minimum covers PQ,PR,QR, proving C. After deleting any one row, the remaining pair still covers all columns, proving D. Wide coverage does not make an implicant essential; a uniquely covered required column would.

## Q48

**Correct answer:** 0.0833 (accepted range 0.08325–0.08335)

Integrate the identity on[0,1]. By substitution u=1−x, both integrals on the left equal I=∫f. Therefore2I=∫0¹(x−x²)dx=1/2−1/3=1/6, giving I=1/12≈0.083333. The individual function need not be uniquely specified for its integral to be determined.

## Q49

**Correct answer:** B, C

If an A value occurs in R but not in S, any corresponding R tuple survives R−S, proving B. A fails for R={(1,x)}, S={(1,y)} with x≠y: the left side is{1}, the right empty. Every tuple in R∩S supplies an A value present in both projections, proving C. The same counterexample has empty intersection but common projected value1, refuting D. Projection can erase the distinctions on which intersection and difference depend.

## Q50

**Correct answer:** 5

0,2 miss into set0;1 misses into set1. The next0 hits and makes0 most recent in set0. Access4 misses and evicts2. Access2 then misses and evicts0. The final1 hits in its unaffected set. There are5 misses. LRU order is maintained separately for each set.

## Q51

**Correct answer:** 2

The original median is(3+7)/2=5. Replacing one3 by7 or a larger number leaves at least four observations at least7 and yields middle pair7,7, so median7 is attainable. It cannot exceed7: five fixed observations are at most7, so both middle positions remain at most7. The maximum increase is2. An arbitrarily large replacement need not make the median arbitrarily large.

## Q52

**Correct answer:** A, C

Totality makes each simulation finish, proving C. A finite-index accepted input in the enumeration is therefore reached after finitely many terminating earlier simulations, proving A. If none is accepted, there are always more inputs to examine; no finite rejected prefix establishes emptiness, so B is false. The promise gives no finite maximum relevant length, refuting D. Total decision procedures may still recognize languages whose emptiness cannot be settled by this enumeration.

## Q53

**Correct answer:** 2

For ab=00, exactly one input is1 iff c=1, so D0=c. For ab=01 and10, c must be0, so D1=D2=NOT c. For ab=11 the count already exceeds one, so D3=0. Exactly2 data inputs use NOT c. The select bits contribute to the population count before the remaining input is considered.

## Q54

**Correct answer:** 3

Before rotation,20 is depth0;10,30 depth1;25,40 depth2;22,27 depth3. After rotation,30 is depth0;20,40 depth1;10,25 depth2;22,27 depth3. Exactly25,22,27 retain their depths, giving3. The middle subtree moves from being30's left subtree to20's right, and the root shift compensates for that reassignment.

## Q55

**Correct answer:** 24

There are three merge levels for eight elements. Every level writes all eight elements once across its buffers, so total writes are3·8=24. Equivalently W(n)=2W(n/2)+n with W(1)=0. This is cumulative work, not simultaneous buffer space.

## Q56

**Correct answer:** A, C

Every nonroot node has a smaller ancestor, so the second-smallest can only be a root child, proving A. The distinct-key min-heap property makes every parent strictly smaller, proving C. The sorted array[1,2,3,4,5,6,7] is a heap with third-smallest at index3, refuting B. The valid heap[1,3,2,7,6,5,4] is not globally sorted, refuting D. Heap order constrains ancestors, not arbitrary array positions.

## Q57

**Correct answer:** B, C

The original components are{a,b,c},{d,e},{f}, linked in that order. There is no path back from d to c, refuting A, and f has no outgoing edge, refuting D. Adding f→b closes a directed cycle among all components, proving B. Reversing all edges reverses mutual paths but preserves their existence in both directions, proving C. One-way reachability between components is insufficient for strong connectivity.

## Q58

**Correct answer:** A, C

The duplicated and inherited descriptors refer to the same open file description under the stated semantics. Its offset is shared, so A,C are true and B false. Closing one descriptor drops one reference; other open references remain valid, refuting D. Descriptor-table entries and open file descriptions are distinct levels of state.

## Q59

**Correct answer:** 6

After the first fork there are two independent copies of x=1. Each increments its own copy to2. The parent's second fork creates a third process inheriting2; the original child also retains2. Three processes each print2, summing to6. Incrementing private state does not update another process's copy.

## Q60

**Correct answer:** B, D

The first header visit has x=0; a later visit can have1,2,and higher values. A single constant0 cannot soundly describe them all, so A is false and B true. Zero or multiple iterations refute C. All reachable values are nonnegative in mathematical integer arithmetic, so a range analysis could retain x≥0, proving D. Losing a precise constant does not imply that all useful invariants are lost.

## Q61

**Correct answer:** 1

For(1,1), y=1 has outgoing second values1 and2, including2≠x, so reject. For(1,2), R(2,2) supplies z=2≠1, so reject. For(2,2), the only z is2=x, so accept. For(3,1), both z=1,2 differ from3, so reject. Exactly one tuple survives. The inner lookup is on the outer y value, not on its x.

## Q62

**Correct answer:** A, C

With a full buffer and no consumer progress, a further blocking write can wait indefinitely, proving A. An open read endpoint is merely a reference, not an action consuming data, so B is false. Closing all readers changes the endpoint condition, rather than leaving an ordinary full pipe with a potential reader, proving C. A finite buffer cannot absorb unlimited data without draining, so D is false. Capacity can postpone blocking but cannot replace consumer progress.

## Q63

**Correct answer:** 45

Without coalescing20 interrupts cost20·3=60 microseconds. Groups of four give5 interrupts and15 microseconds. Savings are60−15=45. The computation concerns CPU handling time, not device completion latency or the waiting delay introduced by batching.

## Q64

**Correct answer:** A, C

Adding e to a spanning tree creates a cycle. Because e crosses the cut, the cycle must cross back via another edge, proving C. If an MST omitted e, replacing that other crossing edge by the uniquely lighter e would reduce total weight, proving A. Lighter edges may exist within one side of the cut, refuting B. Equal-weight alternatives elsewhere may give multiple MSTs, refuting D. A forced edge does not force every other edge.

## Q65

**Correct answer:** 2

Working backward, after d's assignment only d is live. After the reassignment of a, b and new a are live. After c's assignment, b and c are live; old a is dead because it is overwritten before another use. After b's input, a and b are live; after a's input, only a is live. The maximum is2. Counting every defined variable would retain obsolete values and overestimate liveness.
