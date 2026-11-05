# GATE CS 2027 — Full-Length Mock Test 079

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard (target)

## General Instructions

- Attempt the paper within 180 minutes.
- Q1–Q5 and Q11–Q35 carry one mark each; Q6–Q10 and Q36–Q65 carry two marks each.
- General Aptitude contributes 15 marks, Engineering Mathematics 13 marks, and core Computer Science 72 marks.
- MCQ: choose exactly one option. Incorrect one-mark MCQs lose 1/3 mark; incorrect two-mark MCQs lose 2/3 mark.
- MSQ: select all and only the correct options. There is no partial credit and no negative marking.
- NAT: enter the numerical answer at the stated precision. There is no negative marking.
- Unattempted questions receive zero. The answer key follows Question 65.

---

## Section A — General Aptitude

### Q1. [1 Mark] [MCQ]

Every one of twelve sampled buses on a route arrived late on a rainy morning. Which conclusion is supported without treating this sample as a proof about every bus?

A. Rain makes every bus on every route late.
B. The observations suggest lateness on this route under these conditions, but do not establish a universal rule.
C. No bus on this route can arrive on time in dry weather.
D. Rain is proven to be the only possible cause of lateness.

### Q2. [1 Mark] [MCQ]

A cube has six distinct face labels A,B,C,D,E,F. Three valid orientations are listed as (top, front, right): (A,B,C), (A,D,E), and (F,B,E). Which face is opposite B? Rotating the cube does not change its labels.

A. A  
B. C  
C. D  
D. E

### Q3. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Five consecutive readings should form a sequence whose consecutive differences increase by the same amount. The displayed readings are 3,8,16,25,41. Exactly one reading was copied incorrectly. What is the corrected value of that reading?

**Required precision:** Integer.

A. 54  
B. 14  
C. 28  
D. 27

### Q4. [1 Mark] [NAT]

The midpoints of the four sides of a12-by-8 rectangle are joined consecutively to form a quadrilateral. What is its area?

**Answer format:** Integer square units.

### Q5. [1 Mark] [MCQ]

Which sentence has correct subject–verb agreement?

A. Each of the reports have an appendix.
B. The list of required documents are on the desk.
C. Neither of the two proposed routes is suitable.
D. The results of the experiment indicates a change.

### Q6. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A shop expects unit sales to fall by 20% from last month. This month every item will also be sold at a 10% discount on its new sticker price; last month all items sold at their old sticker price. All items have the same price within each month. What percentage increase in sticker price is required to keep sales revenue unchanged? Round to two decimal places.

**Required precision:** Number to 2 decimal places, without the percent sign.

A. 38.89  
B. 77.78  
C. 19.45  
D. 39.89

### Q7. [2 Marks] [MCQ]

Each of four people is either a truth-teller, whose statement below is true, or a liar, whose statement is false. A says “B is a liar.” B says “C is a liar.” C says “D is a liar.” D says “A and B are both truth-tellers.” Which pair consists exactly of the truth-tellers?

A. A,B
B. A,C
C. B,D
D. C,D

### Q8. [2 Marks] [MCQ]

A point initially at (1,2,3) is first rotated 90 degrees about the z-axis by the rule (x,y,z)→(−y,x,z). It is then rotated 90 degrees about the x-axis by the rule (x,y,z)→(x,−z,y). What is the final point?

A. (−2,−3,1)
B. (−3,1,−2)
C. (2,3,1)
D. (−2,3,−1)

### Q9. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A researcher writes: “No failure was observed in a hundred trials. This excludes failure in those trials but does not establish that failure is impossible.” Which additional claim conflicts with that qualification?

A. The observed failure count was zero.  
B. The tested system may still fail in an untested situation.  
C. Future observations could require revising the assessment.  
D. A future failure is logically impossible solely because of these trials.

### Q10. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Four married couples sit around a circular table. All eight people are distinct; arrangements differing only by rotation are identical, but reflections are distinct. How many arrangements have no spouses adjacent?

**Required precision:** Integer.

