# Worked Solutions — Mock Test 036

## Q1

**Correct answer:** 68

The block of 13s ends at 13×14/2=91, and starts after position 78. Thus positions 90,91 contain 13, while 92,93,94 contain 14. Their sum is 2×13+3×14=68. A boundary-crossing sum cannot be obtained by treating all five entries as one block.

## Q2

**Correct answer:** B

The circumference difference is 2π(r+1)−2πr=2π metres. Advancing the outer start by that distance leaves equal distances to the common finish. Equal speeds then give equal finish times. A uses only half the difference; C and D depend on the unspecified radius and do not equal the difference in general.

## Q3

**Correct answer:** C

In C, the introductory phrase modifies the subject technician, assigning the haste correctly. A grammatically attaches the introductory modifier to instrument; D explicitly describes the instrument as hurried. B's wording is unnatural and does not correctly express the intended modifier relationship. A human performer should be the subject governed by this introductory phrase.

## Q4

**Correct answer:** 20

The multiplier is (1+p/100)(1−p/100)=1−p²/10000=0.96. Hence p²=400 and the stipulated positive p is 20. Equal percentage changes in opposite directions do not cancel because the second uses the changed base.

## Q5

**Correct answer:** A, C

Signed implies archived, which implies not editable, proving A. An editable form exists and cannot be signed, proving C. Unsigned forms need not be editable: an unsigned archived form is consistent with all premises, refuting B. Nothing requires any signed form, so D is not entailed. Universal statements alone do not establish existence.

## Q6

**Correct answer:** A

Reflection sends (x,y) to (y,x); clockwise rotation sends (u,v) to (v,−u). The composition is (x,−y), reflection in the x-axis. Thus A works for every point. B sends Q to (−2,0), C also sends Q to (−2,0), and D moves the origin; all conflict with the actual final positions. The order of transformations matters.

## Q7

**Correct answer:** B, D

The closure can redirect readers, so B is a plausible contributor, not an established cause. Sampling only voluntary evening visitors leaves other users' views unconstrained, giving D. A claims a uniquely identified cause despite the simultaneous change. C incorrectly generalizes a selected sample to all residents. Evidence of perceived usefulness among respondents does not by itself establish population-wide opinion or causality.

## Q8

**Correct answer:** 15

Separate cases according to C's group. If C is with A, choose their third member from D,E,F in three ways; C is that group's leader and the other group has two eligible leaders because B is excluded, giving 6 assignments. If C is with B, choose their third member in three ways; C leads that group and any of the three members of A's group may lead it, giving 9. Total 6+9=15. Distinguishing the groups by whether they contain A or B counts every unlabelled partition once, so no further division by two is needed.

## Q9

**Correct answer:** 40

Period 1 succeeds in (81+2)/(90+10)=83% of attempts. Period 2 succeeds in (19+24)/(20+80)=43%. The decrease is 40 percentage points, although East rises from 90% to 95% and West from 20% to 30%. More attempts shifted to the lower-success branch. Averaging the branch percentages equally would ignore their changing weights.

## Q10

**Correct answer:** 6

The punch at x=4 lies on the vertical fold, so unfolding in x does not produce two distinct centres. Reflection in y gives centres (4,1),(4,7), two holes. The other punch produces (2,2),(6,2),(2,6),(6,6), four holes. All six are separated by far more than twice the radius. Counting every punch as four holes double-counts centres fixed by a fold reflection.

## Q11

**Correct answer:** 2

The physical byte is selected by A0…A12, and the enabled region fixes A15,A14. Only A13 is free, giving two addresses per chip byte, separated by 8192. Partial decoding creates aliases rather than extra physical storage.

## Q12

**Correct answer:** B

The old sum is 5×12=60; the new mean is (60+100)/6=80/3. The old median fixes the third ordered observation but not the fourth, and appending 100 does not fix a unique new median. For example [0,0,10,20,30] and [5,5,10,15,25] meet the premises but give different new medians, ranges and variances. Therefore A,C,D are not determined; B is.

## Q13

**Correct answer:** A, C

Matrix multiplication gives (M²)[u,u]=Σ_v M[u,v]M[v,u], counting return walks of length two, so A. Transposition interchanges source and destination, proving C. Each directed edge contributes one entry, not two, disproving B. Opposite edges u→v and v→u give a positive diagonal in M² without self-loops, refuting D.

## Q14

**Correct answer:** C

