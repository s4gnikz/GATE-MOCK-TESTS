# GATE CS 2027 — Mock 008: Worked Solutions

Use the exact values and rounding ranges in the paper's final key.

## Q1

**Correct answer:** B  
**Concept:** Mean versus dispersion.

Reduced variability means reduced dispersion under the reported measure, so B follows. It need not eliminate all variation (A), make the unchanged mean zero (C), or establish bias relative to a true value (D).

**Common misconception:** Precision and accuracy are distinct properties.

## Q2

**Correct answer:** 17  
**Concept:** Simultaneous remainders.

The positive numbers congruent to 2 modulo 5 begin 2,7,12,17. Their remainders modulo 7 are 2,0,5,3. The first qualifying number is 17; earlier positive candidates have been exhausted.

**Common misconception:** Satisfying one congruence does not satisfy the other automatically.

## Q3

**Correct answer:** B  
**Concept:** Context-dependent vocabulary.

“Qualified support” is support with reservations or conditions. B is therefore correct. A expresses its opposite; C concerns a person's credentials rather than the character of the support; D introduces a legal restriction absent from the sentence.

**Common misconception:** A word's sense depends on the phrase in which it occurs.

## Q4

**Correct answer:** 4  
**Concept:** Unfolding reflections.

Each fold doubles the number of layers. The punch passes through four distinct sheet locations, which separate on unfolding. Being away from folds and boundaries ensures the four holes do not coincide or merge.

**Common misconception:** A hole on a fold can behave differently; the stated location rules that out.

## Q5

**Correct answer:** A, C  
**Concept:** Contraposition and existential information.

Passed calibration implies installed, so not installed implies did not pass calibration (A). The second premise explicitly supplies C. B reverses the first implication; D adds an unsupported connection between testing and calibration.

**Common misconception:** “Did not pass” need not mean a test was taken and failed; it is the negation of passing.

## Q6

**Correct answer:** 14  
**Concept:** Negative-marking inequality.

The one-mark section gives 30−10/3=80/3. If k two-mark answers are correct, that section gives 2k−(20−k)2/3=(8k−40)/3. Total is (8k+40)/3. Requiring at least 50 gives k≥13.75, hence the least integer is 14.

**Common misconception:** Increasing k by one replaces a wrong answer as well as adding a correct one.

## Q7

**Correct answer:** C  
**Concept:** Quadratic scaling.

Both areas are proportional to the square of the changed linear dimension. Multiplying that dimension by 1.1 multiplies area by 1.21, a 21% increase. C is correct. A,D confuse linear and area scaling; B omits the additional 0.1² term.

**Common misconception:** Percentage changes in length and area are not equal.

## Q8

**Correct answer:** 3.6  
**Concept:** Expected payout.

Different colours occur with probability 2×(3/6)(3/5)=3/5. The payout is 6 on that event and zero otherwise, so expectation is 6×3/5=3.6.

**Common misconception:** The second draw uses a denominator of five, not six.

## Q9

**Correct answer:** B  
**Concept:** Precedence-constrained parallel tasks.

Run A and B from time zero on the two workers. They finish at 4 and 3; C then runs from 4 to 6. The chain A→C requires at least 4+2=6 hours, so this schedule is optimal. B is correct; A violates that lower bound, while C,D fail to use available concurrency optimally.

**Common misconception:** Worker capacity cannot remove a precedence constraint.

## Q10

**Correct answer:** 0.2857  
**Concept:** Circular adjacency.

Fix one specified person to remove rotational symmetry. The other occupies one of seven remaining positions uniformly, and exactly two are adjacent. Probability is 2/7≈0.285714, rounding to 0.2857.

**Common misconception:** A circle has two adjacent positions around each seat, including the wraparound edge.

## Q11

**Correct answer:** B  
**Concept:** Overlapping pattern occurrences.

