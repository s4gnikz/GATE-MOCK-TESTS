# GATE CS 2027 — Full-Length Mock Test 032

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

Q1–Q5 and Q11–Q35 carry one mark each; Q6–Q10 and Q36–Q65 carry two marks each. The180-minute examination allocates15 marks to General Aptitude,13 to Engineering Mathematics, and72 to core Computer Science.

MCQs have exactly one correct choice. MSQs have multiple correct choices and receive credit only for selecting all and only those choices. An incorrect one-mark MCQ loses1/3 mark; an incorrect two-mark MCQ loses2/3 mark. MSQ and NAT questions have no negative marking. Unattempted questions receive zero; no partial credit applies. NAT answers must follow the stated precision. The answer key follows Question65.

---

## Section A — General Aptitude

### Q1. [1 Mark] [NAT]

Among25 recorded journey times,7 are at most10 minutes,19 are at most20 minutes, and all25 are at most30 minutes. A journey is selected uniformly from those lasting more than10 minutes. What is the probability that it lasted at most20 minutes?

**Answer format:** Decimal rounded to four places.

### Q2. [1 Mark] [MCQ]

A square sheet is folded along both its horizontal and vertical midlines. Small holes are punched through all four layers, with every punch strictly away from the folds and sheet edges. Coordinates are measured from the original square's centre. Which set can be exactly the resulting hole centres after unfolding one punch?

A. {(1,1),(−1,1),(1,−1),(−1,−1)}
B. {(1,1),(−1,1),(1,−1),(−2,−1)}
C. {(1,1),(−1,1)}
D. {(1,1),(−1,−1)}

Assume the sheet is large enough to contain all listed points.

### Q3. [1 Mark] [MCQ]

A narrative says: “The team archived the original readings before recalibrating the instrument. It then repeated the measurements. Only after this repetition did it compare the two sets of readings.” Which event necessarily happened immediately before the comparison among the three later events mentioned?

A. Archiving the original readings
B. Repeating the measurements
C. Recalibrating the instrument
D. Discarding the original readings

### Q4. [1 Mark] [NAT]

A fair six-sided die is rolled. If the first result is odd, it is discarded and the die is rolled once more; otherwise the first result is retained. The second result, if rolled, is always retained. What is the probability that the retained result is6?

**Answer format:** Exact decimal.

### Q5. [1 Mark] [MCQ]

In “The researchers preferred the more parsimonious explanation,” parsimonious most appropriately describes an explanation that:

A. refuses to consider any evidence.
B. accounts for the observations with fewer unnecessary assumptions.
C. contains the greatest number of technical terms.
D. is necessarily true because it is shorter.

### Q6. [2 Marks] [NAT]

For positive real x, suppose log2(x)·log4(x)=8. What is the product of all positive solutions x?

**Answer format:** Exact number.

### Q7. [2 Marks] [MSQ]

For real numbers a,b, define a⋆b=2a+b. Which identities or implications hold for all real a,b,c?

A. (a⋆b)⋆c=a⋆(b⋆c)
B. a⋆b=b⋆a
C. If a⋆b=a⋆c, then b=c.
D. a⋆(b+c)=(a⋆b)+c

### Q8. [2 Marks] [NAT]

Unit cubes are stacked in four columns on a2×2 base. Heights are nonnegative integers. Maximum heights in the first and second rows are3 and1; maximum heights in the first and second columns are2 and3. What is the minimum total number of cubes consistent with these four maxima?

**Answer format:** Integer.

### Q9. [2 Marks] [NAT]

Evaluate the sum from n=1 to8 of1/[n(n+2)].

**Answer format:** Decimal rounded to four places.

### Q10. [2 Marks] [NAT]

A triangle has vertices A=(0,8),B=(−6,0),C=(6,0). Its orthocentre H is the intersection of its altitude lines. What is the y-coordinate of H?

**Answer format:** Exact decimal.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MSQ]

Initially, on-call flags A and B are both 1. Transaction T1 reads B and, if B=1, writes A=0. Transaction T2 reads A and, if A=1, writes B=0. Both read the same initial snapshot. A system rejects concurrent transactions only when they write a common item. Which statements hold?

