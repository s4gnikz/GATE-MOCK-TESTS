# GATE CS 2027 — Full-Length Mock Test 044

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

### Q1. [1 Mark] [NAT]

A sequence begins with a1=1,a2=2 and obeys a(n)=a(n−1)+2a(n−2) for n≥3. Find a6.

**Answer format:** Integer.

### Q2. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A planar shape consists of the four points (1,0),(0,1),(−1,0),(0,−1), with the first point coloured red and the other three blue. A rotation is a symmetry only if it maps the coloured point set to itself, preserving colours. How many rotations about the origin through angles in [0,360) degrees are symmetries?

**Required precision:** Integer.

A. 2  
B. 0  
C. 3  
D. 1

### Q3. [1 Mark] [MCQ]

Which sentence states that every report was read by at least one reviewer, without asserting that a single reviewer read all reports?

A. One reviewer read every report.
B. Every report was read by some reviewer.
C. Every reviewer read every report.
D. No reviewer read a report.

### Q4. [1 Mark] [NAT]

A price is first increased by p percent and then reduced by p percent, where 0<p<100. The final price is 96% of the original. What is p?

**Answer format:** Exact integer.

### Q5. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Exactly two of A, B, C and D must be on duty. If A is on duty, B must be on duty. In addition, C is on duty if and only if D is not on duty. How many different pairs can be on duty?

A. 4  
B. 2  
C. 1  
D. 3

### Q6. [2 Marks] [MCQ]

Solid stacks of unit cubes stand in a 2-by-3 grid. Each stack has a nonnegative integer height and has no gaps. Looking along the two-row direction, the maximum heights in the three columns are 2,3,1 respectively. Looking along the three-column direction, the maximum heights in the two rows are 3,2 respectively. What pair gives the minimum and maximum possible total number of cubes?

A. (7,11)  
B. (6,11)  
C. (6,12)  
D. (8,12)

### Q7. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A report states: “The mean travel time was unchanged after the timetable revision, although individual passengers experienced both increases and decreases.” Which conclusion is supported?

A. Every passenger's travel time stayed unchanged.  
B. Equal means imply identical travel-time distributions.  
C. An unchanged aggregate measure can coexist with changes in individual outcomes.  
D. The timetable revision necessarily improved every passenger's journey.

### Q8. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Six distinct books consist of three mathematics books and three literature books. They are arranged on a shelf so that the mathematics books occur in alphabetical order relative to one another, and no two literature books are adjacent. The literature books have no relative-order restriction. How many arrangements are possible?

**Required precision:** Integer.

A. 48  
B. 12  
C. 25  
D. 24

### Q9. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Of 100 students, 80 study subject A, 75 study B, and 70 study C. What is the smallest possible number who study all three subjects?

**Required precision:** Integer.

A. 50  
B. 13  
C. 25  
D. 26

### Q10. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A rectangular sheet spans0≤x≤8 and0≤y≤2. Fold the left half onto the right along x=4. Then fold the part of that packet with6≤x≤8 onto4≤x≤6 along x=6. Cut straight through all layers along x=5 for the full height of the folded packet. After unfolding and separating along the cuts, how many connected pieces remain? Creases alone do not separate pieces.

**Required precision:** Integer.

A. 5  
B. 10  
C. 3  
D. 6

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A combinational block receives two bits a,b and must output 1 exactly when the two-bit unsigned value is prime. Which output function is correct?

A. a  
B. b  
C. a XOR b  
D. a AND b

### Q12. [1 Mark] [NAT]

In an ER model, each employee belongs to exactly one department, and each department may have any number of employees. There are12 employees and four departments. How many employee-department relationship instances exist?

**Answer format:** Integer.

### Q13. [1 Mark] [NAT]

Weighted intervals are [0,4) with weight 9, [0,2) with weight 4 and [2,4) with weight 4. Nonoverlapping intervals may share an endpoint. An algorithm repeatedly selects the available interval with earliest finish time, then removes conflicting intervals. By how much is its total weight below the optimum?

**Answer format:** Integer.

### Q14. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

In a pumping-lemma argument for L={a^n b^m : n,m≥0 and n≠m}, consider z=a³b⁹ and every decomposition z=uvw satisfying |uv|≤3 and |v|≥1. For each decomposition, choose an integer i≥0 such that uv^i w has equally many a's and b's. What is the largest i required among these decompositions?

