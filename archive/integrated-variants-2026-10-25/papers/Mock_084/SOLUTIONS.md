# Worked Solutions — Mock Test 084

## Q1

**Correct answer:** A, C
**Concept:** Weighted means with positive weights.

The combined mean is a convex combination of 40,60,80 with all weights positive, so it lies strictly between 40 and 80 (A). Equal sizes give 60 (C). Sizes 2,1,1 give mean 55, refuting B and D.

**Common misconception:** An unweighted mean of group means is valid only with suitable group weights.

## Q2

**Correct answer:** B

The circumference difference is 2π(r+1)−2πr=2π metres. Advancing the outer start by that distance leaves equal distances to the common finish. Equal speeds then give equal finish times. A uses only half the difference; C and D depend on the unspecified radius and do not equal the difference in general.

## Q3

**Correct answer:** B

**Concept:** Negating a universal statement.

“Not every” means that at least one submitted report lacks a diagram. Thus B is equivalent. A and C both say none has a diagram, which is stronger; D concerns a report outside the submitted set and need not hold.

**Common misconception:** Negating “all” produces “none” rather than “at least one not”.

## Q4

**Correct answer:** 60

Let the initial volume be V. The removed ten litres contain6 litres of milk. The final milk volume is0.6V−6, and the final total remains V. A1:1 ratio requires0.6V−6=0.5V, so V=60. Water replacement restores volume but not milk.

## Q5

**Correct answer:** C

A's and B's statements are logical opposites, so exactly one of them is true regardless of the coin's location. To have exactly one true label overall, C's statement must be false: the coin is in C. Thus C is correct; locations A and B each make two labels true, and D incorrectly denies the valid location.

## Q6

**Correct answer:** C

Concept: periodic transformations. The orbit is (1,0)→(1,1)→(0,1)→(0,0)→(1,0). Since 2027 leaves remainder three on division by four, the answer is (0,0), C. A, B and D correspond to remainders one, two and zero. The translation term is part of each application.

## Q7

**Correct answer:** D

**Concept:** Distinguishing a rate, a count and causal evidence.

For example,100 issued books with20 late returns gives20%;200 issued books with30 late returns gives15%. Thus a declining fraction can accompany an increasing count. The passage also explicitly withholds a causal conclusion, making D correct. A invents both causality and a claim about every borrower. B contradicts the numerical possibility. C is false: if total volume rises while the timely fraction also rises, the timely count rises, not falls.

**Misconception:** Comparing percentages without their denominators, or treating an observed before/after change as causal proof.

## Q8

**Correct answer:** 48

**Concept:** Circular arrangements with opposite-pair constraints.

Fix one specified person to remove rotational duplication; their partner's opposite seat is forced. Assign the other three couples to the three remaining opposite seat-pairs in 3! ways, then orient each couple in two ways. Total 3!×2³=48. Reflections have not been identified and are correctly counted separately.

**Common misconception:** Dividing by rotations again after already fixing an anchor person.

## Q9

**Correct answer:** 2.5

Initially successes are 80+95=175 out of 200, or87.5%. Later they are160+95=255 out of300, or85%. The decrease is2.5 percentage points. The regional rates are unchanged; changing their weights changes the combined rate.

## Q10

**Correct answer:** 16.8284 (accepted range 16.82835–16.82845)

Reflection of the removed triangle produces one triangular notch with base from(1,0) to(3,0) and apex(2,1). The original perimeter16 loses the base length2 and gains two sides of length sqrt2. Thus P=14+2sqrt2≈16.828427. The shared fold line inside the removed notch does not become an exposed edge.

## Q11

**Correct answer:** C

Concept: postfix translation. Multiplication forms subtree b*c, emitting bc*. Addition emits a, then that subtree, then +, producing abc*+. C is correct. A represents (a+b)*c; B is prefix order; D represents a*(b+c). Tree traversal follows precedence before emitting operators.

## Q12

**Correct answer:** D
**Concept:** Static and dynamic activation links.

R's lexical parent is P, so one static link reaches P. Its caller is Q, whose caller is P, so two dynamic links are required. A reverses the link roles, B assumes caller and lexical parent coincide, and C incorrectly follows a sibling in the static chain.

**Common misconception:** Lexical nesting and call nesting are different structures.

## Q13

**Correct answer:** 4

**Concept:** Ring-counter period.

The single 1 visits four distinct positions before returning to its starting position. Therefore the first return occurs after four edges.

