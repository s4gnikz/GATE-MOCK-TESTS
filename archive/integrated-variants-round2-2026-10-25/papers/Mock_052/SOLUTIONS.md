# Worked Solutions — Mock Test 052

## Q1

**Correct answer:** 42

Concept: constant second differences. Rearranging gives a(n+2)−a(n+1)=a(n+1)−a(n)+2. Differences start at four and then are 6,8,10,12. Thus a6=2+4+6+8+10+12=42. There are five increments between the first and sixth terms.

## Q2

**Correct answer:** 20

The original perimeter is2(6+4)=20. Each corner removal deletes two unit boundary segments and introduces two new unit boundary segments, producing no net change. The four cuts do not overlap, so the remaining perimeter is still20. Loss of area does not necessarily mean loss of perimeter.

## Q3

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Agreement with the head of a subject phrase.

“Neither” is singular here and correctly takes “is”, C. A needs “has”, B's singular “list” needs “is”, and D's plural “results” needs “indicate”.

**Common misconception:** Matching the verb to the nearest noun rather than the subject's grammatical head.

## Q4

**Correct answer:** 10

If the mass is M, initial value is50M. Removal subtracts5·50=250 and replacement adds5·40=200. Thus45M=50M−50, giving M=10. The removed uniform mixture has its existing average cost, not the cost of just one constituent.

## Q5

**Correct answer:** 2

For x=1 the statements have truth pattern true,false,false. For2 it is true,true,false. For3 it is false,false,true, and for4 false,true,false. Exactly two are true only at2. Evaluating the conjunction of all three would answer a different condition.

## Q6

**Correct answer:** C

Concept: periodic transformations. The orbit is (1,0)→(1,1)→(0,1)→(0,0)→(1,0). Since 2027 leaves remainder three on division by four, the answer is (0,0), C. A, B and D correspond to remainders one, two and zero. The translation term is part of each application.

## Q7

**Correct answer:** D

The qualification explicitly denies inferring impossibility from zero observed failures. D asserts exactly that inference and conflicts. A restates the observation; B and C acknowledge untested possibilities and future revision. Empirical absence is not a universal logical proof.

## Q8

**Correct answer:** 216 (exact)
**Concept:** Restricted digit permutations.

The final digit is 0 or 5. Ending in 0 leaves 5!=120 arrangements, all with nonzero first digit. Ending in 5 leaves five digits including zero: there are 5!−4!=96 arrangements whose first digit is nonzero. Total 216.

**Common misconception:** The leading-zero restriction affects the two ending-digit cases differently.

## Q9

**Correct answer:** A, B, D
**Concept:** Mean, median, mode and range.

The original sum is 2+9+7=18. Mean four after adding two x values gives 18+2x=32, hence x=7. The sorted data are 1,1,3,3,3,7,7,7. The middle pair is 3,3, so the median is 3; both 3 and 7 occur three times, so there is no unique mode. Range is 7−1=6. Thus A,B,D hold and C fails.

**Common misconception:** A mean change need not change the median, and a mode need not be unique.

## Q10

**Correct answer:** 45
**Concept:** Overall average speed including idle time.

Total elapsed time is 180/40=4.5 hours. The first 90 km takes 90/45=2 hours, and the stop takes 0.5 hour. The second part therefore takes 2 hours, giving speed 90/2=45 km/h.

**Common misconception:** Average speed uses total elapsed time, including the stop specified in the question.

## Q11

**Correct answer:** C

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **B: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

The IPv4 header checksum covers the source address, so A is true. TCP includes its ports and a pseudo-header containing IP addresses, making B true. C and D incorrectly omit checksum-covered fields. Rewriting at one protocol layer can affect integrity checks at another.

## Q12

**Correct answer:** A, C

Matrix multiplication gives (M²)[u,u]=Σ_v M[u,v]M[v,u], counting return walks of length two, so A. Transposition interchanges source and destination, proving C. Each directed edge contributes one entry, not two, disproving B. Opposite edges u→v and v→u give a positive diagonal in M² without self-loops, refuting D.

