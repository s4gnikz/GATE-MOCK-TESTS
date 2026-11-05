# GATE CS 2027 — Mock 015: Worked Solutions

## Q1

**Correct answer:** A

**Concept:** Monotonic threshold selection.

Any measurement above the higher threshold was also above the old one, so the new flagged set is contained in the old set, A. A strict increase (B) and newly flagging all previously unflagged items (C) contradict that inclusion. The set need not become empty, refuting D.

**Common misconception:** Assuming every threshold change strictly changes the selected set.

## Q2

**Correct answer:** 1

**Concept:** Fixed cells under a half-turn.

A cell at row r,column c maps to row 4−r,column 6−c, numbering from one. Equality requires r=2,c=3, the unique central cell.

**Common misconception:** Counting the full central row or column rather than the cell satisfying both coordinate conditions.

## Q3

**Correct answer:** 32

**Concept:** Second-order recurrence evaluation.

The successive terms are 1,2,4,8,16,32. Each calculation uses the preceding two terms; induction also verifies a_n=2^(n−1).

**Common misconception:** Ignoring the coefficient two on the second preceding term.

## Q4

**Correct answer:** 50

**Concept:** Side sum, squared length and area.

For sides a,b, a+b=15 and a²+b²=125. Hence 2ab=(a+b)²−(a²+b²)=225−125=100, so area ab=50.

**Common misconception:** Treating the diagonal as the sum of the sides.

## Q5

**Correct answer:** C

**Concept:** Agreement with the head of a subject phrase.

“Neither” is singular here and correctly takes “is”, C. A needs “has”, B's singular “list” needs “is”, and D's plural “results” needs “indicate”.

**Common misconception:** Matching the verb to the nearest noun rather than the subject's grammatical head.

## Q6

**Correct answer:** 7.8

**Concept:** Successive price factors and fee base.

For cost 100, marked price is 125 and discounted price 125×0.88=110. The fee is 2.2, leaving net proceeds 107.8 and profit 7.8% on cost.

**Common misconception:** Charging the transaction percentage on cost instead of the specified selling price.

## Q7

**Correct answer:** A

**Concept:** Chained necessary conditions.

A has a symbol but only seven characters, violating the second rule. B triggers neither antecedent. C satisfies the symbol-length requirement without needing a digit. D satisfies both implications. Thus only A necessarily violates a rule.

**Common misconception:** Treating a sufficient antecedent as a required feature of every valid password.

## Q8

**Correct answer:** 6

**Concept:** Area divisibility plus constructive tiling.

Every tile has area six, so an integer square side s must have s² divisible by both two and three. Thus s is divisible by six and cannot be smaller than six. A 6×6 square can be divided into three rows of height two and two columns of width three, proving feasibility.

**Common misconception:** Giving an area bound without showing a tiling exists.

## Q9

**Correct answer:** A

**Concept:** Scope of measured evidence.

Only average processing time was measured as improving, while error counts were not measured. A respects that boundary. B,D invent accuracy findings, and C also turns an average improvement into a statement about every decision.

**Common misconception:** Extending evidence on speed to evidence on accuracy.

## Q10

**Correct answer:** 60

**Concept:** Disjoint composition cases.

Allowed committees contain two engineers and two designers, or three engineers and one designer. Counts are choose(5,2)choose(3,2)=30 and choose(5,3)choose(3,1)=30. Their sum is 60.

**Common misconception:** Including four engineers despite the designer requirement.

## Q11

**Correct answer:** A

**Concept:** Eliminating the changing K-map variable.

Only a differs, while b=c=0, leaving b′c′, A. B and C improperly retain a and drop a fixed variable; D does not describe the two minterms' union.

**Common misconception:** Dropping a fixed literal rather than the bit that changes within the group.

## Q12

**Correct answer:** A, B, C

**Concept:** Refragmentation retains original offsets and identity.

