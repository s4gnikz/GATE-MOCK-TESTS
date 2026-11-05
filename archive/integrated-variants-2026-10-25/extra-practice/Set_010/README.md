# GATE CS — Additional Practice Set 010

**Questions:** 50  
**Maximum marks:** 75

Read the task above each embedded question carefully. For an invalid-answer task, select options that do not correctly answer the embedded question. For a pair task, select the pair containing all valid candidates. MCQ has one correct choice; MSQ requires all correct choices. The answer key follows Q50.

### Q1. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let R be a binary relation on a nonempty domain. Which formula is the logical negation of

`forall x exists y [R(x,y) AND forall z (R(x,z) -> z=y)]`?

All variables in the options are bound as displayed.

A. exists x forall y [NOT R(x,y) OR exists z (R(x,z) AND z!=y)]  
B. exists x exists y [NOT R(x,y) OR exists z (R(x,z) AND z!=y)]  
C. forall x forall y [NOT R(x,y) AND exists z (R(x,z) AND z!=y)]  
D. exists x forall y [NOT R(x,y) OR forall z (R(x,z) AND z!=y)]  

### Q2. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Consider a context-free pumping-lemma proof attempt for L = {a^n b^n c^n : n ≥ 0}. For an arbitrary pumping length p ≥ 1, choose s = a^p b^p c^p. A legal decomposition is s = uvxyz, with |vxy| ≤ p and |vy| > 0, and pumping produces uv^i xy^i z. Which claims are correct?

A. The substring vxy cannot contain both an a and a c.  
B. For every legal decomposition, pumping with i=0 produces a string outside L.  
C. It is sufficient to exhibit one legal decomposition for which pumping with i=0 produces a string outside L.  
D. A proof may assume, without treating other cases, that v and y each contain only a symbols.  

### Q3. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A processor has a write-back data cache with no hardware coherence with DMA. It modifies a buffer, leaving the buffer's cache lines dirty, and then asks a DMA controller to copy that buffer from main memory to a device. The processor will not modify the buffer again during the transfer. Which action before starting DMA ensures that the device receives the updated data?

A. Invalidate the dirty lines without writing them back.  
B. Write back all dirty buffer lines and wait for completion.  
C. Disable device-completion interrupts.  
D. Wait for a DMA-completion interrupt before starting the DMA transfer.  

### Q4. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An 8-bit ALU subtracts B from A using A+(NOT B)+1. The result is reduced modulo 256. N is its most significant bit, V indicates signed two's-complement overflow, and C is carry-out, with C=1 meaning no unsigned borrow. Both operands range independently over all 256 bit patterns.

How many ordered pairs (A,B) produce N=0, V=1 and C=1 simultaneously?

A. 8192  
B. 8128  
C. 8256  
D. 16384  

### Q5. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A policy states: “Unless the permit is renewed before Monday, the pilot must stop on Monday. Renewal alone does not authorize expansion; an independent review is also required.” Assume the policy is followed and the pilot continues on Tuesday. Which conclusion is justified?

A. An independent review must already have authorized expansion.  
B. The permit was renewed before Monday, but authorization for expansion cannot be inferred.  
C. Continuing the pilot automatically authorizes expansion.  
D. The permit could have remained unrenewed because an independent review replaces renewal.  

### Q6. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A hidden source is chosen once: source I with probability 1/3, source II with probability 2/3. Conditional on that source, trials are independent; success probability is 1/4 for I and 1/2 for II. Given exactly two successes in the first three trials, what is the probability of success on the fourth trial?

A. 1/2  
B. 35/76  
C. 3/19  
D. 7/16  

### Q7. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

To apply the regular-language pumping lemma to the language of binary palindromes, choose w=0^p10^p for a putative pumping length p≥1. A permitted decomposition w=xyz satisfies |xy|≤p and |y|≥1. Which statements are correct?

**Candidates**

**I.** Every permitted y consists only of zeros from the initial block.

**II.** Some permitted decomposition remains a palindrome after replacing y by yy.

**III.** Pumping down to xz produces a non-palindrome for every permitted decomposition.

**IV.** Exhibiting just one badly behaving permitted decomposition is sufficient for a nonregularity proof.