## Q13

**Correct answer:** C

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) II.
- **C: Correct.** It includes both valid candidates and no invalid candidate.
- **D: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** NULL in anti-membership queries.

For x=1, NOT IN compares against both 2 and NULL, yielding UNKNOWN; x=2 yields FALSE; x=NULL yields UNKNOWN. WHERE retains none, proving A. NOT EXISTS instead asks whether an equality is TRUE for some inner row. It finds a match only for x=2, returning 1 and NULL (B). Removing the inner NULL permits x=1 through NOT IN but leaves outer x=NULL UNKNOWN, refuting C. IN returns only 2, not three rows, refuting D.

**Common misconception:** NOT IN and correlated NOT EXISTS need not agree in the presence of NULL.

## Q14

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) I.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** TCP connection demultiplexing.

For these IPv4 TCP connections, both endpoint addresses and ports identify the connection, so C holds and distinct remote endpoints can distinguish them, as A states. A listening service routinely retains the same local endpoint for many established connections, refuting B and D.

**Common misconception:** Treating the server's port as the entire connection identity.

## Q15

**Correct answer:** 6

The first fork creates two branches. Its child enters the then branch and one fork produces2 descendants reaching the end. Its parent enters the else branch, where two successive forks double the population twice, producing4 descendants. Total2+4=6. Children created inside a chosen branch continue there; they do not reevaluate the earlier if using a newly returned fork value.

## Q16

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Range restriction and infinite-domain complements.

The result is every integer outside finite R, which is infinite. A correctly identifies the missing range restriction. B reverses the meaning of negation; C contradicts the infinite complement; D incorrectly treats negation itself as a safety guarantee.

**Common misconception:** Silently switching from the stated infinite domain to a finite active domain.

## Q17

**Correct answer:** 2.6667 (accepted range 2.66665–2.66675)

The old squared-deviation sum is 4 observations×variance 4=16. Adding observations equal to the old mean leaves the mean at 5 and adds zero squared deviation. Divide 16 by the new population size 6 to obtain 8/3≈2.6667. The population denominator is 6, not the sample-variance denominator 5.

## Q18

**Correct answer:** A, B, D

Lexicographic row-count minimization favours2 over3 regardless of the secondary cost, so A holds. Cost-first favours6 over8, proving B. These different outcomes disprove C and demonstrate D's ambiguity. State the optimization objective before comparing covers.

## Q19

**Correct answer:** C

Normalize the original time to 1. The new time is 1/2+(1/2)/2=3/4, so speedup is 1/(3/4)=4/3. A incorrectly halves all time; B confuses a time reduction with a speedup factor; D ignores the improved component. The unaffected fraction bounds the benefit.

## Q20

**Correct answer:** 64

Concept: cache geometry. The cache contains 16384/64=256 lines. Four lines per set give 256/4=64 sets. Associativity counts lines per set, not bytes per set.

## Q21

**Correct answer:** 1

Exactly one decoder is enabled, and that decoder raises exactly one output. The other raises none. Therefore one of sixteen outputs is high. Sharing address inputs does not imply both enabled outputs are active.

## Q22

**Correct answer:** 3

**Concept:** Kernel cosets and the image of a homomorphism.

The kernel solves8x≡0 modulo12, equivalently x≡0 modulo3. It contains0,3,6,9 and has size4. The number of kernel cosets is12/4=3, also the size of the image{0,4,8}.

**Misconception:** Returning the number of kernel elements instead of its index.

## Q23

**Correct answer:** 1

After adding c, the three-edge route costs4+3c and the direct edge costs5+c. Direct is strictly cheaper when5+c<4+3c, or c>1/2. The smallest positive integer is1. Adding a constant per edge does not add the same amount to paths with different edge counts.

## Q24

**Correct answer:** C

Concept: bounded blocking queues. Each first send fills its queue. Neither process reaches a receive until after its second send, but those second sends block on full queues. Once both have run that far, neither can make progress, C. A ignores capacity after the first send; B incorrectly distinguishes the symmetric processes; D invents overwrite semantics. Eventual scheduling cannot overcome this circular wait.

