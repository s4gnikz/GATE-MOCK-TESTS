# Worked Solutions — Mock Test 034

## Q1

**Correct answer:** C

The reply permits both agreement and refusal as interpretations, so C captures its ambiguity. A describes length without addressing meaning; B describes evidential support; D contradicts the possibility of refusal. The explanatory clause establishes the relevant sense without requiring a claim about the witness's intent.

## Q2

**Correct answer:** 2

Let the common floor be k≥0. The integer must lie in both[2^k,2^(k+1)) and[3^k,3^(k+1)). For k=0 only x=1 qualifies; for k=1 only x=3 qualifies. For k≥2,3^k≥2^(k+1), since9>8 and the ratio grows by3/2 each step. The intervals are disjoint thereafter. Thus the qualifying integers are1 and3, giving2. Equality of floors does not require equality of logarithms.

## Q3

**Correct answer:** A, C

(3k+1)²=3(3k²+2k)+1, proving A. A finite list alone does not prove the rule for all integers, so B is false. For n=2, n²=4 has remainder1, proving C and giving a counterexample to the converse in D. A true implication need not have a true converse.

## Q4

**Correct answer:** 72

The original outside surface has6×9=54 unit faces. Removing the six face-centre cubes removes six old exposed squares, leaving48 exterior squares. Each removed face-centre cube exposes four side faces of neighboring remaining cubes; its inward neighbor is the removed central cube. These six disjoint sets add24 faces. The central removed cube has only removed face-centre cubes as neighbors, so it adds no further boundary against the remaining solid. Total48+24=72. Counting six new faces for every removed cube would count contacts between two removed cubes.

## Q5

**Correct answer:** 10

The increment2n+1 is (n+1)²−n², so telescoping gives an=n²+1. The strict condition n²+1>100 holds first at n=10, since a9=82 and a10=101. The initial value adds1 to the usual square sequence.

## Q6

**Correct answer:** 1.394 (accepted range 1.3935–1.3945)

The garden has area96; the central rectangle must have area48. Its dimensions are12−2w and8−2w. Their product48 gives4w²−40w+48=0, or w²−10w+12=0. Roots are5±sqrt(13); only5−sqrt(13)≈1.3944487 lies between0 and4. The larger algebraic root is physically impossible. The stated three-decimal range includes the rounded result and exact value.

## Q7

**Correct answer:** B

B attaches the storage clause directly to “samples” while retaining the researcher as the agent of analysis. A makes the introductory participle modify the researcher; C reverses the analysis roles; D explicitly attaches storage to the researcher and also uses an inappropriate relative pronoun for a person. Modifier placement determines which noun has the property.

## Q8

**Correct answer:** 42

Initially there are3 litres of salt-solution component. Removing one fifth leaves2.4 litres, with volume restored to10. Removing half of that mixture leaves1.2 litres of the component. The replacement contributes5×0.6=3 litres, giving4.2 litres in10, or42%. Each removal uses the concentration at that stage, not the original30% throughout.

## Q9

**Correct answer:** 3

If the token is in A, labels B,C are true. In B, labels A,C are true. In C, only A is true. In D, labels C,D are true. Therefore A,B,D are consistent, three possible locations. Exactly two true labels does not uniquely identify a box in this instance.

## Q10

**Correct answer:** 8

T then U maps(1,1) to(1,−1) then(3,−1). U then T maps it to(3,1) then(1,−3). The coordinate difference is(2,2), whose squared length is4+4=8. Translation and rotation need not commute; comparing their order is essential.

## Q11

**Correct answer:** A, B

An open descriptor refers to the opened file object rather than repeatedly resolving its pathname. Thus R retains F(A), while the replaced directory entry sends a later open to G(B). C confuses the directory entry with the existing open-file reference. D is false because the open reference can keep F alive after its last name is removed. Atomic replacement affects pathname visibility, not the identity of already-open files.

## Q12

**Correct answer:** A, C, D

The determinant is−1 independently of t, proving A. Multiplying L=[[1,0],[l,1]] by U=[[u,v],[0,w]] forces u=t,v=1,lt=1,and l+w=0. If t=0, lt=1 is impossible, so B is false. If t≠0, choose l=1/t,w=−1/t, proving C,D. Invertibility does not guarantee an LU factorization without pivoting.

## Q13

**Correct answer:** 4

For A→B, the switch learns A on port1, but B is unknown, so it floods to ports2,3: two copies. B→A teaches B on port2 and is forwarded only to port1: one copy. C→A teaches C on port3 and also uses only port1: one copy. Total2+1+1=4. Learning uses source addresses; the first destination does not become known merely because it appeared as a destination.

