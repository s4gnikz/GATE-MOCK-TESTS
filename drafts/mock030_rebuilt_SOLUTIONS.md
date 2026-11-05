# Worked Solutions — Mock Test 030

## Q1

**Correct answer:** A, C

An exempt design cannot use M. Since D does, it is not exempt, proving C. Approval requires tested or exempt, so it must be tested, proving A and refuting B. D reverses an implication: nothing states that tested designs all use M. Apply the restriction to D, not indiscriminately to all designs.

## Q2

**Correct answer:** -6

The original signed area is(4·3)/2=6. Reflection reverses orientation, multiplying signed area by−1. Rotation preserves both area and orientation, and translation changes neither. The result is−6. The magnitude alone would omit the requested orientation.

## Q3

**Correct answer:** D

Remaining places are necessary for considering a late application, so with none available it cannot be considered: D. A turns a necessary condition into sufficient acceptance and confuses consideration with acceptance. B,C add claims about timely applications not covered by the notice.
## Q4

**Correct answer:** 30

There are6!/(2!2!2!)=90 unrestricted arrangements. For each named adjacent duplicate pair, contraction gives5!/(2!2!)=30 arrangements. For each pair of such events, contraction gives4!/2!=12. All three events give3!=6. Inclusion–exclusion gives90−3·30+3·12−6=30. Duplicate letters are indistinguishable, including within contracted blocks.

## Q5

**Correct answer:** 80

The second class has60−30=30 students and42−18=24 passes. Its pass percentage is100·24/30=80. The combined70% cannot be assigned to each class separately.

## Q6

**Correct answer:** 5

Undo the second fold: the cut x=5 reflects to x=7 in the first packet. Undo the first fold: x=5 and7 reflect across x=4 to x=3 and1. The full-height cuts are therefore at1,3,5,7, dividing the rectangle into five strips. The fold lines themselves are not cuts.

## Q7

**Correct answer:** B, C

The recorded event order is alarm, entry, inspection start, discovery. B follows from that order; A,D contradict it. C is compatible because discovery time is not the time the leak began; the leak may already have existed. The question asks compatibility, not whether every selected statement is forced by the record.

## Q8

**Correct answer:** 2.3125

For each colour, the chance it is observed at least once is1−(3/4)³=37/64. Sum the four indicator expectations:4·37/64=37/16=2.3125. The indicators need not be independent for linearity of expectation.

## Q9

**Correct answer:** A

Corroboration supplies supporting evidence, while the second clause withholds proof of the explanation. A preserves both. B reverses support, C exaggerates it to universal proof, and D mistakes evidentiary support for repetition of wording. Support for an observation and support for its proposed cause are distinct.
## Q10

**Correct answer:** 8

Divisibility by6 forces a≥1 and b≥1. For b=1, the bound2^a≤24 permits a=1,2,3,4. For b=2, it permits2^a≤8, giving three choices. For b=3, only a=1 works; b≥4 permits none. Unique prime factorization makes these4+3+1=8 distinct integers. The bound N≤72 does not require N to divide72.

## Q11

**Correct answer:** A, C

The state, head position and contents of the bounded tape range form a finite configuration space, proving C. Determinism means a repeated complete configuration repeats the future forever. Simulating until halt or repetition therefore decides halting, proving A. A machine may loop within one cell, refuting B. The finite bound is essential and does not apply to unrestricted machines, refuting D.

## Q12

**Correct answer:** 5

Initially three frames are shared. The first parent write to page0 makes one private copy, increasing the count to4; its second write uses that same private frame. The child's first write to page1 makes another copy, giving5. Repeated writes do not repeatedly copy an already private page.

## Q13

**Correct answer:** 18

Idempotence implies every eigenvalue satisfies λ²=λ, hence λ is0 or1. The polynomial t(t−1) has distinct roots, so A is diagonalizable; rank2 gives two eigenvalues1 and one0. A+2I therefore has eigenvalues3,3,2 and determinant18. Rank alone would not determine the eigenvalues without idempotence.

## Q14

**Correct answer:** A, C