The owner key distinguishes loans; the partial key distinguishes installments of a given loan. Their pair identifies each installment, so C. A collides across owners; B collides among installments of one owner. Amount need not be unique at either level, so D fails. A weak entity's partial key is interpreted within its owner.

## Q15

**Correct answer:** A, C

Division requires every B value in S for a selected A. Initially only 1 has both x and y, while P={1,2}, proving A and refuting B. Adding (2,y) makes both A values qualify, proving C. If S becomes {x}, both already have x, so D is false. Division expresses a universal matching condition.

## Q16

**Correct answer:** B

Let initial a=a0 and b=b0. Then t=a0+b0, and the increment makes the last expression a0+1+b0=t+1. B is valid. A omits the increment; C subtracts instead of adding; D omits a0. The expression text repeats, but a's changed value prevents direct reuse of t without adjustment.

## Q17

**Correct answer:** A, B

A spanning tree must connect v, and e is its sole possible connection. Thus every spanning tree, including every minimum one, contains e. C is false because a mandatory bridge can have any weight. Removing e isolates v, refuting D. The bridge argument does not depend on distinct or positive weights.

## Q18

**Correct answer:** 4

Successive powers modulo 10 are 2,4,8,6. The first identity value 6 occurs at exponent 4. The identity of this group is 6 rather than the integer 1; using the ambient multiplication identity would incorrectly suggest no finite order.

## Q19

**Correct answer:** A

The initial in matches the keyword and identifier patterns at equal length, so priority makes it a keyword. The dot is its own token. The entire inner is a five-letter identifier, longer than the keyword prefix in; longest match therefore selects the identifier. A is correct. B and D ignore keyword priority for the first token. C incorrectly lets keyword priority override a longer identifier match. Priority resolves ties only after maximal length is determined.

## Q20

**Correct answer:** A, C

Simulating at most k transitions decides both bounded questions, with the initial-state acceptance test included for C. The computation is finite even when M would run forever. B is the unrestricted halting problem; D is the general Turing-machine language-emptiness problem. Both are undecidable. A finite bound changes the decision problem fundamentally.


## Q21

**Correct answer:** 2

Each triangle is an odd cycle and requires one of its own edges removed. The triangles have disjoint edge sets, so at least two removals are necessary. Removing one edge from each leaves two paths joined by a bridge, a tree, which is bipartite. Thus the lower bound is achievable. Removing the connecting bridge alone leaves both obstructions.

## Q22

**Correct answer:** A, D

Every bit flip toggles overall parity. An odd number of flips gives odd received parity, detecting A and D. An even number preserves even parity, so B and C are undetected by this check. The parity bit itself is not exempt from the same toggling argument.

## Q23

**Correct answer:** 3

Simultaneous transitions are 00→01→10→00. Thus the first return takes three edges. The next-state equations use the old bits; updating one bit first and then using its new value would model a different circuit.

## Q24

**Correct answer:** B

Unlink removes a directory entry and decrements the link count. The open reference still keeps the file accessible through d after the count reaches zero. Final reclamation occurs after that reference is closed, so B. A ignores the open reference; C invents a pathname; D confuses independent directory entries with their common target.

## Q25

**Correct answer:** B

The source address establishes A's location on incoming port 1. B's destination location is unknown, so the frame floods out the other two ports. B is correct. A learns the destination from the wrong evidence; C assigns the wrong source port; D assumes the destination's physical location can be learned merely from its address in this frame.

## Q26

**Correct answer:** A, C

The direct path costs 2, while s→b→a costs 5−4=1, proving A. Settling a at 2 before exploring b can prevent correction, proving C. The graph is acyclic, refuting B. Its shortest path to a has two edges despite an available one-edge path, refuting D. Negative edges, even without a negative cycle, invalidate the usual Dijkstra settling guarantee.

## Q27

**Correct answer:** 16

Every binary word can be split into initial a's followed by zero or more blocks consisting of b and the run of a's immediately after it. Thus the expression denotes all words over {a,b}, and there are 2^4=16 length-four words. Repeated stars do not impose a limit on the number of b's.

## Q28

**Correct answer:** C

Before failure, routes through U and V cost 2+7=9 and 5+3=8. After V is unavailable, the only remaining candidate is 9 through U. C follows. A omits the local link; B retains the failed route; D overlooks U's valid advertisement.

## Q29

**Correct answer:** 1.25

