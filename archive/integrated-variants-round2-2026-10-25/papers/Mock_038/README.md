# GATE CS 2027 — Full-Length Mock Test 038

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

Every certified sample was tested. Some tested samples were rejected. Which conclusion must follow?

A. Some certified samples were rejected.
B. Every tested sample was certified.
C. No untested sample was certified.
D. Every rejected sample was certified.

### Q2. [1 Mark] [MCQ]

Unit cubes form four vertical stacks on a 2×2 footprint, with height rows (1,3) and (2,1). Orthogonal projections onto the horizontal plane and the two vertical coordinate planes count overlapping projected squares only once. What is the sum of the areas of these three projections, in square units?

A. 7
B. 11
C. 12
D. 14

### Q3. [1 Mark] [MCQ]

“A library extended its opening hours. Evening attendance increased, but total daily attendance remained unchanged.” Which interpretation is consistent with both observations?

A. Some visits shifted from earlier hours to the evening.
B. Total daily attendance necessarily increased.
C. Earlier attendance necessarily increased too.
D. The library must have measured attendance incorrectly.

### Q4. [1 Mark] [NAT]

How many distinct arrangements of the multiset A,A,B,B,C,C contain no two identical letters next to each other?

**Answer format:** Integer.

### Q5. [1 Mark] [MCQ]

Choose the word that best completes the sentence: “The committee accepted the proposal, ___ its concern about the short implementation period.”

A. because
B. notwithstanding
C. therefore
D. consequently

### Q6. [2 Marks] [MCQ]

Six unit squares form a cube net. Their centres on a square grid are A=(0,0), B=(1,0), C=(2,0), D=(3,0), E=(1,1), and F=(1,-1). Squares sharing a full edge are hinged, and the net is folded into a cube with labels on the outside. Which pair of faces is opposite, and which triple can meet at one cube vertex?

A. A and C are opposite; A,B,E can meet.
B. B and C are opposite; A,C,E can meet.
C. E and F are opposite; A,B,C can meet.
D. A and D are opposite; B,E,F can meet.

### Q7. [2 Marks] [MCQ]

A report states: “The valve was closed before the pressure was measured. The pressure measurement preceded replacing the gauge. After the replacement, the valve was reopened.” Which event must lie between valve closure and gauge replacement?

A. Reopening the valve.
B. Measuring the pressure.
C. A second valve closure.
D. No event is forced between them.

### Q8. [2 Marks] [MCQ]

A fair coin selects one of two boxes. Box I contains two red balls and one blue ball; Box II contains one red ball and two blue balls. Two balls are drawn uniformly without replacement from the selected box. Given that at least one drawn ball is red, what is the probability that both are red?

A. 1/6  
B. 1/3  
C. 1/5  
D. 2/5

### Q9. [2 Marks] [MCQ]

“The agreement is provisional, not irrevocable; either side may withdraw before the inspection, but neither may withdraw afterward.” Which statement follows?

A. The agreement never binds either side.
B. Withdrawal is permitted after inspection if both sides remain provisional.
C. The right to withdraw exists before inspection and ends afterward.
D. Inspection automatically cancels the agreement.

### Q10. [2 Marks] [NAT]

A positive real number x satisfies log2(x)+log4(x)=log2(7x−36). Determine the sum of all real values of x satisfying the equation. The logarithms must all be defined.

**Answer format:** Exact integer.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

Records (key,id) occur initially as(1,A),(1,B),(2,C). They are stably sorted by ascending key and the whole resulting array is then reversed. Relative to the original input, is this a stable descending-key sort?


A. No, because A and B appear in the opposite order.
B. Yes, because reversing always preserves equal-key order.
C. No, because key2 appears before key1.
D. Yes, because the ascending sort was stable.

### Q12. [1 Mark] [MSQ]

An available-expression analysis tracks the expression a+b. One predecessor of a join computes t=a+b and then changes only c. The other computes u=a+b and then assigns a=0. There are no aliases. Which statements are correct immediately at the join?

A. a+b is available on the first predecessor's exit.
B. a+b is available on the second predecessor's exit solely because it was evaluated there earlier.
C. A conventional must-availability analysis does not mark a+b available at the join.
D. Replacing must-analysis intersection by union is always sound for eliminating a recomputation at the join.