A. 2976  
B. 744  
C. 1489  
D. 1488

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Among permutations π of {1,2,3,4,5}, how many satisfy π(1)≠1 and π(2)≠2? No restriction is placed on the other positions.

**Required precision:** Integer.

A. 156  
B. 78  
C. 39  
D. 79

### Q12. [1 Mark] [MSQ]

An even-parity bit is appended to each fixed-length data word. Which statements are correct?

A. Every single-bit error in the transmitted word is detected.
B. Every two-bit error is detected.
C. Some errors affecting the parity bit and one data bit are undetected.
D. Every odd number of flipped bits is detected.

### Q13. [1 Mark] [MCQ]

For Boolean variables x, y and z, let F=(x OR y) AND ((NOT x) OR z). Which expression is equivalent to F for every input?

A. (x AND z) OR ((NOT x) AND y)  
B. (x AND y) OR ((NOT x) AND z)  
C. y OR z  
D. x XOR y XOR z

### Q14. [1 Mark] [MCQ]

a0=0, a1=1 and a_n=3a_(n−1)−2a_(n−2) for n≥2. Which formal generating function equals Σ_(n≥0) a_n x^n?

A. 1/(1−3x+2x²)  
B. x/(1−3x−2x²)  
C. (1−x)/(1−2x)  
D. x/((1−x)(1−2x))

### Q15. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A file occupies eight data blocks. Its only directory link is removed while one process still has the file open. Assume blocks are reclaimed only when both link count and open-reference count become zero. How many of its data blocks are reclaimed by this unlink operation itself?

**Required precision:** Integer.

A. 1  
B. 2  
C. 0  
D. 3

### Q16. [1 Mark] [MSQ]

A process calls a blocking read on an empty pipe whose write end is still open elsewhere. No signal interrupts the call. Which statements are correct?

A. The process must consume a CPU core continuously until data arrives.
B. The operating system can deschedule the blocked process.
C. Another process can run on the same core while this process waits.
D. Empty at this instant necessarily means end-of-file.

### Q17. [1 Mark] [MCQ]

Over a nonempty domain, which formula is the negation of “For every x, if P(x), there exists y such that R(x,y)”?

A. For every x, P(x) and for every y, not R(x,y).
B. There exists x such that not P(x) and there exists y with R(x,y).
C. There exists x such that P(x) and for every y, not R(x,y).
D. There exists x such that P(x) and there exists y with not R(x,y).

### Q18. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

T1 holds an exclusive lock on x and requests y. T2 holds an exclusive lock on y and requests x. No locks are released until commit or abort. Which statements are correct?

**Candidates**

**I.** Both transactions can remain blocked indefinitely without intervention.

**II.** Aborting either transaction and releasing all its locks can allow the other to proceed.

**III.** Two-phase locking makes this wait cycle impossible.

**IV.** Both transactions must commit simultaneously to resolve it.

A. I and II  
B. II and IV  
C. III and IV  
D. I and III

### Q19. [1 Mark] [MCQ]

A scheduler assigns smaller numeric priority to more urgent jobs. Every waiting job's priority decreases by one per time unit, while a running job's priority is unchanged. Which problem is this aging rule principally intended to mitigate?

A. Deadlock caused by inconsistent mutex acquisition order.
B. Starvation of low-priority jobs under repeated arrivals of more urgent work.
C. Internal fragmentation in a page.
D. Loss of a dirty cache line during DMA.

### Q20. [1 Mark] [MCQ]

An LL(1) parser is built for S→A b, A→a A | ε. The stack top is A and lookahead is b. Which action is correct?

A. Consume b and retain A on the stack.
B. Apply A→ε without consuming input.
C. Apply A→aA.
D. Report an error because b is not in FIRST(aA).

### Q21. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A tree has eight vertices of degree 3, five vertices of degree 2, and all remaining vertices of degree 1. How many leaves does it have?

**Required precision:** Integer.

A. 10  
B. 20  
C. 5  
D. 11