The windows ending at positions 3 and 5 are both 101. The detector emits two pulses, so B holds. A disallows the overlap, C counts the three possible windows without testing them, and D counts bits rather than matches.

**Common misconception:** An overlapping detector may reuse the last bit of an earlier match.

## Q12

**Correct answer:** A, B, D  
**Concept:** Signed encodings.

Sign-magnitude 10000000 is negative zero, numerically zero (A). Two's complement gives −128 (B). With a leading zero, both read the lower seven bits as a nonnegative value (D). With leading one they generally disagree, and the first pattern already refutes C.

**Common misconception:** A bit string has no signed numeric meaning independently of its representation convention.

## Q13

**Correct answer:** 6  
**Concept:** Involutions and cycle structure.

An involutive permutation has only cycles of length one or two. Choose the two fixed points in C(4,2)=6 ways; the remaining pair must be swapped, giving exactly one permutation for each choice. Total six.

**Common misconception:** The remaining nonfixed elements cannot independently choose their images in a permutation.

## Q14

**Correct answer:** 32  
**Concept:** Powers of a rank-one matrix.

A²=2A, so induction gives A⁵=2⁴A. Its trace is 16×2=32. Equivalently, A's eigenvalues are 2 and 0, whose fifth powers sum to 32.

**Common misconception:** Matrix powers do not mean taking powers of individual entries.

## Q15

**Correct answer:** B  
**Concept:** Allocated storage and sizeof.

Allocated storage persists until freed even if its pointer variable leaves scope (B), though losing every pointer can make it unreachable. malloc does not initialize it to zero (A). sizeof *p determines the int type's size without reading its value here (C). Allocation is three times sizeof(int), not necessarily three bytes (D).

**Common misconception:** Pointer-variable lifetime and allocated-object lifetime differ.

## Q16

**Correct answer:** 3  
**Concept:** Binary-search trace.

The compared keys are 8, then 12, then 14. The third comparison finds equality. Midpoint rounding and the stated inclusive halves determine this sequence.

**Common misconception:** The worst-case search depth is not necessarily the depth of a particular target.

## Q17

**Correct answer:** A, B, D  
**Concept:** Regular-language closure.

Reverse a finite automaton's edges and exchange start/final roles using nondeterminism for reversal (A). Complement a complete DFA's accepting set for B. Concatenation can be implemented by an ε-NFA connecting copies, proving D. C fails with L=Σ* and a nonregular CFL: their intersection is that nonregular CFL.

**Common misconception:** Intersection with a language from a larger class need not remain regular.

## Q18

**Correct answer:** B  
**Concept:** Predictive-parser pending terminals.

Each of the two leading a symbols causes an S→aSb expansion that leaves one future b on the stack. After both a symbols are consumed, two b symbols are pending around the remaining S. S→ε then allows them to be consumed. Thus the maximum is two, B; the other counts do not match the two expansions.

**Common misconception:** Count pending stack terminals, not all input symbols already read or still unconsumed.

## Q19

**Correct answer:** 12  
**Concept:** Aliased physical mappings.

The distinct frame numbers are 7,2,9, only three frames. Their total physical storage is 3×4=12 KiB. Two virtual mappings of frame 7 do not allocate two copies of it.

**Common misconception:** Virtual-page count can exceed distinct mapped physical-frame count.

## Q20

**Correct answer:** 10  
**Concept:** Tree degree sum.

Let l be the leaf count. There are l+13 vertices and l+12 edges. Summing degrees gives l+8×3+5×2=2(l+12), so l+34=2l+24 and l=10.

**Common misconception:** Degree-two vertices add edges and vertices without changing the leaf count implied by branching vertices.

## Q21

**Correct answer:** 0.7854  
**Concept:** Riemann sums.

Rewrite each summand as (1/n)/(1+(k/n)²). The limit is ∫₀¹ dx/(1+x²)=arctan(1)−arctan(0)=π/4≈0.785398. Round to 0.7854.

