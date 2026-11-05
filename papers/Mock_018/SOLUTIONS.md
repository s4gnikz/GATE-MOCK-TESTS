# Worked Solutions — Mock Test 018

## Q1
**Correct answer:** A

Concept: vocabulary in context. Reversing a tentative preference is wavering, so A fits. B means working together, C means approaching agreement and D means vanishing; none captures indecision. The sentence's second clause supplies the intended meaning.

## Q2
**Correct answer:** 10

Concept: powers dividing a factorial. Multiples of two contribute six factors, multiples of four contribute three additional factors, and the multiple of eight contributes one more. Thus the exponent is floor(12/2)+floor(12/4)+floor(12/8)=6+3+1=10. Counting just the even factors misses their extra powers of two.

## Q3
**Correct answer:** B

Concept: induction versus proof. The observation establishes correctness only on the tested executions, which is B. A extrapolates to all programs, C invents universal failure outside the suite, and D denies the possibility of a revealing new test. Finite testing alone is not a universal correctness proof.

## Q4
**Correct answer:** 4

Concept: tiling blocks. Three vertical dominoes occupy three columns. The remaining two dominoes must both be horizontal, stacked across the same pair of adjacent columns. Treat this width-two pair as one block among three width-one vertical blocks. It has four possible positions, giving four tilings. Two independently placed horizontal dominoes would leave uncovered cells.

## Q5
**Correct answer:** 42

Concept: constant second differences. Rearranging gives a(n+2)−a(n+1)=a(n+1)−a(n)+2. Differences start at four and then are 6,8,10,12. Thus a6=2+4+6+8+10+12=42. There are five increments between the first and sixth terms.

## Q6
**Correct answer:** 256

Concept: constrained optimization over integers. The volume is V(x)=x(20−2x)(12−2x). Positive dimensions restrict x to 1,2,3,4,5. Corresponding volumes are 180,256,252,192,100; the maximum is 256 at x=2. The maximizing integer must be checked rather than reporting an unconstrained stationary point.

## Q7
**Correct answer:** A, B

Concept: implications and contrapositives. Interviewed implies both forms, and interviewed implies decision. Their contrapositives give A and B. C reverses the first implication; D reverses the second. Neither converse is supplied. “Only applicants who” specifies a necessary condition, not a guarantee of interview.

## Q8
**Correct answer:** 38.89

Concept: compound revenue factors. Let the sticker-price multiplier be r. Revenue relative to last month is 0.8·0.9·r. Setting this to one gives r=1/0.72=25/18. Increase=100(r−1)=38.888…%, rounded to 38.89; accepted range 38.885–38.895. Adding the two losses as 30% would use the wrong compound factor.

## Q9
**Correct answer:** A, C

Concept: exhaustive constraint satisfaction. For prize pairs AB,AC,AD,BC,BD,CD, the numbers of true labels are respectively 2,4,2,3,1,1. Thus only AB and AD are feasible. Both include A and exclude C, making A and C necessary. B fails for AD; D fails for AD as well. Necessary conclusions must hold in every feasible placement.

## Q10
**Correct answer:** C

Concept: periodic transformations. The orbit is (1,0)→(1,1)→(0,1)→(0,0)→(1,0). Since 2027 leaves remainder three on division by four, the answer is (0,0), C. A, B and D correspond to remainders one, two and zero. The translation term is part of each application.

## Q11
**Correct answer:** 0

Concept: relational invariants at joins. The first branch ends with x=y=2, the second with x=y=3. In both cases x−y=0. Knowing that neither variable is individually constant does not imply their difference is unknown; the equality relation survives both paths.

## Q12
**Correct answer:** A, C

Concept: divide-and-conquer tree sums. Level j has 3ʲ calls of size n/2ʲ, costing Θ(n²(3/4)ʲ). Summing this decreasing geometric series gives Θ(n²), A; B incorrectly adds a logarithmic factor. The depth is log₂n and the number of leaves 3^(log₂n)=n^(log₂3), C. D confuses logarithmic depth with n levels.

