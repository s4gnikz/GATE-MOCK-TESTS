# Worked Solutions — Mock Test 017

## Q1
**Correct answer:** B

Concept: agreement and past tense. In the neither/nor construction the nearer subject is singular supervisor, giving was. The decision occurred yesterday, requiring announced. B supplies both. A has the wrong second verb and plural agreement; C lacks a finite past-tense second verb; D uses present announce. Check both blanks, not just one.

## Q2
**Correct answer:** 1

Concept: transfer and conservation. Write the balances as 3k and 5k. The transfer is 0.2·5k=k. New balances are 4k and 4k; their quotient is one. The percentage is taken from the second fund, not the combined total.

## Q3
**Correct answer:** A, B

Concept: finite ordering constraints. The orders with exactly two true comparisons are ABC, BCA and CAB. In CAB, B finishes last, so exclude it. ABC permits A first; BCA permits B first. A and B are correct, C is impossible and D is false because feasible orders exist. Three cyclic before-relations cannot all hold.

## Q4
**Correct answer:** D

Concept: orthogonal projections of stacked cubes. The horizontal projection contains four unit squares. In one vertical view, projected heights are the column maxima 2 and 3, giving area five. In the other, row maxima are 3 and 2, also giving five. Sum=4+5+5=14, so D. A is the volume, not the projection sum; B and C undercount the projections. Occluded cubes do not add duplicate projected squares.

## Q5
**Correct answer:** C

Concept: scope of evidence. The report explicitly permits average passenger delay to fall while average car time rises, so C follows. A replaces averages by a claim about every traveller; B asserts an unmeasured effect; D extrapolates one corridor to all corridors. Preserve both the population and the qualifier of a reported result.

## Q6
**Correct answer:** 1488

Concept: circular permutations and inclusion–exclusion. Total circular arrangements are 7!=5040. For a specified set of k adjacent couples, contract each into one block, giving 2ᵏ(7−k)! circular arrangements. Apply inclusion–exclusion over the four couples:

5040−C(4,1)·2·6!+C(4,2)·4·5!−C(4,3)·8·4!+16·3!
=5040−5760+2880−768+96=1488.

Each contracted couple has two internal orders. Reflections remain distinct, so no additional division by two is allowed.

## Q7
**Correct answer:** 47.73

Concept: changing mixture weights. Old combined percentage=100·91/110=82.72727…. New combined percentage=100·35/100=35. Difference=47.72727… percentage points, rounded to 47.73; range 47.725–47.735. A improves from 90% to 95%, B from 10% to 20%, yet the new mix gives much greater weight to B. Averaging the two centre percentages would ignore candidate counts.

## Q8
**Correct answer:** 8

Concept: inverse reflections in unfolding. Undo the diagonal fold to obtain (1,3) and (3,1). Undo the vertical and horizontal folds to independently choose both coordinate signs. Centres are (±1,±3) and (±3,±1), all distinct, for eight. No point lies on a crease, so no reflected copies coincide.

## Q9
**Correct answer:** C

Concept: inconsistent cyclic evidence and an independent constraint. If each cyclic log entry in turn is the sole false one, the possible chronological orders are R,S,P,Q; S,P,Q,R; P,Q,R,S; Q,R,S,P. The reliable R-before-P record retains only R,S,P,Q and Q,R,S,P. Both place S before P, making C necessary. A and B hold only in the second retained order, not the first. D contradicts the reliable record. One cannot discard an arbitrary log entry without checking the other three together.

## Q10
**Correct answer:** 0.6

Concept: conditioning on a stopping event. P(stop at 1)=2/4=1/2. P(stop at 2)=(2/4)(2/3)=1/3. Thus P(stop at 1 | stop by 2)=(1/2)/(1/2+1/3)=3/5=0.6. The second draw is without replacement, so its red probability after a blue is 2/3.

## Q11
**Correct answer:** 3456

Concept: control-store capacity. Address width=2+3+2=7 bits, giving 128 words. Word width=20+7=27 bits, so total=128·27=3456 bits. The next-address field contributes to word width as well as the physical store having an address input.

## Q12
**Correct answer:** A, C

