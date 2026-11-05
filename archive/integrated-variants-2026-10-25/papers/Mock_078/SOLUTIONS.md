# Worked Solutions — Mock Test 078

## Q1

**Correct answer:** A, C

An existing auditor is a reviewer and therefore not an intern, proving A. The same containment/exclusion argument applies to all auditors, proving C. Non-interns need not be auditors, so B is not implied. Nothing requires interns to exist, so D is not implied. Existential information must be carried only through justified set inclusions.

## Q2

**Correct answer:** B

The combined map is (x,y)→(y+2,x−1). Matching (5,3) gives y=3,x=4, so B. A maps to (6,2), C to (3,5), and D to (8,0). Reversing a composition requires undoing the translation before the reflection.

## Q3

**Correct answer:** B
**Concept:** Ordering constraints.

A must precede B, and B must precede C, so B can be neither first nor last. A can be first in A,B,D,C. C can be last in that same order. D can be first in D,A,B,C. Thus A,C,D do not meet the stated condition, and B does.

**Common misconception:** Not every position must be uniquely determined to exclude both extreme positions for a runner.

## Q4

**Correct answer:** 2

Fix one specified person to remove rotations. The other specified person must sit opposite. The two remaining distinct people can occupy the remaining seats in2! ways. Reflections are distinct, so these two are not identified.

## Q5

**Correct answer:** A, C
**Concept:** Weighted averages and composition effects.

P improves from 80% to 90%; Q improves from 20% to 30%, so A is true. Combined success falls from 100/200=50% to 36/100=36%, making B false. Q's application share rises from 100/200=50% to 90/100=90%, so C is true. D is false: the table neither follows comparable individuals nor identifies a causal policy effect.

**Common misconception:** An aggregate percentage can fall while each group's percentage rises, because the group weights change.

## Q6

**Correct answer:** 4

**Concept:** Reflecting a notch across two folds.

The triangular removal occupies one quadrant around the original centre. Unfolding reflects its diagonal cut into the other three quadrants. The four reflected diagonal segments form a square rotated relative to the paper's edges, with four sides.

**Common misconception:** Counting the fold edges as exposed hole edges after unfolding.

## Q7

**Correct answer:** C

Concept: inconsistent cyclic evidence and an independent constraint. If each cyclic log entry in turn is the sole false one, the possible chronological orders are R,S,P,Q; S,P,Q,R; P,Q,R,S; Q,R,S,P. The reliable R-before-P record retains only R,S,P,Q and Q,R,S,P. Both place S before P, making C necessary. A and B hold only in the second retained order, not the first. D contradicts the reliable record. One cannot discard an arbitrary log entry without checking the other three together.

## Q8

**Correct answer:** 0.75

Describe an outcome by its repeated value r and singleton s. The condition max=5 permits r=5,s∈{1,2,3,4}, or s=5,r∈{1,2,3,4}: eight choices. Each corresponds to three equally likely dice-position orders. The sum2r+s is odd exactly when s is odd. Two choices in the first group and all four in the second qualify, so probability6/8=3/4. Counting only which face values occur would be unsafe without checking their equal numbers of ordered outcomes.

## Q9

**Correct answer:** A

Corroboration supplies supporting evidence, while the second clause withholds proof of the explanation. A preserves both. B reverses support, C exaggerates it to universal proof, and D mistakes evidentiary support for repetition of wording. Support for an observation and support for its proposed cause are distinct.

## Q10

**Correct answer:** 9

After k multiplications the quantity is3×2^k. At k=8 it is768, while at9 it is1536. Monotonic growth makes9 the first value exceeding1000. The initial value3 is not itself a multiplication.

## Q11

**Correct answer:** 65534
**Concept:** End-around carry in one's-complement checksums.

The ordinary sum is 0x10000. Fold the carry into the low word to obtain 0x0001. Its 16-bit complement is 0xFFFE, decimal 65534. Discarding the carry would instead yield the wrong checksum 65535.

**Common misconception:** One's-complement addition is not ordinary addition modulo 2¹⁶.

## Q12

**Correct answer:** A

**Concept:** Eliminating the changing K-map variable.

Only a differs, while b=c=0, leaving b′c′, A. B and C improperly retain a and drop a fixed variable; D does not describe the two minterms' union.

