# GATE CS 2027 — Full-Length Mock Test 053

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

Choose the sentence in which the opening phrase clearly modifies the intended subject and the list has parallel grammatical form.

A. After examining the records, several errors were found by Mira in dates, to calculate totals, and filing.  
B. After examining the records, the totals were checked by Mira and correcting dates.  
C. After examining the records, Mira corrected the dates, recalculated the totals, and reorganized the files.  
D. After examining the records, correcting the dates, the totals were recalculated by Mira.

### Q2. [1 Mark] [NAT]

A fair six-sided die is rolled. If the first result is odd, it is discarded and the die is rolled once more; otherwise the first result is retained. The second result, if rolled, is always retained. What is the probability that the retained result is6?

**Answer format:** Exact decimal.

### Q3. [1 Mark] [MCQ]

“The panel vacillated between the two proposals, repeatedly reversing its tentative preference.” Which word best replaces vacillated without changing the meaning?

A. Wavered
B. Collaborated
C. Converged
D. Disappeared

### Q4. [1 Mark] [NAT]

How many integers x with1≤x≤1000 satisfy floor(log2 x)=floor(log3 x)? Here floor denotes the greatest integer not exceeding its argument.

**Answer format:** Exact integer.

### Q5. [1 Mark] [MCQ]

For a two-digit number with nonzero unequal digits, operation R reverses the digits and operation S replaces each digit d by 9−d. Which statement holds whenever the intermediate results are interpreted as two-digit strings, allowing a leading zero?

A. R followed by S always equals S followed by R.
B. Applying R twice always produces S's result.
C. Applying S twice always swaps the digits.
D. R followed by S always leaves the original string unchanged.

### Q6. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Four unit cubes occupy grid positions (0,0,0), (1,0,0), (1,1,0), and (1,1,1). A position (i,j,k) denotes the cube [i,i+1]×[j,j+1]×[k,k+1]. What is the total exposed surface area of their union, in square units? Shared full faces are internal; contact along an edge does not hide any face area.

**Required precision:** Exact integer.

A. 36  
B. 18  
C. 9  
D. 19

### Q7. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A ten-entry sequence was intended to contain the first ten positive odd integers in order. Exactly one entry was replaced by a different integer. The recorded entries b1,…,b10 satisfy Σ b(i)=106 and Σ i·b(i)=757. What was the intended value of the altered entry?

**Required precision:** Exact integer.

A. 26  
B. 7  
C. 13  
D. 14

### Q8. [2 Marks] [NAT]

Two concentric circles have radii 5 and 3. A straight chord of the larger circle is tangent to the smaller circle. What is the chord's length?

**Answer format:** Integer.

### Q9. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Choose the sentence that preserves both the conditional meaning and correct grammar: the machine should be restarted only after the valve has been closed.

A. Restart the machine before the valve has been closed.  
B. Do not restart the machine until the valve has been closed.  
C. Closing the valve is unnecessary before restarting the machine.  
D. The machine must restart whenever the valve closes, without any other condition.

### Q10. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

An examination awards4 marks for a correct response, subtracts1 for a wrong response and awards0 for an omitted question. A candidate attempted75% of40 questions and scored75 marks. How many attempted responses were wrong?

**Required precision:** Integer.

A. 18  
B. 5  
C. 10  
D. 9

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

A pushdown automaton recognizes {a^n b^n : n≥0}. It pushes one marker per a, then pops one per b, rejecting any a after a b. Which extra condition is needed to avoid accepting strings with fewer b's than a's?

A. Accept as soon as the first b is read.
B. At end of input, require that no unmatched a markers remain.
C. Require at least one input symbol.
D. Ignore the stack once any b has been read.

### Q12. [1 Mark] [MSQ]

L is a language over {a,b}, and its complement is taken with respect to {a,b}*. Which statements necessarily hold?

A. If both L and its complement are finite, then {a,b}* is finite.
B. If L is regular, its complement is context-free.
C. If L is context-free, its complement is regular.
D. If L is finite, its complement is regular.

### Q13. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A sorted data file has fixed-length records, with exactly eight records per data page and no unused slots. A range query matches exactly 16 consecutive records in file order. An index lookup requires exactly two page reads and identifies the first matching record's page and slot. Index pages are separate from data pages, no page is initially cached, and scanning the range reads each needed data page once. What is the largest possible total number of page reads, over the possible starting slots?

A. 3  
B. 4  
C. 5  
D. 6

### Q14. [1 Mark] [MCQ]