## Q13
**Correct answer:** B, D

Concept: true versus name dependences. Renaming separates an earlier reader from a later writer using the same architectural name (WAR), and separates different writers (WAW), so B and D. A's consumer still needs its producer's actual value, and C depends on the branch outcome, so neither is removed merely by register names. Renaming is not value prediction.

## Q14
**Correct answer:** A

Concept: preorder subtree ranges. A first lists root 40, then its valid left subtree 20,10,30, then its valid right subtree 60,50,70. B enters the right subtree at 50 and later returns to 10<40. C similarly puts 20<40 after entering the right subtree. D visits 30 in 20's right subtree then incorrectly places 10 there. Bounds from all ancestors matter.

## Q15
**Correct answer:** 17

Concept: indirect effective addressing. R1+8=108; its memory content is the effective address 200. Loading M[200] yields 17. Reporting 200 would omit the second dereference explicitly required by the instruction.

## Q16
**Correct answer:** 2

Concept: local sensitivity of majority. Initial output is one. Flipping either of the two one bits leaves only one one and changes output to zero. Flipping the zero gives 111 and retains one. Hence two flips change output. Different input positions need not have equal influence at a particular state.

## Q17
**Correct answer:** 5

Concept: Gaussian elimination and LU. Eliminate the lower entry using multiplier 6/2=3, giving L21=3. The remaining lower-right pivot is 5−3·1=2, so U22=2. Sum=5. The multiplier belongs to L, while the updated pivot belongs to U.

## Q18
**Correct answer:** C

Concept: recoverable schedules. T2 depends on T1's uncommitted value but commits first; when T1 aborts, T2 can no longer be rolled back as an uncommitted dependent transaction. This violates recoverability, C. A reverses the required commit order; B and D deny the read dependency. Committing early does not make a dirty read safe.

## Q19
**Correct answer:** 0.3333

Concept: symmetry under substitution. Let I=∫₀¹f(x)dx. Substitution u=1−x gives ∫₀¹f(1−x)dx=I. Integrating the given identity gives 2I=1/3+1/3, so I=1/3. Rounded answer 0.3333; range 0.33325–0.33335. The identity does not require f itself to be symmetric.

## Q20
**Correct answer:** 80

Concept: counting heap labelings. The maximum key is forced at the root. Choose three of the other six keys for the left subtree in C(6,3)=20 ways. Each three-node subtree has its own maximum forced at its root and its remaining two keys freely ordered, giving two assignments each. Total=20·2·2=80. A heap constrains ancestors, not arbitrary left-versus-right key order.

## Q21
**Correct answer:** B, D

Concept: backward liveness. After `x=d`, only y is needed by return. Immediately before that assignment, d is needed as its source and y remains needed, so B and D are live after statement two. The old x is overwritten before any further use, making A false; c has already had its last use, making C false. Syntactic liveness precedes any deletion of the dead assignment.

## Q22
**Correct answer:** 2

Concept: BFS queue timing. Processing s enqueues a,b. Dequeue a, leaving [b]; enqueue c, giving [b,c]. Just before enqueuing d, the queue therefore has two vertices. Vertices already processed are not still queued.

## Q23
**Correct answer:** 820

Concept: moments of an affine transformation. E[Z]=3·10−2=28 and Var(Z)=3²·4=36. Since E[Z²]=Var(Z)+(E[Z])², the answer is 36+784=820. Variance alone is not the second raw moment.

## Q24
**Correct answer:** A, C

Concept: stream EOF versus datagram length. TCP zero after draining input denotes orderly incoming EOF, so A. A valid UDP datagram can have empty payload and yield zero without stream-style EOF, so C. TCP is a byte stream: B and D incorrectly assert preservation of application message/write boundaries. Interpret a return value with the socket's transport semantics.

## Q25
**Correct answer:** D