**Common misconception:** Assuming every four-flip-flop counter has period sixteen regardless of its transition function.

## Q14

**Correct answer:** A, B

SET NULL attempts the null assignment, proving A, but NOT NULL then forbids it, proving B. Constraints do not silently override one another, refuting C. SET NULL is not CASCADE deletion, refuting D. Compatible referential actions and column constraints are necessary for the operation to succeed.

## Q15

**Correct answer:** A, B, C

**Concept:** Refragmentation retains original offsets and identity.

The first child starts at the parent's original offset 100. The second begins 200 bytes later, adding 200/8=25 to give 125, so A holds. The original MF=1 means later original-datagram data still exists after this parent; even its final child therefore keeps MF=1, proving B. The identification remains common to the original datagram, C. D incorrectly restarts the reference frame for offsets.

**Common misconception:** Clearing MF on the last child of a nonfinal parent fragment.

## Q16

**Correct answer:** 32

Each nonbase call creates two children with argument reduced by one. There are five branching levels before the leaves, giving2^5=32 base calls. The question asks only for leaves, not all63 invocations.

## Q17

**Correct answer:** B

A thread holding Y must already have acquired X, so two threads cannot split the locks in opposite acquisition orders. The common order excludes circular wait, proving B and disproving A. It gives neither equal waits nor absence of waiting, so C,D are false. Deadlock prevention is weaker than immediate access or fairness.

## Q18

**Correct answer:** 5 (exact)
**Concept:** Updating first and second moments.

The original sum is 50. The remaining sum is 4×11=44, so the removed observation is 6. The original sum of squares is 5(8+10²)=540. Removing 6² leaves 504. New variance is 504/4−11²=126−121=5.

**Common misconception:** Variance cannot be updated using only the mean without tracking the second moment.

## Q19

**Correct answer:** 2816
**Concept:** Cache addressing fields and metadata.

There are 4096/32=128 lines, requiring seven index bits. A line offset takes five bits. The tag therefore takes 32−7−5=20 bits. Adding valid and dirty bits gives 22 metadata bits per line, or 128×22=2816 bits overall.

**Common misconception:** Cache data capacity excludes tag and status storage unless explicitly stated otherwise.

## Q20

**Correct answer:** A

**Concept:** Microprogrammed versus hardwired control.

Stored control-word sequences characterize microprogramming, and altering them can alter sequencing, establishing A. Such a design still needs sequencing logic, refuting B. C incorrectly assigns microinstruction fetching to the hardwired design. The ISA need not expose internal control formats, refuting D.

**Common misconception:** Treating an instruction-set specification as a specification of internal control implementation.

## Q21

**Correct answer:** B

**Concept:** Probe-cycle length.

The visited slots are 1,5,9,3,7, then 1 again. The period is 10/gcd(10,4)=5. Hence B holds: empty even slots cannot be reached. A and C give incorrect period lengths. D is false because the arithmetic sequence is independent of table contents.

**Common misconception:** Assuming every nonzero step visits the entire table.

## Q22

**Correct answer:** A, B, D
**Concept:** Lossless decomposition and dependency preservation.

The intersection is B, which determines R2's attributes, so the decomposition is lossless. A→B is checkable in R1 and B→C in R2, preserving both. Each component's determinant is its key, so both are BCNF. In R, B does not determine A, and B→C violates BCNF. Thus A,B,D are true and C false.

**Common misconception:** A decomposition may improve normal form while also being lossless and dependency-preserving.

## Q23

**Correct answer:** 4

**Concept:** Element order in a multiplicative group.

Powers of 3 modulo 10 are 3,9,7,1. The first return to the identity is the fourth power, so the order is four.

**Common misconception:** Using the additive order instead of the multiplicative group operation.

## Q24

**Correct answer:** 2 (exact)

**Concept:** Operating Systems — CPU scheduling

A runs0–2, leaving5. B arrives with 4 and runs2–4, leaving2. C runs4–5 and completes; B resumes5–7 and completes; A runs7–12. Waiting times are A:12-0-7=5, B:7-2-4=1, C:5-4-1=0. Average=(5+1+0)/3=2.

**Common misconception:** Preemption compares remaining time, and waiting time includes intervals after preemption.

## Q25

**Correct answer:** B

**Concept:** Enumeration without an end-of-output signal.

