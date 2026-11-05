# GATE CS — Additional Practice Set 012

**Questions:** 50  
**Maximum marks:** 77

Read the task above each embedded question carefully. For an invalid-answer task, select options that do not correctly answer the embedded question. For a pair task, select the pair containing all valid candidates. MCQ has one correct choice; MSQ requires all correct choices. The answer key follows Q50.

### Q1. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A lexer recognizes identifiers by `[a-z][a-z0-9]*`, the keyword `if`, and operators `==`, `=`, `++`, `+`. It uses maximal munch; an identifier lexeme exactly equal to `if` is classified as a keyword. Whitespace is ignored. What token-lexeme sequence is produced for `ifx==if+++x`?

A. if, x, ==, if, ++, +, x  
B. ifx, ==, if, ++, +, x  
C. ifx, =, =, if, +, ++, x  
D. ifx, ==, if, +++, x  

### Q2. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A microprogrammed control unit uses a fixed-width microinstruction. One field jointly encodes the following bus-transfer commands:

- An idle command, in which no source drives the bus and no destination is loaded.
- A non-idle command chooses exactly one of eight sources and a nonempty subset of five destination registers. Every such source/subset pair is allowed.

There are no other bus-transfer commands. Each allowed command needs a distinct binary code, and unused codes are permitted. The other independently encoded fields select one of six ALU operations (including no-operation), one of 128 next addresses, and one of four sequencing conditions (including unconditional sequencing). Codes cannot be shared across these four fields. What is the minimum microinstruction width?

A. 19 bits  
B. 20 bits  
C. 21 bits  
D. 25 bits  

### Q3. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A binary search tree stores distinct keys. A node x has both a left and a right child. Its inorder successor s is used when deleting x. Which statements about s in the tree before deletion are correct?

A. s is in the right subtree of x.  
B. s must be a leaf.  
C. s has no left child.  
D. s may have a right child.  

### Q4. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Over alphabet {a,b}, let L={a,ab}. A pushdown automaton starts with one bottom-of-stack symbol. For empty-stack acceptance, a string is accepted only if all input has been consumed and the stack is empty; no transition is possible once the stack is empty. No right-end marker is supplied. Standard determinism forbids a choice between an epsilon transition and an input-consuming transition for the same state and stack top. Which machine model cannot recognize L?

A. A deterministic finite automaton.  
B. A nondeterministic pushdown automaton accepting by empty stack.  
C. A deterministic pushdown automaton accepting by final state.  
D. A deterministic pushdown automaton accepting by empty stack.  

### Q5. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Which of the following problems have an algorithm that always halts and answers correctly? Machines have finite descriptions; Turing machines are deterministic.

**Candidates**

**I.** Given a Turing machine and an input, determine whether it halts within 100 transitions.

**II.** Given a Turing machine and an input, determine whether it eventually halts.

**III.** Given a DFA over {0,1}, determine whether it accepts every binary string.

**IV.** Given a Turing machine, determine whether it halts on every input.

A. I and II  
B. I and IV  
C. I and III  
D. II and III  

### Q6. [2 Marks] [MSQ]

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

### Q7. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A binary max-heap is stored as [9,8,7,6,5,4,3]. Delete the maximum by moving the last element to the root, then repeatedly swapping it with the larger child until heap order is restored. Which array results?

A. [8,7,6,5,4,3]  
B. [8,6,7,3,5,4]  
C. [7,8,4,6,5,3]  
D. [8,6,7,5,3,4]  

### Q8. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A router uses longest-prefix matching with routes 10.0.0.0/8→A, 10.1.0.0/16→B, 10.1.128.0/17→C, and 10.1.192.0/18→D. Only the /17 route is withdrawn. Which next hops are then used for 10.1.160.1 and 10.1.200.1, respectively?

A. (A,A)  
B. (C,D)  
C. (B,B)  
D. (B,D)  

