# GATE CS 2027 — Full-Length Mock Test 096

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

A factory produces 300 units with a 2% defect rate and another 200 units with a 5% defect rate. What percentage of the combined output is defective?

**Answer format:** Exact finite decimal percentage, without the percent sign.

### Q2. [1 Mark] [NAT]

A number leaves remainder 2 when divided by 5 and remainder 3 when divided by 7. What is the smallest positive such number?

**Answer format:** Integer.

### Q3. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Arrange these sentences into a coherent account. “This discrepancy” refers to the difference between the two measurements, and “the repair” refers to replacing the defective sensor.

P: A replacement sensor brought the readings into agreement.  
Q: Two instruments measuring the same temperature initially gave different readings.  
R: After the repair, both instruments remained stable during a second trial.  
S: This discrepancy led the technician to identify a defective sensor.

A. Q,S,P,R  
B. S,Q,R,P  
C. Q,P,R,S  
D. P,R,Q,S

### Q4. [1 Mark] [NAT]

A fair six-sided die is rolled. If the first result is odd, it is discarded and the die is rolled once more; otherwise the first result is retained. The second result, if rolled, is always retained. What is the probability that the retained result is6?

**Answer format:** Exact decimal.

### Q5. [1 Mark] [MCQ]

“The panel gave the proposal a qualified endorsement: it supported the idea, provided that the budget and access arrangements were revised.” What does “qualified” mean here?

A. Issued by a person holding a professional certificate.
B. Limited by stated conditions.
C. Completely withdrawn.
D. Expressed without reservation.

### Q6. [2 Marks] [NAT]

A positive quantity doubles every three hours. Another positive quantity triples every six hours. They begin with equal values. After how many hours does the ratio of the first quantity to the second first reach16/9? Growth is continuous with these constant exponential rates.

**Answer format:** Exact number of hours.

### Q7. [2 Marks] [NAT]

Four distinct tasks A,B,C,D are placed in a linear order. Consider the four assertions: A is before B; B is before C; C is before D; D is before A. How many task orders make exactly two assertions true?

**Answer format:** Integer.

### Q8. [2 Marks] [NAT]

A cube has face labels equal to the original outward normal directions: +x,−x,+y,−y,+z,−z. First rotate the cube90 degrees about the positive x axis, then90 degrees about the positive y axis, each by the right-hand rule about fixed world axes. Encode the face finally pointing upward(+z) as follows: +x=1,−x=2,+y=3,−y=4,+z=5,−z=6. What code results?

**Answer format:** Integer code.

### Q9. [2 Marks] [NAT]

A sequence starts a1=0. For each positive integer n, define a(n+1)=a(n)+n when n is odd and a(n+1)=a(n)−n when n is even. What is a101?

**Answer format:** Integer, including a minus sign if needed.

### Q10. [2 Marks] [NAT]

An open rectangular box is made by cutting equal squares of integer side x from the four corners of a 20 cm by 12 cm sheet and folding the remaining flaps. Here x is a positive integer and the box must have positive dimensions. What is the largest possible volume in cubic centimetres?

**Answer format:** Integer.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

M is a finite monoid with identity e and satisfies left cancellation: ax=ay implies x=y. Which statements must hold?

A. For each a, the map x↦ax is onto M.  
B. Every a has a two-sided inverse.  
C. M must be commutative.  
D. M is a group.

### Q12. [1 Mark] [MCQ]

A sorted data file has fixed-length records, with exactly eight records per data page and no unused slots. A range query matches exactly 16 consecutive records in file order. An index lookup requires exactly two page reads and identifies the first matching record's page and slot. Index pages are separate from data pages, no page is initially cached, and scanning the range reads each needed data page once. What is the largest possible total number of page reads, over the possible starting slots?

A. 3  
B. 4  
C. 5  
D. 6

### Q13. [1 Mark] [NAT]

A link carries 2 million bits per second. A 1000-byte packet takes how many milliseconds to serialize onto the link, ignoring overhead and propagation?

**Answer format:** Integer milliseconds.

### Q14. [1 Mark] [NAT]

A physically addressed direct-mapped cache holds 4 KiB of data in 64-byte lines. Physical addresses are 24 bits and memory is byte-addressed. How many bits are in each cache tag?

**Answer format:** Integer.

### Q15. [1 Mark] [MSQ]

