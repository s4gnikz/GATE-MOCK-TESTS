# GATE CS 2027 — Full-Length Mock Test 078

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

Among employees, every auditor is a reviewer, and no reviewer is an intern. At least one auditor exists. Which statements must follow?

A. At least one reviewer is not an intern.
B. Every non-intern is an auditor.
C. No auditor is an intern.
D. At least one intern exists.

### Q2. [1 Mark] [MCQ]

A point is first reflected across y=x, then translated by (2,−1). Which point maps to (5,3)?

A. (3,4)
B. (4,3)
C. (6,1)
D. (1,6)

### Q3. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Four runners finish without ties. A finishes before B; C finishes after B; D finishes before C. Which runner can finish neither first nor last?

A. A  
B. B  
C. C  
D. D

### Q4. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Four distinct people sit around a circular table. Rotations are considered identical, but reflections are different. Two specified people must sit opposite each other. How many seating arrangements are possible?

**Required precision:** Integer.

A. 4  
B. 2  
C. 1  
D. 3

### Q5. [1 Mark] [MSQ]

The table gives successful applications divided by total applications for two programmes. Every application belongs to exactly one programme.

| Programme | Year 1 | Year 2 |
|---|---:|---:|
| P | 80/100 | 9/10 |
| Q | 20/100 | 27/90 |

Which statements follow from the table?

A. Each programme's success percentage increased.  
B. The combined success percentage increased.  
C. Programme Q's share of all applications increased.  
D. The table proves that an individual applicant's chance of success increased because of a policy change.

### Q6. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A square sheet is folded along both its horizontal and vertical midlines into four layers. A single triangular notch is cut at the folded corner that corresponds to the centre of the original sheet, with equal cuts along the two fold edges. After complete unfolding, how many sides does the resulting central hole have? The cuts are straight and do not reach any outer boundary.

**Required precision:** Integer.

A. 8  
B. 2  
C. 4  
D. 5

### Q7. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Four events Q,R,S,P occurred at distinct times. Four log entries assert Q before R, R before S, S before P, and P before Q, respectively. Exactly one of these four entries is wrong. An independent reliable record establishes R before P. Which ordering must be true?

A. Q before R.  
B. Q before P.  
C. S before P.  
D. P before R.

### Q8. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Three independent fair six-sided dice are rolled. It is known that exactly two dice have the same value and that the largest of the three values is 5. What is the conditional probability that the sum of the three values is odd?

**Required precision:** Exact decimal.

A. 0.75  
B. 0.25  
C. 0.38  
D. 0.88

### Q9. [2 Marks] [MCQ]

“The new measurement corroborates the earlier report, although it does not establish the proposed explanation.” Which paraphrase preserves both claims?


A. The measurement supports the report but does not by itself prove the explanation.
B. The measurement contradicts the report and disproves its explanation.
C. The measurement proves the report and every explanation consistent with it.
D. The measurement merely repeats the wording of the report without supplying evidence.

### Q10. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A positive quantity is repeatedly multiplied by2. Starting from3, what is the smallest number of multiplications needed to exceed1000? Equality would not suffice.

**Required precision:** Integer.

A. 18  
B. 9  
C. 5  
D. 10

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A checksum scheme adds 16-bit unsigned words using one's-complement addition: every carry beyond bit 15 is added back to the low 16 bits. The checksum is the bitwise complement of the final 16-bit sum. For the two words hexadecimal FFFF and 0001, what is the checksum's decimal value?

**Required precision:** Integer.

A. 131068  
B. 32767  
C. 65535  
D. 65534

### Q12. [1 Mark] [MCQ]

In a three-variable Karnaugh map, minterms 000 and 100 are adjacent. What term results from combining just these two minterms, with variables a,b,c in that order?

A. b′c′
B. a′b′
C. ac′
D. a+b+c

### Q13. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In `x=1; x=2; print(x);`, the first assignment has no side effects apart from storing x. Why may it be removed?

A. Its value is overwritten before any use.  
B. Every assignment of the constant one is invalid.  
C. print never reads its argument.  
D. The second assignment must also be removed.

### Q14. [1 Mark] [MSQ]

A real 2×2 matrix A has distinct eigenvalues 2 and −1. Which statements must hold?

A. A²−A−2I=0.
B. A is singular.
C. A is diagonalizable over the real numbers.
D. A must be symmetric.

### Q15. [1 Mark] [MCQ]

