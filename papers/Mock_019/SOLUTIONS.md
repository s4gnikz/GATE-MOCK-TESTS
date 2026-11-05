# Worked Solutions — Mock Test 019

## Q1
**Correct answer:** C

Concept: scope of survey evidence. The volunteers reported a result, but self-selection can affect representativeness; C preserves that distinction. A generalizes to every resident, B assumes away selection bias, and D asserts dishonesty without evidence. A limitation on generalization does not invalidate the observations themselves.

## Q2
**Correct answer:** 4

Concept: divisibility and leading-zero constraints. The final two digits must form a multiple of four. With the available distinct digits, the possible endings are 12,20,32. Ending 12 leaves 0,3 and allows only prefix 30; ending 20 leaves 1,3 and allows 13 or 31; ending 32 leaves 0,1 and allows only 10. Total=1+2+1=4. Count admissible leading digits separately for each ending.

## Q3
**Correct answer:** C

Concept: cumulative frequencies. The median is the thirteenth ordered observation. The first two bins contain 4+6=10 observations, and the third extends the cumulative count to 20. Hence observation 13 lies in [20,30), C. A and B finish too early; D starts after observation 20. The bin containing the mean need not be identifiable from these data.

## Q4
**Correct answer:** 5

Concept: inverse folding. Immediately before the second fold, positions 2 and 4 both map to the puncture at 4. Undoing the first fold gives original positions 2,8 from folded position 2 and 4,6 from folded position 4. All four positions are distinct. Their mean is (2+4+6+8)/4=5. Each fold must be inverted across every layer actually present.

## Q5
**Correct answer:** B

Concept: precedence constraints. Both A and B must precede C, and D must follow C. Only the order of A and B is free, yielding ABCD and BACD. B is exact; A omits BACD; C puts certification before a prerequisite; D ignores the constraints. A partial order can allow several chronological sequences.

## Q6
**Correct answer:** 0.3333

Concept: conditional subset counting. Fix the first person's subset. Among the ten possible second subsets, nine differ from it. For their union to include all five elements, the second subset must include both elements outside the first and one of its three elements. Thus three of the nine eligible subsets work, giving 1/3. Round to 0.3333; range 0.33325–0.33335. The conditioning excludes the identical subset from the denominator.

## Q7
**Correct answer:** D

Concept: contextual meanings and qualification. D uses impartial for disinterested, approved for sanctioned, and retains criticism of cost. A changes both meanings; B reverses approval and criticism; C incorrectly treats impartiality as loss of interest. Approval of a procedure need not endorse every aspect of it.

## Q8
**Correct answer:** 6

Concept: comparing geometric sums. After n days, A has 4(2ⁿ−1) units and B has (3ⁿ−1)/2. For n=1 through 5 these pairs are (4,1),(12,4),(28,13),(60,40),(124,121); B has not exceeded A. At n=6 they are (252,364), giving the first crossing. Comparing daily outputs alone would give an earlier, incorrect answer.

## Q9
**Correct answer:** C

Concept: repeated ordered transformations. Reverse CAT to TAC and advance by 1,2,3 to obtain UCE. Reverse UCE to ECU and advance again to obtain FEX, C. A stops after the first application; B advances the wrong letters or positions; D does not follow the specified two-stage procedure. The position-dependent shifts must be applied after each reversal.

## Q10
**Correct answer:** 0.5556

Concept: surface changes after removal. The original painted surface has 6·9=54 unit faces. Eight removed corners each remove three painted faces, leaving 54−24=30 painted faces. Each removed corner exposes three previously internal faces, adding 24 unpainted faces. Exposed total=54, and painted fraction=30/54=5/9=0.555555…. Round to 0.5556; range 0.55555–0.55565. Remaining surface is not merely the original surface minus the removed faces.

## Q11
**Correct answer:** C

Concept: bounded blocking queues. Each first send fills its queue. Neither process reaches a receive until after its second send, but those second sends block on full queues. Once both have run that far, neither can make progress, C. A ignores capacity after the first send; B incorrectly distinguishes the symmetric processes; D invents overwrite semantics. Eventual scheduling cannot overcome this circular wait.

