# GATE CS 2027 — Full-Length Mock Test 036

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

Q1–Q5 and Q11–Q35 carry one mark each; Q6–Q10 and Q36–Q65 carry two marks each. General Aptitude contributes 15 marks, Engineering Mathematics 13, and core Computer Science 72.

Select exactly one option for MCQ and all correct options for MSQ. Incorrect one-mark MCQs lose 1/3 mark; incorrect two-mark MCQs lose 2/3 mark. MSQ and NAT have no negative marking; MSQ has no partial credit. Unattempted questions receive zero. Follow each NAT answer format. The answer key follows Question 65.

---

## Section A — General Aptitude

### Q1. [1 Mark] [NAT]

A sequence is formed by writing one copy of 1, two copies of 2, three copies of 3, and so on. What is the sum of the entries in positions 90 through 94, counting the first entry as position 1?

**Answer format:** Exact integer.

### Q2. [1 Mark] [MCQ]

A circular track has two concentric lane centre-lines of radii r and r+1 metres. Two runners move at equal constant speeds toward a finish on a fixed radial line. The inner runner starts on that line and runs one complete lap. The outer runner starts ahead of that line and runs the remainder of the circuit. Both start simultaneously. By how many metres along the outer lane must its start be advanced from the finish line so that the runners finish simultaneously?

A. π
B. 2π
C. πr
D. 2πr

### Q3. [1 Mark] [MCQ]

Choose the sentence that unambiguously states that the technician, rather than the instrument, was in a hurry.

A. Being in a hurry, the instrument was checked by the technician.
B. The instrument was checked in a hurry that belonged to the technician.
C. In a hurry, the technician checked the instrument.
D. The technician checked the instrument that was in a hurry.

### Q4. [1 Mark] [NAT]

A price is first increased by p percent and then reduced by p percent, where 0<p<100. The final price is 96% of the original. What is p?

**Answer format:** Exact integer.

### Q5. [1 Mark] [MSQ]

Every signed form is archived. No archived form is editable. At least one editable form exists. Which conclusions necessarily follow?

A. No signed form is editable.
B. Every unsigned form is editable.
C. At least one unsigned form exists.
D. At least one signed form exists.

### Q6. [2 Marks] [MCQ]

A pattern consists of four distinctly labelled points at coordinates P=(0,0), Q=(2,0), R=(0,1), S=(1,1). First reflect it in the line x=y; then rotate it clockwise through 90 degrees about the origin. Which single transformation gives the same final positions for all four labels?

A. Reflection in the x-axis.
B. Reflection in the y-axis.
C. Rotation through 180 degrees about the origin.
D. Translation by (1,−1).

### Q7. [2 Marks] [MSQ]

Read the passage: “The library extended evening hours and then recorded a rise in visits per week. During the same period, a nearby reading room closed. Visitor surveys were voluntary and were collected only during the new evening hours. Most respondents said that the extended hours were useful.” Which statements are justified?

A. The observed increase by itself identifies the extended hours as the sole cause.
B. The reading-room closure is a possible alternative contributor to the increase.
C. The survey directly estimates the views of all local residents without selection concerns.
D. The survey results are compatible with visitors outside the new hours having different views.

### Q8. [2 Marks] [NAT]

Six distinct students A,B,C,D,E,F are partitioned into two unlabelled groups of three. One leader is chosen in each group. A and B must be in different groups, C must lead the group containing C, and B must not be a leader. How many different group-and-leader assignments are possible? Swapping the names or display order of the two groups does not create a new assignment.

**Answer format:** Exact integer.

### Q9. [2 Marks] [NAT]

Two branches report successful deliveries as follows. Each delivery belongs to exactly one branch and one period.

| Branch | Period 1: successes/attempts | Period 2: successes/attempts |
|---|---:|---:|
| East | 81/90 | 19/20 |
| West | 2/10 | 24/80 |

Both branches improved their success rates. By how many percentage points did the overall success rate decrease from Period 1 to Period 2?

**Answer format:** Exact integer.

### Q10. [2 Marks] [NAT]

