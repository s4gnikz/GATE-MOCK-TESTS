# Worked Solutions — Mock Test 032

## Q1

**Correct answer:** 0.6667 (accepted range 0.66665–0.66675)

There are25−7=18 journeys over10 minutes. Of these,19−7=12 last at most20 minutes. The conditional probability is12/18=2/3≈0.6667. Cumulative counts must be differenced before applying the conditional denominator.

## Q2

**Correct answer:** A

A punch away from both folds unfolds to all four sign combinations of its nonzero coordinates. A is exactly such a reflection orbit. B violates reflection symmetry, while C,D contain only two of the four distinct images. Being away from folds prevents coincident mirrored centres.

## Q3

**Correct answer:** B

The stated order is archive, recalibrate, repeat, compare. Among those events, repeating directly precedes comparison, so B. A,C are earlier, and D never occurs in the account. The question concerns the narrated event ordering, not whether unmentioned activities occurred between them.

## Q4

**Correct answer:** 0.25

A6 is retained either on the first roll, probability1/6, or after an odd first roll and a6 on the second, probability(1/2)(1/6)=1/12. These disjoint cases sum to1/4. The reroll rule changes the distribution from a single fair die.

## Q5

**Correct answer:** B

A parsimonious explanation avoids unnecessary assumptions while accounting for the observations, giving B. A rejects evidence rather than simplifying explanation; C increases terminology without justification; D wrongly treats simplicity as a guarantee of truth.

## Q6

**Correct answer:** 1

Put t=log2(x), so log4(x)=t/2. Then t²/2=8, giving t=4 or−4. Hence x=16 or1/16, whose product is1. Positive x does not imply a positive logarithm, so the negative t solution must not be discarded.

## Q7

**Correct answer:** C, D

Equality2a+b=2a+c gives b=c, proving C. Both sides of D equal2a+b+c. In A, the two sides are4a+2b+c and2a+2b+c, not equal for arbitrary a. In B,2a+b and2b+a need not agree. A familiar-looking operator need not inherit addition's algebraic properties.

## Q8

**Correct answer:** 6

Write the heights as[[a,b],[c,d]]. The second row is at most1, so the column maximum2 forces a=2, and the column maximum3 forces b=3. The second row must have at least one height1; choosing(c,d)=(1,0) or(0,1) adds exactly1. Minimum total2+3+1=6. The row and column maxima need not be realized by four separate tall columns.

## Q9

**Correct answer:** 0.6444 (accepted range 0.64435–0.64445)

Use1/[n(n+2)]=(1/2)(1/n−1/(n+2)). All middle terms cancel, leaving(1/2)(1+1/2−1/9−1/10)=29/45≈0.644444. The gap of two leaves two terms at each end, not just one.

## Q10

**Correct answer:** 4.5

BC is horizontal, so the altitude from A is x=0. Side AC has slope(0−8)/(6−0)=−4/3; the perpendicular altitude from B has slope3/4 and equation y=(3/4)(x+6). At x=0 it gives y=4.5. Altitudes are perpendicular to opposite sides and are not generally angle bisectors or medians.

## Q11

**Correct answer:** A, C, D

This is write skew under the stated snapshot rule. The write sets are {A} and {B}, so both pass the conflict test and both flags become zero: A,C,D are true. In either serial order, the second transaction sees the first flag cleared and does not clear its own flag, making B false. Disjoint writes do not imply preservation of an invariant involving both items.

## Q12

**Correct answer:** A, C

The rule gives (Project,Role)→Employee. Neither project nor role alone determines an assignment under the given constraints, so their pair is a candidate key (A). C describes a direct violation of that dependency. B fails because one employee can hold multiple roles on a project. D discards which roles the employee fills and therefore loses information. A ternary key constrains a combination of two participating entities, not either participant separately.

## Q13

**Correct answer:** 2

Offset 3072 is in logical data block 3. It is beyond the direct block, so one single-indirect pointer block and the target data block are required. Logical blocks 0,1,2 remain holes. Thus two blocks are allocated, not four data blocks.

## Q14

**Correct answer:** C

When a is processed before b, both c and d are enqueued before b can enqueue e. C puts e between c and d and is impossible. A,D are possible with a's neighbors ordered c,d or d,c. B results when b is processed first, discovering e before a discovers c,d. Equal BFS distance does not make every within-level ordering attainable.