A. I and III  
B. II and III  
C. II and IV  
D. III and IV  

### Q8. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Evaluate (7+3)+(−5) using four-bit signed two's-complement integers, rounding neither operand. In implementation S, each addition saturates at −8 or 7 if needed. In implementation W, each addition wraps modulo 16. What are the final signed results (S,W)?

A. (5,5)  
B. (2,5)  
C. (2,−11)  
D. (7,−6)  

### Q9. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Under SQL's usual three-valued logic, table T(x) contains rows 1,2,NULL, and table U(y) contains rows 2,NULL. Which statements are correct?

**Candidates**

**I.** `SELECT x FROM T WHERE x NOT IN (SELECT y FROM U)` returns no rows.

**II.** `SELECT x FROM T WHERE NOT EXISTS (SELECT 1 FROM U WHERE U.y=T.x)` returns the rows 1 and NULL.

**III.** Removing NULL from U makes the NOT IN query return both 1 and NULL.

**IV.** Replacing NOT IN with IN in the first query returns three rows.

A. III and IV  
B. I and III  
C. I and II  
D. I and IV  

### Q10. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A binary floating-point format has four significant bits including the leading 1, unbounded exponents, and round-to-nearest, ties-to-even after each operation. Let a=16, b=1, c=−16, all exactly representable. Which statements are correct?

A. The computed value of (a+b)+c is 0.  
B. The computed value of a+(b+c) is 1.  
C. Both parenthesizations must agree because no overflow occurs.  
D. The exact real-arithmetic value of a+b+c is 1.  

### Q11. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For a unary relation R(x), compare tuple-calculus expressions E1={t | R(t)} and E2={t | NOT R(t)}. Values of t range over an external domain containing the active domain of R. Which statements are correct?

**Candidates**

**I.** E1 is unchanged if the external domain is enlarged without changing R.

**II.** E2 is unchanged under every such enlargement.

**III.** E2 can gain tuples when the external domain is enlarged.

**IV.** E1 necessarily returns every element of the external domain.

A. I and III  
B. I and IV  
C. II and III  
D. II and IV  

### Q12. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Over {a,b}, L consists of strings whose every even-numbered position contains a, numbering positions from one. Odd positions are unrestricted; ε belongs to L. What is the minimum number of states in a complete DFA for L?

A. 2  
B. 3  
C. 4  
D. 5  

### Q13. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An ε-NFA has initial state p, final state r, ε-transitions p→q and q→p, and an a-transition q→r. There are no other transitions. Which statement is correct?

A. The language is infinite because there is an ε-cycle.  
B. The language is {a}, although there are infinitely many finite accepting runs on a.  
C. The empty string is accepted because p and q form a cycle.  
D. No string is accepted because the ε-cycle prevents progress.  

### Q14. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A comparison sorting algorithm sorts n distinct keys. Its decision tree has binary comparison outcomes. Which is a valid worst-case lower-bound argument?

A. There are n possible outputs, so height is at least log₂n.  
B. There are n! possible input orders requiring different sorting permutations, so height is at least ceil(log₂(n!)).  
C. Every sorting algorithm must use exactly n² comparisons.  
D. Each comparison places one key permanently, so n comparisons always suffice.  

### Q15. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A B-tree has minimum degree t=2: every nonroot node has 1–3 keys, an internal node with k keys has k+1 children, and a nonleaf root has at least two children. Height is three edges from root to every leaf. Which pair gives the minimum and maximum possible total numbers of keys?

A. (7,63)  
B. (15,255)  
C. (8,64)  
D. (15,85)  

### Q16. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An algorithm for a directed acyclic graph computes longest paths by processing vertices in topological order and relaxing outgoing edges using maximum instead of minimum. Edge weights may be negative. Which statement is correct?

A. Negative edges invalidate this dynamic program even in a DAG.  
B. A topological order ensures all predecessors are processed before a vertex, so the recurrence is valid.  
C. The algorithm requires all paths to have the same number of edges.  
D. The graph must first be converted to an undirected graph.  

### Q17. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Activities have half-open intervals A=[0,4), B=[1,2), C=[2,3), D=[3,5), E=[4,6). Which statement correctly compares greedy rules for maximizing the number of nonoverlapping activities?