A square sheet occupies 0≤x≤8, 0≤y≤8. Fold the right half onto the left along x=4, then the top half onto the bottom along y=4. Punch one tiny circular hole centred at (4,1), and another centred at (2,2), through every layer. The radii are equal and less than 0.1; the first punch straddles the vertical folded edge. After unfolding completely, how many distinct circular holes are present? Count a hole centred on a former fold line once.

**Answer format:** Exact integer.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

A byte-addressed 16-bit address bus interfaces an 8 KiB memory chip. Chip inputs A0 through A12 connect to the corresponding bus lines. The chip is selected exactly when A15=1 and A14=0; A13 is not decoded. How many distinct CPU byte addresses access the same physical byte of this chip?

**Answer format:** Exact integer.

### Q12. [1 Mark] [MCQ]

A data set has five real observations with median 10 and mean 12. A sixth observation equal to 100 is appended. Which quantity is determined uniquely from this information?

A. The new median.
B. The new mean.
C. The new range.
D. The new population variance.

### Q13. [1 Mark] [MSQ]

For a directed simple graph on n labelled vertices, an adjacency matrix M stores M[u,v]=1 exactly when u→v exists. There are no self-loops. Which statements are correct?

A. A diagonal entry of M² counts directed walks of length two returning to that vertex.
B. The sum of all entries of M always equals twice the number of directed edges.
C. Transposing M reverses every edge.
D. A zero diagonal of M implies a zero diagonal of M².

### Q14. [1 Mark] [MCQ]

A weak entity Installment is identified by its owner Loan and its partial key installment_number. Loan has primary key loan_id. Each installment has exactly one owner, and the same installment_number may occur under different loans. Which primary key preserves this identification when mapping Installment to a relation?

A. installment_number alone.
B. loan_id alone.
C. (loan_id, installment_number).
D. amount alone.

### Q15. [1 Mark] [MSQ]

Under set relational algebra, R(A,B) contains (1,x),(1,y),(2,x), and S(B) contains x,y. Let D=R÷S and P=π_A(R). Which statements hold?

A. D contains exactly the tuple A=1.
B. D=P.
C. Adding (2,y) to R makes D=P.
D. Removing y from S makes D empty.

### Q16. [1 Mark] [MCQ]

All variables below are distinct scalar integers, with exact arithmetic and no side effects. Which expression can replace the right-hand side of the last assignment while preserving the program's result for every initial state?

```text
t = a + b
a = a + 1
u = a + b
```

A. t
B. t + 1
C. t − 1
D. b + 1

### Q17. [1 Mark] [MSQ]

A connected weighted undirected graph has a vertex v incident to exactly one edge e. Edge weights may be negative or equal. Which statements necessarily hold?

A. Every spanning tree contains e.
B. Every minimum spanning tree contains e.
C. e must be the minimum-weight edge in the entire graph.
D. Removing e leaves a connected graph.

### Q18. [1 Mark] [NAT]

Under multiplication modulo 10, consider the set {2,4,6,8}. It forms a group with identity 6. What is the order of the element 2 in this group, namely the least positive k for which 2^k is the group identity?

**Answer format:** Exact integer.

### Q19. [1 Mark] [MCQ]

A lexer recognizes the keyword `in`, identifiers matching [a-z]+, and the single-character token '.'. It uses longest match, giving the keyword priority over an identifier only when their matched lengths tie. What token-type sequence is produced on input `in.inner`?

A. keyword, '.', identifier.
B. identifier, '.', keyword, identifier.
C. keyword, '.', keyword, identifier.
D. identifier, '.', identifier.

### Q20. [1 Mark] [MSQ]

The input consists of a deterministic Turing machine M, a finite word w, and a nonnegative integer k. Which questions are decidable?

A. Does M halt on w within k transitions?
B. Does M ever halt on w?
C. Does M enter an accepting state during its first k transitions, including its initial configuration?
D. Is the language accepted by M empty?

### Q21. [1 Mark] [NAT]

Take two vertex-disjoint triangles and add one edge joining a vertex of one triangle to a vertex of the other. What is the minimum number of edges whose removal makes the resulting graph bipartite?

**Answer format:** Exact integer.

### Q22. [1 Mark] [MSQ]