Concept: conflict graph. w1(X) precedes r2(X), producing T1→T2. w2(Y) precedes r1(Y), producing T2→T1. The cycle precludes conflict serializability, D. A and B each ignore one edge; C is false because read/write pairs on the same item conflict. Commit order cannot remove an existing precedence cycle.

## Q26
**Correct answer:** 0

Concept: multiplicative group orders. Each of 5,7,11 squares to 1 modulo 12, so each has order two; 1 has order one. A generator of this four-element group would need order four. None exists, giving zero. Having four elements does not make a group cyclic.

## Q27
**Correct answer:** 25

Concept: buddy rounding and internal fragmentation. Requests receive blocks of 16,32,8 KiB. Wasted space inside them is (16−9)+(32−17)+(8−5)=7+15+3=25 KiB. The remaining free eight KiB is not internal fragmentation inside allocated blocks.

## Q28
**Correct answer:** C

Concept: negative DNS caching. The cached absence result can remain valid at the resolver until its TTL expires, C. A falsely prohibits later creation, B confuses transport with record updates, and D incorrectly makes the lifetime infinite. An authoritative change does not instantly invalidate every cached answer.

## Q29
**Correct answer:** 3

Concept: bipartite matching and vertex covers. Removing a perfect matching from K3,3 leaves a six-cycle. Its three disjoint alternate edges require at least three cover vertices. Either original bipartition side covers every remaining edge with three vertices. Thus the minimum is three. A matching supplies a lower bound even after other edges are deleted.

## Q30
**Correct answer:** A, B, D

Concept: CFL closure and exact intersection. Each language is context-free; union and concatenation preserve this property, giving A and D. A word in both has the same a-count n but b-count simultaneously n and 2n, forcing n=0; B holds. C is the false general intersection-closure claim: for example {aⁿbⁿcᵐ} and {aᵐbⁿcⁿ} are CFLs whose intersection {aⁿbⁿcⁿ} is not. A particular regular intersection does not establish a general theorem.

## Q31
**Correct answer:** 1058

Concept: encapsulation accounting. Total=1000 application+20 TCP+20 IP+14 Ethernet header+4 FCS=1058 bytes. The expressly excluded preamble and inter-frame gap are not added. Headers of successive layers accumulate.

## Q32
**Correct answer:** B, C

Concept: MST uniqueness conditions. Pairwise distinct weights guarantee a unique MST, B. A graph already a tree offers only its own spanning tree, C, even if all weights are equal; this disproves A. A bridge must be included in every spanning tree regardless of weight, disproving D. Distinct weights are sufficient, not necessary, for uniqueness.

## Q33
**Correct answer:** B

Concept: TLB address-space separation. Without tags, a matching virtual page can retrieve the previous process's frame. Flushing the relevant entries prevents this, B. A ignores different page tables; C destroys data unnecessarily; D denies the point of a cached translation, since a hit does not necessarily walk the page table. A virtual page number is meaningful within an address space.

## Q34
**Correct answer:** 3

Concept: simultaneous next-state evaluation. States follow 10→11→00→01→10→11. After five edges the value is binary 11, or three. Using updated Q0 in the expression for Q1 would incorrectly model a synchronous update as sequential assignment.

## Q35
**Correct answer:** B

Concept: pumping with a common multiple. The pumped a-count is p+(i−1)k. Set this equal to the fixed b-count p+p!, yielding i=1+p!/k. This is a positive integer because every k≤p divides p!, making B correct for every valid split. A does not generally solve the equation; C removes rather than adds the required amount and can be negative; D only adds k², not necessarily p!. The factorial makes one chosen witness handle all permitted pump lengths.

## Q36
**Correct answer:** B, C

Concept: path-sensitive available values. On the true path t is recomputed after a changes; on the false path a is unchanged and t=p=a+b. Thus t equals the current expression on both paths, making B and C true. A fails on the true path; D fails on the false path. A value can be available via a join even when an earlier temporary has been invalidated on one branch.