Consider `p=a*b; a=read_input(); q=a*b;`. Scalars do not alias, but read_input may return any value. Why is replacing the final a*b by p generally invalid?

A. Multiplication is never eligible for common-subexpression elimination.
B. Operand a may have changed since p was computed.
C. b must have changed.
D. p must be uninitialized.

### Q16. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In a three-address representation, evaluate `a+b*c` with normal multiplication precedence, without algebraic reordering. Which sequence is suitable?

A. t1=a+b; t2=t1*c  
B. t1=b*c; t2=a+t1  
C. t1=a*c; t2=t1+b  
D. t1=a+b; t2=b*c

### Q17. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A lexer returns the longest available operator token from {>,>=,>> ,>>=}, ignoring the displayed spacing in this set. With input >>>= and no whitespace, how many operator tokens does it return?

**Required precision:** Integer.

A. 2  
B. 4  
C. 1  
D. 3

### Q18. [1 Mark] [MCQ]

A recognizer accepts every member of L and may loop on nonmembers. Which extra guarantee would make that same machine a decider for L?

A. It uses at least two tape symbols.
B. It halts on every input, rejecting every nonmember.
C. It accepts one input quickly.
D. It has a finite written description.

### Q19. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A differentiable function on [0,3] has f(0)=1 and satisfies 2≤f′(x)≤5 throughout (0,3). Which value of f(3) is possible?

A. 6  
B. 10  
C. 17  
D. 20

### Q20. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A component is selected uniformly from two factories. Factory A produces10% defective components and factory B produces30% defective components. A selected component is found defective by a perfect inspection. What is the conditional probability that it came from B?

**Required precision:** Exact decimal.

A. 0.25  
B. 0.75  
C. 0.38  
D. 0.88

### Q21. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A depth-first search of a directed graph records discovery and finish times. Vertex u has interval [2,9] and vertex v has interval [4,7]. The graph contains an edge v→u. Which conclusion is necessarily correct?

A. The edge v→u is a tree edge.  
B. The graph contains a directed cycle.  
C. The edge v→u must be a cross edge.  
D. The graph must be acyclic because the intervals are nested.

### Q22. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A binary search tree contains distinct keys1,3,4,5,7,8 and has postorder traversal1,4,3,8,7,5. Starting from an empty BST and using ordinary leaf insertion without rotations, how many different insertion orders generate this exact tree?

**Required precision:** Exact integer.

A. 40  
B. 10  
C. 20  
D. 21

### Q23. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An8-bit ALU computes subtraction X−Y as X+(bitwise NOT Y)+1, retaining the low8 bits. Let X=10000000 and Y=00000001. Which combination is correct? Carry-out refers to the ninth bit of this addition, and signed overflow refers to two's-complement interpretation.

A. Result01111111; carry-out0; signed overflow0.  
B. Result01111111; carry-out1; signed overflow1.  
C. Result10000001; carry-out1; signed overflow0.  
D. Result01111111; carry-out0; signed overflow1.

### Q24. [1 Mark] [MSQ]

In the subset lattice of {a,b,c}, ordered by inclusion, which statements are correct?

A. The meet of{a,b} and{b,c} is{b}.
B. Their join is{a,b,c}.
C. They are comparable.
D. The empty set is a lower bound of every pair of elements.

### Q25. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

An IPv4 address set consists exactly of 192.0.2.32 through 192.0.2.95 inclusive. What is the smallest number of CIDR blocks whose union is exactly this set, with no extra addresses?

**Required precision:** Integer.

A. 4  
B. 1  
C. 2  
D. 3

### Q26. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A horizontal microinstruction has five independent one-bit control signals and an eight-bit next-address field. A redesigned encoding replaces the five control bits by a three-bit code selecting one of six permitted control combinations, retaining the next-address field unchanged. How many bits per microinstruction are saved?

**Required precision:** Integer.

A. 2  
B. 4  
C. 1  
D. 3

### Q27. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Over the alphabet {a,b}, let L contain exactly the strings that end in a and contain an even number of b symbols. The empty string is not in L. What is the number of states in a smallest complete DFA for L?

A. 3  
B. 6  
C. 2  
D. 4

### Q28. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A system has one instance each of resources R and S. P holds R and waits for S. Q holds S and waits for R. Resources cannot be preempted, and neither process releases its held resource until its request is satisfied. Which single policy change directly breaks a necessary deadlock condition for this execution?

A. Raise both process priorities equally.  
B. Allow a waiting process's held resource to be forcibly reclaimed.  
C. Add another ready process that requests neither resource.  
D. Increase the CPU clock frequency.