A transmitted binary word contains data bits followed by one even-parity bit. The receiver checks only whether the parity of the whole received word is even. Which errors are always detected?

A. Exactly one data bit flips.
B. Exactly two data bits flip.
C. Exactly one data bit and the parity bit flip.
D. Exactly three distinct bits of the word flip.

### Q23. [1 Mark] [NAT]

Two D flip-flops store bits q1,q0. On every clock edge, q1 becomes the old q0 and q0 becomes NOT(old q1 XOR old q0). Starting at 00, what is the least positive number of edges after which the state is 00 again?

**Answer format:** Exact integer.

### Q24. [1 Mark] [MCQ]

A regular file has two hard links, p and q, and is open through descriptor d. No other links or opens exist. After both p and q are unlinked, which statement describes ordinary Unix file-lifetime semantics?

A. The file's contents must be reclaimed immediately, invalidating d.
B. d can still access the file, and final reclamation waits for the last open reference to close.
C. Unlinking q automatically creates a new pathname for the file.
D. Unlinking p removes q as a directory entry too.

### Q25. [1 Mark] [MCQ]

A learning Ethernet switch's forwarding table is initially empty. Host A on port 1 sends a unicast frame to host B, which is on port 2. The switch has three ports and no filtering restrictions. What does the switch do with this first frame?

A. Learn B on port 1 and forward only to port 2.
B. Learn A on port 1 and flood through ports 2 and 3.
C. Learn A on port 2 and drop the frame.
D. Learn both A and B from the frame and forward only to port 2.

### Q26. [1 Mark] [MSQ]

A directed graph has edges s→a of weight 2, s→b of weight 5, and b→a of weight −4. There are no other edges. Which statements are correct?

A. The shortest s-to-a path has weight 1.
B. The graph has a negative-weight cycle.
C. A Dijkstra implementation that permanently settles a before b can output a wrong distance for a.
D. Every shortest path uses the fewest possible edges.

### Q27. [1 Mark] [NAT]

Over {a,b}, consider the regular expression a*(ba*)*. How many different words of length four belong to its language?

**Answer format:** Exact integer.

### Q28. [1 Mark] [MCQ]

Router R uses a distance-vector update. Its link costs to neighbours U and V are 2 and 5. They advertise distances 7 and 3, respectively, to destination D. R has no other route to D. If the link to V fails and U's advertisement is unchanged, what distance does R compute for D in its next update?

A. 7
B. 8
C. 9
D. Infinity

### Q29. [1 Mark] [NAT]

An unsigned fixed-point format uses six bits with a scale factor of 1/8: the stored unsigned integer k represents k/8. Addition wraps modulo 64 in the stored integer. What numerical value is stored after adding the encodings of 5.75 and 3.5?

**Answer format:** Exact decimal.

### Q30. [1 Mark] [NAT]

How many subsets of {1,2,3,4,5,6} have even cardinality and contain exactly one of 1 and 2?

**Answer format:** Exact integer.

### Q31. [1 Mark] [MSQ]

An insertion-sort implementation shifts a preceding element only when it is strictly greater than the key being inserted. Records have a sorting key and a distinct label. Which statements are correct?

A. Equal-key records retain their initial relative order.
B. Replacing the strict comparison by “greater than or equal” still guarantees stability.
C. On an already sorted array, no record is shifted by the inner loop.
D. On every input, the number of shifts equals the number of adjacent equal-key pairs.

### Q32. [1 Mark] [NAT]

A sequence satisfies a0=1, a1=3 and a(n)=2a(n−1)−a(n−2) for n≥2. What is the coefficient of x^5 in its ordinary generating function Σ a(n)x^n?

**Answer format:** Exact integer.

### Q33. [1 Mark] [MCQ]

A processor initially spends half its execution time stalled for memory and half doing other work. An upgrade halves only the memory-stall time for the same program and input. What is the overall speedup?

A. 2
B. 3/2
C. 4/3
D. 1

### Q34. [1 Mark] [MSQ]

A process calls a blocking read on an empty pipe whose write end is still open elsewhere. No signal interrupts the call. Which statements are correct?

