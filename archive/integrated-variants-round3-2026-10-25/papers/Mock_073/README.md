# GATE CS 2027 — Full-Length Mock Test 073

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

### Q1. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A writer intends to compare the cost of repairing a machine with the cost of replacing that machine, not with the machine itself. Which sentence makes the comparison explicit and parallel?

A. Repairing the machine costs less than the replacement machine.  
B. The cost of repairing the machine is lower than that of replacing it.  
C. Repairing costs less than the machine is replaced.  
D. The machine is cheaper than repairing it costs less.

### Q2. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Six equally efficient workers can complete a job in eight days. They work for two days, after which two workers leave. How many additional days do the remaining workers need? Work is divisible and each worker's daily rate is constant.

**Required precision:** Integer.

A. 18  
B. 5  
C. 10  
D. 9

### Q3. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A positive real number x satisfies log₂x + log₄x = 9. Find x.

**Required precision:** Integer.

A. 128  
B. 64  
C. 32  
D. 65

### Q4. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A machine maps every integer n to an integer f(n). Tests establish f(1)=2, f(2)=4 and f(3)=6; no other restriction on f is given. Which claim is justified?

A. f(4) must equal8.  
B. f is necessarily linear.  
C. The observations are consistent with f(n)=2n but do not uniquely establish it.  
D. No function can satisfy all three observations.

### Q5. [1 Mark] [NAT]

How many distinct arrangements of the letters of BALLOON have all three vowels together? Repeated copies of the same letter are indistinguishable.

**Answer format:** Integer.

### Q6. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

The distinct letters A,B,C,D,E are arranged in a row, each exactly once. Let X be the set of arrangements where A and B are adjacent in either order, and Y the set where B and C are adjacent in either order. Which statements are correct?

**Candidates**

**I.** X contains48 arrangements.

**II.** The intersection of X and Y contains24 arrangements.

**III.** Exactly72 arrangements belong to at least one of X and Y.

**IV.** Exactly36 arrangements belong to neither X nor Y.

A. I and II  
B. I and IV  
C. I and III  
D. II and III

### Q7. [2 Marks] [NAT]

Two branches report successful deliveries as follows. Each delivery belongs to exactly one branch and one period.

| Branch | Period 1: successes/attempts | Period 2: successes/attempts |
|---|---:|---:|
| East | 81/90 | 19/20 |
| West | 2/10 | 24/80 |

Both branches improved their success rates. By how many percentage points did the overall success rate decrease from Period 1 to Period 2?

**Answer format:** Exact integer.

### Q8. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A rectangular sheet occupies 0≤x≤8 and 0≤y≤6. Fold its right half onto the left along x=4, then fold its top half onto the bottom along y=3. In the folded rectangle, cut out the entire small rectangle 3<x≤4, 1<y<2 through all layers. What is the total perimeter of all resulting internal holes after the sheet is unfolded? The cut reaches the folded edge x=4, but does not touch y=3 or the original sheet's outer boundary.

**Required precision:** Exact integer, in the same length units.

A. 24  
B. 12  
C. 6  
D. 13

### Q9. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

An alloy containing 40% copper is mixed with one containing 70% copper to produce 20 kg containing 52% copper. How many kilograms of the 70% alloy are required?

**Required precision:** Integer kilograms.

A. 16  
B. 8  
C. 4  
D. 9

### Q10. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Three counters are drawn independently with replacement from a box containing one counter of each of four colours. What is the expected number of distinct colours observed?

**Required precision:** Exact decimal.

A. 4.6250  
B. 2.3125  
C. 1.1563  
D. 3.3125

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MSQ]

Order the set {1,2,3,6} by divisibility. Which statements hold?

A. Every pair has a greatest lower bound and a least upper bound in this set.
B. 2 and 3 have neither a common upper bound nor a common lower bound.
C. Every element has a complement with respect to bottom 1 and top 6.
D. The order is a total order.

### Q12. [1 Mark] [MCQ]

