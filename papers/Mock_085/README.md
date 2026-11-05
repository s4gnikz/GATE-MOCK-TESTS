# GATE CS 2027 — Full-Length Mock Test 085

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

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A narrative says: “The team archived the original readings before recalibrating the instrument. It then repeated the measurements. Only after this repetition did it compare the two sets of readings.” Which event necessarily happened immediately before the comparison among the three later events mentioned?

**Candidate answers**
I. Archiving the original readings
II. Repeating the measurements
III. Recalibrating the instrument
IV. Discarding the original readings

A. I: valid; II: valid; III: invalid; IV: invalid  
B. I: invalid; II: valid; III: valid; IV: invalid  
C. I: valid; II: invalid; III: valid; IV: valid  
D. I: invalid; II: valid; III: invalid; IV: invalid

### Q2. [1 Mark] [NAT]

A bag contains one red and three blue balls. They are drawn without replacement until the red ball appears. What is the expected total number of draws, including the red ball?

**Answer format:** Exact decimal.

### Q3. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“The proposed change is reversible: the previous configuration can be restored.” Which meaning of reversible applies?

A. Impossible to undo.  
B. Capable of being undone.  
C. Required to happen twice.  
D. Unrelated to the previous configuration.

### Q4. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

How many integers x with1≤x≤1000 satisfy floor(log2 x)=floor(log3 x)? Here floor denotes the greatest integer not exceeding its argument.

**Required precision:** Exact integer.

A. 2  
B. 4  
C. 1  
D. 3

### Q5. [1 Mark] [MSQ]

An engineer tests a device at every integer temperature from 0°C through 100°C. It operates correctly in all tests. No rule governing its behaviour between tested temperatures is known. Which statements are justified solely by these observations?

A. The device operates correctly at 37°C under the tested conditions.
B. The device must operate correctly at 37.5°C.
C. The observations are compatible with a device that fails at 37.5°C.
D. The device must operate correctly at every integer temperature above 100°C.

### Q6. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Unit cubes are stacked in four columns on a2×2 base. A column may have height0,1,or2. The maximum heights seen in the two rows are respectively2 and1; the maximum heights seen in the two columns are respectively2 and1. Rows and columns have fixed labels. How many different height arrays satisfy these four maxima?

**Required precision:** Integer.

A. 5  
B. 10  
C. 3  
D. 6

### Q7. [2 Marks] [NAT]

A sequence satisfies a1=2 and a(n+1)=2a(n)+1 for n≥1. What is the sum of its first four terms?

**Answer format:** Integer.

### Q8. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A rectangular garden is 40 m by 30 m. A path of uniform width runs just inside all four boundaries, leaving a rectangular planted region. If the path occupies 264 m², find its width, which is less than 15 m.

**Required precision:** Integer metres.

A. 4  
B. 1  
C. 3  
D. 2

### Q9. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Five presentations P,Q,R,S,T occupy five consecutive slots, one per slot. Q occurs immediately after P. R occurs before P, and S occurs after Q. How many schedules satisfy these restrictions?

A. 2  
B. 4  
C. 6  
D. 8

### Q10. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A retailer marks an item25% above cost and gives a discount of d% on the marked price. The final profit is5% of cost. What is d?

**Required precision:** Exact percentage number.

A. 16  
B. 32  
C. 8  
D. 17

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A BFS from s runs on an undirected graph with edges sa, sb, ac, ad, be, and ce. Vertices are marked when enqueued. Which discovery order is impossible, regardless of adjacency-list ordering?

**Candidate answers**
I. s,a,b,c,d,e
II. s,b,a,e,c,d
III. s,a,b,c,e,d
IV. s,a,b,d,c,e

A. I: invalid; II: invalid; III: valid; IV: invalid  
B. I: valid; II: invalid; III: valid; IV: invalid  
C. I: invalid; II: invalid; III: invalid; IV: invalid  
D. I: valid; II: valid; III: invalid; IV: valid

### Q12. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Under strict two-phase locking, exclusive locks are retained until commit or abort. Which statements are correct?

**Candidates**

**I.** Another transaction cannot read an item modified under an unreleased exclusive lock.

**II.** Retaining exclusive locks prevents cascading aborts caused by reading those uncommitted writes.

**III.** The rule alone makes deadlock impossible.

**IV.** A transaction may release an exclusive lock immediately after its write under this strict rule.

A. I and III  
B. I and IV  
C. I and II  
D. II and III