A. The process must consume a CPU core continuously until data arrives.
B. The operating system can deschedule the blocked process.
C. Another process can run on the same core while this process waits.
D. Empty at this instant necessarily means end-of-file.

### Q35. [1 Mark] [NAT]

What value is printed by this C program? All accesses are within the array.

```c
#include <stdio.h>
void change(int *p) {
    p += 2;
    *p = *(p - 1) + *p;
}
int main(void) {
    int a[4] = {3, 5, 7, 9};
    int *p = a + 1;
    change(p);
    printf("%d", *p + a[3]);
    return 0;
}
```

**Answer format:** Exact integer.

### Q36. [2 Marks] [NAT]

Consider the grammar S→aSbS | bSaS | ε. How many distinct leftmost derivations produce the word abab? Count derivations differing in production choices or in which substrings are generated by the two occurrences of S separately.

**Answer format:** Exact integer.

### Q37. [2 Marks] [NAT]

The following pseudocode uses a reference to one shared integer x. Arithmetic is exact.

```text
f(n, reference x):
    if n = 0: return x
    x = x + 1
    a = f(n - 1, x)
    x = x + a
    return x
```

Initially x=1. After evaluating f(3,x), what is the final value of x?

**Answer format:** Exact integer.

### Q38. [2 Marks] [MSQ]

An initially empty hash table has slots 0 through 6. All inserted keys have primary hash 0. For each insertion, quadratic probing visits slots i² mod 7 for i=0,1,…,6, in that order, and reports failure if all these visits find occupied slots. There are no deletions. Which statements hold?

A. The first four keys can all be inserted.
B. The fifth insertion succeeds because three slots are still empty.
C. No insertion ever examines slot 3.
D. Replacing this probe rule by i mod 7 would have the same failure point.

### Q39. [2 Marks] [NAT]

A binary floating-point system retains three significant bits including the leading 1, has unbounded exponent range, and rounds each addition to nearest with ties to an even last retained bit. Let fl denote this rounding. For a=8, b=1, c=−8, what is fl(a+fl(b+c))−fl(fl(a+b)+c)? All three operands are represented exactly.

**Answer format:** Exact integer.

### Q40. [2 Marks] [NAT]

Independent unbiased bits a,b,c are supplied to two Boolean circuits. One computes F=(a OR b) AND (a OR c). The other computes G=(a AND b) OR (a AND c). What is the probability that their outputs differ?

**Answer format:** Exact decimal.

### Q41. [2 Marks] [MSQ]

An NPDA chooses one of two branches at the start. Its first branch recognizes {a^i b^j c^k : i=j, i,j,k≥0}; its second recognizes {a^i b^j c^k : j=k, i,j,k≥0}. Acceptance requires consuming the entire input and acceptance by at least one branch. Which words does it accept?

A. aabbccc
B. aabbbccc
C. aaabcc
D. abc

### Q42. [2 Marks] [NAT]

An IPv4 datagram has a 20-byte header without options and 2000 bytes of payload. It traverses a link of MTU 1020 bytes, then a link of MTU 620 bytes. At each link, fragmentation uses the largest legal payload for each nonfinal fragment. Every resulting fragment traverses both links; no reassembly occurs between them. What is the sum of the fragment-offset field values in the four fragments leaving the second link? Offsets are measured in units of eight bytes relative to the original payload.

**Answer format:** Exact integer.

### Q43. [2 Marks] [MSQ]

In tuple relational calculus, R(x) is a unary relation containing {1,2}. Consider the expression {x | NOT R(x)}, with x ranging over the entire interpretation domain. Which statements hold?

A. Over domain {1,2,3}, its result is {3}.
B. Over domain {1,2,3,4}, its result is still {3}.
C. Its result depends on values outside R, so it is not domain-independent.
D. Replacing the formula by R(x) AND NOT R(x) yields a domain-independent empty result.

### Q44. [2 Marks] [NAT]

On the fixed domain {1,2,3}, how many binary relations R satisfy both (∀x ∃y R(x,y)) and NOT(∃y ∀x R(x,y))? Relations are distinguished by their sets of ordered pairs.

**Answer format:** Exact integer.

### Q45. [2 Marks] [MSQ]

Consider the augmented grammar with start S and productions