## Q15

**Correct answer:** 3

Simultaneous updates give 00→01→11→00. There are three distinct states. In particular, B' uses the old A, not A' computed at the same edge.

## Q16

**Correct answer:** B

Invalidation removes the stale clean copy, and the next read fetches the device-updated memory. A leaves the cached value valid; C does not affect cache contents; D can keep reading the stale line indefinitely. Completion ordering alone is insufficient without cache coherence or explicit maintenance.

## Q17

**Correct answer:** A, C

Each spanning tree has n−1 edges, so its new weight is three times its old weight plus 7(n−1). Strict comparisons and uniqueness are preserved: A,C. Paths can have different edge counts, so B need not hold. D ignores both scaling and the number of edges. The shortcut is to identify equal cardinality of all candidate trees.

## Q18

**Correct answer:** A, B, D

Context-free languages are closed under homomorphisms, including erasing ones, giving A. Intersection with a regular language preserves context-freeness, giving B,D. General context-free languages are not closed under complement, so C has no guarantee. Closure with a regular operand is stronger than closure with an arbitrary context-free operand.

## Q19

**Correct answer:** D

Successful exec replaces the executing program within the same process. A is false because it is not fork. B is false because descriptors without close-on-exec can survive. C is false because only a failed exec returns to the old program. D states the preserved process identity correctly.

## Q20

**Correct answer:** 19

A full binary tree with L leaves has 2L−1 vertices, initially 21. The operation removes precisely the chosen leaf and its parent, retaining every vertex of the sibling subtree. Hence 19 remain. A sibling that is internal does not cause its descendants to be deleted.

## Q21

**Correct answer:** 0.9

Conditional independence gives probability 9/16 that both reports are correct and 1/16 that both are incorrect. These are the two disjoint ways to agree, so the conditional probability is (9/16)/(10/16)=9/10. Agreement is not the same event as both being correct.

## Q22

**Correct answer:** A

The first p symbols are all a, so every permitted nonempty v consists solely of a's. Pumping down reduces only their count and leaves all p b's, proving A. B contradicts this location; C reverses the universal quantification required to refute the lemma; D violates |v|≥1. One convenient split is insufficient: the argument must cover all legal splits.

## Q23

**Correct answer:** C

At the join, x merges 2 with 7 and y merges 7 with 2. Each becomes nonconstant in the stated abstraction. Their correlation is discarded, so the analysis cannot infer z=9. Actual execution gives 9 in both branches. A,B incorrectly retain branch-specific constants; D combines values from incompatible branches.

## Q24

**Correct answer:** 238

The product is −1.125, exactly representable with four fractional bits. Its signed scaled integer is −1.125×16=−18. The 8-bit two's-complement bit pattern represents 256−18=238 when read unsigned. No rounding error occurs; unsigned interpretation must happen after encoding the negative value.

## Q25

**Correct answer:** 0.5

There are 16 equally likely ordered pairs and 12 unequal ones. Six unequal pairs have minimum zero: (0,j),(j,0) for j=1,2,3. The conditional probability is 6/12. Equal backoffs, including (0,0), are excluded by the condition.

## Q26

**Correct answer:** A, C

The set is the divisor lattice of 6, with meet gcd and join lcm; all results remain in the set. Complements are 1↔6 and 2↔3, so A,C hold. B is false because 1 and 6 are a lower and upper bound of 2,3. D is false because neither 2 divides 3 nor 3 divides 2.

## Q27

**Correct answer:** 2

Using multipliers 2 and 1 in the first column gives remaining rows (0,1,1) and (0,1,3). Subtract the new second row from the third: (0,0,2). Therefore U33=2. The second-stage entry is computed after the first elimination, not from the original lower-right submatrix alone.

## Q28

**Correct answer:** B

The updated alternatives have costs 2+9=11 through Y and 5+1=6 through Z. X advertises their minimum, 6. A omits link costs; C ignores the still-valid Z route; D combines unrelated quantities. An increased metric must trigger reconsideration of other neighbors.

## Q29

**Correct answer:** 150

Each new payload has 400 bytes, which is divisible by 8. The second fragment starts 400/8=50 offset units after the original fragment, giving 100+50=150. Offsets remain relative to the original datagram, not the fragment being split. Both fragments retain MF=1 because more original data follows.