**Common misconception:** The factor 1/n is essential when identifying a Riemann sum.

## Q22

**Correct answer:** A  
**Concept:** SQL aggregate treatment of NULL and duplicates.

COUNT(*) counts four rows. COUNT(x) excludes the one NULL but retains both rows with value 2, giving three. A is correct. B excludes NULL from COUNT(*); C,D mistakenly apply DISTINCT.

**Common misconception:** COUNT(column) is not COUNT(DISTINCT column).

## Q23

**Correct answer:** 2484  
**Concept:** Per-datagram overhead.

Each of three packets contains 800+8+20=828 bytes. Total is 3×828=2484. Headers are incurred three times because the application sends three separate datagrams.

**Common misconception:** Header overhead applies per packet, not once per application message.

## Q24

**Correct answer:** A  
**Concept:** Full-adder outputs.

With x=y=1, the total is 2+c. Its low bit is c and its carry is always one, yielding A. B incorrectly complements the sum; C,D incorrectly make carry depend on c.

**Common misconception:** Carry indicates a total of at least two, which is already guaranteed by x=y=1.

## Q25

**Correct answer:** 2  
**Concept:** Instruction width versus bus transfer width.

The instruction has four bytes and each transfer supplies two. Alignment permits two complete transfers with no extra boundary overhead. Total is 32/16=2 cycles.

**Common misconception:** Instruction width need not equal the memory interface width.

## Q26

**Correct answer:** A, B, D  
**Concept:** Traversal reconstruction.

Preorder gives root A. A is first in inorder, so it has no left subtree. Repeating the argument gives a right-only chain A→B→C→D (A,B). Postorder visits that chain backward, D,C,B,A (D). C describes the opposite chain and contradicts inorder.

**Common misconception:** Equal preorder and inorder sequences do not indicate a balanced tree.

## Q27

**Correct answer:** 0.0889  
**Concept:** Moments of a transformed variable.

The density of X is 1/2. E[Y]=E[X²]=(1/2)∫₋₁¹x²dx=1/3, and E[Y²]=E[X⁴]=1/5. Variance is 1/5−1/9=4/45≈0.0888889, rounding to 0.0889.

**Common misconception:** E[Y²] here requires the fourth moment of X, not the second.

## Q28

**Correct answer:** D  
**Concept:** Output-sensitive lower bounds.

There are C(n,2)=n(n−1)/2 distinct pairs to emit. Constant work per output gives Ω(n²), so D is the tight bound from output size. A,B,C are asymptotically weaker and do not express the tight output-size requirement.

**Common misconception:** An efficient internal algorithm cannot avoid the time needed to materialize its required output.

## Q29

**Correct answer:** 1  
**Concept:** Acceptance of the empty word.

The initial state accepts ε. Every nonempty word immediately enters the rejecting sink and never leaves. Thus the language is exactly {ε}, containing one word.

**Common misconception:** The empty language and the language containing the empty word are different.

## Q30

**Correct answer:** B  
**Concept:** Precedence-preserving intermediate code.

Multiplication must compute b*c before the addition to a, as in B. A groups (a+b)*c; C changes the products; D computes separate values without combining a with b*c as required.

**Common misconception:** Three-address temporaries must preserve the original expression tree's dependencies.

## Q31

**Correct answer:** A, C  
**Concept:** Blocking versus busy waiting.

A blocked reader can be descheduled, requiring no polling CPU work (A). A writer's successful operation may enable it to resume (C). The writer's ability to make progress refutes necessary system deadlock (B), and it does not require the reader to be executing (D).

**Common misconception:** A blocked process is not synonymous with a deadlocked system.

## Q32

**Correct answer:** 4  
**Concept:** Cartesian product and selection.

Initially there are 3×2=6 tuples. The A=2 condition removes its two pairings with x,y. Four remain, corresponding to the two remaining A values times two B values.

