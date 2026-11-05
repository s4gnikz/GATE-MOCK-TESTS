# GATE CS 2027 — Full-Length Mock Test 088

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

Select the numerical value that correctly answers the following problem.

A report lists the following mutually exclusive journey categories. A journey is chosen uniformly from all recorded journeys. What is the probability that it is a delayed journey lasting more than 20 minutes?

| Duration | Total journeys | Delayed journeys |
|---|---:|---:|
| At most 20 minutes | 40 | 6 |
| More than 20, at most 40 minutes | 35 | 14 |
| More than 40 minutes | 25 | 10 |

**Required precision:** Exact decimal.

A. 0.76  
B. 0.12  
C. 0.24  
D. 0.62

### Q2. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A square sheet is folded along both its horizontal and vertical midlines. Small holes are punched through all four layers, with every punch strictly away from the folds and sheet edges. Coordinates are measured from the original square's centre. Which set can be exactly the resulting hole centres after unfolding one punch?

**Candidate answers**
I. {(1,1),(−1,1),(1,−1),(−1,−1)}
II. {(1,1),(−1,1),(1,−1),(−2,−1)}
III. {(1,1),(−1,1)}
IV. {(1,1),(−1,−1)}

A. I: invalid; II: invalid; III: invalid; IV: invalid  
B. I: valid; II: invalid; III: valid; IV: invalid  
C. I: valid; II: invalid; III: invalid; IV: invalid  
D. I: invalid; II: valid; III: valid; IV: valid

### Q3. [1 Mark] [MCQ]

Arrange the sentences into the most coherent account. No other comparison, restoration or verification is implied.

P. The comparison showed that the missing entries were present in the backup.
Q. The librarian noticed gaps in the catalogue and compared it with a backup.
R. A final check then confirmed that the restored catalogue contained every entry.
S. Using that evidence, she restored the missing entries from the backup.

A. Q, P, S, R
B. P, Q, S, R
C. Q, S, P, R
D. Q, P, R, S

### Q4. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Two inlet pipes, working alone, fill an empty tank in 6 hours and 9 hours. With both inlets and a leak open, an initially empty tank fills in 4 hours. All rates are constant. How many hours would the leak alone take to empty a full tank?

**Required precision:** Integer hours.

A. 72  
B. 18  
C. 36  
D. 37

### Q5. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

“The conclusion is provisional and may be revised after further trials.” Which word is closest in meaning to provisional here?

**Candidate answers**
I. Irrevocable
II. Tentative
III. Unrelated
IV. Unanimous

A. I: valid; II: valid; III: invalid; IV: invalid  
B. I: invalid; II: valid; III: valid; IV: invalid  
C. I: valid; II: invalid; III: valid; IV: valid  
D. I: invalid; II: valid; III: invalid; IV: invalid

### Q6. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Two fair six-sided dice are rolled independently. Given that their scores differ by exactly one, what is the expected larger score?

**Required precision:** Integer.

A. 8  
B. 2  
C. 5  
D. 4

### Q7. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A proposed rule maps every integer n to n²+n+1. Observations for inputs1,2,3 give outputs3,7,13. Which statements are correct?

**Candidate answers**
I. The proposed rule agrees with all three observations.
II. These observations uniquely establish the rule for every integer input.
III. Adding (n−1)(n−2)(n−3) to the proposed rule gives another rule agreeing with the observations.
IV. The proposed rule predicts21 at input4.

A. I: invalid; II: invalid; III: valid; IV: valid  
B. I: valid; II: invalid; III: invalid; IV: valid  
C. I: invalid; II: valid; III: invalid; IV: invalid  
D. I: valid; II: invalid; III: valid; IV: valid

### Q8. [2 Marks] [NAT]

An urn contains three red and three blue balls. Two balls are drawn without replacement. If they have different colours, a prize of 6 units is paid; otherwise nothing is paid. What is the expected prize?