A. Both transactions can commit under this rule.
B. Every serial execution leaves A=B=0.
C. The committed outcome can violate the invariant A+B≥1.
D. Testing only for overlapping write sets fails to prevent this anomaly.

### Q12. [1 Mark] [MSQ]

A ternary ER relationship Assignment(Employee,Project,Role) records who fills each role on each project. Every (Project,Role) pair has at most one assigned employee. An employee may fill several roles on the same project, and may work on several projects. There are no other key constraints. Which statements hold?

A. (Project,Role) is a candidate key of Assignment.
B. (Employee,Project) is necessarily a candidate key.
C. Two assignments with the same project and role but different employees violate the constraint.
D. Replacing the relationship by Employee–Project alone preserves all assignment information.

### Q13. [1 Mark] [NAT]

An inode has one direct pointer and one pointer to a single-indirect block. Blocks contain 1024 bytes and pointers contain 4 bytes. A previously empty file is extended by writing one byte at byte offset 3072, with offsets starting at zero. The file system supports holes and allocates only necessary data and indirect blocks. Excluding the inode, how many blocks are newly allocated?

**Answer format:** Exact integer.

### Q14. [1 Mark] [MCQ]

A BFS from s runs on an undirected graph with edges sa, sb, ac, ad, be, and ce. Vertices are marked when enqueued. Which discovery order is impossible, regardless of adjacency-list ordering?

A. s,a,b,c,d,e
B. s,b,a,e,c,d
C. s,a,b,c,e,d
D. s,a,b,d,c,e

### Q15. [1 Mark] [NAT]

Two positive-edge-triggered flip-flops have state (A,B) and next-state equations A'=A XOR B and B'=NOT A. Starting at (0,0), how many distinct states occur before the first repeated state?

**Answer format:** Exact integer.

### Q16. [1 Mark] [MCQ]

A DMA device writes a buffer in main memory. The CPU has an old, clean copy of that buffer in a non-coherent write-back cache. The DMA completion interrupt has arrived. Which action is sufficient to make a subsequent CPU read obtain the DMA result, assuming no concurrent writes?

A. Write back the old clean cache line without invalidating it.
B. Invalidate the cached buffer lines before reading.
C. Disable interrupts after the completion interrupt.
D. Read the buffer repeatedly until its value changes.

### Q17. [1 Mark] [MSQ]

A connected, undirected graph has a unique minimum spanning tree T. Every edge weight is replaced by w'(e)=3w(e)+7. Which statements necessarily hold?

A. T remains the unique minimum spanning tree.
B. Every shortest path remains a shortest path.
C. The relative weights of any two spanning trees remain ordered in the same way.
D. The weight of T increases by exactly 7.

### Q18. [1 Mark] [MSQ]

Let L be a context-free language over {a,b}. Define h(a)=01 and h(b)=epsilon. Let R be a regular language over {0,1}. Which languages must be context-free?

A. h(L)
B. h(L) intersect R
C. The complement of L over {a,b}*
D. L intersect {a}*

### Q19. [1 Mark] [MCQ]

A process successfully calls exec to replace its program. Which statement is correct under the usual UNIX process model?

A. Its process identifier changes because a new process is created.
B. All open file descriptors necessarily close.
C. Execution eventually returns to the instruction after the successful exec call.
D. The process keeps its identifier but executes the replacement program.

### Q20. [1 Mark] [NAT]

A full binary tree has 11 leaves: every internal vertex has exactly two children. Delete one leaf and its parent, replacing the parent by its other child's subtree; the selected leaf's parent is not the root. How many vertices remain?

**Answer format:** Exact integer.

### Q21. [1 Mark] [NAT]

A hidden bit H is equally likely to be 0 or 1. Conditional on H, two sensors independently report H with probability 3/4 and report the other bit otherwise. The sensors agree. What is the probability that their common report equals H?

**Answer format:** Exact decimal.

### Q22. [1 Mark] [MCQ]