### Q13. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

An HTTP client first opens a new TCP connection and obtains a base HTML document. It then opens exactly three new TCP connections in parallel for six images, requesting one image per connection at a time and reusing each connection for its second image. There is no pipelining. Each TCP handshake takes one RTT, and each request-response takes one RTT. RTT is 40 ms for every connection. Ignore DNS, transmission time, TLS and processing. What is the minimum time from starting the HTML connection until all images arrive, in milliseconds?

**Required precision:** Integer.

A. 400  
B. 100  
C. 201  
D. 200

### Q14. [1 Mark] [NAT]

A min-heap stores distinct keys in a one-based array of length15. A particular key's array index is known to be6. Ignoring its own position, how many other array positions are guaranteed to contain larger keys solely because of the heap-order property?

**Answer format:** Integer.

### Q15. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

On set{1,2,3,4}, define xRy exactly when floor(x/2)=floor(y/2). How many ordered pairs belong to R?

**Required precision:** Integer.

A. 12  
B. 3  
C. 7  
D. 6

### Q16. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A compiler removes an assignment to scalar x as dead code. The right-hand side has no side effects, exceptions, or observable traps. Which conditions support removal?

**Candidate answers**
I. On every outgoing path, x is redefined before its current value is read, or execution ends without reading it.
II. x is read on at least one outgoing path before redefinition.
III. x is not live immediately after the assignment.
IV. x has a short variable name.

A. I: invalid; II: invalid; III: valid; IV: invalid  
B. I: valid; II: invalid; III: valid; IV: invalid  
C. I: valid; II: invalid; III: invalid; IV: invalid  
D. I: invalid; II: valid; III: invalid; IV: valid

### Q17. [1 Mark] [NAT]

A real matrix has rows (0,−2),(1,3). Find the trace of its inverse.

**Answer format:** Exact finite decimal.

### Q18. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A programming language specifies that every evaluation of a volatile memory read is observable, even if the returned values happen to be equal. For two successive expressions x=read_volatile(p) and y=read_volatile(p), which statements are correct?

**Candidates**

**I.** Equal returned values alone justify replacing the second read by y=x.

**II.** Such replacement removes an observable operation.

**III.** Ordinary expression-value equality is insufficient for this optimization.

**IV.** Volatile reads are guaranteed never to return equal values.

A. I and III  
B. I and IV  
C. II and IV  
D. II and III

### Q19. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A differentiable function f on[0,2] has f(0)=1 and f(2)=7, and f'(x)≤3 everywhere on(0,2). What is f(1)?

**Required precision:** Exact integer.

A. 8  
B. 2  
C. 5  
D. 4

### Q20. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Starting with one process, the following code executes. Every fork succeeds, returns 0 only in its new child, and returns a positive child identifier in its parent. Every process reaches the final line once. How many processes execute work()?

```c
int p = fork();
if (p == 0) fork();
fork();
work();
```

**Required precision:** Integer.

A. 12  
B. 3  
C. 7  
D. 6

### Q21. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A tabular minimization pattern `1-0--` has five bit positions. How many minterms does it represent?

**Required precision:** Integer.

A. 8  
B. 16  
C. 4  
D. 9

### Q22. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A directed graph on vertices 0–3 is stored in CSR form with row pointers [0,2,2,5,6] and column indices [1,3,0,2,3,1]. Outgoing neighbours of vertex i occupy indices row[i] through row[i+1]−1. What is the minimum number of directed edges that must be added to make the graph strongly connected?

**Required precision:** Integer.

A. 1  
B. 2  
C. 0  
D. 3

### Q23. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Two threads each execute the following two-iteration loop on shared x, initially 0. Each read and write is atomic, the computation uses a private register r, and execution is a sequentially consistent interleaving preserving each thread's order.

```text
repeat twice:
    r = x
    x = r + 1
```

Which values of x are possible after both threads finish?

A. 1  
B. 2  
C. 3  
D. 4

### Q24. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A cache stores64 data bytes in four-byte blocks and is four-way set associative. How many sets does it contain?

**Required precision:** Integer.

A. 8  
B. 2  
C. 4  
D. 5

### Q25. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A 4-to-1 multiplexer has select bits A,B, with A more significant. Its data inputs for select values 00,01,10,11 are C, NOT C, 1,0 respectively. Minterms are numbered using A,B,C with A most significant. Which set is the output's on-set?

