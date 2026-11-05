# Worked Solutions — Mock Test 031

## Q1

**Correct answer:** A, C

The base2 and increments of2 reach every even integer, proving A. They never reach an odd integer, so B,D do not follow. A separate odd base3 starts the odd chain; together the two chains cover every n≥2, proving C. The induction step's stride determines which base cases are needed.

## Q2

**Correct answer:** 2

The remaining squares form a ring whose adjacency graph is an eight-cycle; dominoes pair adjacent squares. Choose the partner for one corner square: there are two choices. Either choice forces every remaining pairing around the ring, giving exactly two tilings. The removed centre provides no additional adjacency across the gap.

## Q3

**Correct answer:** 4

16!=16·15!, so the ratio contributes exactly the four factors of2 in16=2^4. Thus the exponent increases by4. Computing the entire factorial is unnecessary.

## Q4

**Correct answer:** 20

The original perimeter is2(6+4)=20. Each corner removal deletes two unit boundary segments and introduces two new unit boundary segments, producing no net change. The four cuts do not overlap, so the remaining perimeter is still20. Loss of area does not necessarily mean loss of perimeter.

## Q5

**Correct answer:** D

The relative clause “that were discussed” modifies plural proposals, while the main clause's subject is singular “One,” requiring has. D supplies both. A is wrong in both positions; B gets the relative clause right but not the main clause; C gets the main clause right but not the relative clause.

## Q6

**Correct answer:** 28.5714 (accepted range 28.57135–28.57145)

Normalize the budget to100. Food rises from40 to50, and other costs remain25, leaving25 for transport instead of35. The reduction is10 out of35, or100·10/35=200/7≈28.5714%. The denominator is the original transport allocation, not the total budget.

## Q7

**Correct answer:** B

Let a,b,c,d denote the truth statuses. The statements impose a=NOT b, b=NOT c, c=NOT d, d=a AND b. Since a and b are opposites, a AND b=0, so d=0, c=1, b=0, a=1. Exactly A,C tell the truth, option B. Options A,C,D list pairs inconsistent with these statuses. A liar's statement must be false, not merely unproved.

## Q8

**Correct answer:** 5

Track orientations in the order(top,bottom,north,south,east,west). Initially they are(1,6,2,5,3,4). After north:(5,2,1,6,3,4); east:(4,3,1,6,5,2); south:(1,6,3,4,5,2); west:(5,2,3,4,6,1). The final top is5. A closed path of rolls need not restore orientation.

## Q9

**Correct answer:** C

The passage explicitly combines an unchanged mean with individual changes, which is C. A,D contradict the stated increases and decreases. B incorrectly equates one summary statistic with the entire distribution. Offsetting changes can preserve a mean while altering many other properties.

## Q10

**Correct answer:** 12

The box sizes must be2 and3. Choose which box has size2 in two ways. Its contents must contain exactly one of the two specified files: choose that file in two ways and one of the other three files in three ways. The remaining files go to the other box. Total2·2·3=12. Box labels matter, but the order of files within a box does not.

## Q11

**Correct answer:** D

SELECT DISTINCT x produces one row containing NULL. The outer COUNT(*) counts that row, giving1. COUNT(DISTINCT x), however, ignores NULL values and has no non-NULL distinct values to count, giving0. D is correct. A discards the surviving row, B fails to eliminate duplicates, and C treats the NULL as a counted value in Q2. A DISTINCT result row and a counted non-NULL aggregate input are different objects.
## Q12

**Correct answer:** C

The lemma's requirement concerns language words at least as long as the pumping length. None exist at length≥21, so the implication is vacuously satisfied, giving C. A,B invent long words or substrings. D incorrectly excludes finite regular languages from the condition.

## Q13

**Correct answer:** 11

For x=0, odd y can be1,3,5,7, giving4 choices with z determined. For x=1 the same four choices fit. For x=2, y may be1,3,5, giving3. Total4+4+3=11. The upper bound on x and parity condition prevent direct unrestricted stars-and-bars counting.

## Q14

**Correct answer:** A

The first receive discards DE under the given truncation rule. The next queued datagram is FG, which fits, so A is correct. B,C,D all incorrectly retain discarded bytes or combine separate datagrams. Datagram boundaries differ from stream byte buffering.

## Q15

