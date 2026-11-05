# Worked Solutions — GATE CS 2027 Mock Test 026

## Q1

**Correct answer:** A

The given explanation establishes a shared measurement basis, making A correct. It explicitly rejects B. It says nothing about deception, so C is unsupported, and explicitly uses currency/time units, disproving D. Comparability does not require equality.

## Q2

**Correct answer:** 2

For common floor k, n must lie in both[2^k,2^(k+1)) and[3^k,3^(k+1)). At k=0 the integer1 qualifies; at k=1 only3 qualifies. For k≥2,3^k≥2^(k+1), so the intervals do not overlap. Thus the two integers are1 and3. Equating logarithms themselves would solve a different question.
## Q3

**Correct answer:** A

For2k+1 original entries, the median has sorted rank k+1. Adding the smallest and largest values increases the size to2k+3 and shifts the old median's rank to k+2, exactly the new middle rank. A is true and B false. The appended extremes need not average to this middle value, disproving C; their placement suffices without all numerical entries, disproving D. Paired extreme insertions preserve the central order statistic.
## Q4

**Correct answer:** 22

The original surface area is24. Each removed corner cube had three exterior faces, so six exterior units disappear. Each also had three neighbours, one being the other removed cube, leaving two retained neighbours per removed cube whose shared faces become exposed. Add four, giving24−6+4=22. The face between the two removed cubes does not become a remaining-solid surface.

## Q5

**Correct answer:** 41

The increments for n=1,2,3,4 are2,6,12,20. Starting at1 gives a5=1+2+6+12+20=41. Four increments connect the first term to the fifth.

## Q6

**Correct answer:** 25

The triangles AOB and COD are similar, so AB/CD=OA/OC=2/3. Triangles AOB and BOC share the altitude from B to AC, so their areas are in the ratio OA/OC=2/3; hence BOC has area6. Similarly AOD has area6. Summing the four triangles gives4+6+9+6=25. Diagonals do not generally bisect each other in a trapezium, so the four areas need not be equal.
## Q7

**Correct answer:** C

The rule says nonanonymous implies includes-name. Only C has a true antecedent and false consequent. A and D are anonymous and therefore exempt under this rule, while B satisfies the requirement. No converse prohibition on names in anonymous submissions is stated.

## Q8

**Correct answer:** 16

Scale cost to100. Marked price is125 and required selling price105. The discount is20 out of125, or16%. Percentages apply to different bases; subtracting25−5 would use the wrong denominator.

## Q9

**Correct answer:** A, B, D

If p were true, the implication would force q true, contradicting exactly one true proposition. Thus A holds. The sole true proposition must be q or r, giving B and D. Either can be the true one, so C is not forced.

## Q10

**Correct answer:** 16

The quarter-turn about the square's centre permutes its vertices, leaving their x-coordinate sum4. Translation adds3 to each of four x-coordinates, adding12. Total16. Tracking the invariant set avoids computing four individual rotated coordinates.

## Q11

**Correct answer:** 2

For a2×2 matrix, det(A−I)=det(A)−trace(A)+1=6−5+1=2. This follows by expanding the two-by-two determinant or evaluating its characteristic polynomial at1. No assumption of diagonal form is required.

## Q12

**Correct answer:** A, B

Both one-sided function limits are0, matching f(0), proving A. Difference quotients are−1 from the left and1 from the right, proving B and disproving C. This same example disproves D. An extremum need not have zero derivative when differentiability fails.

## Q13

**Correct answer:** 2

Renaming without replacement relocates one directory entry and preserves the link count. Unlinking a different name removes one entry, reducing3 to2. A pathname's spelling is not an additional inode reference.

## Q14

**Correct answer:** 4

The expression contains+ , / , − and*, each emitted once after its children. The postfix form is ab+cde/−*, with four operators. Translation changes order, not the expression tree's operator count.

## Q15

**Correct answer:** 0

Squaring either possible X gives Y=4 with probability1. A constant random variable has zero variance. Nonzero variability of X does not imply variability after a many-to-one transformation.


## Q16