### Q22. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A zero-indexed array A contains the permutation [2,0,4,1,3]. A separate array B of length five is filled by executing B[A[i]]=i for i=0,1,2,3,4. What is the value of B[B[0]] afterward?

**Required precision:** Exact integer.

A. 3  
B. 6  
C. 2  
D. 4

### Q23. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A DMA transfer completes while the CPU executes unrelated instructions. What mechanism can notify the CPU without requiring it to poll continuously?

A. A completion interrupt.  
B. Deleting every CPU register.  
C. Changing every virtual address to zero.  
D. Disabling the device permanently before completion.

### Q24. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Define f(x)=(e^x−1)/x for x<0, and f(x)=a+bx for x≥0. Which pair (a,b) makes f differentiable at 0?

A. (1,1/2)  
B. (0,1)  
C. (1,1)  
D. (1/2,1)

### Q25. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A complete DFA over {a,b} starts at p and accepts only in r or s. Its transition table is:

| State | a | b |
|---|---|---|
| p | q | r |
| q | p | s |
| r | r | r |
| s | s | s |

Which statements are correct?

A. All four states are reachable.  
B. p and q are distinguishable by some suffix.  
C. r and s are equivalent.  
D. The language is exactly the set of strings containing at least one b.

### Q26. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A doubly linked list has consecutive nodes A,B,C. Deleting B without a sentinel requires setting A.next=C and C.prev=A. How many pointer fields in the surviving nodes must change?

**Required precision:** Integer.

A. 4  
B. 1  
C. 2  
D. 3

### Q27. [1 Mark] [MSQ]

A dynamic array starts with capacity one. Appending to a full array allocates a new array of twice the capacity and copies all existing elements; other appends take constant time. Which statements hold over n appends starting empty?

A. The total copying work is O(n).
B. The total copying work is necessarily Θ(n log n).
C. A single append can take Θ(n) time when the current number of elements is proportional to n.
D. Every individual append has worst-case constant time.

### Q28. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A processor issues instructions out of order but commits their architectural results in program order using a reorder buffer. Which mechanism chiefly prevents a younger completed instruction from exposing its architectural result before an older faulting instruction is resolved?

A. In-order commit from the reorder buffer.  
B. Issuing every ready instruction as soon as possible.  
C. Increasing the number of execution units.  
D. Predicting every branch as taken.

### Q29. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For grammar A→Aa | Ab | c, which regular expression describes its language?

A. (a|b)*c  
B. c(a|b)*  
C. a*b*c  
D. c(ab)*

### Q30. [1 Mark] [NAT]

A byte-addressed machine fetches a four-byte branch instruction at address1000. Its eight-bit displacement field contains11111100. The processor sign-extends this field, multiplies it by4, and adds the result to the address immediately after the instruction. What is the target byte address?

**Answer format:** Exact integer.

### Q31. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A coin system has denominations1,3,4 and unlimited coins. For amount6, how many more coins does repeatedly taking the largest affordable denomination use than an optimal solution?

**Required precision:** Integer.

A. 2  
B. 1  
C. 0  
D. 3

### Q32. [1 Mark] [MCQ]

For L={a^n b^n : n≥0}, choose z=a^p b^p in a pumping-lemma argument, where p≥1. Which statement correctly addresses every decomposition z=uvw with |uv|≤p and |v|≥1?

A. v contains only a's, so removing v produces a string outside L.
B. v contains equal numbers of a's and b's, so repeating v stays in L.
C. Some suitable decomposition must be chosen by the person proving nonregularity.
D. The lemma allows v to be empty if u is nonempty.

### Q33. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A ternary ER relationship Assignment(Employee,Project,Role) records who fills each role on each project. Every (Project,Role) pair has at most one assigned employee. An employee may fill several roles on the same project, and may work on several projects. There are no other key constraints. Which statements hold?

**Candidates**

**I.** (Project,Role) is a candidate key of Assignment.

**II.** (Employee,Project) is necessarily a candidate key.

**III.** Two assignments with the same project and role but different employees violate the constraint.

**IV.** Replacing the relationship by Employee–Project alone preserves all assignment information.