### Q9. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An eight-bit two's-complement negation computes the low eight bits of NOT x plus 1. For which input is the signed result equal to the signed input even though the mathematical negation is not representable?

A. 00000000  
B. 01111111  
C. 11111111  
D. 10000000  

### Q10. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An HTTP client sends a conditional GET containing `If-None-Match: "v7"` for a cached representation. The server's current representation has the same entity tag and is otherwise eligible for the conditional request. Compare a 304 response with a 200 response carrying the entire unchanged representation. Which statement is correct?

A. A 304 necessarily eliminates the request-response round trip.  
B. A 304 supplies a new full representation body that must replace the cached body.  
C. A 304 can save representation-body transfer while still requiring a network round trip.  
D. A 304 proves that all caches on the Internet contain the same body.  

### Q11. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

R(A,B,C) has exactly the dependencies implied by A→B and BC→A. Decompose it into R1(A,B) and R2(A,C). Which statements are correct?

A. The decomposition is lossless under the stated dependencies.  
B. Both components are in BCNF under their projected dependencies.  
C. Enforcing only the projected dependencies on the components need not enforce BC→A on their join.  
D. A is a candidate key of the original R.  

### Q12. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A frame appends one even-parity bit to its data. The receiver checks even parity over the entire received frame. Which corruption patterns are always detected?

**Candidates**

**I.** Exactly one flipped bit anywhere in the frame.

**II.** Exactly two flipped data bits.

**III.** Exactly three flipped bits anywhere in the frame.

**IV.** Any nonempty set of flipped bits.

A. II and III  
B. I and III  
C. II and IV  
D. III and IV  

### Q13. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Routers have converged exact shortest distances d(v) to destination t. Each router v≠t selects a next hop u satisfying d(v)=w(v,u)+d(u). All relevant distances are finite. Which statements are correct?

A. If all link costs are strictly positive, the selected next-hop graph cannot contain a directed cycle.  
B. If zero-cost links are allowed, independent tie choices can create a forwarding cycle despite correct distances.  
C. Correct distances alone prevent forwarding cycles for every set of nonnegative link costs.  
D. With positive costs, distance strictly decreases at every selected hop.  

### Q14. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

R(A,B,C,D) has FDs A→B, B→C, C→D. Which decomposition is both lossless and dependency preserving?

A. AB, BC, CD  
B. AB, CD  
C. AC, BD  
D. AD, BC  

### Q15. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An out-of-order processor retires instructions in program order. Stores may execute speculatively but do not modify architecturally visible memory until retirement. Why is this restriction useful for precise exceptions?

A. It ensures a younger store cannot become visible before an older faulting instruction is handled.  
B. It makes every load take one cycle.  
C. It eliminates all data dependencies.  
D. It guarantees that speculative branches are always predicted correctly.  

### Q16. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A resolver caches a CNAME mapping alias.example to host.example at time 0 with TTL 120 seconds, and the target's A record at time 20 with TTL 50 seconds. At time 80 it receives a new request for alias.example. Assume no prefetching, no stale-answer service, and no other cached answers. Cache hits do not refresh TTLs. Which action and remaining TTL are correct?

A. Reuse both records; each has 40 seconds remaining.  
B. Reuse the CNAME with 40 seconds remaining and obtain a fresh A record for host.example.  
C. Obtain a new CNAME but reuse the A record with 40 seconds remaining.  
D. Reuse both records indefinitely because their names have not changed.  

### Q17. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A basic block is `t=a+b; a=a+1; u=a+b; v=t;`. Arithmetic is exact, and scalar variables have no aliases. Which transformations preserve the final values of a,t,u,v for all initial a,b?

**Candidates**

**I.** Replace `v=t` by `v=a+b-1` after the other statements.

**II.** Replace `u=a+b` by `u=t`.

**III.** Replace `u=a+b` by `u=t+1`.

