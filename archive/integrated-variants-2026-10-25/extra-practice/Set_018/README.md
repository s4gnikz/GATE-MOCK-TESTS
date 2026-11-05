# GATE CS — Additional Practice Set 018

**Questions:** 50  
**Maximum marks:** 72

Read the task above each embedded question carefully. For an invalid-answer task, select options that do not correctly answer the embedded question. For a pair task, select the pair containing all valid candidates. MCQ has one correct choice; MSQ requires all correct choices. The answer key follows Q50.

### Q1. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Consider the grammar S -> SS | aSb | epsilon. Count finite ordered parse trees, distinguishing different tree shapes even when they yield the same string. How many parse trees yield the string ab?

A. Exactly one  
B. Exactly two  
C. A finite number greater than two  
D. Infinitely many  

### Q2. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Eight nonpreemptive activities have the following half-open time intervals; an activity may begin exactly when another finishes.

| Activity | Interval |
|---|---|
| A | [0,3) |
| B | [1,2) |
| C | [2,4) |
| D | [3,5) |
| E | [4,6) |
| F | [5,7) |
| G | [6,8) |
| H | [7,9) |

Let m be the maximum number of mutually nonoverlapping activities that can be selected, and let r be the number of distinct activity subsets attaining this maximum. What is (m,r)?

A. (3,4)  
B. (4,4)  
C. (4,5)  
D. (5,1)  

### Q3. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let F(x,y,z)=x XOR (y AND z). Define D(x,y,z)=F(x,y,z) XOR F(x,NOT y,z). Which expression equals D for every Boolean input?

A. x  
B. y  
C. z  
D. NOT z  

### Q4. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A lexer has the token rules `a`, `b`, `d`, and `ab*c`, where `b*` means zero or more b symbols. It uses longest match. An implementation reads forward until no token rule can still match, then returns to the most recent accepting position to emit that token. Consider the inputs `ab^n d`, with no spaces and arbitrary integer n>=1. Before returning the first token, how much lookahead beyond the most recent accepting position can this implementation require?

A. At most one character, independently of n.  
B. At most two characters, independently of n.  
C. An amount unbounded as n grows.  
D. Zero, because the rule `a` can be emitted immediately upon reading a.  

### Q5. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A real 4×4 matrix M satisfies M²=I and trace(M)=0. Which statements must hold?

A. det(M)=1.  
B. rank(M−I)=2.  
C. M is diagonalizable over the real numbers.  
D. M is symmetric.  

### Q6. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A CRC uses generator G(x)=x³+x+1 over GF(2). An error is undetected exactly when its nonzero error polynomial is divisible by G. Which statements are correct?

A. Error x⁷+1 is undetected.  
B. Error x⁶+1 is undetected.  
C. Every single-bit error is detected.  
D. Every nonzero burst error of length at most three bits is detected.  

### Q7. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A disk scheduler always chooses a pending request closest to the current head, breaking ties by lower cylinder number. New requests can arrive indefinitely. A request far from the current head is pending. Which statement is correct without an arrival-rate bound?

A. The pending request must be served after at most the current queue length requests.  
B. An unending stream of nearer requests can postpone it indefinitely.  
C. Shortest seek distance guarantees fairness.  
D. Tie-breaking alone prevents starvation.  

### Q8. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A file contains bytes abcdef. fd1 opens it read-only; fd2=dup(fd1); fd3 opens the same pathname independently. All operations succeed. Read two bytes from fd1, one from fd2, and one from fd3. Then seek fd2 to absolute offset 1 and read two bytes from fd1. Which bytes does this final read return?

A. de  
B. ab  
C. bc  
D. cd  

### Q9. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An LL(1) parser is built for S→A b, A→a A | ε. The stack top is A and lookahead is b. Which action is correct?

A. Consume b and retain A on the stack.  
B. Apply A→ε without consuming input.  
C. Apply A→aA.  
D. Report an error because b is not in FIRST(aA).  