A correct enumerator must eventually print every member and no nonmember; it need not announce exhaustion. It can keep testing strings forever after its last output, so B holds. A adds an unjustified termination test; C confuses enumeration duration with membership decidability; D is refuted by an enumerator that never prints.

**Common misconception:** Requiring finite languages to have enumerators that halt after their last member.

## Q26

**Correct answer:** 4

Concept: overlapping copies. The preserved source sequence 1,2,3,4 replaces positions 2,3,4,5, giving [1,2,1,2,3,4]. Position 5 contains four. A naive forward assignment loop would not implement the stated overlap-preserving semantics.

## Q27

**Correct answer:** 3

For a connected graph, m−n+1=1 independent cycle, consistent with the given unique cycle. Its four cycle edges are not bridges, because each has an alternative path around that cycle. Every other edge lies outside any cycle and is a bridge. Therefore7−4=3. Connectivity alone does not make all edges bridges.

## Q28

**Correct answer:** 60

The operands are24/16=1.5 and40/16=2.5. Their product is3.75, encoded with four fractional bits as3.75×16=60. Equivalently multiply the raw encodings and shift right by four:960/16=60. Raw multiplication initially doubles the fractional-bit count.

## Q29

**Correct answer:** A, C

**Concept:** Strict asymptotic domination.

f/g=(log₂n)/√n tends to zero. This proves f=o(g), hence also f=O(g), establishing C and A. The reciprocal ratio is unbounded, refuting B and Θ-equivalence in D.

**Common misconception:** Assuming a logarithmic factor exceeds every fractional power.

## Q30

**Correct answer:** 4

The empty word reaches(even,even), b reaches(odd,even), a reaches(odd,odd), and ab reaches(even,odd). All four states are therefore reachable. The two parities are not identical because b changes length without changing the a count.

## Q31

**Correct answer:** 3

The first assignment changes A.next to D. The second changes C.next to A. Starting from q=C, the reachable chain is C→A→D→NULL, containing three nodes. B still exists but is not reachable from q; changing a pointer does not delete a node or automatically reconnect every old predecessor.

## Q32

**Correct answer:** B
**Concept:** SSTF fairness under ongoing arrivals.

Repeated nearby requests can always offer a shorter seek than the distant request. The scheduler can keep choosing them forever, proving B. A's bound ignores future arrivals. C confuses local efficiency with fairness. D only resolves equal distances and cannot defeat strictly nearer arrivals.

**Common misconception:** A finite queue argument cannot establish starvation freedom under unbounded new arrivals.

## Q33

**Correct answer:** 11

For x=0, odd y can be1,3,5,7, giving4 choices with z determined. For x=1 the same four choices fit. For x=2, y may be1,3,5, giving3. Total4+4+3=11. The upper bound on x and parity condition prevent direct unrestricted stars-and-bars counting.

## Q34

**Correct answer:** 128

The /26 range64–127 is wholly inside the /25 range0–127. Their union is the larger range, with128 addresses. Adding the range sizes would double-count the overlap.

## Q35

**Correct answer:** 6
**Concept:** Involutions and cycle structure.

An involutive permutation has only cycles of length one or two. Choose the two fixed points in C(4,2)=6 ways; the remaining pair must be swapped, giving exactly one permutation for each choice. Total six.

**Common misconception:** The remaining nonfixed elements cannot independently choose their images in a permutation.

## Q36

**Correct answer:** A, B, C

**Concept:** Computer Organization and Architecture — Memory interfacing

The region is 0x8000–0xBFFF, so its upper two address bits are 10. A13:A12 enumerate the four 4 KiB subregions, and A11:A0 choose one of 4096 bytes in each chip. Hence A and B hold. Ignoring A14 enables both 0x8000–0xBFFF and 0xC000–0xFFFF; the chip and offset bits are unchanged when A14 flips, so each byte has two aliases, establishing C. In D, A0 is unused, so adjacent byte addresses have the same chip and local address. A12 also redundantly enters the chip's address and decoder, leaving parts inaccessible; one-to-one addressing fails.

- **A:** True: the upper bits 10 identify the 16 KiB window and the next two choose its four chips.
- **B:** True: B123−8000=3123 hexadecimal, giving bank 3 and offset 123.
- **C:** True: toggling the ignored A14 yields another enabled address for the same storage cell.
- **D:** False: ignoring A0 aliases every adjacent address pair.

**Common misconception:** Partial address decoding causes aliasing; chip capacity alone does not guarantee unique processor addresses.

## Q37

**Correct answer:** 16