## Q25

**Correct answer:** A, C, D

**Concept:** Forced edges and alternative perfect matchings.

Vertex b has only neighbour2, so every perfect matching uses b–2. Then a must use1 and c must use3, giving exactly one perfect matching. A and C are true. Edge a–2 is unused in that matching, so removing it does not destroy the matching; B is false. Adding b–1 allows the additional matching a–2,b–1,c–3, so D is true.

**Misconception:** Assuming every edge incident to a matched vertex is essential to the matching.

## Q26

**Correct answer:** 3

Concept: inverse image under a homomorphism. Each nonempty symbol image starts with a and ends with b. Concatenating two or more images creates a ba boundary, forbidden in a*b*. The empty word, 0 and 1 all qualify, and no longer word does. Thus three. Balanced symbol counts alone would not enforce the required order of all as before all bs.

## Q27

**Correct answer:** 4
**Concept:** Cartesian product and selection.

Initially there are 3×2=6 tuples. The A=2 condition removes its two pairings with x,y. Four remain, corresponding to the two remaining A values times two B values.

**Common misconception:** Removing one value from a component domain may remove multiple tuples.

## Q28

**Correct answer:** 78

**Concept:** Inclusion–exclusion for forbidden fixed points.

Begin with 5!=120. Subtract 4!=24 for each of the forbidden events π(1)=1 and π(2)=2, then add 3!=6 for their intersection. The result is 120−24−24+6=78.

**Common misconception:** Subtracting the overlap twice without restoring it.

## Q29

**Correct answer:** 2

Two successful waits consume the initial two permits. The third thread blocks until a signal occurs, which has not yet happened. Therefore at most two enter. Atomicity of waits prevents multiple threads from consuming the same permit.

## Q30

**Correct answer:** 8
**Concept:** VIPT index constraints.

A page has 12 offset bits, of which six address a byte within a cache line. At most six more can index sets, allowing 64 sets. The cache has 32768/64=512 lines, requiring at least 512/64=8 ways. Eight is a power of two and attains the bound.

**Common misconception:** The page offset must hold both the line-offset and set-index fields.

## Q31

**Correct answer:** B, C, D

The underlying question is correctly answered by A. This variant asks for its invalid answers, so select the complementary set: B, C, D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Quantifiers in the pumping lemma.

Regularity promises at least one pumpable valid decomposition. Showing that one chosen decomposition fails does not exclude another. For the selected word, every allowed y lies in the initial zeros and has positive length; pumping it down breaks equal counts. That universal step repairs the proof, as A says. B is not required, C incorrectly bans a permitted pumping exponent, and D reverses the length condition.

**Common misconception:** Choosing the adversary's decomposition in a nonregularity proof.

## Q32

**Correct answer:** A, C, D

The underlying question is correctly answered by B. This variant asks for its invalid answers, so select the complementary set: A, C, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

1. p points to the first row, and q points to the start of row 1. The addition changes a[0][2] from 6 to 9.
2. r initially points to a[0][1]. Because postfix ++ binds before unary *, *r++ stores q[0]=1 at that element, then advances r to a[0][2].
3. q[2]=*r sets a[1][2]=9. The printed sum is 1+9=10. All pointer arithmetic stays inside its row array, and side effects are sequenced across statements.
- Original option A: This misses the earlier update of a[0][2].
- Original option B: The final values are 1 and 9.
- Original option C: This retains the old value 4 in a[0][1].
- Original option D: No access is out of bounds and no scalar has unsequenced conflicting accesses.

## Q33

**Correct answer:** C

Concept: postfix translation. Multiplication forms subtree b*c, emitting bc*. Addition emits a, then that subtree, then +, producing abc*+. C is correct. A represents (a+b)*c; B is prefix order; D represents a*(b+c). Tree traversal follows precedence before emitting operators.

## Q34

**Correct answer:** 1

The first qualifying value7 is at position1; positions2 and3 also qualify but are not first. This is a lower-bound search, not an arbitrary successful match.

## Q35