### Q10. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A TLB tags each translation by an address-space identifier (ASID) and a virtual page number. Processes P and Q have different ASIDs but may use the same virtual addresses. Which statements are correct?

**Candidates**

**I.** A translation for P need not be discarded merely because the CPU switches to Q.

**II.** The ASID alone identifies a physical page without the virtual page number.

**III.** Reusing P's ASID for an unrelated address space may require invalidating stale translations carrying that ASID.

**IV.** ASIDs eliminate the need to update a translation after its page-table mapping changes.

A. I and II  
B. I and IV  
C. II and III  
D. I and III  

### Q11. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let u=(1,1,0)ᵀ, v=(1,0,1)ᵀ, P=uuᵀ/(uᵀu), and Q=vvᵀ/(vᵀv). Which statements are correct?

A. PQ has rank one.  
B. trace(PQ)=1/4.  
C. PQ is symmetric.  
D. The eigenvalues of PQ, counting multiplicity, are 1/4,0,0.  

### Q12. [1 Mark] [MSQ]

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

### Q13. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A sequential detector emits a pulse when the latest three input bits are 101, allowing overlapping matches. It reads 10101 from left to right, starting with no previous bits. How many pulses are emitted?

A. 1  
B. 2  
C. 3  
D. 5  

### Q14. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A TCP receiver advertises zero window because its buffer is full. The network has no loss. Which statement is correct?

A. The sender should interpret this as proof that a router dropped a packet.  
B. Receiver flow control currently prevents ordinary new data from exceeding that advertised allowance.  
C. The receiver has permanently closed the TCP connection.  
D. The sender's congestion window must become exactly zero immediately.  

### Q15. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A five-stage pipeline uses one single-ported memory for both IF instruction fetch and MEM data access. A load instruction is in MEM while a younger instruction needs IF during the same cycle. Even with complete data forwarding, what remains?

A. A structural conflict for the memory port.  
B. A mandatory arithmetic overflow.  
C. A control hazard caused by every load.  
D. No possible conflict because forwarding duplicates the memory port.  

### Q16. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A proposed proof applies the regular-language pumping lemma to L={0ⁿ1ⁿ:n≥0}. After choosing w=0ᵖ1ᵖ, it picks the particular decomposition x=ε,y=0,z=0^(p−1)1ᵖ and shows that this decomposition fails when pumped. What must be repaired to make the argument valid?

A. The proof must show failure for every decomposition satisfying |xy|≤p and |y|>0.  
B. The proof must show that L is finite.  
C. Pumping down is forbidden; only pumping up is permitted.  
D. The selected word must have length less than p.  

### Q17. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“The evaluator called the design economical, not because it was cheap to manufacture, but because each component served several purposes.” Which interpretation best preserves the stated distinction?

A. The evaluator praised efficient use of components without asserting low manufacturing cost.  
B. The evaluator established that manufacturing was inexpensive.  
C. The design uses no components.  
D. Multifunctional components necessarily increase manufacturing cost.  

### Q18. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For grammar S→L=R | R, L→*R | id, R→L, consider an LR(0) item set containing S→L·=R and R→L·. In SLR parsing, FOLLOW(R) contains '='. What conflict occurs in the SLR table for lookahead '='?

A. No conflict, because completed items are ignored on '='.  
B. Shift–reduce conflict between shifting '=' and reducing R→L.  
C. Reduce–reduce conflict between two completed productions shown here.  
D. Accept–reduce conflict because every completed item accepts the input.  

### Q19. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A recovery system uses immediate updates with write-ahead logging, undo of uncommitted transactions and redo of committed transactions. Since the last checkpoint, the log records T1 changing X from 5 to 8, T2 changing Y from 4 to 9, and T1 committing. A crash occurs before T2 commits. Disk may contain either old or new values of each item. After recovery, what must (X,Y) be?

