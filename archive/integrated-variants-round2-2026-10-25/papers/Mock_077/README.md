# GATE CS 2027 — Full-Length Mock Test 077

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

Arrange these steps into a logically coherent experimental sequence: P, record the result; Q, formulate a hypothesis; R, design a test of that hypothesis; S, conduct that test.

A. Q–R–S–P
B. R–Q–P–S
C. P–S–R–Q
D. Q–P–R–S

### Q2. [1 Mark] [NAT]

Household A has three boys. Household B has one boy and one girl. Choose a household with equal probability, then choose one of its children uniformly. Given that the selected child is a boy, what is the probability that household A was chosen?

**Answer format:** Round to four decimal places; accepted tolerance ±0.00005 around the rounded answer.

### Q3. [1 Mark] [MCQ]

Choose the words that fit: “The researcher made ___ measurements at separate time instants and was ___ when discussing confidential results.” Here the first blank means distinct, and the second means tactful.

A. discreet; discrete
B. discrete; discreet
C. discrete; discrete
D. discreet; discreet

### Q4. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An arrow initially points in the positive x direction in a coordinate plane. First reflect the entire plane in the line y=x. Then rotate it clockwise by 90 degrees about the origin. Finally reflect it in the y-axis. In which direction does the arrow point?

A. Positive x  
B. Negative x  
C. Positive y  
D. Negative y

### Q5. [1 Mark] [MCQ]

An inspector accepts or rejects cards using one of the four candidate rules below. Each card has one colour, one shape, and is either filled or hollow. Observations are:

| Colour | Shape | Appearance | Decision |
|---|---|---|---|
| Red | Circle | Filled | Reject |
| Red | Circle | Hollow | Accept |
| Red | Square | Filled | Accept |
| Blue | Circle | Filled | Reject |
| Blue | Circle | Hollow | Reject |

Which candidate rule agrees with every observation?

A. Accept if the card is red and is either circular or filled, including when both hold.  
B. Accept if the card is red and exactly one of “circular” and “filled” holds.  
C. Accept if exactly one of “circular” and “filled” holds, regardless of colour.  
D. Accept if the card is red or circular, including when both hold.

### Q6. [2 Marks] [NAT]

A solid cube of side3 is assembled from27 unit cubes. The central unit cube of each of the six faces and the unit cube at the centre of the large cube are removed. All remaining unit cubes stay in place. What is the total area of the remaining solid's exposed surfaces, including surfaces inside the resulting passages?

**Answer format:** Integer square units.

### Q7. [2 Marks] [MCQ]

Three tasks A,B,C take 4,3,2 hours. A and B may run simultaneously on separate workers, but C requires both to have finished and uses one worker. Exactly two workers are available and tasks cannot be split. What is the minimum completion time for all tasks?

A. 5 hours
B. 6 hours
C. 7 hours
D. 9 hours

### Q8. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A rectangular garden is 16 m long and 10 m wide. A path of uniform width is laid inside all four edges, leaving a smaller rectangular planted region. The path occupies 88 square metres. What is the width of the path?

A. 1 m  
B. 2 m  
C. 3 m  
D. 4 m

### Q9. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Arrange the sentences into a coherent paragraph.

P. To distinguish these explanations, the researchers repeated the trial with freshly calibrated instruments.
Q. The repeated trial again found the increase, weakening the calibration explanation.
R. The first trial showed a temperature increase, but the team was unsure whether it was real or caused by instrument drift.
S. They therefore concluded that further investigation of the physical cause was warranted.

A. P–R–Q–S  
B. R–Q–P–S  
C. R–P–Q–S  
D. S–R–P–Q

### Q10. [2 Marks] [MCQ]

A tank contains 120 litres of a well-mixed milk-water mixture in the ratio 3:2. First, 30 litres are removed and replaced with water. After thorough mixing, 20 litres are removed and replaced with pure milk. What is the final ratio of milk to water? Volumes are additive.

A. 11:13  
B. 13:11  
C. 3:2  
D. 7:5

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

