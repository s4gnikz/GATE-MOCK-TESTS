# GATE CS 2027 — Full-Length Mock Test 063

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

A compiler produced correct output on every program in a finite test suite. No proof of correctness is available. Which inference is justified solely by this observation?

A. It is correct on every possible program.
B. No incorrect output was observed on the tested programs.
C. Every untested program must fail.
D. A larger test suite cannot reveal a fault.

### Q2. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A's and B's present ages are in ratio 4:3. After eight years their ages will be in ratio 6:5. What is their present age difference in years?

**Required precision:** Integer.

A. 4  
B. 8  
C. 2  
D. 5

### Q3. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A sequence satisfies a1=2 and a(n+1)=an+2n+1 for every n≥1. What is the smallest index n for which an exceeds100?

**Required precision:** Exact integer.

A. 20  
B. 5  
C. 10  
D. 11

### Q4. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

The diagonals of a trapezium intersect at O. The two triangles having the parallel sides as bases and O as their opposite vertex have areas9 and16. What is the area of the entire trapezium?

**Required precision:** Exact number.

A. 98  
B. 25  
C. 49  
D. 50

### Q5. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Choose the sentence that unambiguously states that the technician, rather than the instrument, was in a hurry.

A. Being in a hurry, the instrument was checked by the technician.  
B. The instrument was checked in a hurry that belonged to the technician.  
C. In a hurry, the technician checked the instrument.  
D. The technician checked the instrument that was in a hurry.

### Q6. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A fixed event budget initially allocates40% to food,35% to transport and25% to other costs. Food costs rise by25% of their originally allocated amount, and other costs stay fixed. To keep total spending unchanged, by what percentage must the original transport allocation be reduced?

**Required precision:** Percentage rounded to four decimal places, without the percent sign.

A. 57.1428  
B. 28.5714  
C. 14.2857  
D. 29.5714

### Q7. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Exactly one of propositions p,q,r is true. Additionally, p implies q. Which statements must hold?

A. p is false.  
B. Exactly one of q,r is true.  
C. q is necessarily true.  
D. q and r cannot both be false.

### Q8. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A rectangular tile measures 2 by 3 units. An unlimited number of these tiles may be rotated by 90 degrees. What is the smallest positive side length of a square that can be tiled completely without cutting or overlap, if the square's side length must be an integer?

**Required precision:** Integer units.

A. 12  
B. 3  
C. 6  
D. 7

### Q9. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A school introduces an optional tutoring programme. Students who chose it scored higher on average than those who did not. No information is available about their earlier scores or reasons for enrolling. Which statements follow from this description?

**Candidates**

**I.** Participation and the observed scores are associated in this sample.

**II.** The comparison alone does not isolate the causal effect of tutoring.

**III.** Tutoring necessarily caused every participant's score to increase.

**IV.** The participants and nonparticipants necessarily had identical prior achievement.

A. III and IV  
B. I and III  
C. I and II  
D. I and IV

### Q10. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A workshop must produce exactly 20 items using two methods. Method A takes two hours and costs 3 units per item; method B takes one hour and costs 5 units per item. The total processing-time budget is 28 hours, with no overlap of work. What is the minimum total cost?

**Required precision:** Integer cost units.

A. 168  
B. 84  
C. 42  
D. 85

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A file's inode initially has two hard links and one open file descriptor referring to it. Both hard links are removed. There are no other references, and reclamation occurs only when link count and open-reference count are both zero. How many further reference-removing operations are needed before the inode can be reclaimed?

**Required precision:** Integer.

A. 2  
B. 0  
C. 1  
D. 3

### Q12. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A cache has two sets, two lines per set, and uses least-recently-used replacement within each set. Memory block b maps to set b mod 2. The cache is initially empty. The processor reads blocks 0, 2, 0, 4, 2 in that order. Every miss loads the requested block. How many cache misses occur?

**Required precision:** Numeric value; integer.

A. 8  
B. 2  
C. 5  
D. 4

### Q13. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A syntax-directed translation uses E→E₁−T with E.val=E₁.val−T.val, E→T with E.val=T.val, and T→digit with its numeric value. What value is assigned to the expression 9−3−2 under this grammar?

**Required precision:** Integer.

A. 8  
B. 4  
C. 2  
D. 5

### Q14. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A process uses two distinct virtual pages v1 and v2 as aliases of the same physical frame. A simplified inverted page table stores exactly one pair(process ID, virtual page number) per physical frame. A lookup searches those stored pairs; no auxiliary alias information exists. Which statements are correct?