**Common misconception:** Dropping a fixed literal rather than the bit that changes within the group.

## Q13

**Correct answer:** A

Concept: dead stores. No operation reads the first stored value before the second assignment overwrites it; removing that store preserves behavior (A). B invents an invalidity rule; C contradicts print's use of x; D would remove the value that print requires. The side-effect assumption is essential.

## Q14

**Correct answer:** A, C

**Concept:** Characteristic polynomial and diagonalization.

The characteristic polynomial is (λ−2)(λ+1)=λ²−λ−2. Cayley–Hamilton gives A²−A−2I=0, proving A. Distinct real eigenvalues give two independent real eigenvectors, proving C. The determinant is −2, so B is false. For example, the upper triangular matrix with rows (2,1),(0,−1) has these eigenvalues but is not symmetric, refuting D.

**Common misconception:** Confusing real diagonalizability with orthogonal diagonalizability of symmetric matrices.

## Q15

**Correct answer:** B

**Concept:** Availability of expressions after operand redefinition.

p contains the product using the old a, while q uses the input value, which may differ. B explains why the expression is no longer available for reuse. A is an incorrect universal prohibition, C is not implied, and D contradicts the first assignment.

**Common misconception:** Matching expression text without tracking its operands' reaching values.

## Q16

**Correct answer:** B
**Concept:** Precedence-preserving intermediate code.

Multiplication must compute b*c before the addition to a, as in B. A groups (a+b)*c; C changes the products; D computes separate values without combining a with b*c as required.

**Common misconception:** Three-address temporaries must preserve the original expression tree's dependencies.

## Q17

**Correct answer:** 2

At the first character, >> matches two characters; >>= does not match because the third character is >. The remaining >= is one token. Total2. Maximal munch is applied anew at each current position.

## Q18

**Correct answer:** B

Concept: recognizability versus decidability. The existing acceptance guarantee plus halting rejection for every nonmember gives a correct total decision procedure (B). A only describes tape symbols; C gives a single successful case; D holds for recognizers that may loop and therefore is insufficient. Deciders must halt on all inputs.

## Q19

**Correct answer:** B

Concept: mean value theorem bounds. The increase f(3)−f(0) lies between 2·3 and 5·3, so 7≤f(3)≤16. B's value ten is achieved by f(x)=1+3x. A is below seven, C and D exceed sixteen. Bounding derivatives constrains endpoint differences, not just local slopes.

## Q20

**Correct answer:** 0.75

P(B and defective)=0.5×0.3=0.15. Total defective probability is0.5×0.1+0.5×0.3=0.20. The posterior is0.15/0.20=0.75. Equal factory-selection probabilities do not imply equal probabilities after defect information.

## Q21

**Correct answer:** B

**Concept:** Algorithms — Graph traversals

Nested intervals show that u is a proper ancestor of v in the DFS forest. The tree path from u to v consists of directed edges. Adding v→u closes a directed cycle; v→u is a back edge. Thus only B follows.

- **A:** False: a tree edge runs from an ancestor to a newly discovered descendant, not back to an ancestor.
- **B:** True: the tree path u to v together with v→u is a directed cycle.
- **C:** False: the nested intervals identify an ancestor relationship, not separate branches.
- **D:** False: this return edge closes a cycle.

**Common misconception:** Nested DFS intervals alone do not imply acyclicity; edge direction matters.

## Q22

**Correct answer:** 20

The root is5. Its left subtree is rooted at3 with children1,4; its right subtree is rooted at7 with right child8. Root5 must be first. The three left-subtree insertions can interleave with the two right-subtree insertions in C(5,3)=10 ways. The left subtree has two valid orders,3,1,4 and3,4,1; the right has only7,8. Total10×2=20. Subtree interleavings preserve internal ancestor-before-descendant requirements.

## Q23

**Correct answer:** B

**Concept:** Distinct meanings of unsigned carry and signed overflow.

The unsigned addition is128+254+1=383=256+127. Thus the low bits are01111111 and carry-out is1. Signed interpretation computes−128−1=−129, outside the signed8-bit range, so overflow is1. B states all three correctly. A misses carry and overflow. C has the wrong result and overflow. D gives the right result and overflow but the wrong carry-out.