**Correct answer:** A, D

Dovetailing finds an accepting candidate if one exists, proving A. If M is total, every candidate test terminates, proving D. For arbitrary M, even the empty word can encode an unbounded acceptance computation, so finiteness of the candidate set does not give a decider, refuting B. The property is undecidable by reducing machine acceptance to a machine that simulates only on ε and rejects other candidates. If its complement were also recognizable, dovetailing both recognizers would decide it; hence C is false.

## Q16

**Correct answer:** 9

The neighbours are9 and9.25, equidistant from9.125. Spacing0.25 at exponent3 implies six significant bits. The significand of9 is1.00100₂, whose low bit is even;9.25 has1.00101₂. The tie rounds to9. Ordinary decimal rounding rules do not determine this binary tie.

## Q17

**Correct answer:** B

The eight inputs split into four complementary pairs. In each pair, choosing one output forces the other's opposite value. The specified output at000 fixes the pair000/111, leaving three independent binary choices, or2³=8 truth tables. B is correct. A leaves too few free choices; C ignores the fixed pair; D exceeds even the unconstrained self-dual count16.
## Q18

**Correct answer:** 3

Remaining needs are2,2,4. P3 cannot go first. If P1 goes first, available rises to3, forcing P2 next and then P3. If P2 goes first, available rises to4 and either remaining process may go next. The three orders are123,213,231. Available increases by the old allocation when a completing process is accounted for; the temporarily granted need is returned as well.

## Q19

**Correct answer:** A

The reversed result is(2,C),(1,B),(1,A). Its key order is descending, but the tied records A,B have reversed relative order, so A. B,D mistakenly assume stability survives whole-array reversal. C describes the correct descending key order, not the defect.

## Q20

**Correct answer:** 3

The transition over C advances S→·CC to S→C·C. Closure adds C→·cC and C→·d because the dot precedes C. Thus GOTO contains three items. The completed item S→CC· belongs to a later transition, not this one.

## Q21

**Correct answer:** 9

The coefficients of(1−x)^(−2) are n+1. Multiplying by1+x makes the x4 coefficient5+4=9. Equivalently, convolve the two contributions at powers4 and3. Formal power-series arithmetic needs no numerical convergence assumption.

## Q22

**Correct answer:** 5

Squares modulo8 are0,1,4, repeating for the probe sequence. Only three distinct slots are reachable. If all three are occupied, the remaining five can still be empty but inaccessible to that insertion. A low overall load does not guarantee that a particular probing scheme visits an empty slot.

## Q23

**Correct answer:** A, C

With at least two elements, every x has a different witness y, proving A. For Q, take x equal to its proposed y; x≠y then fails, so Q is false in every nonempty domain, proving C and refuting B. Any two-element domain makes P true and Q false, refuting D. Moving the existential quantifier outside removes the ability to choose a witness depending on x.

## Q24

**Correct answer:** D

The shift yields floor(−3.5)=−4, while division truncates to−3. Difference−4−(−3)=−1, option D. A treats both rounding directions as identical; B reverses subtraction; C is unrelated to the two resulting integers.

## Q25

**Correct answer:** -4

vᵀu=2−2+0=0, so(uvᵀ)²=u(vᵀu)vᵀ=0. Hence(I+uvᵀ)(I−uvᵀ)=I and A^(−1)=I−uvᵀ. Its off-diagonal(2,1) entry is−u2·v1=−2·2=−4. The zero scalar product permits this inverse without an infinite series.

## Q26

**Correct answer:** C

Each append grows capacity n→2n and copies n elements. Removing the appended element leaves size n, exactly half the capacity, so it shrinks back and copies n retained elements. The same starting state recurs, costing2n copies per pair and Θ(kn) overall, C. A,B assume amortized growth without accounting for repeated shrink/grow oscillation; D ignores both data size and repetition count.

## Q27

**Correct answer:** 7

Group A needs four choices including none, requiring2 bits. Group B needs six choices including none, requiring3 bits. Two independent signals need2 more bits. Total7. The explicit none option must be included before rounding each field width upward.

## Q28

**Correct answer:** A

A's inherited information cannot depend on a right sibling C under the left-to-right restriction, so A violates it. B,C use information from a left sibling; D uses the parent's inherited information. Those are permitted dependency directions, subject to the rest of the definition being consistent.