### Q13. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

To apply the regular-language pumping lemma to the language of binary palindromes, choose w=0^p10^p for a putative pumping length p≥1. A permitted decomposition w=xyz satisfies |xy|≤p and |y|≥1. Which statements are correct?

**Candidates**

**I.** Every permitted y consists only of zeros from the initial block.

**II.** Some permitted decomposition remains a palindrome after replacing y by yy.

**III.** Pumping down to xz produces a non-palindrome for every permitted decomposition.

**IV.** Exhibiting just one badly behaving permitted decomposition is sufficient for a nonregularity proof.

A. I and III  
B. II and III  
C. II and IV  
D. III and IV

### Q14. [1 Mark] [MSQ]

An undirected graph consists of triangles abc and def together with the single connecting edge cd. Which statements are correct?

A. It has a perfect matching.
B. Every perfect matching contains cd.
C. It is bipartite.
D. Its minimum vertex cover has size3.

### Q15. [1 Mark] [MCQ]

In a three-variable Karnaugh map, minterms 000 and 100 are adjacent. What term results from combining just these two minterms, with variables a,b,c in that order?

A. b′c′
B. a′b′
C. ac′
D. a+b+c

### Q16. [1 Mark] [MCQ]

A four-line direct-mapped cache starts empty and uses block number modulo four as its line index. Which reference sequence has exactly one hit?

A. 0,4,0,4
B. 0,1,0,4
C. 0,1,2,3
D. 0,0,0,0

### Q17. [1 Mark] [MCQ]

Two transactions execute r1(X),w1(X),r2(X),w2(Y),r1(Y), then both commit, with operations listed in execution order. Which statement about conflict serializability is correct?

A. Equivalent to T1 followed by T2 because T1 first accesses X.
B. Equivalent to T2 followed by T1 because T2 writes Y.
C. Serializable because reads never participate in conflicts.
D. Not conflict-serializable because the precedence graph contains both T1→T2 and T2→T1.

### Q18. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For grammar S→aA | bB, A→c | ε, B→c | ε, which statement about predictive parsing is correct?

A. The two ε-productions necessarily cause an LL(1) conflict.  
B. The grammar is LL(1); the choice at S is distinguished by a or b, and the nullable choices use the end marker.  
C. The common terminal c makes the two alternatives of S indistinguishable.  
D. Left recursion prevents predictive parsing.

### Q19. [1 Mark] [NAT]

Two packets of 1000 bits each are ready at time 0 and travel through three store-and-forward links in order. Their rates are 2 Mbit/s, 1 Mbit/s and 2 Mbit/s, respectively; 1 Mbit=10^6 bits. Each link transmits only one packet at a time, buffers are sufficient, and propagation and processing delays are zero. Packets retain their order. Each link begins transmitting as soon as both the packet and that link are available. At what time, in milliseconds, does the last bit of the second packet reach the destination?

**Answer format:** Numeric value; integer.

### Q20. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

The grammar S→aSb | ε is used by a predictive parser. On valid input aabb, what is the maximum number of unconsumed b terminals simultaneously present on its stack, excluding input and the end marker?

A. 1  
B. 2  
C. 3  
D. 4

### Q21. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Two machines are on the same ordinary Ethernet broadcast domain. A host broadcasts an ARP request for its default gateway's IPv4 address. What is it principally trying to learn?

A. The gateway's Ethernet address on that LAN.  
B. The remote web server's TCP sequence number.  
C. The gateway's complete routing table.  
D. The DNS name of every host on the LAN.

### Q22. [1 Mark] [NAT]

Six labelled positions lie on a circle. How many assignments of exactly two1 bits and four0 bits have no adjacent1 bits, including across the last-to-first boundary? Rotations remain distinct assignments.

**Answer format:** Integer.

### Q23. [1 Mark] [NAT]

A binary error-detecting code consists of all four-bit words having even parity. A valid transmitted word suffers exactly two distinct bit flips. How many of the six possible error-position pairs are detected by an even-parity check?