A. III and IV  
B. I and III  
C. I and II  
D. I and IV

### Q34. [1 Mark] [MCQ]

A four-variable Boolean function F(A,B,C,D), with A as the most significant bit of the minterm index, is 1 at minterms 1,3,9,11. Minterms 0,2,8,10 are don't-cares, and all remaining minterms are 0. Which is a minimum-literal sum-of-products implementation?

A. NOT B  
B. NOT D  
C. A OR C  
D. (NOT B) AND D

### Q35. [1 Mark] [NAT]

In a simplified slotted contention scheme, two stations independently choose one of four slots uniformly and transmit once in that slot. A collision occurs if they choose the same slot. Given that station A chose a slot later than slot1, what is the collision probability?

**Answer format:** Exact decimal.

### Q36. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A circular queue uses an array of length5 and reserves one slot to distinguish full from empty. Initially front=rear=0. Three enqueues, two dequeues, and then three enqueues all succeed. Indices advance modulo5. What is rear after the last enqueue?

**Required precision:** Integer index.

A. 2  
B. 0  
C. 3  
D. 1

### Q37. [2 Marks] [MSQ]

A parent creates a pipe and forks one child. Both processes initially inherit both ends. The child reads until EOF. The parent writes a finite message, closes its own write descriptor, and waits for the child; the child has forgotten to close its inherited write descriptor. No other processes hold the pipe. Which statements are correct?

A. After draining the message, the child can block waiting for EOF.
B. The parent's close alone guarantees EOF at the child.
C. Closing the child's inherited write end before its read loop permits EOF once the parent's write end closes and buffered bytes are drained.
D. The parent waiting for the child automatically closes the child's descriptors.

### Q38. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An eight-bit ALU compares signed two's-complement operands A=0x80 and B=0x01 by computing A−B modulo 256. Let N be the result's sign bit, V the signed subtraction-overflow flag, and L the correct signed-less-than result. Which triple (N,V,L) is correct?

A. (1,0,1)  
B. (0,0,0)  
C. (1,1,0)  
D. (0,1,1)

### Q39. [2 Marks] [MSQ]

For L={aⁿbⁿ:n≥0}, choose w=aᵖbᵖ in a regular-language pumping-lemma proof, where p≥1. Which statements hold for every decomposition w=xyz with |xy|≤p and |y|>0?

A. y contains only a symbols.
B. Pumping y twice preserves equal numbers of a and b.
C. Pumping y zero times yields a word outside L.
D. The proof may choose a decomposition that violates |xy|≤p.

### Q40. [2 Marks] [MSQ]

An ordinary binary search tree stores distinct integers. A search for key 45 visits keys 50,20,40,47,45 in that order. Which additional statement is consistent with the BST search constraints?

A. The next node after 40 could instead have been 48.
B. The next node after 20 could instead have been 55.
C. Every node visited after 47 on this search must have key below 47 and above 40 until 45 is found.
D. The path is impossible because it changes direction more than once.

### Q41. [2 Marks] [MCQ]

A 4-to-1 multiplexer has select bits s1,s0 and data inputs D0=0,D1=x,D2=x′,D3=1. For which select settings is its output independent of x?

A. Only 00.
B. Only 11.
C. 00 and 11.
D. 01 and 10.

### Q42. [2 Marks] [MSQ]

X is uniform on {−1,0,1}, and Y=X². Which statements are correct?

A. Cov(X,Y)=0.
B. X and Y are independent.
C. E[Y]=2/3.
D. Knowing Y=0 determines X exactly.

### Q43. [2 Marks] [NAT]

A router knows an undirected network with edges AB=1, AC=4, BC=2, BD=5, CD=1. Using complete link-state information, what is the shortest-path distance from A to D?

**Answer format:** Integer.

### Q44. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

An IPv4 datagram has a20-byte header and1800 bytes of payload. It traverses a link with MTU620 bytes, then one with MTU420 bytes. All fragments use20-byte headers; fragments are not reassembled between links. Each router makes each nonfinal fragment as large as permitted by eight-byte alignment. How many fragments reach the destination?