**Misconception:** Assuming that carry-out and signed overflow are mutually exclusive or equivalent indicators.

## Q24

**Correct answer:** A, B, D

Meet and join in a subset lattice are intersection and union, giving{b} and{a,b,c}. Thus A,B are true. Neither set contains the other, so C is false. The empty set is contained in every subset, proving D. Lattice order is inclusion, not cardinality alone.

## Q25

**Correct answer:** 2
**Concept:** CIDR alignment and exact coverage.

The blocks 192.0.2.32/27 and 192.0.2.64/27 cover 32–63 and 64–95. A single 64-address /26 block must begin at a multiple of 64, so it cannot begin at 32. Larger blocks include extra addresses. Therefore two are necessary and sufficient.

**Common misconception:** A power-of-two address count is insufficient for a single CIDR block without boundary alignment.

## Q26

**Correct answer:** 2

The old word has5+8=13 bits; the new one has3+8=11. Savings are2 bits. Six combinations fit in3 bits, but the unchanged address field must still be counted in both widths.

## Q27

**Correct answer:** 3 (exact)

**Concept:** Theory of Computation — Regular expressions and finite automata

1. Track E0: even b count but not currently accepting; E1: even b count and last symbol a; O: odd b count. In O the last symbol does not affect future acceptance, so one state suffices.
2. Transitions are E0 --a--> E1, E1 --a--> E1, both E states --b--> O; O --a--> O and O --b--> E0. E0 is initial and E1 alone accepts.
3. E1 is distinguished from the others by the empty suffix; E0 and O are distinguished by suffix a. All three are reachable, proving minimality.

**Common misconception:** The naive product construction can contain equivalent states.

## Q28

**Correct answer:** B

Reclaiming a resource removes the no-preemption condition and can let one process finish, breaking the circular wait execution. Priorities, an unrelated ready process, and CPU speed do not release either held resource, so A,C,D do not resolve this resource cycle. Scheduling progress elsewhere is not resolution of the deadlocked pair.

## Q29

**Correct answer:** B, C

Concept: MST uniqueness conditions. Pairwise distinct weights guarantee a unique MST, B. A graph already a tree offers only its own spanning tree, C, even if all weights are equal; this disproves A. A bridge must be included in every spanning tree regardless of weight, disproving D. Distinct weights are sufficient, not necessary, for uniqueness.

## Q30

**Correct answer:** C

Scores are(6+3)/3=3, (8+4)/4=3 and(5+1)/1=6. R has the largest, so C is correct; P,Q do not win and D incorrectly equates all scores. Waiting time is normalized by service demand.

## Q31

**Correct answer:** 0

**Concept:** Eigenvectors and singularity.

For v=(1,−1,1,−1)ᵀ, Pv=−v. Consequently (I+P)v=0 with v nonzero, so I+P is singular and has determinant zero.

**Shortcut:** Find a null vector instead of expanding a 4×4 determinant.

**Common misconception:** Assuming that adding the identity to an invertible matrix preserves invertibility.

## Q32

**Correct answer:** B
**Concept:** Heap deletion and sift-down.

Move 3 to the root and remove the last slot: [3,8,7,6,5,4]. Swap with larger child 8, then larger child 6, giving [8,6,7,3,5,4]. A unnecessarily sorts the keys; C violates root heap order; D swaps the wrong lower-level elements.

**Common misconception:** A heap is partially ordered; deleting its root does not sort the remaining array.

## Q33

**Correct answer:** A, C

For non-NULL a values, UNIQUE excludes repetitions, proving A. NOT NULL on b proves C but imposes no uniqueness, so B is false. Neither constraint requires every value to occur, so D is false. Constraints restrict stored rows; they do not populate absent rows.

## Q34

**Correct answer:** 2

x XOR x is always0, so the output is0 OR y=y. The assignments with y=1 and either x value produce1, giving two. Tied inputs are not independent signals.

## Q35

**Correct answer:** C

Both tuples share B=2 but differ in A, directly violating B→A, so C. A→B holds in this instance because A values are distinct. B,D are trivial dependencies from the combined attribute set. An instance satisfying a dependency does not establish it as a constraint on all future instances.

## Q36

**Correct answer:** 9233
**Concept:** Two-level address translation.

