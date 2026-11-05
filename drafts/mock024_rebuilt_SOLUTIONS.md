# Worked Solutions — GATE CS 2027 Mock Test 024

## Q1

**Correct answer:** 45

Among respondents,120×0.75=90 support. The minimum occurs if none of the80 nonrespondents support, giving90/200=45%. The response rate prevents treating75% as a guaranteed percentage of the whole invited group.

## Q2

**Correct answer:** 2

Reflecting x=4 across x=4 leaves it unchanged, so the first fold contributes no distinct second x-coordinate. The two y-preimages are2 and6. The distinct original points are(4,2),(4,6), giving two, not four. Fold-line points must not be counted twice.

## Q3

**Correct answer:** C

Both weighing and obtaining the address must precede mailing; their mutual order is unspecified. A and B satisfy this, and D accurately recognizes both possibilities. C places address acquisition after mailing, contradicting the account. Partial order information need not specify a unique chronology.

## Q4

**Correct answer:** 2.5

The red ball's position is uniform among1,2,3,4, and that position equals the stopping draw count. The mean is(1+2+3+4)/4=2.5. Sampling stops at the red ball but does not bias its initial random position.

## Q5

**Correct answer:** B

Discrete means distinct or separate; discreet means tactful or careful about confidential matters. B assigns both meanings correctly. A reverses them; C misuses the second word; D misuses the first.

## Q6

**Correct answer:** 9

After k multiplications the quantity is3×2^k. At k=8 it is768, while at9 it is1536. Monotonic growth makes9 the first value exceeding1000. The initial value3 is not itself a multiplication.

## Q7

**Correct answer:** C

At n=40 the expression is1600+40+41=1681=41², composite. Thus C supplies a counterexample. A and B are positive examples and cannot prove universality; D only establishes oddness in one case, which is not primality. One verified counterexample refutes a universal conjecture.

## Q8

**Correct answer:** 2

The first rotation leaves the original−x face pointing−x. The second positive y rotation maps−x to+z. Hence the original−x face ends upward, code2. Equivalently the composite maps(x,y,z) to(y,−z,−x), and solving for output(0,0,1) gives input(−1,0,0). The axes are fixed world axes, not changing body axes.

## Q9

**Correct answer:** 11

The flip counts are1,2,1,3,1,2,1 for000→001→010→011→100→101→110→111. Their sum is11. Binary carries can flip several positions at once; this is not a Gray-code listing.

## Q10

**Correct answer:** 5.64

Water volume is100×5=500 cubic centimetres. The cube displaces64, so100h−64=500 and h=5.64. Since5.64>4, the stipulated full submergence is self-consistent. The cube's volume, not just its footprint, changes the level once submerged.

## Q11

**Correct answer:** 160

Divide by2^n and set bn=an/2^n. The recurrence becomes bn=b(n−1)+1 with b0=0, so bn=n. Hence a5=5×32=160. The forcing term grows at the same rate as the homogeneous multiplier and contributes the additional factor n.
## Q12

**Correct answer:** A, C

Stability preserves the input order of equal-key records, proving A and C. It does not impose a complexity bound, so B is false. Sorting must generally reorder unequal keys, disproving D. Stability is a tie-order property.

## Q13

**Correct answer:** 0

Lookahead a belongs to FOLLOW(A), while the nonempty production begins with b. The parser selects A→ε, adding zero terminals. The existing a on the stack from S→Aa is subsequently matched; it is not added by this A production.

## Q14

**Correct answer:** A, C

A write fault can allocate and copy a private page, preserving the other process's contents, so A and C are true. Deferred copying is the point of copy-on-write, disproving B. Initial physical sharing does not force permanent shared-write semantics, disproving D.

## Q15

**Correct answer:** 3

*p++ means*(p++): x receives the old a[0]=1 and p advances to a[1]. The next statement adds1 to a[1]=2, yielding3. The increment changes the pointer, not the dereferenced integer in the first statement.

## Q16

**Correct answer:** A, B

The IPv4 header checksum covers the source address, so A is true. TCP includes its ports and a pseudo-header containing IP addresses, making B true. C and D incorrectly omit checksum-covered fields. Rewriting at one protocol layer can affect integrity checks at another.