**Correct answer:** 9

The coefficients of(1−x)^(−2) are n+1. Multiplying by1+x makes the x4 coefficient5+4=9. Equivalently, convolve the two contributions at powers4 and3. Formal power-series arithmetic needs no numerical convergence assumption.

## Q36

**Correct answer:** 12
**Concept:** Cardinality bounds from functional dependencies.

For each fixed A, AB→C permits at most one C per each of four B values, bounding the total by 3×4=12. AC→B requires those C choices to be distinct for a fixed A; five C values are available, so four distinct choices are possible. Use the same injective assignment from four B values to four C values for each A to attain twelve tuples.

**Common misconception:** A dependency-based upper bound must also be checked for compatibility with the other dependencies.

## Q37

**Correct answer:** A, B, D

The underlying question is correctly answered by C. This variant asks for its invalid answers, so select the complementary set: A, B, D.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Original needs are P0=(1,2), P1=(1,1), P2=(2,0). With available (1,1), P1 can finish, releasing (0,1), so work becomes (1,2). P0 can then finish, releasing (1,0), making (2,2); P2 then finishes. Thus the original state is safe. Tentatively grant (0,1) to P0: available becomes (1,0), and P0's need becomes (1,1). P1 still needs (1,1) and P2 needs (2,0). No process can finish with (1,0), so the tentative state is unsafe and the request must be deferred. Unsafe does not by itself assert that deadlock has already occurred.
- Original option A: False: after the grant P0 needs one B, but no B is available.
- Original option B: False: P2 needs two A, but only one A is available.
- Original option C: True: the original safe sequence exists, while no process can start the tentative safety reduction.
- Original option D: False: P1,P0,P2 is a safe sequence in the original state.

## Q38

**Correct answer:** 509

The original clock period is max(2,3,10,4)+1=11ns. A four-stage pipeline executes100 independent instructions in100+4−1=103 cycles, taking1133ns. The redesign has five stages and period5+1=6ns, giving104 cycles and624ns. Savings1133−624=509ns. Faster steady-state throughput must be combined with the changed filling latency.

## Q39

**Correct answer:** A, D
**Concept:** Composite foreign keys and three-valued CHECK evaluation.

A skips the foreign-key check because one component is NULL, and qty=5 satisfies CHECK. B skips the foreign-key check but fails qty>0. C has both key components non-NULL, so the missing parent (9,9) rejects it despite the UNKNOWN check. D finds parent (1,2), and NULL qty produces UNKNOWN rather than FALSE, so it succeeds.

**Common misconception:** A nullable CHECK is not equivalent to requiring its expression to be TRUE; NOT NULL is a separate constraint.

## Q40

**Correct answer:** A, C

Once queued bytes have been read, an orderly end of the peer's sending stream can be reported by a zero receive result, proving A. Zero is a count, not an extra byte: B is false. TCP maintains two directions; closing one sending direction does not itself close the other, so C is true and D false. An orderly half-close differs from a connection error or forced process exit.

## Q41

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

N behaves identically on every input. It accepts every string if the embedded simulation accepts, and no strings otherwise, proving A,B. An emptiness decider could therefore distinguish arbitrary acceptance by negating its result, proving C. Producing N requires only embedding the simulation instructions, not resolving their outcome, so D is false.

## Q42

**Correct answer:** B

The underlying question is correctly answered by A, C, D. This variant asks for its invalid answers, so select the complementary set: B.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Backward liveness across branching control flow.

On the B2 path, y is read before any redefinition, so A holds. On B3, a,b,c are read; thus D holds and B is false. The old x is read on neither path: B2 never uses it, and B3 overwrites it before use. Hence C holds. Including the pending branch test, the full live set is {a,b,c,y,p}.

**Common misconception:** Treating a value used earlier in the block as necessarily live after its last use.

## Q43

**Correct answer:** 6

The schedule is P:[0,1), Q:[1,3), R:[3,4), Q:[4,6), P:[6,12). Waiting time equals completion minus arrival minus CPU requirement: P=12−0−7=5, Q=6−1−4=1, R=4−3−1=0. Total6. A process's remaining time, rather than its original demand, determines preemption.