Distributivity holds in arithmetic modulo2^n, so A is valid even across wrapping. Multiplication by0 is always defined and zero, proving C. B changes an undefined zero-divided-by-zero expression into a defined constant, so it does not preserve definedness. For n=2,x=1,y=0, the two orders in D give1 and3, refuting D.

## Q15

**Correct answer:** 0.5413 (accepted range 0.54125–0.54135)

f'(x)=exp(−x)x(2−x). It is positive on(0,2) and negative on(2,infinity), so x=2 gives the global maximum. Its value is4/exp(2)≈0.541341. The endpoint gives0 and the function tends to0 at infinity. A stationary point must be checked against the domain and derivative sign.

## Q16

**Correct answer:** B, D

Let q=P(A∩B). The feasible interval is max(0,0.8+0.7−1)≤q≤min(0.8,0.7), or0.5≤q≤0.7. B chooses0.6 and D implies q=0.5, both feasible. A is below the lower bound. C would give q=0.5·0.7=0.35, also impossible. A conditional probability must be compatible with the other supplied probabilities.

## Q17

**Correct answer:** 15

T1 committed, so recovery redoes its durable update even though x's page was not flushed, producing x=8. T2 did not commit, so its flushed y=9 is undone to7. Therefore x+y=15. A page reaching storage is not equivalent to the transaction committing.

## Q18

**Correct answer:** A, C, D

The divisibility order has chain1<2<4<12 and the extra branch1<3<12. Every pair has a join and meet, so A. In particular join(2,3)=12 and meet(4,3)=1, proving C,D. Distributivity fails: 4 meet(2 join3)=4, whereas(4 meet2) join(4 meet3)=2 join1=2. Thus B is false. Removing a divisor can change a join from the ordinary numerical least common multiple.

## Q19

**Correct answer:** C

For t=7, the read-timestamp test7<5 is false, but7<9 is true, so ignore. For t=4, the first test4<5 already aborts. C is the pair. A,D incorrectly perform the obsolete write; B reverses the priority of the two checks. Each attempt starts from the specified same metadata.
## Q20

**Correct answer:** A, D

The four minterms are0000,0010,1000,1010. A and C vary independently, while B=D=0 throughout. Thus they form a four-cell cube represented by (NOT B)(NOT D), proving A,D and refuting B,C. Karnaugh-map grouping follows Gray-code adjacency, including wraparound, rather than ordinary consecutive decimal labels.

## Q21

**Correct answer:** A, C, D

Transposition reverses product order, giving Aᵀ=UᵀLᵀ, so A is true. Set y=Lᵀx; solve Uᵀy=b first, then Lᵀx=y, proving C. Reversing those solves in B generally solves the wrong product because the factors need not commute. Transposing a unit lower-triangular matrix gives unit upper triangular, proving D.

## Q22

**Correct answer:** 0

Unlink removes the final directory reference, but an open reference remains. The stated reclamation condition is therefore false and none of the eight blocks is freed yet. Namespace removal and storage reclamation can occur at different times.

## Q23

**Correct answer:** 3

Insert index0, value4. Value2 removes4 from the back; value3 removes nothing. Before processing value1, index0 has already gone, so expiration removes nothing. Value1 removes3 and then2 from the back. Total back removals are1+0+2=3. Expiration removals and dominance removals are different operations.

## Q24

**Correct answer:** 5

The first read advances a's open file description to3. dup2 replaces b's independent description with a reference to that same description. Reading2 through b advances the shared offset to5, which a also observes. Opening twice initially creates independent offsets, but the duplication changes that relationship.

## Q25

**Correct answer:** 2

With root4, paths to5 and6 are4→2→5 and4→2→1→3→6. Their deepest common vertex is2. Lowest common ancestors depend on the chosen root even though the undirected edges are unchanged.

## Q26

**Correct answer:** A, C

Don't-cares may be used to enlarge useful cubes, proving A, but they need not be covered, refuting B. OFF inputs must remain0, so C is true. Covering only don't-cares cannot satisfy an additional required ON input and is not mandatory, refuting D. Optimization freedom is not an additional output requirement.

## Q27

**Correct answer:** 4

