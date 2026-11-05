# GATE CS — Additional Practice Set 008

**Questions:** 50  
**Maximum marks:** 75

Read the task above each embedded question carefully. For an invalid-answer task, select options that do not correctly answer the embedded question. For a pair task, select the pair containing all valid candidates. MCQ has one correct choice; MSQ requires all correct choices. The answer key follows Q50.

### Q1. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For Boolean variables x, y and z, let F=(x OR y) AND ((NOT x) OR z). Which expression is equivalent to F for every input?

A. (x AND z) OR ((NOT x) AND y)  
B. (x AND y) OR ((NOT x) AND z)  
C. y OR z  
D. x XOR y XOR z  

### Q2. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A CRC uses generator g(x) = x³ + x + 1 over GF(2). An error polynomial e(x) is undetected exactly when g(x) divides e(x). The transmitted block is long enough to contain each error pattern mentioned below. Which statements are correct? A burst of length L has nonzero first and last bits separated by L−1 positions.

A. Every single-bit error is detected.  
B. Every burst of length at most 3 is detected.  
C. A two-bit error whose nonzero bits are seven positions apart can be undetected.  
D. Every error affecting an odd number of bits is detected.  

### Q3. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Solid stacks of unit cubes stand in a 2-by-3 grid. Each stack has a nonnegative integer height and has no gaps. Looking along the two-row direction, the maximum heights in the three columns are 2,3,1 respectively. Looking along the three-column direction, the maximum heights in the two rows are 3,2 respectively. What pair gives the minimum and maximum possible total number of cubes?

A. (7,11)  
B. (6,11)  
C. (6,12)  
D. (8,12)  

### Q4. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A contiguous memory region occupies addresses [0,240), where [u,v) has size v−u. Initially its free regions are [0,60), [100,180), and [200,240). Process X occupies [60,100), and process Y occupies [180,200). Compare first-fit and best-fit, each starting from this initial state.

First allocate A of size 50, then B of size 35. Next free X and A, leaving B and Y allocated. Every allocation takes space from the lowest-address end of its selected hole. First-fit searches from address 0 on each request; best-fit selects the smallest sufficient hole. Adjacent free regions are immediately coalesced, with no metadata overhead or compaction.

What are the largest single requests that can now be satisfied under (first-fit, best-fit), respectively?

A. (100,180)  
B. (100,100)  
C. (180,180)  
D. (180,100)  

### Q5. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Arrange these sentences into the most coherent chronological paragraph, using the references “that inspection” and “second inspection” consistently.

P. This second inspection found no leak.  
Q. The crew replaced the cracked valve and inspected the pipe again.  
R. A pressure drop first prompted an inspection.  
S. That inspection identified a crack in the valve.

A. R,Q,S,P  
B. S,R,Q,P  
C. R,S,Q,P  
D. Q,P,R,S  

### Q6. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Student(S)={(1),(2)}, Enrollment(S,C)={(1,X)}, and Required(C) is empty. No constraint requires an enrolled course to be in Required. Compare:

- QI: all Student identifiers s such that for every c in Required, (s,c) is in Enrollment.
- QII: relational division Enrollment ÷ Required, with candidate S values taken from the projection of Enrollment on S.

Using set semantics, what are the results (QI,QII)?

A. (empty,empty)  
B. ({1},{1})  
C. ({1,2},{1,2})  
D. ({1,2},{1})  

### Q7. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A cube net consists of unit squares on a square grid. Labelled square centres are A=(0,0), B=(1,0), C=(2,0), D=(1,1), E=(1,2), F=(1,−1). Adjacent grid squares share an edge. Fold the net into a cube. Which listed pairs of faces share an edge on the cube?

A. A and E  
B. A and C  
C. E and F  
D. B and E  

### Q8. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Six distinct keys are in two already sorted runs of three keys each. Only comparisons between keys reveal their relative order. What is the smallest achievable worst-case number of additional comparisons needed to merge the runs into one sorted run?

A. 3  
B. 4  
C. 5  
D. 6  

### Q9. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Equivalence relations R and S on {1,2,3,4,5,6} have partitions {{1,2},{3,4},{5,6}} and {{1},{2,3},{4,5},{6}}, respectively. Let T be the smallest equivalence relation containing R∪S. How many ordered pairs are in R∩S and T, respectively?

A. 6 and 36  
B. 0 and 30  
C. 12 and 36  
D. 6 and 18  

