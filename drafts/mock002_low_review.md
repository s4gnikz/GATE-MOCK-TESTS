# Mock 002 — independent core one-mark review

Reviewed 2026-10-13. Scope: the 20 records in `mock002_core_low.json`, compared with the complete student-facing Mock 001. This is a separate model's mathematical/conceptual review, not human review or executable verification. The source read included proposed answers and solutions; therefore this is not a blinded review. Each answer below was rederived from the statement rather than accepted solely on agreement with the author. No new Python utilities were created.

All 20 proposed answer values/sets are technically correct. Release still requires the editorial and difficulty work below and the other 45 questions' reviews. Uniqueness judgment here is limited to comparison with Mock 001 and within this subset; it is not a commercial-paper or internet-wide originality guarantee.

## Per-question findings

### Q11 — answer 4; technically sound; Medium

All blocks are even, so all use set 0. Tracking the two entries in least-to-most-recent order gives `[0]`, `[0,2]`, `[2,0]`, `[0,4]`, `[4,2]`. Only the third access is a hit. Four misses is an exact integer NAT answer. Mapping followed by recency tracking gives two meaningful steps. Distinct from Mock 001's average-memory-access-time tradeoff.

### Q12 — answer C (4); technically sound; Medium

Root A cannot have a single child B: B would then be the penultimate postorder symbol, whereas D is. The first child subtree closes at B in postorder and contains B,C; the other contains D,E. Each has one child whose left/right orientation is free. Thus 2 times 2 = 4. A ignores both freedoms, B counts only one, D improperly grants A an orientation freedom although A has two children. Medium-Hard is an overestimate for this short traversal reconstruction. No corresponding pilot task.

### Q13 — answer 6; sound but difficulty revision required

The crossing pairs are (2,1), (6,1), (6,4), (9,1), (9,4), (9,8), totaling 6. The exact NAT is correct. However, directly comparing two three-element lists after defining cross inversion is essentially a single counting step. The metadata's two reasoning steps are not justified. Strengthen the task before release; for example, combine comparison observations during a partial merge with inference of an unknown rank and then inversion counting. Do not merely enlarge or change the arrays. Mock 001's insertion-sort question counts additional equal-key shifts, a different reasoning task, although both concern sorting pair counts.

### Q14 — answer B; technically sound; Medium

DMA reads memory, whose version remains stale while dirty cache lines hold the updates. Completing write-back before DMA establishes the required data visibility. A discards updates; C changes notification only; D makes the stated startup sequence impossible and does not publish cache data. The assumptions rule out subsequent CPU modification and hardware coherence. A good conceptual one-mark item, though D is a weak distractor. No pilot duplicate.

### Q15 — answer B; technically sound; Medium

The properly nested DFS intervals place v below u. DFS tree edges give a directed u-to-v path; the specified return edge closes a directed cycle. Thus B alone is necessary. A and C misclassify the edge, and D contradicts the resulting cycle. Interval inference followed by path closure provides meaningful two-step reasoning. No pilot duplicate.

### Q16 — answer A,C,D; wording fix required; Medium

Since x has a right child, its successor is the minimum of that right subtree. It lies there (A) and has no left child (C). It can have a right child (D): x=10, right child=15, and 15's right child=20 is a witness. That witness disproves B. Replace the stem's final sentence with **"Which statements are correct?"** The current "necessarily true" formulation unnecessarily mixes universal structural claims with the existential phrase "may have". The intended answer survives this edit. No pilot duplicate.

### Q17 — answer 3; technically sound; Medium

The active sets after epsilon closure are initially {0}, after the first a {0,1,2}, after the second a {0,1,2}, and after b {1,2,3}. The last set follows 3-to-1-to-2 epsilon edges. Thus size 3, exact NAT. Acceptance states are unnecessary because only the active set is asked for. Relabel from Medium-Hard to Medium: this is a short deterministic simulation. Distinct from pilot DFA minimization.

### Q18 — answer A; technically sound; Medium

Let the initial b,c values be u,v. The successive assignments produce a=u+v, b=u, c=v. A therefore preserves all final values. For B choose u=1,v=2: b changes incorrectly to 2. For C the same values give c=3 instead of 2. For D, b=3 and c=0 are both wrong. Exact-integer and no-alias assumptions adequately avoid overflow or observability complications. Three substitutions do not make this Medium-Hard. Distinct from pilot short-circuit/side-effect optimization.

### Q19 — answer D; technically sound; Medium

Every finite tree is a single chain of nonterminals ending in S-to-ab. For ab the chain has no extra production; for aab it has only aS; for abb only Sb. For aabb it has both aS and Sb, which can occur in either order, giving exactly two ordered trees. Hence only D. Relabel Medium: the chain characterization makes this a short ambiguity exercise. Mock 001 Q32 concerns infinitely many trees created by nullable binary recursion; the current finite prefix/suffix nesting mechanism is meaningfully different, despite the shared ambiguity concept.

