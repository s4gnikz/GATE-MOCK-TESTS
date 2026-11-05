# GATE CS — Additional Practice Set 004

**Questions:** 50  
**Maximum marks:** 80

Read the task above each embedded question carefully. For an invalid-answer task, select options that do not correctly answer the embedded question. For a pair task, select the pair containing all valid candidates. MCQ has one correct choice; MSQ requires all correct choices. The answer key follows Q50.

### Q1. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Seven distinct people A, B, C, D, E, F and G sit around a circular table. A and B must sit next to each other. Neither C and D nor E and F may sit next to each other. Rotations of an arrangement are identical; reflections are different. How many arrangements are possible?

A. 96  
B. 120  
C. 144  
D. 240  

### Q2. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A four-input Boolean function F(a,b,c,d) equals 1 exactly when at least three inputs are 1. It is implemented using a 4-to-1 multiplexer whose select bits are b (more significant) and c (less significant). Data inputs I0, I1, I2, I3 correspond respectively to bc = 00, 01, 10, 11. Which tuple of data-input functions implements F? Here juxtaposition means AND and + means OR.

A. (0, ad, ad, a+d)  
B. (0, a+d, a+d, ad)  
C. (ad, ad, ad, 1)  
D. (0, 0, 0, a+d)  

### Q3. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A rectangular garden is 16 m long and 10 m wide. A path of uniform width is laid inside all four edges, leaving a smaller rectangular planted region. The path occupies 88 square metres. What is the width of the path?

A. 1 m  
B. 2 m  
C. 3 m  
D. 4 m  

### Q4. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A simple undirected graph has vertices A,B,C,D,E,F. Each edge of triangle ABC and each edge of triangle DEF has weight 1. Edges AD, BE and CF have weight 2, and edge AE has weight 3. There are no other edges. Two spanning trees are distinct when their edge sets differ. Which statements are correct?

A. The minimum spanning-tree weight is 6.  
B. There are exactly 27 minimum spanning trees.  
C. There are exactly 45 spanning trees of weight 7.  
D. Every spanning tree of weight 7 uses exactly two weight-2 edges.  

### Q5. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A microprogram must start one memory read at the address in MAR, wait until READY=1, copy the returned data into MDR, and increment register R exactly once. All microinstruction operations execute once on every cycle in which that microinstruction is visited. A START pulse begins a transaction; issuing START again before completion begins an unwanted second transaction. READY remains 0 until the transaction completes and then remains 1 until the routine exits. Which routine meets the requirements for every finite memory latency? A branch tests READY at the end of its cycle.

A. U: START; R=R+1; if READY=0 goto U else goto V. V: MDR=DATA; exit.  
B. U: START; goto V. V: if READY=0 goto V else goto W. W: MDR=DATA; R=R+1; exit.  
C. U: START; goto V. V: R=R+1; if READY=0 goto V else goto W. W: MDR=DATA; exit.  
D. U: START; MDR=DATA; R=R+1; exit.  

### Q6. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A circular singly linked list has traversal 1→2→3→4→1, and tail points to node 4. Execute tail.next=tail.next.next. Then insert a new node 5 immediately after tail and set tail to this new node. What traversal starts at the new head tail.next?

A. 1,2,3,4,5  
B. 5,2,3,4  
C. 2,3,4,5  
D. 2,3,5,4  

### Q7. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Choose the words completing both blanks in standard formal English: “The number of reports that ___ missing ___ now smaller.”

A. is; are  
B. are; are  
C. are; is  
D. is; is  

### Q8. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A lexer recognizes the keyword if, identifiers consisting of a letter followed by letters or digits, double-quoted string literals, and C-style /*...*/ comments. It uses longest match and gives a keyword priority over an identifier in an equal-length tie. Whitespace and comments are discarded. How many keyword tokens and total tokens, respectively, result from this input?

```text
"if" if /*if*/ if2
```

A. (3,4)  
B. (2,3)  
C. (1,4)  
D. (1,3)  