**Correct answer:** 128

The /26 range64–127 is wholly inside the /25 range0–127. Their union is the larger range, with128 addresses. Adding the range sizes would double-count the overlap.

## Q17

**Correct answer:** 30

The two successful reads advance by4 and6, for a total of10. The final offset is20+10=30. A short read's returned count, not its requested count, determines that call's progress.

## Q18

**Correct answer:** A, B, D

Lexicographic row-count minimization favours2 over3 regardless of the secondary cost, so A holds. Cost-first favours6 over8, proving B. These different outcomes disprove C and demonstrate D's ambiguity. State the optimization objective before comparing covers.

## Q19

**Correct answer:** A, C

If f mapped two distinct A elements together, their compositions would coincide, contradicting injectivity; A follows. Distinct points of f(A) also cannot be identified by g, proving C. g may identify points outside that image without affecting the composition, so B is not necessary. For example, embedding a smaller set in B need not be onto, disproving D.

## Q20

**Correct answer:** 0.2

Collision requires a(x−y)=0 modulo5. Since5 is prime and x−y is nonzero modulo5, this occurs only for a=0, one of five equally likely choices. Probability1/5=0.2. Distinct keys need not have distinct hashes for every member of the family.

## Q21

**Correct answer:** 5

Arguments are19,9,4,2,1. There are five invocations, with the last returning without recursion. The count includes both endpoints of the call chain.

## Q22

**Correct answer:** 32

The caller's actual array has size10×4=40. In the parameter declaration, a is adjusted to a pointer and sizeof(a)=8. The difference is32. A bracketed parameter bound does not preserve array-object type for sizeof inside the function.

## Q23

**Correct answer:** 3

Recoverability requires commit(T1) before commit(T2). Exactly half of the six permutations have this order:123,132,312. T3 may be before, between or after the dependent pair. Read-from dependencies constrain commit order even when a third transaction is independent.

## Q24

**Correct answer:** A, B, D

The writes are to x and y separately, so A holds. Together they leave0,0 and violate the invariant, proving B,D. In a serial order, the second transaction sees the first variable become0 and does not perform its conditional write, preserving the invariant; C is false. This is a write-skew pattern rather than a direct write collision.

## Q25

**Correct answer:** B

By-value parameter assignment changes the callee's own scalar copy, proving B and disproving A,D. The parameter can normally be assigned like another local scalar, so C is false. Passing a pointer value would be a different situation expressly excluded here.

## Q26

**Correct answer:** 16

There are eight inclusive ports per address and two addresses, giving16 distinct endpoint pairs. Distinguish the inclusive port count from4007−4000=7.

## Q27

**Correct answer:** 2

A's next field and C's prev field must each change, giving two surviving-node pointer updates. Fields inside the removed node are not included in the question's count.

## Q28

**Correct answer:** -8192

The minimum12-bit signed value is−2^11=−2048. Scaling by four bytes gives−8192. Signed range and displacement scaling are separate steps.

## Q29

**Correct answer:** A, B

The full sum is A+(2^w−1−B)+1=A−B+2^w, so its low bits give the modular difference, proving A. Its carry-out is1 precisely when A≥B, the no-borrow case, proving B. This does not diagnose signed overflow, making C false. Identical low differences can arise with and without borrow, disproving D.

## Q30

**Correct answer:** 31

Work counts are16,8,4,2,1 before i becomes0. Their sum is31. The geometric total is about twice n, not n times the number of halving steps.

## Q31

**Correct answer:** A, C

Epsilon specifies no consumed input, not no state or stack action, so A,C are true. B overrestricts stack behavior, and D misinterprets epsilon as an actual character. Several internal moves may occur without advancing the input head.

## Q32

**Correct answer:** 12

Each of12 employees participates exactly once, so there are12 pairs. A department may participate in many of these pairs or none. Multiplying employee and department counts would ignore the exactly-one ownership condition.

## Q33

**Correct answer:** A, B, D