A bottom-up parser for E→E+T | T and T→id has already reduced the first id in `id+id` to E and shifted `+ id`. Its stack, ignoring states and the bottom marker, is `E + id`; the lookahead is end-of-input. What is the next reduction in the successful reverse-rightmost derivation?

A. E→E+T, reducing the entire stack immediately.
B. T→id, reducing only the final id.
C. E→T, reducing the initial E.
D. No reduction is possible because the input is exhausted.

### Q13. [1 Mark] [MCQ]

A lexer has tokens IF='if', ID=[a-z][a-z0-9]*, and INT=[0-9]+. It applies maximal munch, with IF winning a tie against ID. Which tokenization is produced for the input if2if?

A. IF, INT, IF
B. ID
C. IF, ID
D. Lexical error because digits cannot occur in an identifier.

### Q14. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Two processes use the same virtual page number but map it to different physical frames. A processor's TLB has no address-space tags. Which action can prevent stale translations from the first process being used by the second on a context switch?

A. Retain all translations merely because the virtual page numbers match.  
B. Flush the relevant TLB translations when changing address spaces.  
C. Change every physical memory byte to zero.  
D. Assume every TLB hit automatically consults the new page table again.

### Q15. [1 Mark] [NAT]

A byte-addressed machine fetches a four-byte instruction beginning at address100. Its PC-relative branch displacement is a signed count of four-byte words measured from the address immediately following the instruction. If the displacement is−3, what is the branch target byte address?

**Answer format:** Integer.

### Q16. [1 Mark] [NAT]

A synchronous two-bit state machine has next-state equations Q1'=Q0 and Q0'=NOT Q1. Starting at00, how many clock edges occur before the state first returns to00?

**Answer format:** Integer.

### Q17. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A 4-bit adder-subtractor computes A+(B XOR ssss)+s and keeps the low four result bits. Its carry-out is C and its two's-complement signed overflow flag is V. For A=0111, B=1010 and s=1, which triple (result,C,V) is correct?

A. (1101,1,0)  
B. (1101,0,0)  
C. (0011,1,1)  
D. (1101,0,1)

### Q18. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A directory contains three hard links to the same ordinary file. One link is removed. How many directory hard links to that file remain, assuming no other changes?

**Required precision:** Integer.

A. 2  
B. 4  
C. 1  
D. 3

### Q19. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Eight-bit two's-complement fixed-point words have four fractional bits. Add raw words 0xC8 and 0x34 using eight-bit addition. What real value does the resulting word represent?

**Required precision:** Exact finite decimal, possibly negative.

A. -0.25  
B. -0.50  
C. -0.13  
D. 0.75

### Q20. [1 Mark] [MSQ]

For real t let

```text
A(t) = [1  2  1]
       [2  t  3]
       [1  3  1].
```

Use Doolittle elimination, with unit diagonal in L and no row exchanges unless an option explicitly permits one. Which statements are correct?

A. det(A(t))=-1 for every real t.  
B. An unpivoted factorization A=LU with unit lower-triangular L exists for every real t.  
C. At t=4, exchanging rows 2 and 3 after eliminating column 1 allows elimination to finish without a zero pivot.  
D. At t=5, the final diagonal entry U33 is 1.

### Q21. [1 Mark] [NAT]

A normalized binary floating-point format has a fixed number of significant bits, enough exponent range, and spacing0.25 between successive values in[8,16). It rounds to nearest with ties to an even least significant significand bit. What is the rounded value of9.125?

**Answer format:** Exact decimal.

### Q22. [1 Mark] [NAT]

Evaluate ∫ from −1 to 1 of (x cos x + x²) dx. Angles are in radians. Round to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q23. [1 Mark] [NAT]

An IPv4 receiver has received two fragments of one datagram. The first has offset 0, payload length 80 bytes and MF=1. The other has offset 12 (in the standard eight-byte units), payload length 24 bytes and MF=0. No other fragments have arrived. How many payload bytes are missing between the received regions?

**Answer format:** Integer.

### Q24. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For a directed simple graph on n labelled vertices, an adjacency matrix M stores M[u,v]=1 exactly when u→v exists. There are no self-loops. Which statements are correct?