**Answer format:** Exact finite decimal.

### Q9. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

The three-digit strings000 through111 containing only binary digits are listed in increasing binary numerical order, with leading zeros retained. Between each consecutive pair, count how many digit positions change. What is the sum of these counts over all seven transitions?

**Required precision:** Integer.

A. 22  
B. 6  
C. 11  
D. 12

### Q10. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Two concentric circles have radii 5 and 3. A straight chord of the larger circle is tangent to the smaller circle. What is the chord's length?

**Required precision:** Integer.

A. 16  
B. 4  
C. 8  
D. 9

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

Two processes share a memory segment containing a counter initialized to0. Each performs one ordinary non-atomic read-increment-write operation. Which statements are correct without synchronization?

**Candidate answers**
I. A final value of1 is possible.
II. A final value of2 is possible.
III. Shared memory automatically makes each read-increment-write atomic.
IV. A final value of3 is possible from these two operations alone.

A. I: invalid; II: valid; III: invalid; IV: invalid  
B. I: valid; II: valid; III: valid; IV: invalid  
C. I: valid; II: valid; III: invalid; IV: invalid  
D. I: invalid; II: invalid; III: valid; IV: valid

### Q12. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

An L1 miss is served by L2 with conditional hit probability0.8. An L2 miss causes a main-memory access. If L1's miss probability is0.1, what fraction of all accesses reach main memory?

**Required precision:** Exact decimal.

A. 0.98  
B. 0.01  
C. 0.02  
D. 0.51

### Q13. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A circular singly linked list has traversal 1→2→3→4→1, and tail points to node 4. Execute tail.next=tail.next.next. Then insert a new node 5 immediately after tail and set tail to this new node. What traversal starts at the new head tail.next?

A. 1,2,3,4,5  
B. 5,2,3,4  
C. 2,3,4,5  
D. 2,3,5,4

### Q14. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A sequence satisfies a0=1 and an=2a(n−1)+1 for n≥1. Let A(x)=sum(an x^n), interpreted as a formal power series. What is the coefficient of x^4 in (1−2x)A(x)?

**Required precision:** Integer.

A. 2  
B. 1  
C. 0  
D. 3

### Q15. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A cache contains exactly one four-word line, initially invalid. It uses write-back and write-allocate. A word-store miss fetches the entire target line before updating the word; evicting a dirty line writes the entire line to memory. The accesses are store to block 0, store to block 1, load from block 0. Each access is to one word, blocks 0 and 1 differ, and there is no final cache flush. How many complete cache-line transfers between memory and cache occur, counting reads and write-backs?

**Required precision:** Integer.

A. 5  
B. 10  
C. 3  
D. 6

### Q16. [1 Mark] [MSQ]

Transaction T1 locks every existing row satisfying salary>100 and counts those rows twice. Between the counts, T2 inserts and commits a new row with salary150. The system uses only row locks on existing rows; no predicate or range locks are acquired. Which statements hold?

A. T1's locks need not prevent T2's insertion.
B. The second count can exceed the first despite locking all originally qualifying rows.
C. Locking existing rows necessarily locks every future row satisfying the same predicate.
D. A suitable predicate lock can prevent the insertion until T1 releases it.

### Q17. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let R be a binary relation on a nonempty domain. Which formula is the logical negation of

`forall x exists y [R(x,y) AND forall z (R(x,z) -> z=y)]`?

All variables in the options are bound as displayed.

A. exists x forall y [NOT R(x,y) OR exists z (R(x,z) AND z!=y)]  
B. exists x exists y [NOT R(x,y) OR exists z (R(x,z) AND z!=y)]  
C. forall x forall y [NOT R(x,y) AND exists z (R(x,z) AND z!=y)]  
D. exists x forall y [NOT R(x,y) OR forall z (R(x,z) AND z!=y)]

### Q18. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