A rounds to16KiB at[0,16), B to16KiB at[16,32), and C to32KiB at[32,64). Freeing A releases its16KiB block. Its buddy is B's occupied block, so no coalescence is possible. The largest satisfiable request is16KiB. Total free capacity and largest contiguous buddy block are not interchangeable.

## Q38

**Correct answer:** B, D

**Concept:** Engineering Mathematics — Propositional and predicate logic

1. E lets us follow an R-edge indefinitely from any vertex. Finiteness forces a repeated vertex, hence a directed cycle. Under T, a directed cycle yields a self-loop, contradicting I. Thus A and C have no finite nonempty model, irrespective of F.
2. B has a two-element model {u,v} with only R(u,v) and R(v,u). Every element has one successor; the relation is symmetric and irreflexive.
3. D has a singleton model {u} with R(u,u). It satisfies E, T and S; irreflexivity was not required.

- **A:** A finite successor chain repeats, and transitivity then violates irreflexivity.
- **B:** The two-element swap relation is a witness.
- **C:** Adding functionality cannot repair the E,T,I contradiction.
- **D:** The singleton reflexive relation is a witness.

**Common misconception:** Finiteness changes satisfiability: an irreflexive transitive relation can have successors everywhere on an infinite ordered domain.

## Q39

**Correct answer:** A, C

**Concept:** Finite binary expansions.

A reduced rational has a finite binary expansion exactly when its denominator is a power of two. 3/8=0.011₂ and 7/4=1.11₂ fit the stated precision, giving A,C. The reduced denominators of 1/10 and 1/3 contain odd factors, so B,D require infinitely repeating expansions.

**Common misconception:** Assuming every short decimal fraction is exact in finite binary precision.

## Q40

**Correct answer:** 11

**Concept:** Unspanned blocking factor.

A block has 1000−40=960 usable bytes, fitting floor(960/120)=8 records. Thus ceil(81/8)=11 blocks are needed.

**Common misconception:** Dividing total record bytes by raw block size without accounting for headers and unspanned records.

## Q41

**Correct answer:** 0

FIFO faults on A,B,C and D. The intervening A hit does not change insertion order; D evicts A. The final B is still resident, so FIFO has4 faults. The optimal policy also needs the four distinct pages at least once and can keep B when D arrives, attaining4. The difference is zero. A familiar trace need not exhibit a strict advantage for an optimal policy.

## Q42

**Correct answer:** A, B, D

F selects y when x=1 and z when x=0. Therefore the two cofactors agree exactly when y=z, proving A. Expanding B's product gives xy+(NOT x)z+yz; the consensus term yz is redundant, so B holds. C fails with x=0,y=1, where F=z. When y=NOT z, F equals z for x=0 and NOT z for x=1, hence F XOR z=x: D. Treating the selector as an ordinary OR input obscures these dependencies.

## Q43

**Correct answer:** 3

The distinct mapping keys are (A,4000), (B,4000), and (A,4001). Different servers do not create new mappings under the specified rule, and equal port numbers on different clients do not merge their keys. Therefore there are three mappings. This conclusion depends on the explicitly defined mapping policy, not on an assumed universal NAT policy.

## Q44

**Correct answer:** 1

Subtract the first equation from each of the other two: (t−1)y=1 and(t−1)z=1. For t≠1 these uniquely fix y,z and then x, so the system is consistent with a unique solution. For t=1 both equations demand0=1, making it inconsistent. Exactly one parameter value is inconsistent. The quantity s(t) equals1 whenever a solution exists and does not remove the contradictory exceptional case.

## Q45

**Correct answer:** A, B

Concept: CFG language and ambiguity. Productions create only a symbols, and repeated concatenation generates any number, including zero, so A holds. A tree for a can be wrapped as S→SS with one child deriving ε, repeatedly, producing infinitely many distinct trees; B holds. That also disproves C. An LL(1) grammar is unambiguous, and this grammar additionally has immediate left recursion, so D fails. Infinitely many derivations here correspond to genuinely different trees, not merely different expansion orders.

## Q46

**Correct answer:** 400

The receive window permits bytes1000 through2199 inclusive. The next unsent byte is1800, leaving400 bytes of receive-window space. The800 bytes already in flight leave1500−800=700 bytes of congestion-window allowance. Both limits apply, so the sender may add min(400,700)=400 bytes. Window sizes are limits on the relevant byte range or outstanding data, not quantities added independently.