A. (5,4)  
B. (8,9)  
C. (8,4)  
D. (5,9)  

### Q20. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Relation R contains finitely many integers, while the domain of possible integers is infinite. Consider the tuple-calculus query {x | NOT R(x)}, with no restriction to the active domain. Which statement is correct?

A. It is not range-restricted and its result can be infinite even though R is finite.  
B. Its result must be a subset of R.  
C. Its result is always empty.  
D. Negation makes every tuple-calculus query safe automatically.  

### Q21. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A planar figure is reflected across the x-axis and then across the line y=x. Which coordinate rule describes the combined transformation?

A. (x,y)→(−y,x)  
B. (x,y)→(y,−x)  
C. (x,y)→(−x,−y)  
D. (x,y)→(x,−y)  

### Q22. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A process has two threads sharing ordinary memory. Each executes the non-atomic operation `x = x+1` once, starting from x=0, with separate load/add/store steps and sequentially consistent interleaving. Which final values of x are possible?

**Candidates**

**I.** 0

**II.** 1

**III.** 2

**IV.** 3

A. I and IV  
B. II and IV  
C. III and IV  
D. II and III  

### Q23. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Resource A has two instances and B has one. P holds one A and requests B; Q holds B and requests one A; R holds the other A and requests nothing more. A process that receives its request completes and releases its resources; R can complete immediately. Which statements are correct?

A. The system can finish all processes in order R,Q,P.  
B. The cycle involving P and Q proves deadlock even with R able to release an A instance.  
C. A cycle in the resource-allocation graph is not sufficient here to establish deadlock.  
D. Releasing R's A can enable Q, whose completion can then enable P.  

### Q24. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A recognizer accepts every member of L and may loop on nonmembers. Which extra guarantee would make that same machine a decider for L?

A. It uses at least two tape symbols.  
B. It halts on every input, rejecting every nonmember.  
C. It accepts one input quickly.  
D. It has a finite written description.  

### Q25. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Choose the grammatically correct completion in formal English: “Neither the two applicants nor their supervisor ___ available when the committee ___ its decision yesterday.”

A. were; announce  
B. was; announced  
C. were; announcing  
D. was; announce  

### Q26. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

In four-variable cube notation, a dash means either bit. Two implicants are 0−0− and −00−. Suppose every minterm in either cube is an ON minterm and all other minterms are OFF, except 1100 and 1101, which are don't-cares. Which statements are correct?

**Candidates**

**I.** The cubes cannot be combined by the ordinary one-bit-difference Quine–McCluskey combination rule because their dash positions differ.

**II.** Their union alone already contains all minterms of −−0−.

**III.** The larger cube −−0− includes an OFF minterm under the specified classification.

**IV.** Using the two don't-cares permits −−0− as a valid implicant covering their union.

A. I and III  
B. II and III  
C. II and IV  
D. I and IV  

### Q27. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A resolver caches an authoritative negative DNS response for a name with an unexpired negative-cache TTL. The name is then created at the authoritative server. Assuming no forced refresh or invalidation, why may the resolver temporarily continue reporting that the name does not exist?

A. DNS names can never be created after the first query.  
B. TCP forbids any change to DNS records.  
C. The cached negative result may be reused until its TTL expires.  
D. Every negative DNS response has an infinite lifetime.  

### Q28. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A prime-implicant chart has columns 1,2,3 and rows P covering {1,2}, Q covering {2,3}, R covering {1,3}. All columns must be covered. Which statements are true?

**Candidates**

**I.** P is essential because it covers two columns.

**II.** No prime implicant is essential.

**III.** Two rows suffice to cover all columns.

**IV.** The absence of an essential prime implicant means no cover exists.

A. II and IV  
B. II and III  
C. III and IV  
D. I and II  

### Q29. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A rectangle is cut along a straight segment joining the midpoint of its top side to its bottom-left corner. The resulting triangle and quadrilateral are separated without further cuts. What is the ratio of the triangle's area to the quadrilateral's area?