The following basic block uses exact mathematical integers and ordinary scalar variables, with no aliases or externally visible intermediate states. All three final variable values must be preserved. Which replacement is equivalent for every initial value of b and c?
```text
a = b + c
b = a - c
c = a - b
```

**Candidate answers**
I. a = b + c
II. a = b + c; b = c
III. a = b + c; c = a
IV. a = b + c; b = a; c = 0

A. I: invalid; II: invalid; III: invalid; IV: invalid  
B. I: valid; II: invalid; III: valid; IV: invalid  
C. I: invalid; II: valid; III: valid; IV: valid  
D. I: valid; II: invalid; III: invalid; IV: invalid

### Q19. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A positive-edge-triggered D flip-flop has asynchronous active-low reset. Its clock remains low while reset is asserted. What happens to Q?

A. Q resets without waiting for a rising clock edge.  
B. Q can change only at the next rising edge, even under reset.  
C. Q must toggle repeatedly while reset remains asserted.  
D. Q becomes equal to the complement of D.

### Q20. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

An index lookup requires exactly three distinct index-page reads and returns matching record locations on data pages 4,4,7,9,7. Data and index pages are disjoint. Initially no page is cached; every page read remains cached throughout the query. How many page reads are required in total?

**Required precision:** Integer.

A. 12  
B. 3  
C. 6  
D. 7

### Q21. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A processor has a write-back data cache with no hardware coherence with DMA. It modifies a buffer, leaving the buffer's cache lines dirty, and then asks a DMA controller to copy that buffer from main memory to a device. The processor will not modify the buffer again during the transfer. Which action before starting DMA ensures that the device receives the updated data?

A. Invalidate the dirty lines without writing them back.  
B. Write back all dirty buffer lines and wait for completion.  
C. Disable device-completion interrupts.  
D. Wait for a DMA-completion interrupt before starting the DMA transfer.

### Q22. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Grammar S→aS | Sb | ε generates which language?

A. a*b*  
B. {aⁿbⁿ:n≥0}  
C. (ab)* only  
D. All strings over {a,b}

### Q23. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

Under C17, assume unsigned char has exactly eight bits and i is not modified by anything outside the displayed code. What is the behaviour of this loop?

```c
volatile unsigned char i = 250;
while (i < 255) {
    i = i + 2;
}
```

**Candidate answers**
I. It terminates with i=255.
II. It never terminates.
III. It terminates with i=0.
IV. The addition necessarily causes undefined signed overflow.

A. I: valid; II: valid; III: invalid; IV: invalid  
B. I: invalid; II: valid; III: valid; IV: invalid  
C. I: invalid; II: valid; III: invalid; IV: invalid  
D. I: valid; II: invalid; III: valid; IV: valid

### Q24. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

Coins of denominations 1,3,4 are available without limit. For amount 6, which statement correctly evaluates the rule “repeatedly choose the largest coin not exceeding the remaining amount”?

**Candidate answers**
I. It uses two coins and is optimal.
II. It uses three coins, whereas an optimal solution uses two.
III. It cannot make amount 6 at all.
IV. Every feasible solution uses three coins.

A. I: valid; II: valid; III: invalid; IV: invalid  
B. I: invalid; II: valid; III: invalid; IV: invalid  
C. I: invalid; II: valid; III: valid; IV: invalid  
D. I: valid; II: invalid; III: valid; IV: valid

### Q25. [1 Mark] [NAT]

A TCP sender transmits a SYN with sequence number 400, then 300 data bytes, then a FIN. There are no retransmissions or other data. What acknowledgment number acknowledges everything through the FIN? SYN and FIN each occupy one sequence number.

**Answer format:** Integer.

### Q26. [1 Mark] [NAT]

A disk head is at cylinder 50. Pending requests are at 10,45,55,90. Shortest-seek-time-first scheduling breaks an equal-distance tie in favour of the lower cylinder. No new requests arrive. What total cylinder distance is travelled to serve all requests?