## Q37
**Correct answer:** 5

Concept: maximal munch and priority. Tokens are identifier ifx, integer 12, keyword if, plus, integer 007. Longest match takes ifx rather than splitting keyword if and identifier x. The later exact if tie goes to the keyword. Leading zeroes do not split the integer under the given regex, so total five.

## Q38
**Correct answer:** D

Concept: signed comparison after overflow. A represents −128 and B represents one. Exact difference −129 wraps to 127=0x7F, giving N=0 and V=1. Signed less-than is N XOR V=1. Thus D. A wrongly uses the unrepresentable exact difference's sign as the stored sign; B misses overflow; C gives the wrong stored sign and comparison. A subtraction's sign alone is insufficient when it overflows.

## Q39
**Correct answer:** A, C

Concept: recognizable reachability and reduction. Simulation accepts upon entering PRINT, establishing A. Simulating an arbitrary machine/input and entering PRINT iff it halts reduces halting to this property, establishing C. No universal fixed simulation bound exists, so B is false. If the complement also had a recognizer, dovetailing both would decide the property, contradicting C; D is false. A finite machine description does not bound its halting time.

## Q40
**Correct answer:** 3

Concept: primitive cyclic arrangements. There are C(6,3)=20 labelled words. A smaller least period divides six. Period one cannot give three ones; period three repeats twice and has an even total number of ones. Period two gives only 010101 and 101010. Excluding these leaves 18 words, each in an orbit of six distinct rotations. Therefore 18/6=3 classes. Division by six is valid only after removing shorter-period words.

## Q41
**Correct answer:** 1

Concept: field-wise versus joint encoding. Separate fields need ceil(log₂9)+ceil(log₂5)+8=4+3+8=15 bits. Legal joint choices number 9·5·2⁸=11520, between 2¹³ and 2¹⁴, requiring 14 bits. Excess=1. Independent field padding can waste combinations that a joint code could use.

## Q42
**Correct answer:** 6

Concept: DFA memory and minimization. Use one start state, two states with no equal pair yet and last bit 0/1, two accepting states with exactly one equal pair and last bit 0/1, and one sink after a second equality. All six are reachable. Accepting states differ on suffix 0; zero-equality states also differ on suffix 0. Start differs from each zero-equality state by repeating that state's last bit once. Accepting versus nonaccepting states differ on ε. The sink differs from every other nonaccepting state because each has an accepting continuation. Therefore no states merge. An equality count alone loses the previous-bit information.

## Q43
**Correct answer:** 5

Concept: sparse double-indirect allocation. Each pointer block holds 1024 pointers. Direct blocks cover 0–7; single-indirect covers 8–1031. Block 1032 is double-indirect offset zero, requiring a double-indirect root, one child pointer block and one data block. Block 2061 has double-indirect offset 1029=1024+5, requiring a different child pointer block and its data block but reusing the root. Total=3+2=5. Unwritten intervening file holes consume no blocks.

## Q44
**Correct answer:** 3

Concept: head-of-line blocking. Under FIFO, A blocks B while O1 is unavailable in slots 1–2. I1 wins O1 in slot 3 and sends A. B then uses O2 in slot 4, concurrently with C on O1. With separate output queues, B is eligible immediately and leaves in slot 1. Departure-slot difference=4−1=3. An idle output alone does not imply that a FIFO input exposes a packet for it.

## Q45
**Correct answer:** 4

Concept: ambiguity and semantic values. The five parenthesizations yield 13 for ((1+2)*3)+4, 11 for (1+(2*3))+4, 21 for (1+2)*(3+4), 11 for 1+((2*3)+4), and 15 for 1+(2*(3+4)). Distinct values are {11,13,15,21}, count four. Different parse trees need not produce different numerical values.

## Q46
**Correct answer:** A, D