### Q9. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A report states: “Every approved application was received before the deadline. Several applications received before the deadline were rejected.” Which inference is justified?

A. Receiving an application before the deadline guarantees approval.  
B. Every rejected application arrived after the deadline.  
C. No application was approved.  
D. Timely receipt was necessary but not sufficient for approval in this set of applications.  

### Q10. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A machine has a 1 ns clock, ideal CPI=1, and no overlapping stalls. Conditional branches are 20% of instructions. A static predictor predicts not taken; 60% of branches are taken, and each misprediction costs three additional cycles. A new predictor mispredicts 10% of all branches but requires a 1.1 ns clock; all other CPI contributions stay unchanged. Approximately what is the new processor's speedup over the old one on the same instruction stream?

A. 0.857  
B. 1.166  
C. 1.283  
D. 1.360  

### Q11. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let L={aⁿbⁿ:n≥0}. Which of the following is regular?

A. L  
B. L∩a*b*  
C. L∩a*b³  
D. {a,b}* minus L  

### Q12. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Which sentence unambiguously states that the researchers, rather than the samples, were exhausted when they repeated the experiment?

A. Exhausted, the experiment was repeated on the samples by the researchers.  
B. The exhausted researchers repeated the experiment on the samples.  
C. The researchers repeated the experiment on the exhausted samples.  
D. Repeated by the researchers, the exhausted experiment used the samples.  

### Q13. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A wait-die lock policy lets an older requesting transaction wait for a younger holder, but aborts a younger requester when the holder is older. Transactions T1,T2,T3 have timestamps 1,2,3, respectively (smaller is older). T2 holds x and T3 holds y. T1 requests x, then T2 requests y, then T3 requests a different item z held by T1. No locks are released before the last request. Which transaction is aborted by these requests?

A. T1 only  
B. T2 only  
C. T3 only  
D. None  

### Q14. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A full adder receives inputs x,y and carry-in c. Its sum output is x XOR y XOR c. If x=y=1, what are its sum and carry-out as functions of c?

A. (c,1)  
B. (NOT c,1)  
C. (c,c)  
D. (0,c)  

### Q15. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A rule says, “A consignment will be released only if it is inspected, unless it is exempt.” Which situation necessarily violates the rule?

A. An exempt consignment is released without inspection.  
B. A nonexempt consignment is inspected but not released.  
C. A nonexempt consignment is released without inspection.  
D. An exempt consignment is inspected before release.  

### Q16. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Real 4×4 matrices E,F satisfy E²=E, F²=F, EF=FE, rank(E)=3, and rank(F)=2. Which statements must hold?

A. rank(E−F) is either 1 or 3.  
B. trace(E+F)=5.  
C. rank(EF)=2 in every case.  
D. det(E+F) is either 0 or 2.  

### Q17. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A binary floating-point format rounds to nearest, ties to even, with three significant bits including the leading 1. Exponents can represent all values in this question. What is the rounded representation of 1.101₂?

A. 1.10₂  
B. 1.11₂  
C. 1.00₂  
D. 10.0₂  

### Q18. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Processes communicate through a bounded message queue. A send blocks when the queue is full, and a receive blocks when it is empty. Which statements are correct?

**Candidates**

**I.** A blocked sender can become eligible to proceed after a receive removes an item.

**II.** Bounded buffering alone guarantees absence of deadlock in every application using the queue.

**III.** Blocking communication can synchronize processes without busy waiting by the blocked process.

**IV.** The queue can hold arbitrarily many unreceived messages.

A. II and IV  
B. III and IV  
C. I and II  
D. I and III  

### Q19. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“A survey found that residents near parks reported more exercise. The survey did not record whether those residents had chosen their neighbourhoods because they already exercised regularly.” Which limitation is most directly identified?

A. Park proximity and exercise were measured in different units.  
B. Pre-existing exercise preferences may influence residential location, so the survey alone cannot establish the direction of causation.  
C. The survey proves that parks reduce exercise.  
D. Self-selection is impossible in residential choices.  