**Candidates**

**I.** The simplified table can simultaneously represent both aliases in its one entry for the frame.

**II.** The physical memory arrangement is possible even though the simplified representation cannot encode both aliases.

**III.** A mapping structure with a list of aliases per physical frame can address this representation problem.

**IV.** Aliasing requires the two virtual page numbers to be equal.

A. I and II  
B. I and III  
C. I and IV  
D. II and III

### Q15. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A hash function distributes each key independently and uniformly over five buckets. For three distinct keys, what is the probability that all occupy different buckets?

**Required precision:** Exact decimal.

A. 0.52  
B. 0.24  
C. 0.74  
D. 0.48

### Q16. [1 Mark] [NAT]

How many ordered triples of positive integers (x,y,z) satisfy x+y+z=8 with each entry at most 4?

**Answer format:** Integer.

### Q17. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Which of the following problems have an algorithm that always halts and answers correctly? Machines have finite descriptions; Turing machines are deterministic.

**Candidates**

**I.** Given a Turing machine and an input, determine whether it halts within 100 transitions.

**II.** Given a Turing machine and an input, determine whether it eventually halts.

**III.** Given a DFA over {0,1}, determine whether it accepts every binary string.

**IV.** Given a Turing machine, determine whether it halts on every input.

A. I and II  
B. I and IV  
C. I and III  
D. II and III

### Q18. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Over the alphabet {a,b}, let L contain exactly the strings that end in a and contain an even number of b symbols. The empty string is not in L. What is the number of states in a smallest complete DFA for L?

A. 6  
B. 3  
C. 2  
D. 4

### Q19. [1 Mark] [MCQ]

A language has lexically nested procedures. Procedure P contains Q and R; Q calls R. In a stack activation record for R, which relationship is correct under the usual static-link and dynamic-link model?

A. Both links point to Q's activation record.
B. The static link identifies P's activation; the dynamic link identifies Q's activation.
C. The static link identifies Q's activation; the dynamic link identifies P's activation.
D. Both links identify P's activation regardless of the caller.

### Q20. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A row-major array A[2..4][−1..2] stores four-byte elements with A[2][−1] at address 1000. What is the byte address of A[4][1]?

**Required precision:** Integer.

A. 2080  
B. 520  
C. 1040  
D. 1041

### Q21. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

How many proper vertex colorings of a labelled five-cycle exist using three available labelled colors? Adjacent vertices must differ; not every color need be used.

**Required precision:** Integer.

A. 60  
B. 15  
C. 31  
D. 30

### Q22. [1 Mark] [MCQ]

How many times is work() called asymptotically, for positive integer n?

```text
for i = 1 to n:
    j = i
    while j <= n:
        work()
        j = j + i
```

A. Θ(n)  
B. Θ(n²)  
C. Θ(log n)  
D. Θ(n log n)

### Q23. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A directed graph has edges s→a of weight 2, a→b of weight 3, c→d of weight −1, and d→c of weight 0, with no others. Which statements hold for shortest paths from s?

**Candidates**

**I.** The distance to b is 5.

**II.** The negative cycle makes the distance to b unbounded below.

**III.** Neither c nor d is reachable from s.

**IV.** No vertex reachable from s has a well-defined finite distance.

A. II and IV  
B. III and IV  
C. I and II  
D. I and III

### Q24. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

For three Boolean variables a,b,c, the on-set is {000,001} and the don't-care set is {010,011}; every other input is in the off-set. Among prime implicants that cover at least one on-set input, how many literals does the largest such cube contain?

**Required precision:** Integer.

A. 2  
B. 0  
C. 3  
D. 1

### Q25. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Evaluate the integral ∫₀¹ x/(1+x²) dx, rounded to four decimal places.

**Required precision:** Number to 4 decimal places.

A. 0.6534  
B. 0.1733  
C. 0.6733  
D. 0.3466

### Q26. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Two disjoint circular singly linked lists have nodes labelled 1,2 and 3,4 respectively, with links 1→2→1 and 3→4→3. Swap the next pointers stored in nodes 1 and 3, leaving all other pointers unchanged. Starting from node 1, which node label is reached after exactly two next-pointer traversals?

**Required precision:** Integer.

A. 3  
B. 6  
C. 2  
D. 4