A. 1:2  
B. 1:3  
C. 1:4  
D. 2:3  

### Q30. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

What pair of values is printed? Assume C integer arithmetic is exact for the values used.

```c
#include <stdio.h>
int main(void) {
    int a[] = {2,4,6,8};
    int *p = a + 1;
    int **q = &p;
    (*q)++;
    **q += *(p-1);
    printf("%d %d", a[2], (int)(p-a));
}
```

A. 6 1  
B. 10 1  
C. 10 2  
D. 12 2  

### Q31. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A deterministic pushdown automaton recognizes balanced parentheses by pushing on '(' and popping on ')', rejecting a pop from an empty stack. Acceptance requires the stack to be empty at end of input. Which statements are correct?

**Candidates**

**I.** The empty string is accepted.

**II.** Equal total counts of '(' and ')' guarantee acceptance.

**III.** Every prefix of an accepted string has at least as many '(' as ')'.

**IV.** The string '())(' is accepted.

A. I and III  
B. I and IV  
C. II and III  
D. II and IV  

### Q32. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A NAT keeps an expiring UDP mapping from an internal endpoint to a public endpoint. After it expires, the same public endpoint is assigned to a different internal endpoint. A delayed incoming datagram addressed to the reused public endpoint then arrives. Assume mapping lookup uses only the destination public endpoint. Which statement is correct?

A. The datagram necessarily reaches the original internal endpoint.  
B. The NAT can deliver it to the newly mapped endpoint because the datagram carries no mapping-generation identifier used by this lookup.  
C. UDP sequence numbers universally prevent this.  
D. The mapping can never expire while datagrams are delayed.  

### Q33. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A machine maps every integer n to an integer f(n). Tests establish f(1)=2, f(2)=4 and f(3)=6; no other restriction on f is given. Which claim is justified?

A. f(4) must equal8.  
B. f is necessarily linear.  
C. The observations are consistent with f(n)=2n but do not uniquely establish it.  
D. No function can satisfy all three observations.  

### Q34. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A finite monoid M has identity e and satisfies left cancellation: ax=ay implies x=y for all a,x,y in M. Which statements follow?

A. For fixed a, the map x↦ax is a bijection on M.  
B. Every a has a right inverse b with ab=e.  
C. Such a b also satisfies ba=e.  
D. The conclusion that every element is invertible follows by the same finite-cardinality argument for arbitrary infinite monoids.  

### Q35. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A Boolean cover-selection chart contains candidate rows P and Q. P covers{u,v} at cost3; Q covers{u,v,w} at cost2. The objective is minimum total cost, and selecting a row has no effect except covering its columns. Which statements are correct?

**Candidates**

**I.** An optimal cover can always be chosen without P.

**II.** Replacing P by Q in a cover cannot uncover a column and cannot increase cost.

**III.** P must be retained merely because some of its columns also appear in Q.

**IV.** The same dominance conclusion follows if Q instead costs5, solely from its greater coverage.

A. I and II  
B. I and III  
C. I and IV  
D. II and III  

### Q36. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

At a scheduling decision, nonpreemptive highest-response-ratio-next uses score(waiting time+service time)/service time. Ready jobs P,Q,R have(waiting,service) pairs(6,3),(8,4),(5,1). Which job is selected?

A. P  
B. Q  
C. R  
D. All have equal score.  

### Q37. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An unsigned w-bit subtraction is implemented as A+(bitwise NOT B)+1, with the final carry-out retained. Which statements are correct?

**Candidates**

**I.** The low w bits equal(A−B) modulo2^w.

**II.** Carry-out1 indicates no unsigned borrow under this convention.

**III.** Carry-out1 necessarily indicates signed overflow.

**IV.** The low result bits alone always reveal whether unsigned borrowing occurred.

A. II and III  
B. II and IV  
C. I and II  
D. III and IV  