## Q47

**Correct answer:** C

On()), the stack becomes empty after the prefix(), so the modified machine accepts before processing the remaining unmatched ')'. The original rejects that remaining pop. A,B are valid balanced strings accepted by both; D never empties after consuming a symbol and is rejected by both. Acceptance must account for the entire input.

## Q48

**Correct answer:** 0.1667 (accepted range 0.16665–0.16675)

Taylor expansion gives exp(x)=1+x+x²/2+x³/6+O(x4). Thus f(x)=1/2+x/6+O(x²), requiring f(0)=1/2 and giving derivative1/6. The continuous extension value and its derivative are different coefficients.

## Q49

**Correct answer:** 7

After push7, m=7. Push3 stores −1 and sets m=3; push5 stores5. Push−2 stores−7 and sets m=−2. Popping−7 returns−2 and restores m=2(−2)−(−7)=3. Popping5 returns5. Push1 stores−1 and sets m=1. Its pop returns1 and restores m=3; the next stored−1 pop returns3 and restores m=7. Returned values sum −2+5+1+3=7. Encoded negative entries are restoration information, not the logical popped values.

## Q50

**Correct answer:** B

**Concept:** Theory of Computation — Regular and context-free languages

A deterministic pushdown automaton can push a stack symbol on a and pop one on b, rejecting underflow. Its finite control also remembers the preceding symbol and whether its current run has length one or two; it rejects a third repetition. It accepts at end of input exactly when the stack is empty. Thus L is deterministic context-free.

To show nonregularity, consider the prefixes u_n=(aab)^n for n≥0. For distinct m,n, append v_n=(abb)^n. The string u_n v_n has no triple repetition, never underflows, and has net stack change n−n=0, so it lies in L. But u_m v_n has net stack change m−n≠0, so it cannot lie in L. Hence infinitely many prefixes are pairwise distinguishable by suffixes, and no finite automaton recognizes L. In particular, banning long runs does not bound stack depth: repeated aab blocks keep increasing it.

- **A:** False: (aab)^n raises the stack height without creating aaa or bbb; suffixes distinguish infinitely many such prefixes.
- **B:** True: finite control checks the run restriction while the deterministic stack checks balanced legal operations; the suffix argument proves nonregularity.
- **C:** False: the explicit deterministic push/pop construction handles both restrictions without guessing.
- **D:** False: a pushdown stack together with finite control can impose both restrictions simultaneously.

**Common misconception:** Bounding consecutive pushes does not bound total nesting depth when pushes can be interspersed with fewer pops.

## Q51

**Correct answer:** 1.75 (two decimals)
**Concept:** Short-circuit control flow and expected work.

P is always evaluated. Q is evaluated only if P is true, probability 1/2. R is evaluated only if P is true and Q false, probability 1/4. By adding indicator expectations, the mean is 1+1/2+1/4=1.75.

**Common misconception:** The last predicate is not reached merely because one of the earlier predicates is false; its exact path condition matters.

## Q52

**Correct answer:** 9

Concept: B+ splitting and root growth. Leaf splits occur on inserting 4,6,8,10,12, leaving six leaves [1,2],[3,4],[5,6],[7,8],[9,10],[11,12]. At insertion 10 the root first reaches five children and splits into two internal nodes with two and three children, under a new root. Insertion 12 increases the right internal node to four children without overflowing it. Total=6 leaves+2 internal children+1 root=9. A leaf split does not always create another root level.

## Q53

**Correct answer:** B

**Concept:** Directory-link count versus open references.

Removing the two links removes names but the open descriptor still keeps the file available. Closing the last descriptor then leaves no links or open references, permitting reclamation, B. A leaves both a link and an open reference; C and D do not remove the remaining reference.

**Common misconception:** Equating removal of a filename with immediate destruction of an open file's storage.

## Q54

**Correct answer:** A

Ratios are2,1.8,1.8. The heuristic takes the weight6 item, leaving4, so neither remaining item fits and its value is12. The two weight5 items fit together and yield18. A is correct; B reverses the values, C uses forbidden fractional items, and D ignores the initially fitting items. Fractional-knapsack exchange arguments do not automatically apply to indivisible items.

## Q55

**Correct answer:** B

**Concept:** Listening versus connected sockets.

Accept returns connected sockets with their own lifetimes. Closing the listening socket stops accepting new connections through it but does not itself close c1,c2, proving B and refuting A. No descriptor is automatically promoted to a listener (C), and the established connections retain separate byte streams (D).