A timestamp protocol handles a write by transaction timestamp t as follows: abort if t<readTS(x); otherwise ignore the write if t<writeTS(x); otherwise perform it. Initially readTS(x)=5 and writeTS(x)=9. Two separate attempts are considered from this same initial state, with t=7 and t=4. What are their respective outcomes?


A. Perform, ignore
B. Abort, ignore
C. Ignore, abort
D. Perform, abort

### Q12. [1 Mark] [NAT]

A compiler lays out local objects in declaration order at increasing offsets from zero: char c, int i, double d, char e. Sizes and required alignments are respectively (1,1),(4,4),(8,8),(1,1) bytes. Each object's start is rounded up to its required alignment, and total local storage is rounded up to a multiple of eight. How many bytes are allocated?

**Answer format:** Integer.

### Q13. [1 Mark] [NAT]

For n=16, how many times does work() execute?

```text
i = n
while i > 0:
    for j = 1 to i:
        work()
    i = floor(i/2)
```

**Answer format:** Integer.

### Q14. [1 Mark] [MCQ]

An expression translator uses this grammar and emits postfix code. For E→E−T it emits the left E's code, then T's code, then “−”. For E→T and T→digit it emits the child's code and the digit respectively. What is emitted for 8−3−2?

A. 8 3 2 − −  
B. − − 8 3 2  
C. 8 3 − 2 −  
D. 8 − 3 − 2

### Q15. [1 Mark] [NAT]

Weighted intervals are [0,4) with weight 9, [0,2) with weight 4 and [2,4) with weight 4. Nonoverlapping intervals may share an endpoint. An algorithm repeatedly selects the available interval with earliest finish time, then removes conflicting intervals. By how much is its total weight below the optimum?

**Answer format:** Integer.

### Q16. [1 Mark] [NAT]

A block contains four data bits followed by one even-parity bit. Exactly one of the five transmitted bits is flipped. How many different one-bit error patterns are undetected by the parity check?

**Answer format:** Integer.

### Q17. [1 Mark] [MSQ]

A deterministic finite automaton has missing transitions, which cause immediate rejection. To recognize the complement over the same alphabet, which statements are correct?

A. Swapping accepting and rejecting states alone always suffices.
B. Completing the automaton with a rejecting sink before swapping accepting states works.
C. A word rejected by taking a missing transition must be accepted by a correct complement automaton.
D. Adding a sink after swapping states and leaving that sink rejecting always works.

### Q18. [1 Mark] [MCQ]

On the set of residues {0,1,2,3,4} modulo 5, define permutations f(x)=2x mod 5 and g(x)=(x+1) mod 5. Let h=f composed with g composed with f-inverse composed with g-inverse; the rightmost map acts first. What is the smallest positive integer k for which h applied k times is the identity?

A. 1  
B. 2  
C. 4  
D. 5

### Q19. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Grammar G has start symbol S and productions S→aSb | aS | epsilon. Which strings are generated?

**Candidates**

**I.** aab

**II.** abb

**III.** aaabb

**IV.** ba

A. II and IV  
B. III and IV  
C. I and II  
D. I and III

### Q20. [1 Mark] [MSQ]

On a UNIX-like file system, path p refers to regular file F. Process R has already opened F for reading. Process W creates a different regular file G and atomically renames G over p. No process modifies F or G afterward. Assume rename succeeds and no symbolic links are involved. Which statements hold?

A. R's existing descriptor still refers to F.
B. A later successful open of p refers to G.
C. The rename necessarily changes the inode referred to by R's existing descriptor.
D. F's storage must be reclaimed before the rename can return, even while R retains its descriptor.

### Q21. [1 Mark] [NAT]

A lexically scoped language permits variable shadowing. In the code below, each declaration introduces a distinct variable and declarations take effect immediately. How many distinct declared variables are referenced by the three print expressions, collectively?

```text
var x;
var y;
{
    var x;
    print(x);
    {
        var y;
        print(x + y);
    }
    print(y);
}
```

**Answer format:** Integer.

### Q22. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An undirected graph consists of triangles abc and def together with the single connecting edge cd. Which statements are correct?

**Candidates**