**Answer format:** Integer.

### Q27. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A constant-propagation analysis proves x=4 on every feasible path reaching `y=3*x-2`. Arithmetic is exact. What replacement for the right-hand side is justified?

**Candidate answers**
I. 12
II. 10
III. 2
IV. No constant replacement can ever be made.

A. I: invalid; II: valid; III: invalid; IV: invalid  
B. I: valid; II: valid; III: invalid; IV: invalid  
C. I: invalid; II: valid; III: valid; IV: invalid  
D. I: valid; II: invalid; III: valid; IV: valid

### Q28. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

An edit-distance algorithm allows insertion, deletion and substitution, each of cost one. What is the minimum edit distance from `cat` to `cut`?

**Required precision:** Integer.

A. 1  
B. 2  
C. 0  
D. 3

### Q29. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A segmented address has segment number 2 and offset 120. Segment 2 has base 4000 and limit 100, where valid offsets are 0 through limit−1. What is the correct outcome of translation?

A. Physical address 4120.  
B. Physical address 4100.  
C. An address-bound violation.  
D. Physical address 120.

### Q30. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

An IPv4 fragment has fragment offset75 and carries240 bytes of payload. What is the offset, in bytes from the original datagram payload's beginning, of its final payload byte? Offset fields are in eight-byte units.

**Required precision:** Integer.

A. 1678  
B. 420  
C. 840  
D. 839

### Q31. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A signed eight-bit fixed-point code represents its two's-complement integer divided by16. The exactly represented numbers3.5 and−1.75 are added without overflow. What is the unsigned decimal interpretation of the eight stored result bits?

**Required precision:** Integer.

A. 56  
B. 14  
C. 28  
D. 29

### Q32. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A3×3 matrix A has determinant5. Matrix B is obtained by interchanging A's first and third rows and then multiplying its second column by−2. What is det(B)?

**Required precision:** Exact number.

A. 10  
B. 20  
C. 5  
D. 11

### Q33. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Let f(x)=|x| for real x. Which statements are correct at x=0?

**Candidates**

**I.** f is continuous.

**II.** Its left derivative is−1 and its right derivative is1.

**III.** Its derivative exists and equals0 because f has a minimum there.

**IV.** Every continuous function is differentiable there.

A. II and III  
B. II and IV  
C. I and II  
D. III and IV

### Q34. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A PDA can make epsilon transitions that do not consume input. Which statements are correct?

**Candidates**

**I.** An epsilon transition may still change the state and stack.

**II.** Every epsilon transition must leave the stack unchanged.

**III.** A computation can contain several epsilon transitions between consecutive consumed symbols.

**IV.** An epsilon transition consumes a special extra input character not in the input string.

A. I and III  
B. II and III  
C. II and IV  
D. III and IV

### Q35. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Two independent fair dice give values X,Y. Find E[X | X+Y=7 and X>Y].

**Required precision:** Integer.

A. 10  
B. 3  
C. 6  
D. 5

### Q36. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Functions f:{1,2,3}→{1,2,3} are chosen subject to f(f(x))=f(x) for every x. How many such functions exist?

**Required precision:** Integer.

A. 20  
B. 10  
C. 5  
D. 11

### Q37. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A binary floating-point format has three significant bits including the leading one, minimum normal exponent −2, gradual underflow and round-to-nearest ties-to-even. Compute 0.25×0.25, round to the format, then multiply that stored result by 0.5 and round again. What is the absolute relative error of the final stored result compared with the exact real product 0.25×0.25×0.5?

**Required precision:** Exact finite decimal.

A. 2  
B. 0  
C. 3  
D. 1

### Q38. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A B+ tree stores at most three keys in each leaf and at most three child pointers in each internal node. Its root initially has separator keys [20,40] and these three leaves, from left to right:

```text
[5,10,15]   [20,25,30]   [40,45,50]
```