## Q14

**Correct answer:** 20

The root is5. Its left subtree is rooted at3 with children1,4; its right subtree is rooted at7 with right child8. Root5 must be first. The three left-subtree insertions can interleave with the two right-subtree insertions in C(5,3)=10 ways. The left subtree has two valid orders,3,1,4 and3,4,1; the right has only7,8. Total10×2=20. Subtree interleavings preserve internal ancestor-before-descendant requirements.

## Q15

**Correct answer:** 1

Split at the sign change x=1. On[0,1], the integrand is x−x², whose integral is1/6. On[1,2], it is x²−x, whose integral is5/6. Their sum is1. Dropping the absolute value would subtract rather than add the first region's area.

## Q16

**Correct answer:** B

At most one observation of the first dataset is strictly below2, and at most one of the second is below2 because its median is9. Thus the combined third observation is at least2. Similarly, at most two combined observations exceed9, so the fourth is at most9. Their average lies in[2,9], proving B. For datasets(0,2,3) and(8,9,10), the median is5.5 and need not be an observed value, disproving D. Datasets(0,2,2) and(2,9,9) give combined median2, disproving A. Extreme tail observations make the mean arbitrarily large or small, disproving C.

## Q17

**Correct answer:** 0

Index2 has children at indices4,5 in a seven-element heap. Both must have larger keys than their parent in a distinct-key min-heap, but7 is the largest available key. The stipulated position is impossible, so there are zero such heaps. A heap's largest key must be at a leaf, though a particular leaf is not prescribed.

## Q18

**Correct answer:** 2

Using the first S production i times and the first T production j times gives a^i b^j a^j b^(2i), of length3i+2j. Nonnegative solutions to3i+2j=6 are(i,j)=(0,3),(2,0), producing bbbaaa and aabbbb. They are distinct, so the count is2. Different derivation stages contribute different amounts to total length.

## Q19

**Correct answer:** C

Any adjacent map cells differ in exactly one input, which changes parity. Hence no two1-cells are adjacent, including wraparound neighbors. Each of the four1-cells requires a singleton implicant: C. A,B would include zeros; D is false because the four minterms themselves form an SOP. A compact XOR expression is not a two-level SOP of input literals.

## Q20

**Correct answer:** A, C

Gray v is an ancestor of active u; the tree path v→…→u together with u→v forms a directed cycle, proving A. Directed DFS detects a back edge on every directed cycle, proving C for a complete forest. A black vertex may simply have finished in another branch, with no return path to u, so B is false. A white vertex is undiscovered and cannot already be an ancestor, so D is false. The undirected parent-edge exception does not apply to this directed setting.

## Q21

**Correct answer:** 988

The eight-bit signed displacement11111100 represents−4. Scaling gives−16 bytes; the PC base is1000+4=1004. The target is1004−16=988. Both sign extension and the specified next-instruction PC convention affect the answer.

## Q22

**Correct answer:** A, B, D

A new row did not exist when T1 acquired its row locks and need not conflict with them, so A holds. The newly qualifying row can appear in the repeated predicate query, producing a phantom(B). A suitable predicate/range lock can protect against that insertion(D). C incorrectly equates locking a current result set with locking the predicate's future membership. These statements do not assume an additional snapshot-isolation mechanism beyond the given locking behavior.

## Q23

**Correct answer:** 6

For idempotence, every image element y=f(x) must satisfy f(y)=y. Choose the two image elements in C(3,2)=3 ways and fix each. The remaining element may map to either of them, giving two choices. Total3×2=6. Merely choosing a two-element image does not complete the function; its non-image argument still needs an output.

## Q24

**Correct answer:** B

On the true branch t already equals a+b. On the else branch t equals c+d, so proving equality to a+b there makes the replacement valid on every incoming path: B. A ignores path coverage; C preserves operand values but does not ensure t holds their sum on the else path; D establishes only that t is initialized, not what value it contains. Availability and value equivalence are properties of all feasible predecessor paths.

## Q25

**Correct answer:** 3

No singleton satisfies every factor: P misses(Q+R), Q misses(P+R), and R misses(P+Q). Each two-element subset satisfies all factors, giving covers{P,Q},{P,R},{Q,R}. Thus minimum cardinality is2 and three minimum covers exist. The three-element cover is valid but not minimum; repeated selections do not add new covers.

## Q26