**I.** It has a perfect matching.

**II.** Every perfect matching contains cd.

**III.** It is bipartite.

**IV.** Its minimum vertex cover has size3.

A. I and II  
B. III and IV  
C. I and III  
D. I and IV

### Q23. [1 Mark] [NAT]

A recursive routine visits a binary tree as follows. A null pointer returns immediately; a non-null call invokes the routine on both children, even when a child pointer is null. If the tree has 12 non-null vertices, how many calls receive a null pointer?

**Answer format:** Exact integer.

### Q24. [1 Mark] [MCQ]

A combinational block receives two bits a,b and must output 1 exactly when the two-bit unsigned value is prime. Which output function is correct?

A. a
B. b
C. a XOR b
D. a AND b

### Q25. [1 Mark] [NAT]

A process opens a regular file for reading, obtaining descriptor p with file offset 0, and then executes q=dup(p). It performs the following successful operations in order: read 2 bytes through p; read 3 bytes through q; seek through p to absolute byte offset 1; read 1 byte through q. The file is long enough for every read. What is the resulting shared file offset? Offsets are zero-based.

**Answer format:** Numeric value; integer.

### Q26. [1 Mark] [NAT]

Two D flip-flops store bits q1,q0. On every clock edge, q1 becomes the old q0 and q0 becomes NOT(old q1 XOR old q0). Starting at 00, what is the least positive number of edges after which the state is 00 again?

**Answer format:** Exact integer.

### Q27. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

What does this conforming C program print? Array indices are valid and all arithmetic is representable.

```c
#include <stdio.h>
void f(int a[], int n) {
    int *p = a;
    a = a + 1;
    a[n-2] = p[0] + a[0];
}
int main(void) {
    int x[] = {4,7,9};
    f(x,3);
    printf("%d %d\n", x[0],x[2]);
    return 0;
}
```

A. 7 11  
B. 4 11  
C. 4 9  
D. 11 9

### Q28. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A learning Ethernet switch's forwarding table is initially empty. Host A on port 1 sends a unicast frame to host B, which is on port 2. The switch has three ports and no filtering restrictions. What does the switch do with this first frame?

A. Learn B on port 1 and forward only to port 2.  
B. Learn A on port 1 and flood through ports 2 and 3.  
C. Learn A on port 2 and drop the frame.  
D. Learn both A and B from the frame and forward only to port 2.

### Q29. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A weak entity Installment is identified by its owner Loan and its partial key installment_number. Loan has primary key loan_id. Each installment has exactly one owner, and the same installment_number may occur under different loans. Which primary key preserves this identification when mapping Installment to a relation?

A. installment_number alone.  
B. loan_id alone.  
C. (loan_id, installment_number).  
D. amount alone.

### Q30. [1 Mark] [NAT]

Among real triples satisfying x+y+z=6 and x−y=0, what is the minimum possible value of x²+y²+z²?

**Answer format:** Integer.

### Q31. [1 Mark] [NAT]

A formal power series F(x) satisfies(1−x)²F(x)=1+x. What is the coefficient of x4 in F(x)?

**Answer format:** Integer.

### Q32. [1 Mark] [NAT]

Four routers S,A,B,C have undirected links SA,SB,AC,BC,AB. S originates one new link-state advertisement and sends it on every incident link. Each other router, on its first receipt, forwards one copy on every incident link except the one on which that first copy arrived; later duplicates are discarded without forwarding. Links are reliable, and acknowledgement traffic is ignored. How many advertisement transmissions occur in total, counting each direction separately?

**Answer format:** Integer.

### Q33. [1 Mark] [NAT]

How many truth assignments to p,q,r satisfy (p→q)∧(q→r)∧(r→p)?

**Answer format:** Integer.

### Q34. [1 Mark] [NAT]

A cache lookup takes2 ns. A miss adds60 ns after that lookup. A stream contains100 accesses; exactly10 miss, and no overlap is allowed. An optimization removes five misses but adds1 ns to every lookup. What is the net reduction in total time, in ns?

**Answer format:** Integer.

### Q35. [1 Mark] [NAT]