**Answer format:** Integer.

### Q24. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A symbolic link stores a pathname rather than increasing its target file's hard-link count. Which statements are correct?

**Candidates**

**I.** Deleting the target's only pathname can leave a dangling symbolic link.

**II.** A symbolic link necessarily prevents the target inode from being reclaimed forever.

**III.** A symbolic link can name a target on another file system under ordinary pathname resolution.

**IV.** Every symbolic link is indistinguishable from a hard link in inode reference counting.

A. I and II  
B. I and IV  
C. I and III  
D. II and III

### Q25. [1 Mark] [MCQ]

A DMA transfer completes while the CPU executes unrelated instructions. What mechanism can notify the CPU without requiring it to poll continuously?

A. A completion interrupt.
B. Deleting every CPU register.
C. Changing every virtual address to zero.
D. Disabling the device permanently before completion.

### Q26. [1 Mark] [NAT]

A sequence satisfies a0=1, a1=3 and a(n)=2a(n−1)−a(n−2) for n≥2. What is the coefficient of x^5 in its ordinary generating function Σ a(n)x^n?

**Answer format:** Exact integer.

### Q27. [1 Mark] [MCQ]

For production S→ABC, which proposed inherited-attribute dependency violates the left-to-right dependency restriction of an L-attributed definition?


A. A.in depends on C.out.
B. B.in depends on A.out.
C. C.in depends on B.out.
D. A.in depends on S.in.

### Q28. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Linear probing in a hash table stores keys whose home slot is4 in slots4,5,6. Slot7 is empty. The key in slot5 is deleted. Which deletion action preserves ordinary probing searches for the key in slot6, if searches stop at a never-used empty slot?

A. Mark slot5 as never-used empty without moving keys.  
B. Mark slot5 with a tombstone that searches pass through.  
C. Clear slot6 as well.  
D. Change only the deleted key's hash function.

### Q29. [1 Mark] [MCQ]

A five-stage in-order pipeline has stages IF,ID,EX,MEM,WB, each one cycle. There is no forwarding and no automatic stalling. Register writes occur in the first half of a cycle and ID reads in the second half, so ID may read a value written in WB during the same cycle. The instructions below use ordinary integer registers; R0 is always available. What is the minimum total number of NOP instructions that must be inserted without reordering to guarantee correct results for arbitrary initial register values?
```text
ADD R1,R0,R0
ADD R2,R1,R0
ADD R3,R2,R0
```

A. 2  
B. 3  
C. 4  
D. 6

### Q30. [1 Mark] [MCQ]

A weak entity Installment is identified by its owner Loan and its partial key installment_number. Loan has primary key loan_id. Each installment has exactly one owner, and the same installment_number may occur under different loans. Which primary key preserves this identification when mapping Installment to a relation?

A. installment_number alone.
B. loan_id alone.
C. (loan_id, installment_number).
D. amount alone.

### Q31. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Over a nonempty domain, which formula is the negation of “For every x, if P(x), there exists y such that R(x,y)”?

A. For every x, P(x) and for every y, not R(x,y).  
B. There exists x such that not P(x) and there exists y with R(x,y).  
C. There exists x such that P(x) and for every y, not R(x,y).  
D. There exists x such that P(x) and there exists y with not R(x,y).

### Q32. [1 Mark] [MCQ]

A process successfully calls exec to replace its program. Which statement is correct under the usual UNIX process model?

A. Its process identifier changes because a new process is created.
B. All open file descriptors necessarily close.
C. Execution eventually returns to the instruction after the successful exec call.
D. The process keeps its identifier but executes the replacement program.

### Q33. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A recognizer accepts every member of L and may loop on nonmembers. Which extra guarantee would make that same machine a decider for L?

A. It uses at least two tape symbols.  
B. It halts on every input, rejecting every nonmember.  
C. It accepts one input quickly.  
D. It has a finite written description.

### Q34. [1 Mark] [NAT]

After tabular minimization, selecting prime implicants P,Q,R must satisfy the cover expression (P+Q)(Q+R)(P+R), where + means choosing at least one listed implicant and multiplication means satisfying all requirements. Each selected implicant has equal cost. How many distinct minimum-cardinality covers exist?

