# GATE CS 2027 — Full-Length Mock Test 006

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

- Q1–Q5 and Q11–Q35 carry one mark each. Q6–Q10 and Q36–Q65 carry two marks each.
- MCQ: exactly one of four options is correct. Incorrect answers attract −1/3 mark for a one-mark question and −2/3 mark for a two-mark question.
- MSQ: more than one option is correct. Select all and only the correct options; there is no partial credit or negative marking.
- NAT: enter a number at the stated precision. There is no negative marking. Unattempted questions of any type receive zero.
- General Aptitude carries 15 marks, Engineering Mathematics 13 marks, and core Computer Science 72 marks.
- Unless specified otherwise, pseudocode uses exact integers; graphs are finite; no implicit concurrency, I/O, overflow, or rounding is assumed.

---

## Section A — General Aptitude

### Q1. [1 Mark] [MCQ]

A notice reads: “Only registered participants may enter the laboratory. Registration does not reserve a laboratory seat.” Which statement follows from the notice?

A. Every registered participant is guaranteed a seat.
B. A person allowed to enter must be registered.
C. Every person denied a seat is unregistered.
D. Registration is unnecessary for laboratory entry.

### Q2. [1 Mark] [NAT]

A ten-litre vessel initially contains a uniformly mixed solution with five litres of alcohol. Two litres of solution are removed and replaced by water. After thorough mixing, the same operation is performed again. How many litres of alcohol remain?

**Answer format:** Exact finite decimal.

### Q3. [1 Mark] [MCQ]

Four runners finish without ties. A finishes before B; C finishes after B; D finishes before C. Which runner can finish neither first nor last?

A. A
B. B
C. C
D. D

### Q4. [1 Mark] [MSQ]

Three labelled points form a nondegenerate triangle in the plane, with the labels encountered counterclockwise around its boundary. Each proposed transformation acts on all three points. Which preserve this counterclockwise order?

A. Rotation by 180 degrees about any fixed point.
B. Reflection in the x-axis.
C. Reflection in the x-axis followed by reflection in the y-axis.
D. Translation followed by one reflection in a line.

### Q5. [1 Mark] [MCQ]

Choose the word that best completes the sentence: “The committee accepted the proposal, ___ its concern about the short implementation period.”

A. because
B. notwithstanding
C. therefore
D. consequently

### Q6. [2 Marks] [NAT]

A 180 km journey consists of two equal-distance parts. A vehicle covers the first at 45 km/h. It stops for 30 minutes and then covers the second part at a constant speed. If its overall average speed, including the stop, is 40 km/h, what is its speed on the second part?

**Answer format:** Integer km/h.

### Q7. [2 Marks] [MCQ]

A survey includes 120 people. Seventy read newspaper A, sixty read newspaper B, and twenty read neither. Among those who read at least one, what fraction read exactly one?

A. 3/10
B. 7/10
C. 3/4
D. 5/6

### Q8. [2 Marks] [NAT]

Two rectangular sheets occupy [0,4]×[0,2] and [2,6]×[1,3] in a coordinate plane. Their overlap is glued and becomes internal to the combined flat shape. What is the perimeter of their union?

**Answer format:** Integer length units.

### Q9. [2 Marks] [NAT]

Six teams play a single round-robin tournament, every pair playing once. A win earns three points and a loss zero; a draw gives each team one point. The sum of all teams' final points is 41. How many matches were drawn?

**Answer format:** Integer.

### Q10. [2 Marks] [NAT]

Two fair six-sided dice are rolled independently. Given that their scores differ by exactly one, what is the expected larger score?

**Answer format:** Integer.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MSQ]

A TLB tags each translation by an address-space identifier (ASID) and a virtual page number. Processes P and Q have different ASIDs but may use the same virtual addresses. Which statements are correct?

A. A translation for P need not be discarded merely because the CPU switches to Q.
B. The ASID alone identifies a physical page without the virtual page number.
C. Reusing P's ASID for an unrelated address space may require invalidating stale translations carrying that ASID.
D. ASIDs eliminate the need to update a translation after its page-table mapping changes.

### Q12. [1 Mark] [NAT]

A collision-detection link transmits at 100 Mbit/s. The worst-case one-way propagation time between stations, including repeater delays, is 2.4 microseconds. Ignore all other timing constraints. What is the minimum frame size in bytes required for a sender still to be transmitting when a worst-case collision notification returns?