A B+ tree's root contains separator20 and has two leaf children: [5,10] and [20,30]. The separator is defined as the minimum key of the right child. Each leaf must contain at least one key. After deleting20, which action is required under this separator convention?

A. Merge the leaves because a leaf cannot contain one key.
B. Change the root separator to30; no merge is required.
C. Leave separator20 because internal separators must never change.
D. Remove the root and discard the left leaf.

### Q15. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A circuit-switched connection reserves 64 kbit/s continuously for a one-second interval but carries only 40,000 payload bits during that interval. With 1 kbit=1000 bits, what is its payload utilization percentage?

**Required precision:** Exact finite decimal percentage, without the percent sign.

A. 125.0  
B. 62.5  
C. 31.3  
D. 63.5

### Q16. [1 Mark] [MCQ]

A three-input Boolean function satisfies F(x,y,z)=NOT F(NOT x,NOT y,NOT z) on every input and F(0,0,0)=0. How many different truth tables satisfy these conditions?

A. 4
B. 8
C. 16
D. 32

### Q17. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Which words belong to the language denoted by a*b | ab*?

A. aab  
B. abb  
C. ab  
D. ba

### Q18. [1 Mark] [NAT]

A dynamic program counts ordered sequences of steps of sizes1 or2 whose sum is4, but forbids two consecutive size1 steps. How many sequences are counted?

**Answer format:** Integer.

### Q19. [1 Mark] [NAT]

A divide-and-conquer procedure on 16 elements repeatedly splits each nontrivial problem into equal halves until size one. How many leaves are in its recursion tree?

**Answer format:** Integer.

### Q20. [1 Mark] [NAT]

On the power set of {1,2,3,4}, define X~Y exactly when |X| and |Y| have the same remainder modulo 3. How many equivalence classes does this relation have?

**Answer format:** Integer.

### Q21. [1 Mark] [NAT]

Distinct values1,2,3,4,5 arrive in that order at a single stack. Each value is pushed exactly once and popped exactly once; pushes and pops may be interleaved. How many distinct full output permutations can have4 as their first popped value?

**Answer format:** Integer.

### Q22. [1 Mark] [MSQ]

A database permits uncommitted updates to reach disk and uses an undo log. Before overwriting an on-disk data item, its old value is forced into the log. Which statements are correct?

A. The log-before-data rule supplies information needed to undo an uncommitted on-disk update.
B. Writing the old value to the log only after overwriting the disk item is equally safe against a crash between those writes.
C. A transaction's abort may require restoring disk data, not merely clearing a memory buffer.
D. The stated rule by itself proves that every committed update is already on disk.

### Q23. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A transmitted binary word contains data bits followed by one even-parity bit. The receiver checks only whether the parity of the whole received word is even. Which errors are always detected?

**Candidates**

**I.** Exactly one data bit flips.

**II.** Exactly two data bits flip.

**III.** Exactly one data bit and the parity bit flip.

**IV.** Exactly three distinct bits of the word flip.

A. I and IV  
B. III and IV  
C. I and II  
D. I and III

### Q24. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A real3×3 matrix A satisfies A²=A and has rank2. What is det(A+2I)?

**Required precision:** Exact number.

A. 36  
B. 9  
C. 19  
D. 18

### Q25. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A four-variable Boolean function F(A,B,C,D), with A as the most significant bit of the minterm index, is 1 at minterms 1,3,9,11. Minterms 0,2,8,10 are don't-cares, and all remaining minterms are 0. Which is a minimum-literal sum-of-products implementation?

A. NOT B  
B. NOT D  
C. A OR C  
D. (NOT B) AND D

### Q26. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A rooted ordered tree has root R with children A,B,C in that order. A has children D,E, B has none and C has child F. In the left-child/right-sibling binary representation, how many right-sibling pointers are non-null?

**Required precision:** Integer.

A. 6  
B. 2  
C. 4  
D. 3

### Q27. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In ordinary constant propagation, one predecessor of block B assigns x=4 and another assigns x=7. Both paths are feasible. No assignment to x occurs at B before its first use. What can be concluded at entry to B?

A. x is the constant 4.  
B. x is the constant 7.  
C. x is not a single known constant at this merge.  
D. x is uninitialized on both paths.

### Q28. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

On {1,2,3,4}, a relation initially contains (1,2),(2,1),(2,3),(3,4). How many ordered pairs are in its reflexive transitive closure?

**Required precision:** Integer.

A. 22  
B. 6  
C. 12  
D. 11