### Q29. [1 Mark] [MSQ]

For connected undirected weighted graphs, which statements are correct?

A. Repeated edge weights make a unique MST impossible.
B. Pairwise distinct edge weights guarantee a unique MST.
C. If the graph itself is a tree, it has a unique spanning tree regardless of repeated weights.
D. A globally heaviest edge can never belong to an MST, even if it is a bridge.

### Q30. [1 Mark] [MCQ]

At a scheduling decision, nonpreemptive highest-response-ratio-next uses score(waiting time+service time)/service time. Ready jobs P,Q,R have(waiting,service) pairs(6,3),(8,4),(5,1). Which job is selected?

A. P
B. Q
C. R
D. All have equal score.

### Q31. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

P is the 4×4 permutation matrix that cyclically shifts coordinates: P(x1,x2,x3,x4)ᵀ=(x4,x1,x2,x3)ᵀ. Find det(I+P).

**Required precision:** Integer.

A. 1  
B. 2  
C. 3  
D. 0

### Q32. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A binary max-heap is stored as [9,8,7,6,5,4,3]. Delete the maximum by moving the last element to the root, then repeatedly swapping it with the larger child until heap order is restored. Which array results?

A. [8,7,6,5,4,3]  
B. [8,6,7,3,5,4]  
C. [7,8,4,6,5,3]  
D. [8,6,7,5,3,4]

### Q33. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A table T(a,b) has a UNIQUE constraint on a and a separate NOT NULL constraint on b. Values of a are restricted to non-NULL values in the instances considered. Which statements must hold in every legal instance?

**Candidates**

**I.** No two rows have the same a value.

**II.** Every b value occurs in at most one row.

**III.** Every row has a non-NULL b value.

**IV.** Every possible non-NULL a value appears in a row.

A. II and IV  
B. III and IV  
C. I and II  
D. I and III

### Q34. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A two-input XOR gate's inputs are tied to the same Boolean signal x. Its output feeds one input of a two-input OR gate whose other input is y. How many of the four assignments to(x,y) make the circuit output1?

**Required precision:** Integer.

A. 4  
B. 1  
C. 2  
D. 3

### Q35. [1 Mark] [MCQ]

An instance of R(A,B) contains exactly(1,2) and(2,2). Which proposed functional dependency is violated by this instance?

A. A→B
B. AB→A
C. B→A
D. AB→B

### Q36. [2 Marks] [NAT]

A paged machine uses 1 KiB pages and two page-table levels. Its six-bit virtual page number splits into a two-bit root index and a four-bit leaf index. For root index 2, the root entry selects a leaf table whose entry 3 maps to physical frame 9. What physical byte address corresponds to virtual byte address (35×1024)+17? All mentioned mappings are valid.

**Answer format:** Integer.

### Q37. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Relations R(A,B) and S(B,C) each contain 100 tuples. B is a key of S, and every R.B value references an existing S.B value. No additional constraints are given. Under set semantics, how many tuples must R⋈S contain?

A. 0  
B. 100  
C. 10,000  
D. It cannot be determined even under these constraints.

### Q38. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For 0≤t≤1, define I(t)=∫₀¹|x−t| dx. Which statements are correct?

A. The minimum of I(t) is 1/4, attained only at t=1/2.  
B. I(t)+I(1−t)≥1/2 for all t in [0,1].  
C. ∫₀¹I(t) dt=1/2.  
D. The set of t in [0,1] satisfying I(t)≤5/16 is an interval of length 1/2.

### Q39. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A process has virtual pages0–7. A page table maps pages0,1,4,5 to physical frames3,7,3,9; other pages are absent. The page size is1024 bytes. How many distinct physical byte addresses are represented by all valid virtual addresses in those four mapped pages?

**Required precision:** Integer.

A. 6144  
B. 3072  
C. 1536  
D. 3073

### Q40. [2 Marks] [MSQ]

Grammar E→E+T | T, T→T*F | F, F→id has its usual parse-tree interpretation. Which statements are true?

A. Multiplication binds more tightly than addition.
B. A chain of additions is left-associated.
C. The grammar is immediately suitable for a naive recursive-descent parser without eliminating left recursion.
D. The word id+id*id has two parse trees under this grammar.

### Q41. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A directed graph has edges s→a of weight 3, s→b of weight 8, a→b of weight −4, b→c of weight 2, and a→c of weight 7. Reweight each edge by w'(u,v)=w(u,v)+h(u)−h(v), with h(s)=0, h(a)=0, h(b)=−4, h(c)=−2. What is the shortest-path distance from s to c in the reweighted graph?