**Correct answer:** A, C

If a tree contains e, deleting it partitions the tree into two components. The alternative u-v path must cross this cut on some edge f whose weight is at most7. Inserting f restores a spanning tree and reduces weight by at least1, proving C and excluding e from any MST(A). The alternative path preserves connectivity between e's endpoints, so e is not a bridge and B is false. Its path edges may themselves have alternatives, so D need not hold. The exchange uses a crossing path edge, not an arbitrary edge chosen without checking the cut.

## Q27

**Correct answer:** 36

Four pairs and total participation of the four B entities imply that each B entity occurs exactly once. Each chooses an A endpoint, and all three A entities must occur. Count onto functions from a four-element labeled set to a three-element labeled set:3^4−3×2^4+3×1^4=81−48+3=36. Many-to-many permits these instances; it does not require every entity to have more than one partner.

## Q28

**Correct answer:** 768

The two successful calls have written768+512=1280 bytes. The remainder is2048−1280=768. A partial return reports progress rather than a requirement to restart from the original buffer; retries must advance the pointer and reduce the requested length.

## Q29

**Correct answer:** C

Sequence43 supersedes41, even though its advertised cost is larger. Sequence42 arrives later but is older and is discarded; the repeated43 carries the same information. The retained cost is9(C). A uses last different arrival instead of freshness, B retains obsolete data, and D adds advertisements that should be replacements rather than path segments.

## Q30

**Correct answer:** A, B, D

Popping Z on empty input accepts epsilon(A). Reading ab pushes X and then removes it, restoring Z; a final empty-input pop accepts(B). The same two-step cycle can repeat, accepting abab(D). On aabb, after the first a the top is X, and there is no move for another a, so C is rejected. Popping Z before input ends strands the remaining input and does not cause acceptance under the stated convention.

## Q31

**Correct answer:** 14

From low to high:1+0 gives c1=0;1+1+0 gives c2=1;0+1+1 gives c3=1;1+0+1 gives c4=1. Thus c4c3c2c1=1110, unsigned14. This asks for the internal carry pattern, not the retained four-bit sum0001 or the full five-bit sum10001.

## Q32

**Correct answer:** B

The entire five-character input matches ID, so maximal munch selects one identifier(B). The shorter initial match IF loses despite keyword priority, which applies only on equal-length matches. A,C split before the longest match ends; D contradicts the permitted digits after the first letter. Token priority and longest-match selection serve different roles.

## Q33

**Correct answer:** 3

For a connected graph, m−n+1=1 independent cycle, consistent with the given unique cycle. Its four cycle edges are not bridges, because each has an alternative path around that cycle. Every other edge lies outside any cycle and is a bridge. Therefore7−4=3. Connectivity alone does not make all edges bridges.

## Q34

**Correct answer:** A, C

Conditional next-address logic can select using a status flag(A), while a microinstruction can drive multiple nonconflicting controls in one cycle(C). Control stores can be read-only, so B is false. Different instructions or conditional paths may traverse different numbers of microinstructions, so D is false. Microprogramming specifies control sequencing; it does not impose equal instruction latency or writable storage.

## Q35

**Correct answer:** 6

The first fork creates two branches. Its child enters the then branch and one fork produces2 descendants reaching the end. Its parent enters the else branch, where two successive forks double the population twice, producing4 descendants. Total2+4=6. Children created inside a chosen branch continue there; they do not reevaluate the earlier if using a newly returned fork value.

## Q36

**Correct answer:** 3

Without the edge-count constraint, s→a→b→t costs3. Among routes with at most two edges, direct s→t costs10, s→a→t costs9, and s→b→t costs6. The permitted optimum is6, exceeding3 by3. Keeping only one unrestricted distance per vertex does not encode a remaining hop budget.

## Q37

**Correct answer:** A, C

Each component is context-free: a PDA matches the first two blocks for L1 or the last two for L2. Union closure proves A. Membership in both forces all three counts equal, proving C. That intersection is the standard non-context-free three-equal-block language and therefore is not regular, disproving B. If the union were regular, intersecting it with the regular language a+ b+ (no c) would be regular. That intersection is {a^n b^n:n≥1}, which is nonregular, so D is false. The regular restriction excludes L2's c-free strings with positive b-count.

## Q38

**Correct answer:** 200

The fragments cover byte intervals[0,399],[600,799],[800,919]. MF=0 on the last fixes the original payload end at919, hence length920. Only bytes400 through599 are absent, a gap of200 bytes. Fragment offsets are multiplied by8 and remain relative to the original datagram.