**Candidate answers**
I. {0,3,4,5}
II. {1,2,4,5}
III. {1,2,6,7}
IV. {0,1,2,5}

A. I: valid; II: valid; III: invalid; IV: invalid  
B. I: invalid; II: valid; III: valid; IV: invalid  
C. I: invalid; II: valid; III: invalid; IV: invalid  
D. I: valid; II: invalid; III: valid; IV: valid

### Q26. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Consider L={aⁿbᵐ:n,m≥0 and n≠m}. For an arbitrary positive proposed regular pumping length p, choose w=aᵖb^(p+p!). Every valid split w=xyz with |xy|≤p and |y|>0 has y=aᵏ for some 1≤k≤p. Which pumping exponent i makes xy^i z have equal a and b counts and therefore leave L?

A. i=p!  
B. i=1+p!/k  
C. i=1−p!/k  
D. i=k+1

### Q27. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Recognizers M and N recognize L and its complement respectively. How can they be used to decide L on input w?

A. Run M to completion before starting N.  
B. Accept whenever either machine accepts.  
C. Interleave their steps; accept if M accepts and reject if N accepts.  
D. Reject immediately unless M accepts in its first step.

### Q28. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A connected undirected graph has four vertices and every edge has weight 7. How much does any minimum spanning tree weigh?

**Required precision:** Integer.

A. 42  
B. 21  
C. 11  
D. 22

### Q29. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

An ER relationship between three distinct entities in set A and four distinct entities in set B is many-to-many, with total participation on both sides. Relationship instances are sets of distinct pairs from A×B. How many different relationship instances have exactly four pairs?

**Required precision:** Exact integer.

A. 36  
B. 72  
C. 18  
D. 37

### Q30. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Use set semantics. R(A,B)={(1,x),(1,y),(2,x)} and S(B)={(x),(y)}. Define

`E = projection_A(R) - projection_A((projection_A(R) x S) - R)`

where x is Cartesian product and - is set difference. Which statements are correct? Each proposed change is applied independently to the original relations.

A. For the original relations, E={(1)}.  
B. If S is empty, E={(1),(2)}.  
C. If (2,y) is added to R, E remains {(1)}.  
D. If (z) is added to S, E is empty.

### Q31. [1 Mark] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

P(B)=0.5, P(A|B)=0.6 and P(A|not B)=0.2. Find P(B|A).

**Required precision:** Exact finite decimal.

A. 0.25  
B. 0.75  
C. 0.38  
D. 0.88

### Q32. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A virtually indexed, physically tagged cache has 32 KiB data capacity and 64-byte lines. Pages are 4 KiB. To keep every set-index bit within the page offset, what is the minimum power-of-two associativity? Ignore all metadata and use conventional contiguous offset/index fields.

**Required precision:** Integer number of ways.

A. 16  
B. 4  
C. 8  
D. 9

### Q33. [1 Mark] [NAT]

Let A={1,2} and B={1,2,3,4,5}. Consider the set of all X satisfying A⊆X⊆B, ordered by inclusion. How many ordered pairs (X,Y) satisfy X∩Y=A and X∪Y=B?

**Answer format:** Integer.

### Q34. [1 Mark] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A directed weighted graph has edges s→a(1), a→a(−1), s→t(5), and no others. Distances refer to walks, which may repeat vertices. Which statements are correct?

**Candidate answers**
I. There is a finite shortest-walk distance from s to t, equal to5.
II. Every vertex reachable from s has a finite shortest-walk distance.
III. A negative cycle reachable from s need not make the s-to-t distance unbounded below.
IV. The negative self-loop can be inserted into a walk from s to t.

A. I: valid; II: invalid; III: valid; IV: invalid  
B. I: invalid; II: invalid; III: valid; IV: invalid  
C. I: valid; II: invalid; III: invalid; IV: invalid  
D. I: invalid; II: valid; III: invalid; IV: valid

### Q35. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A router forwards an IPv4 datagram from one Ethernet link to another. Assume no tunnelling or network address translation. Which pair of fields is necessarily replaced with values appropriate to the outgoing link?

A. Source and destination IPv4 addresses  
B. Source and destination TCP port numbers  
C. Ethernet source and destination MAC addresses  
D. Application sequence numbers

### Q36. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

For a binary input string, prepend zeroes if needed to obtain at least three bits. Accept exactly when the last three bits of this padded string have even parity; thus the empty string is accepted. What is the minimum number of states of a complete DFA recognizing this language?