### Q29. [1 Mark] [NAT]

A component is selected uniformly from two factories. Factory A produces10% defective components and factory B produces30% defective components. A selected component is found defective by a perfect inspection. What is the conditional probability that it came from B?

**Answer format:** Exact decimal.

### Q30. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A binary search tree stores distinct keys. A node x has both a left and a right child. Its inorder successor s is used when deleting x. Which statements about s in the tree before deletion are correct?

A. s is in the right subtree of x.  
B. s must be a leaf.  
C. s has no left child.  
D. s may have a right child.

### Q31. [1 Mark] [MSQ]

A partially ordered set has elements0,a,b,1, with0<a<1 and0<b<1; a and b are incomparable. Which statements are correct?

A. a and b have meet0 and join1.
B. The poset is a total order.
C. The poset is a lattice.
D. There is no upper bound of both a and b.

### Q32. [1 Mark] [MCQ]

A process forks, then its child successfully executes a new program using exec. Which statement is correct under ordinary process semantics?

A. exec necessarily creates another process with a new process identifier.
B. The child keeps its process identity while its program image is replaced.
C. The parent's program image is replaced by the child's exec.
D. The child resumes at the instruction after the successful exec call in its old program.

### Q33. [1 Mark] [MCQ]

Two control-unit designs implement the same instruction-set behaviour. One stores sequences of control words in a control memory; the other generates signals through fixed combinational/sequential logic. Which statement is correct?

A. The first is microprogrammed; changing its control words may change instruction sequencing without redesigning all control logic.
B. The first cannot contain any sequencing logic.
C. The second must fetch a microinstruction from control memory every cycle.
D. Both designs must expose the same internal control-word format to application programs.

### Q34. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

After fork, a parent and child initially share read-only physical pages under copy-on-write. Each has its own virtual mappings. Which statements are correct?

**Candidates**

**I.** The first write by one process may trigger a fault and a private copy.

**II.** Every page must be copied immediately at fork under this scheme.

**III.** A successful private copy can allow one process to modify its page without changing the other's contents.

**IV.** Sharing a physical page initially implies that later writes must always be visible to both processes.

A. I and III  
B. I and II  
C. I and IV  
D. II and III

### Q35. [1 Mark] [MCQ]

A byte-addressed 4 KiB window maps to a 2 KiB memory chip. Address bits A10–A0 reach the chip; A11 is ignored and the chip is selected throughout the window 0x000–0xFFF. Which other address accesses the same stored byte as 0x134?

A. 0x135
B. 0x234
C. 0x534
D. 0x934

### Q36. [2 Marks] [MSQ]

A schedule consists of w1(x),w2(x),w1(x), followed by commits after all writes. There are no reads. The first and last writes belong to T1 and the middle write to T2. All writes assign fixed constants independently of prior values. Which statements are correct?

A. Its conflict graph is acyclic.
B. It is view-equivalent to the serial order T2,T1.
C. It is conflict-serializable.
D. Its final writer of x is T1.

### Q37. [2 Marks] [NAT]

An undirected graph has edges sa,sb,ac,bc,cd,ad. BFS from s records distances and counts the number of shortest paths to each vertex. What is the number of shortest s-to-d paths?

**Answer format:** Exact integer.

### Q38. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A simple undirected graph has 64 vertices and m edges. An adjacency matrix uses one bit per possible ordered vertex pair. An adjacency-list representation uses one 32-bit head pointer per vertex and one 32-bit neighbour entry for each direction of every edge, with no other storage. What is the largest integer m for which the list uses strictly fewer bits than the matrix?

**Required precision:** Integer.

A. 62  
B. 16  
C. 31  
D. 32

### Q39. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An undirected connected graph may have equal edge weights. For one edge e, there is a cut for which e is the unique lightest crossing edge. Which statements must hold?

**Candidates**

**I.** Every minimum spanning tree contains e.

**II.** e is the unique lightest edge in the entire graph.

**III.** If a spanning tree omits e, adding e creates a cycle containing another edge crossing that cut.

**IV.** The graph has a unique minimum spanning tree.

A. I and II  
B. I and III  
C. I and IV  
D. II and III

### Q40. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

For an integer t in {0,1,2,3,4,5}, let A(t)=[[t,1,0],[1,1,1],[0,1,2]]. How many choices of t make A(t) nonsingular but prevent a factorization A(t)=LU with unit lower-triangular L and upper-triangular U, without row permutations?

**Required precision:** Integer.