## Q44

**Correct answer:** 3

Using old-state bits simultaneously gives00→01→11→00. The first positive return occurs after3 edges. Updating A and then using its new value for B would describe a different sequential computation, not this synchronous circuit.

## Q45

**Correct answer:** 513

The effective address is 100+12−8=104. Little-endian order places byte01 in bits 7..0 and02 in bits 15..8. The low16 bits are 0x0201=2×256+1=513. Computing the address and interpreting the byte order are separate steps.

## Q46

**Correct answer:** 5

Represent R by a2×2 Boolean matrix, with one row per x. The first condition excludes empty rows; each row has three possible nonempty patterns, giving nine matrices. The second condition requires at least one full row. If neither row is full, each is one of the two singleton rows, giving four excluded matrices. Hence9−4=5. The existential choice of x must cover every y in that same row.

## Q47

**Correct answer:** 15.875

**Concept:** Saturating fixed-point conversion.

The largest signed eight-bit integer code is 127, and three fractional bits give real maximum 127/8=15.875. Exact 17 exceeds that range, so saturation stores 15.875.

**Common misconception:** Wrapping modulo 256 instead of applying the specified saturation rule.

## Q48

**Correct answer:** A, C

The escaped function must still access valid storage for its captured variable, so A is true. A retained environment referenced by a closure supplies such storage, proving C. A reclaimed frame offers no such lifetime guarantee, making B and D false. Lexical visibility and storage lifetime are related but distinct requirements.

## Q49

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

**Concept:** Subtraction flags and signed range.

The full unsigned sum is A+(2ⁿ−1−B)+1=2ⁿ+A−B. A carry exists exactly when A≥B, meaning no unsigned borrow, proving A. Retained bits give the modulo result, proving B. Opposite signed operands can produce a sign inconsistent with A when their difference exceeds range, establishing D. Borrow and signed overflow are different: for four bits, 0−1 borrows but has valid signed result −1, refuting C.

**Common misconception:** Using one flag interpretation for both signed and unsigned arithmetic.

## Q50

**Correct answer:** 6

Track the pair(length mod3, number of1s mod2), giving six states and one accepting pair(0,0). All pairs are reachable: at any sufficiently large length of a chosen residue, choose either zero or one1. For any two distinct pairs, choose a suffix whose length cancels the first residue and whose1-count parity cancels the first parity; sufficiently long suffixes allow either parity. The second pair then fails at least one condition, so all six are distinguishable and six is minimal. A product construction alone establishes only an upper bound; distinguishability supplies the lower bound.

## Q51

**Correct answer:** 19

**Concept:** Counting a pruned recursion tree.

Nonleaf levels handle positions 1 through 5. Their call counts are 1,2,3,5,8: a prefix ending in exclusion allows two next choices; one ending in inclusion allows only exclusion. This yields the Fibonacci recurrence for successive prefix counts. Sum 1+2+3+5+8=19. The thirteen final output calls are leaves and are excluded.

**Common misconception:** Counting a full binary tree despite pruning adjacent selections.

## Q52

**Correct answer:** 4 (exact)

**Concept:** Engineering Mathematics — Matrices determinants and linear systems

1. AX=XA means the entries repeat under a simultaneous cyclic shift of row and column indices. Symmetry therefore forces X to have rows [a,b,c,b], [b,a,b,c], [c,b,a,b], [b,c,b,a].
2. The zero-row-sum requirement gives a+c+2b=0. The vector (1,-1,1,-1) has eigenvalue mu=a+c-2b=-4b. Every vector (p,q,-p,-q) has eigenvalue nu=a-c; this is a two-dimensional eigenspace. Together with the all-ones vector, these spaces span R^4.
3. X^2=X holds exactly when mu and nu each belong to {0,1}, since the remaining eigenvalue is already zero.
4. Every ordered pair (mu,nu) determines one matrix: b=-mu/4, a=mu/4+nu/2, c=mu/4-nu/2. There are 2*2=4 pairs and hence four matrices.