**Answer format:** Integer bytes; use 1 Mbit=10⁶ bits.

### Q13. [1 Mark] [NAT]

The set {1,2,3,4,5,6} is partially ordered by divisibility. What is the largest possible size of an antichain, a subset in which no two distinct elements divide one another?

**Answer format:** Integer.

### Q14. [1 Mark] [NAT]

Among real triples satisfying x+y+z=6 and x−y=0, what is the minimum possible value of x²+y²+z²?

**Answer format:** Integer.

### Q15. [1 Mark] [MCQ]

A quicksort variant partitions a subarray into keys less than, equal to, and greater than its pivot, in time Θ(m) for a subarray of length m. It recurses only on the less-than and greater-than parts. What is its running time on n equal keys?

A. Θ(1)
B. Θ(log n)
C. Θ(n)
D. Θ(n²)

### Q16. [1 Mark] [MSQ]

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

### Q17. [1 Mark] [MCQ]

For relation R(A,B,C), consider F={A→B, A→C, B→C}. Which is a minimal cover with singleton right-hand sides equivalent to F?

A. {A→B, B→C}
B. {A→C, B→C}
C. {A→B, A→C}
D. {A→BC}

### Q18. [1 Mark] [NAT]

Four NAND gates are connected as t=NAND(a,b), u=NAND(a,t), v=NAND(b,t), y=NAND(u,v). Out of the four possible input assignments to a,b, on how many does y differ from OR(a,b)?

**Answer format:** Integer.

### Q19. [1 Mark] [MCQ]

A bottom-up parser for E→E+T | T and T→id has already reduced the first id in `id+id` to E and shifted `+ id`. Its stack, ignoring states and the bottom marker, is `E + id`; the lookahead is end-of-input. What is the next reduction in the successful reverse-rightmost derivation?

A. E→E+T, reducing the entire stack immediately.
B. T→id, reducing only the final id.
C. E→T, reducing the initial E.
D. No reduction is possible because the input is exhausted.

### Q20. [1 Mark] [NAT]

A TCP sender transmits a SYN with sequence number 400, then 300 data bytes, then a FIN. There are no retransmissions or other data. What acknowledgment number acknowledges everything through the FIN? SYN and FIN each occupy one sequence number.

**Answer format:** Integer.

### Q21. [1 Mark] [MSQ]

An available-expression analysis tracks the expression a+b. One predecessor of a join computes t=a+b and then changes only c. The other computes u=a+b and then assigns a=0. There are no aliases. Which statements are correct immediately at the join?

A. a+b is available on the first predecessor's exit.
B. a+b is available on the second predecessor's exit solely because it was evaluated there earlier.
C. A conventional must-availability analysis does not mark a+b available at the join.
D. Replacing must-analysis intersection by union is always sound for eliminating a recomputation at the join.

### Q22. [1 Mark] [NAT]

A byte-addressed machine has 32-bit addresses and a direct-mapped cache with 4 KiB of data capacity and 32-byte lines. Each line stores a tag, a valid bit, and a dirty bit. No other metadata are counted. How many metadata bits are stored in total?

**Answer format:** Integer bits.

### Q23. [1 Mark] [MCQ]

Let L={aⁿbⁿ:n≥0}. Which of the following is regular?

A. L
B. L∩a*b*
C. L∩a*b³
D. {a,b}* minus L

### Q24. [1 Mark] [MCQ]

On an eight-bit two's-complement machine, x has bits 11111011. Define arithmetic right shift as copying the sign bit and logical right shift as inserting zero. What signed values result from one arithmetic right shift and one logical right shift, respectively?

A. −2 and 125
B. −3 and 125
C. −3 and −3
D. −2 and −2

### Q25. [1 Mark] [NAT]

A syntax-directed translation prints operands immediately, prints a binary operator after translating both operands left to right, and prints `neg` after translating a unary-minus operand. For the expression `-(a+b)*c`, how many tokens occur before the `neg` token in the generated postfix sequence? Each identifier and each operator is one token.

**Answer format:** Integer.

### Q26. [1 Mark] [NAT]

How many proper vertex colorings of a labelled five-cycle exist using three available labelled colors? Adjacent vertices must differ; not every color need be used.

**Answer format:** Integer.

### Q27. [1 Mark] [MCQ]

A two-input gate outputs 1 exactly when its inputs differ. Its output is fed to a second identical gate together with a third input c. Which description of the final output is correct?