### Q10. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Three processes each need at most three instances of a single resource type. Instances are identical, acquisitions are one at a time, and a process releases all its instances only when it has obtained its full requirement and completes. What is the smallest total number of instances that guarantees no resource deadlock for every allocation reachable under these rules, assuming runnable processes eventually run?

A. 6  
B. 7  
C. 8  
D. 9  

### Q11. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A process forks, then its child successfully executes a new program using exec. Which statement is correct under ordinary process semantics?

A. exec necessarily creates another process with a new process identifier.  
B. The child keeps its process identity while its program image is replaced.  
C. The parent's program image is replaced by the child's exec.  
D. The child resumes at the instruction after the successful exec call in its old program.  

### Q12. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A sorted array is [1,2,2,2,4,4,7]. A lower-bound search returns the first index whose key is at least x, while an upper-bound search returns the first index whose key is greater than x. Both return 7 if no such index exists, and indexing starts at zero. What pair is returned for x=4?

A. (3,5)  
B. (4,5)  
C. (4,6)  
D. (5,6)  

### Q13. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A receiver expects byte 1000. Segments containing bytes 1100–1199,1200–1299,1300–1399 arrive before the segment containing 1000–1099. It immediately sends a cumulative ACK for each arrival and buffers out-of-order bytes. No bytes are lost. What ACK numbers are sent for these four arrivals in order?

A. 1200,1300,1400,1100  
B. 1000,1000,1000,1400  
C. 1100,1200,1300,1400  
D. 1000,1100,1200,1300  

### Q14. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Two machines are on the same ordinary Ethernet broadcast domain. A host broadcasts an ARP request for its default gateway's IPv4 address. What is it principally trying to learn?

A. The gateway's Ethernet address on that LAN.  
B. The remote web server's TCP sequence number.  
C. The gateway's complete routing table.  
D. The DNS name of every host on the LAN.  

### Q15. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Which words belong to the language denoted by a*b | ab*?

A. aab  
B. abb  
C. ab  
D. ba  

### Q16. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A synchronous two-flip-flop machine starts at (q1,q0)=(0,1). On input 0 its next state is (0,1). On input 1 its next state is (q1 XOR q0, q1). After processing exactly five input bits, it accepts if its state is (0,1). How many of the 32 input strings are accepted?

A. 16  
B. 17  
C. 18  
D. 20  

### Q17. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Two finite, acyclic, singly linked lists may share a suffix by node identity. Their heads are h1 and h2. Which algorithm finds the first shared node, or reports none, in O(m+n) time and O(1) extra space?

A. Compare only the values stored in corresponding nodes.  
B. Measure both lengths, advance the longer list by their difference, then advance both pointers together until they are identical or both null.  
C. Return the first pair of nodes having equal stored values, regardless of identity.  
D. Reverse one list and return its new head without examining the other list.  

### Q18. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A compiler removes an assignment to scalar x as dead code. The right-hand side has no side effects, exceptions, or observable traps. Which conditions support removal?

**Candidates**

**I.** On every outgoing path, x is redefined before its current value is read, or execution ends without reading it.

**II.** x is read on at least one outgoing path before redefinition.

**III.** x is not live immediately after the assignment.

**IV.** x has a short variable name.

A. II and IV  
B. III and IV  
C. I and II  
D. I and III  

### Q19. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In an activation record, which link is normally used to restore the caller's activation when a procedure returns, regardless of lexical nesting?

A. The dynamic link.  
B. The static link in every case.  
C. A pointer to the global symbol table.  
D. A pointer to the first heap object.  

### Q20. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A process has four user-level threads mapped to one kernel-scheduled thread. The mapping does not replace blocking system calls with asynchronous operations. One user thread makes a blocking read that blocks the kernel thread. Which consequence follows while that kernel thread remains blocked?

A. The other user threads in the process automatically run on three other cores.  
B. None of its user threads can run through that blocked sole kernel thread.  
C. The process obtains four new kernel threads automatically.  
D. User-level scheduling can execute instructions without any runnable kernel thread.  

### Q21. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Relation R(A,B) has primary key A and a CHECK constraint `B > 0`, with B allowed to be NULL. Under ordinary SQL CHECK semantics, a row is rejected by CHECK only when the condition is FALSE. Which insertions can satisfy these constraints if A is a fresh non-NULL key each time?

**Candidates**

**I.** B=3

**II.** B=NULL

**III.** B=0

**IV.** B=−2

A. I and IV  
B. II and III  
C. I and II  
D. II and IV  

### Q22. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A translation lookaside buffer misses, but the page-table entry shows that the page is resident and accessible. Which statement is correct?