The first child starts at the parent's original offset 100. The second begins 200 bytes later, adding 200/8=25 to give 125, so A holds. The original MF=1 means later original-datagram data still exists after this parent; even its final child therefore keeps MF=1, proving B. The identification remains common to the original datagram, C. D incorrectly restarts the reference frame for offsets.

**Common misconception:** Clearing MF on the last child of a nonfinal parent fragment.

## Q13

**Correct answer:** A

**Concept:** Output dependencies under out-of-order completion.

Two writes to one register create a write-after-write hazard: the program-order younger value must remain final even if completion order differs. A names it. B involves no writes, C is unrelated to register naming, and D falsely classifies every write as a control transfer.

**Common misconception:** Considering only read-after-write dependencies.

## Q14

**Correct answer:** 6

**Concept:** Surjections by excluding constant maps.

There are 2³=8 functions in total. Exactly two omit a target element: the two constant maps. The remaining six are onto.

**Common misconception:** Treating distinct domain elements as indistinguishable.

## Q15

**Correct answer:** 4

**Concept:** Product of generating functions.

Expanding gives Σ_(i≥0)x^i times Σ_(j≥0)x^(2j). The coefficient counts nonnegative solutions to i+2j=7, with j=0,1,2,3. There are four.

**Common misconception:** Using ordered partitions into arbitrary positive parts instead of the two generating factors' choices.

## Q16

**Correct answer:** A

**Concept:** Existential range-restricted assignment.

The existential requires some listed department to which e is assigned, A. It does not require all departments (B), forbid assignments (C), or universally restrict the domain (D).

**Common misconception:** Reading EXISTS as a universal condition.

## Q17

**Correct answer:** 2

**Concept:** Cyclic implication.

If any variable is true, the implications force the other two true. If none is true, all implications also hold. Therefore only FFF and TTT satisfy the formula.

**Common misconception:** Treating the three implications as independent clauses without propagating their consequences.

## Q18

**Correct answer:** A, C

**Concept:** Nonnegative rather than strictly positive weights.

Dijkstra requires no negative edge, so zero weights are permitted, A. Zero edges or equal-cost routes can give equal distances, C. Paths need not be unique, refuting B, and zero cycles do not decrease path costs without bound, refuting D.

**Common misconception:** Confusing zero-weight cycles with negative-weight cycles.

## Q19

**Correct answer:** 2

**Concept:** Rank–nullity from a row dependence.

The third row is the sum of the first two. Those first rows are independent, so rank is two. Four columns give nullity 4−2=2.

**Common misconception:** Subtracting rank from the number of rows instead of the domain dimension.

## Q20

**Correct answer:** 0.5

**Concept:** Second-order exponential behaviour.

eˣ=1+x+x²/2+O(x³). Cancellation of the constant and linear terms leaves the quotient tending to 1/2.

**Common misconception:** Using only the first-order approximation after its terms cancel.

## Q21

**Correct answer:** A

**Concept:** Longest valid token prefix.

The longest valid initial token is >=, leaving >, so A follows. B invents an undeclared => token, C invents an undeclared full token, and D discards a valid trailing token.

**Common misconception:** Treating longest match as permission to create tokens absent from the lexical specification.

## Q22

**Correct answer:** 8

**Concept:** Free bits in an implicant pattern.

There are three dashes, each independently taking zero or one. Thus the pattern covers 2³=8 minterms.

**Common misconception:** Counting fixed positions instead of free positions.

## Q23

**Correct answer:** A

**Concept:** Characterizing a recursive grammar.

Each a is prepended and each b appended around the remaining S. Thus all generated words are a^n b^m, with counts independently chosen; every such word is obtainable. A is correct. B and C impose unjustified equal counts or alternation; D includes ba, which cannot be generated.

**Common misconception:** Assuming grammar ambiguity changes the generated language into all strings.

## Q24

**Correct answer:** 8

**Concept:** Directed adjacency entries.

Each directed edge is stored once, so eight edges require eight entries. Vertex headers are explicitly excluded; undirected doubling does not apply.