### Q27. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A peripheral produces one byte every10 microseconds. The CPU polls every25 microseconds, reading and clearing all available bytes instantly. Initially the buffer is empty and a poll occurs at time0; arrivals start at time10. What minimum buffer capacity in bytes avoids overflow indefinitely? If an arrival and poll coincide, the arrival occurs first.

**Required precision:** Integer.

A. 3  
B. 6  
C. 2  
D. 4

### Q28. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

TCP has outstanding data segments covering byte ranges[1000,1500),[1500,2000),[2000,2500), and[2500,3000). A cumulative ACK with acknowledgment number2500 arrives. There is no selective acknowledgment information. How many bytes among these four segments remain unacknowledged by this ACK?

**Required precision:** Integer.

A. 500  
B. 1000  
C. 250  
D. 501

### Q29. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A connected TCP socket receives the peer's orderly write shutdown after all previously transmitted bytes have arrived. The local application has read all those bytes. No reset or error occurs. Which statements hold?

**Candidates**

**I.** A subsequent positive-length receive can return0 to indicate end of stream.

**II.** The local application must interpret that0 return as a received zero-valued data byte.

**III.** The local endpoint may still send data if its own write direction remains open and the peer continues receiving.

**IV.** TCP necessarily delivers a separate application record for the shutdown.

A. II and IV  
B. III and IV  
C. I and II  
D. I and III

### Q30. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A two-input XOR gate's inputs are tied to the same Boolean signal x. Its output feeds one input of a two-input OR gate whose other input is y. How many of the four assignments to(x,y) make the circuit output1?

**Required precision:** Integer.

A. 4  
B. 1  
C. 2  
D. 3

### Q31. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

The coefficient rows of a linear system in three unknowns are (1,1,1), (1,2,3), (2,3,4), and the corresponding right-hand sides are 1,t,3. For what value of t does the system have infinitely many solutions?

**Required precision:** Integer.

A. 4  
B. 1  
C. 3  
D. 2

### Q32. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Let f(x)=x² sin(1/x) for x≠0 and f(0)=0. What is f'(0)?

**Required precision:** Exact integer.

A. 1  
B. 2  
C. 0  
D. 3

### Q33. [1 Mark] [MCQ]

A direct-mapped cache has four lines. Block b maps to line b mod 4. Which pair of distinct blocks can coexist in this cache?

A. 1 and 5
B. 2 and 6
C. 3 and 7
D. 4 and 5

### Q34. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Initially, on-call flags A and B are both 1. Transaction T1 reads B and, if B=1, writes A=0. Transaction T2 reads A and, if A=1, writes B=0. Both read the same initial snapshot. A system rejects concurrent transactions only when they write a common item. Which statements hold?

A. Both transactions can commit under this rule.  
B. Every serial execution leaves A=B=0.  
C. The committed outcome can violate the invariant A+B≥1.  
D. Testing only for overlapping write sets fails to prevent this anomaly.

### Q35. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A client asks DNS for an AAAA record. Which result type is being requested?

A. An IPv6 address associated with the name.  
B. An Ethernet hardware address.  
C. A TCP acknowledgment number.  
D. The text of an HTTP response body.

### Q36. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A pipeline has four stages with delays2,5,3,4 ns and a1 ns register overhead per stage boundary included in its clock period. It processes ten independent operations with one operation entering per cycle after start. What is total time from the first entry until the tenth result, counting four cycles for the first result?

**Required precision:** Integer nanoseconds.

A. 156  
B. 39  
C. 78  
D. 79

### Q37. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A disk has cylinders0 through199, and the head starts at50 moving toward larger numbers. Pending requests are at60,70,20, with no future arrivals. LOOK reverses at the largest pending request; SCAN proceeds to199 before reversing. Both stop immediately after serving the last request. How much more total head movement does SCAN make than LOOK?

**Required precision:** Integer cylinders.

A. 258  
B. 516  
C. 129  
D. 259

### Q38. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A three-address code generator translates x=(a+b)*(a+b)+(a+b) and performs local common-subexpression elimination. All operands are unchanged mathematical integers. Each binary operation requires one assignment, and assigning the final expression to x needs no separate copy. What is the minimum number of binary-operation assignments in the resulting code?

**Required precision:** Integer.

A. 6  
B. 2  
C. 4  
D. 3

### Q39. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Weighted activities have half-open intervals and values: A=[0,2), value 4; B=[2,4), value 4; C=[0,4), value 8; D=[4,5), value 1. How many distinct compatible subsets achieve the maximum total value? The empty subset is permitted but need not be optimal.