Every separator is the smallest key in its right child subtree. Insert 35 and then 55. A leaf overflowing to four keys splits into two leaves with two keys each. An internal node overflowing to four children splits into two nodes with two children each; the boundary separator moves to its parent. Splitting the root creates a new root. Existing nodes are reused as one of the split halves. How many nodes, including the root and all leaves, exist after both insertions?

**Required precision:** Numeric value; integer.

A. 16  
B. 8  
C. 4  
D. 9

### Q39. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A real3×3 matrix A has eigenvalues1,2,4, each once. Define B=A²−3A+2I. What is the rank of B?

**Required precision:** Exact integer.

A. 2  
B. 0  
C. 1  
D. 3

### Q40. [2 Marks] [NAT]

A rooted tree has the parent array for vertices1 through7 given by[0,1,1,2,2,4,3], where0 marks the root. An operation cuts the subtree rooted at2 and reattaches its root as a child of7. How much does the sum of depths of all seven vertices increase, with the root's depth defined as0?

**Answer format:** Integer.

### Q41. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A pipeline has four stages with delays2,5,3,4 ns and a1 ns register overhead per stage boundary included in its clock period. It processes ten independent operations with one operation entering per cycle after start. What is total time from the first entry until the tenth result, counting four cycles for the first result?

**Required precision:** Integer nanoseconds.

A. 156  
B. 39  
C. 78  
D. 79

### Q42. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For n a power of two, consider the following routine. Each work() and every arithmetic or control operation takes constant time. What is its asymptotic running time?

```text
F(n):
    if n <= 1: return
    F(n/2)
    F(n/2)
    for i = 1 to n:
        for j = 1 to i:
            k = 1
            while k <= i:
                work()
                k = 2*k
```

A. Θ(n log n)  
B. Θ(n²)  
C. Θ(n² log n)  
D. Θ(n² (log n)²)

### Q43. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let L be any context-free language and R any regular language over the same alphabet. Which language is guaranteed to be context-free?

A. L∩R  
B. The complement of L  
C. The intersection of L with every context-free language  
D. The set difference R−L for every such L,R

### Q44. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A language L satisfies the regular pumping lemma's conclusion for some pumping length. What can be concluded from this fact alone?

**Candidate answers**
I. L is regular, since the condition is sufficient.
II. L is context-free but not regular.
III. It does not by itself prove regularity; the lemma supplies a necessary condition.
IV. L must be finite.

A. I: invalid; II: invalid; III: valid; IV: invalid  
B. I: valid; II: invalid; III: valid; IV: invalid  
C. I: invalid; II: invalid; III: invalid; IV: invalid  
D. I: valid; II: valid; III: invalid; IV: valid

### Q45. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A machine's ADD (R)+,(R)+ instruction first reads the source word at address R and increments R by four, then reads the destination word at the new R and increments R by four again, finally writing the sum to that destination's captured address. Initially R=100, M[100]=3 and M[104]=5. Which pair gives the final R and M[104]?

A. (104,6)  
B. (108,6)  
C. (108,8)  
D. (104,8)

### Q46. [2 Marks] [MSQ]

An algorithm is given a Turing machine M promised to halt on every input and an integer n≥0. Which tasks can be decided by an algorithm that terminates on every promised input?

A. Determine whether M accepts every binary string of length exactly n.
B. Determine whether M accepts at least one binary string of length at most n.
C. Determine whether M accepts every binary string of arbitrary length.
D. Determine whether M accepts no binary strings of arbitrary length.

### Q47. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A TLB lookup takes 2 ns and each physical memory access takes 50 ns, with no overlap. The page table has two levels in memory. A TLB hit needs only the final data access; a miss needs two page-table accesses followed by the data access. All pages are resident. If the TLB hit probability is 0.9, what is the mean access time in ns?

**Required precision:** Exact integer.

A. 124  
B. 31  
C. 62  
D. 63