**Common misconception:** Automatically multiplying every adjacency-list edge count by two.

## Q25

**Correct answer:** 1

**Concept:** HAVING after NULL-sensitive aggregation.

Group A has one non-NULL v and group B two. Only B satisfies COUNT(v)=2, leaving one group.

**Common misconception:** Counting the NULL row in COUNT(v).

## Q26

**Correct answer:** A

**Concept:** One-bit addition.

Unequal inputs yield sum one, giving XOR. Both inputs one produce carry one, giving AND. A combines these correctly. B mishandles 11 in its sum, C swaps incompatible functions, and D does not implement addition even at 00.

**Common misconception:** Using OR as the sum bit without checking the two-one case.

## Q27

**Correct answer:** A

**Concept:** Acceptance requires an exhausted input as well as the stack criterion.

A stack can empty before the unread suffix has been processed. That configuration is not accepting under the stated convention, so A holds. B is false by the convention itself; C and D impose nonexistent restrictions.

**Common misconception:** Ignoring unread input when checking an acceptance configuration.

## Q28

**Correct answer:** 7

**Concept:** Pointer aliasing to a scalar.

p points to x, so reading *p obtains three and assigning *p stores seven into the same x.

**Common misconception:** Assuming a pointer write modifies only the pointer's own storage.

## Q29

**Correct answer:** 64

**Concept:** Bit patterns versus maximum value.

Six unsigned bits encode 2⁶=64 values, from zero to 63 inclusive. The question asks the count, not the greatest value.

**Common misconception:** Answering 63 by confusing maximum value with number of values.

## Q30

**Correct answer:** B

**Concept:** Prefix block boundaries.

A /26 leaves six host bits, so this block covers final octets 128–191. Only 160 lies inside. A is below, C begins the next block, and D changes the preceding octet.

**Common misconception:** Including the first address of the next subnet in the current block.

## Q31

**Correct answer:** A, B

**Concept:** Explicit communication interfaces.

Message passing uses message send/receive operations and can cross separate process address spaces, giving A,B. Application protocols can still race or deadlock, refuting C. Blocking implementations need not busy-wait, refuting D.

**Common misconception:** Treating the communication mechanism as a blanket correctness guarantee.

## Q32

**Correct answer:** A

**Concept:** Atomicity of an invariant-preserving update sequence.

The pair may be inconsistent after the first update and before the second. If that interval is unprotected, another thread can observe it, giving A. B,C,D make false claims about mutex capabilities or implicit atomicity.

**Common misconception:** Protecting individual assignments while leaving the multi-field invariant temporarily exposed.

## Q33

**Correct answer:** 4

**Concept:** Independent nullable choices.

Choose a or ε from A and b or ε from B, giving ab,a,b,ε. They are four distinct terminal strings.

**Common misconception:** Counting ε as a literal terminal character.

## Q34

**Correct answer:** A

**Concept:** S-attributed definitions.

S-attributed definitions use synthesized attributes, computed from child information, so A is correct. B describes a different restriction; C removes the attributes; D excludes the very child dependency synthesis uses.

**Common misconception:** Confusing synthesized and inherited directions of information flow.

## Q35

**Correct answer:** 3

**Concept:** Stable ordering within equal keys.

The key-one records remain B,D, and the key-two records remain A,C. Output is (1,B),(1,D),(2,A),(2,C), placing A third.

**Common misconception:** Reordering equal-key records after sorting by the primary key.

## Q36

**Correct answer:** 4

**Concept:** Endpoint-dependent port reuse.

Four connections to Z require four distinct public ports, giving a lower bound four. Reuse those same four across the three X connections and two Y connections, because external endpoints distinguish the mappings. This attains four.

**Common misconception:** Summing all connection counts despite explicit permission to reuse ports across distinct external endpoints.

## Q37

**Correct answer:** A, C, D

**Concept:** Multiple resource instances and cycle insufficiency.