**IV.** Delete `t=a+b` while leaving `v=t` unchanged and without introducing another definition of t.

A. II and III  
B. II and IV  
C. I and III  
D. III and IV  

### Q18. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Which tuple-calculus expression describes employees e who work in every department listed in relation Department? Works(e,d) records an assignment.

A. Employee(e) ∧ ∀d(Department(d) → Works(e,d))  
B. Employee(e) ∧ ∃d(Department(d) ∧ Works(e,d))  
C. Employee(e) ∧ ∀d(Department(d) ∧ Works(e,d))  
D. Employee(e) ∧ ¬∃d Works(e,d)  

### Q19. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Coins of denominations 1,3,4 are available without limit. For amount 6, which statement correctly evaluates the rule “repeatedly choose the largest coin not exceeding the remaining amount”?

A. It uses two coins and is optimal.  
B. It uses three coins, whereas an optimal solution uses two.  
C. It cannot make amount 6 at all.  
D. Every feasible solution uses three coins.  

### Q20. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Choose the sentence that preserves both the conditional meaning and correct grammar: the machine should be restarted only after the valve has been closed.

A. Restart the machine before the valve has been closed.  
B. Do not restart the machine until the valve has been closed.  
C. Closing the valve is unnecessary before restarting the machine.  
D. The machine must restart whenever the valve closes, without any other condition.  

### Q21. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Grammar E→E+T | T, T→T*F | F, F→id has its usual parse-tree interpretation. Which statements are true?

**Candidates**

**I.** Multiplication binds more tightly than addition.

**II.** A chain of additions is left-associated.

**III.** The grammar is immediately suitable for a naive recursive-descent parser without eliminating left recursion.

**IV.** The word id+id*id has two parse trees under this grammar.

A. I and IV  
B. II and III  
C. I and II  
D. II and IV  

### Q22. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For the unary language L={a^(n²):n≥0}, a pumping proof chooses a^(p²) and a pumped segment of length d with 1≤d≤p. Why does pumping once extra give a contradiction?

A. p²+d lies strictly between p² and (p+1)², so it is not a square.  
B. p²+d is always less than p².  
C. Every unary language is finite.  
D. Pumping is prohibited for unary alphabets.  

### Q23. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A half-adder adds bits x,y without a carry input. Which pair gives (sum,carry)?

A. (x XOR y, x AND y)  
B. (x OR y, x XOR y)  
C. (x AND y, x OR y)  
D. (NOT x, NOT y)  

### Q24. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Which sequence correctly orders an evidence-based correction: P, test the revised version; Q, identify the error; R, revise the faulty step; S, compare the original result with the requirement?

A. P–R–Q–S  
B. S–Q–R–P  
C. R–S–P–Q  
D. Q–P–S–R  

### Q25. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A full-adder sum bit is implemented using a 4-to-1 mux with select bits a,b and remaining input c. Which data inputs (D0,D1,D2,D3) are correct?

A. (0,c,c,1)  
B. (c,c′,c′,c)  
C. (c′,c,c,c′)  
D. (0,0,1,1)  

### Q26. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

SQL table R has non-null values 1,2,3 in column x. Table S has values 2 and NULL in column y. Which statements are correct under standard SQL three-valued logic?

**Candidates**

**I.** `SELECT x FROM R WHERE x NOT IN (SELECT y FROM S)` returns no rows.

**II.** `SELECT x FROM R WHERE NOT EXISTS (SELECT 1 FROM S WHERE S.y=R.x)` returns 1 and 3.

**III.** `SELECT COUNT(y) FROM S` returns 2.

**IV.** The predicate `NULL=NULL` evaluates to TRUE.

A. I and IV  
B. II and III  
C. II and IV  
D. I and II  

### Q27. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Which register dependences can register renaming eliminate by assigning distinct physical destinations, without changing the required flow of produced values to their consumers?

**Candidates**

**I.** A true read-after-write dependence between a producer and its consumer.