Concept: complete address decoding. First interval has high bits A15A14=00, so A is correct. Second interval has A15A14A13=010, giving D. B would also enable the chip over 0x6000–0x7FFF, creating unwanted aliases. Mapped capacity is 16+8=24 KiB of 64 KiB, leaving 40 KiB, so C is false. Chip offset bits and chip-selection bits serve different roles.

## Q47
**Correct answer:** A, C

Concept: nullable productions and FOLLOW propagation. FOLLOW(S)={$}; B ends S's production and occurs before c in its own recursive production, so FOLLOW(B)={c,$}, C. A is followed by nullable B, whose nonempty FIRST is {b}; hence FOLLOW(A)={b,$}, not c, disproving B. A's alternatives use lookahead a versus {b,$}; B's use b versus {c,$}, with no conflicts, proving A. D chooses ε on the lookahead reserved for A→aA and is false.

## Q48
**Correct answer:** 9

Concept: CRC undetected two-bit errors. An error is xʲ(xᵏ+1), k the positive separation. Since G has constant term one, xʲ is coprime to it. Modulo G, successive nonzero powers of x have period seven: 1,x,x²,x+1,x²+x,x²+x+1,x²+1, then 1. Thus k must be a multiple of seven. Available separations are 7 and 14, giving 15−7=8 and 15−14=1 pairs, total nine. Two-bit errors are not necessarily detected for every frame length.

## Q49
**Correct answer:** 19

Concept: separated repeated parts. If there are k twos, there are 8−2k ones. Their gaps provide 9−2k possible positions for at most one two each. Counts for k=0,1,2,3 are C(9,0)=1, C(7,1)=7, C(5,2)=10, C(3,3)=1; k=4 is impossible without adjacency. Total=19. Equivalently use a_n=a_(n−1)+a_(n−3) with a0=1,a1=1,a2=2.

## Q50
**Correct answer:** 3

Concept: implication propagation and model counting. The first clause forces at least one of p,q. Each implies r, so r must be true; then r implies s and s implies t. The only freedom is (p,q)=(1,0),(0,1),(1,1), giving three assignments. Counting each implication independently would overcount inconsistent combinations.

## Q51
**Correct answer:** 240

Concept: ER cardinality as a surjective assignment. Five employees distributed among four nonempty departments must have group sizes 2,1,1,1. Choose the pair of employees in C(5,2)=10 ways, its department in four ways, then biject the remaining employees to the three departments in 3!=6 ways. Total=10·4·6=240. Relationship instances distinguish employee and department identities.

## Q52
**Correct answer:** B, D

Concept: negative edges and premature finalization. True best route s→b→a→t costs 5−4+3=4, so B is true and A false. Other routes cost 5 and 6. The graph is acyclic, so C is false. Dijkstra first finalizes a at two, sets t to five, and then chooses t before b at the specified tie, returning five, so D is true. The negative edge permits later improvement of an already-finalized distance.

## Q53
**Correct answer:** 7

Concept: walk counts in adjacency powers. A length-three closed walk at vertex 1 either takes its self-loop three times (one choice), or follows 1→2→3→1 with 2·3·1=6 parallel-edge choices. Total seven, also (A³)11. Parallel edges multiply walk counts even when the vertex sequence is identical.

## Q54
**Correct answer:** 26

Concept: pointer-to-pointer updates. Initially *p points to x; the first change raises x from 4 to 6. Assigning *p=q changes main's p to point to y. The last change raises y from 7 to 10. Printed value is x+y+*p=6+10+10=26. Updating the caller's pointer requires, and here uses, its address.

## Q55
**Correct answer:** 4

Concept: nonassociativity of saturation. b⊕c=1, then a⊕1=7. In the other grouping a⊕b saturates 11 to 7, then 7⊕(−4)=3. Exact final difference=7−3=4. Saturated intermediate information cannot be recovered by a later subtraction.

## Q56
**Correct answer:** 432