**Required precision:** Exact integer.

A. 7  
B. 14  
C. 4  
D. 8

### Q15. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Two threads in the same ordinary process have different stack pointers but access the same heap object without synchronization. Which statement is correct?

A. Distinct stacks imply their heap writes cannot race.  
B. Shared address-space access permits a data race despite separate stacks.  
C. Sharing the heap requires the threads to share the same stack pointer.  
D. Each thread automatically receives a private copy of every heap allocation.

### Q16. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An undirected connected graph has distinct edge weights except that two edges share a weight. Which assertion is necessarily true?

A. It has at least two minimum spanning trees.  
B. Every maximum-weight edge is absent from every minimum spanning tree.  
C. Any edge that is uniquely lightest across some cut belongs to every minimum spanning tree.  
D. Kruskal's algorithm fails unless all weights are distinct.

### Q17. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A machine enumerates all binary strings and runs an effective test that halts and accepts exactly on strings belonging to a decidable language L. It prints the accepted strings, one at a time. If L is finite, which statement follows?

A. The enumeration must automatically know when its last output has been printed.  
B. Enumeration can continue forever after its last output without contradicting correctness.  
C. L becomes undecidable because enumeration is infinite.  
D. The empty language cannot be enumerated.

### Q18. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Under set semantics, R(A,B)={(1,2),(1,3),(2,3)}. How many tuples does π_A(R)×π_B(R) contain?

**Required precision:** Integer.

A. 4  
B. 8  
C. 2  
D. 5

### Q19. [1 Mark] [NAT]

X takes values 0 and 1, and Y=1−X. If E[X+2Y]=1.7, what is Var(X+2Y)?

**Answer format:** Decimal rounded to two places.

### Q20. [1 Mark] [NAT]

A singly linked list has a noncyclic prefix of three nodes followed by a cycle of four nodes. A slow pointer and a fast pointer both start at the head. In each iteration slow advances one link and fast advances two. Equality is tested only after these advances. After how many iterations do they first point to the same node?

**Answer format:** Integer.

### Q21. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Assume unsigned char has exactly eight bits. What is the behaviour of this C loop?

```c
unsigned char i = 250;
while (i < 255) {
    i = i + 2;
}
```

A. It terminates with i=255.  
B. It never terminates.  
C. It terminates with i=0.  
D. The addition necessarily causes undefined signed overflow.

### Q22. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let R be a finite unary relation over an infinite domain. A tuple-calculus query asks for all x satisfying NOT R(x), with no further restriction on x. Which statement is correct?

A. The result is always finite because R is finite.  
B. The result can be infinite and depends on values outside the active domain.  
C. Negation is forbidden in every safe tuple-calculus query.  
D. The result always equals R.

### Q23. [1 Mark] [NAT]

A stack-machine translation evaluates postfix expression a b + c d − * using PUSH for operands and binary operators that pop two values and push one result. What is the maximum operand-stack depth, starting empty?

**Answer format:** Exact integer.

### Q24. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A relation on a four-element set is symmetric and transitive but not reflexive. What is the maximum possible number of ordered pairs in the relation?

**Required precision:** Integer.

A. 9  
B. 18  
C. 5  
D. 10

### Q25. [1 Mark] [MSQ]

For exact integer arithmetic with no side effects, which local replacements preserve a variable x's value for all x?

A. x+0 → x
B. x*1 → x
C. x*0 → x
D. x−x → 0

### Q26. [1 Mark] [MSQ]

For a binary tree, preorder and inorder traversals are both A,B,C,D with distinct labels. Which statements are correct?

A. The root is A.
B. Every node except D has only a right child.
C. Every node except D has only a left child.
D. The postorder is D,C,B,A.

### Q27. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A real 2×2 matrix A has distinct eigenvalues 2 and −1. Which statements must hold?

**Candidates**

**I.** A²−A−2I=0.

**II.** A is singular.

**III.** A is diagonalizable over the real numbers.

**IV.** A must be symmetric.

A. I and III  
B. II and III  
C. II and IV  
D. III and IV

### Q28. [1 Mark] [MSQ]

A producer sends messages through an operating-system queue and a consumer receives them. Which statements distinguish message passing from directly accessing an ordinary shared variable?