**Common misconception:** Removing one value from a component domain may remove multiple tuples.

## Q33

**Correct answer:** A  
**Concept:** Local next-hop address resolution.

ARP resolves the gateway's IPv4 address to its Ethernet address on the local LAN, enabling a frame to be delivered to that next hop (A). It does not discover TCP sequence numbers (B), routing tables (C), or DNS names (D).

**Common misconception:** For a remote destination, the link-layer next hop can be the gateway rather than the remote IP endpoint.

## Q34

**Correct answer:** 12  
**Concept:** An inessential Boolean variable.

Each of the six qualifying four-variable assignments permits either value of the fifth variable. The count doubles to 12.

**Common misconception:** Independence from an input means both values replicate each output-table entry.

## Q35

**Correct answer:** D  
**Concept:** Direct-mapped conflicts.

Pairs A,B,C map to the same line within each pair: residues 1,2,3 respectively. Blocks 4 and 5 map to lines 0 and 1 and can coexist. Thus D is correct.

**Common misconception:** Distinct memory blocks can still compete for exactly the same direct-mapped cache line.

## Q36

**Correct answer:** 543  
**Concept:** Queue and stack order composition.

The two dequeues remove 1 and 2. The final queue is front-to-back 3,4,5. Pushing that order puts 5 on top, and the pops emit 5,4,3, yielding 543.

**Common misconception:** Transferring through a stack reverses the surviving queue order, not the original entire input history.

## Q37

**Correct answer:** B  
**Concept:** Comparison decision trees.

Correct sorting must distinguish the n! strict input orders, so the tree needs at least n! leaves. A binary tree of height h has at most 2ʰ leaves, giving h≥ceil(log₂(n!)). B is correct. A undercounts orders; C asserts an incorrect universal quadratic cost; D assumes a comparison settles a full key position.

**Common misconception:** A comparison supplies one binary outcome, not a key's complete rank.

## Q38

**Correct answer:** A, C  
**Concept:** Unequal-count context-free language.

Split L into i<j and i>j; a PDA can match counts with its stack and accept an unmatched excess on either side, so their union is context-free (A). Its complement within a*b* is exactly the equal-count language (C). If L were regular, subtracting it from regular a*b* would make that equal-count language regular, a contradiction, so B is false. ε has equal zero counts and is excluded (D false).

**Common misconception:** Context-free unequal-count languages need not be regular.

## Q39

**Correct answer:** 3  
**Concept:** Value-based DAG sharing.

Let original operands be a0,b0,c0. t1 and t2 share node N1=a0+b0. The assignment to a creates N2=N1+c0. t3 creates N3=N2+b0, because a's value has changed. t4=N1+c0 shares N2. Exactly three addition nodes suffice.

**Common misconception:** Expression identity depends on operand values and versions, not only textual variable names.

## Q40

**Correct answer:** 7  
**Concept:** Optimal page replacement.

The initial 1,2,3 incur three faults. On 4, evict 3, whose next use is furthest away. On 5, evict 4. After hits on 1,2, references 3 and 4 each fault, replacing pages no longer needed before the final 5. Total faults occur at positions 1,2,3,4,7,10,11: seven. At each replacement choose a page whose next use is furthest or absent.

**Common misconception:** Optimal replacement uses future next-use distance, not past recency.

## Q41

**Correct answer:** A  
**Concept:** Dependency-preserving chained decomposition.

AB,BC,CD directly enforce each stated FD. Joining AB with BC is lossless because B determines BC; joining that result with CD is lossless because C determines CD. Thus A has both properties. B loses B→C across its disjoint components; C and D similarly cannot enforce the original chain using only their projected dependencies and lose essential associations.

**Common misconception:** Keeping all attributes across components does not by itself preserve their dependencies or tuple associations.

## Q42

**Correct answer:** 370  
**Concept:** Fragment offsets.