**Required precision:** Exact integer.

A. 6  
B. 2  
C. 3  
D. 4

### Q42. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Run stable insertion sort in increasing order on [4,1,3,1,2]. In each iteration, shift only elements strictly larger than the key one position right. Count only these rightward shifts, not the final placement of the key. How many shifts occur?

**Required precision:** Integer.

A. 6  
B. 12  
C. 3  
D. 7

### Q43. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A512-byte slotted page has a32-byte fixed header and six retained four-byte slot entries. Each record must occupy a contiguous region. Its six records, in adjacent physical order, have lengths60,70,80,50,40,30 bytes. All remaining free space is one contiguous gap between the slot directory and records. Delete the adjacent80-byte and50-byte records, retaining their slot entries. A new record must use a new four-byte slot entry. What is the increase in the maximum insertable record length if the remaining records may be compacted, compared with insertion without moving them?

**Required precision:** Integer bytes.

A. 244  
B. 61  
C. 122  
D. 123

### Q44. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A B+ tree root has two leaf children, containing[2,5] and[8,11]. Leaves hold at most 3 keys. Inserting into a full leaf first forms four sorted keys, then splits them into two leaves with two keys each. The first key of the new right leaf is copied to the parent. Internal nodes can have at most 3 children. Insert 6, then7. How many keys are in the root afterward?

**Required precision:** Exact integer.

A. 4  
B. 1  
C. 3  
D. 2

### Q45. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A hash table has slots0 through6 and uses linear probing with h(k)=k modulo7. Insert keys0,7,14,1 in that order. Delete7 by marking its slot EMPTY rather than using a tombstone or moving entries. A search stops at the first EMPTY slot. How many of the remaining three stored keys are now incorrectly reported absent by their ordinary searches?

**Required precision:** Integer.

A. 2  
B. 4  
C. 1  
D. 3

### Q46. [2 Marks] [MCQ]

A recovery system uses immediate updates with write-ahead logging, undo of uncommitted transactions and redo of committed transactions. Since the last checkpoint, the log records T1 changing X from 5 to 8, T2 changing Y from 4 to 9, and T1 committing. A crash occurs before T2 commits. Disk may contain either old or new values of each item. After recovery, what must (X,Y) be?

A. (5,4)
B. (8,9)
C. (8,4)
D. (5,9)

### Q47. [2 Marks] [NAT]

For observations0,0,4,10, first choose x to minimize the sum of absolute deviations from x. Among all such minimizers, choose x to minimize the sum of squared deviations. What value is selected?

**Answer format:** Exact decimal.

### Q48. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Consider the grammar S→aSbS | bSaS | ε. How many distinct leftmost derivations produce the word abab? Count derivations differing in production choices or in which substrings are generated by the two occurrences of S separately.

**Required precision:** Exact integer.

A. 4  
B. 1  
C. 3  
D. 2

### Q49. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A process uses a 32-bit virtual address with 4 KiB pages. Two-level paging divides the address into a 10-bit directory index, a 10-bit second-level index, and a 12-bit offset. Every directory and second-level table occupies exactly one 4 KiB physical page. A second-level table is allocated only if it contains at least one valid mapping. Exactly virtual page numbers 0,1023,1024 and 1048575 are mapped. No page-table pages are shared. Including the directory but excluding mapped data pages, how many KiB of physical memory do the page tables occupy?

**Required precision:** Numeric value; integer.

A. 32  
B. 16  
C. 8  
D. 17

### Q50. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A finite monoid M has identity e and satisfies left cancellation: ax=ay implies x=y for all a,x,y in M. Which statements follow?

A. For fixed a, the map x↦ax is a bijection on M.  
B. Every a has a right inverse b with ab=e.  
C. Such a b also satisfies ba=e.  
D. The conclusion that every element is invertible follows by the same finite-cardinality argument for arbitrary infinite monoids.

### Q51. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

In an undirected graph with vertices s,a,b,t, edges have weights sa=1,sb=1,ab=0,at=1,bt=1. A path must be simple, so it cannot repeat vertices. How many shortest s-to-t paths exist?

**Required precision:** Integer.

A. 8  
B. 2  
C. 5  
D. 4

### Q52. [2 Marks] [NAT]

Among all monic real quadratics p(x)=x²+ax+b, what is the smallest possible value of max{|p(x)|: −1≤x≤1}?