A 16 KiB cache has four ways and 64-byte lines. How many sets does it have? Count data capacity only; 1 KiB=1024 bytes.

**Answer format:** Integer.

### Q36. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An NPDA recognizes strings ww^R over {a,b} by nondeterministically choosing a midpoint, pushing before the midpoint and matching/popping afterward. It accepts only when the input is exhausted and the stack is empty. Which statement correctly explains the midpoint choice?

A. Every midpoint guess must accept for the input to be accepted.  
B. A successful branch must choose a midpoint leaving equally long push and pop portions; wrong guesses may reject.  
C. The machine needs two stacks to compare the reverse.  
D. Nondeterminism allows acceptance with unread symbols.

### Q37. [2 Marks] [NAT]

Singly linked nodes initially form A: 1→2→3→4→null and B: 9→3→4→null, sharing the actual nodes 3 and 4. The A list is reversed in place by changing its nodes' next pointers; B's head pointer is unchanged. What is the sum of node labels encountered from B's head after the reversal?

**Answer format:** Integer.

### Q38. [2 Marks] [MCQ]

A process initially has three threads. One thread calls fork under POSIX semantics, and the child does not call exec. No further threads are created. Which statement is correct immediately after fork?

A. Parent and child each have three threads.
B. The parent has three threads, and the child has one thread.
C. The parent has one thread, and the child has three threads.
D. Both processes have one thread.

### Q39. [2 Marks] [NAT]

Values1,2,3,4,5 arrive in that order at a single stack, with pushes and pops interleaved as needed. What is the minimum stack capacity permitting the complete pop sequence3,4,2,1,5?

**Answer format:** Integer elements.

### Q40. [2 Marks] [NAT]

A compiler translates a short-circuit Boolean expression (p AND q) OR r into a decision graph. Each predicate occurrence is evaluated at most once on any execution, in source short-circuit order. How many different subsets of {p,q,r} can be evaluated during an execution, as their truth values vary?

**Answer format:** Integer.

### Q41. [2 Marks] [NAT]

Weighted activities have half-open intervals and values: A=[0,2), value 4; B=[2,4), value 4; C=[0,4), value 8; D=[4,5), value 1. How many distinct compatible subsets achieve the maximum total value? The empty subset is permitted but need not be optimal.

**Answer format:** Integer.

### Q42. [2 Marks] [MSQ]

Processes P and Q communicate through a finite-capacity pipe. P writes until the pipe is full; Q still has an open read end but never reads. Assume blocking writes and no signals or failures. Which statements are correct?

A. P may block on a further write.
B. Keeping a read end open guarantees that Q consumes bytes.
C. Closing all read ends changes the situation from merely having a full pipe.
D. A finite buffer guarantees completion for an arbitrarily large write workload even if Q never reads.

### Q43. [2 Marks] [MSQ]

Let M have rows (2,1,0),(1,1,1),(0,1,2). For arbitrary b=(b1,b2,b3)ᵀ, consider Mx=b over the real numbers. Which statements are correct?

A. M has rank 2.  
B. The null space is spanned by (1,−2,1)ᵀ.  
C. Mx=b is consistent exactly when b1−2b2+b3=0.  
D. Every consistent system Mx=b has a unique solution.

### Q44. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Under set semantics let R(A,B)={(1,x),(2,y)}, S(B) be empty, and U(A)={1,2,3}. Standard relational division R÷S uses candidate A values from π_A(R). Separately, a query selects each A in U for which no B in S lacks a matching tuple in R. Which statements are true?

**Candidates**

**I.** R÷S returns {1,2}.

**II.** R÷S returns {1,2,3}.

**III.** The separately described query returns {1,2,3}.

**IV.** Both results must be empty because S is empty.

A. II and IV  
B. I and III  
C. III and IV  
D. I and II

### Q45. [2 Marks] [MCQ]