## Q12
**Correct answer:** 6

Concept: critical-word-first miss latency. Sequential delivery returns offsets 0 through 6 at cycles 12 through 18. Critical-word-first returns the needed offset at cycle 12. The CPU resumes six cycles earlier. Full-line completion time is different from latency to the required word.

## Q13
**Correct answer:** 9

Concept: finite ticket-number wraparound. Eight outstanding contenders can hold the eight distinct ticket values, including the owner. The ninth issued ticket repeats the owner's value while it is still served, allowing a second contender to satisfy the entry test. Thus nine is the first unsafe outstanding count. Atomic issuance does not prevent modulo-counter aliasing.

## Q14
**Correct answer:** 4

Concept: overlapping copies. The preserved source sequence 1,2,3,4 replaces positions 2,3,4,5, giving [1,2,1,2,3,4]. Position 5 contains four. A naive forward assignment loop would not implement the stated overlap-preserving semantics.

## Q15
**Correct answer:** 7

Concept: duplicate-suppressed flooding. Source S sends on its two incident links. Routers A and B each have degree three and each forwards on two links after its first arrival. C has degree two and forwards on one. Total=2+2+2+1=7 transmissions. Arrival order can choose which link is excluded but does not change these counts; later duplicates never trigger further sends.

## Q16
**Correct answer:** 3

Concept: don't-care minimization. Allowing minterm 7 makes all four minterms with c=1 usable, so F=c costs one literal. Requiring 7 OFF leaves F=a'c+b'c: four literal occurrences. No larger cube is valid, and minterms 3 and 5 need separate implicants, so four is minimal. Increase=4−1=3. A don't-care may enlarge an implicant without being required in the output's ON set.

## Q17
**Correct answer:** B, C

Concept: essential prime implicants. Every column is covered by two rows, so no row uniquely covers a required minterm; B is true and A false. Any two rows cover all three columns, proving C. D is false: a cover need not contain an essential row. Covering many columns alone does not establish essentiality.

## Q18
**Correct answer:** A, C

Concept: amortized geometric copying. Copies occur at sizes 1,2,4,... below n. Their sum is less than 2n, so A holds and B fails. An append at a full capacity proportional to n copies Θ(n) elements, making C true and D false. Amortized constant time does not mean worst-case constant time per operation.

## Q19
**Correct answer:** 1

Concept: weighted interval scheduling. Earliest finish first chooses [0,2), then [2,4), total weight eight. Choosing only [0,4) yields nine, which is optimal among the listed choices. Shortfall=1. The unweighted greedy rule does not generally maximize weights.

## Q20
**Correct answer:** A, D

Concept: PDA acceptance-mode conversion. After consuming all input in an original final state, drain mode can empty the protected stack and accept, A. If input remains, drain mode has no consuming transitions and cannot meet the all-input-consumed requirement, D; B is therefore false. The fresh marker protects against premature empty-stack acceptance and must be distinguished from original symbols, so C is false. Acceptance requires both the stack/final-state condition and complete input consumption.

## Q21
**Correct answer:** 1

Concept: expressing exactly two related values. The existential part supplies two distinct B values and the universal part excludes any others. A=1 has exactly {a,b}; A=2 has only {a}; A=3 has {a,b,c}. Only A=1 qualifies, giving one. Existential witnesses alone would express at least two rather than exactly two.

## Q22
**Correct answer:** 1

Concept: rationalization. For nonzero x near zero, multiply by the conjugate to obtain 2/(sqrt(1+x)+sqrt(1−x)). The denominator tends to two, giving limit one. Substituting before removing the zero-over-zero form does not evaluate the limit.

## Q23
**Correct answer:** 1

Concept: NULL-aware aggregate conditions. Group A has zero distinct non-null x values and fails. B has one distinct non-null value and counts COUNT(*)=2, COUNT(x)=1, passing both tests. C has one distinct value but both counts equal two, failing the second test. Only B remains. COUNT(DISTINCT x) and COUNT(x) both ignore NULL, unlike COUNT(*).