A. 4  
B. 1  
C. 2  
D. 3

### Q41. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A cache performs write-through with a write buffer of capacity two pending writes. Stores occur at cycles0,1,2. Each buffered write occupies memory for five cycles, serially, and the first begins immediately at cycle0. A completed write leaves the buffer at the start of its completion cycle; a blocked store can enter then. How many cycles does the third store wait before entering the buffer? Count the in-service write as occupying one buffer slot.

**Required precision:** Integer.

A. 3  
B. 6  
C. 2  
D. 4

### Q42. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A four-port Ethernet switch initially has dynamic entries A→1, B→2, C→3 and no entry for D. It learns or updates the source port before forwarding each frame, floods an unknown destination to every port except ingress, and has no entry expiry during this sequence. Four frames arrive in order: (ingress 3, source A, destination B), (ingress 2, source B, destination A), (ingress 3, source C, destination D), (ingress 4, source D, destination C). Which lists their respective egress-port sets?

A. {2}; {3}; {1,2,4}; {3}  
B. {2}; {1}; {1,2,4}; {3}  
C. {2}; {3}; {1,2,3,4}; {3}  
D. {2}; {3}; {4}; {1,2,3}

### Q43. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A ternary relation R(S,P,J) contains (s1,p1,j1),(s1,p2,j2),(s2,p1,j2). Form the natural join of its three binary projections on SP, SJ and PJ, using set semantics. Which statements are correct?

A. The join has four tuples.  
B. The join contains the spurious tuple (s1,p1,j2).  
C. Joining all binary projections of any ternary relation always recovers exactly that relation.  
D. The original R satisfies SP→J.

### Q44. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An ordinary binary search tree stores distinct integers. A search for key 45 visits keys 50,20,40,47,45 in that order. Which additional statement is consistent with the BST search constraints?

**Candidates**

**I.** The next node after 40 could instead have been 48.

**II.** The next node after 20 could instead have been 55.

**III.** Every node visited after 47 on this search must have key below 47 and above 40 until 45 is found.

**IV.** The path is impossible because it changes direction more than once.

A. I and IV  
B. II and III  
C. II and IV  
D. I and III

### Q45. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Evaluate ∫₀¹ ln(1+x)/(1+x) dx, rounded to four decimal places.

**Required precision:** Number to 4 decimal places.

A. 0.2402  
B. 0.7598  
C. 0.1201  
D. 0.6201

### Q46. [2 Marks] [NAT]

A distance-vector router has neighbours A and B with link costs2 and5. Their advertised distances to destination d are7 and3 respectively. No other routes exist. What distance does the router select?

**Answer format:** Integer.

### Q47. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Relations R(A,B)={(1,x),(1,y),(2,x),(3,z)} and S(B,C)={(x,p),(x,q),(y,p)} use set semantics. How many tuples remain after naturally joining R with S and then projecting onto(A,C)?

**Required precision:** Integer.

A. 8  
B. 2  
C. 5  
D. 4

### Q48. [2 Marks] [MCQ]

A four-input Boolean function F(a,b,c,d) equals 1 exactly when at least three inputs are 1. It is implemented using a 4-to-1 multiplexer whose select bits are b (more significant) and c (less significant). Data inputs I0, I1, I2, I3 correspond respectively to bc = 00, 01, 10, 11. Which tuple of data-input functions implements F? Here juxtaposition means AND and + means OR.

A. (0, ad, ad, a+d)  
B. (0, a+d, a+d, ad)  
C. (ad, ad, ad, 1)  
D. (0, 0, 0, a+d)

### Q49. [2 Marks] [NAT]

Let s=aabbb and L=a*b*. Consider decompositions s=xyz satisfying |xy|≤3 and |y|>0. How many such decompositions have xy^i z in L for every integer i≥0? Different choices of the lengths of x and y count separately.

**Answer format:** Integer.

### Q50. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Evaluate a binary expression tree using two rules: evaluate both children recursively, retain the first child's result while evaluating the second, then combine the results in one register and release the other. Leaves require one register. Child evaluation order may be chosen independently at each node, and no spilling or recomputation is allowed. The expression is `(a+b)*((c+d)+(e+f))`, with all leaves distinct. What is the minimum number of registers needed?

**Required precision:** Integer.

A. 6  
B. 3  
C. 2  
D. 4

### Q51. [2 Marks] [MSQ]

In this control-flow fragment, a and b are not modified, and arithmetic has no side effects or overflow:

```text
if flag:
    t = a + b
else:
    u = a + b
v = a + b
```

Which statements are correct?

A. The expression a+b has been evaluated on every path reaching the assignment to v.
B. Replacing v=a+b with v=t is always valid even if t is undefined on the else path.
C. A compiler may compute a+b into one common temporary before the branch and use it on both paths and afterward.
D. Replacing v=a+b with v=u is always valid even if u is undefined on the then path.

### Q52. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A direct-mapped cache has two 16-byte lines, is initially empty, and uses write-back with write allocation. Arrays A and B each contain four four-byte words. A begins at byte address 0 and B at byte address 32. Execute, for i=0,1,2,3, in this order: read A[i], write B[i], read A[i]. Each miss transfers one whole block from memory; each dirty eviction writes one whole block to memory. Ignore all other traffic and do not flush the cache afterwards. How many bytes are transferred between cache and memory in total?

**Required precision:** Integer.

A. 208  
B. 416  
C. 104  
D. 209

### Q53. [2 Marks] [MSQ]

An undirected simple graph with n vertices and m edges is represented either by a Boolean adjacency matrix or adjacency lists. Lists are unsorted and store each undirected edge twice. Which worst-case bounds hold?

A. The matrix uses Θ(n²) entries even for an empty graph.
B. Enumerating all neighbours of v from the matrix takes Θ(deg(v)) time for every v without extra indexing.
C. Enumerating all neighbours of v from its list takes Θ(1+deg(v)) time, including access to an empty list.
D. The lists require Θ(n+m) storage, including vertex headers.

### Q54. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A system defines the working set immediately after a reference as the distinct pages in that reference and the previous three references, or all references so far if fewer than four exist. For the reference string 1,2,1,3,4,2,4,5, what is the sum of the working-set sizes immediately after references 4 through 8?

**Required precision:** Integer.

A. 34  
B. 9  
C. 17  
D. 18

### Q55. [2 Marks] [MSQ]

Consider the simple complete bipartite graph K2,3. A Hamiltonian path visits every vertex exactly once; an Euler trail uses every edge exactly once. Which statements are correct?

A. It has an Euler trail.
B. It has an Euler circuit.
C. It has a Hamiltonian path.
D. It has no Hamiltonian cycle.

### Q56. [2 Marks] [MSQ]

Suppose a hypothetical oracle correctly answers whether any supplied ordinary Turing machine halts on any supplied input. Fix an ordinary recognizer M of a language L. Which tasks become possible using this oracle?

A. Decide whether any given word belongs to L by first querying whether M halts and, when it does, simulating its outcome.
B. Conclude that M must already halt on every word without querying the oracle.
C. Enumerate the complement of L by testing words one by one with the resulting oracle-assisted decision procedure.
D. Replace all oracle calls by one universal fixed finite simulation-time bound for ordinary machines.

### Q57. [2 Marks] [NAT]

What integer is printed? All pointed-to objects remain alive.

```c
void change(int **p, int *q) {
    **p += 2;
    *p = q;
    **p += 3;
}
/* Inside main: */
int x=4, y=7;
int *p=&x;
change(&p, &y);
printf("%d", x+y+*p);
```

**Answer format:** Integer.

### Q58. [2 Marks] [NAT]

How many binary strings of length 6 contain exactly two occurrences of the substring 01? Occurrences are counted by their starting positions.

**Answer format:** Exact integer.

### Q59. [2 Marks] [NAT]

A directed acyclic graph has edges s→a of weight 4, s→b of weight 2, a→b of weight −3, a→t of weight 4, b→t of weight 2. How many distinct s-to-t paths have total weight at most 4?

**Answer format:** Integer.

### Q60. [2 Marks] [NAT]

A synchronous three-bit register has next-state rule (a,b,c)→(b,c,a XOR c), using old bits simultaneously. Starting at 001, how many clock edges occur before the state first becomes 100?

**Answer format:** Integer.

### Q61. [2 Marks] [NAT]

Two IPv4 fragments of the same original datagram have fragment offsets 0 and 120, and payload lengths 1000 and 600 bytes, respectively. Offsets use the standard eight-byte units. How many original payload-byte positions are covered by both fragments?

**Answer format:** Integer.

### Q62. [2 Marks] [MCQ]

A regular file contains bytes ABCDE. Descriptor p opens it at offset zero; q=dup(p); descriptor r comes from a separate open of the same file, also at zero. With no intervening operations, execute read(p,2), read(q,1), seek(r,1 from start), read(r,2), read(p,1). All reads succeed fully. What are the byte strings from the four reads in order?