## Q29

**Correct answer:** B

Following alpha reaches beta, which immediately leads back to alpha. No address record is supplied, so B. A,C,D invent an address unsupported by this configuration. Cycle detection can stop the futile traversal but cannot derive missing address data.

## Q30

**Correct answer:** A, B

For NULL, x>0 is UNKNOWN, which this CHECK accepts, proving A and refuting C. A non-NULL integer passes exactly when it is positive, proving B. NOT NULL would exclude the previously permitted NULL, refuting D. SQL CHECK acceptance differs from WHERE filtering of UNKNOWN.

## Q31

**Correct answer:** 14

Estimated order is A,B,C. Actual waiting times are0,8,9, totaling17. Knowing actual bursts, execute B,C,A or C,B,A; waiting times are0,1,2, totaling3. The difference is14. Estimates choose the order, while actual durations determine the resulting waits.

## Q32

**Correct answer:** 6

The call chain is F(7),G(5),F(4),G(2),F(1),G(−1). The last returns1 and each of the five preceding calls adds1, so F(7)=6. The two functions reduce their arguments by different amounts.

## Q33

**Correct answer:** C

Both tuples share B=2 but differ in A, directly violating B→A, so C. A→B holds in this instance because A values are distinct. B,D are trivial dependencies from the combined attribute set. An instance satisfying a dependency does not establish it as a constraint on all future instances.

## Q34

**Correct answer:** 16

The first copy produces[1,1,2,3,4]. The second saves its source[2,3,4] before overwriting positions0–2, yielding[2,3,4,3,4]. The sum is16. Temporary-copy semantics prevent an overlapping write from changing a later source read within the same copy.

## Q35

**Correct answer:** A, C

A finite derivative implies f(x)−f(0)=x times a quantity with finite limit, so continuity follows: A. The same argument on each side proves C. The function |x| is continuous but not differentiable at0, refuting B. Equal finite one-sided derivative limits give the common two-sided derivative, refuting D. Unequal derivatives can cause a corner without a discontinuity.


## Q36

**Correct answer:** A, B

OR and XOR both yield0 at00 and1 at01,10, proving A,B. Their disagreement at11 is permitted because that state is unreachable. AND is0 on the two required one-input cases, refuting C. NAND is1 at00, refuting D. Don't-care freedom applies only to the explicitly unreachable assignment.

## Q37

**Correct answer:** 122

Initially the records occupy330 bytes and metadata occupies32+6·4=56, leaving126 free. Deleting adjacent80- and50-byte records creates a130-byte hole. A new slot consumes4 bytes from the free gap, leaving122 there; without moving records the largest available record region is max(130,122)=130. With compaction, total free record space is126+130−4=252. Increase252−130=122. Slot entries retained by deletion are not reclaimed.

## Q38

**Correct answer:** A, C

An aligned two-byte word uses both banks at one word address, proving A. An odd-start two-byte load crosses an aligned-word boundary, refuting B. Independent bank enables permit a one-byte store without changing its neighbour, proving C. Endianness concerns byte significance, not whether an address number is even, refuting D.

## Q39

**Correct answer:** A, C, D

The unnormalized joint weights at(1,0),(1,1),(2,0),(2,1) are1,2,2,3, summing to8, so A. Summing the Y=1 column gives5/8, proving C. Given Y=0, X=1,2 have probabilities1/3,2/3, so the conditional mean is5/3, proving D. Independence fails since P(1,0)=1/8 differs from P(X=1)P(Y=0)=(3/8)(3/8)=9/64, refuting B.

## Q40

**Correct answer:** A, C

Both items have value density2. Any feasible packing of total weight5 achieves the maximum value10, proving A. A whole four-unit item plus one unit from the other also attains it, proving C. The allocation2.5+2.5 has two partial items, refuting B, and many such allocations refute D. A greedy algorithm can produce an optimum with at most one partial item without that property holding for every optimum.

## Q41

**Correct answer:** 2

No single row covers all columns. The only two-row covers are AC and BD, each costing5. Any three rows cost at least2+2+3=7, so none ties them. Exactly two minimum-cost covers exist. Cover cardinality and cost are distinct objectives; here both optimal pairs have the same cost.

## Q42

**Correct answer:** 7