### Q38. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A connected undirected graph has distinct edge weights, and e is the unique heaviest edge on a cycle. Which statements are correct?

**Candidates**

**I.** Every spanning tree contains e.

**II.** Deleting e leaves the graph connected.

**III.** No minimum spanning tree contains e.

**IV.** e must be the heaviest edge of the entire graph.

A. II and IV  
B. III and IV  
C. I and II  
D. II and III  

### Q39. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A compiler lowers the condition (p!=0) AND ((*p)>0) using short-circuit evaluation. The pointer p may be null. Which statements are correct?

**Candidates**

**I.** The dereference may be skipped when p is null.

**II.** Evaluating both operands before combining their Boolean values always preserves behaviour.

**III.** A control-flow edge can bypass the dereference after a false first test.

**IV.** The second comparison must be evaluated before the first comparison.

A. I and III  
B. III and IV  
C. I and II  
D. I and IV  

### Q40. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An editor wants to say that the archivist digitized the files and then found them easier to search. Which revision correctly expresses that meaning without a dangling modifier?

A. Having digitized the files, searching was easier for the archivist.  
B. Having digitized the files, the search facility became faster.  
C. Having digitized the files, the archivist found them easier to search.  
D. Having digitized the files, the documents were easier for the archivist to search.  

### Q41. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A fractional knapsack permits dividing items; all weights and values are positive. Which statements are correct?

**Candidates**

**I.** Sorting by decreasing value/weight yields an optimal packing.

**II.** Sorting by decreasing absolute value always yields an optimal packing.

**III.** With distinct ratios, an optimum produced by the ratio rule has at most one partially selected item.

**IV.** The same ratio rule is guaranteed optimal when items become indivisible.

A. I and IV  
B. II and III  
C. I and III  
D. II and IV  

### Q42. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

L is context-free and R is regular. Which languages are necessarily context-free?

A. L∩R  
B. L∪R  
C. The complement of L  
D. The concatenation LR  

### Q43. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A real function f is defined on a neighbourhood of0. Which statements are correct?

**Candidates**

**I.** Differentiability at0 implies continuity there.

**II.** Continuity at0 implies differentiability there.

**III.** If both one-sided derivatives at0 exist as finite real numbers, f is continuous at0 even if those derivatives differ.

**IV.** Equal finite one-sided derivatives at0 are insufficient for differentiability there.

A. I and III  
B. II and IV  
C. III and IV  
D. I and II  

### Q44. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A ternary ER relationship Assignment(Employee,Project,Role) records who fills each role on each project. Every (Project,Role) pair has at most one assigned employee. An employee may fill several roles on the same project, and may work on several projects. There are no other key constraints. Which statements hold?

**Candidates**

**I.** (Project,Role) is a candidate key of Assignment.

**II.** (Employee,Project) is necessarily a candidate key.

**III.** Two assignments with the same project and role but different employees violate the constraint.

**IV.** Replacing the relationship by Employee–Project alone preserves all assignment information.

A. III and IV  
B. I and III  
C. I and II  
D. I and IV  

### Q45. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

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

### Q46. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Let P be the set of all subsets of {a,b,c}, ordered by inclusion. Remove only {a,b,c}, keeping the other seven elements. Which statements hold in the resulting poset?

**Candidates**

**I.** Every pair still has a greatest lower bound.

**II.** Every pair still has a least upper bound.

**III.** The empty set remains the least element.

**IV.** There is a greatest element.

A. I and IV  
B. II and III  
C. II and IV  
D. I and III  

### Q47. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Over a finite candidate relation C(x) and a finite required relation S(y), query Q selects candidates satisfying FOR ALL y(S(y) IMPLIES R(x,y)). Query P instead requires FOR ALL y(S(y) AND R(x,y)), where the quantified domain is infinite and S is finite. Which statement holds when S is empty and C is nonempty?