**Candidates**

**I.** A diagonal entry of M² counts directed walks of length two returning to that vertex.

**II.** The sum of all entries of M always equals twice the number of directed edges.

**III.** Transposing M reverses every edge.

**IV.** A zero diagonal of M implies a zero diagonal of M².

A. I and III  
B. III and IV  
C. I and II  
D. I and IV

### Q25. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For a PDA accepting by empty stack with all input consumed, why must the input-consumption condition be checked explicitly?

A. Emptying the stack while unread input remains is not by itself acceptance under this convention.  
B. A stack can never be empty.  
C. Input is always consumed in one transition.  
D. Empty-stack acceptance requires a finite input alphabet of exactly one symbol.

### Q26. [1 Mark] [MCQ]

What is the smallest single CIDR block containing both 10.0.4.0/24 and 10.0.5.0/24, without covering any additional /24 block? Use canonical network-address notation with all host bits zero.

A. 10.0.4.0/23
B. 10.0.4.0/22
C. 10.0.5.0/23
D. 10.0.0.0/21

### Q27. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A database permits uncommitted updates to reach disk and uses an undo log. Before overwriting an on-disk data item, its old value is forced into the log. Which statements are correct?

**Candidates**

**I.** The log-before-data rule supplies information needed to undo an uncommitted on-disk update.

**II.** Writing the old value to the log only after overwriting the disk item is equally safe against a crash between those writes.

**III.** A transaction's abort may require restoring disk data, not merely clearing a memory buffer.

**IV.** The stated rule by itself proves that every committed update is already on disk.

A. II and III  
B. II and IV  
C. III and IV  
D. I and III

### Q28. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A directed graph has a negative-weight cycle that is unreachable from source s. Which statement about source-reachable shortest paths follows?

A. Every source-reachable distance is necessarily undefined.  
B. The unreachable cycle alone does not destroy shortest-path distances from s.  
C. The cycle must be removed before even identifying vertices reachable from s.  
D. All edge weights reachable from s must therefore be nonnegative.

### Q29. [1 Mark] [NAT]

Let h be a homomorphism from binary words to words over {a,b}, defined by h(0)=ab and h(1)=aabb. How many binary words w satisfy h(w)∈a*b*? Include the empty word when applicable.

**Answer format:** Integer.

### Q30. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Two transactions execute r1(X),w1(X),r2(X),w2(Y),r1(Y), then both commit, with operations listed in execution order. Which statement about conflict serializability is correct?

A. Equivalent to T1 followed by T2 because T1 first accesses X.  
B. Equivalent to T2 followed by T1 because T2 writes Y.  
C. Serializable because reads never participate in conflicts.  
D. Not conflict-serializable because the precedence graph contains both T1→T2 and T2→T1.

### Q31. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Five real observations all lie in [−1,1], have mean0, and have median0. What is the largest possible population variance?

**Required precision:** Exact decimal.

A. 0.2  
B. 0.4  
C. 0.8  
D. 0.9

### Q32. [1 Mark] [MCQ]

The grammar S→aSb | ε is used by a predictive parser. On valid input aabb, what is the maximum number of unconsumed b terminals simultaneously present on its stack, excluding input and the end marker?

A. 1
B. 2
C. 3
D. 4

### Q33. [1 Mark] [NAT]

A nondecreasing array is[1,2,2,2,4,7], with indices0–5. A binary search for the first index with value at least2 uses a half-open search interval[l,r), initially[0,6), and updates r=mid when A[mid]≥2, otherwise l=mid+1, where mid=floor((l+r)/2). How many array-element comparisons occur before l=r?

**Answer format:** Integer.

### Q34. [1 Mark] [MCQ]

To use the pumping lemma for context-free languages to prove non-context-freeness, a proof must handle which choice of decomposition w=uvxyz?

A. Only the lexicographically first decomposition.
B. Every decomposition satisfying |vxy|≤p and |vy|>0, after choosing a suitable w with |w|≥p.
C. Only decompositions with v=y=ε.
D. No decomposition, because choosing a long word is sufficient.