### Q48. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A routing table contains prefix203.0.113.0/24 via X and more-specific prefix203.0.113.128/25 via Y. No other route matches. Which statements are correct under longest-prefix matching?

A. Address203.0.113.200 uses Y.  
B. Address203.0.113.100 uses X.  
C. Installing the /24 after the /25 necessarily makes it override the /25.  
D. Removing the /25 makes203.0.113.200 use X.

### Q49. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

Two internal TCP clients connect to the same external server through a translator sharing one public address. The translator assigns different public source ports. Which information is essential for routing a returning server segment to the correct internal connection?

**Candidate answers**
I. Only the external server's destination port, ignoring the translated port.
II. A translation mapping that includes the public-side connection endpoint information and its corresponding internal endpoint.
III. Only the Ethernet broadcast address.
IV. Only the length of the TCP payload.

A. I: invalid; II: valid; III: invalid; IV: invalid  
B. I: valid; II: valid; III: invalid; IV: invalid  
C. I: invalid; II: valid; III: valid; IV: invalid  
D. I: valid; II: invalid; III: valid; IV: valid

### Q50. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

Reads return the latest preceding write in this schedule:

```text
w1(x); r2(x); w2(y); r3(y); c1; c2; c3
```

Which properties hold?

**Candidate answers**
I. Recoverability.
II. Cascadelessness.
III. Conflict serializability.
IV. Strictness.

A. I: invalid; II: invalid; III: valid; IV: invalid  
B. I: valid; II: invalid; III: invalid; IV: invalid  
C. I: invalid; II: valid; III: invalid; IV: valid  
D. I: valid; II: invalid; III: valid; IV: invalid

### Q51. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In a binary tree with distinct keys, each node has a parent pointer. Given a pointer to x, an algorithm finds the next node in preorder traversal: if x has a left child, return it; otherwise, if x has a right child, return it; otherwise ascend. During ascent, when the current node is a left child and its parent has a right child, return that right child; if the root is passed, return NULL. What is the total time for starting at the root and repeatedly applying this algorithm until NULL, for a tree of n nodes?

A. Θ(log n) for every tree  
B. Θ(n)  
C. Θ(n log n) for every tree  
D. Θ(n²) for a path-shaped tree

### Q52. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Processor A has a 1 ns clock and base CPI 1. Loads constitute 30% of instructions, and 10% of loads incur a 20-cycle penalty in addition to base execution. Processor B halves the load-miss probability, retains base CPI 1 and the 20-cycle penalty, but may have a longer clock period. Penalties do not overlap and there are no other stalls. What is the largest clock period for B, in ns, for which its mean instruction time is no greater than A's? Round to four decimal places.

**Required precision:** Number to 4 decimal places.

A. 1.2308  
B. 2.4616  
C. 0.6154  
D. 2.2308

### Q53. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Independent unbiased bits a,b,c are supplied to two Boolean circuits. One computes F=(a OR b) AND (a OR c). The other computes G=(a AND b) OR (a AND c). What is the probability that their outputs differ?

**Required precision:** Exact decimal.

A. 0.75  
B. 0.25  
C. 0.13  
D. 0.63

### Q54. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A binary max-heap contains distinct keys 1 through 7 in an array indexed 1 through 7. The key 6 is at index 3. Which statement characterizes all possible positions of key 5?

A. It must be at index 2.  
B. It can be at any of indices 2,4,5,6,7.  
C. It can be at indices 2,6,7, and no others.  
D. It can be at index 1 or 2 only.

### Q55. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A three-variable Boolean function is1 on every input except000 and111. Product terms may cover only1-inputs. What is the minimum number of product terms in a sum-of-products implementation?

**Required precision:** Integer.

A. 3  
B. 6  
C. 2  
D. 4

### Q56. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A and B are real 4×4 matrices, each of rank 3. Which statements are correct?

