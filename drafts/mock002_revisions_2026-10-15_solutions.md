## Q38

**Correct answer:** A, B, C

**Concept:** Algorithms — Minimum spanning trees and constrained counting

1. A spanning tree needs five edges and must connect the two triangles. Four unit edges and one weight-2 connector give weight 6. A lighter tree cannot connect all six vertices, since every connector weighs at least 2.
2. For weight 6, choose a spanning tree in each triangle in 3 ways each, then one of AD, BE, CF in 3 ways. This gives 3×3×3=27.
3. A weight-7 tree has either four unit edges and AE, or three unit edges and two weight-2 connectors. The first case gives 3×3=9.
4. In the second case choose the two connectors in 3 ways. The three unit edges must split as two in one triangle and one in the other: taking all three from a triangle would create a cycle. There are 2 choices of which triangle gets two edges, 3 choices of its spanning tree, and 2 choices of the other triangle's single edge. That edge must attach its otherwise unconnected third vertex to a connector endpoint. Thus this case contributes 3×2×3×2=36.
5. Total weight-7 trees: 9+36=45.

- **A:** Correct: the lower bound 6 is attained.
- **B:** Correct: the three independent choices give 27 distinct edge sets.
- **C:** Correct: the two disjoint weight compositions give 45 trees.
- **D:** Incorrect: a spanning tree in each triangle together with AE has weight 7 and uses no weight-2 edge.

**Common misconception:** Equal-weight edges create multiple optima, and counting the next weight requires checking connectivity and cycles, not just the number of chosen edges.

## Q43

**Correct answer:** A

**Concept:** Operating Systems — Contiguous allocation and coalescing

1. First-fit allocates A at [0,50). B cannot fit the remaining [50,60), so it occupies [100,135).
2. Freeing A and X joins [0,50), [50,60), and [60,100) into [0,100). B prevents further merging. The other holes have sizes 45 and 40. The largest is 100.
3. Best-fit also puts A at [0,50), since the 60-unit hole is the smallest that fits 50. It puts B in the 40-unit hole at [200,235).
4. When A and X are freed, the entire interval [0,180) becomes free: the original [100,180) hole was never occupied. Y prevents merging beyond 180. The largest hole is 180.

- **A:** Correct: the maxima are 100 and 180.
- **B:** Incorrect: best-fit leaves [100,180) available for coalescing.
- **C:** Incorrect: first-fit's B blocks the interval at address 100.
- **D:** Incorrect: it reverses the two outcomes.

**Common misconception:** A choice that leaves a smaller immediate remainder can improve a later allocation by preserving holes that will coalesce after deallocation.

## Q45

**Correct answer:** B

**Concept:** Computer Organization and Architecture — Signed overflow and unsigned comparison

1. N=0 with V=1 means the mathematical signed subtraction was less than −128, wrapping into a nonnegative result. Positive overflow would instead produce N=1.
2. Therefore A represents a negative signed number and B a nonnegative signed number. Write the unsigned value of A as 128+r, where 0≤r≤127, and the value of B as b, where 0≤b≤127. Their signed difference is r−128−b.
3. Overflow requires r−128−b<−128, hence b>r. Every such pair automatically has unsigned A>B, so C=1.
4. For r=0 there are 127 choices of b, for r=1 there are 126, and so on down to zero. The count is 127+126+⋯+1=127×128/2=8128.

- **A:** Incorrect: 8192 treats the boundary as exactly half of all opposite-sign pairs without excluding the equality diagonal.
- **B:** Correct: the strict triangular inequality gives 8128.
- **C:** Incorrect: 8256 includes b=r, whose signed result is exactly −128 and does not overflow.
- **D:** Incorrect: 16384 counts all opposite-sign pairs, including those with no overflow.

**Common misconception:** Unsigned carry and signed overflow describe different properties; endpoint pairs must be checked against the signed representable range.

## Q48

**Correct answer:** B, C, D

**Concept:** Databases — Conflict and view serializability with blind writes

1. The first w1(x) precedes w2(x), creating conflict edge T1→T2. The last w1(x) follows w2(x), creating T2→T1. The conflict graph is cyclic.
2. The only read, r4(x), sees T2's write. The final writer of x is T1; the final writer of y is T4.
3. A view-equivalent serial order must place T2 before T4. Because T1 must be the final x writer, T1 is after T2; because T4 must still read T2's x, T1 cannot intervene between T2 and T4. Thus T2<T4<T1.
4. Both T2 and T3 write y, so both must precede final y-writer T4. T2 and T3 can be ordered either way. The only view-equivalent orders are (T2,T3,T4,T1) and (T3,T2,T4,T1).
5. Delete the first w1(x). The y conflicts now force T3<T2<T4, and the x conflicts force T2<T4<T1. Together they yield the unique conflict-equivalent order (T3,T2,T4,T1).