## Q30

**Correct answer:** A, C

The first x value feeds y=x+2, so A is true. The last x value is never used, so B is false. y must survive the intervening x assignment to the return, giving C. The assignment to y kills its previous value; that old value is not used on its right-hand side, so D is false. Liveness concerns values needed in the future, not merely variables appearing somewhere later.

## Q31

**Correct answer:** A, C

A finite simulation of k transitions decides both acceptance within the bound and the number of distinct tape cells visited, so A,C are decidable even if binary k makes the simulation expensive. Unbounded acceptance is undecidable, ruling out B. Halting on every input is also undecidable, ruling out D. Complexity and decidability are different issues.

## Q32

**Correct answer:** 4

Issue the first load in cycle 1. Its consumer can issue in cycle 4, leaving cycles 2,3 idle. The independent add issues in 5 and the second load in 6; its consumer issues in 9, leaving 7,8 idle. There are four idle cycles. Fixed ordering prevents moving the independent add into an earlier empty cycle.

## Q33

**Correct answer:** 0.3333 (accepted range 0.33325–0.33335)

The fundamental theorem gives F'(x)=2x+1, while direct integration gives F(x)=x²+x. Hence xF'(x)−F(x)=2x²+x−x²−x=x². Its integral on [0,1] is 1/3≈0.3333. Differentiating F and evaluating F are distinct steps; the integration variable t is a dummy variable.

## Q34

**Correct answer:** D

The predecessor is the maximum key in v's left subtree. A right child would contradict that maximality, so it has no right child and may have a left child. Thus D is true and A,B are not guaranteed. It may be several edges below v, making C false. Splicing a node with at most one child is straightforward.

## Q35

**Correct answer:** 2.6667 (accepted range 2.66665–2.66675)

The old squared-deviation sum is 4 observations×variance 4=16. Adding observations equal to the old mean leaves the mean at 5 and adds zero squared deviation. Divide 16 by the new population size 6 to obtain 8/3≈2.6667. The population denominator is 6, not the sample-variance denominator 5.

## Q36

**Correct answer:** 21

Count runs of equal symbols. If a string starts in 0 and ends in 1, two 01 transitions imply four runs; compositions of length 6 into four positive run lengths give C(5,3)=10. Starting and ending in 0 gives five runs, contributing C(5,4)=5. Starting and ending in 1 also gives five runs, contributing 5. Starting in 1 and ending in 0 gives six runs, contributing 1. Total 10+5+5+1=21. Counting arbitrary pairs of positions would ignore consistency of shared symbols.

## Q37

**Correct answer:** A, B, D

A does not modify either operand. B,D store the operand's existing value, so the sum is unchanged despite aliasing. C is insufficient: with a=0,b=5,p=&b, the old sum is 5 and the new sum is 0. Aliasing alone neither establishes nor rules out redundancy; the stored value also matters.

## Q38

**Correct answer:** 3

C×Required is empty. Subtracting R and projecting still gives the empty set, and C−empty=C. Thus u,v,w all qualify by vacuous satisfaction of all required courses. Restricting candidates to students appearing in R would incorrectly exclude w from this explicitly defined query.

## Q39

**Correct answer:** C

Key 7 must be the root. Key 6 is already at index 3. If 5 were at index 4 or 5, its parent at index 2 would have to exceed 5; both available larger keys are already elsewhere. Index 2 is possible, and indices 6,7 have parent 6, so each is possible. Hence exactly {2,6,7}: C. A excludes feasible child positions; B includes impossible positions 4,5; D includes the root occupied by 7.

## Q40

**Correct answer:** 123

The saved source is 7. R changes 100→104→100 before the destination fetch, so the destination is the same word and becomes 14. The word at 104 stays 9, and R ends at 100. Their sum is 100+14+9=123. Evaluating both addresses from an imagined simultaneous operand fetch would violate the given instruction semantics.

## Q41

**Correct answer:** 2

With three significant bits, representable values near 8 are 8,10,12,14. The exact sum 9 ties between 8=1.00×2³ and 10=1.01×2³, so ties-to-even selects 8. Thus (a+b)+c rounds to 8 twice. On the other side b+c=2 exactly and a+2=10 exactly. The final difference is 10−8=2. Floating-point addition need not be associative.