**Required precision:** Integer.

A. 8  
B. 16  
C. 4  
D. 9

### Q37. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A comparison-based search probes a sorted array of15 distinct keys by repeatedly choosing the middle of the remaining interval. What is the maximum number of key comparisons for a successful search?

**Required precision:** Integer.

A. 4  
B. 8  
C. 2  
D. 5

### Q38. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Two processes communicate over two initially empty FIFO channels of capacity one message each. Sending blocks when the destination channel is full; receiving blocks when it is empty. P executes send(a),send(b),receive(x), while Q executes send(c),receive(y),receive(z). P's sends go to Q and Q's send goes to P. Both run fairly, and local computation takes no time. How many messages can remain queued when both processes finish?

**Required precision:** Exact integer.

A. 1  
B. 2  
C. 0  
D. 3

### Q39. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A synchronous machine has two different states that produce the same output now. Which statements are correct about state minimization?

**Candidate answers**
I. Equal current outputs alone guarantee equivalence.
II. A future input sequence yielding different output sequences distinguishes the states.
III. Equivalent states must have equivalent successors for every input under the usual deterministic Moore-machine definition.
IV. Different state encodings alone guarantee distinguishability by external observations.

A. I: valid; II: valid; III: valid; IV: invalid  
B. I: invalid; II: valid; III: invalid; IV: invalid  
C. I: invalid; II: valid; III: valid; IV: invalid  
D. I: valid; II: invalid; III: invalid; IV: valid

### Q40. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For a finite relation R(x,y), consider the formula R(x,y) AND NOT exists z(R(x,z) AND z≠y), with x,y free. Which statements are correct?

**Candidates**

**I.** It selects tuples whose x value has exactly one distinct associated y value in R.

**II.** It rejects every tuple whenever R contains two different x values.

**III.** The existential variable z ranges over possible competing y values for the same x.

**IV.** It can return an(x,y) pair not in R.

A. II and IV  
B. I and III  
C. III and IV  
D. I and II

### Q41. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

For the grammar S→ABc, A→a | ε, B→AD | b, D→d | ε, with start S, how many distinct terminal symbols belong to FOLLOW(A)? The end marker is not a terminal symbol.

**Required precision:** Integer.

A. 8  
B. 2  
C. 4  
D. 5

### Q42. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An input describes a Turing machine M over {0,1}, with the promise that M halts on every input string. Algorithms below need only behave correctly on machines satisfying the promise. Which statements are correct?

**Candidates**

**I.** Nonemptiness of L(M) is semidecidable by testing strings and eventually accepting whenever an accepted string exists.

**II.** Emptiness of L(M) is decidable solely because every individual simulation halts.

**III.** Equivalence of L(M) to the empty language is decidable under this promise.

**IV.** Whether M accepts at least one string of length at most ten is decidable.

A. I and III  
B. I and IV  
C. II and III  
D. II and IV

### Q43. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

A 0/1 knapsack has capacity 8 and five distinct items with (weight,value): A=(2,3), B=(2,3), C=(3,4), D=(3,4), E=(4,5). Each may be selected at most once. How many distinct subsets attain the maximum possible value without exceeding capacity? Subsets differing only by A versus B or C versus D still count as distinct.

**Required precision:** Integer.

A. 6  
B. 2  
C. 4  
D. 3

### Q44. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

Routers have converged exact shortest distances d(v) to destination t. Each router v≠t selects a next hop u satisfying d(v)=w(v,u)+d(u). All relevant distances are finite. Which statements are correct?

**Candidate answers**
I. If all link costs are strictly positive, the selected next-hop graph cannot contain a directed cycle.
II. If zero-cost links are allowed, independent tie choices can create a forwarding cycle despite correct distances.
III. Correct distances alone prevent forwarding cycles for every set of nonnegative link costs.
IV. With positive costs, distance strictly decreases at every selected hop.

A. I: valid; II: valid; III: invalid; IV: valid  
B. I: invalid; II: valid; III: invalid; IV: valid  
C. I: valid; II: valid; III: valid; IV: valid  
D. I: invalid; II: invalid; III: valid; IV: invalid

### Q45. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

An initially empty five-stage IF-ID-EX-MEM-WB pipeline issues at most one instruction per cycle. Without stalls, N retired instructions take N+4 cycles. Full forwarding leaves exactly one stall cycle for an immediately dependent load-use pair. A taken branch incurs exactly two additional cycles, with no other penalties. A path retires, in order, a load, an ALU instruction using that load, a taken branch depending on that ALU result, and a target ALU instruction. ALU-to-branch forwarding avoids any additional data stall. How many cycles elapse through the final instruction's WB?