## Q17

**Correct answer:** 6

The stipulated timeout rule sets the threshold to10/2=5 and window to1. Sum6. Use the explicitly supplied simplified rule rather than assuming another congestion-control variant or retaining the old threshold.

## Q18

**Correct answer:** 2

The first accesses to0 and4 are compulsory misses. They map to the same line and evict each other, so the final0 and4 accesses also miss; these are the two requested conflict misses. Classification and total miss count are different quantities.

## Q19

**Correct answer:** 4

The base production accounts for the first d. Each recursive production adds one more d, so five digits require four recursive applications. Attribute evaluation follows the parse structure but does not change the production count.

## Q20

**Correct answer:** B

A separate slot in every active activation record preserves each call's local value, making B correct. A overwrites older calls' values, C cannot represent arbitrary evolving locals, and D confuses control information with variable storage.

## Q21

**Correct answer:** 7.75

All five value bits set to1 gives raw31, scaled by2², or31/4=7.75. Three integer bits permit values below8, not a representable endpoint8 in this format.

## Q22

**Correct answer:** 32

Each nonbase call creates two children with argument reduced by one. There are five branching levels before the leaves, giving2^5=32 base calls. The question asks only for leaves, not all63 invocations.

## Q23

**Correct answer:** A, C

Negating NOT p OR q gives p AND NOT q, so A is true. Under p=true, p XOR q equals NOT q; under p=false, conjunction with p is false, proving C equivalent. B is the original implication and D represents the opposite asymmetric case.

## Q24

**Correct answer:** A, B

The two zeros compare equal but have distinct signs; reciprocal division can yield positive versus negative infinity, proving A,B and disproving C. Infinity is outside the finite representable values, so D is false. Numeric equality need not imply bitwise equality.

## Q25

**Correct answer:** 0.48

After the first key chooses any bucket, the second must avoid one bucket (probability4/5) and the third avoid two (3/5). Product12/25=0.48. Uniform independent placements allow multiplication of these conditional probabilities.

## Q26

**Correct answer:** A, C

The link's stored path may stop resolving after deletion, so A is true. Pathnames can cross mounted file systems, making C true. Symbolic links do not increment the target's hard-link count or inherently retain its inode, so B,D are false. Name resolution and inode reference counting are separate.

## Q27

**Correct answer:** 1

Rank-nullity gives nullity3−2=1. A nonempty solution set is one particular solution plus the null space, an affine line. Consistency is necessary to speak of a nonempty affine solution set.

## Q28

**Correct answer:** 256

The transfer comprises4096/16=256 whole bursts and hence256 handshakes. This counts the stipulated burst grants, not individual byte transfers.

## Q29

**Correct answer:** A, C

Acceptance by a recognizer certifies membership, so A is true. A sufficiently long computation may still accept later, invalidating B's arbitrary cutoff. Deciders halt on every input, proving C; recognizers need not, disproving D.

## Q30

**Correct answer:** 3

For x≠1, factoring the numerator gives f(x)=x²+x+1. Its limit at1 is3, the unique continuous extension. The original undefined quotient does not prevent a removable extension.

## Q31

**Correct answer:** 0.6875

E[X]=0+1/4+2/4=3/4. E[X²]=1/4+4/4=5/4. Variance=5/4−9/16=11/16=0.6875. Square the mean, not the individual probabilities, in the variance formula.

## Q32

**Correct answer:** 1

Any b sends the machine to the rejecting sink permanently. Only aaaa is accepted at length4, giving one string. The accepting initial state also accepts ε, but that string has length0 and is excluded here.

## Q33

**Correct answer:** A, B

A selects at least one true input but excludes both true, while B explicitly selects the two unequal-input cases. Both are XOR. C also accepts11; D complements XOR and accepts equal inputs. A truth table verifies all four cases.

## Q34

**Correct answer:** A

A reader must not commit before the transaction whose value it read if recoverability is required. Otherwise a later writer abort would invalidate an already committed reader. A is correct; B,C,D concern unrelated properties and do not address the commit dependency.

## Q35

**Correct answer:** A, B

An exclusive lock blocks conflicting reads until the writer ends, preventing those dirty reads and their cascading aborts, so A,B are true. Transactions can still wait cyclically for locks, disproving C. D directly violates retention until commit or abort. Strictness and deadlock freedom are different guarantees.