**Answer format:** Exact integer.

### Q35. [1 Mark] [NAT]

A2×2 real matrix A has trace5 and determinant6. What is det(A−I)?

**Answer format:** Exact number.

### Q36. [2 Marks] [MCQ]

A process has four user-level threads mapped to one kernel-scheduled thread. The mapping does not replace blocking system calls with asynchronous operations. One user thread makes a blocking read that blocks the kernel thread. Which consequence follows while that kernel thread remains blocked?

A. The other user threads in the process automatically run on three other cores.
B. None of its user threads can run through that blocked sole kernel thread.
C. The process obtains four new kernel threads automatically.
D. User-level scheduling can execute instructions without any runnable kernel thread.

### Q37. [2 Marks] [MSQ]

A closure captures a local variable by reference. The closure can be invoked after its defining procedure returns. Which statements are correct?

A. The captured storage must remain valid for those later invocations.
B. Keeping only a pointer into an already-reused stack frame is always sufficient.
C. Heap allocation or another lifetime-preserving mechanism can support the capture.
D. Lexical scope alone guarantees that arbitrary stack storage remains allocated forever.

### Q38. [2 Marks] [NAT]

A hypothetical CSMA/CD link transmits at 100 million bits per second with a minimum frame of 512 bits. Signal propagation speed in the cable is 200 million metres per second. In addition to cable propagation, devices introduce 0.4 microseconds of delay in each direction. Requiring the minimum-frame transmission time to be at least the worst-case round-trip delay, what is the maximum cable length in metres?

**Answer format:** Integer.

### Q39. [2 Marks] [MSQ]

For x≠0 let f(x)=x sin(1/x) and g(x)=x² sin(1/x), with f(0)=g(0)=0. Which statements are correct?

A. f is continuous at 0.  
B. f is differentiable at 0.  
C. g is differentiable at 0.  
D. g′ is continuous at 0.

### Q40. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Under set semantics, R(A,B) and S(A,B) have the same schema. Which statements hold for every instance?

**Candidates**

**I.** πA(R−S)=πA(R)−πA(S).

**II.** πA(R−S) contains πA(R)−πA(S).

**III.** πA(R∩S) is contained in πA(R)∩πA(S).

**IV.** πA(R∩S)=πA(R)∩πA(S).

A. I and II  
B. II and III  
C. I and III  
D. I and IV

### Q41. [2 Marks] [MSQ]

Define MUX(s,u,v) to return u when s=0 and v when s=1. A circuit computes T=MUX(s,a,b), then F=MUX(T,s,NOT s). Which statements are correct?

A. F=(NOT s AND a) OR (s AND NOT b).
B. If a=b, toggling s toggles F.
C. If a and b differ, F is independent of s.
D. F always equals s XOR a XOR b.

### Q42. [2 Marks] [MCQ]

For n≥4, what is the asymptotic number of calls to work()? Arithmetic uses unbounded integers.

```text
i = 2
while i <= n:
    j = 2
    while j <= i:
        work()
        j = j*j
    i = 2*i
```

A. Θ(log n)
B. Θ(log n log log n)
C. Θ(n log log n)
D. Θ((log n)²)

### Q43. [2 Marks] [NAT]

Routers A,B,C form a line with link costs AB=1 and BC=1. Destination C initially has distances at A=2,B=1. Link BC fails. Before receiving B's failure update, A advertises its old distance2 to B. With ordinary distance-vector updating and no split horizon, what distance can B incorrectly adopt through A?

**Answer format:** Integer.

### Q44. [2 Marks] [NAT]

A complete DFA over {0,1} accepts exactly the strings that end in 01. What is the minimum number of states in such a DFA?

**Answer format:** Integer.

### Q45. [2 Marks] [NAT]

Processes P and Q arrive at time 0, with P initially ahead of Q. Round-robin scheduling uses a quantum of 2 time units and zero context-switch cost. P executes a CPU burst of 2, performs I/O for 3, then executes a CPU burst of 2 and terminates. Q has one CPU burst of 5. A process finishing I/O joins the tail of the ready queue without preempting the running process. A quantum-expired process also joins the tail. What is the sum of their waiting times in the ready queue? I/O time is not waiting time.