**Required precision:** Exact integer.

A. 22  
B. 6  
C. 11  
D. 12

### Q46. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For grammar S→aSb | T and T→cT | ε, which statements are true?

A. Every generated word has equally many a and b symbols.  
B. Every generated word has all c symbols between its a and b blocks.  
C. The grammar generates abcc.  
D. The grammar generates aacbb.

### Q47. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

A system has two resource types A and B. It uses the Banker's safety test. Current allocation and maximum claims are:

| Process | Allocation (A,B) | Maximum (A,B) |
|---|---|---|
| P0 | (1,0) | (2,2) |
| P1 | (0,1) | (1,2) |
| P2 | (1,1) | (3,1) |

The available vector is (1,1). P0 requests (0,1). The request is within its remaining claim and the available resources. Which conclusion is correct?

**Candidate answers**
I. Grant it: P0,P1,P2 is a safe sequence afterward.
II. Grant it: P2,P1,P0 is a safe sequence afterward.
III. Defer it: the present state is safe, but the tentative grant is unsafe.
IV. Defer it: the present state is already unsafe.

A. I: valid; II: invalid; III: valid; IV: invalid  
B. I: invalid; II: invalid; III: valid; IV: invalid  
C. I: invalid; II: invalid; III: invalid; IV: invalid  
D. I: valid; II: valid; III: invalid; IV: valid

### Q48. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Five distinguishable bins each hold at most two identical tokens. In how many ways can exactly five tokens be distributed among the bins?

**Required precision:** Integer.

A. 102  
B. 26  
C. 52  
D. 51

### Q49. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

Over GF(2), a CRC generator is g(x)=x³+x+1. The transmitted codeword suffers error polynomial e(x)=x^k g(x), for some k≥0 that fits within the transmitted frame. Which statements are correct?

**Candidate answers**
I. The CRC remainder of the error polynomial is zero.
II. This nonzero error can escape detection.
III. Multiplication by x^k guarantees detection of every nonzero polynomial.
IV. The error polynomial must be a single-bit error.

A. I: invalid; II: valid; III: invalid; IV: invalid  
B. I: valid; II: valid; III: invalid; IV: invalid  
C. I: valid; II: valid; III: valid; IV: invalid  
D. I: invalid; II: invalid; III: valid; IV: valid

### Q50. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A lexer has the token rules `a`, `b`, `d`, and `ab*c`, where `b*` means zero or more b symbols. It uses longest match. An implementation reads forward until no token rule can still match, then returns to the most recent accepting position to emit that token. Consider the inputs `ab^n d`, with no spaces and arbitrary integer n>=1. Before returning the first token, how much lookahead beyond the most recent accepting position can this implementation require?

A. At most one character, independently of n.  
B. At most two characters, independently of n.  
C. An amount unbounded as n grows.  
D. Zero, because the rule `a` can be emitted immediately upon reading a.

### Q51. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

D(id) contains 1 and 2. E(eid,did,active) contains (10,1,0) and (11,1,1); all columns are non-NULL. Consider this SQL query:

```sql
SELECT D.id, COUNT(*) AS n, COUNT(E.eid) AS m
FROM D LEFT JOIN E
  ON D.id = E.did AND E.active = 1
GROUP BY D.id;
```

Which statements are correct?

**Candidates**

**I.** The row for id=1 has n=1 and m=1.

**II.** The row for id=2 has n=1 and m=0.

**III.** Moving E.active=1 from ON to WHERE necessarily preserves the result.

**IV.** The row for id=2 has n=0 and m=0.

A. I and III  
B. I and II  
C. I and IV  
D. II and III

### Q52. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

In an idealized CSMA/CD network, the farthest stations have a one-way propagation time of12 microseconds. A100-Mbit/s transmitter must still be transmitting at the latest possible collision-detection instant. Ignoring all encoding overhead and assuming a collision can occur just before a distant station first senses the transmission, what is the minimum frame length in bytes?

**Required precision:** Integer.

A. 600  
B. 150  
C. 301  
D. 300