### Q35. [1 Mark] [MCQ]

In the additive group Z12, let H be the subgroup generated by 8. What is the order of the coset 5+H in the quotient group Z12/H?

A. 3  
B. 4  
C. 6  
D. 12

### Q36. [2 Marks] [NAT]

How many labelled trees on vertices 1,…,6 have degrees d1=3,d2=2,d3=2,d4=d5=d6=1?

**Answer format:** Integer.

### Q37. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A linear-probing table has occupied slots 2,3,4 holding keys whose home slots are respectively 2,2,4. Slot 5 has never been occupied. The key in slot 2 is deleted. Which repair preserves searches for the two remaining keys if no tombstones are allowed?

A. Leave slot 2 empty and do nothing else.  
B. Move the key from slot 3 to slot 2 and leave slot 3 empty; keep the key whose home is 4 in slot 4.  
C. Move the key from slot 4 to slot 2 and leave slot 3 unchanged.  
D. Clear all three slots without reinserting either remaining key.

### Q38. [2 Marks] [MCQ]

R(A,B,C,D) has FDs A→B, B→C, C→D. Which decomposition is both lossless and dependency preserving?

A. AB, BC, CD
B. AB, CD
C. AC, BD
D. AD, BC

### Q39. [2 Marks] [MSQ]

Real 4×4 matrices E,F satisfy E²=E, F²=F, EF=FE, rank(E)=3, and rank(F)=2. Which statements must hold?

A. rank(E−F) is either 1 or 3.
B. trace(E+F)=5.
C. rank(EF)=2 in every case.
D. det(E+F) is either 0 or 2.

### Q40. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Functions on nonnegative integers satisfy f(0)=1, g(0)=0 and, for n≥1, f(n)=f(n−1)+g(n−1), g(n)=f(n−1)−g(n−1). What is f(10)?

**Required precision:** Integer.

A. 64  
B. 16  
C. 33  
D. 32

### Q41. [2 Marks] [MCQ]

For grammar S→L=R | R, L→*R | id, R→L, consider an LR(0) item set containing S→L·=R and R→L·. In SLR parsing, FOLLOW(R) contains '='. What conflict occurs in the SLR table for lookahead '='?

A. No conflict, because completed items are ignored on '='.
B. Shift–reduce conflict between shifting '=' and reducing R→L.
C. Reduce–reduce conflict between two completed productions shown here.
D. Accept–reduce conflict because every completed item accepts the input.

### Q42. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A Boolean function f of three variables is monotone if changing any input from 0 to 1 without changing the others cannot change its output from 1 to 0. It is self-dual if f(NOT x,NOT y,NOT z)=NOT f(x,y,z). How many Boolean functions satisfy both properties? Variables are labelled; permuting them can produce a different function.

**Required precision:** Integer.

A. 8  
B. 4  
C. 2  
D. 5

### Q43. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A microprogrammed control unit uses a fixed-width microinstruction. One field jointly encodes the following bus-transfer commands:

- An idle command, in which no source drives the bus and no destination is loaded.
- A non-idle command chooses exactly one of eight sources and a nonempty subset of five destination registers. Every such source/subset pair is allowed.

There are no other bus-transfer commands. Each allowed command needs a distinct binary code, and unused codes are permitted. The other independently encoded fields select one of six ALU operations (including no-operation), one of 128 next addresses, and one of four sequencing conditions (including unconditional sequencing). Codes cannot be shared across these four fields. What is the minimum microinstruction width?

A. 19 bits  
B. 20 bits  
C. 21 bits  
D. 25 bits

### Q44. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A file contains 100 fixed-size records in ten disk blocks, ten records per block. An in-memory index gives the exact block containing any requested record. Ten requested record numbers are independently and uniformly selected with replacement from the 100 records. A data block is read from disk only on its first request and then remains cached. Which expression is the expected number of disk reads?

A. 10  
B. 10(1−(9/10)¹⁰)  
C. 100(1−(99/100)¹⁰)  
D. (9/10)¹⁰