## Q24
**Correct answer:** 16

Concept: reassembly offsets. The first fragment covers bytes 0–79. Offset 12 means byte 96, so the last fragment covers 96–119. Missing positions 80–95 total sixteen bytes. The offset is not measured in bytes, and headers are not part of the reassembled payload offsets.

## Q25
**Correct answer:** A, C

Concept: attribute dependency ordering. X is the left child, but its inherited value depends on right sibling Y's synthesized attribute, violating the usual L-attributed restriction, A. Y is independent of X, so there is no forced cycle; compute Y.v first, then X.i, making C true and B false. Attribute dependencies do not establish syntactic ambiguity, so D is false. A valid evaluation order need not be the standard left-to-right attributed order.

## Q26
**Correct answer:** 0.3

Concept: normalizing a density and computing a moment. Integral of x(1−x) on [0,1] is 1/2−1/3=1/6, hence c=6. E[X²]=6∫₀¹(x³−x⁴)dx=6(1/4−1/5)=3/10. A density's scale must be fixed before using it to compute expectations.

## Q27
**Correct answer:** 2

Concept: powers of permutation cycles. The cycles have lengths three and two. Since 2026 is even, the two-cycle fixes both 4 and 5 after that many applications. Since 2026 mod 3=1, the three-cycle still moves every one of 1,2,3. Exactly two fixed points remain. Repeated composition is governed separately by each cycle length.

## Q28
**Correct answer:** 5

Concept: write-allocate and dirty eviction. Store to block 0 fetches one line and dirties it. Store to block 1 writes back block 0 and fetches block 1. Load from block 0 writes back dirty block 1 and fetches block 0. Total=3 reads+2 write-backs=5. No final flush is requested, and the final load leaves a clean line.

## Q29
**Correct answer:** 1.5

Concept: inverse matrix and trace. Determinant is 0·3−(−2)·1=2. The inverse is (1/2) times the matrix with rows (3,2),(−1,0). Its trace is 3/2=1.5. In general trace(A inverse) is not the reciprocal of trace(A).

## Q30
**Correct answer:** 3

Concept: pointer rewiring. After swapping the two links, 1 points to 4 and 3 points to 2; the other links remain 4→3 and 2→1. Starting at 1, two traversals give 1→4→3, hence three. Track actual pointers rather than the original list memberships.

## Q31
**Correct answer:** 3

Concept: inverse image under a homomorphism. Each nonempty symbol image starts with a and ends with b. Concatenating two or more images creates a ba boundary, forbidden in a*b*. The empty word, 0 and 1 all qualify, and no longer word does. Thus three. Balanced symbol counts alone would not enforce the required order of all as before all bs.

## Q32
**Correct answer:** B, D

Concept: frame lifetime in tail calls. Q uses the address of x, so a correct transformation must retain valid storage and the intended value for that use, B. Tail position by itself does not justify overwriting all of P's frame, D. A ignores the live addressed object; C contradicts the explicitly passed pointer. Tail-call optimization is constrained by observable storage lifetimes.

## Q33
**Correct answer:** B

Concept: mean value theorem bounds. The increase f(3)−f(0) lies between 2·3 and 5·3, so 7≤f(3)≤16. B's value ten is achieved by f(x)=1+3x. A is below seven, C and D exceed sixteen. Bounding derivatives constrains endpoint differences, not just local slopes.

## Q34
**Correct answer:** 4

Concept: priority encoding. Code 10 requires D3=0 and D2=1. D1 and D0 are arbitrary, giving 2²=4 patterns. Validity is automatically one because D2 is asserted. Lower-priority asserted inputs do not change the code.

## Q35
**Correct answer:** 3

Concept: minimum pumping length with exceptional short words. For p≤2, w=a³ must be pumpable but any allowed y has length one or two; pumping it down gives length two or one, neither in L. Thus p≥3. At p=3, use |y|=3 for a³, obtaining lengths 0,3,6,...; use |y|=2 for a⁵, obtaining 3,5,7,...; and use |y|=1 for all lengths at least six, obtaining lengths at least five. All choices obey the prefix bound and remain in L for every i≥0. Hence p=3 suffices.