**Answer format:** Exact finite decimal.

### Q53. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A memory device has address inputs A0–A9 and one active-high chip-select. A system connects only A0–A8 to varying address bits and permanently ties A9 to0. What fraction of the device's addressable locations can be selected through this wiring?

**Required precision:** Exact decimal.

A. 0.5  
B. 0.3  
C. 0.8  
D. 0.1

### Q54. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

An HTTP client has no DNS cache and needs one DNS lookup taking20 ms. Establishing a TCP connection takes one RTT of40 ms. A base HTML request and response take one additional RTT; transmission times are negligible. The HTML references three small objects on the same server, discovered only after the HTML arrives. A single persistent connection fetches these objects sequentially with one RTT per object, without pipelining. How many milliseconds are saved by pipelining all three object requests together after receiving the HTML? DNS, connection establishment and base retrieval are unchanged.

**Required precision:** Integer.

A. 80  
B. 160  
C. 40  
D. 81

### Q55. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A syntax-directed translator emits postfix code for fully parenthesized binary expressions. It recursively emits the entire left operand, then the entire right operand, and finally the binary operator. The generated code is evaluated on an initially empty stack: an operand pushes one value, and an operator pops two values and pushes their result. No temporary storage other than this stack is used. What is the maximum stack depth reached when evaluating the translation of `(a+b)*(c+(d*e))`?

A. 4  
B. 8  
C. 2  
D. 5

### Q56. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A binary-input transducer outputs, after reading each input bit, that bit XOR the preceding input bit; before the first input the preceding bit is defined to be zero. Implement it as a deterministic Moore machine whose output after each input is determined by its reached state. The initial state's output before any input is ignored. What is the minimum number of states?

**Required precision:** Integer.

A. 8  
B. 4  
C. 2  
D. 5

### Q57. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A processor first checks L1. Every L1 access takes 1 ns. On an L1 miss it next checks L2, taking an additional 6 ns; on an L2 miss it additionally accesses memory, taking 60 ns. There is no overlap. Initially the L1 miss probability is 0.10 and the L2 local miss probability conditional on an L1 miss is 0.20. An L1 redesign reduces its miss probability to 0.05 but changes its access time to t ns. L2 timing and its conditional miss probability remain unchanged. For strictly lower average access time, which condition on t is necessary and sufficient?

A. t < 1.9 ns  
B. t < 2.8 ns  
C. t < 1.3 ns  
D. t < 3.6 ns

### Q58. [2 Marks] [MCQ]

Which expression is guaranteed to stay within the same C array object when a is an array of four integers and p=a+4? Forming a one-past pointer is permitted, but dereferencing it is not.

A. *p
B. *(p−1)
C. *(p+1)
D. a[4]

### Q59. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A four-bit signed fixed-point format has no fractional bits and uses saturating addition: results above 7 become 7, and results below −8 become −8. Let ⊕ denote this addition. For a=6,b=5,c=−4, what is `a⊕(b⊕c) − ((a⊕b)⊕c)`, with the final subtraction performed as an exact ordinary integer subtraction?

**Required precision:** Integer.

A. 8  
B. 4  
C. 2  
D. 5

### Q60. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A closure captures a local variable by reference. The closure can be invoked after its defining procedure returns. Which statements are correct?

**Candidates**

**I.** The captured storage must remain valid for those later invocations.

**II.** Keeping only a pointer into an already-reused stack frame is always sufficient.

**III.** Heap allocation or another lifetime-preserving mechanism can support the capture.

**IV.** Lexical scope alone guarantees that arbitrary stack storage remains allocated forever.

A. I and IV  
B. II and III  
C. I and III  
D. II and IV

### Q61. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A toy binary floating-point system has precision 3 significant bits, unbounded exponents, and rounding to nearest with ties to even. Every addition is rounded immediately. Let a=8, b=1, c=1. What is the numerical value of (a+(b+c))−((a+b)+c), where the final subtraction is evaluated exactly on the two already rounded results?

**Required precision:** Exact integer.

A. 4  
B. 2  
C. 1  
D. 3

### Q62. [2 Marks] [MCQ]

A queue is represented by a circular array of length 8. head points to the next element to remove, tail to the next free insertion slot, and one slot is always left unused. Initially head=6 and tail=2. Execute dequeue, enqueue X, enqueue Y, dequeue, enqueue Z, with all operations successful. What are (head,tail,number of stored elements) at the end?