For L={a^n b^n : n≥0}, choose z=a^p b^p in a pumping-lemma argument, where p≥1. Which statement correctly addresses every decomposition z=uvw with |uv|≤p and |v|≥1?

A. v contains only a's, so removing v produces a string outside L.
B. v contains equal numbers of a's and b's, so repeating v stays in L.
C. Some suitable decomposition must be chosen by the person proving nonregularity.
D. The lemma allows v to be empty if u is nonempty.

### Q23. [1 Mark] [MCQ]

A compiler uses a non-relational constant-propagation analysis: it tracks each variable separately and joins different constants to “not constant.” Both branches below are feasible.

```text
if p then { x=2; y=7; }
else      { x=7; y=2; }
z=x+y;
```

At the assignment to z, which description is correct?

A. The analysis proves x=2 and z=9.
B. The analysis proves y=7 and z=9.
C. The stated analysis cannot prove z constant, although z is always 9.
D. z can equal 4 or 14 during execution.

### Q24. [1 Mark] [NAT]

An 8-bit signed two's-complement fixed-point format has four fractional bits. Two encoded operands represent 1.5 and −0.75. Their full-precision product is rounded back to this format, with no overflow. Interpreting the final 8-bit encoding as an unsigned integer, what is its value?

**Answer format:** Exact integer.

### Q25. [1 Mark] [NAT]

Two Ethernet stations collide and independently choose their backoff values uniformly from {0,1,2,3}. Conditional on their values being different, what is the probability that the smaller value is zero?

**Answer format:** Exact decimal.

### Q26. [1 Mark] [MSQ]

Order the set {1,2,3,6} by divisibility. Which statements hold?

A. Every pair has a greatest lower bound and a least upper bound in this set.
B. 2 and 3 have neither a common upper bound nor a common lower bound.
C. Every element has a complement with respect to bottom 1 and top 6.
D. The order is a total order.

### Q27. [1 Mark] [NAT]

Gaussian elimination without row exchanges factors A=LU, where L has unit diagonal. For

```text
A = [ 2  1  0
      4  3  1
      2  2  3 ]
```

what is the entry U33 after both elimination stages?

**Answer format:** Exact integer.

### Q28. [1 Mark] [MCQ]

A distance-vector router X has links of costs 2 and 5 to neighbors Y and Z. Before processing updates, their advertised distances to D are 4 and 1, respectively. Only Y then advertises distance 9. Using the latest advertisement from each neighbor and no other route to D, what should X advertise?

A. 4
B. 6
C. 11
D. 14

### Q29. [1 Mark] [NAT]

An IPv4 fragment has a 20-byte header, 800 payload bytes, fragment offset 100, and MF=1. It encounters an MTU of 420 bytes and is split into two fragments with equal payloads. What is the fragment offset field of the second new fragment?

**Answer format:** Exact integer.

### Q30. [1 Mark] [MSQ]

Consider the following code. The return is the only program exit and has no implicit use of other variables.

```text
x = 1;
y = x + 2;
x = 4;
return y;
```

Which statements about backward liveness hold?

A. x is live immediately after x=1.
B. The value assigned by x=4 is live immediately after that assignment.
C. y is live immediately before x=4.
D. y is live immediately before y=x+2.

### Q31. [1 Mark] [MSQ]

Input consists of a deterministic Turing machine M, a string w, and a nonnegative integer k in binary. Which tasks are decidable?

A. Determine whether M accepts w within k transitions.
B. Determine whether M ever accepts w, with no time bound.
C. Determine whether M visits more than k distinct tape cells during its first k transitions.
D. Determine whether M halts on every input.

### Q32. [1 Mark] [NAT]

A single-issue, in-order pipeline can issue one instruction per cycle. Without a stall, an instruction immediately after its producer has issue-cycle separation 1. A load's dependent instruction requires separation at least 3; an ALU instruction's dependent instruction requires separation at least 1. Independent instructions have no restrictions. How many idle issue cycles are required for this fixed sequence?

```text
load r1,[a]
add  r2,r1,r3
add  r4,r5,r6
load r7,[b]
add  r8,r7,r2
```