**Answer format:** Integer time units.

### Q46. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A 5×5 matrix is stored in row-major order in a one-dimensional C array: row r, column c is a[5*r+c], for 0≤r,c<5. Consider this complete program. All arithmetic fits in int.
```c
#include <stdio.h>
static void swap(int *p, int *q) {
    int t = *p; *p = *q; *q = t;
}
int main(void) {
    int a[25];
    for (int i = 0; i < 25; ++i) a[i] = i;
    for (int k = 0; k < 2027; ++k) {
        for (int r = 0; r < 5; ++r)
            for (int c = r + 1; c < 5; ++c)
                swap(&a[5*r+c], &a[5*c+r]);
        for (int r = 0; r < 5; ++r)
            for (int c = 0; c < 2; ++c)
                swap(&a[5*r+c], &a[5*r+4-c]);
    }
    printf("%d %d", a[7], a[17]);
    return 0;
}
```
What is printed?

A. 13 11  
B. 11 13  
C. 7 17  
D. 17 7

### Q47. [2 Marks] [MCQ]

A machine's ADD (R)+,(R)+ instruction first reads the source word at address R and increments R by four, then reads the destination word at the new R and increments R by four again, finally writing the sum to that destination's captured address. Initially R=100, M[100]=3 and M[104]=5. Which pair gives the final R and M[104]?

A. (104,6)
B. (108,6)
C. (108,8)
D. (104,8)

### Q48. [2 Marks] [MCQ]

Over alphabet {a,b}, let L={a,ab}. A pushdown automaton starts with one bottom-of-stack symbol. For empty-stack acceptance, a string is accepted only if all input has been consumed and the stack is empty; no transition is possible once the stack is empty. No right-end marker is supplied. Standard determinism forbids a choice between an epsilon transition and an input-consuming transition for the same state and stack top. Which machine model cannot recognize L?

A. A deterministic finite automaton.  
B. A nondeterministic pushdown automaton accepting by empty stack.  
C. A deterministic pushdown automaton accepting by final state.  
D. A deterministic pushdown automaton accepting by empty stack.

### Q49. [2 Marks] [NAT]

A pipe initially contains no bytes and has two open write descriptors referring to its write end, one in P and one in Q. P writes 5 bytes and closes its descriptor. Reader R requests 10 bytes and receives the available 5. R then performs another blocking read while Q still holds its descriptor but never writes. Later Q closes that descriptor. How many bytes does R's second read return upon completion? Assume no signals or errors.

**Answer format:** Exact integer.

### Q50. [2 Marks] [NAT]

Independent fair-coin tosses continue until the first head. Let N be the number of tosses, including the head. Given that N is odd, what is E[N]? Round to four decimal places.

**Answer format:** Decimal rounded to four places.

### Q51. [2 Marks] [NAT]

How many equivalence relations on a labelled four-element set have exactly two equivalence classes?

**Answer format:** Integer.

### Q52. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A loop visits consecutive integer indices i starting at s and loads the four-byte array element at byte address base+4*i. Arithmetic is exact, base is unchanged, and i is also used by other statements. Which strength reductions preserve the load addresses and those other uses?

**Candidates**

**I.** Initialize address p=base and increment p by four each iteration for arbitrary s.

**II.** Initialize p=base+4*s, use p for each load, and increment p by four after each iteration while retaining i's original updates.

**III.** The multiplication used to form each load address can then be removed from the loop body if it has no other uses.

**IV.** Remove every update of i merely because a running address is available.

A. I and IV  
B. II and IV  
C. II and III  
D. III and IV

### Q53. [2 Marks] [MCQ]

The block below uses exact integer arithmetic, ordinary scalars and no aliases. An optimizer may share identical expressions, treating multiplication as commutative, and remove unnecessary copies. It must preserve all returned values. It may not use distributivity or introduce operations other than the displayed additions and multiplications. What are the minimum numbers of multiplications and additions, respectively?

```text
a = x * y
b = y * x
c = a + z
d = b + z
x = x + 1
e = x * y
f = e + z
return (c,d,f)
```