f and g reference the same closure and captured x, so their first calls return1 and2. h has its own environment and returns1. The final f call advances the first environment to3. Sum1+2+1+3=7. Copying a closure reference is not creating a fresh capture environment.

## Q43

**Correct answer:** -2

There are six monotone paths. In move order RRDD,RDRD,RDDR,DRRD,DRDR,DDRR, their best costs after zeroing one visited cell are4,−1,−2,−2,−2,4. Thus the minimum is−2. For example RDDR visits costs0,5,−4,2,0 and zeroes5. A dynamic program can track whether the replacement has already been used. Zeroing the negative cost would increase, not reduce, the sum.

## Q44

**Correct answer:** A, C

TCP offers a byte stream, not application-write messages, proving A. UDP datagrams can be carried in multiple IPv4 fragments, refuting B; IP reassembly can present the complete datagram to UDP, proving C. Routers replace link-specific framing on different links, refuting D. Transport units and link/network transmission units need not align one-for-one.

## Q45

**Correct answer:** D

The intended loads are2 and1, giving a[0]=3. The faulty first store sets a[0]=2; because k=0, the second statement then reads that changed2 for both terms, yielding4. Difference4−3=1, option D. A reverses the difference, B ignores aliasing, and C is not the difference between the two outcomes.

## Q46

**Correct answer:** B

The minimum is2 root children, each with2 leaf children, each leaf with2 keys:2·2·2=8. The maximum is4·4·4=64. B gives the pair. A omits a branching level; C understates maximum fan-out; D overstates the minimum. Count data keys at leaves, not separator copies.

## Q47

**Correct answer:** A, B

At a shared suffix, linking the same node again can make its next pointer refer to itself or to an earlier shared node, proving A and refuting D. When current pointers are equal, their entire remaining suffix is the same physical list and can be attached once, proving B. Distinct nodes may contain equal values, refuting C. An in-place merge relies on aliasing assumptions as well as sort order.

## Q48

**Correct answer:** A, C

To have f(g(0))=0, g(0) may be a or b. To have f(g(1))=1, g(1) must be c. Hence two right inverses, proving A, and both are injective, proving C. A left inverse would have to send f(a)=f(b)=0 to both a and b, impossible, refuting B. f itself is not injective, refuting D.

## Q49

**Correct answer:** A, D

Inclusion would be violated if an evicted L2 block remained in L1, so a corresponding L1 invalidation can be needed, proving A. L2 can contain blocks absent from L1, refuting B. Exclusivity forbids simultaneous copies, refuting C. Inclusive replication consumes slots without adding distinct blocks, proving D. The policies constrain contents, not merely replacement order.

## Q50

**Correct answer:** 35

SSTF chooses55, whose seek5 plus rotational wait50 gives55. The other service times are20+0=20 for30 and30+0=30 for80. Minimum20, so excess55−20=35. Minimum seek distance does not necessarily minimize seek-plus-rotation time.

## Q51

**Correct answer:** 200

First-fit takes250 from the500-byte hole, leaving200,250,300; its next200 consumes the first hole, leaving a largest hole300. Best-fit takes250 from300, leaving200,500,50; then consumes200 exactly, leaving largest hole500. Difference500−300=200. Both policies allocate successfully, but their remaining hole distributions differ.

## Q52

**Correct answer:** 3

To pop3 first,1,2,3 must all be pushed before any pop, requiring capacity at least3. Pop3, push and pop4, pop2 and1, then push and pop5. This never exceeds three entries, proving capacity3 sufficient. The lower bound follows from the first demanded output, not the total number of inputs.

## Q53

**Correct answer:** A, C

XOR cancellation gives u XOR v=x XOR z=w, proving A and refuting D: only four parity triples occur. Complementing all three inputs preserves u,v,w, so B is false. Those outputs identify a pair of complementary input triples; with three inputs, their majority bits are opposite. Adding t selects exactly one member, proving C. A nonlinear extra output can resolve information lost by the parity outputs.

## Q54

**Correct answer:** A, C

Each transaction's shared lock prevents the other from obtaining an exclusive lock, proving C and allowing the wait cycle in A. Two-phase locking ensures a serializability property but does not by itself exclude deadlock, refuting B. Shared locks are mutually compatible, refuting D. The conflict arises on upgrade.

## Q55

**Correct answer:** 8