### Q53. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Keys 40,20,60,10,30,50,70,25,35 are inserted in that order into an initially empty ordinary BST. Delete 20 by replacing its key with its inorder predecessor and physically removing that predecessor's original node. Then delete 40 by replacing its key with its inorder successor and physically removing that successor's original node. What is the key at the lowest common ancestor of 25 and 70 in the resulting tree?

**Required precision:** Integer key.

A. 50  
B. 100  
C. 25  
D. 51

### Q54. [2 Marks] [NAT]

A continuously differentiable function f on[0,2] satisfies f(2)=4 and the integral of f(x) over[0,2] equals3. What is the integral of x f'(x) over[0,2]?

**Answer format:** Exact number.

### Q55. [2 Marks] [NAT]

A stack machine stores four-byte integers. PUSH first subtracts4 from SP, then writes at the new SP. POP reads at SP, then adds4 to SP. Initially SP=100. Execute PUSH7, PUSH9, POP into R, then store R at address SP+4, then POP into S. What is R+S? The stack is ordinary writable memory and all addresses are valid.

**Answer format:** Integer.

### Q56. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

An8-bit two's-complement ALU computes the expression (x+y)−y, wrapping after each operation. For x=100 and y=60, count how many of the two operations signal signed overflow. The overflow flag is recomputed separately for each operation.

**Required precision:** Integer.

A. 4  
B. 1  
C. 2  
D. 3

### Q57. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

Relation Child(cid,pid) has primary key cid and a foreign key pid referencing Parent(pid), whose primary key is pid. Child.pid is nullable and referential integrity uses ordinary SQL semantics without additional restrictions. Which statements are correct?

**Candidate answers**
I. Two Child rows with different cid values may reference the same parent.
II. A non-NULL Child.pid must match a Parent.pid.
III. Every parent must be referenced by at least one child.
IV. Child.pid must be unique because it is a foreign key.

A. I: invalid; II: valid; III: invalid; IV: invalid  
B. I: valid; II: valid; III: valid; IV: invalid  
C. I: valid; II: valid; III: invalid; IV: invalid  
D. I: invalid; II: invalid; III: valid; IV: valid

### Q58. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

For grammar S→AB, A→aA | ε, B→bBc | ε, with start symbol S and end marker $, which statements are correct?

**Candidate answers**
I. The grammar is LL(1).
II. c belongs to FOLLOW(A).
III. FOLLOW(B)={c,$}.
IV. The production A→ε must be selected on lookahead a in an LL(1) table.

A. I: valid; II: invalid; III: valid; IV: invalid  
B. I: invalid; II: invalid; III: valid; IV: invalid  
C. I: valid; II: invalid; III: invalid; IV: invalid  
D. I: invalid; II: valid; III: invalid; IV: valid

### Q59. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A syntax-directed translation uses the grammar E→E−T | T and T→digit. The semantic rules are E→E1−T: E.val=E1.val−T.val; E→T: E.val=T.val; T→digit: T.val=the digit's value. For the input9−4−2, a second implementation incorrectly rewrites the grammar to right recursion E→T−E | T and uses ordinary subtraction of the child values. What is the correct implementation's value minus the second implementation's value?

**Required precision:** Integer, possibly negative.

A. -8  
B. -2  
C. -3  
D. -4

### Q60. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

Six observations are3,3,3,7,7,7. Replace exactly one observation by any real number, keeping the other five fixed. The median of six observations is the average of the third and fourth values in sorted order. What is the largest possible increase in the median?

**Required precision:** Exact number.

A. 4  
B. 1  
C. 3  
D. 2

### Q61. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

Procedure F(n), for n≥0, returns immediately when n≤1. Otherwise it calls F(n−1), then F(n−2), with no memoization. Count only calls with n=0. How many such calls occur during F(6)?

**Required precision:** Integer.

A. 10  
B. 3  
C. 5  
D. 6

### Q62. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A toy floating-point format has four significant binary bits and round-to-nearest, ties-to-even. It supports all exponents needed below. Which real values round to exactly1.5?

A. 1.4375  
B. 1.49  
C. 1.5625  
D. 1.625

### Q63. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Over alphabet {a,b}, let L={a,ab}. A pushdown automaton starts with one bottom-of-stack symbol. For empty-stack acceptance, a string is accepted only if all input has been consumed and the stack is empty; no transition is possible once the stack is empty. No right-end marker is supplied. Standard determinism forbids a choice between an epsilon transition and an input-consuming transition for the same state and stack top. Which machine model cannot recognize L?