A finite union of singleton strings has a regular expression and hence a DFA, proving A,D. Regular languages are context-free, proving B. A finite language need not contain ε, so C is false. Finiteness guarantees recognizability classes, not particular members.

## Q34

**Correct answer:** 10

Eigenvalues of A² are9 and1, whose sum is its trace10. Trace(A²) is not generally(trace(A))², which would give4 here.

## Q35

**Correct answer:** 2

x XOR x is always0, so the output is0 OR y=y. The assignments with y=1 and either x value produce1, giving two. Tied inputs are not independent signals.

## Q36

**Correct answer:** 4

The join contributes (1,x,p),(1,x,q),(1,y,p),(2,x,p),(2,x,q). Projection produces (1,p) twice before duplicate elimination. Under set semantics the result is {(1,p),(1,q),(2,p),(2,q)}, of size4. Counting join tuples without applying projection's duplicate elimination gives the wrong answer5.

## Q37

**Correct answer:** 4

The possible (|x|,|y|) pairs are (0,1),(0,2),(0,3),(1,1),(1,2),(2,1). The first two remove or repeat only a's; (1,1) also pumps only a, and (2,1) pumps only b. All four preserve an a-block followed by a b-block, including when i=0. The remaining y strings, aab and ab, contain both letters; pumping twice introduces a b followed by an a. Thus exactly four decompositions work. The lemma does not require every admissible decomposition to work.

## Q38

**Correct answer:** A, C

The only child thread is T1, while the copied mutex records a lock whose owner has no surviving child thread. With no repair or possible releaser, a wait can persist indefinitely: A,C are true. B contradicts the specified fork model. D confuses a private copied mutex with shared synchronization storage; changing the parent's copy does not unlock the child's. The conclusion depends on the explicit model, not on assuming arbitrary library calls are safe after fork.

## Q39

**Correct answer:** 4

The reachable cycle is 000,001,011,111,110,100, then 000. Exactly 011 and110 have two set bits. Twelve observations consist of two complete six-state cycles, giving4 output-one observations. Count the initial state as requested; do not assume the register traverses all eight binary states.

## Q40

**Correct answer:** A, D

Simulate at most k transitions while checking the halting condition, including the initial configuration if k=0. This always terminates, so A is true and B false. An m-bit value of k can be about 2^m, supporting D. No universal finite simulation bound decides unrestricted eventual halting, so C is false. Large finite running time and undecidability are different properties.

## Q41

**Correct answer:** 8

State1 records that the latest symbol was a without any aa yet. State2 records that aa has occurred and is absorbing. Count strings avoiding aa: if F(n) is their count, F(n)=F(n−1)+F(n−2), with F(0)=1,F(1)=2. Hence F(2)=3,F(3)=5,F(4)=8. Subtract from all16 length-four strings to get8 accepted strings. Counting occurrences instead of strings can double-count words such as aaaa.

## Q42

**Correct answer:** A, C

The outer R(x,y) requires membership. The negated existential rules out another y value for that same x, so A,C are true. Other x values are irrelevant to this test, making B false. The membership conjunct excludes pairs outside R, making D false. Uniqueness is per x, not a requirement that the whole relation contain one tuple.

## Q43

**Correct answer:** 1

Continuity on the closed interval and differentiability inside allow Rolle's theorem: some c in (0,2) satisfies f'(c)=0. For any interior u<v, apply the mean value theorem to f' on [u,v]; f'(v)−f'(u)=f''(w)(v−u)>0. Thus f' is strictly increasing and cannot have two zeros. Existence and uniqueness together give exactly1. Strict convexity alone must still be combined with the endpoint equality to establish existence.

## Q44

**Correct answer:** 35

Only two jobs fit. The two largest profits sum to20+15=35, an upper bound for any schedule. A in slot1 and B in slot2 attains it and respects both deadlines. Therefore the optimum is35. Choosing by profit requires checking feasibility; the upper bound is not automatically attainable for arbitrary deadlines.

## Q45

**Correct answer:** 2

Entering V, execution must remember both where V returns inside U and where U returns inside Main. These are two distinct live return addresses. Overwriting the sole link register on U's call to V loses the older one unless another location preserves it. The question asks the required simultaneous information, not the number of registers already supplied.