Relations Employee(e,d), Required(d,p) and Done(e,p) contain the following tuples (set semantics):
```text
Employee = {(u,A), (v,A), (w,B), (z,C)}
Required = {(A,p), (A,q), (B,q)}
Done     = {(u,p), (u,q), (u,r), (v,p), (v,q), (w,q), (z,r)}
```
Let E be the set of employee identifiers e for which there exists an Employee tuple (e,d) satisfying
`for every project identifier t: Done(e,t) if and only if Required(d,t)`.
Quantification is over all project identifiers, and no tuples other than those listed exist. Which set is E?

A. {u,v,w}  
B. {v,w}  
C. {v,w,z}  
D. {u,v,w,z}

### Q46. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An IPv4 receiver reassembles fragments using the tuple(source address,destination address,protocol,identification). Two fragments have the same identification value but different source addresses. Which statements are correct under this rule?

**Candidates**

**I.** They belong to different reassembly contexts.

**II.** Equal identification values alone are sufficient to combine them.

**III.** The fragment offset determines placement within a context rather than replacing the context key.

**IV.** Arrival order alone uniquely identifies which datagram each fragment belongs to.

A. III and IV  
B. I and II  
C. I and IV  
D. I and III

### Q47. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

The input sequence 1,2,3,4,5 is passed through one stack. Each input may be pushed only in this order; a pop emits the current top. Which output permutations are possible?

**Candidates**

**I.** 3,2,1,5,4

**II.** 3,1,2,4,5

**III.** 2,4,3,5,1

**IV.** 4,2,3,1,5

A. II and IV  
B. III and IV  
C. I and III  
D. I and II

### Q48. [2 Marks] [MCQ]

Let L be the binary strings containing equally many 0s and 1s. Define K={w: there exists z in 0* such that wz is in L}. Which description of K is correct? Counts refer to w.

A. Number of 0s equals number of 1s.  
B. Number of 0s is at most number of 1s.  
C. Number of 0s is at least number of 1s.  
D. Every binary string belongs to K.

### Q49. [2 Marks] [NAT]

Shared x initially equals0. Two threads each execute this sequence once, using the same binary semaphore mutex initially1:

```text
wait(mutex);
t = x;          // t is local to the thread
x = t + 1;
signal(mutex);
```

A third thread performs only wait(mutex); signal(mutex). All three threads finish successfully. How many distinct final values of x are possible?

**Answer format:** Exact integer.

### Q50. [2 Marks] [NAT]

A signed eight-bit fixed-point format has three fractional bits. An exact real result of 17 is converted to this format using saturation to the largest representable value on positive overflow. What real value is stored?

**Answer format:** Exact finite decimal.

### Q51. [2 Marks] [NAT]

A CPU would execute1000 instructions at a CPI of2. A DMA controller transfers100 words, stealing one CPU cycle per word; each stolen cycle stalls the CPU by exactly one cycle, and there are no other effects. An alternative programmed-I/O method adds four CPU cycles per word and uses no DMA stalls. How many CPU clock cycles does DMA save over programmed I/O for the same computation and transfer?

**Answer format:** Integer.

### Q52. [2 Marks] [MSQ]

Let L={a^m b^n : m and n are positive integers, and m divides n}. For an arbitrary integer p≥2 choose w=a^p b^p. Consider every decomposition w=xyz satisfying |xy|≤p and |y|≥1. Which choices of pumping exponent i guarantee that xy^i z is outside L for every such decomposition?

A. i=0
B. i=1
C. i=2
D. i=p+2

### Q53. [2 Marks] [MCQ]

Table T(k,v) contains exactly these rows; NULL denotes the SQL null value, and duplicates are retained:
```text
(1,10), (1,NULL), (1,10), (2,NULL), (2,NULL), (3,5)
```
What rows, in any order, does the following standard SQL query return?
```sql
SELECT k, COUNT(*) AS n, COUNT(v) AS c
FROM T
GROUP BY k
HAVING COUNT(v) < COUNT(*) AND SUM(v) >= 10;
```

A. (1,3,2) only  
B. (1,3,2) and (2,2,0)  
C. (1,2,1) only  
D. No rows

### Q54. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

In a language with exact integer arithmetic, division by zero raises an observable exception. Consider `t=1/x; t=2; print(t);`, with x unchanged and print observable. Which statements are correct?