### Q20. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An ordinary file has two hard links and is open through one file descriptor. Both directory entries are unlinked, but the descriptor remains open. Under a file system that preserves unlinked files while open, which event permits reclaiming the file's storage, assuming no new references arise?

A. Removing only the first hard link.  
B. Closing the final open descriptor after both links have been removed.  
C. Reading the first byte through the descriptor.  
D. Merely changing the current directory.  

### Q21. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A Boolean function F(x,y,z) satisfies F(x,y,z)=F(x,y,z′) for every assignment. Which statements must hold?

**Candidates**

**I.** z is inessential: the two cofactors at z=0 and z=1 are identical.

**II.** F can be implemented by a function of x,y alone.

**III.** F must be constant.

**IV.** Every sum-of-products expression for F must contain a literal z or z′.

A. I and IV  
B. II and III  
C. I and II  
D. II and IV  

### Q22. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A network-layer service can deliver datagrams out of order and may lose them. Which responsibilities can a reliable transport protocol implement above it?

**Candidates**

**I.** Detect missing data and retransmit it.

**II.** Reassemble a delivered byte stream in order.

**III.** Guarantee that no physical link ever experiences a bit error.

**IV.** Eliminate the need to distinguish simultaneous application endpoints.

A. II and III  
B. II and IV  
C. III and IV  
D. I and II  

### Q23. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A valid password must satisfy both rules: if it contains a digit, it must contain a symbol; if it contains a symbol, it must contain at least eight characters. Which case necessarily violates these rules?

A. A seven-character password containing a digit and a symbol.  
B. An eight-character password containing neither digits nor symbols.  
C. A nine-character password containing a symbol but no digit.  
D. An eight-character password containing both a digit and a symbol.  

### Q24. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

R(A,B,C) has dependencies A→B and B→C. Decompose it into R1(A,B) and R2(B,C). Which statements are correct?

A. The decomposition is lossless with respect to the dependencies.  
B. The dependencies are preserved by enforcing them separately in R1 and R2.  
C. R itself is in BCNF under the given dependencies.  
D. Both decomposed relations are in BCNF under their projected dependencies.  

### Q25. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A DMA transfer completes while the CPU executes unrelated instructions. What mechanism can notify the CPU without requiring it to poll continuously?

A. A completion interrupt.  
B. Deleting every CPU register.  
C. Changing every virtual address to zero.  
D. Disabling the device permanently before completion.  

### Q26. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Router A reaches destination D through neighbour B at total cost 5; A also has a direct link to D of cost 8. A currently selects B as next hop. With poisoned reverse, what distance to D does A advertise to B for this selected route?

A. 5  
B. 8  
C. Infinity  
D. The cost of A's link to B only  

### Q27. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A function f is continuously differentiable on [0,1], with f(0)=0, f(1/2)=2 and f(1)=1. Which statements must hold?

A. f′ equals 4 somewhere in (0,1/2).  
B. f′ is positive throughout (0,1).  
C. f′ equals −2 somewhere in (1/2,1).  
D. f′ equals zero somewhere in (0,1).  

### Q28. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For a Turing machine started on a blank tape, consider the property that it eventually enters a designated state PRINT. Which statements are true for arbitrary encoded machines?

**Candidates**

**I.** The set of machines having the property is recognizable.

**II.** Simulating a machine for a sufficiently large fixed number of steps decides the property for every machine.

**III.** The property is undecidable, since a machine can simulate an arbitrary machine/input pair and enter PRINT exactly when that simulation halts.

**IV.** The complement is also recognizable.

A. II and IV  
B. I and III  
C. III and IV  
D. I and II  