A. Communication uses send/receive operations on messages.
B. A messaging interface can transfer data between distinct address spaces.
C. Message passing necessarily makes every application free of race conditions.
D. All message passing must use busy waiting.

### Q29. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A full binary tree has 11 leaves: every internal vertex has exactly two children. Delete one leaf and its parent, replacing the parent by its other child's subtree; the selected leaf's parent is not the root. How many vertices remain?

**Required precision:** Exact integer.

A. 19  
B. 38  
C. 10  
D. 20

### Q30. [1 Mark] [MSQ]

A browser already knows a server's IP address and establishes a new TCP connection to request an HTTP resource. The server responds with a redirection to a different hostname. Which statements hold?

A. The initial request need not perform a new DNS query if its address is already usable.
B. The redirect guarantees that the original server's IP address is valid for the new hostname.
C. Following the redirect may require resolving the new hostname.
D. An HTTP redirect changes the destination address of the already transmitted request.

### Q31. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A function f is continuous on [0,2], differentiable on (0,2), and satisfies f(0)=f(2)=1. Which conclusions must hold?

**Candidates**

**I.** Some c∈(0,2) satisfies f′(c)=0.

**II.** f is constant on [0,2].

**III.** f attains both a maximum and a minimum on [0,2].

**IV.** f′(1)=0 necessarily.

A. III and IV  
B. I and II  
C. I and III  
D. I and IV

### Q32. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A direct-mapped cache has four lines, one word per line, with block number b mapped to line b modulo4. Initially empty, it receives word-block references0,1,4,1,0,1. How many hits occur?

**Required precision:** Integer.

A. 4  
B. 2  
C. 1  
D. 3

### Q33. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A fair coin and a double-headed coin are selected with equal probability. The selected coin is tossed twice and both outcomes are heads. What is the probability that a third toss of the same coin is heads?

**Required precision:** Exact finite decimal.

A. 0.1  
B. 0.5  
C. 1.0  
D. 0.9

### Q34. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

One application message of 1000 bytes is carried in one TCP segment with a 20-byte TCP header, one IPv4 packet with a 20-byte IP header, and one Ethernet frame with a 14-byte header and four-byte FCS. There are no other headers, padding or fragmentation. Excluding preamble and inter-frame gap, how many bytes are transmitted in the frame?

**Required precision:** Integer.

A. 2116  
B. 1058  
C. 529  
D. 1059

### Q35. [1 Mark] [NAT]

A synchronous three-bit state register is interpreted as an unsigned integer q. At every clock edge, q becomes0 if q≥5, and otherwise becomes q+1. Starting with q=7 before the first edge, what is q after14 edges?

**Answer format:** Integer.

### Q36. [2 Marks] [MSQ]

A one-slot producer–consumer buffer uses semaphores empty=1 and full=0. The producer incorrectly performs wait(empty), signal(full), then writes the item. The consumer performs wait(full), reads the item, signal(empty). Assume semaphore operations are atomic and scheduling may switch between any two operations. Which statements are correct?

A. The consumer can read before the producer writes the new item.
B. Atomic semaphore operations alone eliminate this ordering error.
C. Moving the producer's signal(full) after the write repairs this particular publication error.
D. The consumer's wait(full) forces all future producer writes to occur before its read.

### Q37. [2 Marks] [NAT]

SQL table T(g,v) contains(A,2),(A,NULL),(B,NULL),(B,NULL),(C,5). How many rows are returned by the following query?

```sql
SELECT g
FROM T
GROUP BY g
HAVING COUNT(*) > COUNT(v) AND SUM(v) > 1;
```

**Answer format:** Exact integer.

### Q38. [2 Marks] [NAT]

Insert the distinct keys8,4,12,2,6,10,14,5,7 into an initially empty binary search tree, without balancing. Delete key8 by copying its inorder predecessor into its node and then deleting the predecessor's original node. What is the sum of the keys compared with the target during a successful ordinary BST search for5 in the resulting tree, including5 itself?

**Answer format:** Integer.

### Q39. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Exact integer variable x starts at zero. A loop executes `x=1-x` an arbitrary finite number of times, possibly zero. After the loop, y=x*(x−1) is evaluated. Which statements are true?

**Candidates**