A. It is 1 exactly when one input, but not all three, is 1.
B. It is 1 exactly when an odd number of the three inputs are 1.
C. It is 1 exactly when at least two inputs are 1.
D. It is 1 exactly when all inputs agree.

### Q28. [1 Mark] [NAT]

Evaluate the integral ∫₀¹ x/(1+x²) dx, rounded to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q29. [1 Mark] [NAT]

X is binomial with four trials and success probability p, where 0<p<1. Given P(X=0)=P(X=2), find E[X], rounded to three decimal places.

**Answer format:** Number to 3 decimal places.

### Q30. [1 Mark] [MSQ]

A JK flip-flop obeys Q′=J(NOT Q)+(NOT K)Q. Which settings force the stated behaviour for both possible current values of Q?

A. J=0,K=0 holds Q unchanged.
B. J=1,K=1 toggles Q.
C. J=1,K=0 forces Q′=0.
D. J=0,K=1 forces Q′=0.

### Q31. [1 Mark] [MCQ]

A process forks, then its child successfully executes a new program using exec. Which statement is correct under ordinary process semantics?

A. exec necessarily creates another process with a new process identifier.
B. The child keeps its process identity while its program image is replaced.
C. The parent's program image is replaced by the child's exec.
D. The child resumes at the instruction after the successful exec call in its old program.

### Q32. [1 Mark] [MCQ]

A binary tree has distinct labels, preorder A,B,D,E,C,F and inorder D,B,E,A,C,F. What is its postorder?

A. D,E,B,F,C,A
B. D,B,E,F,C,A
C. E,D,B,C,F,A
D. D,E,F,B,C,A

### Q33. [1 Mark] [MCQ]

An unweighted directed graph has exactly the edges s→a, s→b, a→c, a→d, b→d, c→t, d→t. Which pair gives the shortest s-to-t path length in edges and the number of distinct shortest s-to-t paths?

A. (3,3)
B. (3,2)
C. (4,3)
D. (3,4)

### Q34. [1 Mark] [MSQ]

For a unary relation R(x), compare tuple-calculus expressions E1={t | R(t)} and E2={t | NOT R(t)}. Values of t range over an external domain containing the active domain of R. Which statements are correct?

A. E1 is unchanged if the external domain is enlarged without changing R.
B. E2 is unchanged under every such enlargement.
C. E2 can gain tuples when the external domain is enlarged.
D. E1 necessarily returns every element of the external domain.

### Q35. [1 Mark] [NAT]

What integer is printed? The static variable is initialized once.

```c
#include <stdio.h>
int f(int n) {
    static int k = 0;
    int a = ++k;
    if (n == 0) return a;
    return a + f(n-1);
}
int main(void) {
    int x = f(2);
    int y = f(1);
    printf("%d\n", x+y);
    return 0;
}
```

**Answer format:** Integer.

### Q36. [2 Marks] [NAT]

A store-and-forward network has links S→R and R→D, each taking 1 ms to transmit one packet. Propagation is zero. At time 0, S has packets A,B,C in order. A and C must traverse both links; B terminates at R. Each link begins transmitting whenever its next eligible packet is available, preserving source order among packets that use it. What time in milliseconds does C finish arriving at D?

**Answer format:** Integer.

### Q37. [2 Marks] [MSQ]

Two threads share ordinary Boolean flags f0=f1=false. Under sequential consistency, thread i sets fi=true, then busy-waits while the other flag is true, enters its critical section, and finally sets fi=false. Reads and writes of each flag are atomic. Which statements are correct?

A. Both threads can be stuck waiting forever even if both are scheduled fairly.
B. Both threads can be simultaneously in their critical sections.
C. Mutual exclusion holds.
D. Replacing the flags with volatile flags alone necessarily prevents the waiting failure.

### Q38. [2 Marks] [NAT]

The complete undirected graph on labelled vertices A,B,C,D has one edge between every pair. How many spanning trees contain edge AB but do not contain edge AC?

**Answer format:** Integer.

### Q39. [2 Marks] [NAT]

A 1 Mbit/s output link receives a burst of three 1000-bit packets simultaneously at time 0 and thereafter no packets. It transmits nonpreemptively at full rate. A packet's queueing delay excludes its own transmission time and includes only waiting before transmission begins. What is the average queueing delay, in milliseconds, of these three packets?

**Answer format:** Integer.

### Q40. [2 Marks] [NAT]