**Common misconception:** Treating all accepted connections as the same socket as the listener.

## Q56

**Correct answer:** 24
**Concept:** Full binary recursion trees.

Every internal invocation has exactly two children; there are 13 unit-segment leaves. A full binary tree with L leaves has L−1 internal nodes, so there are 13+12=25 invocations and markers. In postorder the root emits last. Immediately before that final emission, the other 24 have been emitted.

**Common misconception:** Unequal split sizes change the shape but not the full-binary-tree leaf/internal-node identity.

## Q57

**Correct answer:** B

**Concept:** Dead results versus observable evaluation.

The unused store can be removed, but the device effect of the call must remain, B. A,C remove it; D duplicates it. Dead-variable reasoning does not license eliminating side effects.

**Common misconception:** Treating a dead destination as proof that the whole right-hand expression is dispensable.

## Q58

**Correct answer:** A, B, C
**Concept:** Lossless BCNF decomposition versus dependency preservation.

The intersection is A, which determines R1=AB, proving losslessness (A). R1 has key A; R2 has no nontrivial projected dependency with a non-superkey determinant, so both are BCNF (B). To refute preservation of BC→A, take R1={(1,b),(2,b)} and R2={(1,c),(2,c)}. Both obey their projected dependencies, but their join contains (1,b,c),(2,b,c), violating BC→A (C). A alone cannot determine C in the original schema, so it is not a key (D is false).

**Common misconception:** Losslessness and dependency preservation are different properties.

## Q59

**Correct answer:** 19

Concept: constrained selection. Nonadjacent pairs (1,3),(1,4),(1,5),(2,4),(2,5),(3,5) have costs at most seven and values 17,19,15,17,13,14 respectively. The maximum is 19 from jobs 1 and 4, whose cost is 4+3=7. Considering values alone could select an adjacent or over-budget pair.

## Q60

**Correct answer:** A, C

Both incoming definitions assign the same constant2, so their join retains x=2. The second condition is therefore true and z=7, proving A and C. The program does not assign y, so B is false. A join of equal constants preserves that constant, not the nonconstant value, making D false. Multiple reaching definitions are not by themselves evidence of varying values.

## Q61

**Correct answer:** B
**Concept:** A recurrence with dominant nonrecursive work.

Let f(n)=n²/log₂n. Relative to f(n), the next recursion level contributes 3f(n/2)/f(n)=(3/4)log₂n/(log₂n−1), which is bounded below one for all sufficiently large n. The levels therefore sum geometrically to Θ(f(n)); the finite last levels and leaf cost n^(log₂3) are lower order. B follows. A drops the denominator; C treats the leaves as dominant; D applies a boundary-case logarithmic accumulation that does not occur.

**Common misconception:** A logarithmic divisor does not automatically put a recurrence into the critical Master-theorem case.

## Q62

**Correct answer:** 3

Before rotation,20 is depth0;10,30 depth1;25,40 depth2;22,27 depth3. After rotation,30 is depth0;20,40 depth1;10,25 depth2;22,27 depth3. Exactly25,22,27 retain their depths, giving3. The middle subtree moves from being30's left subtree to20's right, and the root shift compensates for that reassignment.

## Q63

**Correct answer:** 1.6667 (accepted range 1.66665–1.66675)

P(N=2k+1)=2^{−(2k+1)} for k≥0. The odd probability is(1/2)/(1−1/4)=2/3. Conditional on being odd, K=(N−1)/2 has probabilities(3/4)(1/4)^k and mean(1/4)/(3/4)=1/3. Therefore E[N|odd]=1+2/3=5/3≈1.6667. Conditioning on parity changes the distribution and cannot be handled by rounding the unconditional mean.

## Q64

**Correct answer:** 1.5476 (range 1.54755–1.54765)

**Concept:** CPI improvement versus instruction-count expansion.

Old CPI is 1+0.04×40=2.6. New CPI is 1+0.01×40=1.4, but new instruction count is 1.2 times old. The time ratio is 2.6/(1.2×1.4)=65/42=1.547619…. Accepted range: 1.54755–1.54765.

**Common misconception:** Comparing CPIs without accounting for changed instruction count.

## Q65

**Correct answer:** A, B

The fixed bits yield a NOT c; b,d are absent because all their combinations are covered. Thus A,B are true and C false. Specified zeros cannot be included in a valid exact SOP group, making D false.