```text
S → A a | b A c | d c | b d a
A → d
```

Consider the parser state reached after shifting the viable prefix bd. Which statements are correct?

A. The LR(0) item set contains S→bd·a and A→d·.
B. An SLR(1) table has a shift/reduce conflict on a in this state.
C. The completed A→d· item in the corresponding canonical LR(1) state has lookahead c, so it does not cause a conflict on a.
D. FOLLOW(A) contains only c.

### Q46. [2 Marks] [NAT]

A syntax-directed definition assigns each bit string X two attributes: length X.len and fraction X.val. For a single bit b, len=1 and val=b/2. For concatenation X=YZ, the rules are X.len=Y.len+Z.len and X.val=Y.val+Z.val/2^(Y.len). A parse tree concatenates Y=10 and Z=11. What is X.val?

**Answer format:** Exact decimal.

### Q47. [2 Marks] [NAT]

A cache has one data line and a separate one-line victim cache, both initially empty. A hit in the victim cache swaps its line with the main-cache line and does not access memory. On a miss in both, memory supplies the requested block to the main cache; its old valid block replaces the victim-cache line. Blocks are clean. For the access sequence A,B,A,C,B, how many memory block reads occur?

**Answer format:** Exact integer.

### Q48. [2 Marks] [MSQ]

Let L={ww : w∈{a,b}*}, a non-context-free language. Define the homomorphism h by h(a)=h(b)=0. Which statements are correct?

A. h(L) consists of all even-length words over {0}.
B. h(L) is regular.
C. Non-context-freeness of L implies non-context-freeness of h(L).
D. The word 000 belongs to h(L).

### Q49. [2 Marks] [MSQ]

D(id) contains 1 and 2. E(eid,did,active) contains (10,1,0) and (11,1,1); all columns are non-NULL. Consider this SQL query:

```sql
SELECT D.id, COUNT(*) AS n, COUNT(E.eid) AS m
FROM D LEFT JOIN E
  ON D.id = E.did AND E.active = 1
GROUP BY D.id;
```

Which statements are correct?

A. The row for id=1 has n=1 and m=1.
B. The row for id=2 has n=1 and m=0.
C. Moving E.active=1 from ON to WHERE necessarily preserves the result.
D. The row for id=2 has n=0 and m=0.

### Q50. [2 Marks] [NAT]

Routers R and S forward packets by longest-prefix match. R has a connected route for 10.0.0.0/25 and a default route via S. S has a connected route for 10.0.0.192/26 and a default route via R. A packet addressed within 10.0.0.0/24 begins at R. Ignore TTL expiration and count every address, including subnet endpoints. For how many destination addresses does the packet loop between R and S rather than reach either connected network?

**Answer format:** Exact integer.

### Q51. [2 Marks] [MSQ]

F=(a OR b) AND ((NOT a) OR c) is implemented as a two-level OR-AND circuit with an inverter for NOT a. Inputs b=c=0 are held fixed while a changes. Gate delays are positive and unequal. Which statements are correct?

A. F is logically 0 before and after the change.
B. Unequal path delays can briefly make F=1.
C. Adding the factor (b OR c) leaves the Boolean function unchanged and prevents this particular static-0 hazard in the resulting two-level realization.
D. Adding the factor (b OR c) necessarily changes the truth table.

### Q52. [2 Marks] [MSQ]

For real t consider

```text
x1 + x2 + x3 = 1
x1 + 2x2 + 3x3 = 2
2x1 + 3x2 + 4x3 = t
```

Which statements are correct?

A. The system is consistent exactly when t=3.
B. When t=3, there are infinitely many solutions.
C. Every solution satisfies x1=x3.
D. When t=3, the coefficient matrix is invertible.

### Q53. [2 Marks] [NAT]

A NAT allocates one public source port per distinct internal (IP address, UDP source port) pair, reusing that mapping for all remote destinations. It never expires a mapping during this experiment. Client A uses source port 4000 to contact three different servers; client B uses source port 4000 to contact two servers; client A additionally uses source port 4001 to contact one server. A and B have different internal IP addresses. How many mappings exist afterward?

**Answer format:** Exact integer.