A. (0,5,5)
B. (0,5,4)
C. (1,5,4)
D. (0,4,4)

### Q63. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A sender uses selective-repeat ARQ with 3-bit sequence numbers and sender and receiver windows both of size 4. The receiver initially expects sequence numbers 0–3. It receives 0,2,3,1 in that order, with no corruption or loss. After each arrival it delivers all newly available contiguous packets in order and slides its window. What is the lower edge of its receive window after all four arrivals?

**Required precision:** Integer sequence number.

A. 4  
B. 8  
C. 2  
D. 5

### Q64. [2 Marks] [MCQ]

A synchronous two-flip-flop machine starts at (q1,q0)=(0,1). On input 0 its next state is (0,1). On input 1 its next state is (q1 XOR q0, q1). After processing exactly five input bits, it accepts if its state is (0,1). How many of the 32 input strings are accepted?

A. 16
B. 17
C. 18
D. 20

### Q65. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A compiler performs copy propagation on `x=y; z=x+1; y=5; w=x+1;`, with exact ordinary scalar variables and no aliases. Which replacement of both uses of x is valid for every initial y?

A. Replace both by the current y without any saved value.  
B. Replace only the use in z by y; the later use needs the old value represented by x or another saved copy.  
C. Replace both by 5.  
D. Replace neither use under any circumstances.

## ANSWER KEY — MOCK TEST 078

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MSQ | 1 | A, C |
| 2 | MCQ | 1 | B |
| 3 | MSQ | 1 | A, C, D |
| 4 | MCQ | 1 | B |
| 5 | MSQ | 1 | A, C |
| 6 | MCQ | 2 | C |
| 7 | MSQ | 2 | A, B, D |
| 8 | MSQ | 2 | B, C, D |
| 9 | MCQ | 2 | A |
| 10 | MCQ | 2 | B |
| 11 | MSQ | 1 | A, B, C |
| 12 | MCQ | 1 | A |
| 13 | MSQ | 1 | B, C, D |
| 14 | MSQ | 1 | A, C |
| 15 | MCQ | 1 | B |
| 16 | MSQ | 1 | A, C, D |
| 17 | MSQ | 1 | B, C, D |
| 18 | MCQ | 1 | B |
| 19 | MSQ | 1 | A, C, D |
| 20 | MCQ | 1 | B |
| 21 | MSQ | 1 | A, C, D |
| 22 | MSQ | 1 | A, B, D |
| 23 | MSQ | 1 | A, C, D |
| 24 | MSQ | 1 | A, B, D |
| 25 | MCQ | 1 | C |
| 26 | MSQ | 1 | B, C, D |
| 27 | MSQ | 1 | B, C, D |
| 28 | MSQ | 1 | A, C, D |
| 29 | MSQ | 1 | B, C |
| 30 | MCQ | 1 | C |
| 31 | MSQ | 1 | A, B, C |
| 32 | MSQ | 1 | A, C, D |
| 33 | MCQ | 1 | D |
| 34 | MCQ | 1 | C |
| 35 | MCQ | 1 | C |
| 36 | NAT | 2 | 9233 |
| 37 | MSQ | 2 | A, C, D |
| 38 | MCQ | 2 | C |
| 39 | MSQ | 2 | A, C, D |
| 40 | MSQ | 2 | A, B |
| 41 | MSQ | 2 | A, B, D |
| 42 | MSQ | 2 | B, C, D |
| 43 | MSQ | 2 | A, B, D |
| 44 | MSQ | 2 | A, B, C |
| 45 | MCQ | 2 | A |
| 46 | MCQ | 2 | C |
| 47 | NAT | 2 | 3.5 |
| 48 | MCQ | 2 | D |
| 49 | MCQ | 2 | B |
| 50 | MCQ | 2 | D |
| 51 | MCQ | 2 | D |
| 52 | NAT | 2 | 0.5 |
| 53 | MSQ | 2 | B, C, D |
| 54 | MCQ | 2 | A |
| 55 | MSQ | 2 | B, C, D |
| 56 | MCQ | 2 | B |
| 57 | MSQ | 2 | B, C, D |
| 58 | MCQ | 2 | B |
| 59 | MCQ | 2 | B |
| 60 | MCQ | 2 | C |
| 61 | MCQ | 2 | B |
| 62 | MCQ | 2 | A |
| 63 | MSQ | 2 | B, C, D |
| 64 | MCQ | 2 | C |
| 65 | MSQ | 2 | A, C, D |