A. A TLB miss necessarily requires disk I/O.  
B. The translation can be obtained from the page table without a page fault.  
C. The virtual address must be invalid.  
D. The access must terminate the process.  

### Q23. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A tuple-calculus query uses `Employee(e) AND EXISTS d (Department(d) AND Works(e,d))`. What does it require of each returned employee?

A. Assignment to at least one listed department.  
B. Assignment to every department.  
C. No assignments at all.  
D. That every domain object be a department.  

### Q24. [2 Marks] [MSQ]

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

### Q25. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A DFS of a directed graph has discovery/finish intervals u:[2,11] and v:[4,7]. Edge u→v exists but is not a tree edge. How is it classified under standard DFS edge categories?

A. Back edge.  
B. Forward edge.  
C. Cross edge.  
D. Impossible because intervals may never nest.  

### Q26. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Records have fields name and department. The desired ascending order uses name as primary key and department as secondary key. Which methods guarantee that order for arbitrary input?

**Candidates**

**I.** Stable sort by name, followed by stable sort by department.

**II.** Stable sort by department, followed by stable sort by name.

**III.** Sort by department, followed by an arbitrary unstable sort comparing only names.

**IV.** Sort directly with a lexicographic comparator on (name,department).

A. I and III  
B. I and IV  
C. II and III  
D. II and IV  

### Q27. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A compiler produced correct output on every program in a finite test suite. No proof of correctness is available. Which inference is justified solely by this observation?

A. It is correct on every possible program.  
B. No incorrect output was observed on the tested programs.  
C. Every untested program must fail.  
D. A larger test suite cannot reveal a fault.  

### Q28. [2 Marks] [MCQ]

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

### Q29. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An NFA has states p,q,r, initial state p and sole accepting state r. Its transitions are δ(p,0)={p,q}, δ(p,1)={p}, δ(q,0)=δ(q,1)={r}, and δ(r,0)=δ(r,1)=∅. There are no epsilon transitions. Which statements are true?

A. After reading 010, the reachable-state set is {p,q}.  
B. The NFA accepts 010 because some earlier prefix reached r.  
C. Subset construction has exactly four reachable subsets.  
D. The recognized language consists of binary words whose second-last symbol is zero.  

### Q30. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A two-level AND–OR circuit implements f=ab+(NOT a)c. Assume b=c=1 and only a changes from0 to1. Gate delays are arbitrary positive values; a and NOT a need not change simultaneously. Which extra product term can be ORed into the output without changing f's Boolean function and eliminates the possible static-1 hazard for this transition?

A. (NOT b)(NOT c)  
B. a(NOT c)  
C. bc  
D. (NOT a)(NOT b)  

### Q31. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For a two-digit number with nonzero unequal digits, operation R reverses the digits and operation S replaces each digit d by 9−d. Which statement holds whenever the intermediate results are interpreted as two-digit strings, allowing a leading zero?

A. R followed by S always equals S followed by R.  
B. Applying R twice always produces S's result.  
C. Applying S twice always swaps the digits.  
D. R followed by S always leaves the original string unchanged.  

### Q32. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Let L={a^n : n is a perfect square}, including ε. For a hypothetical regular pumping length p≥1, choose s=a^(p²). A legal pumped part has length k with1≤k≤p. Which statements are correct?

**Candidates**

**I.** Pumping once more gives length p²+k, strictly between p² and(p+1)².

**II.** For every legal decomposition, pumping twice leaves the language.

**III.** The proof depends on choosing the pumped part to have exactly p symbols.

**IV.** The pumping lemma therefore proves L regular.

A. II and III  
B. I and II  
C. II and IV  
D. III and IV  

### Q33. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For x≠0 define g(x)=sin(1/x). Which statements are correct?

A. There exists a sequence of positive x approaching0 on which g(x)=1.  
B. There exists a sequence of positive x approaching0 on which g(x)=−1.  
C. The limit of xg(x) as x approaches0 is0.  
D. Assigning g(0)=0 makes g continuous at0.  

### Q34. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A binary linear error-detecting code regards a received vector as valid exactly when its syndrome is zero. Which statements are correct?

**Candidates**

**I.** Adding a nonzero codeword as an error pattern is undetected.

**II.** A zero syndrome proves that no bits were altered.

**III.** The syndrome of the received word equals the syndrome of the error when the transmitted word was valid.

**IV.** Every nonzero error pattern has a nonzero syndrome.

A. III and IV  
B. I and II  
C. I and IV  
D. I and III  

### Q35. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A function recursively calls itself. Its local scalar variable v must have a separate value for each active call. Which storage arrangement directly supports this requirement?