A. rank(AB) is at least 2.  
B. rank(AB) can be 3.  
C. rank(AB) can be 1.  
D. rank(AB) can be 2.

### Q57. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A sparse file uses 4096-byte blocks and four-byte pointers. Its inode has eight direct pointers, one single-indirect pointer and one double-indirect pointer. Logical block numbers start at zero. Starting with no allocated data or indirect blocks, one byte is written in logical block 1032, then one byte in logical block 2061. Only necessary data and pointer blocks are allocated; holes consume no blocks, and the existing inode is not counted. How many blocks have been allocated after both writes?

**Required precision:** Integer.

A. 5  
B. 10  
C. 3  
D. 6

### Q58. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A directed graph has edges a→b,b→c,c→a,c→d,d→e,e→d,e→f. Which statements are correct?

**Candidate answers**
I. c and d are in the same strongly connected component.
II. Adding the edge f→b makes the entire graph strongly connected.
III. Reversing every edge preserves the partition into strongly connected components.
IV. In the original graph, f can reach a.

A. I: valid; II: valid; III: valid; IV: invalid  
B. I: invalid; II: valid; III: invalid; IV: invalid  
C. I: valid; II: invalid; III: invalid; IV: valid  
D. I: invalid; II: valid; III: valid; IV: invalid

### Q59. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

An undirected graph has triangle vertices A,B,C with all three triangle edges of weight1. Vertex D is joined to A by a weight2 edge and to B by a weight3 edge; there are no other edges. How many distinct minimum spanning trees does the graph have?

**Required precision:** Integer.

A. 6  
B. 2  
C. 4  
D. 3

### Q60. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Two four-bit two's-complement operands A,B independently range over all 16 bit patterns. How many of the 256 ordered operand pairs cause signed overflow when their sum is retained in four bits?

**Required precision:** Integer.

A. 64  
B. 128  
C. 32  
D. 65

### Q61. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A component is faulty with probability 1/4. Each test is positive with probability 4/5 for a faulty component and 1/10 for a sound component. Repeated results are conditionally independent given the component's status. Testing stops at the first negative result or after three tests, whichever occurs first. N is the number of tests performed. Which statements are correct?

**Candidate answers**
I. E[N]=577/400.
II. P(faulty | N=3)=512/515.
III. Given that exactly two positive results were observed before a negative result, the probability of a faulty component is 128/155.
IV. Given that the first result was positive and the stopping result was negative, the probability of a faulty component is 32/65.

A. I: invalid; II: invalid; III: valid; IV: valid  
B. I: valid; II: invalid; III: invalid; IV: valid  
C. I: valid; II: invalid; III: valid; IV: valid  
D. I: invalid; II: valid; III: invalid; IV: invalid

### Q62. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A block computes t=a+b, then branches. Path P executes a=a+1, while path Q changes neither a nor b. At the join, u=a+b is computed. Arithmetic is over mathematical integers. Which statements are correct?

**Candidate answers**
I. On path P, the join expression equals t+1.
II. Replacing u by t on both paths is valid.
III. The original t is overwritten by updating a.
IV. Selecting t+1 for path P and t for path Q preserves u.

A. I: invalid; II: invalid; III: invalid; IV: valid  
B. I: valid; II: invalid; III: valid; IV: valid  
C. I: invalid; II: valid; III: valid; IV: invalid  
D. I: valid; II: invalid; III: invalid; IV: valid

### Q63. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A process opens a file, obtaining descriptor3 with file offset0, and then duplicates descriptor3 to descriptor4 using dup. It reads6 bytes through descriptor3, seeks through descriptor4 to absolute offset2, and reads3 bytes through descriptor3. All operations succeed fully. What file offset is then observed through descriptor4?

**Required precision:** Integer.

A. 10  
B. 3  
C. 6  
D. 5