An eight-state DFA can store the latest three bits, starting at000 and shifting on each input. All eight states are reachable after three symbols. For two distinct stored triples, consider appending zero, one, or two zeroes: the tested parities are respectively the parity of all three bits, the last two bits, and the last bit. If all three parities agreed between the triples, each bit would agree, contradicting distinctness. Thus some suffix distinguishes every pair, proving that all eight states are necessary. Padding is built into the initial000 state.

## Q56

**Correct answer:** A

At depth d there are2^d calls, each initializing2^d cells, so total initializations sum4^d from d=0 to k, which is Θ(4^k)=Θ(n²). Sequential depth-first processing keeps only one root-to-leaf chain of buffers live at once; its sizes sum1+2+...+2^k=2n−1, giving Θ(n). A follows. B,D undercount total work, and C counts allocations from nonoverlapping sibling calls as simultaneously live.

## Q57

**Correct answer:** 1601

In milliseconds, circuit time is1+L/2000 and packet time is(L+100·ceil(L/900))/1000. Circuit wins exactly when L+200·ceil(L/900)>2000. For1≤L≤900, the left side is at most1100. For901≤L≤1800, it becomes L+400 and exceeds2000 first at L=1601. This is the first qualifying range, so1601 is minimal. Equality at1600 is not a strict win.

## Q58

**Correct answer:** A, B, D

With x=0 the loop is skipped, proving A. With x=1, every update keeps x positive and strictly increases it, so the original never returns while the rewritten code returns immediately, proving B. C ignores observable termination; D correctly recognizes that obligation. An unused computed value does not automatically make its entire computation removable.

## Q59

**Correct answer:** A, C

Pinning prevents eviction/reuse until the physical-address transfer finishes, proving A. If the frame is reused, the device still targets that same physical address and may corrupt the new allocation, proving C. A stable virtual name does not prevent physical reuse, refuting B, and D contradicts the stated DMA addressing model. Page-table remapping and device address state require coordination.

## Q60

**Correct answer:** 3

A has eigenvalues1 and2, with eigenvectors(1,1)ᵀ and(1,2)ᵀ. Write v=α(1,1)ᵀ+β(1,2)ᵀ. Then A^n v=α(1,1)ᵀ+2^nβ(1,2)ᵀ. Boundedness forces β=0, and x+y=2α=6 gives α=3, so x=3. A component along the expanding eigenvector cannot remain bounded.

## Q61

**Correct answer:** A, C

Base strings a,b are odd palindromes, and recursive productions add the same symbol at both ends, preserving that property, proving A. No production removes the central base symbol, refuting B. A palindrome equals its reversal, proving C. Both a and b are generated but their concatenation ab is not, refuting D. Recursive symmetry does not imply closure under concatenation.

## Q62

**Correct answer:** 2

Stack height begins at1, increases by1 on a and decreases by1 on b. An accepted length-five word needs two a's and three b's, with the height positive at every proper prefix. The only such words are aabbb and ababb. Other permutations empty the stack too early, preventing further input consumption. Final count balance alone is insufficient.

## Q63

**Correct answer:** 4

For f(x)=x³−3x, stationary points are±1. Checking those and endpoints±2 gives absolute value2 in all four cases; monotonicity between stationary points shows no larger value occurs. Alternatively f(x)=2 factors as(x−2)(x+1)²=0 and f(x)=−2 as(x+2)(x−1)²=0. The distinct maximizers are−2,−1,1,2, giving4. Count distinct locations rather than root multiplicities.

## Q64

**Correct answer:** 5

For flips at i<j, the error polynomial is x^i(1+x^(j−i)). Since g has nonzero constant term, the shift x^i does not affect divisibility. Modulo g, x³=1 and neither x nor x² is1, so the separation must be a multiple of3. Separation3 gives four pairs and separation6 gives one, total5. There are21 possible pairs overall, but only these have zero syndrome.

## Q65

**Correct answer:** 2

Row stride is4+p words and must be even. With p=0, block indices of the first words are0,2,4,6, mapping to sets0,2,0,2, so it fails. The next permitted p is2; stride6 gives block indices0,3,6,9 and sets0,3,2,1, all distinct. Therefore minimum padding2 words. Padding changes mapping through block indices, not directly through byte or word offsets alone.