### Q29. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A SQL table has nullable columns a,b, CHECK(a+b>0), UNIQUE(a,b), and a composite foreign key (a,b) with MATCH SIMPLE semantics. For this question, UNIQUE treats tuples containing NULL as distinct, CHECK rejects only FALSE, and MATCH SIMPLE skips the referenced-row check if any referencing column is NULL. The referenced table is empty. Which statements are true?

**Candidates**

**I.** Inserting (NULL,−5) can satisfy all these constraints.

**II.** CHECK(a+b>0) alone forces both columns to be non-null.

**III.** Two copies of (NULL,−5) can coexist under the specified UNIQUE semantics.

**IV.** Inserting (1,1) satisfies the foreign key despite the empty referenced table.

A. III and IV  
B. I and II  
C. I and III  
D. I and IV  

### Q30. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Six unit squares form a cube net. Their centres on a square grid are A=(0,0), B=(1,0), C=(2,0), D=(3,0), E=(1,1), and F=(1,-1). Squares sharing a full edge are hinged, and the net is folded into a cube with labels on the outside. Which pair of faces is opposite, and which triple can meet at one cube vertex?

A. A and C are opposite; A,B,E can meet.  
B. B and C are opposite; A,C,E can meet.  
C. E and F are opposite; A,B,C can meet.  
D. A and D are opposite; B,E,F can meet.  

### Q31. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Relations Candidate(x)={a,b}, Required(y)=empty, and Completed(x,y)=empty use set semantics. The desired query returns candidates who have completed every required item. Which statements are correct?

**Candidates**

**I.** The result is empty because Completed is empty.

**II.** The result is {a,b} by vacuous truth.

**III.** For each candidate, testing that no required item lacks a matching Completed tuple implements the desired condition.

**IV.** Replacing the outer Candidate relation by the x-projection of Completed preserves the result for this instance.

A. II and III  
B. I and III  
C. I and IV  
D. II and IV  

### Q32. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let L1={a^n b^n c^m : n,m≥0} and L2={a^m b^n c^n : n,m≥0}. Which statements are correct?

A. Both L1 and L2 are context-free.  
B. Their intersection is {a^n b^n c^n : n≥0}.  
C. Their intersection must be context-free because each language is context-free.  
D. Their union is context-free.  

### Q33. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

What is the asymptotic number of executions of work()?

```text
for i = 1 to n:
    j = 1
    while j <= i:
        for k = 1 to j:
            work()
        j = 2*j
```

A. Θ(n log n)  
B. Θ(n²)  
C. Θ(n² log n)  
D. Θ(log² n)  

### Q34. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

The following code operates on ordinary integer variables; assignment copies a value and does not create an alias.

```text
x = 4
y = x
x = 9
z = y + x
```

Which statements are correct?

**Candidates**

**I.** z is13.

**II.** y is9 at the end.

**III.** The value assigned by the first line contributes to z.

**IV.** Changing x on line3 also changes y.

A. III and IV  
B. I and II  
C. I and IV  
D. I and III  

### Q35. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A conjecture states: “For every positive integer n, n²+n+41 is prime.” Which single calculation is sufficient to refute the conjecture?

A. It equals43 at n=1.  
B. It equals47 at n=2.  
C. It equals41² at n=40.  
D. It is odd at n=3.  

### Q36. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An IP router forwards a packet across two different Ethernet links. The packet's IPv4 source and destination are unchanged by assumption; TTL is decremented. Which statements are correct?

A. The outgoing Ethernet header can differ from the incoming Ethernet header.  
B. The IPv4 header checksum must account for the TTL change.  
C. End-to-end IP destination being unchanged requires the Ethernet destination address to remain unchanged on every hop.  
D. Link-layer addressing and network-layer addressing serve different scopes.  

### Q37. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A B+ tree index has all data entries in leaves, and linked leaves support ordered scans. Which statements are correct?

**Candidates**

**I.** Searching once for the lower range bound can be followed by leaf-link traversal for the rest of the range.

**II.** Every subsequent leaf necessarily requires a fresh root-to-leaf search.

**III.** Internal separator keys can duplicate key values present in leaves.