A. A deterministic finite automaton.  
B. A nondeterministic pushdown automaton accepting by empty stack.  
C. A deterministic pushdown automaton accepting by final state.  
D. A deterministic pushdown automaton accepting by empty stack.

### Q64. [2 Marks] [MSQ]

Select ALL options that are NOT valid numerical answers to the following problem. Exactly three options must be selected.

How many subgroups of the permutation group S3 are abelian? Include the trivial subgroup and count distinct subgroups, not isomorphism types.

**Required precision:** Integer.

A. 10  
B. 3  
C. 5  
D. 6

### Q65. [2 Marks] [MCQ]

Evaluate the problem and its four candidate answers below. A candidate is valid if it correctly answers the embedded problem (for a multiple-answer problem, judge each candidate individually). Which option gives the correct validity audit of ALL four candidates?

**Problem**

What is the asymptotic number of executions of work()?

```text
for i = 1 to n:
    j = 1
    while j <= i:
        for k = 1 to j:
            work()
        j = 2*j
```

**Candidate answers**
I. Θ(n log n)
II. Θ(n²)
III. Θ(n² log n)
IV. Θ(log² n)

A. I: valid; II: valid; III: invalid; IV: invalid  
B. I: invalid; II: valid; III: valid; IV: invalid  
C. I: valid; II: invalid; III: valid; IV: valid  
D. I: invalid; II: valid; III: invalid; IV: invalid

## ANSWER KEY — MOCK TEST 085

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | D |
| 2 | NAT | 1 | 2.5 |
| 3 | MSQ | 1 | A, C, D |
| 4 | MCQ | 1 | A |
| 5 | MSQ | 1 | A, C |
| 6 | MSQ | 2 | B, C, D |
| 7 | NAT | 2 | 41 |
| 8 | MSQ | 2 | A, B, C |
| 9 | MSQ | 2 | A, C, D |
| 10 | MCQ | 2 | A |
| 11 | MCQ | 1 | A |
| 12 | MCQ | 1 | C |
| 13 | MSQ | 1 | A, B, C |
| 14 | NAT | 1 | 2 |
| 15 | MCQ | 1 | D |
| 16 | MCQ | 1 | B |
| 17 | NAT | 1 | 1.5 |
| 18 | MCQ | 1 | D |
| 19 | MSQ | 1 | A, B, C |
| 20 | MCQ | 1 | D |
| 21 | MCQ | 1 | A |
| 22 | MSQ | 1 | B, C, D |
| 23 | MCQ | 1 | A |
| 24 | MSQ | 1 | A, B, D |
| 25 | MCQ | 1 | C |
| 26 | MSQ | 1 | A, C, D |
| 27 | MSQ | 1 | A, B, D |
| 28 | MCQ | 1 | B |
| 29 | MCQ | 1 | A |
| 30 | MCQ | 1 | C |
| 31 | MSQ | 1 | A, C, D |
| 32 | MCQ | 1 | C |
| 33 | NAT | 1 | 8 |
| 34 | MCQ | 1 | A |
| 35 | MSQ | 1 | A, B, D |
| 36 | MSQ | 2 | B, C, D |
| 37 | MCQ | 2 | A |
| 38 | MCQ | 2 | C |
| 39 | MCQ | 2 | C |
| 40 | MCQ | 2 | B |
| 41 | MSQ | 2 | A, B, D |
| 42 | MCQ | 2 | B |
| 43 | MSQ | 2 | A, B, C |
| 44 | MCQ | 2 | A |
| 45 | MCQ | 2 | C |
| 46 | MCQ | 2 | C |
| 47 | MCQ | 2 | B |
| 48 | MCQ | 2 | D |
| 49 | MCQ | 2 | B |
| 50 | MSQ | 2 | A, B, D |
| 51 | MCQ | 2 | B |
| 52 | MSQ | 2 | A, B, C |
| 53 | MCQ | 2 | A |
| 54 | NAT | 2 | 5 |
| 55 | NAT | 2 | 16 |
| 56 | MCQ | 2 | C |
| 57 | MCQ | 2 | C |
| 58 | MCQ | 2 | A |
| 59 | MCQ | 2 | D |
| 60 | MCQ | 2 | D |
| 61 | MSQ | 2 | A, B, D |
| 62 | MCQ | 2 | D |
| 63 | MSQ | 2 | A, B, C |
| 64 | MSQ | 2 | A, B, D |
| 65 | MCQ | 2 | D |