**Required precision:** Integer.

A. 12  
B. 3  
C. 6  
D. 7

### Q45. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A microinstruction controls three mutually exclusive groups containing 5,3 and 9 signals respectively. In each group, at most one signal may be asserted, and “none” is also needed. A fully encoded design gives each group its own minimum-width binary field. There are also four independent control signals represented by one bit each. How many control bits are required, excluding sequencing and address fields?

**Required precision:** Integer.

A. 26  
B. 7  
C. 14  
D. 13

### Q46. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let u=(1,1,0)ᵀ, v=(1,0,1)ᵀ, P=uuᵀ/(uᵀu), and Q=vvᵀ/(vᵀv). Which statements are correct?

A. PQ has rank one.  
B. trace(PQ)=1/4.  
C. PQ is symmetric.  
D. The eigenvalues of PQ, counting multiplicity, are 1/4,0,0.

### Q47. [2 Marks] [NAT]

A rooted tree has root r with children a,b,c. Vertex a has two leaf children, b has one leaf child, and c is a leaf. How many different preorder sequences of vertex labels are possible if the order of children at every vertex may be chosen independently? All seven vertex labels are distinct.

**Answer format:** Exact integer.

### Q48. [2 Marks] [MSQ]

For a 0/1 knapsack with nonnegative integer capacity W and items of positive integer weights wi and positive values vi, let D[j] initially be zero for every 0 ≤ j ≤ W. Each item may be used at most once. Consider the update `D[j] = max(D[j], D[j-wi] + vi)` for j ≥ wi. Which statements are correct?

A. Processing each item once and scanning j downward from W to wi computes the maximum value for capacity W.  
B. Processing each item once and scanning j upward from wi to W always computes the same 0/1 optimum.  
C. With one item of weight 2 and value 3 and capacity 4, an upward scan produces D[4]=6.  
D. For a downward scan, immediately before updating D[j] for an item, D[j-wi] still excludes that item.

### Q49. [2 Marks] [MCQ]

A compiler analyzes `if (p) x=2; else x=3; y=x-x;`, with exact integer arithmetic and no aliases. Which statement distinguishes simple constant propagation from an algebraic simplification?

A. At the merge x is a single known constant 2.
B. A nonrelational constant-only analysis that evaluates operations only on constant operands may leave y unknown, while the identity x−x=0 proves y is zero.
C. y can equal 1 because x has two possible values.
D. Algebraic simplification is invalid because p is unknown.

### Q50. [2 Marks] [MCQ]

Two threads execute the following operations on atomic Boolean flags, initially false, under sequential consistency:

```text
Thread 0: flag0 = true; while (flag1) {} ; critical_section; flag0 = false;
Thread 1: flag1 = true; while (flag0) {} ; critical_section; flag1 = false;
```

Which assessment is correct?

A. Mutual exclusion can fail because both flags may be false at the start.
B. Mutual exclusion holds, but both threads can wait forever after setting their flags.
C. Both mutual exclusion and progress are guaranteed.
D. The algorithm implements strict alternation using a turn variable.

### Q51. [2 Marks] [NAT]

Let A=[[0,1],[−2,3]] and let v=(x,y)ᵀ satisfy x+y=6. The sequence A^n v must remain bounded as n tends to infinity. What is x?

**Answer format:** Exact number.

### Q52. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Two positive-edge-triggered D flip-flops store bits (q1,q0). At every active clock edge both are updated simultaneously according to q1(next) = q0 XOR q1 and q0(next) = NOT q1. The initial state is (0,0). What is the state after 2027 active clock edges?

A. (0,0)  
B. (0,1)  
C. (1,1)  
D. (1,0)

### Q53. [2 Marks] [MCQ]

A BST has root 40, with left child 20 and right child 60. Node 60 has left child 50; node 50 has left child 45; node 45 has right child 47. All unspecified child links are null. Delete key 40 by copying its inorder successor's key into the root and then removing the successor's original node, reconnecting that node's child if necessary. In the resulting tree, what are respectively the parent key of node 47 and the inorder successor key of 47?