- **A:** Incorrect: T1 and T2 form a conflict cycle in the original schedule.
- **B:** Correct: the two displayed serial orders preserve the read source and final writers.
- **C:** Correct: the precedence requirements leave only the relative order of T2 and T3 free.
- **D:** Correct: after deletion all four transactions lie on the forced chain T3→T2→T4→T1.

**Common misconception:** Blind writes can make a schedule view-serializable even when its conflict graph has a cycle; preserving final writers is essential.

## Q51

**Correct answer:** A, C

**Concept:** Theory of Computation — Closure properties and regular restrictions

1. L is context-free: it is the union of the context-free languages with i=j and with j=k. R is regular, expressed as a*(epsilon|b|bb)c*.
2. For each fixed j in {0,1,2}, membership of L intersect R requires i=j or k=j. Its portion for that j is a^j b^j c* union a* b^j c^j. These are regular, and their finite union is regular.
3. L minus R equals L intersect the complement of R. A context-free language intersected with a regular language remains context-free.
4. L minus R is not regular. Intersect it with the regular language a*b* (no c symbols). Since j>2, the alternative j=k=0 is impossible, leaving {a^n b^n:n≥3}, which is nonregular. A regular L minus R could not have this nonregular regular-language intersection.
5. In L intersect S we have i=k, together with i=j or j=k. Either alternative forces all three counts equal. Thus the intersection is {a^n b^n c^n:n≥0}, which is not context-free. For the standard pumping argument, choose a^p b^p c^p: a pumping window of length at most p cannot cover all three blocks, so pumping changes at least one count while leaving another unchanged, or violates block order.

- **A:** Correct: the middle block is bounded, giving a finite union of regular languages.
- **B:** Incorrect: the c-free regular slice proves nonregularity.
- **C:** Correct: difference by a regular language preserves context-freeness.
- **D:** Incorrect: the equal-outer-count restriction forces three equal block counts.

**Common misconception:** Intersection with a regular language preserves context-freeness, but intersection with another context-free language need not; bounded and unbounded restrictions behave differently.

## Q53

**Correct answer:** B

**Concept:** Programming and Data Structures — Directed multigraph representation and edge-distinct walks

1. Every closed walk without a repeated edge decomposes into directed cycles using disjoint edges. Here a four-edge walk can be either two two-edge cycles or one three-edge cycle plus the self-loop at vertex 3. There is no four-vertex simple cycle and only one loop.
2. The first case combines 1→2→1 with 2→3→2. The 1→2 edge has two choices. For either choice, the resulting four-edge circuit has four distinct cyclic starting positions, including two distinct edge orders starting at vertex 2. Contribution: 2×4=8.
3. The only directed three-vertex cycle is 1→3→2→1. Insert the loop 3→3 at vertex 3. This circuit has four distinct cyclic starting positions. Contribution: 4.
4. Repeating the 1↔2 cycle would reuse the sole 2→1 edge; repeating the 2↔3 cycle would also reuse edges. Neither is allowed. The total is 8+4=12.

- **A:** Incorrect: 7 is the ordinary closed-walk count for length two, not this task.
- **B:** Correct: the two permissible cycle decompositions give 12.
- **C:** Incorrect: it does not follow from the permitted disjoint-edge decompositions.
- **D:** Incorrect: reversing a directed circuit is not automatically permitted; doubling 12 counts nonexistent reversals.

**Common misconception:** Powers of an adjacency matrix count unrestricted walks, including edge reuse. An edge-distinct restriction requires additional state or a structural counting argument.

## Q61

**Correct answer:** 5000 (exact)

**Concept:** Computer Networks — Sliding receive and congestion windows

1. Initially the receive-window right edge is 1001+6000=7001, and the congestion-window right edge is 1001+8000=9001. The next new byte is 5001, so the sender may transmit 2000 new bytes, advancing next to 7001.
2. After ACK=3001, the receive-window right edge becomes 3001+3500=6501, behind the next new byte. Existing data remains outstanding; no additional new data is permitted at this step.
3. After ACK=5501, the receive edge is 10501 and the congestion edge is 5501+4500=10001. The binding edge is 10001. With next still 7001, the sender can transmit 3000 new bytes.
4. Total new data is 2000+0+3000=5000 bytes. The intervals are half-open, so no extra byte is added at an edge.

**Common misconception:** A receive window is anchored at the accompanying acknowledgement, and shrinking it does not retract previously transmitted data or reset the next sequence number.