Maximum payload is 1500−20=1480, already divisible by eight. The payloads are 1480,1480,1040. The final fragment starts after 2960 payload bytes, so its offset field is 2960/8=370.

**Common misconception:** Fragment offsets measure original payload position, excluding all IPv4 headers.

## Q43

**Correct answer:** A, C  
**Concept:** Combinational dependency depth.

The final carry can depend sequentially on all n propagation stages, taking n units (A). Extra lookahead/group logic can shorten that dependency chain (C). Physical simultaneous presence of gates does not remove signal dependencies, refuting B. The ripple bound grows with n, refuting D.

**Common misconception:** Gate parallelism and critical-path depth are different measures.

## Q44

**Correct answer:** 24  
**Concept:** Strong components of a tournament.

There are 64 orientations in total. A non-strong tournament on four vertices is either transitive, giving 4!=24 orders, or consists of a directed three-cycle and a fourth vertex that beats all three or loses to all three. The latter gives 4 choices of singleton, 2 cycle orientations, and 2 directions, totaling 16. These cases are disjoint and exhaustive because a nontrivial strongly connected tournament needs at least three vertices. Therefore strongly connected tournaments number 64−24−16=24.

**Common misconception:** A tournament with a directed cycle need not be strongly connected as a whole.

## Q45

**Correct answer:** 40  
**Concept:** Instruction-count and CPI tradeoff.

Old time is 10⁹×1.2/(2×10⁹)=0.6 seconds. New time is 0.8×10⁹×1.4/(2×10⁹)=0.56 seconds. The reduction is 0.04 seconds=40 ms.

**Common misconception:** A reduction in instruction count does not translate directly into the same percentage time reduction when CPI changes.

## Q46

**Correct answer:** B  
**Concept:** Bottom-up heap construction.

Processing index 3 swaps 3 with 7, producing [1,2,7,4,5,6,3]. Index 2 swaps 2 with 5, giving [1,5,7,4,2,6,3]. At index 1, swap 1 with 7 and then with 6, yielding [7,5,6,4,2,1,3]. The counts are 1+1+2=4, so B is correct. A counts only root repair, C misses one downward swap, and D overcounts the four actual exchanges.

**Common misconception:** Bottom-up construction first repairs child subtrees; the root must be traced using those updated values.

## Q47

**Correct answer:** 4  
**Concept:** Zero-weight edges and shortest simple paths.

Every s-to-t path must pay one unit leaving s and one entering t, so its weight is at least two. Paths s-a-t, s-b-t, s-a-b-t, and s-b-a-t each attain two. These exhaust simple paths because only a,b can be internal vertices. Thus the count is four.

**Common misconception:** Counting walks instead would permit repetitions around a zero-weight cycle and change the problem fundamentally.

## Q48

**Correct answer:** A, C  
**Concept:** Pumping-lemma quantifiers.

The first p symbols are all a, and y is a nonempty part of that prefix, proving A. Pumping down removes positive a count while leaving p b symbols, so the result is outside L (C). Pumping twice also unbalances counts, refuting B. D violates the lemma's required decomposition constraints.

**Common misconception:** A contradiction must work for every allowed decomposition of the selected witness.

## Q49

**Correct answer:** C  
**Concept:** Uses before overwrites.

The first x value is used immediately in y=x*c before being overwritten, and y is then returned. Neither definition is dead, so C holds. A,D ignore the intervening use of x; B ignores return y. The later x=0 may itself be dead under the stated observability assumption, but that is not one of the two assignments asked about.

**Common misconception:** A later overwrite does not kill earlier uses that already consumed the previous value.

## Q50

**Correct answer:** A, C  
**Concept:** Counting-semaphore permits.

Each signal contributes one permit, and Q needs two, so eventual scheduling lets it print (A). If Q arrives before the first signal it blocks, proving C. Counting permits do not collapse (B false), and Q cannot complete both waits before the second permit is produced (D false).