Concept: left factoring versus ambiguity. Both S alternatives start with a, producing the LL(1) conflict in A. Factoring a leaves X alternatives distinguished by b and c, so C is true. The language consists only of ab and ac and has an unambiguous grammar, disproving B. A deterministic parser exists, disproving D. A predictive-table conflict need not mean an ambiguous language.

## Q13
**Correct answer:** A, C, D

Concept: sequential consistency and ordering cycles. Running A entirely before B yields (0,1), so A is possible; reversing their order yields (1,0), so C is possible. Performing both writes before both reads yields (1,1), so D is possible. To obtain (0,0), A's read must precede B's write and B's read must precede A's write. Together with the two program-order edges this would form a strict ordering cycle, impossible in a sequentially consistent total order. Thus B is false. Weak-memory outcomes must not be assumed under the stated stronger model.

## Q14
**Correct answer:** 2

Concept: existential guard plus universal restriction. x=1 has neighbours a,b, both in S; x=2 has only a; x=3 has c, which fails. Hence x=1,2 satisfy the predicate, count two. The existential clause excludes vacuous success for x values with no R tuple.

## Q15
**Correct answer:** C

Concept: poisoned reverse. A advertises infinity back to the neighbour it uses as next hop for D, discouraging B from routing D through A. C is correct. A advertises the selected cost without poisoning; B advertises an unselected direct alternative rather than the specified poisoned route; D is not a distance-to-D advertisement. Poisoning is neighbour-specific.

## Q16
**Correct answer:** C

Concept: postfix translation. Multiplication forms subtree b*c, emitting bc*. Addition emits a, then that subtree, then +, producing abc*+. C is correct. A represents (a+b)*c; B is prefix order; D represents a*(b+c). Tree traversal follows precedence before emitting operators.

## Q17
**Correct answer:** D

Concept: address aliasing. Ignoring A11 makes addresses differing by hexadecimal 800 identical at the chip. 134+800=934, so D. A, B and C change one or more of the connected low eleven bits. A larger decoded window need not imply more physical storage.

## Q18
**Correct answer:** B

Concept: quantifier order. For every x choose y=x, making ∀x∃y true. No single y equals both 0 and 1, so ∃y∀x is false. B gives this pair. A and C incorrectly reject the per-x choice; C and D incorrectly permit one common witness. A witness may depend on the preceding universal variable.

## Q19
**Correct answer:** 2

Concept: rank and consistency. Row three is row one plus row two; the first two rows are independent. Consistency requires 3=1+t, so t=2. Then rank is two in three unknowns, leaving one free parameter and infinitely many solutions. A dependent coefficient row does not guarantee consistency for arbitrary right-hand sides.

## Q20
**Correct answer:** B, D

Concept: stable multi-key sorting. Sorting secondary department first and then stably sorting primary name preserves department order among equal names, so B works. A gives department primary priority. C can scramble equal-name records' department order. D compares the desired tuple directly and works regardless of how equal complete tuples are ordered. The final stable pass sets the primary key.

## Q21
**Correct answer:** A, B, D

Concept: IPv4 fragment payload units. Subtract the 20-byte header: payloads are 512,520,532,536. Dividing by eight gives integers for A, B and D; 532 leaves remainder four, so C fails. MF=1 means more fragments follow, so this is not the final-payload exception. Alignment applies to payload length, not total length.

## Q22
**Correct answer:** -0.25

Concept: fixed-point scaling. Raw signed integers are −56 and 52, representing −3.5 and 3.25. Their sum is −4, raw FC, scaled by 1/16 to −0.25. The raw hex result alone is not the represented real value.

## Q23
**Correct answer:** 0.25

Concept: repeated rounding at ties. Near one, three-bit significands represent 1.00₂=1 and 1.01₂=1.25. The exact 1.125 is midway; ties-to-even selects 1.00₂. The second addition encounters the same tie and again stores one. Exact sum=1.25; error=1.25−1=0.25. Rounding after each operation differs from rounding only the final exact sum.

## Q24
**Correct answer:** D

Concept: negating the pumping condition. The regular-language statement has order ∃p ∀w ∃split ∀i with membership preserved. Negation gives ∀p ∃w ∀split ∃i with membership failing, exactly D. A only exhibits one bad split; B chooses the split and even requires failure at i=1, which reproduces w; C uses the wrong initial quantifier and still allows a bad chosen split. The adversary chooses the decomposition.