**I.** x is necessarily zero after the loop.

**II.** x is always either zero or one after the loop.

**III.** y is always zero and may be replaced by that constant.

**IV.** y can equal one if the iteration count is odd.

A. II and III  
B. III and IV  
C. I and II  
D. I and III

### Q40. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Over {0,1}, a language contains exactly strings whose third symbol from the right is 1. Strings shorter than three symbols are rejected. How many states are required by a minimal complete DFA?

**Required precision:** Integer.

A. 8  
B. 16  
C. 4  
D. 9

### Q41. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A nonnegative fixed-point value x=11/16 is first rounded to two fractional binary bits, then rounded again to one fractional binary bit. Each rounding uses nearest, ties to even, with enough integer bits. Compare this with rounding x directly to one fractional binary bit. What is the two-stage result minus the direct result?

**Required precision:** Exact decimal.

A. 0.3  
B. 0.5  
C. 0.8  
D. 0.1

### Q42. [2 Marks] [MSQ]

Two processes share a bounded queue initially empty, a mutex M initially 1, a counting semaphore E initially equal to the positive capacity, and a counting semaphore F initially 0. A proposed consumer performs `wait(M); wait(F); remove; signal(E); signal(M)`. A producer performs `wait(E); wait(M); insert; signal(M); signal(F)`. Semaphore operations are atomic. Which statements are correct?

A. If the consumer acquires M first, the system can deadlock.
B. Moving the consumer's wait(F) before wait(M) removes this specific empty-buffer deadlock.
C. Increasing the initial value of E while keeping F=0 always prevents the deadlock.
D. The proposed consumer may hold M while waiting for an item that the producer needs M to insert.

### Q43. [2 Marks] [NAT]

A divide-and-conquer procedure on an array of length8 splits each nonsingleton interval into equal halves and recurses on both. At each internal node it merges the halves into a new buffer, writing every element exactly once; singleton leaves perform no writes. How many element writes occur across all merge buffers?

**Answer format:** Integer.

### Q44. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A synchronous two-flip-flop machine starts at (q1,q0)=(0,1). On input 0 its next state is (0,1). On input 1 its next state is (q1 XOR q0, q1). After processing exactly five input bits, it accepts if its state is (0,1). How many of the 32 input strings are accepted?

A. 16  
B. 17  
C. 18  
D. 20

### Q45. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Consider this loop with scalar variables and no aliases:

```text
L: if p goto B else E
B: x = x + y
   y = 0
   goto L
E: return x
```

The value of p does not change in this code, but liveness analysis conservatively treats both outgoing edges of L as feasible each time. Which variables are live at entry to L at the least fixed point?

A. x  
B. y  
C. p  
D. A separate variable z that is never used or assigned here.

### Q46. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A BFS starts at s in an undirected graph with edges sa,sb,ac,ad,bd,be. Vertices are marked when first enqueued; neighbours may be scanned in any order. Count distinct full discovery orders, including s. How many are possible? Different adjacency scans producing the same discovery order count only once.

**Required precision:** Integer.

A. 8  
B. 2  
C. 5  
D. 4

### Q47. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A table has two rows with distinct primary keys1 and2 and a UNIQUE non-null code column initially containing A and B respectively. A transaction first updates row1's code to B and then row2's code to A. No other transaction runs. Which statement correctly distinguishes immediate checking from checking the UNIQUE constraint only at transaction commit?

A. Both modes must accept because the final state is unique.  
B. Immediate checking rejects the first update; commit-only checking can accept the final swapped state.  
C. Commit-only checking must reject because any intermediate duplicate is forbidden in that mode.  
D. Both modes necessarily change the primary keys.

### Q48. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Consider S→aSbS | bSaS | ε. Which statements are true?

A. Every generated word has equally many a and b symbols.  
B. The word abab has more than one parse tree.  
C. Every prefix of every generated word has at least as many a as b symbols.  
D. The generated language is regular.

### Q49. [2 Marks] [NAT]

For R(A,B,C), dependencies are A→B and B→C. How many of the seven nonempty subsets of{A,B,C} are superkeys?

**Answer format:** Integer.

### Q50. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A PDA for even-length palindromes over{a,b} pushes symbols in phase1, nondeterministically guesses the midpoint using an epsilon move, then matches and pops in phase2. Acceptance requires exhausting input and returning to the bottom marker. Which statements are correct?