Keys 40,20,60,10,30,50,70,25,35 are inserted in that order into an initially empty ordinary BST. Delete 20 by replacing its key with its inorder predecessor and physically removing that predecessor's original node. Then delete 40 by replacing its key with its inorder successor and physically removing that successor's original node. What is the key at the lowest common ancestor of 25 and 70 in the resulting tree?

**Answer format:** Integer key.

### Q41. [2 Marks] [MSQ]

R(A,B,C) has exactly the dependencies implied by A→B and BC→A. Decompose it into R1(A,B) and R2(A,C). Which statements are correct?

A. The decomposition is lossless under the stated dependencies.
B. Both components are in BCNF under their projected dependencies.
C. Enforcing only the projected dependencies on the components need not enforce BC→A on their join.
D. A is a candidate key of the original R.

### Q42. [2 Marks] [NAT]

A five-stage in-order pipeline has IF,ID,EX,MEM,WB, each one cycle. With full forwarding, a load followed immediately by an instruction using its result incurs exactly one stall. A taken branch resolved at the end of EX squashes the two younger instructions in IF and ID and incurs exactly two extra cycles. These penalties do not overlap. A completed program path has eight instructions, one such load-use pair and two taken branches. Starting with an empty pipeline, how many cycles elapse through the final WB?

**Answer format:** Integer cycles.

### Q43. [2 Marks] [MCQ]

Five variables a,b,c,d,e have an interference graph that is exactly the cycle a–b–c–d–e–a. Two variables connected by an edge cannot share a register; there are no preassigned registers, spills, or other constraints. Which pair gives the size of the largest clique and the minimum number of registers?

A. (2,2)
B. (2,3)
C. (3,3)
D. (3,5)

### Q44. [2 Marks] [NAT]

A system defines the working set immediately after a reference as the distinct pages in that reference and the previous three references, or all references so far if fewer than four exist. For the reference string 1,2,1,3,4,2,4,5, what is the sum of the working-set sizes immediately after references 4 through 8?

**Answer format:** Integer.

### Q45. [2 Marks] [MSQ]

A circuit is a two-to-one multiplexer with output F=(NOT s)a+sb. Its select line is tied to its own data input a, so s=a. Which statements are correct?

A. The resulting function is ab.
B. When a=0, changing b changes F.
C. The function can be implemented with one two-input NAND followed by one inverter.
D. The resulting function is a OR b.

### Q46. [2 Marks] [NAT]

An eight-bit unsigned multiplier retains only the low eight product bits. For a fixed odd input a=13, how many inputs b in {0,…,255} produce output 0? Count b values, not ordered pairs of inputs.

**Answer format:** Integer.

### Q47. [2 Marks] [NAT]

A six-bit unsigned register x initially holds 45. One operation rotates its bits left by two positions within the six-bit word, then XORs the result with binary 001111. What decimal value results after two such operations?

**Answer format:** Integer.

### Q48. [2 Marks] [MSQ]

An undirected graph on A,B,C,D has edges AB=1, AC=2, BC=2, BD=3, CD=3, AD=4. Which statements are correct?

A. Every minimum spanning tree contains AB.
B. Exactly four minimum spanning trees exist.
C. The smallest spanning-tree weight strictly greater than the minimum is 8.
D. Raising AD's weight from 4 to 100 leaves the set of minimum spanning trees unchanged.

### Q49. [2 Marks] [NAT]

For grammar S→CC, C→cC | d, use canonical LR(0) item sets for the augmented grammar S′→S. How many distinct states contain a completed item C→d·? Count states, not transitions into them.

**Answer format:** Integer.

### Q50. [2 Marks] [MCQ]

A proposed undecidability proof transforms a machine M and input w into a recognizer N that, on every input x, simulates M on w and accepts x if that simulation halts. It then claims that testing whether L(N) is regular decides whether M halts on w. What is the flaw?

A. The construction requires knowing in advance whether M halts.
B. Both possible languages of N are regular, so the test does not distinguish halting from nonhalting.
C. N always recognizes a nonregular language.
D. A recognizer cannot simulate another machine on a fixed input.

### Q51. [2 Marks] [NAT]

A program spends 40% of its original execution time in a component that can be accelerated. The remaining 60% is unchanged. To make the whole program exactly 25% faster, by what factor must that component be accelerated? Interpret “25% faster” as speedup 1.25.

**Answer format:** Integer factor.

### Q52. [2 Marks] [MCQ]