A. Earliest starting time always yields an optimum and selects three here.  
B. Earliest finishing time can select B,C,D, while choosing A first limits the total to two.  
C. Shortest duration is the only rule that can produce three here.  
D. Every maximal compatible set must have the same cardinality.  

### Q18. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An undirected connected graph has a unique minimum-weight edge e crossing a particular nontrivial cut. Which statements hold?

**Candidates**

**I.** Every MST contains e.

**II.** No MST can contain any other edge crossing that cut.

**III.** Adding e to an MST that omitted it would allow a strictly lighter crossing edge exchange, contradicting minimality.

**IV.** e must be a bridge in the original graph.

A. II and IV  
B. III and IV  
C. I and II  
D. I and III  

### Q19. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In a four-variable Karnaugh map, why are columns labelled 00,01,11,10 rather than 00,01,10,11?

A. Every pair of horizontally adjacent columns, including wraparound, then differs in exactly one bit.  
B. Binary numbers must always be written in Gray-code order.  
C. The order changes the function's truth table values.  
D. Adjacent columns must differ in both bits.  

### Q20. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“The conclusion is provisional and may be revised after further trials.” Which word is closest in meaning to provisional here?

A. Irrevocable  
B. Tentative  
C. Unrelated  
D. Unanimous  

### Q21. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For an arbitrary Turing machine M, define L_M={x : M accepts x within at most |x| transition steps}. Which statements are correct?

**Candidates**

**I.** L_M is decidable for every M.

**II.** Deciding L_M requires deciding whether M eventually halts on x.

**III.** A decider can simulate exactly the bounded number of allowed steps and reject if no acceptance has occurred.

**IV.** L_M must be empty whenever M fails to halt on some other input.

A. I and IV  
B. II and III  
C. I and III  
D. II and IV  

### Q22. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For exact integer arithmetic with no side effects, which local replacements preserve a variable x's value for all x?

A. x+0 → x  
B. x*1 → x  
C. x*0 → x  
D. x−x → 0  

### Q23. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A lexer has tokens `>` and `>=` and uses longest match. How does it tokenize `>=>`?

A. `>=` followed by `>`.  
B. `>` followed by `=>`, where `=>` is not a declared token.  
C. One token `>=>` even though none is declared.  
D. It must discard the final character.  

### Q24. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A binary floating-point format has finite precision. Ignore overflow and underflow, and assume its precision is at least four significant bits. Which real values can be represented exactly?

**Candidates**

**I.** 3/8

**II.** 1/10

**III.** 7/4

**IV.** 1/3

A. III and IV  
B. I and III  
C. I and II  
D. I and IV  

### Q25. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A directed graph has edges s→a of weight 1, a→b of weight 0, b→a of weight 0, and b→t of weight 2. Walks may revisit vertices. Which statement is correct?

A. The shortest s-to-t walk weight is unbounded below.  
B. The shortest weight is 3 and only one shortest walk exists.  
C. The shortest weight is 3 and infinitely many shortest walks exist.  
D. No walk from s to t exists.  

### Q26. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

To refute the regular-language pumping condition, which quantifier order must a proof establish? Here p is a positive pumping length, w∈L has length at least p, and a valid split means w=xyz, |xy|≤p, |y|>0; “fails” means xy^i z∉L for i≥0.

A. There exist p,w, a valid split and i that fails.  
B. For every p, there exist w and a valid split for which every i fails.  
C. There exists p such that every w has a failing split.  
D. For every p, there exists w such that every valid split has some i that fails.  

### Q27. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A plane transformation T maps (x,y) to (1−y,x). Starting at (1,0), apply T exactly 2027 times. What is the final point?

A. (1,1)  
B. (0,1)  
C. (0,0)  
D. (1,0)  

### Q28. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Let A(a) have rows (1,a,0), (0,1,a), (a,0,1), where a is real. Consider A(a)x=(1,1,1)ᵀ. Which statements are true?

**Candidates**

**I.** A(a) is singular for every real a.

**II.** det(A(a))=1+a³.