**Candidates**

**I.** A successful branch guesses a midpoint after exactly half the input.

**II.** Every midpoint guess must succeed for a palindrome to be accepted.

**III.** Guessing at the beginning accepts every nonempty input.

**IV.** The empty word can be accepted by guessing immediately.

A. I and IV  
B. I and III  
C. II and III  
D. II and IV

### Q51. [2 Marks] [NAT]

A binary floating-point format has three significant bits including the leading one, minimum normal exponent −2, gradual underflow and round-to-nearest ties-to-even. Compute 0.25×0.25, round to the format, then multiply that stored result by 0.5 and round again. What is the absolute relative error of the final stored result compared with the exact real product 0.25×0.25×0.5?

**Answer format:** Exact finite decimal.

### Q52. [2 Marks] [NAT]

For four Boolean inputs a,b,c,d, let F=(a XOR b) AND (b XOR c) AND (c XOR d). How many input assignments make F=1?

**Answer format:** Integer.

### Q53. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Order the divisors of 30 by divisibility. How many maximal chains run from 1 to 30? A chain is maximal when no further divisor can be inserted between successive elements.

**Required precision:** Exact integer.

A. 12  
B. 6  
C. 3  
D. 7

### Q54. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

An eight-bit one's-complement checksum adds bytes 0xFE and 0x02 using end-around carry, then complements the resulting eight bits. What unsigned integer is the checksum?

**Required precision:** Integer.

A. 508  
B. 127  
C. 254  
D. 255

### Q55. [2 Marks] [NAT]

A CPU would execute1000 instructions at a CPI of2. A DMA controller transfers100 words, stealing one CPU cycle per word; each stolen cycle stalls the CPU by exactly one cycle, and there are no other effects. An alternative programmed-I/O method adds four CPU cycles per word and uses no DMA stalls. How many CPU clock cycles does DMA save over programmed I/O for the same computation and transfer?

**Answer format:** Integer.

### Q56. [2 Marks] [MSQ]

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

### Q57. [2 Marks] [NAT]

A scalar pipeline can issue one instruction per cycle. A multiply produces its result three cycles after its issue; an add produces its result one cycle after issue. A consumer may issue in the cycle its last operand becomes available. Consider independent multiplies M1,M2 followed by add A consuming both, then add B consuming A. Issue M1 at cycle0 and schedule as early as possible, without other hazards. In what cycle does B's result become available?

**Answer format:** Integer cycle number.

### Q58. [2 Marks] [NAT]

Let A have rows (2,1,1), (4,3,3), (8,7,9). Solve Ax=b for b=(4,10,30)ᵀ using exact arithmetic. What is the second component of x?

**Answer format:** Integer, possibly negative.

### Q59. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An undirected weighted graph has a cycle whose edge weights are 1,2,2,5. Other edges may exist. Which statements necessarily hold?

**Candidates**

**I.** The weight-5 edge on this cycle belongs to no minimum spanning tree of a connected graph containing it.

**II.** Every weight-2 edge on the cycle belongs to no minimum spanning tree.

**III.** Removing that weight-5 edge preserves connectivity of its original connected component.

**IV.** The minimum spanning tree is necessarily unique.

A. I and II  
B. I and IV  
C. I and III  
D. II and III

### Q60. [2 Marks] [NAT]

A processor uses 16-bit instructions and has 16 registers. Each register operand occupies four bits. In a two-register instruction, the first eight bits form the opcode. In a one-register instruction, the first twelve bits form the opcode. A zero-register instruction uses all sixteen bits as its opcode. Decoding must be unambiguous: no complete opcode may be a prefix of another complete opcode. Exactly 200 two-register opcodes and 800 one-register opcodes are allocated. What is the maximum number of distinct zero-register instructions that can also be allocated?

**Answer format:** Numeric value; integer.

### Q61. [2 Marks] [NAT]

A directed graph with four vertices has adjacency matrix A, where A[i,j] is the number of directed edges i→j. Its only edges are1→2,1→3,2→4,3→4,4→1, one of each. What is entry(1,1) of A³?

**Answer format:** Integer.

### Q62. [2 Marks] [NAT]