## Q36
**Correct answer:** A, C

Concept: SQL NULL constraint semantics. For (NULL,−5), the CHECK evaluates UNKNOWN rather than FALSE, and MATCH SIMPLE skips the foreign-key lookup. UNIQUE permits NULL-containing duplicates under the stated rule. Thus A and C hold. B wrongly treats UNKNOWN as a rejection; D fails because non-null (1,1) requires a referenced row and none exists. All three constraint semantics were explicitly specified to avoid database-specific ambiguity.

## Q37
**Correct answer:** 0.5385

Concept: Bayesian evidence from experiment length. The likelihood of at least one head is 1−1/4=3/4 for two tosses and 1−1/8=7/8 for three. Equal prior weights give posterior (7/8)/(3/4+7/8)=7/13=0.538461…. Rounded value 0.5385; range 0.53845–0.53855. Longer experiments are more likely to generate the reported event.

## Q38
**Correct answer:** B, D

Concept: instance-level functional dependencies. Each AB pair occurs once, so AB→C holds (B). Repeated C=p always has B=x; q and r each have B=y, so C→B holds (D). A=1 has C=p and q, disproving A. C=p occurs with A=1 and 2, disproving C. A dependency is checked by equal determinant values, not by counting columns or rows alone.

## Q39
**Correct answer:** 19

Concept: constrained selection. Nonadjacent pairs (1,3),(1,4),(1,5),(2,4),(2,5),(3,5) have costs at most seven and values 17,19,15,17,13,14 respectively. The maximum is 19 from jobs 1 and 4, whose cost is 4+3=7. Considering values alone could select an adjacent or over-budget pair.

## Q40
**Correct answer:** 4

Concept: Mealy-style output to Moore-state memory. A reached state must encode the preceding bit for the next output and the output currently displayed. All four pairs (preceding bit,last output) are reachable. States with different displayed outputs are distinct immediately; states with the same displayed output but different preceding bits produce different outputs upon the next zero. Thus four are necessary and sufficient. The initial state can share the state for (0,0), since its initial output is ignored.

## Q41
**Correct answer:** B

Concept: pending-bit coalescence. Events at 1,2,3 collapse into one pending bit. At time 5 the handler clears it and runs to 7. The event at 6 sets it again, causing a second handler from 7 to 9. Hence B=(2,9). A counts every masked event separately; C loses the event during the handler; D has one extra invocation. A pending bit is not an event counter.

## Q42
**Correct answer:** A, C

Concept: oracle-assisted recognition versus ordinary computation. If the oracle says M does not halt on w, then w is not accepted; otherwise simulate to its halting accept/reject outcome. This decides membership with the oracle, proving A. Apply this decision to all words and output the nonmembers to enumerate the complement, C. B confuses recognizers with total deciders; D would imply an ordinary finite-time halting decision bound and is false. Oracle-assisted conclusions do not assert ordinary decidability.

## Q43
**Correct answer:** 7

Concept: basic blocks and control-flow edges. Leaders are lines 1,2,3,4,7,9, producing six blocks. Edges are 1→2; 2→3 and 2→9; 3→4 and 3→7; 4–6→2; 7–8→2. Total seven distinct block edges. Internal sequential statements within a block do not add inter-block edges.

## Q44
**Correct answer:** A, C, D

Concept: subset simulation and accepting suffixes. Starting at {p}, input 0 gives {p,q}, then 1 gives {p,r}, then 0 gives {p,q}; A holds and B fails because final acceptance requires r after the whole word, not an earlier prefix. Reachable subsets are {p},{p,q},{p,r},{p,q,r}, proving C. A zero creates q, and exactly one more symbol reaches r; r has no outgoing transitions. Thus final acceptance records a zero exactly two positions from the end, proving D.

## Q45
**Correct answer:** A, C