**Answer format:** Exact integer.

### Q33. [1 Mark] [NAT]

Define F(x)=the integral of (2t+1) from t=0 to t=x. What is the integral of xF'(x)−F(x) over x from 0 to 1?

**Answer format:** Decimal rounded to four places.

### Q34. [1 Mark] [MCQ]

A binary search tree contains distinct keys. Delete a node v that has two children by copying its inorder predecessor's key into v and then deleting the predecessor's original node. Which property makes the final deletion simple?

A. The predecessor must be a leaf.
B. The predecessor must have no left child.
C. The predecessor must be v's immediate left child.
D. The predecessor has no right child and therefore has at most one child.

### Q35. [1 Mark] [NAT]

A dataset of four values has mean 5 and population variance 4. Append two more observations, both equal to the old mean. What is the new population variance?

**Answer format:** Decimal rounded to four places.

### Q36. [2 Marks] [NAT]

How many binary strings of length 6 contain exactly two occurrences of the substring 01? Occurrences are counted by their starting positions.

**Answer format:** Exact integer.

### Q37. [2 Marks] [MSQ]

Consider this straight-line fragment. All variables are integers, addresses are valid, and there are no volatile objects or concurrent accesses. Pointer p may refer to a, b, or a distinct variable c. The assignment through p must be retained.

```text
t = a + b;
*p = 0;
u = a + b;
```

Which conditions are each sufficient to replace the last expression a+b by t for every execution satisfying that condition? Assume arithmetic does not overflow.

A. p points to c, which is distinct from a and b.
B. p points to a, and a was zero immediately before the store.
C. p points to b, and a was zero immediately before the store.
D. p points to b, and b was zero immediately before the store.

### Q38. [2 Marks] [NAT]

Use set relational algebra. C(Student)={u,v,w}, R(Student,Course)={(u,x),(u,y),(v,x)}, and Required(Course) is empty. A query is defined as

```text
C − project_Student((C × Required) − R)
```

How many student tuples does the query return, including students with no tuples in R?

**Answer format:** Exact integer.

### Q39. [2 Marks] [MCQ]

A binary max-heap contains distinct keys 1 through 7 in an array indexed 1 through 7. The key 6 is at index 3. Which statement characterizes all possible positions of key 5?

A. It must be at index 2.
B. It can be at any of indices 2,4,5,6,7.
C. It can be at indices 2,6,7, and no others.
D. It can be at index 1 or 2 only.

### Q40. [2 Marks] [NAT]

A hypothetical machine executes ADD (R)+,−(R) with the following precise semantics: fetch the source word at R, increment R by 4, then decrement R by 4, then fetch the destination word at R, add the saved source to it, and write the result to that destination address. Initially R=100, memory word at 100 is 7, and word at 104 is 9. What is the sum of the final values of R and these two memory words?

**Answer format:** Exact integer.

### Q41. [2 Marks] [NAT]

A toy binary floating-point system has precision 3 significant bits, unbounded exponents, and rounding to nearest with ties to even. Every addition is rounded immediately. Let a=8, b=1, c=1. What is the numerical value of (a+(b+c))−((a+b)+c), where the final subtraction is evaluated exactly on the two already rounded results?

**Answer format:** Exact integer.

### Q42. [2 Marks] [MSQ]

An 8-bit ALU performs subtraction x−y as x+(NOT y)+1 and retains only the low eight result bits. C is the carry out of bit 7; V indicates signed two's-complement overflow. For x=0x80 and y=0x01, which statements hold?

A. The retained result is 0x7F.
B. C=0, indicating an unsigned borrow.
C. V=1.
D. The signed mathematical result is representable in eight bits.

### Q43. [2 Marks] [NAT]

An undirected multigraph has vertices a,b,c, two parallel edges between a and b, one edge between b and c, and one self-loop at a. An incidence matrix has one column per edge; a non-loop contributes 1 to each endpoint, and a loop contributes 2 to its vertex. An adjacency-list representation stores two entries for every undirected edge, including a loop. What is the sum of the degree of a and the total number of adjacency-list entries?