The stored integers are 46 and 28. Their sum 74 wraps modulo 64 to 10, which decodes as 10/8=1.25. The exact numerical sum is 9.25, outside the format's maximum 63/8. Wraparound is neither saturation nor rounding.

## Q30

**Correct answer:** 16

Choose one of {1,2} in two ways. The remaining four elements must contribute odd cardinality, giving C(4,1)+C(4,3)=8 choices. Total 2×8=16. Even total size requires odd size in the remaining subset because one element is already included.

## Q31

**Correct answer:** A, C

A strict greater-than shift never moves an equal predecessor past the key, so A holds. On sorted input no predecessor exceeds its key, proving C. A non-strict comparison can move equal records past each other, disproving B. Shifts correspond to strict inversions; distinct descending records already disprove D. Equality is crucial to stability but not to the shift count claimed in D.

## Q32

**Correct answer:** 11

Rearranging gives a(n)−a(n−1)=a(n−1)−a(n−2), so every first difference is 2. Therefore a(n)=1+2n and a5=11. By the definition of the ordinary generating function, the requested coefficient is precisely a5. The recurrence's repeated root leads to linear, not exponential, growth.

## Q33

**Correct answer:** C

Normalize the original time to 1. The new time is 1/2+(1/2)/2=3/4, so speedup is 1/(3/4)=4/3. A incorrectly halves all time; B confuses a time reduction with a speedup factor; D ignores the improved component. The unaffected fraction bounds the benefit.

## Q34

**Correct answer:** B, C

A blocking operation can suspend the caller, making the core available to another runnable process; B and C hold. The caller need not busy-wait, so A is false. An empty pipe with a writer still open may later receive data; emptiness alone does not establish EOF, refuting D.

## Q35

**Correct answer:** 21

The parameter p is a copy of the caller's pointer. Inside change it advances from a+1 to a+3 and replaces a[3] by a[2]+a[3]=7+9=16. The caller's p still points to a[1], whose value is 5. Thus the print computes 5+16=21. Passing a pointer by value permits mutation of its target but does not permit rebinding the caller's pointer through the local parameter alone.

## Q36

**Correct answer:** 2

The first symbol forces the production aSbS. Its displayed b can match the second or fourth symbol of abab. Matching the second leaves the inner S empty and the final S generating ab. Matching the fourth leaves the inner S generating ba and the final S empty. Each two-letter substring has one derivation, and the empty substring must use ε. Thus there are exactly two leftmost derivations. Different orders of expanding nonterminals are excluded by the leftmost requirement.

## Q37

**Correct answer:** 32

Descent increments the shared x three times, from 1 to 4. The base call returns 4. Each returning frame receives the current x as a and adds it to the same shared x, doubling it: 4→8→16→32. The final return is also 32. Treating x as a separate local copy per call would ignore reference semantics.

## Q38

**Correct answer:** A, C

The probes are 0,1,4,2,2,4,1. Four distinct slots are reachable, so the first four insertions succeed and the fifth fails despite three unused slots. This proves A and refutes B. Slot 3 is never probed, proving C. Linear probing visits all seven slots and permits seven insertions, so D is false. Table occupancy alone does not ensure a restricted probe sequence finds an empty slot.

## Q39

**Correct answer:** 1

At magnitude 8, representable values immediately around 9 are 8 and 10. The midpoint rounds to 8 because its final significand bit is even. Thus fl(fl(8+1)−8)=0. On the other grouping, 1−8=−7 is exactly representable with three significant bits, and 8−7=1 is exact. The requested difference is 1−0=1. Rounding after intermediate operations breaks associativity.

## Q40

**Correct answer:** 0.25

Absorption gives F=a OR (b AND c), whereas G=a AND (b OR c). If a=0, the outputs differ exactly at b=c=1. If a=1, they differ exactly at b=c=0. These are two of eight equally likely inputs, so the probability is 1/4. Distributing one expression does not make the two circuits identical.

## Q41

**Correct answer:** A, B, D

A has (i,j,k)=(2,2,3), so its first branch accepts. B has (2,3,3), so its second accepts. D has (1,1,1), so both accept. C has (3,1,2), satisfying neither equality, and is rejected. Nondeterministic choice gives a union, not an intersection of the branches' languages.

## Q42

**Correct answer:** 400

The first link produces payloads of 1000 bytes each, at offsets 0 and 125; 1000 is divisible by 8. At the second link each splits into 600 and 400 bytes, both respecting the nonfinal alignment. Relative to the original payload, starts are 0,600,1000,1600 bytes, hence offset fields 0,75,125,200. Their sum is 400. Offsets are not restarted at zero when an existing fragment is fragmented again.