## Q39

**Correct answer:** 0.5

Normally F is1 only for inputs01 and10. The stuck-high D1 makes F always1, so inputs00 and11 are wrong and the other two remain correct. The fraction is2/4=0.5. A fault may alter a decoder output without making every primary-output observation wrong.

## Q40

**Correct answer:** A

Pumping twice adds k=|v|, with1≤k≤p. Since(p+1)²−p²=2p+1>p, the new length lies strictly between consecutive squares, proving A. Primality is irrelevant and not guaranteed(B); the next square is too far away(C); pumping twice increases rather than decreases length(D). The interval argument covers every legal block length, not one selected decomposition.

## Q41

**Correct answer:** 0

Q can send c because its outgoing channel starts empty. It then receives a, freeing P's channel so P can send b. Q can receive b, and P can receive c; fair scheduling ensures completion. Three total sends and three successful receives leave zero queued messages. P temporarily blocking on its second send does not establish deadlock because Q has a receive available after its first send.

## Q42

**Correct answer:** 8

For one fixed chip byte, A10..A0 are fixed, as are the select bits A15,A14. The three ignored bits A13,A12,A11 can vary freely, producing2³=8 aliases. Chip capacity determines internal address bits, while incomplete external decoding creates repeated mappings.

## Q43

**Correct answer:** 42

All arrangements number6!/(2!2!2!)=90. With AA treated as a block there are5!/(2!2!)=30 arrangements; likewise30 with BB together. With both blocks, there are4!/2!=12. Inclusion–exclusion gives90−30−30+12=42. Each repeated-letter pair is indistinguishable internally; no extra factor2 is used for its block.

## Q44

**Correct answer:** 0

Two-edge paths yield(a,c),(b,c),(c,c). The two paths from a to c collapse into one tuple under set projection. Each resulting pair already belongs to E, so subtracting E leaves zero tuples. Self-loops create length-two paths but do not necessarily create new reachability pairs.

## Q45

**Correct answer:** 9

The first store enters at0 and frees the buffer at3. Subsequent stores enter at3,6,9, respectively. Requested earlier issue times do not bypass a full buffer. The fourth is accepted at9; its later completion at12 is not what was asked.

## Q46

**Correct answer:** 9

Insertion-sort shifts count inversions. Every one of4,5,6 exceeds each later1,2,3, creating3×3=9 inversions. No inversion lies within an ascending block or involves the final7,8. Thus nine shifts occur. Counting key placements would add operations outside the requested metric.

## Q47

**Correct answer:** A, C, D

The Boolean matrix merges all parallel edges into one true entry, losing multiplicities(A,D). Therefore its row sum can undercount outdegree, disproving B. Parallel-edge multiplicity does not change whether a path exists, so collapsing them preserves reachability(C). Multiplicity matters for degrees and edge counts even when it does not matter for reachability.

## Q48

**Correct answer:** 5

Compare each input with the preceding input, taking the initial preceding value as q=0. Inputs110101 yield outputs1,0,1,1,1,1, so five outputs are1. Each output uses the old state; updating q before producing y would incorrectly make every output zero.

## Q49

**Correct answer:** A, B, D

A displaced key's probe chain can cross a deleted slot, so turning it into EMPTY would terminate search prematurely(A). Remembering a tombstone while checking the remaining chain avoids duplicate insertion and allows reuse(B). Searches must continue past tombstones, disproving C and explaining the added unsuccessful-search work in D. Deleted and never-used slots have different historical meanings.

## Q50

**Correct answer:** B

With S empty, the implication in Q is true for every y, so every candidate qualifies. The conjunction in P is false for every y; the infinite domain is nonempty, so its universal statement is false and no candidate qualifies. Thus B; A,C,D each mis-handle one quantifier. Logical implication restricts the required witnesses; conjunction does not implement relational division.

## Q51

**Correct answer:** A, C

Dovetail over all strings and allocate increasing finite steps to both recognizers on each. If a common accepted string exists, both accepting runs eventually finish, proving A,C. B can become stuck forever on an early nonmember before reaching that witness. No finite failure to find a witness proves that none exists, so D is false. A semidecision procedure need only terminate for positive instances.

## Q52

**Correct answer:** 1

For A, COUNT(*)=2,COUNT(v)=1,SUM(v)=2, so both conditions hold. For B, counts2 and0 satisfy the first condition, but SUM(v)=NULL and NULL>1 is UNKNOWN, which HAVING rejects. For C, the counts are equal, failing the first condition. Only group A returns, giving one row. SUM of entirely NULL inputs is NULL, not zero.