## Q36

**Correct answer:** B

Let m=floor(log2 n). At outer iteration i=2^k, the inner values are2^(2^r), so there are floor(log2 k)+1 iterations. Summing for k=1..m givesΘ(m log m)=Θ(log n log log n). B is correct. A omits the growing inner count, C treats the outer loop as linear in n, and D treats the inner squaring loop as ordinary doubling.

## Q37

**Correct answer:** 1

Close-on-exec is a descriptor flag. Descriptor3 is closed by successful exec, while descriptor4 was not flagged and remains. Both initially referred to the same open-file description, but their flags are distinct. One descriptor remains.

## Q38

**Correct answer:** A, B, D

The aS production adds an unmatched leading a; aSbS adds a matched enclosing pair around the first S and then a valid suffix. Structural induction shows no generated prefix has more b's than a's, proving B and hence A. ba violates that prefix condition, disproving C. Derive aab via S→aS→aaSbS→aab using epsilon subderivations, proving D.

## Q39

**Correct answer:** 3

No four-cell cube avoids both000 and111: fixing any one variable still admits one of them. Thus a valid cube covers at most two of the six1-inputs, giving a lower bound of three terms. The cubes a'c, bc' and ab' cover disjoint pairs001/011,010/110,100/101, attaining three. A power-of-two group cannot cross a specified zero.

## Q40

**Correct answer:** B, C

The stream abc could split as a|bc or ab|c, so B is true. A length field can disambiguate such splits, proving C. TCP preserves bytes and order, not application record boundaries, so A,D are false. Network read sizes cannot replace a framing protocol.

## Q41

**Correct answer:** 6

The first fork gives two processes. Each then forks, giving four, of which the two newly created children enter the conditional body and each fork once more. Total6. The condition is evaluated separately in each parent/child return path.

## Q42

**Correct answer:** 2

Three-bit reversal pairs1(001) with4(100), and3(011) with6(110). Indices0,2,5,7 are fixed. Therefore there are two swaps. Counting each direction separately would double-count the pairs.

## Q43

**Correct answer:** 3

p is always evaluated. If p is false, q is skipped and r is evaluated: subset{p,r}. If p and q are true, r is skipped: {p,q}. If p is true and q false, all three are evaluated. These are three distinct subsets. Truth assignments sharing a control path need not create new subsets.

## Q44

**Correct answer:** 6

Issue M1 at0 and M2 at1; their results arrive at3 and4. A can issue at4 and finish at5. B issues at5 and finishes at6. Independent multiply overlap does not remove the need to wait for the later operand.

## Q45

**Correct answer:** A, B

Q covers a superset of P's columns at lower cost. If a cover contains P but not Q, replacing P by Q preserves coverage and reduces cost; if it already contains Q, dropping P preserves coverage. Thus A,B hold. C ignores dominance, and D ignores the objective's cost comparison: a larger but more expensive row need not dominate.

## Q46

**Correct answer:** 12

Every student-course pair participates, so the relationship contains3×4=12 rows. The pair of entity keys identifies a row and its grade. Many-to-many cardinality is represented by a relationship table, not one row per student or per course.

## Q47

**Correct answer:** 72

The equation g∘f=id_A forces f injective. Choose distinct images for A's three labelled elements in4×3×2=24 ways. g is then forced on those three images, while its value on the unused B element is any of three A elements. Total24×3=72. A left inverse need not be uniquely determined outside the image.

## Q48

**Correct answer:** A, C, D

The original successor's value occupies p's position and its node is bypassed, giving the value sequence in A. A successor is needed to perform that operation, proving C. The actual removed node is the successor, not p; external references can distinguish this, so D is true and B false. Value-sequence equivalence is weaker than identity preservation.

## Q49

**Correct answer:** 2

First read the pointer at1012; its value2040 supplies the second read's address for the operand. Thus two data-memory reads are required. Address arithmetic itself is not a memory read, and the operand's four bytes are one specified word read here.

## Q50

**Correct answer:** B, C