## Q42

**Correct answer:** A, C

Unsigned addition gives 0x80+0xFE+1=0x17F, so the low byte is 0x7F and carry C=1. Therefore A is true and B is false. Signed subtraction is −128−1=−129, outside [−128,127], so V=1 and D is false. Carry and signed overflow answer different questions.

## Q43

**Correct answer:** 12

The two parallel edges contribute degree 2 to a and its loop contributes 2 more, giving degree(a)=4. Four total edges contribute eight adjacency-list entries. The requested sum is 4+8=12. A loop has two incidences even when stored in a single matrix column.

## Q44

**Correct answer:** A, B, D

F selects y when x=1 and z when x=0. Therefore the two cofactors agree exactly when y=z, proving A. Expanding B's product gives xy+(NOT x)z+yz; the consensus term yz is redundant, so B holds. C fails with x=0,y=1, where F=z. When y=NOT z, F equals z for x=0 and NOT z for x=1, hence F XOR z=x: D. Treating the selector as an ordinary OR input obscures these dependencies.

## Q45

**Correct answer:** 14

A parse tree with five terminal leaves is an ordered full binary tree with four binary internal nodes. Let t1=1 and tn=Σ(i=1..n−1) ti t(n−i). Then t2=1,t3=2,t4=5, and t5=5+2+2+5=14. Different expansion orders of the same tree are not additional trees; counting derivation sequences would overcount.

## Q46

**Correct answer:** B

The parent retains its three threads. Only the calling thread is replicated into the child, which therefore starts with one thread. B is correct; A,C,D have incorrect thread counts. A copied address space can contain synchronization objects representing the old multithreaded state, but this does not recreate the other threads.

## Q47

**Correct answer:** 2

Write x=g^j in the cyclic group of order 16. x^4=1 requires 16 to divide 4j, giving j=0,4,8,12. The equation x²=1 holds for j=0,8. Exclude those two, leaving two elements of exact order 4. Divisibility is applied to exponents modulo the group order.

## Q48

**Correct answer:** 2

All minterms with A=1 are included, and all with B=0 are included; the excluded minterms 4,5,6,7 have A=0,B=1. Thus F=A OR (NOT B), requiring two literals. A zero-literal constant or single literal cannot have precisely these four zero assignments out of sixteen. The two literals therefore achieve the lower bound. C,D disappear because each corresponding K-map group spans both their values.

## Q49

**Correct answer:** A, C

A deterministic PDA is a restricted nondeterministic PDA, so its language is context-free (A). Final-state and empty-stack acceptance have equivalent expressive power for nondeterministic PDAs; the standard simulation gives C. Deterministic PDAs recognize only a proper subset of context-free languages, so B is false. D can introduce acceptance in previously nonfinal states after input consumption. An equivalence theorem about machine classes is not permission to alter acceptance states arbitrarily.

## Q50

**Correct answer:** 0

After the first read the pipe is empty. The second read blocks while any writer descriptor remains open; closing only P's copy does not signal end-of-file. When Q closes the final writer descriptor, an empty pipe yields EOF, represented by a zero-byte return. This differs from an error and from a short positive read.

## Q51

**Correct answer:** A, C

A selects a subset of finite R. C is exactly membership in R because its witness must equal x, so it too is finite. B is the complement of the finite union R∪S and is infinite. D is true for every x when S is empty, hence need not be finite. Quantifying over an empty relation can turn a universal condition into an unbounded result.

## Q52

**Correct answer:** 6

The tokens are ID(ifif), EQEQ(==), EQ(=), keyword(if), EQ(=), ID(iff). Longest match prevents splitting ifif or iff into a keyword plus suffix. Three consecutive equals signs yield a two-character token followed by a one-character token. There are six tokens in total.

## Q53

**Correct answer:** 3

Original path s→a→b→c has weight 3−4+2=1, less than the alternative weights 10 and 10. Reweighting changes every s-to-c path by the same amount h(s)−h(c)=2, hence the new distance is 3. Direct transformed edge weights are 3,12,0,0,9 respectively; the same best path has cost 3. Potential differences telescope over an entire path.

## Q54

**Correct answer:** 208

Begin with all 256 addresses assigned A. The /26 removes 64. The more specific /27 restores 32 of them to A, but the /28 removes 16 from that restored block. Thus 256−64+32−16=208. Counting the /24 and /27 separately without subtracting overridden subranges would double count.