**Candidates**

**I.** The first assignment can always be removed because its stored value is dead.

**II.** Its stored value is dead, but its possible exception can prevent unconditional removal.

**III.** Both assignments can always be removed, leaving print(t) with t's old value.

**IV.** If x is proved nonzero, the whole fragment may be replaced by print(2).

A. II and IV  
B. I and IV  
C. II and III  
D. III and IV

### Q55. [2 Marks] [MSQ]

A forwarding table routes 10.2.0.0/25 and 10.2.0.128/25 to next hop H, and 10.2.0.64/26 to next hop J. A default route goes to K. Replace the two /25 entries by 10.2.0.0/24→H while retaining the /26 exception and default. Under longest-prefix matching, which statements are true?

A. Every destination keeps the same next hop.
B. The /24 aggregate overrides the /26 exception because it was inserted later.
C. Destinations outside 10.2.0.0/24 continue using the default route.
D. Removing the /26 exception as well would preserve every destination's next hop.

### Q56. [2 Marks] [NAT]

A processor can issue one instruction per cycle. A loop has 100 instructions, including ten branches. Exactly three of the branches mispredict, each inserting four cycles with no issue. Each of eight cache misses adds five stall cycles, but two of those misses occur entirely during branch-stall intervals and add no extra cycles. All other penalties are disjoint. Ignoring pipeline fill/drain, how many cycles does the loop take?

**Answer format:** Integer.

### Q57. [2 Marks] [MSQ]

For x≠0 define g(x)=sin(1/x). Which statements are correct?

A. There exists a sequence of positive x approaching0 on which g(x)=1.
B. There exists a sequence of positive x approaching0 on which g(x)=−1.
C. The limit of xg(x) as x approaches0 is0.
D. Assigning g(0)=0 makes g continuous at0.

### Q58. [2 Marks] [NAT]

A divide-and-conquer procedure on an array of length8 splits each nonsingleton interval into equal halves and recurses on both. At each internal node it merges the halves into a new buffer, writing every element exactly once; singleton leaves perform no writes. How many element writes occur across all merge buffers?

**Answer format:** Integer.

### Q59. [2 Marks] [NAT]

A binary floating-point system has three significant bits, including the leading1, and sufficient exponent range. It rounds each operation to nearest, with ties to an even significand low bit. Compute the absolute difference between fl(fl(8+1)−8) and fl(8+fl(1−8)). Here fl means rounding one operation in that format.

**Answer format:** Exact number.

### Q60. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A router receives destination 172.16.5.200. Its routes are 172.16.0.0/16→A, 172.16.4.0/22→B, 172.16.5.128/25→C, and a default route→D. A forwarding policy first chooses the longest matching prefix; among equal-length matches it chooses the lowest metric. The /25 route has metric 100 and the /22 route metric 1. Which next hop is selected, and why?

A. B, because metric 1 is smaller than 100.  
B. C, because prefix length is considered before metric.  
C. A, because a /16 covers more addresses.  
D. D, because the overlapping routes are ambiguous.

### Q61. [2 Marks] [NAT]

For a Boolean function F(x,y,z), define its Boolean difference with respect to a variable as the XOR of its restrictions when that variable is zero and one. How many functions satisfy all of the following: the difference with respect to x equals y for every y,z; the difference with respect to z equals one for every x,y; and F(0,0,0)=0?

**Answer format:** Integer.

### Q62. [2 Marks] [NAT]

X and Y are independent numbers of failures before the first success in repeated independent Bernoulli trials, each with success probability 1/3. What is E[min(X,Y)]?

**Answer format:** Decimal rounded to two places.

### Q63. [2 Marks] [MSQ]

A constant-propagation pass treats integer comparisons exactly and removes unreachable branches. Integer arithmetic is unbounded. Consider:

```text
x=0;
if x==0 { y=4; } else { y=input(); }
z=y*y;
```

Which statements hold?

A. The call input() is unreachable.
B. z can be replaced by16 after proving the branch condition.
C. It is necessary to execute input() to determine whether z is constant.
D. y is nonconstant solely because one syntactic assignment uses input().