A. (1,2)  
B. (2,2)  
C. (2,3)  
D. (3,3)

### Q54. [2 Marks] [NAT]

An IPv4 datagram has a20-byte header and2400 bytes of payload. A router fragments it for an MTU of1020 bytes using the largest legal payload in each nonfinal fragment. The final fragment is later forwarded onto a link with MTU220 bytes and is fragmented again if necessary. All headers remain20 bytes, with no options. What is the fragment-offset field of the last fragment reaching the final link? Offset fields are in8-byte units relative to the original datagram payload.

**Answer format:** Integer.

### Q55. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A weighted undirected connected graph has some negative edge weights. Which statements about Kruskal's MST algorithm are true?

**Candidates**

**I.** Sorting edges by nondecreasing weight and rejecting cycle-forming edges remains correct.

**II.** Every negative edge must be included, even if the negative edges form a cycle.

**III.** The cut/exchange justification does not require all weights to be nonnegative.

**IV.** Replacing all weights w by w+c for one constant c can change which spanning trees minimize total weight.

A. I and III  
B. I and IV  
C. II and III  
D. II and IV

### Q56. [2 Marks] [MCQ]

A language L is both recognizable and co-recognizable. Given recognizers for L and its complement, how can a decider be constructed?

A. Run the recognizer for L forever and reject if it has not accepted after any fixed universal timeout.
B. Dovetail the two recognizers and decide according to which accepts first.
C. Reject all strings because nontermination is possible.
D. Reverse the transitions of the recognizer for L.

### Q57. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Over a finite candidate relation C(x) and a finite required relation S(y), query Q selects candidates satisfying FOR ALL y(S(y) IMPLIES R(x,y)). Query P instead requires FOR ALL y(S(y) AND R(x,y)), where the quantified domain is infinite and S is finite. Which statement holds when S is empty and C is nonempty?

A. Both queries return C.  
B. Q returns C, while P returns no candidates.  
C. Q returns no candidates, while P returns C.  
D. Both queries return no candidates.

### Q58. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Three processes each need at most three instances of a single resource type. Instances are identical, acquisitions are one at a time, and a process releases all its instances only when it has obtained its full requirement and completes. What is the smallest total number of instances that guarantees no resource deadlock for every allocation reachable under these rules, assuming runnable processes eventually run?

A. 6  
B. 7  
C. 8  
D. 9

### Q59. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An 8-bit ALU subtracts B from A using A+(NOT B)+1. The result is reduced modulo 256. N is its most significant bit, V indicates signed two's-complement overflow, and C is carry-out, with C=1 meaning no unsigned borrow. Both operands range independently over all 256 bit patterns.

How many ordered pairs (A,B) produce N=0, V=1 and C=1 simultaneously?

A. 8192  
B. 8128  
C. 8256  
D. 16384

### Q60. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Two finite, acyclic, singly linked lists may share a suffix by node identity. Their heads are h1 and h2. Which algorithm finds the first shared node, or reports none, in O(m+n) time and O(1) extra space?

A. Compare only the values stored in corresponding nodes.  
B. Measure both lengths, advance the longer list by their difference, then advance both pointers together until they are identical or both null.  
C. Return the first pair of nodes having equal stored values, regardless of identity.  
D. Reverse one list and return its new head without examining the other list.

### Q61. [2 Marks] [MCQ]

A complete binary tree is stored in an array with root index 1 and children 2i,2i+1. It has 100 nodes. What is the number of nodes in the subtree rooted at index 6, including that root?

A. 15
B. 20
C. 21
D. 31

### Q62. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For a 0/1 knapsack with nonnegative integer capacity W and items of positive integer weights wi and positive values vi, let D[j] initially be zero for every 0 ≤ j ≤ W. Each item may be used at most once. Consider the update `D[j] = max(D[j], D[j-wi] + vi)` for j ≥ wi. Which statements are correct?

A. Processing each item once and scanning j downward from W to wi computes the maximum value for capacity W.  
B. Processing each item once and scanning j upward from wi to W always computes the same 0/1 optimum.  
C. With one item of weight 2 and value 3 and capacity 4, an upward scan produces D[4]=6.  
D. For a downward scan, immediately before updating D[j] for an item, D[j-wi] still excludes that item.

