# GATE CS — Additional Practice Set 020

**Questions:** 50  
**Maximum marks:** 75

Read the task above each embedded question carefully. For an invalid-answer task, select options that do not correctly answer the embedded question. For a pair task, select the pair containing all valid candidates. MCQ has one correct choice; MSQ requires all correct choices. The answer key follows Q50.

### Q1. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Let L={w#reverse(w) : w is a string over {0,1}}, where # is a separator not in {0,1}. A pushdown recognizer reads input left to right and may reject immediately on a mismatch. Which statements are correct?

**Candidates**

**I.** A deterministic pushdown recognizer can push before # and compare/pop after #.

**II.** The recognizer can accept after input exhaustion even if unmatched symbols remain on its stack.

**III.** The same push-then-pop equality test recognizes {w#w : w over {0,1}}.

**IV.** The one-symbol input # belongs to L.

A. I and III  
B. II and III  
C. I and IV  
D. II and IV  

### Q2. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

The following schema uses immediate constraint checking after each SQL statement. The database initially contains Parent ids 1 and 2, and Child rows (10,1), (11,2), (12,NULL).
```sql
CREATE TABLE Parent (id INTEGER PRIMARY KEY);
CREATE TABLE Child (
    id INTEGER PRIMARY KEY,
    pid INTEGER,
    FOREIGN KEY (pid) REFERENCES Parent(id)
        ON DELETE SET NULL ON UPDATE CASCADE
);
```
Each proposed operation below is considered independently from this initial state. Which statements are correct?

A. Deleting Parent row id=1 succeeds and leaves Child row id=10 with pid=NULL.  
B. Updating Parent id=2 to id=3 succeeds and changes Child row id=11 to pid=3.  
C. Inserting Child row (13,NULL) violates the foreign-key constraint because no Parent id is NULL.  
D. Updating Parent id=1 to id=2 fails even though ON UPDATE CASCADE is specified.  

### Q3. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A five-stage in-order pipeline has stages IF,ID,EX,MEM,WB, each one cycle. There is no forwarding and no automatic stalling. Register writes occur in the first half of a cycle and ID reads in the second half, so ID may read a value written in WB during the same cycle. The instructions below use ordinary integer registers; R0 is always available. What is the minimum total number of NOP instructions that must be inserted without reordering to guarantee correct results for arbitrary initial register values?
```text
ADD R1,R0,R0
ADD R2,R1,R0
ADD R3,R2,R0
```

A. 2  
B. 3  
C. 4  
D. 6  

### Q4. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Consider the augmented grammar with start symbol S:

```text
S' -> S
S  -> a S b S | epsilon
```

Use standard LL(1), LR(0), and SLR(1) constructions, with end marker $. Which statements are correct?

**Candidates**

**I.** The grammar is LL(1).

**II.** The grammar is ambiguous.

**III.** The grammar is SLR(1).

**IV.** The grammar is LR(0).

A. III and IV  
B. I and III  
C. I and II  
D. I and IV  

### Q5. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An expression translator uses this grammar and emits postfix code. For E→E−T it emits the left E's code, then T's code, then “−”. For E→T and T→digit it emits the child's code and the digit respectively. What is emitted for 8−3−2?

A. 8 3 2 − −  
B. − − 8 3 2  
C. 8 3 − 2 −  
D. 8 − 3 − 2  

### Q6. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For 0≤t≤1, define I(t)=∫₀¹|x−t| dx. Which statements are correct?

A. The minimum of I(t) is 1/4, attained only at t=1/2.  
B. I(t)+I(1−t)≥1/2 for all t in [0,1].  
C. ∫₀¹I(t) dt=1/2.  
D. The set of t in [0,1] satisfying I(t)≤5/16 is an interval of length 1/2.  

### Q7. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A segment has byte offsets 0 through 5999. It is paged using 4096-byte pages, with both required pages present. Segment bounds are checked independently of page presence. Which statements are correct?

**Candidates**

**I.** Offset 5000 is valid and uses page 1 with offset 904.

**II.** Offset 7000 is valid because page 1 is present.

**III.** Offset 5999 is the last valid byte.

**IV.** Allocating the second page automatically enlarges the segment to 8192 bytes.

A. I and III  
B. II and III  
C. II and IV  
D. III and IV  

### Q8. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let L={w#w^R:w∈{0,1}*}, where # is a distinct separator and w^R reverses w. Which statements are correct?

A. A deterministic pushdown automaton with final-state acceptance can recognize L.  
B. L is regular.  
C. Erasing the separator from every word of L produces a context-free language.  
D. L intersect 0*#1* is exactly {#}.  

### Q9. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A table has rows (department,salary): (A,10),(A,10),(A,20),(B,20),(B,NULL). Consider:

```sql
SELECT department
FROM T
GROUP BY department
HAVING COUNT(DISTINCT salary) = 2
   AND SUM(salary) > 30;
```

Which result is returned under standard SQL aggregate rules?

A. No rows  
B. A only  
C. B only  
D. A and B  

### Q10. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A complete DFA over {a,b} starts at p and accepts only in r or s. Its transition table is:

| State | a | b |
|---|---|---|
| p | q | r |
| q | p | s |
| r | r | r |
| s | s | s |

Which statements are correct?

A. All four states are reachable.  
B. p and q are distinguishable by some suffix.  
C. r and s are equivalent.  
D. The language is exactly the set of strings containing at least one b.  

### Q11. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A queue is represented by a circular array of length 8. head points to the next element to remove, tail to the next free insertion slot, and one slot is always left unused. Initially head=6 and tail=2. Execute dequeue, enqueue X, enqueue Y, dequeue, enqueue Z, with all operations successful. What are (head,tail,number of stored elements) at the end?

A. (0,5,5)  
B. (0,5,4)  
C. (1,5,4)  
D. (0,4,4)  

### Q12. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A process opens a file descriptor, sets its close-on-exec flag, and forks. The child successfully execs a new program. The parent does not exec or close the descriptor. Which statement is correct?

A. The descriptor is closed in both processes by the child's exec.  
B. It remains open in the parent but is closed in the child during exec.  
C. The flag prevents fork from creating a child.  
D. The descriptor must remain open in the child because it was inherited.  

### Q13. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In C, assuming the proper standard header and successful allocation, which statement about `int *p=malloc(3*sizeof *p);` is correct before any initialization of the allocated int objects?

A. All three int values are guaranteed to be zero.  
B. The allocated storage persists until it is freed, even if the local pointer variable leaves scope.  
C. sizeof *p evaluates an indeterminate pointed-to int value.  
D. The allocation contains exactly three bytes on every implementation.  

### Q14. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A schedule is `r1(x), w1(x), r2(x), c1, c2`, where T2 reads the value written by T1. Which statements are correct?

**Candidates**

**I.** It is recoverable.

**II.** It is cascadeless.

**III.** T2 could require cascading rollback if T1 aborted before its displayed commit instead.

**IV.** T2 commits before T1 in the displayed schedule.

A. III and IV  
B. I and II  
C. I and IV  
D. I and III  

### Q15. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let L consist of binary strings of length at least four whose fourth symbol from the right is 1. What is the number of states in a smallest complete DFA for L?

A. 5  
B. 16  
C. 17  
D. 32  

### Q16. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A language L is recognizable by a Turing machine, and its complement is also recognizable. Which conclusions follow?

**Candidates**

**I.** L is decidable.

**II.** L must be regular.

**III.** A decider can interleave simulations of the two recognizers on the same input.

**IV.** Every recognizer for L must halt on every input.

A. I and IV  
B. I and III  
C. II and III  
D. II and IV  

### Q17. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A depth-first search of an undirected simple graph records parent pointers. Which statements hold?

**Candidates**

**I.** Every edge joining an ancestor to a descendant can be represented as a tree edge or a back edge.

**II.** A non-tree edge necessarily joins vertices in unrelated DFS subtrees.

**III.** An edge to the parent should not by itself be treated as evidence of a cycle.

**IV.** DFS discovery order must equal breadth-first discovery order.

A. II and III  
B. II and IV  
C. I and III  
D. III and IV  

### Q18. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A TCP server has a listening socket and accepts two connections, producing descriptors c1 and c2. It then closes only the listening socket. No shutdown is applied to c1 or c2. Which statement is correct?

A. Both accepted connections necessarily close immediately.  
B. c1 and c2 remain usable; closing the listener does not itself close those connected sockets.  
C. c1 becomes a new listening socket automatically.  
D. The two clients must now share one TCP byte stream.  

### Q19. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For positive integer n, an algorithm splits into subproblems of sizes floor(n/3) and n−floor(n/3), then does Θ(n) additional work, with constant-time base cases for n≤2. What is its asymptotic running time?

A. Θ(log n)  
B. Θ(n)  
C. Θ(n log n)  
D. Θ(n²)  

### Q20. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A lexical analyzer distinguishes an identifier token from a symbol-table entry. Which statement is correct?

A. Every occurrence of the same identifier spelling must create a permanently distinct name entry regardless of scope or implementation.  
B. Token recognition and name binding are different tasks; returning an identifier token does not alone determine which declaration it denotes.  
C. Recognizing a token proves that the entire program is type-correct.  
D. Whitespace must always be emitted as an identifier token.  

### Q21. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Arrange the following troubleshooting steps coherently: P, verify that the replacement resolves the fault; Q, isolate the faulty component using measurements; R, replace the isolated component; S, observe and record the original symptom.

A. S–Q–R–P  
B. Q–P–S–R  
C. R–S–P–Q  
D. P–Q–R–S  

### Q22. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A binary min-heap contains distinct keys. Decreasing the key at an arbitrary nonroot index may violate heap order with which nodes first?

A. Its parent; upward restoration may be needed.  
B. Only its children; downward restoration is always required.  
C. Every node necessarily becomes invalid.  
D. No heap-order violation can result from decreasing a key.  

### Q23. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A compiler translates `x != 0 && 10/x > 1` using left-to-right short-circuit evaluation over exact integers, with division by zero raising an observable exception. Which transformations preserve behaviour for every x?

**Candidates**

**I.** Test x!=0 first and branch around the division when false.

**II.** Evaluate 10/x before testing x!=0 for all x.

**III.** Replace the conjunction by an evaluation that performs the division only on the x!=0 branch.

**IV.** Replace the whole expression by true because 10 is positive.

A. I and III  
B. II and IV  
C. III and IV  
D. I and II  

### Q24. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A page has been modified in memory since it was loaded from disk. Which statements about replacement are correct in an ordinary write-back paging system?

**Candidates**

**I.** Its dirty status may require writing its current contents to backing storage before its frame is reused.

**II.** A clean page with an unchanged backing copy may be discarded without such a write.

**III.** Every page fault proves the evicted page was dirty.

**IV.** Dirty status alone determines which page every replacement policy must choose.

A. III and IV  
B. I and II  
C. I and III  
D. I and IV  

### Q25. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Unit cubes form four vertical stacks on a 2×2 footprint, with height rows (1,3) and (2,1). Orthogonal projections onto the horizontal plane and the two vertical coordinate planes count overlapping projected squares only once. What is the sum of the areas of these three projections, in square units?

A. 7  
B. 11  
C. 12  
D. 14  

### Q26. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A lexically scoped language has procedure P with local x=10. Procedures Q and S are declared directly inside P. Q has its own local x=20 and declares R inside Q. S increments its lexically nearest x and returns that x. During one activation of P, Q calls R, and R calls S twice in sequence. What is the sum of S's returned values?

A. 21  
B. 23  
C. 43  
D. 40  

### Q27. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For connected undirected weighted graphs, which statements are correct?

**Candidates**

**I.** Repeated edge weights make a unique MST impossible.

**II.** Pairwise distinct edge weights guarantee a unique MST.

**III.** If the graph itself is a tree, it has a unique spanning tree regardless of repeated weights.

**IV.** A globally heaviest edge can never belong to an MST, even if it is a bridge.

A. II and III  
B. I and IV  
C. II and IV  
D. III and IV  

### Q28. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A nondeterministic PDA accepts by final state only after consuming the entire input. In a conversion to empty-stack acceptance, a fresh protected bottom marker is placed below the original stack, and from an original final state the machine may enter a new mode that uses only epsilon transitions to pop all remaining stack symbols, including that marker. Empty-stack acceptance also requires all input consumed. Which statements are correct?

**Candidates**

**I.** The drain mode can successfully finish an accepting computation after the entire input has been consumed in an original final state.

**II.** Entering drain mode with unread input automatically accepts that input as well.

**III.** The new bottom marker must be treated as an ordinary original-stack symbol by every old transition, without restriction.

**IV.** The requirement to consume all input prevents a drained stack reached too early from accepting a remaining suffix.

A. II and IV  
B. I and IV  
C. III and IV  
D. I and II  

### Q29. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Four switches P,Q,R,S are either ON or OFF. Exactly two are ON. Whenever P is ON, Q is ON. Whenever R is OFF, S is ON. Which statements must hold?

A. P is OFF.  
B. At least one of R and S is ON.  
C. Q is ON.  
D. If Q is OFF, both R and S are ON.  

### Q30. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For n a positive integer, what is the asymptotic number of executions of work()?

```text
for i = 1 to n:
    j = i
    while j <= n:
        work()
        j = j + i
```

A. Θ(n)  
B. Θ(n log n)  
C. Θ(n sqrt(n))  
D. Θ(n²)  

### Q31. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

In a finite directed network, every link has strictly positive cost and every router can reach destination d. Each router u other than d selects any outgoing neighbour v satisfying dist(u,d)=cost(u,v)+dist(v,d), using exact shortest-path distances. Different routers may break equal-cost ties independently. Which statements are correct?

**Candidates**

**I.** The selected next-hop graph can contain a directed cycle because tie-breaking is independent.

**II.** Distance to d strictly decreases at each selected hop.

**III.** Every packet following these next hops eventually reaches d.

**IV.** Allowing zero-cost links would leave the strict-decrease argument unchanged.

A. II and III  
B. I and III  
C. I and IV  
D. II and IV  

### Q32. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Linear probing in a hash table stores keys whose home slot is4 in slots4,5,6. Slot7 is empty. The key in slot5 is deleted. Which deletion action preserves ordinary probing searches for the key in slot6, if searches stop at a never-used empty slot?

A. Mark slot5 as never-used empty without moving keys.  
B. Mark slot5 with a tombstone that searches pass through.  
C. Clear slot6 as well.  
D. Change only the deleted key's hash function.  

### Q33. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Exactly two of A,B,C attend a meeting. A says “B attends”; B says “C does not attend”; C says “A does not attend.” Exactly one of these statements is true, regardless of whether its speaker attends. Who does not attend?

A. A  
B. B  
C. C  
D. No assignment satisfies the conditions.  

### Q34. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A synchronous machine has two different states that produce the same output now. Which statements are correct about state minimization?

**Candidates**

**I.** Equal current outputs alone guarantee equivalence.

**II.** A future input sequence yielding different output sequences distinguishes the states.

**III.** Equivalent states must have equivalent successors for every input under the usual deterministic Moore-machine definition.

**IV.** Different state encodings alone guarantee distinguishability by external observations.

A. III and IV  
B. I and II  
C. I and III  
D. II and III  

### Q35. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Let A=[[2,1],[0,2]]. Which statements are correct?

**Candidates**

**I.** A has two linearly independent eigenvectors over the real numbers.

**II.** A⁵ has diagonal entries32 and32.

**III.** A⁵−32I has rank1.

**IV.** A⁵=32I.

A. II and III  
B. I and II  
C. I and III  
D. I and IV  

### Q36. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A total computable function maps every pair(machine M,input w) to a machine N that ignores its own input, simulates M on w and accepts if that simulation accepts. Which statements are correct?

A. If M accepts w, N recognizes all strings.  
B. If M does not accept w, N recognizes the empty language.  
C. A decider for whether N's language is empty would decide arbitrary machine acceptance.  
D. The construction requires deciding whether M accepts w before producing N.  

### Q37. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

L is a finite language over a finite alphabet. Which statements necessarily hold?

A. L is regular.  
B. L is context-free.  
C. L contains the empty string.  
D. Some DFA recognizes L.  

### Q38. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Two threads execute atomic fetch-and-add(counter,1), each exactly once, with counter initially0. Each operation returns the value before its increment. Which statements must hold after both finish?

**Candidates**

**I.** The final counter is2.

**II.** Both operations return0.

**III.** The two returned values are0 and1 in some order.

**IV.** The thread that starts first must receive0, even if it is delayed before executing its atomic operation.

A. II and IV  
B. III and IV  
C. I and II  
D. I and III  

### Q39. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A nondeterministic pushdown automaton accepts if at least one computation branch consumes the whole input and reaches a designated final state. Which statements are correct?

**Candidates**

**I.** A rejecting branch prevents acceptance even if another branch accepts.

**II.** An infinite branch need not prevent acceptance by a different finite branch.

**III.** Reaching a final state before consuming all input is sufficient under the stated rule.

**IV.** Acceptance uses an existential condition over branches.

A. II and IV  
B. III and IV  
C. I and II  
D. I and III  

### Q40. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A deterministic finite automaton has missing transitions, which cause immediate rejection. To recognize the complement over the same alphabet, which statements are correct?

**Candidates**

**I.** Swapping accepting and rejecting states alone always suffices.

**II.** Completing the automaton with a rejecting sink before swapping accepting states works.

**III.** A word rejected by taking a missing transition must be accepted by a correct complement automaton.

**IV.** Adding a sink after swapping states and leaving that sink rejecting always works.

A. I and II  
B. II and III  
C. I and III  
D. I and IV  

### Q41. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A notice says: “Applications received after Friday will be considered only if places remain.” Which conclusion is justified?

A. Every late application will be accepted if a place remains.  
B. Applications submitted before Friday are considered only if places remain.  
C. Every application received by Friday will be accepted.  
D. No late application can be considered when all places have been filled.  

### Q42. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Relations R(x),S(x) are finite but the underlying value domain is infinite. Which formulas, with x free, always return a finite set of values?

**Candidates**

**I.** R(x) AND NOT S(x)

**II.** NOT R(x)

**III.** R(x) OR S(x)

**IV.** NOT R(x) AND NOT S(x)

A. II and III  
B. II and IV  
C. III and IV  
D. I and III  

### Q43. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A16-bit memory interface consists of two independently enabled eight-bit banks. The low bank holds even byte addresses; the high bank holds odd byte addresses. One bus transaction accesses both bytes of one aligned two-byte word, and can enable either bank or both. Which statements are correct?

**Candidates**

**I.** An aligned two-byte load can be serviced in one transaction.

**II.** A two-byte load starting at an odd address always fits in one aligned-word transaction.

**III.** A byte store can preserve the other byte by enabling only its target bank.

**IV.** Changing endianness changes which numerical byte address is even.

A. I and III  
B. II and IV  
C. III and IV  
D. I and II  

### Q44. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A DMA device writes a buffer in main memory. The CPU has an old, clean copy of that buffer in a non-coherent write-back cache. The DMA completion interrupt has arrived. Which action is sufficient to make a subsequent CPU read obtain the DMA result, assuming no concurrent writes?

A. Write back the old clean cache line without invalidating it.  
B. Invalidate the cached buffer lines before reading.  
C. Disable interrupts after the completion interrupt.  
D. Read the buffer repeatedly until its value changes.  

### Q45. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Choose the grammatically correct completion: “Had the survey included night-shift workers, its conclusion ____ different.”

A. will have been  
B. would have been  
C. would be being  
D. had been being  

### Q46. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“The witness gave an equivocal reply: it could reasonably be understood as either agreement or refusal.” In this sentence, “equivocal” most nearly means:

A. deliberately brief  
B. supported by independent evidence  
C. open to conflicting interpretations  
D. expressing definite agreement  

### Q47. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Consider these C declarations inside a function. No operation shown overflows.

```c
int a[3] = {2,4,6};
int *p = a + 3;
```

Which subsequent expressions have defined behavior?

A. p - a  
B. *(p - 1)  
C. *p  
D. p == a + 3  

### Q48. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

In an expression language, evaluating an operand may have side effects; && and || evaluate left to right and short-circuit. Values are Boolean. Which rewrites preserve both returned value and operand side effects in every execution?

**Candidates**

**I.** false && f() → false

**II.** f() && false → false

**III.** true || f() → true

**IV.** f() || true → true

A. II and IV  
B. I and III  
C. III and IV  
D. I and II  

### Q49. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A directed graph has edges s→a of weight 2, s→b of weight 5, and b→a of weight −4. There are no other edges. Which statements are correct?

**Candidates**

**I.** The shortest s-to-a path has weight 1.

**II.** The graph has a negative-weight cycle.

**III.** A Dijkstra implementation that permanently settles a before b can output a wrong distance for a.

**IV.** Every shortest path uses the fewest possible edges.

A. III and IV  
B. I and II  
C. I and III  
D. I and IV  

### Q50. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Unit cubes form four vertical columns on a 2×2 grid, with no gaps within a column. All four columns are nonempty. Let h(i,j) be the positive integer height in row i, column j. Orthographic views establish

```text
max(h(1,1),h(1,2)) = 3
max(h(2,1),h(2,2)) = 2
max(h(1,1),h(2,1)) = 3
max(h(1,2),h(2,2)) = 2
```

Which total numbers of cubes are possible?

A. 7  
B. 8  
C. 9  
D. 10  

---

## ANSWER KEY — SET 020

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | C |
| 2 | MCQ | 2 | C |
| 3 | MSQ | 1 | A, B, D |
| 4 | MCQ | 2 | B |
| 5 | MSQ | 1 | A, B, D |
| 6 | MCQ | 2 | C |
| 7 | MCQ | 1 | A |
| 8 | MCQ | 2 | B |
| 9 | MSQ | 2 | A, C, D |
| 10 | MCQ | 1 | B |
| 11 | MSQ | 2 | B, C, D |
| 12 | MSQ | 1 | A, C, D |
| 13 | MSQ | 1 | A, C, D |
| 14 | MCQ | 2 | D |
| 15 | MSQ | 2 | A, C, D |
| 16 | MCQ | 1 | B |
| 17 | MCQ | 1 | C |
| 18 | MSQ | 2 | A, C, D |
| 19 | MSQ | 2 | A, B, D |
| 20 | MSQ | 1 | A, C, D |
| 21 | MSQ | 2 | B, C, D |
| 22 | MSQ | 2 | B, C, D |
| 23 | MCQ | 2 | A |
| 24 | MCQ | 1 | B |
| 25 | MSQ | 1 | A, B, C |
| 26 | MSQ | 2 | A, C, D |
| 27 | MCQ | 1 | A |
| 28 | MCQ | 1 | B |
| 29 | MCQ | 1 | C |
| 30 | MSQ | 2 | A, C, D |
| 31 | MCQ | 2 | A |
| 32 | MSQ | 1 | A, C, D |
| 33 | MSQ | 2 | A, B, C |
| 34 | MCQ | 2 | D |
| 35 | MCQ | 2 | A |
| 36 | MCQ | 2 | D |
| 37 | MCQ | 1 | C |
| 38 | MCQ | 1 | D |
| 39 | MCQ | 1 | A |
| 40 | MCQ | 1 | B |
| 41 | MSQ | 1 | A, B, C |
| 42 | MCQ | 2 | D |
| 43 | MCQ | 2 | A |
| 44 | MSQ | 1 | A, C, D |
| 45 | MSQ | 1 | A, C, D |
| 46 | MSQ | 1 | A, B, D |
| 47 | MCQ | 2 | C |
| 48 | MCQ | 2 | B |
| 49 | MCQ | 1 | C |
| 50 | MCQ | 2 | D |