A. Both queries return C.  
B. Q returns C, while P returns no candidates.  
C. Q returns no candidates, while P returns C.  
D. Both queries return no candidates.  

### Q48. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

In a tabular Boolean minimization, a dash in a four-bit cube denotes a free variable. The ON-set is {0,1,2,3,8,9}, the don't-care set is {10}, and all remaining minterms are OFF. Which operations are valid? A combined cube must contain no OFF minterm.

**Candidates**

**I.** Combine 000- and 001- to obtain 00--.

**II.** Combine 00-- and 100- to obtain -0--.

**III.** Combine 00-0 and 10-0 to obtain -0-0.

**IV.** Combine -00- and -010 to obtain -0--.

A. II and IV  
B. I and III  
C. III and IV  
D. I and II  

### Q49. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A regular file has two hard links, p and q, and is open through descriptor d. No other links or opens exist. After both p and q are unlinked, which statement describes ordinary Unix file-lifetime semantics?

A. The file's contents must be reclaimed immediately, invalidating d.  
B. d can still access the file, and final reclamation waits for the last open reference to close.  
C. Unlinking q automatically creates a new pathname for the file.  
D. Unlinking p removes q as a directory entry too.  

### Q50. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“The panel gave the proposal a qualified endorsement: it supported the idea, provided that the budget and access arrangements were revised.” What does “qualified” mean here?

A. Issued by a person holding a professional certificate.  
B. Limited by stated conditions.  
C. Completely withdrawn.  
D. Expressed without reservation.  

---

## ANSWER KEY — SET 018

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MSQ | 1 | A, B, C |
| 2 | MSQ | 2 | A, B, D |
| 3 | MSQ | 1 | A, B, D |
| 4 | MSQ | 2 | A, B, D |
| 5 | MCQ | 1 | D |
| 6 | MCQ | 2 | B |
| 7 | MSQ | 1 | A, C, D |
| 8 | MSQ | 2 | A, B, D |
| 9 | MSQ | 1 | A, C, D |
| 10 | MCQ | 1 | D |
| 11 | MCQ | 2 | C |
| 12 | MSQ | 1 | A, C, D |
| 13 | MSQ | 1 | A, C, D |
| 14 | MSQ | 2 | A, C, D |
| 15 | MSQ | 1 | B, C, D |
| 16 | MSQ | 1 | B, C, D |
| 17 | MSQ | 2 | B, C, D |
| 18 | MSQ | 2 | A, C, D |
| 19 | MSQ | 2 | A, B, D |
| 20 | MSQ | 1 | B, C, D |
| 21 | MSQ | 1 | B, C, D |
| 22 | MCQ | 2 | D |
| 23 | MCQ | 2 | B |
| 24 | MSQ | 1 | A, C, D |
| 25 | MSQ | 1 | A, C, D |
| 26 | MCQ | 2 | D |
| 27 | MSQ | 1 | A, B, D |
| 28 | MCQ | 1 | B |
| 29 | MSQ | 1 | A, C, D |
| 30 | MSQ | 2 | A, B, D |
| 31 | MCQ | 1 | A |
| 32 | MSQ | 1 | A, C, D |
| 33 | MSQ | 1 | A, B, D |
| 34 | MCQ | 2 | D |
| 35 | MCQ | 2 | A |
| 36 | MSQ | 1 | A, B, D |
| 37 | MCQ | 1 | C |
| 38 | MCQ | 1 | D |
| 39 | MCQ | 1 | A |
| 40 | MSQ | 2 | A, B, D |
| 41 | MCQ | 2 | C |
| 42 | MCQ | 2 | C |
| 43 | MCQ | 1 | A |
| 44 | MCQ | 1 | B |
| 45 | MCQ | 2 | C |
| 46 | MCQ | 2 | D |
| 47 | MSQ | 2 | A, C, D |
| 48 | MCQ | 2 | B |
| 49 | MSQ | 1 | A, C, D |
| 50 | MSQ | 1 | A, C, D |