## Q43

**Correct answer:** A, C, D

The unrestricted complement contains domain elements absent from R. It is {3} in the first domain, proving A, and {3,4} in the second, refuting B. Changing the ambient domain changes the answer without changing R, proving C. The contradictory bounded formula in D returns nothing over any domain, so D holds. Negation without a suitable range restriction can introduce domain dependence.

## Q44

**Correct answer:** 174

Represent R as a 3×3 Boolean matrix. The first formula says every row is nonempty, giving 7³ matrices. The second forbids a column of three ones. For a specified all-one column, each row's other two entries are free, giving 4³ matrices; for two specified all-one columns there are 2³; for all three there is one. Inclusion-exclusion yields 7³−3×4³+3×2³−1=174. The two quantifier orders impose distinct row and column conditions.

## Q45

**Correct answer:** A, B, C

After b, the relevant items include S→b·Ac, S→b·da, and A→·d. Shifting d gives the two LR(0) items in A. FOLLOW(A)={a,c}, so SLR reduces A→d on a while S→bd·a shifts a: B holds and D fails. In canonical LR(1), A was introduced here only by S→b·Ac, so its lookahead is c. Reducing on c and shifting on a are compatible, establishing C. FOLLOW merges contexts that LR(1) lookaheads keep separate.

## Q46

**Correct answer:** 0.6875

For Y=10, Y.val=1/2+0/4=1/2 and Y.len=2. For Z=11, Z.val=1/2+1/4=3/4. Concatenation shifts Z's fraction right by Y.len places: X.val=1/2+(3/4)/4=11/16=0.6875. Using Z.len in this shift happens to match here but is not the stated general rule; the preceding prefix length determines placement.

## Q47

**Correct answer:** 4

Track (main,victim). A reads memory and gives (A,empty). B reads memory and gives (B,A). A hits the victim and swaps to (A,B). C misses both, reads memory, and gives (C,A), discarding B. Finally B misses both again and reads memory. Four memory reads occur. A victim-cache hit is a swap rather than an additional memory fetch.

## Q48

**Correct answer:** A, B

For any w of length n, h(ww)=0^(2n), and every n≥0 occurs. Thus h(L)=(00)*, proving A and B. The image has only even lengths, so D is false. C is disproved by this very regular image: a many-to-one homomorphism can erase the distinguishing information responsible for non-context-freeness.

## Q49

**Correct answer:** A, B

For id=1 only employee 11 passes the ON condition; both counts are 1. For id=2 the left join supplies one NULL-extended row. COUNT(*) counts it, while COUNT(E.eid) ignores its NULL, yielding n=1,m=0. Hence A,B are true and D false. Moving the active filter to WHERE rejects that NULL-extended row, removing id=2 and disproving C. Filtering matches and filtering the joined result have different effects on outer joins.

## Q50

**Correct answer:** 64

R directly handles last octets 0–127. S directly handles 192–255 after R forwards them. Addresses 128–191 match neither connected prefix, so R and S repeatedly apply their defaults to each other. There are 192−128=64 such addresses. Prefix coverage, not the mere presence of a default route, determines whether forwarding makes progress.

## Q51

**Correct answer:** A, B, C

With b=c=0 the expression is a AND NOT a, always 0, proving A. During a transition, the direct and inverted paths can temporarily make both OR outputs 1, proving B. By the consensus theorem, (a+b)(NOT a+c) already implies (b+c), so adding that factor preserves the truth table. When b=c=0 the added factor remains 0 and blocks the glitch, proving C and refuting D. A redundant Boolean factor can be physically useful for hazard suppression.

## Q52

**Correct answer:** A, B, C

The third left-hand side is the sum of the first two, requiring t=3. The first two rows are independent, leaving one free variable when consistent. Subtracting twice the first equation from the second gives −x1+x3=0. Equivalently, solutions are (s,1−2s,s) for arbitrary real s. Thus A,B,C hold. Rank is 2, not 3, so D is false.

## Q53

**Correct answer:** 3

The distinct mapping keys are (A,4000), (B,4000), and (A,4001). Different servers do not create new mappings under the specified rule, and equal port numbers on different clients do not merge their keys. Therefore there are three mappings. This conclusion depends on the explicitly defined mapping policy, not on an assumed universal NAT policy.

## Q54