**II.** A write-after-read name dependence.

**III.** The control dependence on an unresolved branch.

**IV.** A write-after-write name dependence.

A. II and IV  
B. I and IV  
C. II and III  
D. III and IV  

### Q28. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A regular file contains bytes ABCDE. Descriptor p opens it at offset zero; q=dup(p); descriptor r comes from a separate open of the same file, also at zero. With no intervening operations, execute read(p,2), read(q,1), seek(r,1 from start), read(r,2), read(p,1). All reads succeed fully. What are the byte strings from the four reads in order?

A. AB; A; BC; A  
B. AB; C; BC; E  
C. AB; C; DE; D  
D. AB; C; BC; D  

### Q29. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A machine's ADD (R)+,(R)+ instruction first reads the source word at address R and increments R by four, then reads the destination word at the new R and increments R by four again, finally writing the sum to that destination's captured address. Initially R=100, M[100]=3 and M[104]=5. Which pair gives the final R and M[104]?

A. (104,6)  
B. (108,6)  
C. (108,8)  
D. (104,8)  

### Q30. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

In the following code, p and q point to valid integer objects and may alias. Integer overflow does not occur.

```c
int x = *p + 1;
*q = 9;
int y = *p + 1;
```

Which statements are correct for all allowed executions?

**Candidates**

**I.** Replacing the initialization of y by y=x is always valid.

**II.** If p and q are proved to point to distinct objects, reusing x for y is valid.

**III.** If p=q and the original pointed-to value is4, x and y differ.

**IV.** The repeated textual expression alone proves that common-subexpression elimination is valid.

A. I and II  
B. I and III  
C. I and IV  
D. II and III  

### Q31. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let R be a finite unary relation over an infinite domain. A tuple-calculus query asks for all x satisfying NOT R(x), with no further restriction on x. Which statement is correct?

A. The result is always finite because R is finite.  
B. The result can be infinite and depends on values outside the active domain.  
C. Negation is forbidden in every safe tuple-calculus query.  
D. The result always equals R.  

### Q32. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A study reports that among applicants who passed a competitive screening, experience and examination score were negatively associated. The screening favoured applicants with either strong experience or a high score. Which conclusion is justified by this description alone?

A. Experience causes lower examination scores in all applicants.  
B. Restricting attention to screened applicants may create an association absent in the full applicant pool.  
C. The screening must have ignored experience.  
D. No applicant can have both strong experience and a high score.  

### Q33. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Unary relations R and S are finite. Compare query F={x : R(x) AND NOT S(x)} with query G={x : NOT S(x)} over an unrestricted infinite domain. Which statements are correct?

A. F is contained in the active domain of R.  
B. G can return infinitely many values.  
C. The occurrence of NOT makes F necessarily unsafe.  
D. Positive range restriction by R is relevant to F's domain independence.  

### Q34. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Relation R(A,B,C,D) has dependency set F={AB→C, C→B, A→D, D→C}. Which statements are correct?

**Candidates**

**I.** AB→C can be removed without changing the closure of F.

**II.** C→B can be removed without changing the closure of F.

**III.** A is a candidate key of R.

**IV.** D is a candidate key of R.

A. III and IV  
B. I and II  
C. I and IV  
D. I and III  

### Q35. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A recognizer for a language may loop on some nonmembers. Which statements are correct?

**Candidates**

**I.** If it accepts an input, that input is a member.

**II.** If it has not halted after a fixed finite number of steps, the input must be a nonmember.

**III.** A decider must halt on every input.

**IV.** Every recognizer is automatically a decider.

A. I and III  
B. I and II  
C. I and IV  
D. II and III  

### Q36. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Two threads use a mutex to protect a counter. The counter is initialized once before either starts. Each thread locks, reads, increments, writes and unlocks exactly once. Which statements are correct under ordinary correct mutex semantics?

**Candidates**