**IV.** Leaf links by themselves eliminate the need to locate the first relevant leaf.

A. II and III  
B. II and IV  
C. I and III  
D. III and IV  

### Q38. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A synchronous message-passing send completes only when a matching receive occurs. Process P first sends to Q and then receives from Q; process Q first sends to P and then receives from P. Neither channel buffers a message. Which statements are correct?

**Candidates**

**I.** Both processes can block on their first operation.

**II.** The program is guaranteed to finish because each process eventually has a receive in its source code.

**III.** Changing Q to receive first and then send removes this particular cyclic wait.

**IV.** Adding a mutex around both sequences necessarily fixes the protocol.

A. II and IV  
B. III and IV  
C. I and II  
D. I and III  

### Q39. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An undirected graph consists of triangles abc and def together with the single connecting edge cd. Which statements are correct?

**Candidates**

**I.** It has a perfect matching.

**II.** Every perfect matching contains cd.

**III.** It is bipartite.

**IV.** Its minimum vertex cover has size3.

A. I and II  
B. III and IV  
C. I and III  
D. I and IV  

### Q40. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

L is a nonregular language over alphabetΣ. Which statements must hold?

A. Its complement Σ*\L is nonregular.  
B. L union (Σ*\L) is regular.  
C. Intersecting L with any infinite regular language always gives a nonregular language.  
D. Removing finitely many strings from L leaves a nonregular language.  

### Q41. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An HTTP cache has a stale response with an entity tag. It validates the response using If-None-Match and receives304 Not Modified. Which action matches the response's meaning?

A. Replace the representation body by the digits304.  
B. Treat the resource as permanently deleted.  
C. Reuse the cached representation body subject to the updated cache metadata.  
D. Assume the server transmitted a complete replacement body.  

### Q42. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Events A,B have P(A)=0.8 and P(B)=0.7. Which additional specifications are individually consistent with these two probabilities?

**Candidates**

**I.** P(A∩B)=0.4

**II.** P(A∩B)=0.6

**III.** P(A|B)=0.5

**IV.** P(A∪B)=1

A. I and IV  
B. II and III  
C. III and IV  
D. II and IV  

### Q43. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Each of four people is either a truth-teller, whose statement below is true, or a liar, whose statement is false. A says “B is a liar.” B says “C is a liar.” C says “D is a liar.” D says “A and B are both truth-tellers.” Which pair consists exactly of the truth-tellers?

A. A,B  
B. A,C  
C. B,D  
D. C,D  

### Q44. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A B+ tree has all leaves exactly two edges below the root. The root and each nonroot internal node have between two and four children. Each leaf stores between two and four data keys; internal separator copies are not data keys. Which pair gives the minimum and maximum possible data-key counts?

A. (4,16)  
B. (8,64)  
C. (8,32)  
D. (16,64)  

### Q45. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For L={a^n b^n : n≥0}, choose z=a^p b^p in a pumping-lemma argument, where p≥1. Which statement correctly addresses every decomposition z=uvw with |uv|≤p and |v|≥1?

A. v contains only a's, so removing v produces a string outside L.  
B. v contains equal numbers of a's and b's, so repeating v stays in L.  
C. Some suitable decomposition must be chosen by the person proving nonregularity.  
D. The lemma allows v to be empty if u is nonempty.  

### Q46. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A prime-implicant chart has four columns m0,m1,m2,m3 and four rows. P covers m0,m1; Q covers m1,m2; R covers m2,m3; S covers m0,m3. All rows have equal literal cost and no other prime implicants exist. Which statements hold?

A. No row is essential.  
B. Every minimum cover contains P.  
C. {P,R} is a minimum cover.  
D. Removing P still leaves a cover using two rows.  

### Q47. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For real t, let A be the matrix below. An LU factorization here means A=LU without row exchanges, with L lower triangular with diagonal entries1 and U upper triangular. Which statements hold?

```text
A = [ t  1
      1  0 ]
```