**III.** At a=−1, the displayed system has infinitely many solutions.

**IV.** At a=−1, A(a) has rank two.

A. II and III  
B. II and IV  
C. III and IV  
D. I and II  

### Q29. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A forwarding table routes 10.2.0.0/25 and 10.2.0.128/25 to next hop H, and 10.2.0.64/26 to next hop J. A default route goes to K. Replace the two /25 entries by 10.2.0.0/24→H while retaining the /26 exception and default. Under longest-prefix matching, which statements are true?

**Candidates**

**I.** Every destination keeps the same next hop.

**II.** The /24 aggregate overrides the /26 exception because it was inserted later.

**III.** Destinations outside 10.2.0.0/24 continue using the default route.

**IV.** Removing the /26 exception as well would preserve every destination's next hop.

A. III and IV  
B. I and II  
C. I and III  
D. I and IV  

### Q30. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A B+ tree's root contains separator20 and has two leaf children: [5,10] and [20,30]. The separator is defined as the minimum key of the right child. Each leaf must contain at least one key. After deleting20, which action is required under this separator convention?

A. Merge the leaves because a leaf cannot contain one key.  
B. Change the root separator to30; no merge is required.  
C. Leave separator20 because internal separators must never change.  
D. Remove the root and discard the left leaf.  

### Q31. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Initially head points to node A in the singly linked list A→B→C→NULL. Consider these assignments, evaluated in order:

```text
p = head.next
head.next = p.next
p.next = head
head = p
```

Which list is reachable from head afterward?

A. A→C→B→NULL  
B. B→A→C→NULL  
C. B→C→A→NULL  
D. A→B→C→NULL  

### Q32. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A total decider D exists for language L over a finite alphabet. Consider a machine that enumerates all strings in length-lexicographic order, runs D on each, and prints precisely those D accepts. Which statements are correct?

**Candidates**

**I.** Every string of L is eventually printed.

**II.** If L is empty, the enumerator must eventually halt.

**III.** If L is finite, the enumerator as described can run forever after printing its last member.

**IV.** The construction requires a known uniform bound on D's running time over all inputs.

A. II and III  
B. I and III  
C. II and IV  
D. III and IV  

### Q33. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A proposed PDA for L={a^n b^n : n≥0} pushes for every a and pops for every b, rejects an attempted pop from empty, and accepts at end exactly when the stack is empty. It has no state recording whether b's have begun, so it allows pushing after popping. Which statements are correct?

**Candidates**

**I.** It accepts abab, which is outside L.

**II.** Adding a phase distinction that forbids a after the first b can repair the order constraint.

**III.** Its empty-stack condition alone guarantees all a's precede all b's.

**IV.** It rejects aabb.

A. II and IV  
B. III and IV  
C. I and II  
D. I and III  

### Q34. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Two threads always acquire mutexes X and Y in the order X then Y, and release both after finite computation. No other resources or waits exist. Which statement is correct?

A. A cycle of these two threads each holding one of X,Y and waiting for the other is possible.  
B. The common acquisition order excludes a circular wait involving these mutexes.  
C. The order guarantees equal waiting times.  
D. Deadlock freedom implies that neither thread can ever wait.  

### Q35. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A floating-point format has both signed zeros and infinities, with ordinary IEEE-style comparisons and division. Which statements are correct?

**Candidates**

**I.** +0 and−0 compare equal.

**II.** Dividing positive1 by+0 and by−0 can distinguish their signs in the resulting infinities.

**III.** Equal comparison necessarily means identical bit representations.

**IV.** Positive infinity is an ordinary largest finite number in the format.

A. I and II  
B. I and III  
C. I and IV  
D. II and III  

### Q36. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A partially ordered set has elements0,a,b,1, with0<a<1 and0<b<1; a and b are incomparable. Which statements are correct?

A. a and b have meet0 and join1.  
B. The poset is a total order.  
C. The poset is a lattice.  
D. There is no upper bound of both a and b.  

### Q37. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“The two estimates are commensurate because both measure annual cost in the same currency; this does not mean they are equal.” Which meaning of “commensurate” fits this explanation?

A. Comparable on a common basis.  
B. Necessarily identical in magnitude.  
C. Deliberately misleading.  
D. Measured without units.  