### Q64. [2 Marks] [NAT]

A byte-addressed processor fetches instructions of lengths 2 or 4 bytes. Starting at address 100, it executes a 2-byte instruction, a 4-byte instruction, and then a 2-byte PC-relative branch. The branch target is computed from the next-instruction address plus a signed displacement measured in two-byte units. The branch displacement is −3. What is the target byte address?

**Answer format:** Integer.

### Q65. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Let f:{a,b,c}→{0,1} satisfy f(a)=f(b)=0 and f(c)=1. Which statements are correct?

**Candidates**

**I.** Exactly two functions g:{0,1}→{a,b,c} satisfy f composed with g equal to the identity on{0,1}.

**II.** Some function g satisfies g composed with f equal to the identity on{a,b,c}.

**III.** Every g satisfying the identity in A is injective.

**IV.** f is injective.

A. III and IV  
B. I and III  
C. I and II  
D. I and IV

## ANSWER KEY — MOCK TEST 077

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | A |
| 2 | NAT | 1 | 0.6667 (accepted range 0.66665–0.66675) |
| 3 | MCQ | 1 | B |
| 4 | MSQ | 1 | A, C, D |
| 5 | MCQ | 1 | B |
| 6 | NAT | 2 | 72 |
| 7 | MCQ | 2 | B |
| 8 | MSQ | 2 | A, C, D |
| 9 | MSQ | 2 | A, B, D |
| 10 | MCQ | 2 | B |
| 11 | MCQ | 1 | C |
| 12 | NAT | 1 | 24 |
| 13 | NAT | 1 | 31 |
| 14 | MCQ | 1 | C |
| 15 | NAT | 1 | 1 |
| 16 | NAT | 1 | 0 |
| 17 | MSQ | 1 | B, C |
| 18 | MCQ | 1 | D |
| 19 | MCQ | 1 | D |
| 20 | MSQ | 1 | A, B |
| 21 | NAT | 1 | 3 |
| 22 | MCQ | 1 | A |
| 23 | NAT | 1 | 13 |
| 24 | MCQ | 1 | A |
| 25 | NAT | 1 | 2 (exact) |
| 26 | NAT | 1 | 3 |
| 27 | MSQ | 1 | A, C, D |
| 28 | MSQ | 1 | A, C, D |
| 29 | MSQ | 1 | A, B, D |
| 30 | NAT | 1 | 12 |
| 31 | NAT | 1 | 9 |
| 32 | NAT | 1 | 7 |
| 33 | NAT | 1 | 2 |
| 34 | NAT | 1 | 200 |
| 35 | NAT | 1 | 64 |
| 36 | MSQ | 2 | A, C, D |
| 37 | NAT | 2 | 15 |
| 38 | MCQ | 2 | B |
| 39 | NAT | 2 | 3 |
| 40 | NAT | 2 | 3 |
| 41 | NAT | 2 | 2 |
| 42 | MSQ | 2 | A, C |
| 43 | MSQ | 2 | A, B, C |
| 44 | MCQ | 2 | B |
| 45 | MCQ | 2 | B |
| 46 | MCQ | 2 | D |
| 47 | MCQ | 2 | C |
| 48 | MCQ | 2 | B |
| 49 | NAT | 2 | 1 |
| 50 | NAT | 2 | 15.875 |
| 51 | NAT | 2 | 300 |
| 52 | MSQ | 2 | C, D |
| 53 | MCQ | 2 | A |
| 54 | MCQ | 2 | A |
| 55 | MSQ | 2 | A, C |
| 56 | NAT | 2 | 142 |
| 57 | MSQ | 2 | A, B, C |
| 58 | NAT | 2 | 24 |
| 59 | NAT | 2 | 1 |
| 60 | MSQ | 2 | A, C, D |
| 61 | NAT | 2 | 2 |
| 62 | NAT | 2 | 0.80 (two decimals) |
| 63 | MSQ | 2 | A, B |
| 64 | NAT | 2 | 102 |
| 65 | MCQ | 2 | B |