### Q45. [2 Marks] [MSQ]

A multithreaded process has threads T1,T2. T2 holds a user-space mutex when T1 duplicates the process using a model in which the child contains only the calling thread but inherits a copy of the mutex's locked state. In the child, no automatic repair occurs and no surviving thread can release T2's lock. Which statements are correct?

A. The child's copied mutex may remain permanently locked.
B. The child's copy of T2 necessarily continues and releases it.
C. Waiting on that mutex in the child can block indefinitely under this model.
D. The parent's later unlock necessarily changes the child's private copied mutex state.

### Q46. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A16-bit memory interface consists of two independently enabled eight-bit banks. The low bank holds even byte addresses; the high bank holds odd byte addresses. One bus transaction accesses both bytes of one aligned two-byte word, and can enable either bank or both. Which statements are correct?

**Candidates**

**I.** An aligned two-byte load can be serviced in one transaction.

**II.** A two-byte load starting at an odd address always fits in one aligned-word transaction.

**III.** A byte store can preserve the other byte by enabling only its target bank.

**IV.** Changing endianness changes which numerical byte address is even.

A. I and III  
B. II and IV  
C. III and IV  
D. I and II

### Q47. [2 Marks] [MCQ]

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

### Q48. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

An array of eight distinct values is reordered in place by exchanging entries whose indices are reversals of each other's three-bit binary representation. Indices range0–7. Each unequal pair is exchanged once, and equal-index pairs are untouched. How many swaps occur?

**Required precision:** Integer.

A. 4  
B. 1  
C. 2  
D. 3

### Q49. [2 Marks] [MCQ]

Two finite, acyclic, singly linked lists may share a suffix by node identity. Their heads are h1 and h2. Which algorithm finds the first shared node, or reports none, in O(m+n) time and O(1) extra space?

A. Compare only the values stored in corresponding nodes.
B. Measure both lengths, advance the longer list by their difference, then advance both pointers together until they are identical or both null.
C. Return the first pair of nodes having equal stored values, regardless of identity.
D. Reverse one list and return its new head without examining the other list.

### Q50. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An inclusive two-level cache requires every block in L1 also to be present in L2. An exclusive design instead requires blocks resident in L1 to be absent from L2. Ignore other cache levels. Which statements are correct?

**Candidates**

**I.** Evicting an L2 block in the inclusive design may require invalidating its L1 copy.

**II.** An inclusive L1 miss can never be an L2 hit.

**III.** The exclusive design permits the same block to remain simultaneously in both levels by definition.

**IV.** Replication in the inclusive design can reduce the number of distinct resident blocks compared with equal-capacity exclusive levels.

A. III and IV  
B. I and II  
C. I and III  
D. I and IV

### Q51. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A syntax-directed definition for binary strings uses S→S1 b and S→b, where b is0 or1. For S→b, set S.val=b and S.len=1. For S→S1 b, set S.val=S1.val+2^(S1.len)·b and S.len=S1.len+1. What is S.val for the string10110?

**Required precision:** Integer.

A. 13  
B. 26  
C. 7  
D. 14

### Q52. [2 Marks] [MCQ]

A NAT maps internal TCP endpoint 192.168.1.8:5000 to public endpoint 203.0.113.2:42000 for a connection to 198.51.100.9:443. It translates an outgoing IPv4 packet with no options and no fragmentation. Which checksum fields must be updated because of these substitutions?

A. Only the IPv4 header checksum.
B. Only the TCP checksum.
C. Neither checksum, because payload bytes are unchanged.
D. Both the IPv4 header checksum and the TCP checksum.

### Q53. [2 Marks] [MCQ]

A TCP receiver initially expects byte 1000. Four 100-byte segments cover byte ranges 1000–1099,1100–1199,1200–1299,1300–1399. They arrive in the order third,first,fourth,second. The receiver buffers out-of-order data and sends a cumulative ACK after each arrival, stating the next missing byte. Which ACK sequence is correct?

A. 1300,1100,1400,1200
B. 1000,1100,1100,1400
C. 1000,1200,1300,1400
D. 1100,1200,1300,1400