**Required precision:** Integer.

A. 2  
B. 4  
C. 1  
D. 3

### Q40. [2 Marks] [MCQ]

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

### Q41. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A binary-input transducer outputs, after reading each input bit, that bit XOR the preceding input bit; before the first input the preceding bit is defined to be zero. Implement it as a deterministic Moore machine whose output after each input is determined by its reached state. The initial state's output before any input is ignored. What is the minimum number of states?

**Required precision:** Integer.

A. 8  
B. 2  
C. 4  
D. 5

### Q42. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A process successfully executes a new program image through an exec-like operation with the following specified semantics: its PID is retained, its old address space is replaced, and descriptors marked close-on-exec are closed while others remain open. Which observations are possible immediately afterwards?

**Candidates**

**I.** The PID is unchanged although the executed code is different.

**II.** An unmarked file descriptor remains usable by the new program.

**III.** Every pointer into the old heap is guaranteed to remain valid with its old object.

**IV.** Every inherited descriptor must have been closed.

A. I and III  
B. I and IV  
C. II and III  
D. I and II

### Q43. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A circular queue uses an array of length5 and reserves one slot to distinguish full from empty. Initially front=rear=0. Three enqueues, two dequeues, and then three enqueues all succeed. Indices advance modulo5. What is rear after the last enqueue?

**Required precision:** Integer index.

A. 2  
B. 0  
C. 1  
D. 3

### Q44. [2 Marks] [MSQ]

Assume ordinary TCP, UDP and IPv4 layering, without application-specific boundary reconstruction. Which statements are correct?

A. TCP does not preserve individual application write boundaries as receive-message boundaries.
B. A UDP datagram can never be fragmented at the IPv4 layer.
C. IPv4 fragmentation may be hidden from the receiving UDP application by IP reassembly.
D. A link-layer frame's header must remain unchanged across all routers on a path.

### Q45. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A recursive procedure on a list segment performs a postorder traversal: it first visits the left half, then the right half, then emits one marker. A segment of size 1 emits a marker and returns. For a segment of size n>1, the halves have sizes floor(n/2) and ceil(n/2). Starting with n=13, how many markers have been emitted immediately before the root invocation emits its marker?

**Required precision:** Integer.

A. 48  
B. 12  
C. 25  
D. 24

### Q46. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Two unsigned eight-bit fixed-point operands each have four fractional bits. Their encoded integers are 24 and 20. Their exact product is rescaled to the same format by dividing the integer product by 16 and rounding to nearest, with ties to even. What encoded integer is stored? No overflow occurs.

**Required precision:** Integer.

A. 60  
B. 15  
C. 30  
D. 31

### Q47. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Three independent draws select uniformly from three colours, with replacement. Let D be the number of distinct colours observed. What is Var(D)?

**Required precision:** Round to four decimal places; accepted tolerance ±0.00005 around the rounded answer.

A. 0.6790  
B. 0.3210  
C. 0.1605  
D. 0.6605

### Q48. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A tournament on four labelled vertices has exactly one directed edge between each pair. How many of the 2⁶ tournaments are strongly connected?

**Required precision:** Integer.

A. 24  
B. 48  
C. 12  
D. 25

### Q49. [2 Marks] [MSQ]

A is a real 3x3 matrix with distinct eigenvalues 1, 2 and 4. Let u be a nonzero column vector satisfying Au=2u, and let v be a real column vector satisfying v^T u=-2. Define B=A+u v^T. Which statements hold for every such A,u,v?

A. Zero is an eigenvalue of B.  
B. B is diagonalizable over the real numbers.  
C. A and B necessarily commute.  
D. rank(B)=2.

### Q50. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

For real x,y≥0 with x+y=6, maximize x²y. What is the maximum value?

**Required precision:** Integer.

A. 64  
B. 16  
C. 33  
D. 32

### Q51. [2 Marks] [MSQ]

For grammar S→SS | a | ε, which statements are true?

A. Its language is a*.
B. The word a has infinitely many distinct parse trees.
C. Every generated word has exactly one parse tree.
D. The grammar is LL(1) as written.

### Q52. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

An ER relationship assigns each of five distinct employees to exactly one of four distinct departments. Every department must have at least one employee. How many different relationship instances satisfy these participation and cardinality constraints?

**Required precision:** Integer.

A. 480  
B. 240  
C. 120  
D. 241