## Q46

**Correct answer:** 11

Track K, the best nonempty subarray sum ending at each position with no deletion, and D, the best with exactly one deletion, allowing the last element to be the deleted one. Initialize K=4,D=−infinity. For each next x, set D'=max(D+x,K) and K'=max(x,K+x). The successive K values are4,3,5,−2,5,3,6; D values are −infinity,4,6,5,10,8,11. The maximum is11. It is attained by taking the full array and deleting −7. Removing an element anywhere in the array without respecting a contiguous enclosing interval is a different problem.

## Q47

**Correct answer:** 0.5

There are 2^10 total locations but only 2^9 distinct supplied addresses because A9 is fixed. All nine lower bits vary independently, so exactly half the locations are reachable: 2^9/2^10=0.5. Chip selection enables the device; it does not provide an additional internal address bit.

## Q48

**Correct answer:** 100

ACK400 covers bytes through399, so the transmitted prefix100–399 is acknowledged. The half-open SACK block covers500–699. The only uncovered transmitted interval is400–499, containing100 bytes. Neither acknowledgment includes byte400 through the cumulative ACK, and the exclusive right endpoint700 is not a transmitted byte here.

## Q49

**Correct answer:** 3

Compute t1=a+d, t2=b+c, result=t1*t2: two additions and one multiplication. The factorized expression has three binary internal nodes, each requiring an operation in this representation. Factoring is valid under the stated mathematical-integer semantics; machine overflow or floating-point reassociation would require separate justification.

## Q50

**Correct answer:** A, C

Both first operations are sends and require a receive that neither process has reached; A is true and B false. If Q receives first, it matches P's send, after which Q's send can match P's receive; C is true. A mutex can keep a needed partner from entering its communication sequence and does not create a receive, so D is false. Textual presence of matching operations is insufficient when blocking order prevents reaching them.

## Q51

**Correct answer:** A, C

Once queued bytes have been read, an orderly end of the peer's sending stream can be reported by a zero receive result, proving A. Zero is a count, not an extra byte: B is false. TCP maintains two directions; closing one sending direction does not itself close the other, so C is true and D false. An orderly half-close differs from a connection error or forced process exit.

## Q52

**Correct answer:** 7

After push7, m=7. Push3 stores −1 and sets m=3; push5 stores5. Push−2 stores−7 and sets m=−2. Popping−7 returns−2 and restores m=2(−2)−(−7)=3. Popping5 returns5. Push1 stores−1 and sets m=1. Its pop returns1 and restores m=3; the next stored−1 pop returns3 and restores m=7. Returned values sum −2+5+1+3=7. Encoded negative entries are restoration information, not the logical popped values.

## Q53

**Correct answer:** A, C

A is realized by a root whose left child is a leaf and whose right subtree has a left leaf and a right pair of leaves. C is the complete depth-two tree. B is impossible: a first leaf at depth2 lies in the root's left subtree, which must supply at least one more leaf before the root's right depth-one leaf can appear; the second leaf cannot already have depth1. In D the depth-one leaf is third, so it would have to be the root's right leaf and therefore last, a contradiction. All four lists satisfy the numerical sum of 2^(−depth)=1, but that condition alone does not enforce the specified left-to-right order. Ignoring order would incorrectly accept B and D.
## Q54

**Correct answer:** 0.6667 (accepted range 0.66665–0.66675)

For bag A, P(first blue,second red)=(1/3)(2/2)=1/3. For bag B it is (2/3)(1/2)=1/3. Averaging gives joint probability1/3. By symmetry of draw positions, the second-red probability is (1/2)(2/3)+(1/2)(1/3)=1/2. The requested conditional probability is (1/3)/(1/2)=2/3, rounded to0.6667. Conditioning changes the bag mixture; one cannot simply average the two within-bag conditional probabilities with the original equal weights.

## Q55

**Correct answer:** 18