Concept: collision detection timing. Frame transmission time is 512/10⁸ seconds=5.12 microseconds, allowing one-way delay 2.56 microseconds. Subtract device delay 0.4 to get cable propagation budget 2.16 microseconds. Distance=2.16·10⁻⁶·2·10⁸=432 metres. Both device delays must be included in the round trip, not added only once to it.

## Q57
**Correct answer:** A, C

Concept: universal conditions over an empty set. Every candidate passes the “for every B in S” condition vacuously. Division's candidates are {1,2}, giving A and disproving B. The second query's candidates are U={1,2,3}, giving C. D mistakes an empty requirement set for a failed requirement. The candidate universe still matters when the condition is vacuous.

## Q58
**Correct answer:** B, D

Concept: comparison lower bounds for merging. Internal orders are fixed, so choose which three of six positions come from the first list: C(6,3)=20, B, not 6!, so A is false. Four comparisons provide at most 16 leaves in a binary decision tree, insufficient; C is false. Five are necessary, and ordinary merging uses at most 3+3−1=5, proving D. A lower bound becomes optimality only when paired with an achieving algorithm.

## Q59
**Correct answer:** 12

Concept: restored state in recursion. At each level the first branch contributes one to x and the second zero, with the increment restored before the second call. The eight leaves correspond to three binary choices; their x values are 3,2,2,1,2,1,1,0. Sum=12. Alternatively each of three levels contributes one at four leaves, giving 3·4. The global variable is restored across branches despite not being a local variable.

## Q60
**Correct answer:** B, D

Concept: determinant and augmented consistency. Expansion gives det A=1+a³, B, nonzero for real a≠−1, disproving A. At −1 the rows sum to zero but the first two are independent, so rank is two, D. The right-hand sides sum to three, contradicting that row dependency; the displayed system is inconsistent, not infinitely soluble, so C is false. A singular matrix alone does not determine the number of solutions.

## Q61
**Correct answer:** A, C

Concept: affine hashing over a prime field. Given outputs r,s, subtract the equations to get a(x−y)=r−s modulo five. Since x−y is nonzero, its inverse determines one a, and then b is determined, proving A. Equal outputs occur exactly when a=0, with probability 1/5, proving C and disproving B because these functions are constant. Conditional on a≠0, outputs can never be equal, whereas independent uniforms would be equal with probability 1/5; D is false. Conditioning can destroy pairwise independence.

## Q62
**Correct answer:** 1

Concept: subnormal spacing and rounding to zero. Minimum normal is 2⁻²=1/4; with two stored fraction bits, subnormal spacing is 2⁻⁴=1/16. The first product 1/16 is exactly representable. Multiplying by 1/2 gives 1/32, midway between zero and 1/16. Ties-to-even chooses zero. Relative error=|0−1/32|/(1/32)=1. Normal-range relative-error bounds need not hold at underflow.

## Q63
**Correct answer:** D

Concept: open-file descriptions versus descriptors. p and q share an offset: read(p,2) gets AB and moves it to two; read(q,1) gets C and moves it to three. r has its own offset; seek to one and read two gives BC without changing p/q. The final p read gets D. Thus D. A treats dup as a separate open; B wrongly advances the shared offset on r's read; C misplaces r's explicit seek. Sharing the underlying file does not always mean sharing an offset.

## Q64
**Correct answer:** 22

Concept: fork isolation, shared mappings and threads. Child's private x=10 does not replace parent's x=2. Shared y becomes 20, visible after the wait. The parent's thread shares its x and computes 2+20=22; join completes before inspection. Treating private memory as shared across fork would give 30; treating the shared mapping as private would give five.

## Q65
**Correct answer:** 2

Concept: reconstructing a Boolean function from differences. The x difference condition gives F=xy XOR g(y,z), where g=F(0,y,z). The z difference then forces g=z XOR h(y). The specified value at 000 imposes h(0)=0, while h(1) remains free. The two functions are xy XOR z and xy XOR y XOR z. Both directly satisfy all constraints. A Boolean difference determines dependence on one variable but leaves a function of the others to be constrained.