Write A=2I+N with N²=0 and N≠0. Then A⁵=32I+5×16N=32I+80N. This proves B,C and disproves D. The eigenspace solves Nv=0 and has dimension1, not2, so A is false. Repeated eigenvalues do not ensure diagonalizability.

## Q51

**Correct answer:** 0.1481 (accepted range 0.14805–0.14815)

For f=x²−x³, f'=2x−3x²=x(2−3x). The interior critical point is2/3; the endpoints give0 and the interior value is4/27≈0.148148. It is the global maximum on the closed interval. Compare endpoints as well as stationary points.

## Q52

**Correct answer:** 3

The first three sends fill the three slots. The fourth finds no capacity and blocks before completing, so three have completed. Counting attempted sends would give four, which is not the requested quantity.

## Q53

**Correct answer:** A, C

An earliest-finishing interval ends no later than the first chosen interval in an optimum, leaving at least as much remaining scheduling time, proving A. Half-open endpoints allow back-to-back compatibility, proving C. Weighted objectives can prefer a later-finishing higher-value interval, so B is false. A long interval can block many short intervals, disproving D. The exchange proof relies on the equal-value cardinality objective.

## Q54

**Correct answer:** 5

Start at height1. Two a's push four symbols, reaching height5; the following four b's return it to1 without underflow. The maximum is5. Include the bottom marker and the two-symbol push rule.

## Q55

**Correct answer:** A, B, D

The identity holds over integers and remains equal after reduction modulo2^w, proving A,B. Whether the rewrite helps depends on instruction costs and target code generation, proving D. Semantic reasoning must still respect the language and representation, so the broad permission in C is false. Equivalence and profitability are separate tests.

## Q56

**Correct answer:** 1

The projection is{1,2}; duplicate occurrences of1 collapse under set semantics. Difference from{1,2,3} leaves{3}, containing one tuple. Projection cardinality does not equal the number of input tuples here.

## Q57

**Correct answer:** A, C, D

Rename the inner bound variable to y to obtain R(x) AND exists y S(y), proving A. The existential part is independent of the free output x: it is true for nonempty S and false for empty S, proving C,D. It does not test S(x), so B's intersection interpretation is false. Equal variable spellings do not override quantifier scope.

## Q58

**Correct answer:** 5000

The full response sends5200 bytes; the revalidation response sends200. Saving=5000 bytes. The cached body is reused locally and is not retransmitted as part of the specified304 response.

## Q59

**Correct answer:** 20

The exact unsigned sum is20. Low bits hold4 and carry-out1, reconstructing4+16=20. Carry-out restores the fifth bit omitted from the four-bit result.

## Q60

**Correct answer:** 1

Rear advances for six successful enqueues in total, ending at6 modulo5=1. Front advances twice to2; the queue then holds four elements, the maximum allowed with one reserved slot. Dequeues do not move rear.

## Q61

**Correct answer:** A, B, D

Forwarding normally creates a new link-layer header for the outgoing link, while IP destination remains end-to-end, proving A,D and disproving C. TTL is within the IPv4 header and affects its checksum, proving B. Different layers can legitimately change different fields at the same hop.

## Q62

**Correct answer:** 15

The selection tree has16 data leaves and every internal node is a two-input multiplexer. A full binary tree has one fewer internal node than leaves, giving15. Equivalently8+4+2+1=15 across the levels.

## Q63

**Correct answer:** 4

The LCS length is2, attainable by AA or BA. The unequal length-three strings cannot have a common subsequence of length3. Shortest common supersequence length is3+3−2=4, attained for example by ABAA. Aligning an LCS avoids duplicating those matched characters.

## Q64

**Correct answer:** A, B, C

Only reachable incoming values describe possible executions. Ignoring the unreachable7 leaves constant5, proving A,B. Including it would join5 with7 and lose constancy, proving C. D contradicts this example. Semantic reachability can sharpen a syntactic data-flow join.

## Q65

**Correct answer:** B, C

P(both positive)=0.1×0.9²+0.9×0.2²=0.081+0.036=0.117, proving B. Bayes gives0.081/0.117=9/13, proving C. Each marginal positive probability is0.27, whose square0.0729 differs from0.117, so A is false. After one positive the posterior is0.09/0.27=1/3; the second raises it to9/13, disproving D. Conditional independence does not imply unconditional independence.