The virtual page number is 35=2×16+3, giving root index 2 and leaf index 3. The mapping supplies physical frame 9, while the byte offset stays 17. Physical address is 9×1024+17=9233.

**Common misconception:** Translation changes the page/frame number, not the offset within the page.

## Q37

**Correct answer:** B

**Concept:** Key–foreign-key join cardinality.

Every R tuple finds at least one S tuple by the foreign key and at most one by the key of S. Hence exactly 100 joined tuples result. Set projection cannot collapse them here because the join includes all R attributes: distinct R tuples remain distinct. A contradicts the foreign key; C ignores uniqueness in S; D ignores the exact bound established by both constraints.

**Common misconception:** Assuming every join can expand to the Cartesian-product size regardless of keys.

## Q38

**Correct answer:** A, B, D
**Concept:** Absolute-value integration and parameter inequalities.

Split at x=t: I(t)=t²/2+(1−t)²/2=(t−1/2)²+1/4. The minimum and its unique location prove A. Symmetry gives I(1−t)=I(t), so their sum is at least 1/2, proving B. Integration gives ∫(t²−t+1/2)dt=1/3, not 1/2, refuting C. The last inequality becomes (t−1/2)²≤1/16, hence t∈[1/4,3/4], proving D.

**Common misconception:** Integrating an absolute value requires determining where the inner expression changes sign.

## Q39

**Correct answer:** 3072

The valid mappings use distinct frames3,7,9. Pages0 and4 alias frame3, so counting virtual pages would double-count its addresses. Three frames each supply1024 distinct byte addresses, total3072.

## Q40

**Correct answer:** A, B

**Concept:** Precedence and associativity encoded in grammar levels.

Multiplication is built inside T before addition combines T terms, establishing A. Left-recursive addition groups chains on the left, establishing B. Immediate left recursion causes naive recursive descent to recurse without consuming input, refuting C. The separated precedence levels give the unique parse id+(id*id), refuting D.

**Common misconception:** Assuming left recursion implies ambiguity rather than an implementation issue for naive top-down parsing.

## Q41

**Correct answer:** 3

Original path s→a→b→c has weight 3−4+2=1, less than the alternative weights 10 and 10. Reweighting changes every s-to-c path by the same amount h(s)−h(c)=2, hence the new distance is 3. Direct transformed edge weights are 3,12,0,0,9 respectively; the same best path has cost 3. Potential differences telescope over an entire path.

## Q42

**Correct answer:** 6

**Concept:** Strict inversions in stable insertion sort.

The leading 4 forms inversions with all four later elements. The 3 forms two more with the later 1 and 2. No other inversions exist; equal 1 values are not shifted past one another. Each strict inversion causes one shift, for six shifts.

**Common misconception:** Counting equal-valued pairs as inversions in a stable implementation.

## Q43

**Correct answer:** 122

Initially the records occupy330 bytes and metadata occupies32+6·4=56, leaving126 free. Deleting adjacent80- and50-byte records creates a130-byte hole. A new slot consumes4 bytes from the free gap, leaving122 there; without moving records the largest available record region is max(130,122)=130. With compaction, total free record space is126+130−4=252. Increase252−130=122. Slot entries retained by deletion are not reclaimed.

## Q44

**Correct answer:** 2

Insert 6 into the left leaf, producing[2,5,6]. Inserting 7 produces[2,5,6,7], split into[2,5] and[6,7]; separator 6 is added alongside the existing separator 8. The root now has three leaf children and two keys, within its capacity. Leaf promotion copies rather than removes the separator key from the new leaf.

## Q45

**Correct answer:** 2

Insertions place0,7,14,1 in slots0,1,2,3. Clearing slot1 makes a search for14 start at0, inspect key0, then stop at empty1 before reaching2. A search for1 starts at empty1 and also fails. Key0 remains findable immediately. Thus two stored keys become false absences. A tombstone would preserve continuation through the deleted slot.

## Q46

**Correct answer:** C

**Concept:** Undo/redo recovery.

T1 committed, so recovery ensures its X=8 update is present through redo if necessary. T2 did not commit, so its Y=9 update must be undone to Y=4 if it reached disk. The final pair is (8,4), C. A loses committed work, B retains uncommitted work, and D does both.

**Common misconception:** Letting the accidental precrash disk state determine the final recovered values.