**Answer format:** Exact integer.

### Q44. [2 Marks] [MSQ]

For Boolean inputs x,y,z, a circuit outputs F=(x AND y) OR ((NOT x) AND z). Which statements hold?

A. Flipping x leaves F unchanged exactly when y=z.
B. F equals (x OR z) AND ((NOT x) OR y).
C. F is independent of z whenever y=1.
D. When y=NOT z, F XOR z equals x.

### Q45. [2 Marks] [NAT]

For the grammar S→SS | a, how many distinct parse trees generate a string of five a's? Count trees, not different orders of expanding independent nodes.

**Answer format:** Exact integer.

### Q46. [2 Marks] [MCQ]

A process initially has three threads. One thread calls fork under POSIX semantics, and the child does not call exec. No further threads are created. Which statement is correct immediately after fork?

A. Parent and child each have three threads.
B. The parent has three threads, and the child has one thread.
C. The parent has one thread, and the child has three threads.
D. Both processes have one thread.

### Q47. [2 Marks] [NAT]

Let G be the multiplicative group of nonzero residues modulo 17. How many elements x in G satisfy x^4=1 but x²≠1? You may use that G is cyclic.

**Answer format:** Exact integer.

### Q48. [2 Marks] [NAT]

A four-variable Boolean function F(A,B,C,D) is 1 on minterms {0,1,2,3,8,9,10,11,12,13,14,15} and 0 elsewhere. A is the most significant minterm bit. A two-level sum-of-products implementation must cover all 1-minterms and no 0-minterms. What is the minimum total number of literals in a valid SOP?

**Answer format:** Exact integer.

### Q49. [2 Marks] [MSQ]

A deterministic PDA has a designated set of final states. Acceptance by final state requires all input to be consumed, and the stack may remain nonempty. Which assertions are valid?

A. Every language accepted by such a machine is context-free.
B. Every context-free language can be accepted by some deterministic PDA.
C. A nondeterministic PDA can accept the same language using empty-stack acceptance instead.
D. Simply declaring all states final always preserves the accepted language.

### Q50. [2 Marks] [NAT]

A pipe initially contains no bytes and has two open write descriptors referring to its write end, one in P and one in Q. P writes 5 bytes and closes its descriptor. Reader R requests 10 bytes and receives the available 5. R then performs another blocking read while Q still holds its descriptor but never writes. Later Q closes that descriptor. How many bytes does R's second read return upon completion? Assume no signals or errors.

**Answer format:** Exact integer.

### Q51. [2 Marks] [MSQ]

Relations R(x) and S(x) are finite subsets of an infinite domain D. In the following tuple-calculus formulas, x is the only free variable and quantifiers range over D. Which formulas necessarily define finite result sets for every finite R,S?

A. R(x) AND NOT S(x)
B. NOT R(x) AND NOT S(x)
C. EXISTS y (R(y) AND x=y)
D. FOR ALL y (S(y) IMPLIES x=y)

### Q52. [2 Marks] [NAT]

A lexer uses maximal munch. Its tokens are ID=[a-z]+, EQ='=', and EQEQ='=='. Keyword 'if' takes precedence over ID only when both match the same longest lexeme. Whitespace is ignored. How many tokens result from this input?

```text
ifif===if = iff
```

**Answer format:** Exact integer.

### Q53. [2 Marks] [NAT]

A directed graph has edges s→a of weight 3, s→b of weight 8, a→b of weight −4, b→c of weight 2, and a→c of weight 7. Reweight each edge by w'(u,v)=w(u,v)+h(u)−h(v), with h(s)=0, h(a)=0, h(b)=−4, h(c)=−2. What is the shortest-path distance from s to c in the reweighted graph?

**Answer format:** Exact integer.

### Q54. [2 Marks] [NAT]

A routing table contains only the following entries, plus a default route. For destinations in 10.0.0.0/24, how many addresses select interface A under longest-prefix matching?

```text
10.0.0.0/24     A
10.0.0.64/26    B
10.0.0.96/27    A
10.0.0.112/28   C
```