## Q25
**Correct answer:** A, B

Concept: limits on dense subsets. Since |f(x)|=|x|, f tends to zero at zero and f(0)=0, proving A. For nonzero x, the difference quotient f(x)/x is 1 on rationals and −1 on irrationals; rational and irrational inputs occur arbitrarily close to zero, so this quotient has no limit and no derivative exists. B is true and D false. At one the rational and irrational limits are 1 and −1, so C is false. Continuity of the function does not force its difference quotient to converge.

## Q26
**Correct answer:** 12

Concept: pointer and pointee increments. `*p++` means `*(p++)`: x receives 2 and p advances to a[1]. `++*p` increments that element from 4 to 5 and gives y=5. The sum is 2+5+5=12. Incrementing a pointer and incrementing the pointed value are different operations.

## Q27
**Correct answer:** A, B

Concept: NULL and anti-joins. For x=1 or 3, NOT IN encounters UNKNOWN from comparison with NULL; for x=2 it is false. WHERE retains none, so A holds. NOT EXISTS checks for a true equality match; only x=2 has one, giving 1,3 and making B true. COUNT(y) ignores NULL and returns one, so C is false. NULL=NULL is UNKNOWN, not TRUE, so D is false. NOT IN and NOT EXISTS are not interchangeable with nullable subqueries.

## Q28
**Correct answer:** -1

Concept: recurrence periodicity. Values starting at n=0 are 0,1,1,0,−1,−1,0,1. The pair (0,1) repeats at positions 6,7, so the recurrence repeats with period six. 2027 mod 6=5, giving −1. Repeated evaluation is unnecessary once the state pair recurs.

## Q29
**Correct answer:** 5

Concept: conditional sample spaces. The eligible equally likely outcomes are (4,3),(5,2),(6,1). Their X values average to (4+5+6)/3=5. Conditioning on the sum alone would instead give 3.5.

## Q30
**Correct answer:** 9

Concept: symmetric transitive relations. If an element x is related to any y, symmetry gives yRx and transitivity gives xRx. Therefore any element missing its self-pair has no incident pairs at all. Nonreflexivity forces at least one such isolated element; at most three active elements remain, allowing at most 3²=9 pairs. The complete relation on three elements, with the fourth isolated, attains nine. Nonreflexive does not mean every self-pair is absent.

## Q31
**Correct answer:** 6

Concept: cascading referential actions. Delete the parent, its two children, and their three grandchildren. Total=1+2+3=6. A cascade follows both declared levels rather than stopping after direct references.

## Q32
**Correct answer:** A, B

Concept: resource-allocation cycles. Deadlock requires a directed cycle, making A true and its contrapositive B true. With multiple instances a cycle need not be sufficient: another holder may release an instance and enable progress, so C fails. Acyclic waiting may include unfinished processes, disproving D. Distinguish a necessary condition from a sufficient one.

## Q33
**Correct answer:** C

Concept: dovetailing recognizers. Exactly one of L and its complement contains w, so its recognizer eventually accepts. Interleaving steps ensures that acceptance is reached even if the other machine loops; C gives the appropriate answer. A can wait forever on M for a nonmember. B mislabels complement acceptance; D imposes an unjustified time bound. A recognizer need not halt when its answer would be negative.

## Q34
**Correct answer:** 1040

Concept: lower-bound-adjusted indexing. Each row has four elements. Element offset=(4−2)·4+(1−(−1))=10. Byte address=1000+4·10=1040. Both index origins must be subtracted before computing the offset.

## Q35
**Correct answer:** D

Concept: preserving probe-chain semantics. A tombstone can be remembered as a potential insertion location, but searching must continue for an existing equal key. D does this. A creates a duplicate; B and C confuse a formerly occupied slot with a never-used stopping slot. Deletion must not break searches for displaced entries.

## Q36
**Correct answer:** 15

Concept: aliasing in linked structures. Reversal makes 4→3→2→1→null. B still points to node 9, whose next pointer is still node 3; node 3's next has changed to 2. Thus B now visits 9,3,2,1, sum 15. The nodes are shared objects, not independent copies of their labels.

## Q37
**Correct answer:** B, C