A. One shared static cell for v with no saving.  
B. A separate v slot in each activation record.  
C. A single constant compiled into the program.  
D. The caller's instruction address used as v's only storage.  

### Q36. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Among employees, every auditor is a reviewer, and no reviewer is an intern. At least one auditor exists. Which statements must follow?

**Candidates**

**I.** At least one reviewer is not an intern.

**II.** Every non-intern is an auditor.

**III.** No auditor is an intern.

**IV.** At least one intern exists.

A. I and IV  
B. I and III  
C. II and III  
D. II and IV  

### Q37. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Consider ordinary IPv4 fragmentation. Payload means the fragment's bytes after its own IP header. Which statements are correct?

A. A fragment with MF=1 must have a payload length divisible by8.  
B. A final fragment may have a payload length that is not divisible by8.  
C. The fragment-offset field directly gives a byte count without scaling.  
D. A fragment's own IP header bytes are not included when locating its payload using the fragment offset.  

### Q38. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Distinct keys are inserted into an unbalanced BST. Which statements are correct?

**Candidates**

**I.** Inserting sorted ascending keys can produce height n−1 for n keys, counting edges.

**II.** The inorder traversal is sorted regardless of insertion order.

**III.** Every insertion order produces the same tree shape.

**IV.** A sorted inorder traversal proves that search always takes logarithmic time.

A. II and IV  
B. III and IV  
C. I and III  
D. I and II  

### Q39. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

What does this C program print? All pointer accesses are valid.

```c
#include <stdio.h>
int main(void) {
    int u[] = {1, 3, 5}, v[] = {2, 4, 6};
    int *p[] = {u, v};
    int **q = p;
    int *tmp = q[0];
    q[0] = q[1];
    q[1] = tmp;
    q[0]++;
    *q[0] += *q[1];
    printf("%d %d\n", v[1], u[0]);
    return 0;
}
```

A. 4 2  
B. 5 1  
C. 4 1  
D. 5 2  

### Q40. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

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

### Q41. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

On a nonempty domain, P and Q are unary predicates. Which implications are valid for every interpretation?

**Candidates**

**I.** (∀x P(x)) OR (∀x Q(x)) implies ∀x(P(x) OR Q(x)).

**II.** ∀x(P(x) OR Q(x)) implies (∀x P(x)) OR (∀x Q(x)).

**III.** ∃x(P(x) AND Q(x)) implies (∃x P(x)) AND (∃x Q(x)).

**IV.** (∃x P(x)) AND (∃x Q(x)) implies ∃x(P(x) AND Q(x)).

A. I and IV  
B. II and III  
C. I and III  
D. II and IV  

### Q42. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An invertible matrix A has factorization A=LU, with L unit lower triangular and U upper triangular. To solve Aᵀx=b, which statements are correct?

A. Aᵀ=UᵀLᵀ.  
B. Solving Lᵀy=b and then Uᵀx=y always gives the desired x.  
C. One can first solve Uᵀy=b, then Lᵀx=y.  
D. Lᵀ is unit upper triangular.  

### Q43. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A datagram socket has two queued datagrams, with payloads ABCDE and FG in that order. A receive buffer has space for three bytes. In this specified model, a receive returns at most one datagram and discards any excess bytes of a truncated datagram. After one receive returns ABC, what payload does the next receive return?

A. FG  
B. DE  
C. DEF  
D. DEFG  

### Q44. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A circuit maps input bits x,y,z to u=x XOR y, v=y XOR z, w=x XOR z. Let t be the three-input majority bit. Which statements are correct?

**Candidates**

**I.** w=u XOR v.

**II.** The triple(u,v,w) uniquely determines(x,y,z).

**III.** The four outputs(u,v,w,t) uniquely determine(x,y,z).

**IV.** All eight possible triples(u,v,w) occur.

A. III and IV  
B. I and III  
C. I and II  
D. I and IV  

### Q45. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Consider the following code. The return is the only program exit and has no implicit use of other variables.

```text
x = 1;
y = x + 2;
x = 4;
return y;
```

Which statements about backward liveness hold?

**Candidates**

**I.** x is live immediately after x=1.

**II.** The value assigned by x=4 is live immediately after that assignment.

**III.** y is live immediately before x=4.

**IV.** y is live immediately before y=x+2.

A. I and II  
B. I and IV  
C. I and III  
D. II and III  

### Q46. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A combinational block has Boolean inputs a,b,c and outputs s=a XOR b XOR c and k=ab OR ac OR bc. Which statements hold?