Evaluate ∫₀¹ max(x²,1−x) dx, rounded to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q63. [2 Marks] [NAT]

An undirected graph has edges AB of weight x, BC of weight2, AC of weight5, AD of weight1, and CD of weight4. For how many integer choices x in {0,1,2,3,4,5,6} does the graph have more than one minimum spanning tree?

**Answer format:** Integer.

### Q64. [2 Marks] [NAT]

Five observations have sum 20 and sum of squares 90. One observation equal to 6 is removed. What is the population variance of the remaining four observations, using divisor four?

**Answer format:** Exact finite decimal.

### Q65. [2 Marks] [NAT]

An idealized half-duplex CSMA/CD link connects two stations 2400 m apart. Propagation speed is 2×10^8 m/s and the bit rate is 100 Mb/s, where 1 Mb/s = 10^6 bits/s. Detection circuitry adds 2 microseconds after the collision disturbance reaches a transmitting station. Ignore all other delays and framing overhead. A sender must still be transmitting when a worst-case collision is detected. Under the model, what is the minimum integer frame length in bytes? Treat the worst-case round-trip propagation bound as inclusive.

**Answer format:** Numeric value; integer.

---

## ANSWER KEY — MOCK TEST 044

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | NAT | 1 | 32 |
| 2 | MCQ | 1 | D |
| 3 | MCQ | 1 | B |
| 4 | NAT | 1 | 20 |
| 5 | MCQ | 1 | B |
| 6 | MCQ | 2 | B |
| 7 | MSQ | 2 | A, B, D |
| 8 | MCQ | 2 | D |
| 9 | MCQ | 2 | C |
| 10 | MCQ | 2 | A |
| 11 | MSQ | 1 | B, C, D |
| 12 | NAT | 1 | 12 |
| 13 | NAT | 1 | 1 |
| 14 | MCQ | 1 | A |
| 15 | MSQ | 1 | A, C, D |
| 16 | MSQ | 1 | A, B, D |
| 17 | MSQ | 1 | A, C, D |
| 18 | MCQ | 1 | A |
| 19 | NAT | 1 | 0.21 (two decimals) |
| 20 | NAT | 1 | 4 |
| 21 | MSQ | 1 | A, C, D |
| 22 | MSQ | 1 | A, C, D |
| 23 | NAT | 1 | 3 |
| 24 | MCQ | 1 | A |
| 25 | MSQ | 1 | A, B, D |
| 26 | MSQ | 1 | A, B, D |
| 27 | MCQ | 1 | A |
| 28 | MSQ | 1 | A, B |
| 29 | MCQ | 1 | A |
| 30 | MSQ | 1 | A, C |
| 31 | MCQ | 1 | C |
| 32 | MCQ | 1 | B |
| 33 | MCQ | 1 | D |
| 34 | MCQ | 1 | B |
| 35 | NAT | 1 | 1 |
| 36 | MSQ | 2 | A, C |
| 37 | NAT | 2 | 1 |
| 38 | NAT | 2 | 22 |
| 39 | MCQ | 2 | A |
| 40 | MCQ | 2 | A |
| 41 | MCQ | 2 | B |
| 42 | MSQ | 2 | A, B, D |
| 43 | NAT | 2 | 24 |
| 44 | MSQ | 2 | A, B, D |
| 45 | MCQ | 2 | D |
| 46 | MCQ | 2 | D |
| 47 | MSQ | 2 | A, C, D |
| 48 | MSQ | 2 | C, D |
| 49 | NAT | 2 | 4 |
| 50 | MCQ | 2 | A |
| 51 | NAT | 2 | 1 |
| 52 | NAT | 2 | 2 |
| 53 | MCQ | 2 | B |
| 54 | MCQ | 2 | C |
| 55 | NAT | 2 | 300 |
| 56 | MSQ | 2 | A, B, D |
| 57 | NAT | 2 | 6 |
| 58 | NAT | 2 | -2 (exact) |
| 59 | MCQ | 2 | C |
| 60 | NAT | 2 | 1536 (exact) |
| 61 | NAT | 2 | 2 |
| 62 | NAT | 2 | 0.6817 (range 0.68165–0.68175) |
| 63 | NAT | 2 | 1 |
| 64 | NAT | 2 | 1.25 |
| 65 | NAT | 2 | 325 (exact) |