A. A is invertible for every real t.  
B. Such an LU factorization exists for t=0.  
C. Such an LU factorization exists for every nonzero t.  
D. For nonzero t, U22=−1/t.  

### Q48. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“The panel sought a disinterested assessor: the assessor needed to examine the evidence carefully but have no financial stake in the outcome.” Which replacement best preserves the intended meaning of “disinterested” here?

A. indifferent to the evidence  
B. impartial regarding the outcome  
C. inexperienced in assessment  
D. certain that the proposal would fail  

### Q49. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Let L={a^m b^n : m and n are positive integers, and m divides n}. For an arbitrary integer p≥2 choose w=a^p b^p. Consider every decomposition w=xyz satisfying |xy|≤p and |y|≥1. Which choices of pumping exponent i guarantee that xy^i z is outside L for every such decomposition?

**Candidates**

**I.** i=0

**II.** i=1

**III.** i=2

**IV.** i=p+2

A. II and IV  
B. I and II  
C. III and IV  
D. I and III  

### Q50. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A process calls a blocking read on an empty pipe whose write end is still open elsewhere. No signal interrupts the call. Which statements are correct?

**Candidates**

**I.** The process must consume a CPU core continuously until data arrives.

**II.** The operating system can deschedule the blocked process.

**III.** Another process can run on the same core while this process waits.

**IV.** Empty at this instant necessarily means end-of-file.

A. I and II  
B. I and III  
C. I and IV  
D. II and III  

---

## ANSWER KEY — SET 004

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MSQ | 2 | B, C, D |
| 2 | MSQ | 2 | B, C, D |
| 3 | MSQ | 2 | A, C, D |
| 4 | MCQ | 2 | D |
| 5 | MSQ | 2 | A, C, D |
| 6 | MSQ | 1 | A, B, D |
| 7 | MSQ | 1 | A, B, D |
| 8 | MSQ | 2 | A, B, C |
| 9 | MSQ | 1 | A, B, C |
| 10 | MSQ | 2 | A, C, D |
| 11 | MSQ | 1 | A, B, D |
| 12 | MSQ | 1 | A, C, D |
| 13 | MSQ | 2 | A, B, D |
| 14 | MSQ | 1 | B, C, D |
| 15 | MSQ | 1 | A, B, D |
| 16 | MCQ | 2 | C |
| 17 | MSQ | 1 | B, C, D |
| 18 | MCQ | 1 | D |
| 19 | MSQ | 2 | A, C, D |
| 20 | MSQ | 2 | A, C, D |
| 21 | MCQ | 2 | C |
| 22 | MCQ | 1 | D |
| 23 | MSQ | 2 | B, C, D |
| 24 | MCQ | 2 | C |
| 25 | MSQ | 1 | B, C, D |
| 26 | MSQ | 1 | A, B, D |
| 27 | MCQ | 2 | B |
| 28 | MCQ | 2 | B |
| 29 | MCQ | 2 | C |
| 30 | MSQ | 2 | B, C, D |
| 31 | MCQ | 2 | A |
| 32 | MCQ | 2 | C |
| 33 | MSQ | 2 | A, C, D |
| 34 | MCQ | 1 | D |
| 35 | MSQ | 2 | A, B, D |
| 36 | MCQ | 2 | C |
| 37 | MCQ | 2 | C |
| 38 | MCQ | 2 | D |
| 39 | MCQ | 1 | A |
| 40 | MCQ | 2 | C |
| 41 | MSQ | 1 | A, B, D |
| 42 | MCQ | 1 | D |
| 43 | MSQ | 2 | A, C, D |
| 44 | MSQ | 2 | A, C, D |
| 45 | MSQ | 1 | B, C, D |
| 46 | MCQ | 1 | B |
| 47 | MCQ | 1 | B |
| 48 | MSQ | 2 | A, C, D |
| 49 | MCQ | 2 | C |
| 50 | MCQ | 1 | D |