A binary linear error-detecting code regards a received vector as valid exactly when its syndrome is zero. Which statements are correct?

A. Adding a nonzero codeword as an error pattern is undetected.
B. A zero syndrome proves that no bits were altered.
C. The syndrome of the received word equals the syndrome of the error when the transmitted word was valid.
D. Every nonzero error pattern has a nonzero syndrome.

### Q16. [1 Mark] [NAT]

After tabular minimization, selecting prime implicants P,Q,R must satisfy the cover expression (P+Q)(Q+R)(P+R), where + means choosing at least one listed implicant and multiplication means satisfying all requirements. Each selected implicant has equal cost. How many distinct minimum-cardinality covers exist?

**Answer format:** Exact integer.

### Q17. [1 Mark] [NAT]

For f(x)=ln x on [1,e], the mean value theorem gives a point c in (1,e) satisfying f′(c)=(f(e)−f(1))/(e−1). What is c, rounded to three decimal places?

**Answer format:** Number to 3 decimal places.

### Q18. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An invertible matrix A has factorization A=LU, with L unit lower triangular and U upper triangular. To solve Aᵀx=b, which statements are correct?

A. Aᵀ=UᵀLᵀ.  
B. Solving Lᵀy=b and then Uᵀx=y always gives the desired x.  
C. One can first solve Uᵀy=b, then Lᵀx=y.  
D. Lᵀ is unit upper triangular.

### Q19. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Consider the grammar S -> SS | aSb | epsilon. Count finite ordered parse trees, distinguishing different tree shapes even when they yield the same string. How many parse trees yield the string ab?

A. Exactly one  
B. Exactly two  
C. A finite number greater than two  
D. Infinitely many

### Q20. [1 Mark] [MSQ]

A directed graph has edges s→a of weight 2, s→b of weight 5, and b→a of weight −4. There are no other edges. Which statements are correct?

A. The shortest s-to-a path has weight 1.
B. The graph has a negative-weight cycle.
C. A Dijkstra implementation that permanently settles a before b can output a wrong distance for a.
D. Every shortest path uses the fewest possible edges.

### Q21. [1 Mark] [NAT]

What integer is printed? The static variable is initialized once.

```c
#include <stdio.h>
int f(int n) {
    static int k = 0;
    int a = ++k;
    if (n == 0) return a;
    return a + f(n-1);
}
int main(void) {
    int x = f(2);
    int y = f(1);
    printf("%d\n", x+y);
    return 0;
}
```

**Answer format:** Integer.

### Q22. [1 Mark] [NAT]

A stable sort by key is applied to records (2,A),(1,B),(2,C),(1,D). What is the one-based position of record (2,A) in the sorted output?

**Answer format:** Integer.

### Q23. [1 Mark] [NAT]

A four-input priority encoder gives highest priority to D3, then D2, D1,D0, and outputs the two-bit index of the highest asserted input. Its validity output is one whenever any input is one. How many four-bit input patterns produce code 10 with validity one?

**Answer format:** Integer.

### Q24. [1 Mark] [NAT]

Let f be continuous on[0,1], and define F(x)=the integral of f(t) from0 to x. If f(x)=2x and F(0)=0, what is the integral of F(x) from0 to1?

**Answer format:** Decimal rounded to four places.

### Q25. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A lexer recognizes identifiers by `[a-z][a-z0-9]*`, the keyword `if`, and operators `==`, `=`, `++`, `+`. It uses maximal munch; an identifier lexeme exactly equal to `if` is classified as a keyword. Whitespace is ignored. What token-lexeme sequence is produced for `ifx==if+++x`?

A. if, x, ==, if, ++, +, x  
B. ifx, ==, if, ++, +, x  
C. ifx, =, =, if, +, ++, x  
D. ifx, ==, if, +++, x

### Q26. [1 Mark] [NAT]

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

### Q27. [1 Mark] [NAT]

A DMA transfer moves 4 KiB using bursts of 16 bytes. Each burst occupies the memory bus for 3 cycles, and different bursts do not overlap. How many bus cycles are occupied by the transfer? Here 1 KiB=1024 bytes.

**Answer format:** Integer.

### Q28. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In C, `char s[]="a\0bc";` is declared. What are sizeof(s) and strlen(s), respectively? The proper standard header is included.