R can finish without another resource and release one A. Q then obtains A, completes and releases B (and A); P obtains B and finishes. Thus A and D hold. The apparent P–Q cycle does not prevent this external release, establishing C and refuting B.

**Common misconception:** Applying the single-instance cycle criterion to a resource type with multiple instances.

## Q38

**Correct answer:** B

**Concept:** Cumulative acknowledgment across holes.

The third segment leaves byte 1000 missing, so ACK=1000. The first fills 1000–1099 but leaves 1100 missing, so ACK=1100. The fourth still leaves that hole, so ACK stays 1100. The second finally fills the hole and joins all buffered data through 1399, so ACK=1400. B is correct; A follows arrival ends, while C,D advance past missing bytes too early.

**Common misconception:** Treating cumulative ACKs as acknowledgments of the most recently arriving segment alone.

## Q39

**Correct answer:** A

**Concept:** Deferred referential-integrity checks.

The final pair of rows references existing keys in both tables. Deferred checking permits constructing that mutually dependent state within the transaction, whereas immediate checking rejects the first insertion into either initially empty table. A holds. Deferral changes checking time, not the final constraint, refuting B,C; D denies the achievable valid state.

**Common misconception:** Treating deferred checking as disabling the constraint permanently.

## Q40

**Correct answer:** 10

**Concept:** Lexical environment identity versus caller environment.

Q1 retains the environment of P1, the activation that created it. Its x is therefore P1.x=10, even though P2 with another x is the caller.

**Common misconception:** Resolving lexical variables from the most recent caller's activation.

## Q41

**Correct answer:** 0.375

**Concept:** Conditional density over a planar region.

P(Y>X²)=∫₀¹(1−x²)dx=2/3. The weighted first moment over that event is ∫₀¹x(1−x²)dx=1/4. Dividing gives (1/4)/(2/3)=3/8=0.375.

**Common misconception:** Conditioning by substituting Y=X² instead of integrating the region above the curve.

## Q42

**Correct answer:** 6

**Concept:** Simultaneous sequential-state updates.

The states are 001→011→111→110→101→010→100. The target first appears after six edges. Every new bit uses the preceding state's bits, not earlier updates in the same edge.

**Common misconception:** Updating flip-flop variables sequentially as an in-place software assignment.

## Q43

**Correct answer:** 64

**Concept:** Counting signed overflow pairs.

Overflow occurs for two nonnegative operands summing to at least eight, or two negative operands summing below −8. For values 0–7, the first count is 1+2+…+7=28. Write negative magnitudes as 1–8; sums greater than eight occur in 1+2+…+8=36 ordered pairs. Opposite signs cannot overflow. Total 28+36=64.

**Common misconception:** Counting unordered pairs or excluding the asymmetric endpoint −8.

## Q44

**Correct answer:** 5

**Concept:** Counting a particular base-case leaf.

Let Z(n) count zero-argument calls. Z(0)=1, Z(1)=0 and Z(n)=Z(n−1)+Z(n−2). Thus Z(2),…,Z(6) are 1,1,2,3,5. Only the last count is requested, not the total number of calls.

**Common misconception:** Counting both base cases together.

## Q45

**Correct answer:** A, C

**Concept:** Preserving short-circuit effects and exceptions.

A and C both avoid division when x=0, preserving the original behaviour. B introduces a division-by-zero exception on that input. D changes the false result for x=0 and for many other values. Thus only A,C are sound.

**Common misconception:** Reordering apparently pure arithmetic while ignoring observable traps.

## Q46

**Correct answer:** B

**Concept:** Dead results versus observable evaluation.

The unused store can be removed, but the device effect of the call must remain, B. A,C remove it; D duplicates it. Dead-variable reasoning does not license eliminating side effects.

**Common misconception:** Treating a dead destination as proof that the whole right-hand expression is dispensable.

## Q47

**Correct answer:** 7

**Concept:** Equivalence relations as set partitions.

Choose a nonempty proper subset as one block: 2⁴−2=14 choices. Each two-block partition is counted twice, once for each complementary block. Therefore there are 14/2=7 relations.