### Q38. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A DNS record is cached with a positive TTL. The authoritative server changes the record before that TTL expires. Assume ordinary caching without an explicit invalidation mechanism. Which statements are correct?

**Candidates**

**I.** A resolver can continue returning the cached old record until expiry.

**II.** Every cache is immediately informed of the authoritative change by the TTL field itself.

**III.** Reducing the authoritative record's TTL afterward does not retroactively shorten a previously cached expiry under this model.

**IV.** TTL is a guarantee that the authoritative value cannot change during that interval.

A. II and IV  
B. III and IV  
C. I and II  
D. I and III  

### Q39. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Records have fields (department,score,id). A stable sorting routine is available. The desired order is department ascending, then score descending, preserving original order for records tied on both fields. Which procedures always achieve that order?

**Candidates**

**I.** Stable sort by score descending, then stable sort by department ascending.

**II.** Stable sort by department ascending, then stable sort by score descending.

**III.** One stable sort using the lexicographic key (department,negative score).

**IV.** First reverse the entire input, then use procedure A.

A. I and III  
B. III and IV  
C. I and II  
D. I and IV  

### Q40. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Under set semantics, R(A,B) and S(A,B) have the same schema. Which statements hold for every instance?

**Candidates**

**I.** πA(R−S)=πA(R)−πA(S).

**II.** πA(R−S) contains πA(R)−πA(S).

**III.** πA(R∩S) is contained in πA(R)∩πA(S).

**IV.** πA(R∩S)=πA(R)∩πA(S).

A. I and II  
B. II and III  
C. I and III  
D. I and IV  

### Q41. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A real matrix A has three columns. Its reduced row-echelon form has pivots in columns1 and3. The system Ax=b is consistent. Which statements are correct?

**Candidates**

**I.** There is exactly one free variable.

**II.** Every consistent right-hand side yields a unique solution.

**III.** The solution set is an affine line in R³.

**IV.** The nullspace has dimension2.

A. I and IV  
B. II and III  
C. I and III  
D. II and IV  

### Q42. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A router runs link-state routing. Assume all routers have received the same complete link-state database and use the same positive link costs. Which statements are correct?

**Candidates**

**I.** Routers can independently compute shortest paths from that database.

**II.** Each router needs only its neighbours' currently advertised distances, with no topology information.

**III.** Different source routers may obtain different shortest-path trees from the same database.

**IV.** Identical topology information forces every router to choose the same next hop for a fixed destination.

A. II and III  
B. II and IV  
C. III and IV  
D. I and III  

### Q43. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Records (key,id) occur initially as(1,A),(1,B),(2,C). They are stably sorted by ascending key and the whole resulting array is then reversed. Relative to the original input, is this a stable descending-key sort?

A. No, because A and B appear in the opposite order.  
B. Yes, because reversing always preserves equal-key order.  
C. No, because key2 appears before key1.  
D. Yes, because the ascending sort was stable.  

### Q44. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A full binary recursion tree has n=2^k leaves at depth k, with the root at depth0. Every call at depth d allocates and initializes2^d buffer cells, retains them while processing its children sequentially in depth-first order, then frees them before returning. Leaves also allocate their stated buffers. What are the tight orders of total cell initializations and maximum simultaneously live buffer cells, respectively?

A. (Θ(n²),Θ(n))  
B. (Θ(n log n),Θ(n))  
C. (Θ(n²),Θ(n²))  
D. (Θ(n log n),Θ(log n))  

### Q45. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

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

### Q46. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A SQL table declares id as PRIMARY KEY and parent_id as a nullable foreign key referencing id in the same table. There are no other constraints. Which statements hold?

**Candidates**

**I.** A row may have parent_id=NULL.

**II.** The declarations alone prevent a row from referencing itself.

**III.** The declarations alone prevent a cycle involving two rows.

**IV.** Every non-NULL parent_id must match an existing id when the foreign-key constraint is checked.

A. I and III  
B. II and III  
C. II and IV  
D. I and IV  

### Q47. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

In a connected undirected weighted graph, edge e joins u to v and has weight8. There is a u-to-v path avoiding e on which every edge has weight at most7. Which statements necessarily hold?