### Q20 — answer 4; technically sound; Medium-Hard

At convergence, distances to C are A=2, B=1. In round 1, A still uses B's old 1, so A=min(10,1+1)=2; B has lost its C link and advertises 1+2=3. In round 2, A=min(10,1+3)=4. The simultaneous-update convention is explicit and removes the usual timing ambiguity. Exact NAT 4. This two-round stale-information effect is distinct from the pilot network problems.

### Q21 — answer A,C; technically sound; Medium

Three significant bits give spacing 1/4 on [1,2), and 1/2 on [2,4). Therefore 1.125 is the midpoint of 1.0 and 1.25; the trailing retained bit in 1.00 is even, so A holds. B's spacing is false. The exact sum 1.75+0.25=2 is representable, so C holds. D fails at 9, which would require 1.001 times 2 cubed (four significant bits); 8 and 10 are the neighbouring values. Add a space in "leading 1". Unlike pilot fixed-point multiplication, this tests binade spacing and rounding parity.

### Q23 — answer A,D; technically sound; Medium-Hard

Each concrete path yields z=5, proving A. At the join, x receives two unequal constants, so B is false; y likewise loses its constant. The stated nonrelational domain retains no x+y correlation, so C is false. Computing z inside each branch gives the same incoming constant 5 and preserves it across the join, proving D. This is a useful concrete-versus-abstract reasoning task, not present in the pilot.

### Q25 — answer A; sound but difficulty revision required

From the query point, the only later read is y in return. The old x is killed, and a,b,c have no subsequent uses. Thus A={y}; B wrongly includes killed x, C includes past-used c, and D includes all past inputs. Supplying the entire liveness definition and selecting a point directly before a trivial overwrite makes this easier than the requested level. Strengthen using a branch or back edge and ask for a particular live-in set requiring a union or fixed-point step. The answer is correct for the present version. No pilot liveness duplicate.

### Q26 — answer C; technically sound; Medium

XOR cancels the duplicated x, leaving (y AND z) XOR ((NOT y) AND z). When z=0 the result is 0; when z=1 exactly one AND term is 1. Hence D=z, proving C. Counterexamples: x=0,z=1 disproves A; y=0,z=1 disproves B; z=0 disproves D. This changes the task from pilot Boolean equivalence/minimization to sensitivity under input complementation and is not a trivial reparameterization.

### Q27 — answer 2; technically sound; Medium

SRTF order and intervals are A:0–2, B:2–4, C:4–5, B:5–7, A:7–12. Completion times (12,7,5) imply waits (5,1,0). Their average is 2 time units, exact NAT. No ties occur, so no tie-break rule is needed. Two preemptions followed by wait calculation is a solid medium item; Medium-Hard overstates it. No corresponding pilot scheduling simulation.

### Q28 — answer C; technically sound; Medium-Hard

C is never generated from another attribute. A and B determine each other, so the minimal keys are AC and BC. All attributes are prime, satisfying 3NF for the closure of the dependencies, but A-to-B and B-to-A have non-superkey determinants, violating BCNF. Therefore A and B incorrectly reject lower normal forms, C is correct, D is false. The stem's "exactly ... implied" wording prevents hidden additional dependencies. Repair spaces in options: "not 2NF", "not 3NF". No pilot normal-form duplicate.

### Q30 — answer 175; technically sound; Medium

Incoming payload is 1020−20=1000 bytes. The outgoing payload capacity is 620−20=600 bytes, already a multiple of 8. The first fragment covers 600 bytes from original offset 100; the second starts at 100+600/8=175. Both outgoing fragments inherit the fact that later original data exists, consistent with MF=1; the second's 400-byte payload is also 8-aligned. Exact NAT 175. Relabel Medium; the ordinary formula has one important existing-offset trap. Add spaces around all quantities and units. No pilot fragmentation duplicate.

### Q31 — answer 120; sound but difficulty revision required

The stated LOOK rule directly yields 50→70→90→40→10 and movement 20+20+50+30=120. Exact NAT correct. Because the stem gives the full scheduling rule, the requested operation is simple ordering and subtraction. Strengthen via a precisely timed new request or a comparison of two defined policies with an inferred initial direction; ensure the event convention is explicit. No pilot disk-scheduling duplicate.

### Q32 — answer C (4); technically sound with assumption clarification; Medium