**Common misconception:** Treating the two classes as labelled or ordered.

## Q48

**Correct answer:** 4

**Concept:** Cycles of a modular rotation permutation.

Repeatedly adding eight modulo twelve returns after 12/gcd(12,8)=3 positions. Each cycle has length three, so the twelve positions form four cycles. For example one is 0,8,4.

**Common misconception:** Equating the rotation amount with the number of permutation cycles.

## Q49

**Correct answer:** A, C

**Concept:** Reversal matching versus copying.

Even palindromes are context-free: a PDA can guess the midpoint and match the second half by stack reversal, proving A. The copy language is not context-free. Intersecting it with 0*1*0*1* gives matching separated zero and one blocks; the word 0^p1^p0^p1^p cannot satisfy every CFL pumping requirement because a length-p window cannot change both separated copies of each affected block while retaining their equalities and order. This refutes B. On the unary alphabet the copy language is exactly (00)*, proving C. CFLs are not closed under general CFL intersection, refuting D.

**Common misconception:** Assuming a stack can compare a second copy in the same order as easily as a reversed copy.

## Q50

**Correct answer:** B

**Concept:** Backward-shift deletion respecting probe paths.

The key in slot 3 has home 2, so moving it into the hole at 2 preserves its search path. The key at 4 has home 4 and can remain there; an empty slot 3 does not interrupt a search starting at 4. Thus B is valid. A strands the home-2 key behind an empty slot. C moves a home-4 key before its starting point and makes it unreachable by the specified search. D loses keys.

**Common misconception:** Shifting every later key blindly rather than checking whether its probe path crosses the hole.

## Q51

**Correct answer:** A, B, D

**Concept:** Lossless dependency-preserving BCNF decomposition.

The intersection is B, and B→BC determines all of R2, giving losslessness, A. A→B is enforced in R1 and B→C in R2, proving B. In R, B is not a superkey but determines C, so C is false. A is a key of R1 and B a key of R2; their nontrivial projected dependencies have key determinants, proving D.

**Common misconception:** Inferring BCNF for the original relation from BCNF of its components.

## Q52

**Correct answer:** 9

**Concept:** Spectral constraints from a matrix polynomial.

Symmetry gives a real orthonormal eigenbasis. Each eigenvalue satisfies λ³=λ, so λ∈{−1,0,1}. Rank four gives four nonzero eigenvalues, and trace zero forces two +1 and two −1, with one zero. I+2A therefore has eigenvalues 3,3,−1,−1,1, whose product is nine.

**Common misconception:** Treating rank and trace separately without combining them to determine multiplicities.

## Q53

**Correct answer:** 128

**Concept:** Constrained volume maximization.

Volume V(x)=x(12−2x)². Its derivative factors as (12−2x)(12−6x), giving the interior stationary point x=2. Volume tends to zero at both endpoints and rises then falls around two, so the maximum is 2×8²=128.

**Common misconception:** Choosing the largest possible cut, which collapses the base area.

## Q54

**Correct answer:** A

**Concept:** Vacuous pumping conditions for a finite language.

With p=8, no word in L has length at least p, so the condition holds vacuously. For any positive p≤7, word a⁷ is long enough; every valid pumped segment is nonempty, and pumping it twice produces a word longer than seven, outside L. Thus no smaller p works. A is correct, B,C fail this test, and D denies regularity of finite languages.

**Common misconception:** Assuming a pumping lemma must actually pump some word even when all words are shorter than its bound.

## Q55

**Correct answer:** 136

**Concept:** External-sort passes and buffer fan-in.

Initial generation produces ceil(17/3)=6 runs. Two-way merge passes reduce run counts 6→3→2→1, requiring three merge passes plus the initial pass. Each reads and writes seventeen blocks, so total transfers are 4×2×17=136.

**Common misconception:** Using all three buffers as input streams instead of reserving an output buffer.

## Q56

**Correct answer:** 21

**Concept:** Floyd meeting time and reset phase.