### Q63. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A table has rows (department,salary): (A,10),(A,10),(A,20),(B,20),(B,NULL). Consider:

```sql
SELECT department
FROM T
GROUP BY department
HAVING COUNT(DISTINCT salary) = 2
   AND SUM(salary) > 30;
```

Which result is returned under standard SQL aggregate rules?

A. No rows  
B. A only  
C. B only  
D. A and B

### Q64. [2 Marks] [NAT]

A microinstruction has 16 independent control bits, a field selecting one of eight branch conditions, and two absolute next-address fields for true and false outcomes. The control store holds 256 microinstructions. With fixed-width fields and no shared encoding, how many bits does one microinstruction require?

**Answer format:** Integer.

### Q65. [2 Marks] [NAT]

A real3×3 matrix A has eigenvalues1,2,4, each once. Define B=A²−3A+2I. What is the rank of B?

**Answer format:** Exact integer.

---

## ANSWER KEY — MOCK TEST 038

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | C |
| 2 | MCQ | 1 | D |
| 3 | MCQ | 1 | A |
| 4 | NAT | 1 | 30 |
| 5 | MCQ | 1 | B |
| 6 | MCQ | 2 | A |
| 7 | MCQ | 2 | B |
| 8 | MCQ | 2 | C |
| 9 | MCQ | 2 | C |
| 10 | NAT | 2 | 45 |
| 11 | MCQ | 1 | A |
| 12 | MSQ | 1 | A, C |
| 13 | MCQ | 1 | A |
| 14 | MSQ | 1 | A, B |
| 15 | MCQ | 1 | A |
| 16 | MCQ | 1 | B |
| 17 | MCQ | 1 | D |
| 18 | MSQ | 1 | A, C, D |
| 19 | NAT | 1 | 3 (exact) |
| 20 | MSQ | 1 | A, C, D |
| 21 | MSQ | 1 | B, C, D |
| 22 | NAT | 1 | 9 |
| 23 | NAT | 1 | 0 |
| 24 | MCQ | 1 | C |
| 25 | MCQ | 1 | A |
| 26 | NAT | 1 | 11 |
| 27 | MCQ | 1 | A |
| 28 | MSQ | 1 | A, C, D |
| 29 | MCQ | 1 | C |
| 30 | MCQ | 1 | C |
| 31 | MSQ | 1 | A, B, D |
| 32 | MCQ | 1 | D |
| 33 | MSQ | 1 | A, C, D |
| 34 | NAT | 1 | 3 |
| 35 | NAT | 1 | 2 |
| 36 | MCQ | 2 | B |
| 37 | MSQ | 2 | A, C |
| 38 | NAT | 2 | 432 |
| 39 | MSQ | 2 | A, C |
| 40 | MCQ | 2 | B |
| 41 | MSQ | 2 | A, B, C |
| 42 | MCQ | 2 | B |
| 43 | NAT | 2 | 3 |
| 44 | NAT | 2 | 3 |
| 45 | NAT | 2 | 5 |
| 46 | MSQ | 2 | B, C, D |
| 47 | MCQ | 2 | C |
| 48 | MCQ | 2 | D |
| 49 | NAT | 2 | 0 |
| 50 | NAT | 2 | 1.6667 (accepted range 1.66665–1.66675) |
| 51 | NAT | 2 | 7 |
| 52 | MCQ | 2 | C |
| 53 | MCQ | 2 | C |
| 54 | NAT | 2 | 275 |
| 55 | MCQ | 2 | A |
| 56 | MCQ | 2 | B |
| 57 | MSQ | 2 | A, C, D |
| 58 | MSQ | 2 | A, C, D |
| 59 | MSQ | 2 | A, C, D |
| 60 | MSQ | 2 | A, C, D |
| 61 | MCQ | 2 | B |
| 62 | MCQ | 2 | B |
| 63 | MSQ | 2 | A, C, D |
| 64 | NAT | 2 | 35 |
| 65 | NAT | 2 | 1 |