**Common misconception:** The commuting and symmetry constraints couple entries before idempotence is imposed; an arbitrary projection is not allowed.

## Q53

**Correct answer:** A, B, D

**Concept:** Structural description of a grammar's language.

Each S expansion adds a at the front and b at the end; T generates an arbitrary central block of c symbols. Thus the language is {aⁿcᵐbⁿ:n,m≥0}. A and B follow. abcc puts c symbols after b and cannot be generated, so C is false. aacbb has n=2,m=1, proving D.

**Common misconception:** Tracking symbol counts without tracking their ordering restrictions.

## Q54

**Correct answer:** C

The underlying question is correctly answered by A, B, D. This variant asks for its invalid answers, so select the complementary set: C.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Forwarding normally creates a new link-layer header for the outgoing link, while IP destination remains end-to-end, proving A,D and disproving C. TTL is within the IPv4 header and affects its checksum, proving B. Different layers can legitimately change different fields at the same hop.

## Q55

**Correct answer:** A
**Concept:** Conflict versus view serializability with blind writes.

On x, the first two writes create T1→T2, while the second and third create T2→T1. This cycle rules out conflict serializability. For view equivalence, x's final writer T1 forces T2 before T1. The read of y by T3 reads T2's write, forcing T2 before T3. No constraint orders T1 versus T3. Thus the two serial orders are T2,T1,T3 and T2,T3,T1. A is correct. B,D incorrectly ignore the conflict cycle; C incorrectly treats it as proof against view serializability.

**Common misconception:** Blind writes allow some view-serializable schedules to fail conflict serializability.

## Q56

**Correct answer:** 3
**Concept:** Counting distinct optimal knapsack subsets.

With E selected, four units of capacity remain. The best addition is A+B, value 6, for total value 11. C or D adds only 4 and cannot be paired with A or B within the remaining capacity. Without E, choosing C+D leaves room for exactly one of A,B, also giving value 11 in two ways. Choosing at most one of C,D yields at most A+B+C or A+B+D, value 10. Thus the optimum is 11 and exactly ABE,ACD,BCD attain it.

**Common misconception:** Items with equal weights and values remain distinct when counting subsets.

## Q57

**Correct answer:** A

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) II, IV and omits valid candidate(s) I, III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Preserving short-circuit effects and exceptions.

A and C both avoid division when x=0, preserving the original behaviour. B introduces a division-by-zero exception on that input. D changes the false result for x=0 and for many other values. Thus only A,C are sound.

**Common misconception:** Reordering apparently pure arithmetic while ignoring observable traps.

## Q58

**Correct answer:** 60
**Concept:** Deadline-constrained unit jobs.

Schedule A in slot 1, C in slot 2, D in slot 3 for profit 20+30+10=60. The only three slots with any feasible deadline are 1–3. Among A,B,C, whose deadlines are at most 2, at most two can be chosen; A and C give the largest pair profit 50. D adds 10, proving optimality.

**Common misconception:** Choosing high-profit jobs still requires enough slots before their individual deadlines.

## Q59

**Correct answer:** 8

With four significant binary bits, representable values near8 are8=1.000×2³ and9=1.001×2³, spacing1. The exact sum8.5 is halfway; ties-to-even picks8 because its trailing significand bit is0. The second addition again rounds8.5 to8. Thus the result is8, although performing the exact sum first would give9. Rounding after each operation is consequential.

## Q60

**Correct answer:** D

The underlying question is correctly answered by A, B, C. This variant asks for its invalid answers, so select the complementary set: D.

- **A: Do not select.** It is a valid answer to the underlying question.
- **B: Do not select.** It is a valid answer to the underlying question.
- **C: Do not select.** It is a valid answer to the underlying question.
- **D: Select.** It is not a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

Choose x_n=1/(π/2+2πn) for value1 and y_n=1/(3π/2+2πn) for value−1; both approach0 positively. A and B are true and their different limits disprove D. Since |x sin(1/x)|≤|x|, the squeeze theorem proves C. Bounded oscillation can disappear after multiplication by a vanishing factor.