A. (4,4)  
B. (5,1)  
C. (5,4)  
D. (4,1)

### Q29. [1 Mark] [MCQ]

A B+ tree supports scanning all keys in sorted order. Which property directly allows continuing from one leaf to the next without returning to the root after every leaf?

A. Leaf-level sibling links.
B. Equal key values in every internal node.
C. One separate root per leaf.
D. Absence of separators in internal nodes.

### Q30. [1 Mark] [MSQ]

A nondeterministic PDA begins with one bottom symbol Z on its stack. It has exactly these moves: on input a with top Z, replace Z by XZ; on input b with top X, pop X; on empty input with top Z, pop Z. There are no moves with an empty stack. Acceptance requires the entire input to be consumed and the stack to be empty. Which strings are accepted?

A. epsilon
B. ab
C. aabb
D. abab

### Q31. [1 Mark] [NAT]

A binary buddy allocator manages a contiguous1024-byte region and rounds each allocation up to a power of two. Four256-byte blocks at offsets0,256,512,768 are allocated. The blocks at offsets0 and512 are then freed; the others remain allocated. With no relocation, what is the largest single allocation request, in bytes, that can now be satisfied?

**Answer format:** Integer.

### Q32. [1 Mark] [NAT]

A synchronous modulo-5 counter uses three flip-flops. Legal states 000,001,010,011,100 advance cyclically in that order; each illegal state goes to 000 on the next edge. From initial state 111, what unsigned state value appears after seven clock edges?

**Answer format:** Exact integer.

### Q33. [1 Mark] [MSQ]

Grammar S→aA | aB, A→b, B→c is rewritten as S→aX, X→A | B, A→b, B→c. Which statements are correct?

A. Both grammars generate exactly {ab,ac}.
B. The rewritten grammar can choose between X→A and X→B using one lookahead token.
C. The original grammar's two S alternatives have disjoint FIRST sets.
D. Left factoring necessarily removes ambiguity from every ambiguous grammar.

### Q34. [1 Mark] [NAT]

Let f(x)=x³+x on the real line, and let g be its inverse. Find g′(2).

**Answer format:** Exact finite decimal.

### Q35. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

In a production S→XY, the inherited attribute X.i is defined to equal the synthesized attribute Y.v. Y.v depends only on the tokens in Y's subtree and on no attributes of X. Which statements are correct?

**Candidates**

**I.** This rule violates the usual L-attributed restriction for an inherited attribute of X.

**II.** This dependency necessarily creates a cycle in the attribute graph.

**III.** A suitable evaluation order can compute Y.v before assigning X.i.

**IV.** The grammar must be syntactically ambiguous because this attribute rule exists.

A. I and III  
B. III and IV  
C. I and II  
D. I and IV

### Q36. [2 Marks] [NAT]

A five-stage in-order pipeline has stages IF,ID,EX,MEM,WB, one cycle each. ALU results can be forwarded from EX/MEM or MEM/WB to EX, but load data becomes available only after MEM. A dependent instruction immediately following a load must stall one cycle. No other stalls occur. For the sequence below, how many total cycles elapse from the first IF through the last WB, starting empty?

```text
load r1, [r0]
add  r2, r1, r3
sub  r4, r2, r5
load r6, [r4]
add  r7, r6, r2
```

**Answer format:** Integer.

### Q37. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Relation R(A,B,C,D) has dependencies A→B, B→A and C→D, with no additional independent dependencies. Which statements are true?

**Candidates**

**I.** AC and BC are exactly its candidate keys.

**II.** R is already in BCNF.

**III.** Decomposition into AB, CD and AC is lossless and preserves all the given dependencies.

**IV.** Decomposition into AB and CD alone is guaranteed lossless.

A. I and IV  
B. I and III  
C. II and III  
D. II and IV

### Q38. [2 Marks] [MSQ]

G is a finite group of odd order, with identity e. An element x satisfies x^4=e and x^6=e. Which statements must hold?

A. x=e.
B. x has order2.
C. x²=e.
D. x has order3.

### Q39. [2 Marks] [NAT]

An open-addressed hash table has12 slots numbered0–11. For a particular key the probe sequence is (2+8i) modulo12 for i=0,1,2,... . All slots that this sequence can reach are occupied; all other slots are empty. If the secondary step is replaced by5 while the starting slot remains2, how many probes, including the initial probe, are needed to reach the first empty slot?