Both reachable incoming paths provide4, and the unreachable path contributes no possible execution. Joining only reachable states therefore retains constant4. Treating unreachable information as a real conflicting value would lose precision.

## Q28

**Correct answer:** 2

The valid sequences are(2,2) and(1,2,1). The remaining compositions of4 use adjacent1 steps: (1,1,2),(2,1,1),(1,1,1,1). Thus the count is2. A recurrence that tracks only remaining sum without the previous-step condition would overcount.

## Q29

**Correct answer:** A, C

A full link-state database supports independent shortest-path computation from each router, proving A. The source differs, so the resulting trees and next hops can differ, proving C and refuting D. B describes distance-vector-style information rather than the stated topology database. Shared input topology is not a shared source vertex.

## Q30

**Correct answer:** 4

The cache has64/4=16 data blocks. Four blocks per set give16/4=4 sets. Associativity counts ways within a set, not the total number of blocks.

## Q31

**Correct answer:** 839

The fragment starts at75·8=600 bytes. Its240-byte payload occupies offsets600 through600+240−1=839. The final byte has an inclusive offset, one less than the next byte's position.

## Q32

**Correct answer:** A, C

The successor is the leftmost node in v's right subtree, so it cannot have a left child, proving A and refuting D. It may lie several edges below v, refuting B. Its possible right child can replace it at its original parent link, proving C. If s is v's immediate right child, that former parent is v itself.

## Q33

**Correct answer:** 3

Between polls0 and25, arrivals occur at10 and20. Between25 and50, arrivals occur at30,40,50, with the arrival at50 preceding the poll. The pattern repeats every50 microseconds, so at most three bytes accumulate, and that number is attained. Capacity2 overflows before the poll at50.

## Q34

**Correct answer:** 4

The empty word reaches(even,even), b reaches(odd,even), a reaches(odd,odd), and ab reaches(even,odd). All four states are therefore reachable. The two parities are not identical because b changes length without changing the a count.

## Q35

**Correct answer:** 5

Let L(n) count leaf calls. L(1)=L(2)=1 and L(n)=L(n/2)+L(n/4) for n≥4. Hence L(4)=2,L(8)=3,L(16)=5. The two children have different sizes, so counting a complete balanced binary tree would be incorrect.

## Q36

**Correct answer:** A, B, C

For s=0, T=a and F=T=a. For s=1, T=b and F=NOT T=NOT b. This proves A. When a=b, these two outputs are complements, proving B. When a≠b, a=NOT b and they agree, proving C. With s=a=b=0, F=0, but with s=0,a=b=1, F=1 whereas s XOR a XOR b=0, refuting D. Evaluate the two selection levels in their stated order.

## Q37

**Correct answer:** 15

The successive states before the first return are0001,0010,0100,1001,0011,0110,1101,1010,0101,1011,0111,1111,1110,1100,1000, followed by0001. They are15 distinct states. The feedback is computed from old a,b; updating bits one at a time would produce another machine.

## Q38

**Correct answer:** 509

The original clock period is max(2,3,10,4)+1=11ns. A four-stage pipeline executes100 independent instructions in100+4−1=103 cycles, taking1133ns. The redesign has five stages and period5+1=6ns, giving104 cycles and624ns. Savings1133−624=509ns. Faster steady-state throughput must be combined with the changed filling latency.

## Q39

**Correct answer:** 2

The expression inside the absolute value changes sign at1. The integral is ∫0¹(1−x²)dx+∫1²(x²−1)dx=2/3+4/3=2. Integrating x²−1 without splitting would cancel part of the area that the absolute value makes positive.

## Q40

**Correct answer:** A, C, D

The identifier is the pair, permitting the same room number under different owners, proving A and refuting B. BuildingID contributes to identification, proving C. Replacing it with another owner's identifier can duplicate an existing pair, proving D. A partial key is not a global key.

## Q41

**Correct answer:** 3

At the point queried, p is needed for the branch. If execution goes to Again, b supplies the next a; if it goes to Exit, the current a is returned. Thus a,b,p are live under may-liveness, giving3. The analysis unions possible successor uses; it does not require all three to be used on the same execution path.

## Q42