Bank indices are0,0,1,1,2,2,3,3. Issue cycles are respectively0,3,4,7,8,11,12,15: each consecutive same-bank pair incurs a wait until the bank is free, and switching banks still obeys one issue per cycle. The final request finishes at15+3=18. The controller cannot issue later independent requests early because requests must remain in order.

## Q56

**Correct answer:** B, C

A conditional can avoid evaluating an unsafe expression. Unconditionally evaluating it can introduce invalid division even if the eventual selected arithmetic value seems unchanged. Hence B,C are true and A false. D is false precisely because branch removal can introduce extra evaluations. Safety and side effects must be checked in addition to value identities; the stated proof is relevant, not a universal sufficient condition for all transformations.

## Q57

**Correct answer:** 15.9375

The stored signed integer runs from−128 to127. Scaling gives endpoints−8 and127/16=7.9375, so the interval width is7.9375−(−8)=15.9375. There are256 representable points but only255 gaps between the extreme values. Confusing point count with interval width gives16 incorrectly.

## Q58

**Correct answer:** 4

Only key1 matches. Each of A's two occurrences matches each of B's two, giving2×2=4 rows. Keys2 and3 have no partners. Projection without DISTINCT preserves those four occurrences under bag semantics. A join is not a one-to-one pairing of duplicate rows.

## Q59

**Correct answer:** A, B

Ascending insertion gives a right-child chain with n−1 edges, so A is true. The BST invariant ensures that inorder traversal returns sorted keys, proving B. For keys1,2,3, inserting2 first can give a balanced root, whereas inserting1,2,3 gives a chain; C is false. The chain has sorted inorder output but linear worst-case search, refuting D. Traversal order does not certify balance.

## Q60

**Correct answer:** A, B, D

The feasible pairs are (1,2),(2,1), both with sum3, so A is true. Joining x's constants1 and2 produces nonconstant; y does the same. Their pairing is lost, proving B and refuting C. A relational invariant x+y=3 can preserve that fact, proving D. Independent possible-value information can admit infeasible combinations unless correlations are retained.

## Q61

**Correct answer:** 2

a must be first and d last. The middle elements b,c are incomparable and can occur in either order. Thus the extensions are a,b,c,d and a,c,b,d, giving2. A linear extension must preserve existing comparisons but can choose an order for incomparable elements.

## Q62

**Correct answer:** 30

Only one root-to-leaf path has live nested calls at a time because siblings are processed sequentially. Its internal buffers have sizes16,8,4,2; their sum is30. Leaves allocate0. Equivalently M(n)=n+M(n/2), M(1)=0, giving M(16)=30. Summing allocations over both children counts total activity rather than simultaneous live storage.

## Q63

**Correct answer:** 7

Below4, spacing is1/4, so the predecessor is3.75; above4, spacing is1/2, so the successor is4.5. The rounding interval for4 therefore extends from midpoint3.875 to midpoint4.25. Both ties round to4 because its significand1000 has even low bit, whereas neighbouring significands1111 and1001 have odd low bits. Multiplying endpoints by16 gives k=62 through68 inclusive, seven integers. The rounding interval is asymmetric at a binade boundary.

## Q64

**Correct answer:** A, C

A positive TTL permits reuse of a cached answer until its expiry under this model, so A is true. TTL is a lifetime field, not a push channel; B is false. Changing the authoritative TTL does not edit already stored expiry times, proving C. The authoritative value can change during a cached record's lifetime, so D is false. Caching freshness is bounded by reuse policy, not guaranteed by preventing updates.

## Q65

**Correct answer:** 2

The determinant is t(2−1)−2=t−2, so only t=2 is singular. A unit-lower/upper factorization of a nonsingular matrix requires nonzero leading pivots. Here u11=t and the leading two-by-two determinant is t−1; for t≠0, the second pivot is (t−1)/t. Thus t=0 and t=1 obstruct unpermuted LU while remaining nonsingular. For t=3,4,5 both leading pivots and the determinant are nonzero, so elimination succeeds. Exactly two choices qualify. Nonsingularity alone does not guarantee elimination without row exchanges.