### Q54. [2 Marks] [NAT]

Procedure P lexically contains Q and S; Q lexically contains R. During execution P calls S, S calls Q, and Q calls R. There is no recursion. Each frame has a static link to its lexical parent's active frame and a dynamic link to its caller. Starting at R's frame, how many more dynamic-link traversals than static-link traversals are needed to reach P's frame?

**Answer format:** Exact integer.

### Q55. [2 Marks] [NAT]

Initially its completion counter is zero and its timer is stopped. A device completes DMA requests at times 0,3,6,9,12,… microseconds. On the first completion after an interrupt, it starts a 10-microsecond timer and sets a completion counter to 1. Further completions increment the counter. It interrupts when either the counter reaches 8 or the timer expires, then clears the counter and stops the timer. Completions are instantaneous; none coincide with the first two timer expirations. How many interrupts occur at or before time 30 microseconds?

**Answer format:** Exact integer.

### Q56. [2 Marks] [NAT]

Assume every fork succeeds. Each child starts at the statement after its own fork, and x is ordinary private process memory. How many total lines are printed by all processes?

```c
int x = 0;
if (fork() == 0) x = 1;
if (x == 0) fork();
printf("done\n");
```

No code outside this fragment creates processes or prints lines.

**Answer format:** Exact integer.

### Q57. [2 Marks] [MSQ]

Consider the following algorithm, with n≥2 and a constant-time body that allocates no storage:

```text
for i = 1 to n:
    for j = i to n step i:
        body()
```

Which statements are correct?

A. The body executes exactly Σ(i=1..n) floor(n/i) times.
B. The running time is Θ(n log n).
C. The algorithm needs Θ(n) auxiliary words merely to execute these loops.
D. The body executes Θ(n²) times.

### Q58. [2 Marks] [MCQ]

The available closed intervals are [0,4], [3,8], [7,10], [0,6], [6,9], [8,10]. Starting at 0, a greedy covering algorithm repeatedly chooses, among intervals beginning at or before the current covered endpoint, an interval extending that endpoint farthest. It stops when [0,10] is covered. Which sequence does it select?

A. [0,4], [3,8], [8,10]
B. [0,6], [6,9], [8,10]
C. [0,6], [7,10]
D. [0,4], [7,10]

### Q59. [2 Marks] [MSQ]

Let f(x)=min(x²,2−x²) on the interval [−2,2]. Which statements are correct?

A. The maximum value is 1, attained at both x=−1 and x=1.
B. The minimum value is −2.
C. f is differentiable at x=0.
D. f is differentiable at x=1.

### Q60. [2 Marks] [MSQ]

A parent creates a pipe and forks one child. Both processes initially inherit both ends. The child reads until EOF. The parent writes a finite message, closes its own write descriptor, and waits for the child; the child has forgotten to close its inherited write descriptor. No other processes hold the pipe. Which statements are correct?

A. After draining the message, the child can block waiting for EOF.
B. The parent's close alone guarantees EOF at the child.
C. Closing the child's inherited write end before its read loop permits EOF once the parent's write end closes and buffered bytes are drained.
D. The parent waiting for the child automatically closes the child's descriptors.

### Q61. [2 Marks] [NAT]

An array has indices 0 through 14. A rearrangement moves the old element at index i to index 2i mod 15. To implement this permutation in place, an algorithm processes each nontrivial permutation cycle once, using one temporary element per cycle; a fixed point needs no processing. How many nontrivial cycles must it process?

**Answer format:** Exact integer.

### Q62. [2 Marks] [MSQ]

Two threads each execute the following twice, sharing x initially 0:

```text
r = atomic_read(x)    // r is private to this thread
atomic_write(x, r+1)
```

All reads and writes are sequentially consistent, but the read/write pair is not atomic. Each thread preserves its own program order. Which final values of x are possible after both threads finish?

A. 1
B. 2
C. 3
D. 4

### Q63. [2 Marks] [NAT]