A file contains 100 fixed-size records in ten disk blocks, ten records per block. An in-memory index gives the exact block containing any requested record. Ten requested record numbers are independently and uniformly selected with replacement from the 100 records. A data block is read from disk only on its first request and then remains cached. Which expression is the expected number of disk reads?

A. 10
B. 10(1−(9/10)¹⁰)
C. 100(1−(99/100)¹⁰)
D. (9/10)¹⁰

### Q53. [2 Marks] [NAT]

How many binary strings of length eight contain no adjacent zeros and have an even number of ones?

**Answer format:** Integer.

### Q54. [2 Marks] [MSQ]

Let u=(1,1,0)ᵀ, v=(1,0,1)ᵀ, P=uuᵀ/(uᵀu), and Q=vvᵀ/(vᵀv). Which statements are correct?

A. PQ has rank one.
B. trace(PQ)=1/4.
C. PQ is symmetric.
D. The eigenvalues of PQ, counting multiplicity, are 1/4,0,0.

### Q55. [2 Marks] [MCQ]

A router receives destination 172.16.5.200. Its routes are 172.16.0.0/16→A, 172.16.4.0/22→B, 172.16.5.128/25→C, and a default route→D. A forwarding policy first chooses the longest matching prefix; among equal-length matches it chooses the lowest metric. The /25 route has metric 100 and the /22 route metric 1. Which next hop is selected, and why?

A. B, because metric 1 is smaller than 100.
B. C, because prefix length is considered before metric.
C. A, because a /16 covers more addresses.
D. D, because the overlapping routes are ambiguous.

### Q56. [2 Marks] [MCQ]

A queue is represented by a circular array of length 8. head points to the next element to remove, tail to the next free insertion slot, and one slot is always left unused. Initially head=6 and tail=2. Execute dequeue, enqueue X, enqueue Y, dequeue, enqueue Z, with all operations successful. What are (head,tail,number of stored elements) at the end?

A. (0,5,5)
B. (0,5,4)
C. (1,5,4)
D. (0,4,4)

### Q57. [2 Marks] [NAT]

A 0/1 knapsack has capacity 8 and five distinct items with (weight,value): A=(2,3), B=(2,3), C=(3,4), D=(3,4), E=(4,5). Each may be selected at most once. How many distinct subsets attain the maximum possible value without exceeding capacity? Subsets differing only by A versus B or C versus D still count as distinct.

**Answer format:** Integer.

### Q58. [2 Marks] [NAT]

For real a, let f_a(x)=x³−3ax on the closed interval [−1,1]. There is exactly one value of a for which f_a has two distinct global minimizers on that interval. Find a.

**Answer format:** Exact finite decimal.

### Q59. [2 Marks] [NAT]

A B+ tree has a root with two leaf children. The leaves, in order, contain [5,10] and [20,25]. A leaf holds at most three keys; an overflowing four-key leaf splits into two leaves with two keys each. Internal separators are the smallest keys in the nonleftmost child. The root can hold up to three separators. Insert 15, then 12, then 30. What is the sum of the root's separators afterward?

**Answer format:** Integer.

### Q60. [2 Marks] [MSQ]

In C, a function returns a pointer in each of the following independent versions. Assume allocations succeed and no frees occur before the caller's first access. Which versions permit the caller to access a live int object through the returned pointer after the function returns?

A. `int *f(void) { int x=7; return &x; }`
B. `int *f(void) { static int x=7; return &x; }`
C. `int *f(void) { int *p=malloc(sizeof *p); *p=7; return p; }` with the proper standard header.
D. `int *f(void) { int a[1]={7}; return a; }`

### Q61. [2 Marks] [NAT]

An insertion-sort implementation counts only comparisons between keys inside the shifting loop. It scans left while the preceding key is strictly greater than the inserted key, stopping at the first non-greater key or the array boundary. On input [5,1,4,2,3], how many key comparisons occur? Index-boundary tests are not key comparisons.

**Answer format:** Integer.

### Q62. [2 Marks] [NAT]

A byte-addressed memory contains 64 KiB and is built from chips storing 8K words of four bits each. Chips are arranged so one addressed byte is transferred at once. How many chips are needed in total?

**Answer format:** Integer.

### Q63. [2 Marks] [MSQ]

Let L be any language over a finite alphabet. Define Pref(L)={x:xy∈L for some string y}. Which statements are correct?