**Answer format:** Integer.

### Q40. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A dynamic array doubles its capacity when full. Initially it is empty with capacity one. Appending a value costs one unit, and a resizing append additionally copies every existing value at one unit per copy. For n=2^k appends, k≥1, what is the exact total cost?

A. n+k  
B. 2n−1  
C. n log₂n  
D. 3n

### Q41. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Transactions have timestamps T1=10,T2=20,T3=30, with lower meaning older. A wait-die lock manager lets an older requester wait for a younger holder but aborts a younger requester asking for an older holder's lock. T2 holds X, T3 requests X, then T1 requests X. What happens to these two requests, assuming T2 still holds X?

A. Both requesters wait.  
B. T3 aborts and T1 waits.  
C. T3 waits and T1 aborts.  
D. Both requesters abort.

### Q42. [2 Marks] [MSQ]

A ternary relation R(S,P,J) contains (s1,p1,j1),(s1,p2,j2),(s2,p1,j2). Form the natural join of its three binary projections on SP, SJ and PJ, using set semantics. Which statements are correct?

A. The join has four tuples.  
B. The join contains the spurious tuple (s1,p1,j2).  
C. Joining all binary projections of any ternary relation always recovers exactly that relation.  
D. The original R satisfies SP→J.

### Q43. [2 Marks] [NAT]

The function below uses a single shared counter c, initially0. Evaluation order is exactly as written.

```text
F(n):
    if n == 0: return c
    c = c + 1
    x = F(n-1)
    c = c + 1
    return x + c
```

What does F(3) return?

**Answer format:** Integer.

### Q44. [2 Marks] [NAT]

A byte-addressed machine loads a32-bit word using effective address Rbase+4×Rindex−8. Initially Rbase=100 and Rindex=3. Memory bytes at addresses104 through111 are 01,02,03,04,05,06,07,08 in hexadecimal. The machine is little-endian. What is the decimal value of the least significant16 bits of the loaded word?

**Answer format:** Exact integer.

### Q45. [2 Marks] [NAT]

A procedure make() creates a fresh variable x=0 and returns a closure inc that increments that captured variable by1 and returns its new value. Set f=make(), g=f, and h=make(). Each closure retains its environment after make returns. Calls f(),g(),h(),f() are made in that order. What is the sum of the returned values?

**Answer format:** Integer.

### Q46. [2 Marks] [MSQ]

A process opens a file once, duplicates that descriptor, and then forks. Assume ordinary shared-open-file-description semantics, no later opens, and sequential rather than concurrent reads. Which statements are correct?

A. Parent and child descriptor references can share one file offset.
B. Duplicating a descriptor necessarily creates an independent offset.
C. A read through one of the shared references can change the offset seen by the others.
D. Closing one reference necessarily closes every remaining reference immediately.

### Q47. [2 Marks] [NAT]

A three-address intermediate representation has one binary operation per assignment. To compute a*b+a*c+d*b+d*c, a compiler may reassociate and factor over mathematical integers and reuse intermediates. What is the minimum number of binary additions/multiplications needed if it uses the factorization(a+d)*(b+c)?

**Answer format:** Integer.

### Q48. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An 8-bit ALU performs subtraction x−y as x+(NOT y)+1 and retains only the low eight result bits. C is the carry out of bit 7; V indicates signed two's-complement overflow. For x=0x80 and y=0x01, which statements hold?

**Candidates**

**I.** The retained result is 0x7F.

**II.** C=0, indicating an unsigned borrow.

**III.** V=1.

**IV.** The signed mathematical result is representable in eight bits.

A. I and II  
B. I and IV  
C. I and III  
D. II and III

### Q49. [2 Marks] [NAT]

A connected undirected graph has six vertices and seven edges. Removing a particular edge e leaves it connected. How many edges must then be removed from the remaining graph to obtain a spanning tree, if removals may be chosen appropriately?

**Answer format:** Integer.

### Q50. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let h be a homomorphism that maps each symbol of a finite alphabet to a finite string, possibly ε. Which statements are correct?

A. The image under h of a regular language is regular.  
B. The image under h of a context-free language is context-free.  
C. A nonregular language must remain nonregular under every such h.  
D. Erasing every symbol maps every nonempty language to{ε}.