Concept: Boolean sensitivity. F(0,y,z)=yz; F(1,y,z)=y+z. Their XOR is one exactly when y and z differ, giving y XOR z (B). The substituted expression has no x (C). A fails at y=z=1 because the difference is zero but OR is one; D fails at y=1,z=0 because the difference is one but AND is zero. Boolean difference uses XOR, not ordinary subtraction.

## Q38
**Correct answer:** 7

Concept: product states and distinguishability. Track a-count zero or one, together with length modulo three: six states. A second a enters one permanent sink. All seven are reachable. Different residues with the same count can be separated by a suitable suffix: only b symbols for count one, or one a plus enough bs for count zero. A zero-count state and a one-count state are separated by a suffix containing exactly one a that completes a multiple-of-three length for the zero-count state; it sends the other to the sink. Every nonsink state has an accepting continuation. Thus no states merge and seven is minimal.

## Q39
**Correct answer:** 16

Concept: isolated ON minterms. F is one only for 0101,0110,1001,1010. Changing any single bit breaks one of the two XOR conditions, so no ON minterm has an ON neighbour. Hence no product may omit a variable without including an OFF input. Four products of four literals are necessary and sufficient, total 16. An XOR-based multilevel expression can be short while its two-level SOP is long.

## Q40
**Correct answer:** C

Concept: sparse expensive iterations. The inner loop runs only at i=1,2,4,...,2^m where 2^m≤n<2^(m+1). Its total work is 1+2+...+2^m=2^(m+1)−1, between n and 2n. The outer loop also costs Θ(n), so C. A counts only trigger events, B charges an average logarithmic inner cost to every iteration, and D treats the expensive loop as running for every i. Sum actual executed lengths rather than multiplying syntactic bounds.

## Q41
**Correct answer:** A, B

Concept: grammar invariants and ambiguity. Each nonempty production adds one a and one b, proving A. For abab, the root production aSbS can pair its initial a with the second symbol b (empty first S, second S→ab), or with the final b (first S→ba, second S→ε). These are different parse trees, proving B. The word ba is generated, disproving C. In fact the language is all equal-count words: split any nonempty such word at the first return of its count balance to zero and induct on the two balanced parts. Intersecting with regular a*b* gives {aⁿbⁿ}, which is nonregular; therefore D is false. Equal total counts do not impose a prefix-balance condition.

## Q42
**Correct answer:** A, D

Concept: cube union and don't-care expansion. The cubes cover respectively {0000,0001,0100,0101} and {0000,0001,1000,1001}. Their union has six minterms, while −−0− has eight; the missing ones are 1100 and 1101. Hence B is false. These are explicitly don't-cares, so the larger cube contains no OFF minterm: C is false and D true. Ordinary pairwise Quine–McCluskey combination needs matching dash positions and one remaining bit difference; A correctly notes that these two original cubes do not meet that direct rule. A valid larger implicant can still be reached by using additional don't-care cubes.

## Q43
**Correct answer:** 8

Concept: bounded-stack permutations. Each valid push/pop history determines a unique permutation because inputs are pushed in a fixed order. Conversely the desired next output determines which unpushed inputs must be pushed before its pop, making the history unique. A nonempty push/pop path of maximum height two decomposes into excursions of the form push, k repetitions of push-pop at height one, pop. Such an excursion uses any positive number of pushes and has one shape for each number. Histories with four pushes therefore correspond to ordered compositions of four, counted by 2³=8. Counting all Catalan paths would allow stacks of height three or four.

## Q44
**Correct answer:** 1.3333

Concept: overlapping bottlenecks. Original compute time per iteration=8/2=4 ns; memory time=24/8=3 ns. With perfect overlap, effective time is max(4,3)=4. After optimization it is max(2,3)=3 ns. Throughput ratio=(1/3)/(1/4)=4/3, rounded to 1.3333; range 1.33325–1.33335. Halving arithmetic work does not double throughput after memory becomes limiting.

## Q45
**Correct answer:** A, C

Concept: keys and lossless decomposition. C cannot be derived, so every key includes C. Either A or B then supplies the other; C supplies D. Exactly AC and BC are minimal keys (A). Determinants A,B,C are not superkeys of R, so B is false. Split off AB using A→B, leaving ACD; split that using C→D into CD and AC. Both binary splits are lossless, and AB preserves A→B and B→A while CD preserves C→D, so C is true. AB and CD alone lose the association between A and C: two original rows with distinct A and C values can recombine into four rows, so D is false. Dependency preservation alone does not prove losslessness.