Count all addresses, without excluding network or broadcast addresses.

**Answer format:** Exact integer.

### Q55. [2 Marks] [MCQ]

A NAT maps internal TCP endpoint 192.168.1.8:5000 to public endpoint 203.0.113.2:42000 for a connection to 198.51.100.9:443. It translates an outgoing IPv4 packet with no options and no fragmentation. Which checksum fields must be updated because of these substitutions?

A. Only the IPv4 header checksum.
B. Only the TCP checksum.
C. Neither checksum, because payload bytes are unchanged.
D. Both the IPv4 header checksum and the TCP checksum.

### Q56. [2 Marks] [NAT]

A stable sorting procedure performs two passes on records (key1,key2,id): first ascending by key2, then ascending by key1. Initially the records are

```text
(2,1,A), (1,2,B), (2,1,C), (1,1,D), (2,0,E)
```

Number final positions from 1. What is the sum of the final positions of records A and C?

**Answer format:** Exact integer.

### Q57. [2 Marks] [MSQ]

A reusable barrier for two threads uses shared integer count, initially 0, and shared Boolean sense, initially false. Each thread has its own local Boolean mySense, initially false. The following operations execute under sequential consistency; increment-and-test is atomic.

```text
mySense = NOT mySense;
if atomic_increment(count) == 2 {
    count = 0;
    sense = mySense;
} else {
    while sense != mySense { }
}
```

Only these two threads use the barrier, and each calls it sequentially once per phase. Which statements hold?

A. The sense change releases the waiting thread for the current phase.
B. The last arriving thread must reset count before publishing the changed sense.
C. A fast thread may complete the next barrier without the other thread reaching it.
D. Separate local mySense values distinguish consecutive barrier phases.

### Q58. [2 Marks] [NAT]

A TCP sender has 3000 bytes outstanding. Its congestion window is 5000 bytes, and its receiver-advertised window is 4000 bytes. An ACK newly acknowledges 1000 bytes and advertises a new receiver window of 2500 bytes. The congestion window remains 5000. No other data is sent or acknowledged during this event. How many additional bytes may the sender transmit immediately?

**Answer format:** Exact integer.

### Q59. [2 Marks] [NAT]

Assume all array accesses in this C program are valid and int can represent all values shown. What value is returned?

```c
int f(void) {
    int a[4] = {3, 5, 7, 9};
    int *p = a + 1;
    int **q = &p;
    (*q)++;
    **q += a[0];
    return p[-1] + a[2] + (int)(p - a);
}
```

**Answer format:** Exact integer.

### Q60. [2 Marks] [NAT]

A simple graph consists of two vertex-disjoint triangles, with one additional edge joining one vertex of the first triangle to one vertex of the second. How many proper colorings using three labeled colors does the graph have?

**Answer format:** Exact integer.

### Q61. [2 Marks] [NAT]

Six distinct books are arranged on a shelf. Books A and B must have exactly one book between them, and books C and D must be adjacent. How many arrangements satisfy both conditions?

**Answer format:** Exact integer.

### Q62. [2 Marks] [NAT]

SQL uses bag semantics and ordinary three-valued logic. T(k) has rows 1,1,NULL and U(k) has rows 1,NULL. How many rows does this query return?

```sql
SELECT T.k, U.k
FROM T LEFT JOIN U ON T.k = U.k
WHERE U.k IS NULL;
```

**Answer format:** Exact integer.

### Q63. [2 Marks] [NAT]

A microprogram executes one microinstruction per clock, with no other stalls. Register changes and the branch decision stated in a row both occur in that clock. Branches test the new register value. Execution begins at address 0.

| Address | Operation and next address |
|---|---|
| 0 | R=3; go to 1 |
| 1 | S=R; go to 2 |
| 2 | S=S−1; if S≠0 go to 2, otherwise go to 3 |
| 3 | R=R−1; if R≠0 go to 1, otherwise go to 4 |
| 4 | Halt |

How many clocks elapse, including execution of the halt microinstruction?