### Q51. [2 Marks] [NAT]

A file-system inode contains four direct block pointers and one single-indirect pointer. Each disk block is 1024 bytes and each pointer is four bytes. No other addressing scheme exists. What is the largest file size in bytes that this inode can address? Indirect-block storage is not part of the file's data.

**Answer format:** Integer.

### Q52. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Weighted activities have half-open time intervals, so one may start when another finishes:

| Activity | Interval | Weight |
|---|---|---:|
| A | [0,2) | 4 |
| B | [1,3) | 5 |
| C | [2,4) | 4 |
| D | [3,5) | 5 |
| E | [4,6) | 4 |
| F | [5,6) | 3 |

An earliest-finish greedy algorithm repeatedly chooses the compatible activity finishing first, breaking a tie by the earlier start. What pair gives (greedy total weight, maximum possible total weight)?

A. (12,12)  
B. (13,13)  
C. (12,13)  
D. (11,13)

### Q53. [2 Marks] [NAT]

How many distinct arrangements of AAABBBCCC have no two A symbols adjacent? Identical letters are indistinguishable.

**Answer format:** Integer.

### Q54. [2 Marks] [NAT]

A signed fixed-point representation stores an eight-bit two's-complement integer scaled by1/16. What is the width of its representable real interval, defined as largest value minus smallest value?

**Answer format:** Exact decimal.

### Q55. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Consider proving that L={a^(n²) : n≥0} is not regular using pumping length p≥1 and word a^(p²). Which statements are correct?

**Candidates**

**I.** Every permitted pumping substring y has length d satisfying1≤d≤p.

**II.** Pumping y twice gives length p²+d, strictly between consecutive squares p² and(p+1)².

**III.** Choosing y of length0 is permitted and defeats the proof.

**IV.** The word's length is too small to invoke the lemma for any p≥1.

A. I and III  
B. I and IV  
C. II and III  
D. I and II

### Q56. [2 Marks] [NAT]

A process has descriptor3 for an open file. It calls dup(3), obtaining descriptor4. It then sets the close-on-exec flag on descriptor3 only and successfully executes a new program. No other descriptor refers to this open-file description. How many descriptors in the new program refer to it?

**Answer format:** Integer.

### Q57. [2 Marks] [NAT]

In one slotted random-access attempt, four stations independently transmit with probability 1/2. A success occurs exactly when one station transmits. What is the probability of success in this slot?

**Answer format:** Exact finite decimal.

### Q58. [2 Marks] [NAT]

Routers A,B,C form a triangle with all three link costs 1. A also has a cost-1 link to destination D. Initially their distances to D are (1,2,2). The A–D link fails. They then run synchronous distance-vector rounds without split horizon or poison reverse. In each round every router computes its new distance using neighbours' distances from the preceding round; A cannot use its failed direct link. The first round uses the stated initial distances. What is the sum of A,B,C's distances after the second round?

**Answer format:** Integer.

### Q59. [2 Marks] [NAT]

A sequence has a0=1 and an=sum(a_i for i=0,...,n−1) for n≥1. What is a6?

**Answer format:** Integer.

### Q60. [2 Marks] [NAT]

A store-and-forward network has links S→R and R→D, each taking 1 ms to transmit one packet. Propagation is zero. At time 0, S has packets A,B,C in order. A and C must traverse both links; B terminates at R. Each link begins transmitting whenever its next eligible packet is available, preserving source order among packets that use it. What time in milliseconds does C finish arriving at D?

**Answer format:** Integer.

### Q61. [2 Marks] [NAT]

A syntax-directed definition evaluates a binary numeral by left-recursive production B→B₁ digit, with B.val=2×B₁.val+digit.val. A leaf digit has its numeric value. To support a binary point, production N→B . F uses N.val=B.val+F.val, and F→digit F₁ uses F.val=(digit.val+F₁.val)/2, with F→ε assigned 0. What value is assigned to `101.011`? Enter the exact decimal value.

**Answer format:** Exact finite decimal.

### Q62. [2 Marks] [NAT]

A C array `int a[2][3]={{1,2,3},{4,5,6}};` is followed by `int (*p)[3]=a;`. Evaluate `*(*(p+1)+2) + (*p)[1]`.

**Answer format:** Integer.