### Q54. [2 Marks] [NAT]

Under set semantics, R(A,B)={(1,x),(1,y),(2,x),(3,x),(3,y)} and S(B)={x,y}. How many tuples are in relational division R÷S?

**Answer format:** Integer.

### Q55. [2 Marks] [MSQ]

The Boolean function F=AB+(NOT A)C is implemented directly as a two-level AND-OR circuit, with a separate inverter generating NOT A. Gate delays are positive and may differ. Only one primary input changes at a time, after the circuit has settled. Which statements are correct?

A. Adding the product term BC does not change the Boolean function.  
B. With B=C=1, a change of A can produce a temporary 0 at the output for some gate delays.  
C. Adding the product term ABC guarantees removal of this possible temporary 0 for every choice of positive gate delays.  
D. Adding the product term BC guarantees removal of this possible temporary 0 during changes of A with B=C=1.

### Q56. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let e_n be the number of binary strings of length n that have no consecutive 1s and contain an even number of 1s. The empty string is counted, so e_0=1. Which formal ordinary generating function E(x)=sum over n>=0 of e_n*x^n is correct?

A. (1+x)/(1-x-x^2)  
B. (1-x+x^3)/(1-2x+x^2-x^4)  
C. 1/(1-x-x^2)  
D. (1-x)/(1-2x+x^2-x^4)

### Q57. [2 Marks] [MSQ]

A fractional knapsack permits dividing items; all weights and values are positive. Which statements are correct?

A. Sorting by decreasing value/weight yields an optimal packing.
B. Sorting by decreasing absolute value always yields an optimal packing.
C. With distinct ratios, an optimum produced by the ratio rule has at most one partially selected item.
D. The same ratio rule is guaranteed optimal when items become indivisible.

### Q58. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Procedure P is lexically nested inside Main. Procedures Q and R are both lexically nested inside P. During execution, Main calls P, P calls Q, and Q calls R. Each activation has a static link to its immediate lexical parent's activation and a dynamic link to its caller. From R's activation, how many static links must be followed to access a local variable of Main?

**Required precision:** Integer.

A. 4  
B. 1  
C. 3  
D. 2

### Q59. [2 Marks] [NAT]

The domain is the labeled set {a,b}. How many binary relations R on this domain satisfy both FOR ALL x EXISTS y R(x,y) and EXISTS x FOR ALL y R(x,y)?

**Answer format:** Exact integer.

### Q60. [2 Marks] [MSQ]

A recognizer for L1 and a recognizer for L2 may loop on nonmembers. Which proposed procedures recognize the stated languages for every such pair of recognizers?

A. For L1∪L2, interleave one step of each recognizer and accept when either accepts.
B. For L1∪L2, run the first recognizer to completion before starting the second, accepting if either accepts.
C. For L1∩L2, run the first until it accepts, then the second until it accepts, and then accept.
D. For the complement of L1, accept if its recognizer has not accepted after one million steps.

### Q61. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Two processes communicate using two separate FIFO channels, one in each direction. Each channel has a positive integer capacity measured in messages. Each process sends two messages to the other, then receives two. A send blocks only while its channel is full; a receive blocks only while its channel is empty. Under fair execution, what is the minimum sum of the two channel capacities that guarantees completion?

**Required precision:** Integer.

A. 6  
B. 2  
C. 3  
D. 4

### Q62. [2 Marks] [MSQ]

A prime-implicant chart has required columns u,v,w and rows P={u,v}, Q={v,w}, R={u,w}. Every row has equal cost. Which statements are correct?

A. Every row is essential because it covers two columns.
B. No single row covers all required columns.
C. There are exactly three distinct minimum-cardinality covers.
D. Deleting any one row leaves at least one valid cover.

### Q63. [2 Marks] [MCQ]

Student(S)={(1),(2)}, Enrollment(S,C)={(1,X)}, and Required(C) is empty. No constraint requires an enrolled course to be in Required. Compare:

- QI: all Student identifiers s such that for every c in Required, (s,c) is in Enrollment.
- QII: relational division Enrollment ÷ Required, with candidate S values taken from the projection of Enrollment on S.

Using set semantics, what are the results (QI,QII)?

A. (empty,empty)  
B. ({1},{1})  
C. ({1,2},{1,2})  
D. ({1,2},{1})

### Q64. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Over alphabet {0,1}, a DFA must accept exactly strings whose length is divisible by3 and whose number of1s is even. What is the minimum number of states in a complete DFA?

**Required precision:** Exact integer.

A. 12  
B. 6  
C. 3  
D. 7

### Q65. [2 Marks] [MCQ]

Let L={aⁱbʲcᵏ : i,j,k≥0 and i=j or j=k}. Which statement is correct?

A. L is not context-free because it contains aⁿbⁿcⁿ.
B. L is regular because the condition uses “or.”
C. L is context-free, but its intersection with {aⁿbⁿcⁿ:n≥0} is not context-free.
D. L is finite.

---

## ANSWER KEY — MOCK TEST 073

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MSQ | 1 | A, C, D |
| 2 | MCQ | 1 | D |
| 3 | MCQ | 1 | B |
| 4 | MSQ | 1 | A, B, D |
| 5 | NAT | 1 | 180 |
| 6 | MCQ | 2 | B |
| 7 | NAT | 2 | 40 |
| 8 | MCQ | 2 | B |
| 9 | MCQ | 2 | B |
| 10 | MCQ | 2 | B |
| 11 | MSQ | 1 | A, C |
| 12 | MCQ | 1 | B |
| 13 | MCQ | 1 | B |
| 14 | MSQ | 1 | A, C, D |
| 15 | NAT | 1 | 92 |
| 16 | NAT | 1 | 4 |
| 17 | MSQ | 1 | A, B, C |
| 18 | MCQ | 1 | A |
| 19 | MCQ | 1 | A |
| 20 | MSQ | 1 | A, C |
| 21 | NAT | 1 | 9 |
| 22 | NAT | 1 | 0.6667 (range 0.66665–0.66675) |
| 23 | NAT | 1 | 16 |
| 24 | MCQ | 1 | A |
| 25 | MSQ | 1 | B, C, D |
| 26 | MCQ | 1 | A |
| 27 | MCQ | 1 | D |
| 28 | MSQ | 1 | A, C, D |
| 29 | NAT | 1 | 3 |
| 30 | MSQ | 1 | A, B, C |
| 31 | MCQ | 1 | C |
| 32 | MCQ | 1 | B |
| 33 | NAT | 1 | 3 |
| 34 | MCQ | 1 | B |
| 35 | MCQ | 1 | B |
| 36 | NAT | 2 | 12 |
| 37 | MSQ | 2 | A, C, D |
| 38 | MCQ | 2 | A |
| 39 | MSQ | 2 | A, B, D |
| 40 | MCQ | 2 | D |
| 41 | MCQ | 2 | B |
| 42 | MCQ | 2 | B |
| 43 | MSQ | 2 | A, C, D |
| 44 | MSQ | 2 | A, C, D |
| 45 | MSQ | 2 | A, C |
| 46 | MCQ | 2 | A |
| 47 | MCQ | 2 | B |
| 48 | MCQ | 2 | C |
| 49 | MCQ | 2 | B |
| 50 | MCQ | 2 | D |
| 51 | MCQ | 2 | A |
| 52 | MCQ | 2 | D |
| 53 | MCQ | 2 | B |
| 54 | NAT | 2 | 2 |
| 55 | MSQ | 2 | A, B, D |
| 56 | MSQ | 2 | A, C, D |
| 57 | MSQ | 2 | A, C |
| 58 | MCQ | 2 | D |
| 59 | NAT | 2 | 5 |
| 60 | MSQ | 2 | A, C |
| 61 | MCQ | 2 | C |
| 62 | MSQ | 2 | B, C, D |
| 63 | MCQ | 2 | D |
| 64 | MCQ | 2 | B |
| 65 | MCQ | 2 | C |