## Q53

**Correct answer:** −288

The scaled operand integers are24 and−12. Their full-precision product is−288, stored with eight fractional bits, representing−288/256=−1.125. The requested intermediate integer is−288, not the rescaled four-fractional-bit integer−18. Multiplication adds the numbers of fractional bits.

## Q54

**Correct answer:** A, B, D

p is a valid one-past pointer. Subtracting a within the same array yields3(A), stepping back and dereferencing yields6(B), and comparing with the same one-past pointer is defined(D). Dereferencing p itself accesses no array element and is undefined(C). Formation and comparison of one-past pointers are permitted; dereference is not.

## Q55

**Correct answer:** 3

FIRST(A) contains a and epsilon. The first occurrence of A is followed by b, and the second by c, so FOLLOW(A)={b,c}. Put A→a in column a and A→epsilon in columns b,c. Three cells are occupied; the end marker is not in FOLLOW(A), since neither occurrence ends a sentential suffix capable of vanishing.

## Q56

**Correct answer:** 1

The semaphore serializes both complete read-modify-write operations. Each increments x exactly once, and the third critical section changes no data. Every completed execution ends with x=2, so there is exactly one distinct final value. The requested count of possible results is1, not the result2 itself.

## Q57

**Correct answer:** 2

Use10.8.0.0/22 for the first four /24 blocks and10.8.4.0/23 for the remaining two. One CIDR prefix always contains a power-of-two number of addresses; six /24 blocks have1536 addresses, which is not a power of two. Hence one is impossible and two suffice. A /21 would advertise unwanted addresses10.8.6.0 through10.8.7.255.

## Q58

**Correct answer:** 13

The rule attaches each next bit at the next higher binary position, so the leftmost bit is least significant. The value is1×2⁰+0×2¹+1×2²+1×2³+0×2⁴=13. The ordinary most-significant-bit-first interpretation gives a different number because it would multiply the old value by2 instead.

## Q59

**Correct answer:** 15

TCP has10 free ports and UDP has5 free ports. Their independent namespaces let these capacities be used simultaneously, adding15 mappings. Excess TCP requests cannot consume UDP-only free capacity under the stipulated per-protocol rule. Remote peer differences do not expand either pool because sharing within a protocol is expressly prohibited.

## Q60

**Correct answer:** B

The free instance of R satisfies Q's pending request. Q can then finish and release S, allowing P to finish, establishing B. A incorrectly treats a resource-type cycle as sufficient with multiple instances. C ignores the free resource and D invents an exclusivity rule across different instances. The execution has a completion sequence despite its cycle in the type-level graph.

## Q61

**Correct answer:** 64

The first write to each of the two blocks causes one16-byte write-allocate fetch, totaling32 bytes. The other two writes hit those lines. Flushing writes the two dirty blocks once each, adding32 bytes. Total traffic is64 bytes. One-byte stores do not imply one-byte memory transfers under the given full-block policy.

## Q62

**Correct answer:** 11

Arguments2 through6 are each computed once on a miss, and each such computation invokes two children: five nodes create ten calls. Add the initial invocation to obtain eleven calls total. Equivalently, the distinct arguments are0..6, with four later cache hits. Memoization reduces repeated computation but does not eliminate the invocations that discover hits.

## Q63

**Correct answer:** 29

With no2s, there are2⁴=16 strings. With exactly two2s, they must form one adjacent pair: three positions for that pair and2² assignments to the other positions, giving12. With four2s, only2222 occurs, adding1. Odd numbers of2s cannot have all runs even. Thus a4=16+12+1=29. Counting a pair as an independent block is safe here because the four2 case is handled separately.

## Q64

**Correct answer:** 5

Represent R by a2×2 Boolean matrix, with one row per x. The first condition excludes empty rows; each row has three possible nonempty patterns, giving nine matrices. The second condition requires at least one full row. If neither row is full, each is one of the two singleton rows, giving four excluded matrices. Hence9−4=5. The existential choice of x must cover every y in that same row.

## Q65

**Correct answer:** 1

Subtract the first equation from each of the other two: (t−1)y=1 and(t−1)z=1. For t≠1 these uniquely fix y,z and then x, so the system is consistent with a unique solution. For t=1 both equations demand0=1, making it inconsistent. Exactly one parameter value is inconsistent. The quantity s(t) equals1 whenever a solution exists and does not remove the contradictory exceptional case.