## Q55

**Correct answer:** D

Changing the IPv4 source address affects the IPv4 header checksum. The TCP checksum covers both its header, including the source port, and a pseudo-header containing IP addresses, so it also changes. D is correct. A omits TCP's pseudo-header/header changes; B omits the IP header change; C wrongly treats checksums as covering only payload. Incremental checksum updates are possible, but both fields require adjustment.

## Q56

**Correct answer:** 9

After the key2 pass the order is E,A,C,D,B: A,C,D retain their original relative order within key2=1. The stable key1 pass yields D,B,E,A,C. Therefore A and C occupy positions 4 and 5, whose sum is 9. The last stable pass establishes the primary key; earlier ordering breaks its ties.

## Q57

**Correct answer:** A, B, D

The last arrival resets count and publishes the phase's sense, allowing the waiter to leave: A. Publishing first could let the waiter enter the next phase and increment count before the old phase resets it, losing that arrival; hence B. Both local senses toggle per phase, distinguishing one release from the next (D). A fast thread can arrive at the next barrier but must wait for the other thread's increment, making C false. These claims use the stipulated atomic increment and sequential consistency; unsynchronized language-level data races are not being assumed away by ordinary C syntax.

## Q58

**Correct answer:** 500

The new outstanding amount is 3000−1000=2000 bytes. The current sending limit is min(5000,2500)=2500 bytes, leaving room for 500 more. The advertised receive window in the ACK is relative to the newly acknowledged position; it should not be added to the old allowance.

## Q59

**Correct answer:** 17

q points to p. The parenthesized (*q)++ advances p from a+1 to a+2; it does not increment an array element. Then **q adds 3 to a[2], changing 7 to 10. Finally p[-1]=a[1]=5 and p−a=2. The return value is 5+10+2=17. Parentheses distinguish incrementing a pointer through a pointer-to-pointer from incrementing its pointee.

## Q60

**Correct answer:** 24

The first triangle has 3!=6 colorings. Once its bridge endpoint's color is fixed, the second bridge endpoint has two choices. Its remaining two triangle vertices must use the two other colors, in 2!=2 orders. Thus 6×2×2=24. Multiplying two independent triangle counts would ignore the bridge restriction.

## Q61

**Correct answer:** 48

Choose the unordered pair of positions for A,B at distance 2: (1,3),(2,4),(3,5),(4,6). The remaining positions admit respectively 2,1,1,2 adjacent position pairs for C,D. For each such selection, orient A,B in two ways, orient C,D in two ways, and arrange the two other books in two ways. The total is (2+1+1+2)×2×2×2=48. Therefore the required count is 48.

## Q62

**Correct answer:** 1

Each of T's two rows with key 1 matches U's single key-1 row, giving two joined rows with non-NULL U.k; both fail the WHERE filter. T's NULL does not equal U's NULL, so it generates one NULL-extended unmatched row, which passes. The result has one row. SQL equality on two NULLs is UNKNOWN, not TRUE.

## Q63

**Correct answer:** 14

Address 0 executes once. The outer loop runs for R=3,2,1, so address 1 executes three times and address 3 executes three times. Address 2 executes 3+2+1=6 times as S decreases to zero in each outer iteration. Address 4 executes once. Total clocks are 1+3+6+3+1=14. Counting branch targets without testing updated values can introduce an extra inner iteration.

## Q64

**Correct answer:** 16

At total 10, the even number of 3-parts can be zero or two. Zero gives the single all-1 composition. Two consume 6 units, leaving four 1-parts; arranging these six parts gives C(6,2)=15. Total e10=16. More generally E(x) is one half of [1/(1−x−x³)+1/(1−x+x³)], since averaging cancels compositions with an odd number of 3-parts. Ordered compositions count arrangements, not merely partitions.

## Q65

**Correct answer:** A, C

Both original S alternatives have FIRST set {a}, causing an LL(1) table conflict: A. Factoring leaves alternatives b and c with disjoint FIRST sets, giving the equivalent LL(1) grammar in C; this disproves B. Each generated string, ab or ac, has a unique parse tree, so D is false. Failure of a particular grammar to be LL(1) does not imply ambiguity or impossibility of an LL(1) grammar for its language.