Once both pointers are in the cycle, their positions agree when the slow step count is a multiple of five. The first such count at least the prefix length three is five, so phase one has five iterations and 15 traversals. Resetting one pointer to the head makes them meet at the entry after three paired steps, adding six traversals. Total 21.

**Common misconception:** Counting iterations as traversals or counting the pointer reset as walking the prefix.

## Q57

**Correct answer:** B

**Concept:** Datagram truncation semantics.

The first receive copies eight bytes from the twelve-byte datagram and discards its four-byte excess. The second receives the separate five-byte datagram. Thus B gives 8,5. A combines datagrams improperly, C exceeds the buffer, and D retains excess bytes explicitly specified to be discarded.

**Common misconception:** Applying byte-stream receive semantics to a datagram interface.

## Q58

**Correct answer:** A, B

**Concept:** Starvation under strict priority.

Persistent higher-priority work can always be selected first, establishing A. An aging policy that eventually raises a waiting job sufficiently can address that risk, B. Readiness alone gives no time bound under strict priority, refuting C; preemption does not create fairness, refuting D.

**Common misconception:** Equating eligibility to run with a guarantee of timely scheduling.

## Q59

**Correct answer:** B

**Concept:** Summing coupled loop costs.

For each i, work runs i floor(n/i) times, at most n, giving O(n²). For i>n/2, floor(n/i)=1, and the sum of these i values alone is Θ(n²), giving a matching lower bound. Thus B is tight. A omits the innermost factor, C treats all three bounds as independent n, and D ignores the outer iterations.

**Common misconception:** Multiplying maximum loop bounds without using their dependence on i.

## Q60

**Correct answer:** A, C

**Concept:** Online scheduling fairness versus finite workloads.

Nearby arrivals can keep winning shortest-seek choices and starve a distant request, proving A and refuting B. For a finite queue without arrivals, each service removes one request, so all are eventually served, C. D describes an endpoint constraint associated with SCAN, not SSTF.

**Common misconception:** Inferring bounded waiting under arbitrary arrivals from termination on a fixed finite queue.

## Q61

**Correct answer:** 22

**Concept:** Microinstruction field allocation.

The next-address field needs log₂256=8 bits. Add twelve control bits and two sequencing bits: 12+8+2=22.

**Common misconception:** Confusing the number of control-store words with the address-field bit count.

## Q62

**Correct answer:** 170

**Concept:** Unit-job scheduling with deadlines and profits.

Schedule A in slot one, B in slot two and D in slot three for profit 70+60+40=170. A,B,C all have deadlines at most two, so at most two of them can be taken; the best pair is A,B. D is the only job eligible to add a third-slot profit. Thus 170 is both attainable and maximal.

**Common misconception:** Selecting the three largest profits without checking deadline feasibility.

## Q63

**Correct answer:** -1.5

**Concept:** Signed ties-to-even fixed-point rounding.

Scaling by four gives exact encoded value −5.5, midway between −6 and −5. The even integer is −6, so the stored real value is −6/4=−1.5.

**Common misconception:** Assuming ties-to-even always rounds toward zero for negative inputs.

## Q64

**Correct answer:** 9

**Concept:** Bank reuse constraints in interleaved memory.

The first four requests issue at cycles 0,1,2,3 to different banks. Their banks become reusable at 6,7,8,9, so the next four issue at those cycles. The eighth request issues at nine, not at seven, because each bank remains busy for six cycles.

**Common misconception:** Assuming bank interleaving hides every latency regardless of the number of banks.

## Q65

**Correct answer:** A, C

**Concept:** Finite binary expansions.

A reduced rational has a finite binary expansion exactly when its denominator is a power of two. 3/8=0.011₂ and 7/4=1.11₂ fit the stated precision, giving A,C. The reduced denominators of 1/10 and 1/3 contain odd factors, so B,D require infinitely repeating expansions.

**Common misconception:** Assuming every short decimal fraction is exact in finite binary precision.