## Q46
**Correct answer:** 31

Concept: nested routing prefixes. /11 contains 2^(16−11)=32 /16 blocks, with second octets 96–127. Exactly one, 10.100.0.0/16, has the more-specific D route. The remaining 31 use C, which overrides the broader A and B routes. Do not subtract all space covered by a less-specific route.

## Q47
**Correct answer:** 6

Concept: block boundary accounting. Starting at slot 7 leaves three records in the first block; the remaining twenty fill two more blocks. Data reads=3. Add the three distinct index reads for a total of six. Dividing 23 by ten and rounding happens to give three here, but the starting offset must still be checked: generally use ceil((offset+count)/capacity).

## Q48
**Correct answer:** B

Concept: lexical versus dynamic scope. S is declared inside P, so its x is P's x, regardless of the R→S call chain. The two calls return 11 and 12, summing to 23 (B). A omits one increment's effect; C would increment Q's x instead, giving 21+22; D simply uses Q's unchanged value twice. Static links follow declarations, not the immediate caller.

## Q49
**Correct answer:** A, C

Concept: external connection identity and checksum coverage. With identical public IP and remote endpoint, two simultaneous translated TCP connections need distinct external source ports (A). Distinct remote endpoints can disambiguate a reused external port if the NAT's mapping and lookup support that policy (C). TCP's checksum includes a pseudo-header containing IP addresses, so B is false. Two internal hosts may share a local source port, so D is false. A port is only one component of a connection identifier.

## Q50
**Correct answer:** 4

Concept: tree diameter endpoints. The leaves are D,E,G,H. A longest path in an unweighted tree has leaf endpoints. D–E and G–H each have distance two; any pair with one endpoint in {D,E} and the other in {G,H} has distance five, through B,A,C,F. Thus the diameter is five and exactly 2·2=4 unordered endpoint pairs attain it. Reversing endpoints does not create another pair.

## Q51
**Correct answer:** A, B

Concept: Huffman tie choices. Merge the two ones to make 2; then merge any two of the three weight-two nodes to make 4. Remaining weights are 2,4,4, one four being the original symbol. If the next merge uses the other four, the original four is a child of the final root and has length one (A). If it uses the original four, that symbol has length two (B). Its first possible merge is this penultimate merge, so depths three or four cannot occur; C and D fail. Equal-weight choices can change individual lengths while preserving optimal weighted cost.

## Q52
**Correct answer:** B, C

Concept: induction-variable strength reduction. At iteration i=s+r, B's running address is base+4s+4r=base+4i; retaining i preserves its other uses. The now-unused address multiplication can be removed, so C also holds. A starts at the wrong element unless s=0. D corrupts statements that still depend on i. A derived induction variable need not replace the original variable everywhere.

## Q53
**Correct answer:** 3

Concept: outstanding data versus two window limits. First allowance=min(10,12)−8=2, making flight size ten. ACK of five leaves five outstanding. The new limit is min(8,6)=6, so only one more segment can be sent. Total new segments=2+1=3. An ACK frees space relative to both the remaining flight size and the updated limiting window.

## Q54
**Correct answer:** 54

Concept: rank-one eigenspaces. For any x in the three-dimensional kernel of vᵀ, Ax=x. Also Au=u+u(vᵀu)=0. Since vᵀu≠0, u is outside that kernel, completing a basis. Thus A has eigenvalues 1,1,1,0; A+2I has 3,3,3,2. Determinant=3³·2=54. Adding 2I shifts every eigenvalue, not the determinant by two.

## Q55
**Correct answer:** A, C, D

Concept: mean value theorem and continuity of f′. On [0,1/2] the secant slope is 2/(1/2)=4, proving A. On [1/2,1] it is (1−2)/(1/2)=−2, proving C and disproving B. The derivative is continuous and takes both signs, so it equals zero between those two interior points, proving D. The whole-interval secant slope alone would hide both the rise and the fall.

## Q56
**Correct answer:** 10