**Candidates**

**I.** No minimum spanning tree contains e.

**II.** Removing e disconnects the graph.

**III.** If a spanning tree contains e, some cheaper spanning tree can be obtained by exchanging one edge.

**IV.** Every edge of the alternative path must belong to every minimum spanning tree.

A. I and III  
B. II and III  
C. II and IV  
D. III and IV  

### Q48. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A device sets a level-triggered interrupt request while its completion-status bit is 1. An interrupt handler acknowledges the CPU interrupt controller but leaves the device status bit unchanged. Assuming the controller permits subsequent delivery, what behavior is possible after return from the handler?

A. Another interrupt is delivered because the device still asserts its request.  
B. The device's status bit necessarily clears when the CPU acknowledges its controller.  
C. The device's completed transfer is automatically undone.  
D. The interrupt line necessarily changes into an edge-triggered source.  

### Q49. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A data set has five real observations with median 10 and mean 12. A sixth observation equal to 100 is appended. Which quantity is determined uniquely from this information?

A. The new median.  
B. The new mean.  
C. The new range.  
D. The new population variance.  

### Q50. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

F=(a OR b) AND ((NOT a) OR c) is implemented as a two-level OR-AND circuit with an inverter for NOT a. Inputs b=c=0 are held fixed while a changes. Gate delays are positive and unequal. Which statements are correct?

A. F is logically 0 before and after the change.  
B. Unequal path delays can briefly make F=1.  
C. Adding the factor (b OR c) leaves the Boolean function unchanged and prevents this particular static-0 hazard in the resulting two-level realization.  
D. Adding the factor (b OR c) necessarily changes the truth table.  

---

## ANSWER KEY — SET 010

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MSQ | 1 | B, C, D |
| 2 | MSQ | 2 | C, D |
| 3 | MSQ | 1 | A, C, D |
| 4 | MSQ | 2 | A, C, D |
| 5 | MSQ | 2 | A, C, D |
| 6 | MSQ | 2 | A, C, D |
| 7 | MCQ | 1 | A |
| 8 | MSQ | 2 | A, C, D |
| 9 | MCQ | 1 | C |
| 10 | MCQ | 2 | C |
| 11 | MCQ | 1 | A |
| 12 | MSQ | 1 | A, C, D |
| 13 | MSQ | 2 | A, C, D |
| 14 | MSQ | 2 | A, C, D |
| 15 | MSQ | 1 | A, C, D |
| 16 | MSQ | 2 | A, C, D |
| 17 | MSQ | 2 | A, C, D |
| 18 | MCQ | 1 | D |
| 19 | MSQ | 1 | B, C, D |
| 20 | MSQ | 1 | A, C, D |
| 21 | MCQ | 2 | C |
| 22 | MCQ | 1 | C |
| 23 | MSQ | 1 | B, C, D |
| 24 | MCQ | 2 | B |
| 25 | MSQ | 2 | A, B, D |
| 26 | MSQ | 1 | A, B, C |
| 27 | MSQ | 2 | A, B, D |
| 28 | MCQ | 2 | B |
| 29 | MCQ | 2 | C |
| 30 | MSQ | 1 | A, C, D |
| 31 | MSQ | 1 | A, C, D |
| 32 | MCQ | 2 | B |
| 33 | MCQ | 2 | C |
| 34 | MSQ | 1 | A, C, D |
| 35 | MCQ | 1 | A |
| 36 | MSQ | 1 | B, D |
| 37 | MSQ | 1 | B, C, D |
| 38 | MCQ | 2 | D |
| 39 | MCQ | 2 | A |
| 40 | MCQ | 2 | B |
| 41 | MCQ | 2 | C |
| 42 | MCQ | 1 | D |
| 43 | MSQ | 1 | B, C, D |
| 44 | MSQ | 2 | B, C, D |
| 45 | MCQ | 2 | C |
| 46 | MCQ | 1 | D |
| 47 | MCQ | 1 | A |
| 48 | MSQ | 1 | B, C, D |
| 49 | MSQ | 1 | A, C, D |
| 50 | MCQ | 2 | D |