**Correct answer:** A, D

Let the original operands be a0,b0, so t=a0+b0. Path P makes the sum a0+1+b0=t+1, proving A. Path Q leaves it t, making the path-dependent selection in D valid. Global reuse of t in B misses the increment. Assigning a does not mutate the already computed scalar t, refuting C. Dependency of a value at computation time is not an ongoing reference link.

## Q43

**Correct answer:** A, B

v's discovery and finish interval lies strictly inside u's, so it is a descendant, proving A. An edge from that descendant to u is a back edge, proving B. An edge u→v can skip intervening descendants and be forward rather than tree, refuting C. During v's exploration w would be undiscovered; an edge v→w would then discover w before v finished at7, contradicting w's discovery time10, so D is false. DFS intervals impose restrictions beyond merely labelling edges after the fact.

## Q44

**Correct answer:** 8

Immediately after fork the parent has3 threads and the child1. Each adds2, yielding5+3=8. Fork's specified child-thread rule differs from copying every parent thread.

## Q45

**Correct answer:** 6

The distinct nonempty subsequences of nullable occurrences in ABA are ABA,AB,BA,AA,A,B. Retaining only the first A and retaining only the final A produce the same right-hand side A and are counted once. Thus6. There are eight omission patterns, but one is empty and two collapse to the same A.

## Q46

**Correct answer:** 4

Replacing index4 by the last value4 leaves[1,10,2,4,12,3]. Its parent10 exceeds4, so sift upward: exchange indices4 and2 to obtain[1,4,2,10,12,3]. No further exchange is needed. Index2 contains4. Arbitrary-index deletion may require upward repair, unlike the familiar root deletion's usual downward repair.

## Q47

**Correct answer:** 1

For x<4, the unique MST uses AD,BC,AB, with total x+3. These three edges form a tree and each alternative connection costs more; ties x=1 or2 do not create a same-weight cycle exchange. At x=4, either AB or CD can connect the components formed by AD and BC, giving two MSTs of weight7. For x>4, AD,BC,CD form the unique MST; AC=5 and AB≥5 cannot replace a cheaper cut edge at no cost. Exactly one integer choice, x=4, produces multiplicity. Equal weights matter only when they offer interchangeable connections.

## Q48

**Correct answer:** 3.5

The absolute-deviation objective is minimized at every median, here every x in[0,4]. The squared-deviation objective is minimized at the mean(0+0+4+10)/4=3.5. That mean lies inside the permitted first-stage minimizer interval, so3.5 is selected. The second criterion resolves the first criterion's nonuniqueness.

## Q49

**Correct answer:** A, C

The order of x divides both4 and6, hence divides2, proving x²=e and C. It also divides the odd group order, so it cannot be2; its order is1, giving x=e and A. B,D contradict that order. The two exponent equations alone would allow order2; the odd-order hypothesis eliminates it.

## Q50

**Correct answer:** A, C

On an input-consuming PDA step, update the DFA with the same symbol, proving A. A PDA epsilon step changes only the PDA component and leaves the DFA state unchanged, refuting B. The finite DFA state is stored in the finite product control; the original stack suffices, proving C and refuting D. Acceptance must require the PDA's acceptance condition and an accepting DFA state after the input is consumed.

## Q51

**Correct answer:** 4

Two-step paths yield P={(a,c),(a,a),(b,a),(c,b),(c,c)}. Of these, only(a,c) is already in E. Therefore P−E has4 pairs. Set projection eliminates duplicate witnesses, and self-pairs are permitted when a two-edge cycle returns to the start.

## Q52

**Correct answer:** A, C

The HEX token stops after1 because G is outside[0-9A-F]; ID then matches G. This proves A and refutes B,D. The resulting token sequence may still violate the parser grammar, proving C. Lexical validity and grammatical validity are separate questions.

## Q53

**Correct answer:** 2

The retained ranges are.0–.63 and.128–.255, represented by10.1.0.0/26 and10.1.0.128/25. Thus two prefixes suffice. One prefix describes a single contiguous aligned range and cannot include both retained ranges while omitting the gap. Two is therefore minimal.

## Q54