A. AB; A; BC; A
B. AB; C; BC; E
C. AB; C; DE; D
D. AB; C; BC; D

### Q63. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

In the additive group Z8×Z2, how many elements have order exactly four?

**Required precision:** Integer.

A. 4  
B. 8  
C. 2  
D. 5

### Q64. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A lexer uses maximal munch, breaking equal-length ties by rule priority. Its tokens include INTEGER=[0-9]+, REAL=[0-9]+\.[0-9]*, and RANGE=\.\., where an escaped dot denotes a literal dot. A single dot is not a token. For input1..2, which statements are correct?

A. The first token under these rules is REAL with lexeme `1.`.  
B. Giving RANGE highest priority makes the first token INTEGER with lexeme1.  
C. After the first token, scanning encounters a dot at which no token can start.  
D. Requiring at least one digit after the dot in REAL would allow the tokenization INTEGER,RANGE,INTEGER.

### Q65. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An interrupt source sets a single pending bit on each event; setting an already-set bit has no extra effect. Interrupts are masked until time 5. Events occur at times 1,2,3,6. On entering a handler the bit is cleared; each handler lasts two time units, and events during it can set the bit again. A pending interrupt is handled immediately when unmasked and no handler is running. Which pair gives the number of handler invocations and the final handler's completion time?

A. (4,13)  
B. (2,9)  
C. (1,7)  
D. (3,11)

## ANSWER KEY — MOCK TEST 053

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MSQ | 1 | A, B, D |
| 2 | NAT | 1 | 0.25 |
| 3 | MCQ | 1 | A |
| 4 | NAT | 1 | 2 |
| 5 | MCQ | 1 | A |
| 6 | MCQ | 2 | B |
| 7 | MCQ | 2 | C |
| 8 | NAT | 2 | 8 |
| 9 | MSQ | 2 | A, C, D |
| 10 | MCQ | 2 | D |
| 11 | MCQ | 1 | B |
| 12 | MSQ | 1 | A, B, D |
| 13 | MSQ | 1 | A, B, D |
| 14 | MCQ | 1 | B |
| 15 | MCQ | 1 | B |
| 16 | MCQ | 1 | B |
| 17 | MCQ | 1 | D |
| 18 | NAT | 1 | 2 |
| 19 | NAT | 1 | 16 |
| 20 | NAT | 1 | 3 |
| 21 | NAT | 1 | 4 |
| 22 | MSQ | 1 | A, C |
| 23 | MCQ | 1 | A |
| 24 | MCQ | 1 | D |
| 25 | MSQ | 1 | B, C, D |
| 26 | MCQ | 1 | D |
| 27 | MSQ | 1 | A, B, D |
| 28 | MCQ | 1 | D |
| 29 | NAT | 1 | 0.75 |
| 30 | MCQ | 1 | B |
| 31 | MSQ | 1 | A, C |
| 32 | MCQ | 1 | B |
| 33 | MCQ | 1 | A |
| 34 | MCQ | 1 | A |
| 35 | MCQ | 1 | D |
| 36 | MSQ | 2 | B, D |
| 37 | NAT | 2 | 1 |
| 38 | MCQ | 2 | C |
| 39 | MCQ | 2 | B |
| 40 | MCQ | 2 | C |
| 41 | MCQ | 2 | A |
| 42 | MSQ | 2 | B, C, D |
| 43 | MCQ | 2 | C |
| 44 | MCQ | 2 | D |
| 45 | MCQ | 2 | A |
| 46 | NAT | 2 | 8 |
| 47 | MCQ | 2 | D |
| 48 | MCQ | 2 | A |
| 49 | NAT | 2 | 4 |
| 50 | MCQ | 2 | B |
| 51 | MSQ | 2 | A, C |
| 52 | MCQ | 2 | A |
| 53 | MSQ | 2 | A, C, D |
| 54 | MCQ | 2 | C |
| 55 | MSQ | 2 | A, C, D |
| 56 | MSQ | 2 | A, C |
| 57 | NAT | 2 | 26 |
| 58 | NAT | 2 | 21 |
| 59 | NAT | 2 | 2 |
| 60 | NAT | 2 | 6 |
| 61 | NAT | 2 | 40 (exact) |
| 62 | MCQ | 2 | D |
| 63 | MCQ | 2 | A |
| 64 | MCQ | 2 | B |
| 65 | MSQ | 2 | A, C, D |