### Q63. [2 Marks] [NAT]

A singly linked structure has nodes0,1,2,3,4,5 and next pointers 0→1→2→3→4→5→2. Floyd's cycle-detection algorithm starts slow=fast=node0. In each iteration, slow advances once and fast twice, then equality is tested. What is the node label at the first equality after an iteration?

**Answer format:** Exact integer.

### Q64. [2 Marks] [NAT]

A binary floating-point system has precision p=4 significant bits, includes an implicit leading1 for normalized numbers, and has enough exponent range for all numbers here. It rounds to nearest, ties to even. Compute fl(fl(8+0.5)+0.5), rounding after each addition. What value results?

**Answer format:** Exact decimal or integer.

### Q65. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Let F(x,y,z)=xy+yz+zx using Boolean AND and OR. Define its Boolean difference with respect to x as F(0,y,z) XOR F(1,y,z). Which statements are correct?

**Candidates**

**I.** The difference equals y+z.

**II.** The difference equals y XOR z.

**III.** The difference is independent of x.

**IV.** The difference equals yz.

A. I and III  
B. II and III  
C. I and IV  
D. II and IV

## ANSWER KEY — MOCK TEST 096

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | NAT | 1 | 3.2 |
| 2 | NAT | 1 | 17 |
| 3 | MSQ | 1 | B, C, D |
| 4 | NAT | 1 | 0.25 |
| 5 | MCQ | 1 | B |
| 6 | NAT | 2 | 12 |
| 7 | NAT | 2 | 16 (exact) |
| 8 | NAT | 2 | 2 |
| 9 | NAT | 2 | -50 |
| 10 | NAT | 2 | 256 |
| 11 | MCQ | 1 | C |
| 12 | MCQ | 1 | C |
| 13 | NAT | 1 | 4 |
| 14 | NAT | 1 | 12 |
| 15 | MSQ | 1 | A, C |
| 16 | NAT | 1 | 3 |
| 17 | NAT | 1 | 1.718 (range 1.7175–1.7185) |
| 18 | MCQ | 1 | B |
| 19 | MSQ | 1 | A, B, C |
| 20 | MSQ | 1 | A, C |
| 21 | NAT | 1 | 15 |
| 22 | NAT | 1 | 3 |
| 23 | NAT | 1 | 4 |
| 24 | NAT | 1 | 0.3333 (accepted range 0.33325–0.33335) |
| 25 | MSQ | 1 | A, C, D |
| 26 | NAT | 1 | 21 |
| 27 | NAT | 1 | 768 |
| 28 | MSQ | 1 | A, C, D |
| 29 | MCQ | 1 | A |
| 30 | MSQ | 1 | A, B, D |
| 31 | NAT | 1 | 256 |
| 32 | NAT | 1 | 1 |
| 33 | MSQ | 1 | A, B |
| 34 | NAT | 1 | 0.25 |
| 35 | MCQ | 1 | A |
| 36 | NAT | 2 | 11 |
| 37 | MCQ | 2 | B |
| 38 | MSQ | 2 | A, C |
| 39 | NAT | 2 | 2 |
| 40 | MSQ | 2 | A, C, D |
| 41 | MSQ | 2 | A, C, D |
| 42 | MSQ | 2 | A, B, D |
| 43 | NAT | 2 | 18 |
| 44 | NAT | 2 | 513 |
| 45 | NAT | 2 | 7 |
| 46 | MSQ | 2 | A, C |
| 47 | NAT | 2 | 3 |
| 48 | MCQ | 2 | C |
| 49 | NAT | 2 | 1 |
| 50 | MCQ | 2 | C |
| 51 | NAT | 2 | 266240 |
| 52 | MSQ | 2 | A, B, D |
| 53 | NAT | 2 | 700 |
| 54 | NAT | 2 | 15.9375 |
| 55 | MCQ | 2 | D |
| 56 | NAT | 2 | 1 |
| 57 | NAT | 2 | 0.25 |
| 58 | NAT | 2 | 9 |
| 59 | NAT | 2 | 32 |
| 60 | NAT | 2 | 4 |
| 61 | NAT | 2 | 5.375 |
| 62 | NAT | 2 | 8 |
| 63 | NAT | 2 | 4 |
| 64 | NAT | 2 | 8 |
| 65 | MCQ | 2 | B |