**Common misconception:** Counting semaphores preserve multiple permits, unlike a single Boolean notification flag.

## Q51

**Correct answer:** 7.3  
**Concept:** Nonuniform coupon collection.

Use inclusion–exclusion on missing-symbol events and sum tail probabilities. The expectation is Σ1/p_i − Σ1/(p_i+p_j) +1/(p_A+p_B+p_C). Thus E=2+3+6−6/5−3/2−2+1=7.3. Each reciprocal comes from summing a geometric tail for avoiding the indicated set of symbols.

**Common misconception:** Replacing unequal probabilities with their average destroys the waiting-time contribution of the rare symbol.

## Q52

**Correct answer:** 3  
**Concept:** Candidate-key closure and minimality.

B never appears on a right-hand side, so every key contains B. AB determines C then D; BC determines D then A; BD determines A then C. Each pair is minimal, and B alone determines none of A,C,D. Any larger key contains one of these pairs and is not minimal. There are exactly three candidate keys.

**Common misconception:** Supersets of candidate keys are superkeys, not additional candidate keys.

## Q53

**Correct answer:** B  
**Concept:** Flow versus congestion control.

The advertised window is receiver-buffer flow control, so ordinary new data cannot exceed its zero allowance (B). It is not evidence of router loss (A), does not itself close the connection (C), and does not require the independent congestion window to be zero (D).

**Common misconception:** Receiver capacity and network congestion are different constraints on sending.

## Q54

**Correct answer:** 218  
**Concept:** Counting Boolean functions by essential variables.

There are 2⁸=256 functions of three inputs. For each chosen inessential variable, the function is determined by four truth-table entries, giving 16 functions. For two specified inessential variables there are four functions; for all three there are two constants. Inclusion–exclusion leaves 256−3×16+3×4−2=218 functions depending on every input.

**Common misconception:** Functions ignoring several variables belong to several excluded sets and must not be subtracted repeatedly without correction.

## Q55

**Correct answer:** 5  
**Concept:** Inclusive cache invalidation across instruction/data traffic.

Data A and B each fetch from memory; the second data A is an L1 hit and leaves L2's order A,B unchanged. Instruction C fetches, making L2 order A,B,C. Instruction D fetches and evicts its LRU block A, invalidating A in L1. The final data A misses both levels and fetches again. The five fetches are A,B,C,D,A. Instruction traffic never enters L1 but can still invalidate it through inclusion.

**Common misconception:** A recently used L1 block can remain old in L2 when L1 hits do not update L2 replacement state.

## Q56

**Correct answer:** A, B, D  
**Concept:** Array pointer arithmetic boundaries.

p+4 points to the last element (A). p+5 is the permitted one-past pointer (B), though dereferencing it would be invalid. Subtracting two from that pointer returns to element 3 (D). p+6 lies beyond the allowed array-or-one-past range, so even forming it is not permitted (C false).

**Common misconception:** A pointer may be valid to form but invalid to dereference.

## Q57

**Correct answer:** 60  
**Concept:** Deadline-constrained unit jobs.

Schedule A in slot 1, C in slot 2, D in slot 3 for profit 20+30+10=60. The only three slots with any feasible deadline are 1–3. Among A,B,C, whose deadlines are at most 2, at most two can be chosen; A and C give the largest pair profit 50. D adds 10, proving optimality.

**Common misconception:** Choosing high-profit jobs still requires enough slots before their individual deadlines.

## Q58

**Correct answer:** B  
**Concept:** Decidability from two recognizers.

Every input belongs to exactly one of L and its complement, so exactly the corresponding recognizer is guaranteed eventually to accept. Dovetailing reaches that event in finite time and yields a decision (B). A has no valid universal timeout, C discards the complementary recognizer's guarantee, and D is not a construction for complementation of arbitrary machines.

**Common misconception:** The two recognizers need not halt on their nonmembers for the combined decider to halt.

## Q59