### Q64. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A TCP sender has congestion window 10 segments, advertised receive window 12 segments and eight unacknowledged segments. It first sends as many additional segments as allowed. A subsequent cumulative ACK acknowledges five of the outstanding segments; for the next send decision, congestion window is set to eight and the new advertised receive window is six segments. There are no retransmissions or other changes. How many new segments can be sent in total across these two send decisions?

**Required precision:** Integer.

A. 6  
B. 2  
C. 4  
D. 3

### Q65. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A lock manager uses shared and exclusive locks. Initially T1 holds S(A), T2 holds S(A) and S(B), and T3 holds S(B). T1 then requests X(B); T3 requests X(A); T2 requests an upgrade to X(A). All three requests wait, all existing locks are retained, and a request waits only for incompatible locks held by other transactions. How many directed edges are in the wait-for graph, counting each ordered pair once?

**Required precision:** Integer.

A. 10  
B. 5  
C. 3  
D. 6

## ANSWER KEY — MOCK TEST 088

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | C |
| 2 | MCQ | 1 | C |
| 3 | MCQ | 1 | A |
| 4 | MCQ | 1 | C |
| 5 | MCQ | 1 | D |
| 6 | MSQ | 2 | A, B, C |
| 7 | MCQ | 2 | D |
| 8 | NAT | 2 | 3.6 |
| 9 | MSQ | 2 | A, B, D |
| 10 | MCQ | 2 | C |
| 11 | MCQ | 1 | C |
| 12 | MSQ | 1 | A, B, D |
| 13 | MSQ | 1 | A, B, D |
| 14 | MCQ | 1 | B |
| 15 | MSQ | 1 | B, C, D |
| 16 | MSQ | 1 | A, B, D |
| 17 | MSQ | 1 | B, C, D |
| 18 | MCQ | 1 | D |
| 19 | MSQ | 1 | B, C, D |
| 20 | MSQ | 1 | A, B, D |
| 21 | MSQ | 1 | A, C, D |
| 22 | MSQ | 1 | B, C, D |
| 23 | MCQ | 1 | C |
| 24 | MCQ | 1 | B |
| 25 | NAT | 1 | 702 |
| 26 | NAT | 1 | 130 |
| 27 | MCQ | 1 | A |
| 28 | MCQ | 1 | A |
| 29 | MSQ | 1 | A, B, D |
| 30 | MCQ | 1 | D |
| 31 | MCQ | 1 | C |
| 32 | MCQ | 1 | A |
| 33 | MCQ | 1 | C |
| 34 | MCQ | 1 | A |
| 35 | MSQ | 1 | A, B, C |
| 36 | MSQ | 2 | A, C, D |
| 37 | MCQ | 2 | D |
| 38 | MSQ | 2 | A, C, D |
| 39 | MSQ | 2 | A, B, D |
| 40 | NAT | 2 | 8 |
| 41 | MCQ | 2 | C |
| 42 | MSQ | 2 | A, B, D |
| 43 | MSQ | 2 | B, C, D |
| 44 | MCQ | 2 | A |
| 45 | MSQ | 2 | A, B, D |
| 46 | MSQ | 2 | A, B |
| 47 | MCQ | 2 | C |
| 48 | MCQ | 2 | C |
| 49 | MCQ | 2 | A |
| 50 | MCQ | 2 | D |
| 51 | MSQ | 2 | A, C, D |
| 52 | MCQ | 2 | A |
| 53 | MSQ | 2 | A, C, D |
| 54 | MSQ | 2 | A, B, D |
| 55 | MCQ | 2 | A |
| 56 | MCQ | 2 | C |
| 57 | MSQ | 2 | B, C, D |
| 58 | MCQ | 2 | D |
| 59 | MSQ | 2 | A, B, C |
| 60 | MCQ | 2 | A |
| 61 | MCQ | 2 | C |
| 62 | MCQ | 2 | D |
| 63 | MSQ | 2 | A, B, C |
| 64 | MSQ | 2 | A, B, C |
| 65 | MCQ | 2 | B |