### Q53. [2 Marks] [MSQ]

Assume mathematical integer arithmetic and a Boolean flag whose value is not known at compile time. Compare these blocks:

```text
Original:
    x = 0
    if flag: x = 1
    y = x + 1

Proposed:
    x = 0
    y = 1
    if flag: x = 1
```

Both x and y are observable at exit. Which statements are correct?

A. The transformation preserves both outputs when flag is false.
B. The transformation preserves both outputs when flag is true.
C. Treating x=0 as an invariant across the conditional is unsound here.
D. Making y unobservable at exit would make these particular blocks equivalent on their remaining observable output x.

### Q54. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Relations R(A,B)={(1,x),(1,y),(2,x)} and S(A,B)={(1,x)} use set semantics. Compare E1=projection_A(R−S) and E2=projection_A(R)−projection_A(S). Which statements are correct?

A. E1={1,2}.  
B. E2={2}.  
C. Projection always distributes over set difference.  
D. The surviving tuple(1,y) explains why1 belongs to E1 but not E2.

### Q55. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A circuit-switched transfer has setup time1ms and then sends L payload bits at2 Mbit/s with no other overhead. A packet-switched alternative has no setup, sends at1 Mbit/s, and adds100 header bits per packet with at most900 payload bits per packet. Packets are filled except possibly the last; ignore all other delays. What is the smallest positive integer L for which the circuit-switched transfer finishes strictly earlier?

**Required precision:** Integer bits.

A. 3202  
B. 1601  
C. 801  
D. 1602

### Q56. [2 Marks] [MSQ]

A toy floating-point format has four significant binary bits and round-to-nearest, ties-to-even. It supports all exponents needed below. Which real values round to exactly1.5?

A. 1.4375
B. 1.49
C. 1.5625
D. 1.625

### Q57. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Over GF(2), a CRC generator is g(x)=x³+x+1. The transmitted codeword suffers error polynomial e(x)=x^k g(x), for some k≥0 that fits within the transmitted frame. Which statements are correct?

**Candidates**

**I.** The CRC remainder of the error polynomial is zero.

**II.** This nonzero error can escape detection.

**III.** Multiplication by x^k guarantees detection of every nonzero polynomial.

**IV.** The error polynomial must be a single-bit error.

A. I and II  
B. I and IV  
C. II and III  
D. II and IV

### Q58. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

In a BST subtree, root x has left subtree A and right child y. Node y has left subtree B and right subtree C. A contains 4 nodes, B 6 nodes and C 9 nodes. Perform a standard left rotation at x, making y the new subtree root. Every key is equally likely in a successful search, and a key at depth d from the full-tree root costs d+1 comparisons. What is the change (new minus old) in the sum of successful-search comparison counts over all keys in the full tree?

**Required precision:** Integer, possibly negative.

A. -10  
B. -3  
C. -4  
D. -5

### Q59. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A process has two threads sharing ordinary memory. Each executes the non-atomic operation `x = x+1` once, starting from x=0, with separate load/add/store steps and sequentially consistent interleaving. Which final values of x are possible?

**Candidates**

**I.** 0

**II.** 1

**III.** 2

**IV.** 3

A. I and IV  
B. II and IV  
C. III and IV  
D. II and III

### Q60. [2 Marks] [NAT]

A byte-addressed processor fetches instructions of lengths 2 or 4 bytes. Starting at address 100, it executes a 2-byte instruction, a 4-byte instruction, and then a 2-byte PC-relative branch. The branch target is computed from the next-instruction address plus a signed displacement measured in two-byte units. The branch displacement is −3. What is the target byte address?

**Answer format:** Integer.

### Q61. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

An8-bit two's-complement ALU computes the expression (x+y)−y, wrapping after each operation. For x=100 and y=60, count how many of the two operations signal signed overflow. The overflow flag is recomputed separately for each operation.

**Required precision:** Integer.

A. 4  
B. 2  
C. 1  
D. 3

### Q62. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A PDA starts with one bottom-of-stack marker. On each input a it pushes two ordinary symbols; on each b it pops one ordinary symbol and rejects if only the bottom marker remains. Acceptance requires input exhaustion with only the marker left. For input aabbbb, what is the maximum stack height, counting the marker, reached during the computation?

**Required precision:** Integer.

A. 10  
B. 3  
C. 6  
D. 5

### Q63. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Let L1={a^n b^n c^m:n,m≥0} and L2={a^m b^n c^n:n,m≥0}. Which statements hold?