Concept: duplicate minima. The two pushes of one store only one auxiliary minimum. Popping one removes that minimum even though the other one remains in the data stack, so A is true and B false. Storing equal minima as separate entries keeps their multiplicities synchronized, C. Never removing minima would retain values after their last occurrence was popped, so D fails. An auxiliary summary must represent duplicate occurrences or their counts.

## Q46
**Correct answer:** A, C

Concept: aggregation with longest-prefix exceptions. The two /25s exactly partition the /24 and share H. Keeping the more-specific /26 retains J for its destinations, so A. No address outside the /24 gains a matching nondefault route, so C. Longest-prefix matching selects by prefix length, not insertion time, disproving B. Removing the /26 would send its destinations to H instead of J, disproving D.

## Q47
**Correct answer:** B

Concept: minimum-size balanced trees. Let N(−1)=0,N(0)=1. To attain height h with minimum nodes, child heights are h−1 and h−2, giving N(h)=1+N(h−1)+N(h−2). Values through h=5 are 1,2,4,7,12,20. Leaf counts with L(0)=1,L(1)=1 obey the corresponding sum and give 1,1,2,3,5,8. Thus B=(20,8). A is not the minimum-size height-five tree; C describes height four; D has the right node total but wrong leaf count. Balanced does not mean perfect.

## Q48
**Correct answer:** 7

Concept: nullable-occurrence deletion with deduplication. Distinct S right-hand sides are ABA, BA, AA, AB, A, B, ε. Deleting the left A and B or deleting B and the right A both produce A, so they count once. Total seven, rather than the eight occurrence-subset choices. Identical grammar productions are not duplicated by distinct derivational deletion choices.

## Q49
**Correct answer:** 10

Concept: latency versus initiation interval. Pipelined multiplies finish at times 3,4,5,6,7,8; the accumulator adds then finish at 4,5,6,7,8,9. Unpipelined multiplies finish at 3,6,9,12,15,18, and each one-cycle add finishes one cycle later; the last is 19. Gain=19−9=10 cycles. Pipelining changes the rate at which independent multiplies start, not each multiply's latency.

## Q50
**Correct answer:** 0.25

Concept: signed requantization. Original raw integer is −1.375·16=−22. Arithmetic shift rounds −22/4=−5.5 down to −6, representing −6/4=−1.5 in the new format. Truncation toward zero gives −5, representing −1.25. Absolute difference is 0.25. The binary scale changes as the fractional-bit count changes.

## Q51
**Correct answer:** A, C

Concept: safety versus current deadlock. Initially no remaining need fits available (0,0), so the state is unsafe, A. Adding only B gives (0,1), still enabling none, so B is false. Adding A gives (1,0): P can finish, making (1,1); R then finishes, making (2,2); Q can finish. C is true. Maximum claims need not be current requests, so unsafe does not itself prove actual deadlock; D is false.

## Q52
**Correct answer:** 8

Concept: overflow in an otherwise valid cancellation. For x=−4,...,3, doubling stays in −8,...,7 and exact halving recovers x: eight values. For x=4,...,7, the wrapped product is 2x−16 and halving gives x−8. For x=−8,...,−5, it is 2x+16 and halving gives x+8. None of these recover x. Algebraic cancellation can fail when the intermediate representation overflows.

## Q53
**Correct answer:** 7

Concept: tournament certificates for second maximum. Only keys directly defeated by the overall winner can be second largest; every other key lost to another nonmaximum key. Here there are exactly two such candidates. One further comparison determines the larger, and in the worst case that comparison is necessary because their mutual order is not fixed by the separate winning subtrees. Total=6+1=7. The winner's path length, not just total input size, controls the final selection cost.

## Q54
**Correct answer:** 10

Concept: ideals in a product order. In each row an ideal includes a prefix of columns. Let row-one prefix length be a and row-two length b. Downward closure requires 0≤b≤a≤3. For a=0,1,2,3 there are a+1 choices of b, total 1+2+3+4=10. Arbitrary subsets can omit a required predecessor and therefore are not ideals.

## Q55
**Correct answer:** 4