**I.** The two increment regions cannot overlap.

**II.** The final value is the initial value plus2.

**III.** The mutex by itself specifies which thread increments first.

**IV.** Removing the lock but retaining the unlock preserves the synchronization guarantee.

A. I and IV  
B. I and II  
C. II and III  
D. II and IV  

### Q37. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A policy says, “Unless a submission is anonymous, it must include the author's name.” Which submission violates this rule?

A. An anonymous submission without a name.  
B. A nonanonymous submission with a name.  
C. A nonanonymous submission without a name.  
D. An anonymous submission with a name.  

### Q38. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“The panel described the evidence as suggestive rather than conclusive; its recommendation was consequently provisional.” Which revision preserves both the strength of the evidence and the status of the recommendation?

A. The evidence proved the claim, so the recommendation was final.  
B. The evidence offered some support, so the recommendation remained open to revision.  
C. The evidence disproved the claim, so the recommendation was withdrawn.  
D. The evidence was irrelevant, so the recommendation was unanimous.  

### Q39. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Let HALT={(M,w): M eventually halts on w}. Assume a computable many-one reduction from HALT to a language L. Which conclusions follow?

**Candidates**

**I.** L cannot be decidable.

**II.** L must be recursively enumerable.

**III.** A decider for L would yield a decider for HALT.

**IV.** The existence of this reduction alone guarantees a computable many-one reduction from L to HALT.

A. I and III  
B. III and IV  
C. I and II  
D. I and IV  

### Q40. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A binary min-heap contains distinct keys. Its array uses one-based indexing. Which statements must hold for every heap of at least seven elements?

**Candidates**

**I.** The second-smallest key is at index2 or3.

**II.** The third-smallest key is necessarily at index4 or5.

**III.** The parent of a node always has a smaller key than that node.

**IV.** The array is globally sorted in increasing order.

A. I and II  
B. I and III  
C. I and IV  
D. II and III  

### Q41. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let L={ww : w in {a,b}*}. Which statements are correct?

A. Every word in L has even length.  
B. Every even-length palindrome belongs to L.  
C. L contains words that are not palindromes.  
D. L is closed under reversal.  

### Q42. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Define MUX(s,u,v) to return u when s=0 and v when s=1. A circuit computes T=MUX(s,a,b), then F=MUX(T,s,NOT s). Which statements are correct?

A. F=(NOT s AND a) OR (s AND NOT b).  
B. If a=b, toggling s toggles F.  
C. If a and b differ, F is independent of s.  
D. F always equals s XOR a XOR b.  

### Q43. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An arithmetic right shift by one on the signed value−7 produces floor(−7/2). Integer division by2 instead truncates toward zero. What is the shifted value minus the division result?

A. 0  
B. 1  
C. −7  
D. −1  

### Q44. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A DMA device is programmed with a physical frame address, and it does not consult the process's page table on subsequent writes. An operating system is considering evicting and reusing that frame before DMA completion. Which statements are correct?

**Candidates**

**I.** Pinning the frame until completion can prevent reuse during the transfer.

**II.** Keeping the process's virtual address unchanged alone guarantees that reuse is safe.

**III.** Reusing the frame can direct later DMA writes into another allocation.

**IV.** The DMA device automatically follows any new page-table mapping under the stated model.

A. III and IV  
B. I and III  
C. I and II  
D. I and IV  

### Q45. [2 Marks] [MCQ]

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

### Q46. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A TCP server has a listening socket l. A successful accept(l) returns connected socket c. Which statement is correct?

A. The listening socket becomes c and can no longer accept connections.  
B. Every write to l broadcasts data to all accepted clients.  
C. Closing c necessarily closes l.  
D. l can continue accepting other connections while c serves the accepted connection.  

### Q47. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A lexer has tokens IF='if', ID=[a-z][a-z0-9]*, and INT=[0-9]+. It applies maximal munch, with IF winning a tie against ID. Which tokenization is produced for the input if2if?