A. (45,50)
B. (50,50)
C. (50,60)
D. (45,60)

### Q54. [2 Marks] [MSQ]

A total computable function maps every pair(machine M,input w) to a machine N that ignores its own input, simulates M on w and accepts if that simulation accepts. Which statements are correct?

A. If M accepts w, N recognizes all strings.
B. If M does not accept w, N recognizes the empty language.
C. A decider for whether N's language is empty would decide arbitrary machine acceptance.
D. The construction requires deciding whether M accepts w before producing N.

### Q55. [2 Marks] [NAT]

A complete DFA over {0,1} accepts exactly the strings that end in 01. What is the minimum number of states in such a DFA?

**Answer format:** Integer.

### Q56. [2 Marks] [MCQ]

Over a finite candidate relation C(x) and a finite required relation S(y), query Q selects candidates satisfying FOR ALL y(S(y) IMPLIES R(x,y)). Query P instead requires FOR ALL y(S(y) AND R(x,y)), where the quantified domain is infinite and S is finite. Which statement holds when S is empty and C is nonempty?

A. Both queries return C.
B. Q returns C, while P returns no candidates.
C. Q returns no candidates, while P returns C.
D. Both queries return no candidates.

### Q57. [2 Marks] [MSQ]

A function f is continuously differentiable on [0,1], with f(0)=0, f(1/2)=2 and f(1)=1. Which statements must hold?

A. f′ equals 4 somewhere in (0,1/2).
B. f′ is positive throughout (0,1).
C. f′ equals −2 somewhere in (1/2,1).
D. f′ equals zero somewhere in (0,1).

### Q58. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A router uses longest-prefix matching with routes 10.0.0.0/8→A, 10.1.0.0/16→B, 10.1.128.0/17→C, and 10.1.192.0/18→D. Only the /17 route is withdrawn. Which next hops are then used for 10.1.160.1 and 10.1.200.1, respectively?

A. (A,A)  
B. (C,D)  
C. (B,B)  
D. (B,D)

### Q59. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

In the code below, execution starts at line1 and exits after line6. Only z is observed on exit. Expressions have no side effects.

```text
1: x = 1
2: if flag goto 5
3: y = x + 1
4: goto 6
5: y = 4
6: z = y
```

Which statements are correct about ordinary may-liveness analysis?

**Candidates**

**I.** x is live immediately after line2.

**II.** x is live immediately before line5.

**III.** y is live immediately before line6.

**IV.** Line1 is dead because one path does not use x.

A. II and III  
B. I and III  
C. II and IV  
D. III and IV

### Q60. [2 Marks] [NAT]

A byte-addressed device has256 byte locations. Its chip-select decoder matches address bits15–12 to1010, while address bits11–8 are ignored; bits7–0 address the device. Within the16-bit address space, how many distinct CPU byte addresses alias device offset0x35?

**Answer format:** Integer.

### Q61. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A comparison tournament finds the largest of seven distinct keys using six comparisons. The eventual winner received one initial bye and participated in exactly two comparisons. Using only the recorded results plus further key comparisons, what is the minimum total number of comparisons, including the original six, sufficient to identify both the largest and second-largest keys in the worst case under this condition?

**Required precision:** Integer.

A. 14  
B. 4  
C. 7  
D. 8

### Q62. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A DFS of a directed graph has discovery/finish intervals u:[2,11] and v:[4,7]. Edge u→v exists but is not a tree edge. How is it classified under standard DFS edge categories?

A. Back edge.  
B. Forward edge.  
C. Cross edge.  
D. Impossible because intervals may never nest.

### Q63. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An algorithm for a directed acyclic graph computes longest paths by processing vertices in topological order and relaxing outgoing edges using maximum instead of minimum. Edge weights may be negative. Which statement is correct?

A. Negative edges invalidate this dynamic program even in a DAG.  
B. A topological order ensures all predecessors are processed before a vertex, so the recurrence is valid.  
C. The algorithm requires all paths to have the same number of edges.  
D. The graph must first be converted to an undirected graph.