**Correct answer:** 1

Static links follow R→Q→P, two traversals. Dynamic links follow the actual call chain R→Q→S→P, three traversals. The difference is one. Calling Q from S does not make S the lexical parent of Q.

## Q55

**Correct answer:** 2

The first timer starts at 0 and expires at 10, after completions at 0,3,6,9: four completions, below threshold 8. The next timer starts at 12 and expires at 22, again with four completions. The next starts at 24 and would expire at 34. Therefore only interrupts at 10 and 22 occur by time 30. No completion counter reaches 8 first.

## Q56

**Correct answer:** 3

The first fork yields a parent with x=0 and child with x=1. Only the x=0 parent executes the second fork, producing one additional process. Each of the resulting three processes reaches the print once. Private x values prevent the first child's assignment from suppressing the parent's second fork.

## Q57

**Correct answer:** A, B

For each i the inner loop visits i,2i,…,floor(n/i)i, proving A. The total is bounded above by nH_n and below by nH_n−n, hence Θ(n log n), proving B and refuting D. Only loop counters and constant-size state are needed; no array of iterations must be stored, so C is false. Counting the inner loop as n iterations independently of its stride overestimates the work.

## Q58

**Correct answer:** B

At endpoint 0 choose [0,6], which extends farther than [0,4]. At endpoint 6, [6,9] extends farther than [3,8]. At endpoint 9 choose [8,10], reaching the target; B is the stated sequence. A starts with a nongreedy choice even though it also covers the target. C leaves (6,7) uncovered, and D leaves (4,7) uncovered. A later interval cannot repair an earlier uncovered gap under this covering rule.

## Q59

**Correct answer:** A, B, C

The two expressions cross at x=±1. For |x|≤1 the minimum is x²; outside it is 2−x². Thus maximum 1 occurs at ±1, and minimum −2 at endpoints ±2, proving A,B. Near 0 the function is the polynomial x² and differentiable, proving C. At 1 the left derivative is 2 and right derivative −2, refuting D. Continuity at a branch crossing does not imply differentiability.

## Q60

**Correct answer:** A, C

EOF requires no write descriptors remain open and all buffered bytes are consumed. The child itself retains an open write end, so it can block after reading the message, proving A and refuting B. Closing that unused end removes the obstacle; after the parent's close and buffer drain, EOF can occur, proving C. Waiting does not close another process's descriptors, refuting D. The parent's wait can therefore participate in a hang caused by inherited descriptor ownership.

## Q61

**Correct answer:** 4

The cycles are (0), (1,2,4,8), (3,6,12,9), (5,10), and (7,14,13,11). Only (0) is a fixed point, leaving four nontrivial cycles. Each index appears once because multiplication by 2 is invertible modulo 15. Counting moves or moved elements would give a different quantity from the number of cycles.

## Q62

**Correct answer:** B, C, D

If both threads read the same value before either writes at each round, updates are lost and the final value is 2. Serial execution gives 4. For 3, let both first reads see 0, let both write 1, then execute each second increment serially. These establish B,C,D. Every second write is based on a read after that thread's first write; all first writes are at least 1 and no later write can be 0. Hence every second write is at least 2. A final value 1 is impossible because the last write belongs to a thread's second increment. Atomic individual accesses do not make the increment atomic.

## Q63

**Correct answer:** 11

Four retired instructions require 4+4=8 cycles without penalties. The load-use dependence adds one and the taken branch adds two, giving 11. The stated forwarding rule prevents another stall between the ALU instruction and branch. Wrong-path work is already represented by the two-cycle penalty, so it must not be counted again as retired instructions.

## Q64

**Correct answer:** 21

After t advances, slow is t links from the head and fast 2t. Once both are in the cycle, coincidence requires t divisible by 5. The first such t with t≥3 is 5, so phase one traverses 5+10=15 links. Resetting slow and advancing both requires three steps to the entry, contributing 3+3=6 traversals. Total 21. Resetting does not itself follow any next link.

## Q65

**Correct answer:** 0.3210 (accepted range 0.32095–0.32105)

Of 27 equally likely ordered draws, 3 have one distinct colour and 6 have all three; the remaining 18 have exactly two. Therefore E[D]=(3+36+18)/27=19/9 and E[D²]=(3+72+54)/27=43/9. Variance is 43/9−(19/9)²=26/81≈0.32098765, rounding to 0.3210. The number of distinct colours is not binomial because colour-presence indicators are dependent.