**Answer format:** Exact integer.

### Q64. [2 Marks] [NAT]

Let en count ordered compositions of n into parts 1 and 3 with an even number of parts equal to 3; the empty composition contributes e0=1. Odd numbers of 3-parts are excluded. What is the coefficient of x10 in E(x)=Σ(n≥0) en x^n?

**Answer format:** Exact integer.

### Q65. [2 Marks] [MSQ]

Consider the grammar

```text
S → a A | a B
A → b
B → c
```

The start symbol is S and the terminals are a,b,c. Which statements hold?

A. The grammar as written has an LL(1) conflict in S's row.
B. The language cannot be generated by any LL(1) grammar.
C. Left factoring S into S→aX, X→b|c yields an LL(1) grammar for the same language.
D. The grammar is ambiguous because both S productions begin with a.


---

## ANSWER KEY — MOCK TEST 032

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | NAT | 1 | 0.6667 (accepted range 0.66665–0.66675) |
| 2 | MCQ | 1 | A |
| 3 | MCQ | 1 | B |
| 4 | NAT | 1 | 0.25 |
| 5 | MCQ | 1 | B |
| 6 | NAT | 2 | 1 |
| 7 | MSQ | 2 | C, D |
| 8 | NAT | 2 | 6 |
| 9 | NAT | 2 | 0.6444 (accepted range 0.64435–0.64445) |
| 10 | NAT | 2 | 4.5 |
| 11 | MSQ | 1 | A, C, D |
| 12 | MSQ | 1 | A, C |
| 13 | NAT | 1 | 2 |
| 14 | MCQ | 1 | C |
| 15 | NAT | 1 | 3 |
| 16 | MCQ | 1 | B |
| 17 | MSQ | 1 | A, C |
| 18 | MSQ | 1 | A, B, D |
| 19 | MCQ | 1 | D |
| 20 | NAT | 1 | 19 |
| 21 | NAT | 1 | 0.9 |
| 22 | MCQ | 1 | A |
| 23 | MCQ | 1 | C |
| 24 | NAT | 1 | 238 |
| 25 | NAT | 1 | 0.5 |
| 26 | MSQ | 1 | A, C |
| 27 | NAT | 1 | 2 |
| 28 | MCQ | 1 | B |
| 29 | NAT | 1 | 150 |
| 30 | MSQ | 1 | A, C |
| 31 | MSQ | 1 | A, C |
| 32 | NAT | 1 | 4 |
| 33 | NAT | 1 | 0.3333 (accepted range 0.33325–0.33335) |
| 34 | MCQ | 1 | D |
| 35 | NAT | 1 | 2.6667 (accepted range 2.66665–2.66675) |
| 36 | NAT | 2 | 21 |
| 37 | MSQ | 2 | A, B, D |
| 38 | NAT | 2 | 3 |
| 39 | MCQ | 2 | C |
| 40 | NAT | 2 | 123 |
| 41 | NAT | 2 | 2 |
| 42 | MSQ | 2 | A, C |
| 43 | NAT | 2 | 12 |
| 44 | MSQ | 2 | A, B, D |
| 45 | NAT | 2 | 14 |
| 46 | MCQ | 2 | B |
| 47 | NAT | 2 | 2 |
| 48 | NAT | 2 | 2 |
| 49 | MSQ | 2 | A, C |
| 50 | NAT | 2 | 0 |
| 51 | MSQ | 2 | A, C |
| 52 | NAT | 2 | 6 |
| 53 | NAT | 2 | 3 |
| 54 | NAT | 2 | 208 |
| 55 | MCQ | 2 | D |
| 56 | NAT | 2 | 9 |
| 57 | MSQ | 2 | A, B, D |
| 58 | NAT | 2 | 500 |
| 59 | NAT | 2 | 17 |
| 60 | NAT | 2 | 24 |
| 61 | NAT | 2 | 48 |
| 62 | NAT | 2 | 1 |
| 63 | NAT | 2 | 14 |
| 64 | NAT | 2 | 16 |
| 65 | MSQ | 2 | A, C |