A. If L is regular, Pref(L) is regular.
B. If L is recognizable, Pref(L) is recognizable.
C. If Pref(L) is regular, L must be regular.
D. If L is nonempty, ε belongs to Pref(L).

### Q64. [2 Marks] [MCQ]

A compiler translates `if (p && q) x=1; else x=2;` with short-circuit evaluation. Evaluating p or q may have side effects, and each Boolean expression's result is determined at its evaluation. Which transformation preserves the evaluations and assignments for all executions?

A. Evaluate q first, then p, and test their conjunction.
B. Evaluate both p and q unconditionally, then test their conjunction.
C. Evaluate p; if false assign 2, otherwise evaluate q and assign 1 if q is true and 2 otherwise.
D. Evaluate p twice and q only if the second evaluation is true.

### Q65. [2 Marks] [MSQ]

Transactions obey basic two-phase locking: a growing phase acquires locks, and after the first unlock no more locks may be acquired. Exclusive locks conflict with every other transaction's lock on that item; shared locks conflict with exclusive locks. Locks need not be held until commit. Which statements are correct?

A. Every resulting complete schedule is conflict serializable.
B. Cascading aborts are impossible.
C. Deadlock is possible.
D. Holding all exclusive locks until commit is a stronger restriction that prevents another transaction from reading an uncommitted written value.

---

## ANSWER KEY — MOCK TEST 006

Integer and exact-decimal NAT answers are exact. For rounded answers the accepted closed ranges are displayed.

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | B |
| 2 | NAT | 1 | 3.2 |
| 3 | MCQ | 1 | B |
| 4 | MSQ | 1 | A, C |
| 5 | MCQ | 1 | B |
| 6 | NAT | 2 | 45 |
| 7 | MCQ | 2 | B |
| 8 | NAT | 2 | 18 |
| 9 | NAT | 2 | 4 |
| 10 | NAT | 2 | 4 |
| 11 | MSQ | 1 | A, C |
| 12 | NAT | 1 | 60 |
| 13 | NAT | 1 | 3 |
| 14 | NAT | 1 | 12 |
| 15 | MCQ | 1 | C |
| 16 | MSQ | 1 | A, C, D |
| 17 | MCQ | 1 | A |
| 18 | NAT | 1 | 1 |
| 19 | MCQ | 1 | B |
| 20 | NAT | 1 | 702 |
| 21 | MSQ | 1 | A, C |
| 22 | NAT | 1 | 2816 |
| 23 | MCQ | 1 | C |
| 24 | MCQ | 1 | B |
| 25 | NAT | 1 | 3 |
| 26 | NAT | 1 | 30 |
| 27 | MCQ | 1 | B |
| 28 | NAT | 1 | 0.3466 (range 0.34655–0.34665) |
| 29 | NAT | 1 | 1.160 (range 1.1595–1.1605) |
| 30 | MSQ | 1 | A, B, D |
| 31 | MCQ | 1 | B |
| 32 | MCQ | 1 | A |
| 33 | MCQ | 1 | A |
| 34 | MSQ | 1 | A, C |
| 35 | NAT | 1 | 15 |
| 36 | NAT | 2 | 4 |
| 37 | MSQ | 2 | A, C |
| 38 | NAT | 2 | 5 |
| 39 | NAT | 2 | 1 |
| 40 | NAT | 2 | 50 |
| 41 | MSQ | 2 | A, B, C |
| 42 | NAT | 2 | 17 |
| 43 | MCQ | 2 | B |
| 44 | NAT | 2 | 17 |
| 45 | MSQ | 2 | A, C |
| 46 | NAT | 2 | 1 |
| 47 | NAT | 2 | 40 |
| 48 | MSQ | 2 | A, B, D |
| 49 | NAT | 2 | 1 |
| 50 | MCQ | 2 | B |
| 51 | NAT | 2 | 2 |
| 52 | MCQ | 2 | B |
| 53 | NAT | 2 | 27 |
| 54 | MSQ | 2 | A, B, D |
| 55 | MCQ | 2 | B |
| 56 | MCQ | 2 | A |
| 57 | NAT | 2 | 3 |
| 58 | NAT | 2 | 0.25 |
| 59 | NAT | 2 | 32 |
| 60 | MSQ | 2 | B, C |
| 61 | NAT | 2 | 9 |
| 62 | NAT | 2 | 16 |
| 63 | MSQ | 2 | A, B, D |
| 64 | MCQ | 2 | C |
| 65 | MSQ | 2 | A, C, D |