A. IF, INT, IF  
B. ID  
C. IF, ID  
D. Lexical error because digits cannot occur in an identifier.  

### Q48. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For n≥2, consider the following pseudocode, with constant-time integer operations:

```text
j=1;
for i=1 to n:
    while j<=i:
        j=2*j;
```

What is the tight asymptotic running time?

A. Theta(log n)  
B. Theta(n log n)  
C. Theta(n)  
D. Theta(n²)  

### Q49. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A weak entity Installment is identified by its owner Loan and its partial key installment_number. Loan has primary key loan_id. Each installment has exactly one owner, and the same installment_number may occur under different loans. Which primary key preserves this identification when mapping Installment to a relation?

A. installment_number alone.  
B. loan_id alone.  
C. (loan_id, installment_number).  
D. amount alone.  

### Q50. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Consider the following algorithm, with n≥2 and a constant-time body that allocates no storage:

```text
for i = 1 to n:
    for j = i to n step i:
        body()
```

Which statements are correct?

**Candidates**

**I.** The body executes exactly Σ(i=1..n) floor(n/i) times.

**II.** The running time is Θ(n log n).

**III.** The algorithm needs Θ(n) auxiliary words merely to execute these loops.

**IV.** The body executes Θ(n²) times.

A. I and III  
B. I and IV  
C. II and III  
D. I and II  

---

## ANSWER KEY — SET 012

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MSQ | 1 | A, C, D |
| 2 | MSQ | 2 | A, C, D |
| 3 | MCQ | 1 | B |
| 4 | MSQ | 2 | A, B, C |
| 5 | MCQ | 1 | C |
| 6 | MSQ | 2 | A, B, D |
| 7 | MSQ | 1 | A, C, D |
| 8 | MSQ | 2 | A, B, C |
| 9 | MSQ | 1 | A, B, C |
| 10 | MSQ | 2 | A, B, D |
| 11 | MCQ | 2 | D |
| 12 | MCQ | 1 | B |
| 13 | MCQ | 2 | C |
| 14 | MSQ | 2 | B, C, D |
| 15 | MSQ | 1 | B, C, D |
| 16 | MSQ | 2 | A, C, D |
| 17 | MCQ | 2 | C |
| 18 | MSQ | 1 | B, C, D |
| 19 | MSQ | 1 | A, C, D |
| 20 | MSQ | 2 | A, C, D |
| 21 | MCQ | 2 | C |
| 22 | MSQ | 2 | B, C, D |
| 23 | MSQ | 1 | B, C, D |
| 24 | MSQ | 1 | A, C, D |
| 25 | MSQ | 2 | A, C, D |
| 26 | MCQ | 1 | D |
| 27 | MCQ | 1 | A |
| 28 | MSQ | 2 | A, B, C |
| 29 | MSQ | 2 | A, B, D |
| 30 | MCQ | 1 | D |
| 31 | MSQ | 1 | A, C, D |
| 32 | MSQ | 1 | A, C, D |
| 33 | MCQ | 2 | C |
| 34 | MCQ | 2 | D |
| 35 | MCQ | 1 | A |
| 36 | MCQ | 1 | B |
| 37 | MSQ | 2 | A, B, D |
| 38 | MSQ | 2 | A, C, D |
| 39 | MCQ | 2 | A |
| 40 | MCQ | 2 | B |
| 41 | MCQ | 2 | B |
| 42 | MCQ | 2 | D |
| 43 | MSQ | 1 | A, B, C |
| 44 | MCQ | 2 | B |
| 45 | MCQ | 2 | C |
| 46 | MSQ | 1 | A, B, C |
| 47 | MSQ | 1 | A, C, D |
| 48 | MSQ | 1 | A, B, D |
| 49 | MSQ | 1 | A, B, D |
| 50 | MCQ | 2 | D |