Concept: quantum tradeoffs. Steady-state useful fraction is q/(q+1), at least 0.8 iff q≥4. The fifth process starts after four quanta and four switches, at 4(q+1), at most 20 iff q≤4. Thus q=4 is the only choice. Initial-response time and steady-state efficiency impose different inequalities.

## Q56
**Correct answer:** C

Concept: ordered auto-increment addressing. Source read uses 100 and gives three, then R becomes 104. Destination read uses 104 and gives five, then R becomes 108. The sum eight is written to captured destination 104. C=(108,8). A and D omit an increment; B reads the wrong destination value. The explicitly stated evaluation order resolves reuse of the same address register.

## Q57
**Correct answer:** 112

Concept: slotted-page free space. Existing occupancy is 32+12·4+3900=3980 bytes, leaving 116. The new slot consumes four, leaving 112 bytes for its record. Compaction can gather fragmented free space but cannot eliminate existing metadata.

## Q58
**Correct answer:** B, C

Concept: finite-state value invariants. Starting at zero, x alternates between zero and one. B holds, while A fails for an odd number of iterations. Both values make x(x−1)=0, proving C and disproving D. The expression can be constant even when a constituent variable is not.

## Q59
**Correct answer:** 3.5

Concept: permutation and triangular solves. From PA=LU, solve Ly=Pb with Pb=(2,1,3). Forward substitution gives y1=2, y2=1−2·2=−3, and y3=3−(−1·2+3·(−3))=14. The last U row gives 4x3=14, so x3=3.5. Applying L to the unpermuted right-hand side would solve the wrong system.

## Q60
**Correct answer:** A, C

Concept: edge identities in multigraph DFS. Traversing one edge u→v and returning on the other forms the allowed length-two cycle, A. At v, only the entering edge should be ignored; the other edge to the already visited parent reveals the cycle, C. B incorrectly ignores both edges; D discards a structurally distinct edge. Parent-vertex exclusion assumes a simple graph.

## Q61
**Correct answer:** A, D

Concept: SSTF starvation under arrivals. The head alternates between tracks 0 and 1, each new nearby request being closer than track 100. Thus the far request can wait forever, A, disproving B. A finite request set decreases by one per completed service and cannot sustain this infinite pattern, so C is false and D true. Low immediate seek cost is not a waiting-time guarantee.

## Q62
**Correct answer:** 7

Concept: BST range pruning. Non-null visited nodes are 8,4,6,7,12,10,9. At 6 the left subtree is pruned because key>lo is false; at 10 the right subtree is pruned because key<hi is false. Five keys are reported, but the two boundary-search ancestors 4 and 12 are also visited, making seven. Reporting count and traversal count differ.

## Q63
**Correct answer:** B, D

Concept: sortable floating-point bit keys. Positive encodings grow with magnitude, so B. Negative raw encodings also grow with magnitude but that makes their numerical values smaller, disproving C. Raw unsigned ordering puts positive encodings before negative ones, disproving A. Complementing negatives reverses their magnitude order and places them below 0x80; flipping the sign bit of positives places them above. Thus D preserves increasing numeric order for the specified finite nonzero values. Excluding NaNs and signed-zero ties is important to the stated strict comparison.

## Q64
**Correct answer:** B

Concept: NAT mapping capacity. Policy I needs six distinct external ports, requiring ceil(6/4)=2 public addresses. Policy II needs only three port values for each remote endpoint and may reuse them across X and Y, fitting one address. B=(2,1). A ignores policy I's six mappings; C misses remote-endpoint reuse; D overstates both requirements. Mapping identity determines which flows compete for a port namespace.

## Q65
**Correct answer:** 0.6817

Concept: integrating an upper envelope. The crossing r in [0,1] solves r²=1−r, so r=(sqrt(5)−1)/2. The maximum is 1−x on [0,r] and x² on [r,1]. Integral=r−r²/2+(1−r³)/3. Using r²=1−r and r³=2r−1 reduces it to (5sqrt(5)−3)/12=0.6816949906…. Round to 0.6817; range 0.68165–0.68175. Integrating one branch over the entire interval would miss where the larger function changes.