If producer 1 enters IF at cycle 1, WB is cycle 5. Consumer 2 must read at ID cycle 5 or later, hence IF cycle 4, requiring two intervening NOPs. Its WB is cycle 8, so consumer 3 must enter IF at 7, requiring two further NOPs. Total 4. A repairs only one gap, B leaves one gap too short, and D needlessly forbids the explicitly allowed same-cycle read/write. Add **"The inserted NOPs must preserve sequential execution results for arbitrary initial register values."** This prevents exploiting coincidentally correct preexisting values (the instructions all produce related zero-like results if R0 is assumed to be zero). Relabel Medium. No pilot pipeline scheduling task.

### Q34 — answer C (5); technically sound; Medium

Number the first slot s from 0 to 7. The range covers floor((s+15)/8)+1 data pages: two at s=0, three for s=1 through 7. Add the specified two index reads to obtain maximum 5. A omits index reads; B only counts the aligned case; D overcounts beyond the largest span. The two-page index cost is explicitly given, so no B-tree convention is needed. Relabel Medium, not Medium-Hard. No corresponding pilot file-page alignment task.

## Required editorial pass

Restore spaces in the source solution prose, including "set 0", "references 0 and 2", "value 2", "state 0", "round 1", "advertises 0", "length 1020 bytes", "cylinders 0 through 99", "matches exactly 16", and similar concatenations throughout. Preserve mathematical notation but do not print prose such as "giving2*2" or "notBCNF". This is a readability issue affecting student-facing solutions as well as draft metadata.

## Overall recommendation

No answer-key correction is needed for these current stems. Make the Q16 wording fix and Q32 all-initial-values clarification; strengthen Q13, Q25, and Q31; then reassess paper-wide difficulty using the review's lower estimates rather than forcing the blueprint labels. The remaining routine one-mark items can appropriately serve the medium portion of a paper whose two-mark section supplies depth. All 20 families are distinct from the accepted pilot at the reasoning-task level, with the specific conceptual overlaps discussed above.

## Revision review — direct Markdown edition

Re-read the revised Q13, Q16, Q25, Q31 and Q32 in `mock002_front_questions.md` and their explanations in `mock002_front_solutions.md`. The revised questions supersede the earlier draft for the findings below. Review remains model-based, not human review.

### Revised Q13 — accept answer 6; Medium-Hard

Represent a merged order by four L symbols and three R symbols. Its inversion count is the number of R-before-L pairs. Exhausting L in at most five comparisons places at most one R before the final L, permitting at most four inversions. Exhausting R in at most five comparisons leaves at least two L symbols afterward, forcing at least six inversions. Exactly five rules out both possibilities, so at least six comparisons are required. The merged pattern L,R,L,R,L,L,R has 3+2=5 cross inversions and exhausts L on the sixth comparison; left [1,3,5,6], right [2,4,7] realizes it. The answer and supplied solution agree. This is a meaningful redesign involving a lower-bound proof and an attaining example, distinct from the pilot sorting problem. The original difficulty objection is resolved.

### Revised Q16 — accept A,C,D; Medium

The new question asks which statements are correct and removes the universal/existential wording clash. The original successor proof and all distractor checks remain valid. Wording objection resolved.

### Revised Q25 — accept A; Medium

At P the assignment reads the current z immediately and kills the current y. Following the back edge, L overwrites the current x before the branch could read x through a return. The branch reads flag without any intervening flag definition. Therefore precisely z and flag are live at P. B incorrectly retains old x; C incorrectly retains old y; D incorrectly retains both. Tracking definitions across the back edge supplies the previously missing reasoning depth. No extra live variable can arise through further loop iterations because every route from P first performs these kills. The answer and solution are correct; difficulty objection resolved.

### Revised Q31 — accept 205; Medium

The initial upward sweep reaches 70 at t=20, then 90 at t=40. With 10 still pending and nothing farther upward, reversal occurs at 90. At t=45 the head is at 85 moving downward; the new 95 request is behind it, and the explicit policy forbids an early reversal while 10 remains ahead. Arrival at 10 occurs at t=120, followed by 85 additional cylinders upward to 95. Total distance is 40+80+85=205. No arrival coincides with a service or reversal event, so no event-order ambiguity remains. The supplied answer and solution agree. Dynamic arrival interpretation gives the task appropriate medium depth; original difficulty objection resolved.

### Revised Q32 — accept C (4); Medium

The new requirement of correctness for arbitrary initial register values excludes reliance on stale values accidentally equalling the computed values. Each producer-consumer pair independently requires consumer ID no earlier than producer WB. Their IF stages must therefore be at least three cycles apart, requiring two NOPs in each of two gaps. Four total is both sufficient and necessary. All original option explanations remain valid; assumption objection resolved.

### Revision outcome

All five revised items pass this conceptual and editorial-content review. The direct Markdown files still contained concatenated prose tokens elsewhere when inspected (for example "initial state0", "round1", "not2NF"); the earlier general spacing pass remains necessary. Add blank lines before the next heading after Q13, Q25 and Q31 for consistent Markdown source formatting. The revised content needs no answer correction.