**Correct answer:** -3

Left grouping gives sat(7+3)=7, followed by sat(7−3)=4. Right grouping gives sat(3−3)=0, then sat(7+0)=7. The requested difference is4−7=−3. Saturating addition is not associative, even though ordinary integer addition is.

## Q55

**Correct answer:** 8

A perfect matching must use newly added edges to both initially isolated right vertices3 and4. The pair a,b also needs an escape from its single neighbour1, and c,d needs an escape from2. With only two new edges, choose one endpoint from{a,b}, one from{c,d}, and assign them bijectively to3,4. There are2·2·2=8 choices, each completing a matching with the remaining original edges. Any other two-edge choice leaves a deficient pair or isolated right vertex.

## Q56

**Correct answer:** 16

PUSH7 writes7 at96; PUSH9 writes9 at92. POP sets R=9 and SP=96. The explicit store writes9 at100, not at96. The final POP therefore reads the still-present7 at96 into S, giving R+S=16. The store uses the current SP after the first pop.

## Q57

**Correct answer:** 2

Dijkstra extracts a at tentative distance1 and sets t to2. It then extracts t before b, reporting2. The actual path s→b→a→t costs4−5+1=0, and the other paths cost2 or14, so the shortest distance is0. Difference2−0=2. The negative edge invalidates the assumption behind early finalization.

## Q58

**Correct answer:** 3

With capacities1 and1, both processes fill their outgoing channel with the first send and block on the second before either receives: sum2 fails. With capacities2 and1, the process whose outgoing channel has capacity2 can finish both sends and reach its receive operations. Those receives free the other's smaller outgoing channel, allowing its second send and subsequent receives. Fair scheduling then completes both. Positive capacities and the failing sum2 case establish the minimum sum3. Both channels need not separately hold the entire outgoing batch.

## Q59

**Correct answer:** A, B, D

Context-free languages are closed under intersection with regular languages, proving A. A regular language is context-free, and context-free languages are closed under union and concatenation, proving B,D. They are not generally closed under complement, so C is not guaranteed. The regularity condition on R is essential for the intersection guarantee.

## Q60

**Correct answer:** 3

The original edges are0→1,0→3,1→2,2→0,2→3. Original indegrees, which become reversed outdegrees, are[1,1,1,2]. Prefix sums give new offsets[0,1,2,3,5], so vertex3's offset is3. CSR row offsets store cumulative counts, not the degree alone.

## Q61

**Correct answer:** A, C

After signal(full), the consumer can pass its wait and read while the producer is paused before writing, proving A. Atomic operations do not reorder the intervening ordinary write, refuting B,D. Publishing full only after writing ensures that this signal cannot authorize an early read, proving C under the stated one-producer, one-consumer ordering. Synchronization operations must surround the data access in the correct order.

## Q62

**Correct answer:** A, C

A is a subset of finite R and C is the union of two finite sets, so both are finite. B excludes only finite R from an infinite domain, leaving infinitely many values. D excludes finite R∪S and is likewise infinite. Negation alone does not restrict free variables to stored values.

## Q63

**Correct answer:** 12

For each of the two remote endpoints, six public ports can be used. The same port can be reused for the other remote endpoint because that endpoint participates in the distinguishing key. Thus6·2=12 mappings fit. Treating the public port alone as globally unique would ignore the explicit model.

## Q64

**Correct answer:** B

The first test reads a[0]=1 and increments i to1; the body adds a[1]=2. The next test reads a[1]=2 and increments i to2; the body adds a[2]=0. The next test reads a[2]=0 and increments i to3, but the body is skipped. It prints3 2, option B. A,D incorrectly sum tested elements rather than the body accesses; C misses the increment in the failed test. No out-of-bounds body access occurs for this particular array.

## Q65

**Correct answer:** 400

The receive window permits bytes1000 through2199 inclusive. The next unsent byte is1800, leaving400 bytes of receive-window space. The800 bytes already in flight leave1500−800=700 bytes of congestion-window allowance. Both limits apply, so the sender may add min(400,700)=400 bytes. Window sizes are limits on the relevant byte range or outstanding data, not quantities added independently.