**Correct answer:** 4  
**Concept:** FOLLOW through nullable sequences.

In S→ABc, the suffix after A is Bc. B can start with a via A, d via nullable A followed by D, or b directly; B can also vanish, exposing c. Thus a,b,c,d all enter FOLLOW(A). In B→AD, D contributes d and can vanish, so FOLLOW(B) contributes c, adding nothing new. FOLLOW(A) is exactly {a,b,c,d}, of size four. The trailing c in S prevents an end marker from propagating to these occurrences.

**Common misconception:** A nullable symbol requires examining the entire suffix, not only the next symbol's nonempty FIRST set.

## Q60

**Correct answer:** 5  
**Concept:** CPU affinity, assignment, and local scheduling order.

If C goes to CPU 1, CPU 0 executes B then A with waits 0,3, while CPU 1 executes C,D in either order with waits 0,2. Total waiting is 5. If C goes to CPU 0, its three bursts are 2,3,4; shortest-first minimizes their sum to 0+2+5=7, and D waits zero on CPU 1. These exhaust C's two possible placements. Deliberate idle time cannot reduce waiting because every job is already available. The minimum is 5.

**Common misconception:** Selecting a per-CPU ordering alone is insufficient when a flexible job's CPU assignment changes the attainable total.

## Q61

**Correct answer:** A, C  
**Concept:** Recoverability versus dirty reads.

T2 commits after the transaction whose value it read, so the displayed schedule is recoverable (A). Its read nevertheless occurs before T1 commits, making it a dirty read and refuting cascadelessness (B). If T1 instead aborted after that read, T2 could need rollback (C). The displayed commit order directly refutes D.

**Common misconception:** Recoverable schedules can still permit cascading aborts.

## Q62

**Correct answer:** 24  
**Concept:** Sequence-space lifetime and window constraints.

At 2²⁰ bytes/s, reuse time is 2^(n−20) seconds. Strictly exceeding 12 requires n≥24: n=23 gives 8 seconds and n=24 gives 16. The window needs at least 2²⁰ bytes and must be smaller than 2^(n−1); at n=24 that is feasible. The lifetime condition is the tighter one, so 24 is minimal.

**Common misconception:** The sequence-space period and the window-size bound impose separate constraints, and strict inequalities matter at boundaries.

## Q63

**Correct answer:** A, C  
**Concept:** State encoding and unused-state behaviour.

Two bits encode at most four states, so at least three are needed (A). Three bits provide eight patterns, leaving three outside the five-state cycle (C). Five one-hot bits are one possible encoding, not a necessity (B false). Recovery from unused states depends on the chosen transition logic and is not automatic (D false).

**Common misconception:** Designing the intended cycle does not by itself specify safe behaviour from every other encoding.

## Q64

**Correct answer:** A, B, D  
**Concept:** Rank of a composition.

The image of B has dimension three. A's one-dimensional kernel can remove at most one dimension from that image, so rank(AB)≥2, proving A and excluding C. Taking A=B=diag(1,1,1,0) gives rank three (B). Taking A=diag(1,1,1,0) and B=diag(1,1,0,1) gives AB=diag(1,1,0,0), rank two (D).

**Common misconception:** Knowing the two individual ranks does not uniquely determine the product rank; the kernel/image alignment matters.

## Q65

**Correct answer:** 0.3679  
**Concept:** Tangent intercepts and area minimization.

The tangent is y=(ln a+1)x−a. Its intercepts are −a and a/(ln a+1), so area is a²/[2(ln a+1)] for the given positive denominator. Set u=ln a+1>0: area is e^(2u−2)/(2u). Its logarithmic derivative is 2−1/u, negative below u=1/2 and positive above. Thus the global minimum is at a=e^(−1/2), with area e⁻¹≈0.367879, rounding to 0.3679.

**Common misconception:** Use the magnitude of the negative vertical intercept when computing the triangle's positive area.