### Q64. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Sales(dept,amount) contains (A,10),(A,NULL),(A,20),(B,NULL),(B,NULL),(C,5). Standard SQL NULL and aggregate semantics apply. Consider:

```sql
SELECT dept, SUM(amount) AS total
FROM Sales
GROUP BY dept
HAVING COUNT(*) > COUNT(amount) AND SUM(amount) > 10;
```

Which statements are correct?

A. The query returns exactly one row.  
B. The row for A has total 30.  
C. The query returns B with total 0.  
D. Replacing COUNT(amount) in the HAVING clause by COUNT(*) makes the result empty.

### Q65. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A grammar has S→ABA, A→a | ε, B→b | ε. When eliminating epsilon productions, form S's nonempty right-hand sides by independently retaining or omitting nullable occurrences in ABA, then remove duplicate right-hand sides. How many distinct nonempty right-hand sides result for S?

**Required precision:** Integer.

A. 12  
B. 3  
C. 6  
D. 7

## ANSWER KEY — MOCK TEST 079

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | B |
| 2 | MCQ | 1 | C |
| 3 | MCQ | 1 | D |
| 4 | NAT | 1 | 48 |
| 5 | MCQ | 1 | C |
| 6 | MCQ | 2 | A |
| 7 | MCQ | 2 | B |
| 8 | MCQ | 2 | A |
| 9 | MSQ | 2 | A, B, C |
| 10 | MCQ | 2 | D |
| 11 | MCQ | 1 | B |
| 12 | MSQ | 1 | A, C, D |
| 13 | MCQ | 1 | A |
| 14 | MCQ | 1 | D |
| 15 | MCQ | 1 | C |
| 16 | MSQ | 1 | B, C |
| 17 | MCQ | 1 | C |
| 18 | MCQ | 1 | A |
| 19 | MCQ | 1 | B |
| 20 | MCQ | 1 | B |
| 21 | MCQ | 1 | A |
| 22 | MCQ | 1 | A |
| 23 | MSQ | 1 | B, C, D |
| 24 | MSQ | 1 | B, C, D |
| 25 | MCQ | 1 | B |
| 26 | MCQ | 1 | C |
| 27 | MSQ | 1 | A, C |
| 28 | MSQ | 1 | B, C, D |
| 29 | MSQ | 1 | A, C, D |
| 30 | NAT | 1 | 988 |
| 31 | MCQ | 1 | B |
| 32 | MCQ | 1 | A |
| 33 | MCQ | 1 | B |
| 34 | MCQ | 1 | A |
| 35 | NAT | 1 | 0.25 |
| 36 | MCQ | 2 | D |
| 37 | MSQ | 2 | A, C |
| 38 | MSQ | 2 | A, B, C |
| 39 | MSQ | 2 | A, C |
| 40 | MSQ | 2 | A, C |
| 41 | MCQ | 2 | C |
| 42 | MSQ | 2 | A, C, D |
| 43 | NAT | 2 | 4 |
| 44 | MCQ | 2 | C |
| 45 | MCQ | 2 | D |
| 46 | MCQ | 2 | C |
| 47 | NAT | 2 | 12 |
| 48 | MSQ | 2 | A, C, D |
| 49 | MCQ | 2 | B |
| 50 | MCQ | 2 | B |
| 51 | NAT | 2 | 3 |
| 52 | MSQ | 2 | A, B, D |
| 53 | MCQ | 2 | B |
| 54 | MSQ | 2 | A, B, C |
| 55 | NAT | 2 | 3 |
| 56 | MCQ | 2 | B |
| 57 | MSQ | 2 | A, C, D |
| 58 | MSQ | 2 | A, B, C |
| 59 | MCQ | 2 | B |
| 60 | NAT | 2 | 16 |
| 61 | MCQ | 2 | C |
| 62 | MSQ | 2 | A, C, D |
| 63 | MSQ | 2 | A, C, D |
| 64 | MCQ | 2 | C |
| 65 | MCQ | 2 | C |