Concept: queue order at a quantum boundary. Timeline: P 0–2; Q 2–4; R 4–5; P 5–7; Q 7–8; P 8–9. At time 2 the queue is Q,R,P by the specified arrival rule. Completion times are 9,8,5. Waiting times C−arrival−burst are 4,4,2, total ten. A boundary convention can change later queue order and must not be assumed silently.

## Q57
**Correct answer:** A, C

Concept: nondeterministic midpoint matching. To consume abba and empty its pushed portion, push and matching lengths must both be two, proving A. The matched suffix ba is the reversal of prefix ab. A guess after one symbol cannot ignore a mismatch or extra input, so B is false. For abab the only possible balanced lengths are two and two, but suffix ab is not the reversal ba, so C is true. Nondeterministic acceptance needs one successful branch; incorrect guesses do not invalidate another accepting branch, so D fails.

## Q58
**Correct answer:** 9

Concept: B+ splitting and root growth. Leaf splits occur on inserting 4,6,8,10,12, leaving six leaves [1,2],[3,4],[5,6],[7,8],[9,10],[11,12]. At insertion 10 the root first reaches five children and splits into two internal nodes with two and three children, under a new root. Insertion 12 increases the right internal node to four children without overflowing it. Total=6 leaves+2 internal children+1 root=9. A leaf split does not always create another root level.

## Q59
**Correct answer:** 178

Concept: matrix-chain optimization. The five parenthesizations have costs:

- ((AB)C)D: 100+80+120=300.
- (A(BC))D: 160+400+120=680.
- (AB)(CD): 100+48+30=178.
- A((BC)D): 160+240+150=550.
- A(B(CD)): 48+60+150=258.

Minimum is 178. Multiplication dimensions change with each intermediate result; multiplying the locally cheapest pair is not a general optimality proof.

## Q60
**Correct answer:** 3

Concept: indexing conflicts and associativity. Mapping I puts all three even block numbers in set zero. Cycling through three blocks in a two-way LRU set yields six misses. Mapping II puts 0 and 4 in set zero, 2 in set one. Each fits after its first load, giving three misses. Difference=6−3=3. Total cache capacity alone does not prevent conflict misses.

## Q61
**Correct answer:** 133

Concept: stolen-cycle accounting. Every full four-cycle group completes three CPU instructions and one DMA transfer. After 33 groups (132 cycles), the CPU has completed 99 instructions and DMA 33 transfers, so DMA is still active. Cycle 133 is not stolen and completes instruction 100. Treating 100 CPU cycles as elapsed cycles ignores stalls; assuming all 64 transfers finish first ignores overlap.

## Q62
**Correct answer:** 0.8

Concept: Bayes with a biased reporting rule. Joint probabilities of prize A and opening B, prize B and opening B, prize C and opening B are respectively 1/12,0,1/3. Condition on opening B: P(prize C)=(1/3)/(1/12+1/3)=4/5=0.8. The host's selection rule affects the evidence and cannot be replaced by an assumed symmetric rule.

## Q63
**Correct answer:** 6

Concept: automorphisms of a divisor lattice. Since 30=2·3·5 is square-free, divisors correspond to subsets of three primes, ordered by inclusion. An order-preserving bijection fixes the least element and permutes its three immediate successors 2,3,5. Every larger element is determined by the set of atoms below it, so this permutation determines the entire map. All 3!=6 atom permutations extend to valid maps. Arbitrarily permuting all eight divisors does not preserve the order.

## Q64
**Correct answer:** 48

Concept: online SCAN arrivals. The head reaches 99 at time 49. At time 30 it is already at 80, so the new track-70 request waits for reversal. Returning from 99 to 70 takes 29 ms, giving service time 78. Waiting since arrival is 78−30=48 ms. LOOK would reverse differently; the stated physical-endpoint rule must be used.

## Q65
**Correct answer:** B, D

Concept: dead values versus observable effects. The first stored value is overwritten before print, but evaluating 1/x may raise an observable exception (B). Thus A is false when x=0. C leaves print dependent on an unrelated old value and also removes the possible exception. If x is known nonzero, the division has no observable effect under the stated exact-arithmetic model, and the second assignment fixes the printed value to two; D is correct. Dead-store elimination does not automatically justify deleting a potentially trapping right-hand side.