## Q61

**Correct answer:** B

**Concept:** Programming and Data Structures — Linked lists

The first iteration detaches node 2 and prepends it to q, leaving head 1→3→4→5→6, q 2, and p at 3. The second detaches 4, leaving head 1→3→5→6, q 4→2, p at 5. The third detaches 6, leaving head 1→3→5, q 6→4→2, p NULL. Every detached successor is prepended, so its list is reversed. All terminal next pointers are NULL.

- **A:** False: prepending each removed node reverses their order.
- **B:** True: odd-position nodes remain, and removed even-position nodes are reversed.
- **C:** False: p advances to the next surviving node, so node 3 is never detached.
- **D:** False: removal is based on alternating successors, not splitting the original list in half.

**Common misconception:** Updating next links changes what the subsequent advance follows; removed nodes are prepended rather than appended.

## Q62

**Correct answer:** A, B, C

The underlying question is correctly answered by D. This variant asks for its invalid answers, so select the complementary set: A, B, C.

- **A: Select.** It is not a valid answer to the underlying question.
- **B: Select.** It is not a valid answer to the underlying question.
- **C: Select.** It is not a valid answer to the underlying question.
- **D: Do not select.** It is a valid answer to the underlying question.

**Underlying reasoning.** The following explanation evaluates A–D against the original question. An option described as correct there is deliberately excluded by this variant's selection rule.

For k²≤i<(k+1)², the step is k and the band's width is2k+1. Thus a constant number of iterations suffices to leave each band, giving O(sqrt(n)) over the bands. Each step before termination is at most sqrt(n), while total increase must be at least n−1, giving Ω(sqrt(n)). Together this proves D. A is too small; B,C overestimate growth by treating the increment as constant. Perfect-square boundaries change step size gradually, not multiplicatively.

## Q63

**Correct answer:** 0.80 (two decimals)
**Concept:** Tail probabilities of an independent minimum.

For integer k≥1, P(X≥k)=(2/3)^k. Independence gives P(min(X,Y)≥k)=(4/9)^k. Summing the nonnegative integer variable's tails yields E[min]=Σ_(k≥1)(4/9)^k=(4/9)/(5/9)=4/5=0.80.

**Common misconception:** The expected minimum is not the minimum of the two expectations.

## Q64

**Correct answer:** A

Candidates I, II are exactly the valid answers to the underlying question.
- **A: Correct.** It includes both valid candidates and no invalid candidate.
- **B: Incorrect.** It includes invalid candidate(s) III and omits valid candidate(s) I.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **D: Incorrect.** It includes invalid candidate(s) III, IV and omits valid candidate(s) I, II.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

Concept: Huffman tie choices. Merge the two ones to make 2; then merge any two of the three weight-two nodes to make 4. Remaining weights are 2,4,4, one four being the original symbol. If the next merge uses the other four, the original four is a child of the final root and has length one (A). If it uses the original four, that symbol has length two (B). Its first possible merge is this penultimate merge, so depths three or four cannot occur; C and D fail. Equal-weight choices can change individual lengths while preserving optimal weighted cost.

## Q65

**Correct answer:** D

Candidates I, III are exactly the valid answers to the underlying question.
- **A: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) I.
- **B: Incorrect.** It includes invalid candidate(s) II and omits valid candidate(s) III.
- **C: Incorrect.** It includes invalid candidate(s) IV and omits valid candidate(s) III.
- **D: Correct.** It includes both valid candidates and no invalid candidate.

**Underlying reasoning.** In the retained explanation below, original labels A, B, C and D refer respectively to candidates I, II, III and IV above, not to the new pair-choice labels.

**Concept:** Online scheduling fairness versus finite workloads.

Nearby arrivals can keep winning shortest-seek choices and starve a distant request, proving A and refuting B. For a finite queue without arrivals, each service removes one request, so all are eventually served, C. D describes an endpoint constraint associated with SCAN, not SSTF.

**Common misconception:** Inferring bounded waiting under arbitrary arrivals from termination on a fixed finite queue.