**Candidates**

**I.** The numerical sum a+b+c equals s+2k.

**II.** k is 1 exactly when all three inputs are 1.

**III.** Complementing all three inputs complements s and complements k.

**IV.** Distinct input triples always produce distinct output pairs (s,k).

A. I and IV  
B. II and III  
C. II and IV  
D. I and III  

### Q47. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Transaction T1 locks every existing row satisfying salary>100 and counts those rows twice. Between the counts, T2 inserts and commits a new row with salary150. The system uses only row locks on existing rows; no predicate or range locks are acquired. Which statements hold?

A. T1's locks need not prevent T2's insertion.  
B. The second count can exceed the first despite locking all originally qualifying rows.  
C. Locking existing rows necessarily locks every future row satisfying the same predicate.  
D. A suitable predicate lock can prevent the insertion until T1 releases it.  

### Q48. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Relation R(A,B,C) has exactly the functional dependencies implied by AB→C and C→B. Assuming atomic attribute values, which classification is correct?

A. R is in BCNF because every attribute belongs to a key.  
B. R is in3NF but not BCNF.  
C. R violates2NF because C→B has a single-attribute determinant.  
D. A alone is a candidate key.  

### Q49. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A pattern consists of four distinctly labelled points at coordinates P=(0,0), Q=(2,0), R=(0,1), S=(1,1). First reflect it in the line x=y; then rotate it clockwise through 90 degrees about the origin. Which single transformation gives the same final positions for all four labels?

A. Reflection in the x-axis.  
B. Reflection in the y-axis.  
C. Rotation through 180 degrees about the origin.  
D. Translation by (1,−1).  

### Q50. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Let L={ww : w∈{a,b}*}, a non-context-free language. Define the homomorphism h by h(a)=h(b)=0. Which statements are correct?

**Candidates**

**I.** h(L) consists of all even-length words over {0}.

**II.** h(L) is regular.

**III.** Non-context-freeness of L implies non-context-freeness of h(L).

**IV.** The word 000 belongs to h(L).

A. I and III  
B. I and IV  
C. II and III  
D. I and II  

---

## ANSWER KEY — SET 008

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MSQ | 1 | B, C, D |
| 2 | MCQ | 2 | D |
| 3 | MSQ | 2 | A, C, D |
| 4 | MSQ | 2 | B, C, D |
| 5 | MSQ | 1 | A, B, D |
| 6 | MSQ | 2 | A, B, C |
| 7 | MSQ | 2 | B, D |
| 8 | MSQ | 2 | A, B, D |
| 9 | MSQ | 1 | B, C, D |
| 10 | MSQ | 2 | A, C, D |
| 11 | MSQ | 1 | A, C, D |
| 12 | MSQ | 1 | A, B, D |
| 13 | MSQ | 2 | A, C, D |
| 14 | MSQ | 1 | B, C, D |
| 15 | MCQ | 1 | D |
| 16 | MSQ | 2 | A, B, D |
| 17 | MSQ | 2 | A, C, D |
| 18 | MCQ | 1 | D |
| 19 | MSQ | 1 | B, C, D |
| 20 | MSQ | 2 | A, C, D |
| 21 | MCQ | 2 | C |
| 22 | MSQ | 1 | A, C, D |
| 23 | MSQ | 1 | B, C, D |
| 24 | MSQ | 2 | A, C, D |
| 25 | MSQ | 2 | A, C, D |
| 26 | MCQ | 1 | D |
| 27 | MSQ | 1 | A, C, D |
| 28 | MCQ | 2 | B |
| 29 | MCQ | 2 | B |
| 30 | MSQ | 1 | A, B, D |
| 31 | MSQ | 1 | B, C, D |
| 32 | MCQ | 2 | B |
| 33 | MCQ | 2 | D |
| 34 | MCQ | 1 | D |
| 35 | MSQ | 1 | A, C, D |
| 36 | MCQ | 1 | B |
| 37 | MCQ | 2 | C |
| 38 | MCQ | 2 | D |
| 39 | MSQ | 2 | A, C, D |
| 40 | MCQ | 2 | B |
| 41 | MCQ | 1 | C |
| 42 | MCQ | 1 | B |
| 43 | MSQ | 1 | B, C, D |
| 44 | MCQ | 2 | B |
| 45 | MCQ | 1 | C |
| 46 | MCQ | 1 | D |
| 47 | MCQ | 1 | C |
| 48 | MSQ | 1 | A, C, D |
| 49 | MSQ | 2 | B, C, D |
| 50 | MCQ | 2 | D |