## Q47

**Correct answer:** 3.5

The absolute-deviation objective is minimized at every median, here every x in[0,4]. The squared-deviation objective is minimized at the mean(0+0+4+10)/4=3.5. That mean lies inside the permitted first-stage minimizer interval, so3.5 is selected. The second criterion resolves the first criterion's nonuniqueness.

## Q48

**Correct answer:** 2

The first symbol forces the production aSbS. Its displayed b can match the second or fourth symbol of abab. Matching the second leaves the inner S empty and the final S generating ab. Matching the fourth leaves the inner S generating ba and the final S empty. Each two-letter substring has one derivation, and the empty substring must use ε. Thus there are exactly two leftmost derivations. Different orders of expanding nonterminals are excluded by the leftmost requirement.

## Q49

**Correct answer:** 16 (exact)

**Concept:** Operating Systems — Virtual memory

Each second-level table covers 1024 virtual page numbers. Directory indices are floor(VPN/1024): the four mapped pages use indices 0,0,1,1023. Thus three distinct second-level tables are needed, in addition to one directory. Four pages times 4 KiB per page gives 16 KiB.

**Common misconception:** Four mapped data pages need not require four second-level tables; shared high-order address bits determine table reuse.

## Q50

**Correct answer:** A, B, C

Left cancellation makes x↦ax injective. On a finite set it is then surjective, proving A and giving b with ab=e, proving B. Now a(ba)=(ab)a=a=ae, so cancellation yields ba=e, proving C. On an infinite set an injective map need not be surjective; nonnegative integers under addition supply a cancellative monoid with noninvertible positive elements, disproving D.

## Q51

**Correct answer:** 4
**Concept:** Zero-weight edges and shortest simple paths.

Every s-to-t path must pay one unit leaving s and one entering t, so its weight is at least two. Paths s-a-t, s-b-t, s-a-b-t, and s-b-a-t each attain two. These exhaust simple paths because only a,b can be internal vertices. Thus the count is four.

**Common misconception:** Counting walks instead would permit repetitions around a zero-weight cycle and change the problem fundamentally.

## Q52

**Correct answer:** 0.5
**Concept:** A minimax lower bound and construction.

Let M=max|p(x)|. The identity p(−1)+p(1)−2p(0)=2 holds for every monic quadratic. By the triangle inequality, 2≤|p(−1)|+|p(1)|+2|p(0)|≤4M, so M≥1/2. The polynomial x²−1/2 stays in [−1/2,1/2] on the interval and attains the bound. Thus the minimum is 0.5.

**Common misconception:** Optimizing only at a stationary point does not by itself bound the maximum over the whole interval.

## Q53

**Correct answer:** 0.5

There are 2^10 total locations but only 2^9 distinct supplied addresses because A9 is fixed. All nine lower bits vary independently, so exactly half the locations are reachable: 2^9/2^10=0.5. Chip selection enables the device; it does not provide an additional internal address bit.

## Q54

**Correct answer:** 80

Sequential object retrieval costs3×40=120 ms after the HTML. Pipelining costs one40 ms RTT under the stated negligible-size model. The saved time is80 ms. The common DNS20, handshake40 and base40 cancel; totals are220 versus140 ms. Do not re-charge connection establishment for each object on a persistent connection.

## Q55

**Correct answer:** 4 (exact)

**Concept:** Compiler Design — Syntax-directed translation

The postfix code is `a b + c d e * + *`. Stack depths after successive tokens are 1, 2, 1, 2, 3, 4, 3, 2, 1. The maximum is 4. Equivalently assign a leaf peak 1 and a binary node peak max(left.peak, 1 + right.peak): the left result must remain on the stack throughout evaluation of the right subtree.

**Common misconception:** Expression-tree height alone does not give stack depth without the operand evaluation order.

## Q56

**Correct answer:** 4

Concept: Mealy-style output to Moore-state memory. A reached state must encode the preceding bit for the next output and the output currently displayed. All four pairs (preceding bit,last output) are reachable. States with different displayed outputs are distinct immediately; states with the same displayed output but different preceding bits produce different outputs upon the next zero. Thus four are necessary and sufficient. The initial state can share the state for (0,0), since its initial output is ignored.

## Q57