**Candidates**

**I.** L1 union L2 is context-free.

**II.** L1 intersect L2 is regular.

**III.** L1 intersect L2 equals {a^n b^n c^n:n≥0}.

**IV.** L1 union L2 is regular.

A. I and III  
B. II and III  
C. II and IV  
D. III and IV

### Q64. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An algorithm runs the following loops, with work() constant time:

```text
for i = 1 to n:
    for j = 1 to floor(n/i):
        for k = 1 to i:
            work()
```

What is its tight asymptotic running time?

A. Θ(n log n)  
B. Θ(n²)  
C. Θ(n³)  
D. Θ(log n)

### Q65. [2 Marks] [MSQ]

Consider exact integers, pure arithmetic, and an arbitrary input n. A compiler proposes moving the division in this loop to just before the loop:

```text
i = 0
while i < n:
    t = 100 / n
    use(t)
    i = i + 1
```

Integer division truncates toward zero; division by zero traps. `use` does not modify n. Which statements are correct?

A. The expression 100/n is loop invariant.
B. Unconditionally hoisting it is semantics-preserving for every integer n.
C. Hoisting it inside a preceding `if n > 0` guard preserves division behaviour and use results.
D. Invariance alone is insufficient to justify evaluating the expression on a path where the original did not evaluate it.

---

## ANSWER KEY — MOCK TEST 063

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | B |
| 2 | MSQ | 1 | B, C, D |
| 3 | MCQ | 1 | C |
| 4 | MCQ | 1 | C |
| 5 | MSQ | 1 | A, B, D |
| 6 | MSQ | 2 | A, C, D |
| 7 | MCQ | 2 | C |
| 8 | MCQ | 2 | C |
| 9 | MCQ | 2 | C |
| 10 | MCQ | 2 | B |
| 11 | MSQ | 1 | A, B, D |
| 12 | MCQ | 1 | D |
| 13 | MCQ | 1 | B |
| 14 | MCQ | 1 | D |
| 15 | MCQ | 1 | D |
| 16 | NAT | 1 | 12 |
| 17 | MCQ | 1 | C |
| 18 | MCQ | 1 | B |
| 19 | MCQ | 1 | B |
| 20 | MCQ | 1 | C |
| 21 | MCQ | 1 | D |
| 22 | MCQ | 1 | D |
| 23 | MCQ | 1 | D |
| 24 | MSQ | 1 | A, B, C |
| 25 | MSQ | 1 | A, B, C |
| 26 | MCQ | 1 | A |
| 27 | MCQ | 1 | A |
| 28 | MSQ | 1 | B, C, D |
| 29 | MCQ | 1 | D |
| 30 | MSQ | 1 | A, B, D |
| 31 | MCQ | 1 | D |
| 32 | MCQ | 1 | C |
| 33 | MCQ | 1 | D |
| 34 | MCQ | 1 | B |
| 35 | MSQ | 1 | B, C, D |
| 36 | MSQ | 2 | A, B, D |
| 37 | MSQ | 2 | B, C, D |
| 38 | MCQ | 2 | D |
| 39 | MSQ | 2 | B, C, D |
| 40 | MCQ | 2 | C |
| 41 | MSQ | 2 | A, B, D |
| 42 | MCQ | 2 | D |
| 43 | MSQ | 2 | A, B, D |
| 44 | MSQ | 2 | A, C |
| 45 | MSQ | 2 | A, B, C |
| 46 | MSQ | 2 | A, B, D |
| 47 | MSQ | 2 | A, C, D |
| 48 | MSQ | 2 | B, C, D |
| 49 | MSQ | 2 | A, B, D |
| 50 | MSQ | 2 | A, B, C |
| 51 | MSQ | 2 | A, B |
| 52 | MSQ | 2 | A, C, D |
| 53 | MSQ | 2 | A, C, D |
| 54 | MCQ | 2 | C |
| 55 | MSQ | 2 | A, C, D |
| 56 | MSQ | 2 | A, B, C |
| 57 | MCQ | 2 | A |
| 58 | MCQ | 2 | D |
| 59 | MCQ | 2 | D |
| 60 | NAT | 2 | 102 |
| 61 | MSQ | 2 | A, C, D |
| 62 | MSQ | 2 | A, B, C |
| 63 | MCQ | 2 | A |
| 64 | MSQ | 2 | A, C, D |
| 65 | MSQ | 2 | A, C, D |