An initially empty five-stage IF-ID-EX-MEM-WB pipeline issues at most one instruction per cycle. Without stalls, N retired instructions take N+4 cycles. Full forwarding leaves exactly one stall cycle for an immediately dependent load-use pair. A taken branch incurs exactly two additional cycles, with no other penalties. A path retires, in order, a load, an ALU instruction using that load, a taken branch depending on that ALU result, and a target ALU instruction. ALU-to-branch forwarding avoids any additional data stall. How many cycles elapse through the final instruction's WB?

**Answer format:** Exact integer.

### Q64. [2 Marks] [NAT]

A singly linked structure has three nodes before its cycle entry and a cycle of five nodes. Floyd's algorithm starts slow and fast at the head, then repeatedly advances slow by one link and fast by two until they first coincide after advancing. It then resets slow to the head and advances both by one until they meet at the entry. Across both phases, how many individual next-link traversals are performed? Resetting a pointer is not counted as a traversal.

**Answer format:** Exact integer.

### Q65. [2 Marks] [NAT]

Three independent draws select uniformly from three colours, with replacement. Let D be the number of distinct colours observed. What is Var(D)?

**Answer format:** Round to four decimal places; accepted tolerance ±0.00005 around the rounded answer.



---

## ANSWER KEY — MOCK TEST 036

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | NAT | 1 | 68 |
| 2 | MCQ | 1 | B |
| 3 | MCQ | 1 | C |
| 4 | NAT | 1 | 20 |
| 5 | MSQ | 1 | A, C |
| 6 | MCQ | 2 | A |
| 7 | MSQ | 2 | B, D |
| 8 | NAT | 2 | 15 |
| 9 | NAT | 2 | 40 |
| 10 | NAT | 2 | 6 |
| 11 | NAT | 1 | 2 |
| 12 | MCQ | 1 | B |
| 13 | MSQ | 1 | A, C |
| 14 | MCQ | 1 | C |
| 15 | MSQ | 1 | A, C |
| 16 | MCQ | 1 | B |
| 17 | MSQ | 1 | A, B |
| 18 | NAT | 1 | 4 |
| 19 | MCQ | 1 | A |
| 20 | MSQ | 1 | A, C |
| 21 | NAT | 1 | 2 |
| 22 | MSQ | 1 | A, D |
| 23 | NAT | 1 | 3 |
| 24 | MCQ | 1 | B |
| 25 | MCQ | 1 | B |
| 26 | MSQ | 1 | A, C |
| 27 | NAT | 1 | 16 |
| 28 | MCQ | 1 | C |
| 29 | NAT | 1 | 1.25 |
| 30 | NAT | 1 | 16 |
| 31 | MSQ | 1 | A, C |
| 32 | NAT | 1 | 11 |
| 33 | MCQ | 1 | C |
| 34 | MSQ | 1 | B, C |
| 35 | NAT | 1 | 21 |
| 36 | NAT | 2 | 2 |
| 37 | NAT | 2 | 32 |
| 38 | MSQ | 2 | A, C |
| 39 | NAT | 2 | 1 |
| 40 | NAT | 2 | 0.25 |
| 41 | MSQ | 2 | A, B, D |
| 42 | NAT | 2 | 400 |
| 43 | MSQ | 2 | A, C, D |
| 44 | NAT | 2 | 174 |
| 45 | MSQ | 2 | A, B, C |
| 46 | NAT | 2 | 0.6875 |
| 47 | NAT | 2 | 4 |
| 48 | MSQ | 2 | A, B |
| 49 | MSQ | 2 | A, B |
| 50 | NAT | 2 | 64 |
| 51 | MSQ | 2 | A, B, C |
| 52 | MSQ | 2 | A, B, C |
| 53 | NAT | 2 | 3 |
| 54 | NAT | 2 | 1 |
| 55 | NAT | 2 | 2 |
| 56 | NAT | 2 | 3 |
| 57 | MSQ | 2 | A, B |
| 58 | MCQ | 2 | B |
| 59 | MSQ | 2 | A, B, C |
| 60 | MSQ | 2 | A, C |
| 61 | NAT | 2 | 4 |
| 62 | MSQ | 2 | B, C, D |
| 63 | NAT | 2 | 11 |
| 64 | NAT | 2 | 21 |
| 65 | NAT | 2 | 0.3210 (accepted range 0.32095–0.32105) |