**Correct answer:** A

**Concept:** Computer Organization and Architecture — Memory hierarchy and performance

The expected additional cost of an L1 miss is 6+0.20×60=18 ns. The initial mean is 1+0.10×18=2.8 ns. The redesigned mean is t+0.05×18=t+0.9 ns. Strict improvement requires t+0.9<2.8, or t<1.9 ns. The L2 miss probability is local, so only the fraction 0.10×0.20 (or 0.05×0.20) of all accesses reaches memory.

- **A:** True: the redesign saves 0.9 ns of expected miss cost, so L1 can rise by less than that.
- **B:** False: it ignores the redesigned system's remaining 0.9 ns expected miss cost.
- **C:** False: this is sufficient but not necessary; for example t=1.8 ns also improves performance.
- **D:** False: values such as t=3 ns satisfy it but are slower than the original.

**Common misconception:** Local miss rates must be multiplied along the hierarchy, and a hit-time increase affects every access.

## Q58

**Correct answer:** B

p−1=a+3 points to the last actual element and may be dereferenced. p itself is one-past, so A,D dereference outside the array. p+1 goes beyond even the permitted one-past pointer, making C invalid. Forming a boundary pointer does not authorize reading at it.

## Q59

**Correct answer:** 4

Concept: nonassociativity of saturation. b⊕c=1, then a⊕1=7. In the other grouping a⊕b saturates 11 to 7, then 7⊕(−4)=3. Exact final difference=7−3=4. Saturated intermediate information cannot be recovered by a later subtraction.

## Q60

**Correct answer:** A, C

Later by-reference accesses need live storage, proving A. Lifetime-preserving allocation or another valid mechanism can supply it, proving C. A dangling pointer to reused stack storage does not suffice, refuting B. Lexical visibility is not a storage-lifetime guarantee, refuting D.

## Q61

**Correct answer:** 2

With three significant bits, representable values near 8 are 8,10,12,14. The exact sum 9 ties between 8=1.00×2³ and 10=1.01×2³, so ties-to-even selects 8. Thus (a+b)+c rounds to 8 twice. On the other side b+c=2 exactly and a+2=10 exactly. The final difference is 10−8=2. Floating-point addition need not be associative.

## Q62

**Correct answer:** A
**Concept:** Circular-array indices and occupancy.

Initially occupancy is (2−6) mod 8=4. The operations change head/tail as follows: dequeue (7,2), enqueue (7,3), enqueue (7,4), dequeue (0,4), enqueue (0,5). Occupancy is 4−1+1+1−1+1=5, agreeing with (5−0) mod 8. A is correct; B has the right indices but inconsistent occupancy, and C,D miscount index advances.

**Common misconception:** Index wraparound does not reset queue occupancy to zero.

## Q63

**Correct answer:** 4
**Concept:** Selective-repeat buffering and contiguous delivery.

Receiving 0 delivers it and moves the lower edge to 1. Packets 2 and 3 are buffered while 1 is missing; the lower edge stays 1. Arrival of 1 enables delivery of 1,2,3 in order, moving the lower edge to 4. Sequence-space wraparound is not reached in these four arrivals.

**Common misconception:** Receiving a higher sequence number alone does not move the lower edge past a missing packet.

## Q64

**Correct answer:** C

**Concept:** State-cycle analysis and input counting.

Input 1 cycles 01→10→11→01, while input 0 resets to 01. Acceptance therefore requires the trailing run of ones to have length divisible by three. At length five, a string containing a zero is accepted with trailing run length 0 or 3: respectively 16 strings ending in 0 and two ending in 0111 (one free prefix bit). The all-one string has five trailing ones and is rejected. Total 18, option C. A omits the trailing-three case; B includes only one of its two prefixes; D exceeds the exhaustive count.

**Common misconception:** Counting all ones rather than only those after the last reset.

## Q65

**Correct answer:** B

**Concept:** Copy propagation and killed facts.

Before the assignment y=5, x and y have the same value, so the use in z may be replaced. Afterwards x still has the original y while y has 5, so a direct replacement in w is generally wrong. B is correct. A ignores the redefinition; C assumes every initial y equals 5; D forbids the valid first substitution.

**Common misconception:** Treating a copy assignment as a permanent alias relationship.

