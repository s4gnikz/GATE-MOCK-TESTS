# GATE CS — Additional Practice Set 005

**Questions:** 50  
**Maximum marks:** 80

Read the task above each embedded question carefully. For an invalid-answer task, select options that do not correctly answer the embedded question. For a pair task, select the pair containing all valid candidates. MCQ has one correct choice; MSQ requires all correct choices. The answer key follows Q50.

### Q1. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Two teams produce identical items. The table lists working hours and completed items in two months. Overall productivity means total completed items divided by total working hours.

| Team | Month 1 hours | Month 1 items | Month 2 hours | Month 2 items |
|---|---:|---:|---:|---:|
| A | 40 | 400 | 60 | 660 |
| B | 60 | 900 | 40 | 640 |

What is the percentage change in overall productivity from Month 1 to Month 2?

A. 0%  
B. 8% increase  
C. 10% increase  
D. 12% increase  

### Q2. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

The following pseudocode uses static (lexical) scoping and ordinary stack activation records. Main contains A; A contains the sibling procedures B and C. Each call has fresh local variables, assignments to a variable found in an enclosing activation modify that variable, and the two assignments in the recursive case of B execute in their displayed order.
```text
procedure Main():
    local x = 20
    procedure A():
        local x = 4
        procedure C():
            x = x + 1
            return x
        procedure B(n):
            local x = 100 + n
            if n == 0:
                return C()
            t = B(n-1)
            u = C()
            return t + u
        return B(2)
    print A()
```
Here t and u are local temporaries of each B activation. What is printed?

A. 18  
B. 306  
C. 15  
D. 66  

### Q3. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Choose the revision that is grammatically correct and preserves both intended meanings: Mira did not leave earlier, so she missed the train; Mira, not the meeting, reached the office late.

Original: “If Mira had left earlier, she will catch the train. Having reached the office late, the meeting had already begun.”

A. If Mira left earlier, she will catch the train. Having reached the office late, the meeting began.  
B. If Mira had left earlier, she would have caught the train. When Mira reached the office late, the meeting had already begun.  
C. If Mira had left earlier, she would catch the train. Having reached the office late, the meeting had begun.  
D. If Mira would have left earlier, she caught the train. When the meeting reached the office late, Mira had begun.  

### Q4. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let e_n be the number of binary strings of length n that have no consecutive 1s and contain an even number of 1s. The empty string is counted, so e_0=1. Which formal ordinary generating function E(x)=sum over n>=0 of e_n*x^n is correct?

A. (1+x)/(1-x-x^2)  
B. (1-x+x^3)/(1-2x+x^2-x^4)  
C. 1/(1-x-x^2)  
D. (1-x)/(1-2x+x^2-x^4)  

### Q5. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

After a library extended its evening hours, the number of evening visits increased, while total weekly visits remained unchanged. A report concludes that the extension attracted additional weekly visitors. Which criticism is best supported by the information given?

A. Evening visits cannot increase unless weekly visits increase.  
B. Some visits may have shifted from daytime to evening, and visit counts do not identify distinct visitors.  
C. The extension must have reduced the number of distinct visitors.  
D. Every evening visitor previously visited during daytime.  

### Q6. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Every memory access first spends 1 ns at L1. An L1 miss spends an additional 9 ns at L2; an L2 miss spends another 90 ns at memory. The L1 hit probability is 0.8, and the L2 hit probability conditional on an L1 miss is 0.5. Which statements are correct?

A. The probability of an L1 miss followed by an L2 hit is 0.1.  
B. The probability of accessing main memory is 0.1.  
C. The average access time is 11.8 ns.  
D. Half of all original accesses are L2 hits.  

### Q7. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Some A are B. Every B is C. No C is D. Which conclusions necessarily follow?

**Candidates**

**I.** Every A is C.

**II.** Some A are not D.

**III.** Some D are A.

**IV.** No B is D.

A. I and IV  
B. II and III  
C. II and IV  
D. III and IV  

### Q8. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Reads return the latest preceding write in this schedule:

```text
w1(x); r2(x); w2(y); r3(y); c1; c2; c3
```

Which properties hold?

**Candidates**

**I.** Recoverability.

**II.** Cascadelessness.

**III.** Conflict serializability.

**IV.** Strictness.

A. II and IV  
B. III and IV  
C. I and II  
D. I and III  

### Q9. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In a group of 20 workers the mean daily output is 30 units. After removing the five workers with the lowest outputs, the mean of the remaining workers is 34. A second group of five workers, each producing 28 units, joins those remaining workers. What is the difference between the new 20-worker mean and the mean of the five removed workers?

A. 12.5 units  
B. 14.5 units  
C. 16 units  
D. 18 units  

### Q10. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let L={aⁱbʲcᵏ : i,j,k≥0 and i=j or j=k}. Which statement is correct?

A. L is not context-free because it contains aⁿbⁿcⁿ.  
B. L is regular because the condition uses “or.”  
C. L is context-free, but its intersection with {aⁿbⁿcⁿ:n≥0} is not context-free.  
D. L is finite.  

### Q11. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

On an eight-bit two's-complement machine, x has bits 11111011. Define arithmetic right shift as copying the sign bit and logical right shift as inserting zero. What signed values result from one arithmetic right shift and one logical right shift, respectively?

A. −2 and 125  
B. −3 and 125  
C. −3 and −3  
D. −2 and −2  

### Q12. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Three nonempty groups have mean scores 40,60,80. Their sizes are positive integers but otherwise unspecified. Which statements must hold for the combined mean μ?

**Candidates**

**I.** 40<μ<80.

**II.** μ=60.

**III.** μ can equal 60 for some group sizes.

**IV.** μ is always at least 60.

A. II and III  
B. II and IV  
C. III and IV  
D. I and III  

### Q13. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A singly linked list is 1→2→3→4→5→NULL. Pointers p and q initially refer to nodes 2 and 4. Execute the following assignments in the displayed order, with t a temporary pointer:

```text
t = p.next
p.next = q.next
q.next = t
```

Starting at node 1 afterward, what happens when next links are followed?

A. The traversal is 1,2,5 and then NULL.  
B. The traversal is 1,2,3,4,5 and then NULL.  
C. The traversal is 1,2,4,3,5 and then NULL.  
D. The traversal enters a cycle containing node 1.  

### Q14. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An algorithm outputs every unordered pair of distinct elements from an n-element input, with one constant-time operation per emitted pair. What is the tight asymptotic lower bound arising from output size alone?

A. Ω(log n)  
B. Ω(n)  
C. Ω(n log n)  
D. Ω(n²)  

### Q15. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A school introduced optional tutoring. Participants subsequently scored higher than nonparticipants. The report concludes that tutoring caused the entire observed score difference. Which additional finding most directly weakens this conclusion?

A. Participants already had higher scores before tutoring began.  
B. The tutoring sessions occurred in classrooms.  
C. Both groups took the same final examination.  
D. The report stated each group's size.  

### Q16. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A singly linked list must be reversed in place. The code maintains pointers prev,cur,next and uses three assignments per iteration after saving next=cur.next. Which order preserves access to the remaining unreversed suffix?

A. cur=cur.next; cur.next=prev; prev=cur  
B. cur.next=prev; prev=cur; cur=next  
C. prev=cur; cur=next; cur.next=prev  
D. cur.next=next; prev=next; cur=prev  

### Q17. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A language permits a function to return a nested function that refers to its local variable x. Two separate calls to the outer function return functions F and G, capturing different x variables. Both returned functions are called after the outer calls have returned. Which implementation preserves lexical scoping and separate mutable x variables?

A. Put every captured x in the same global cell.  
B. Keep each captured environment alive beyond the outer call and associate the appropriate environment with each returned function.  
C. Keep only a pointer into the outer function's discarded stack frame.  
D. Copy the current value of x anew from the most recent caller whenever F or G is invoked.  

### Q18. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

M is a finite monoid with identity e. Every element a has a right inverse b satisfying ab=e. Which statements necessarily hold?

**Candidates**

**I.** Every element has a two-sided inverse.

**II.** M is a group.

**III.** M must be commutative.

**IV.** The right inverse of an element can be chosen arbitrarily from M.

A. II and IV  
B. I and II  
C. III and IV  
D. I and III  

### Q19. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A disk scheduler uses LOOK, moving toward increasing cylinder numbers. The head is at 40; pending requests are 10,30,55,70. No further requests arrive. Which service order follows?

A. 55,70,30,10  
B. 30,10,55,70  
C. 55,30,70,10  
D. 70,55,30,10  

### Q20. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A process successfully executes a new program image through an exec-like operation with the following specified semantics: its PID is retained, its old address space is replaced, and descriptors marked close-on-exec are closed while others remain open. Which observations are possible immediately afterwards?

**Candidates**

**I.** The PID is unchanged although the executed code is different.

**II.** An unmarked file descriptor remains usable by the new program.

**III.** Every pointer into the old heap is guaranteed to remain valid with its old object.

**IV.** Every inherited descriptor must have been closed.

A. I and III  
B. I and IV  
C. II and III  
D. I and II  

### Q21. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An n-bit ALU, n≥2, computes A−B as A+(NOT B)+1. Which statements hold when carry-out is retained separately from the n-bit result?

A. Carry-out 1 indicates no borrow in unsigned subtraction.  
B. The retained result represents (A−B) modulo 2ⁿ.  
C. Unsigned borrow and signed overflow are always the same event.  
D. Signed subtraction overflow can occur when A and B have opposite signs and the result's sign differs from A's.  

### Q22. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A compiler lowers `if (p) x=a; else x=b; use(x);` to a control-flow graph. What must both branch arms do before the common use(x) block?

A. Define x along their respective paths.  
B. Execute both assignments unconditionally in source order.  
C. Eliminate the branch condition regardless of its value.  
D. Assign the same constant to x in every case.  

### Q23. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“A new policy reduced average processing time, but the study did not measure the number of incorrect decisions.” Which claim is justified by the study as described?

A. Processing became faster on average, while the effect on decision accuracy remains unmeasured.  
B. Decision accuracy necessarily improved.  
C. Every decision became faster and more accurate.  
D. Incorrect decisions necessarily increased.  

### Q24. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For the finite language L={ε,a,a²,…,a⁷}, what is the smallest positive pumping length p satisfying the regular-language pumping lemma? The lemma imposes its decomposition requirement only on words of length at least p.

A. 8  
B. 7  
C. 1  
D. No pumping length exists because the language is finite.  

### Q25. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In `x=1; x=2; print(x);`, the first assignment has no side effects apart from storing x. Why may it be removed?

A. Its value is overwritten before any use.  
B. Every assignment of the constant one is invalid.  
C. print never reads its argument.  
D. The second assignment must also be removed.  

### Q26. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A syntax-directed translation emits each operand when recognized and emits a binary operator after translating both operands. Multiplication binds more tightly than addition. What does it emit for a+b*c?

A. ab+c*  
B. +a*bc  
C. abc*+  
D. abc+*  

### Q27. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A nondeterministic PDA recognizes even-length palindromes over {a,b} by pushing an initial segment, guessing its midpoint using an epsilon transition, and then matching and popping the remaining symbols; it accepts only after consuming all input and returning to its bottom marker. Which statements are correct?

**Candidates**

**I.** Any accepting computation on abba must guess the midpoint after two input symbols.

**II.** Guessing the midpoint after one input symbol can accept abba by ignoring a mismatched stack symbol.

**III.** The word abab is rejected on every computation.

**IV.** An incorrect midpoint guess must make every computation on an actual palindrome reject.

A. II and III  
B. II and IV  
C. I and III  
D. III and IV  

### Q28. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A byte-addressed 16-bit address space contains a 16 KiB chip at 0x0000–0x3FFF and an 8 KiB chip at 0x4000–0x5FFF. Both chips use active-high enables and are fully decoded, with A15 the most significant address bit. Which statements are correct?

**Candidates**

**I.** The 16 KiB chip's enable can be NOT A15 AND NOT A14.

**II.** The 8 KiB chip's enable can be NOT A15 AND A14, without considering A13.

**III.** Exactly 32 KiB of the address space is unmapped by these chips.

**IV.** The 8 KiB chip's enable can be NOT A15 AND A14 AND NOT A13.

A. II and IV  
B. III and IV  
C. I and II  
D. I and IV  

### Q29. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Relation R(A,B,C) contains exactly (1,x,p),(1,y,q),(2,x,p),(2,y,r). Which functional dependencies hold on this relation instance?

**Candidates**

**I.** A→C

**II.** AB→C

**III.** C→A

**IV.** C→B

A. II and IV  
B. III and IV  
C. I and II  
D. I and III  

### Q30. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An8-bit ALU computes subtraction X−Y as X+(bitwise NOT Y)+1, retaining the low8 bits. Let X=10000000 and Y=00000001. Which combination is correct? Carry-out refers to the ninth bit of this addition, and signed overflow refers to two's-complement interpretation.

A. Result01111111; carry-out0; signed overflow0.  
B. Result01111111; carry-out1; signed overflow1.  
C. Result10000001; carry-out1; signed overflow0.  
D. Result01111111; carry-out0; signed overflow1.  

### Q31. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A parent creates a pipe and then forks. Both processes initially inherit both pipe ends. The parent closes its own write end and reads until EOF. The child writes some data and then becomes idle without exiting or closing either descriptor. Assume all data already written have been read. Which statements are correct?

**Candidates**

**I.** The parent's next blocking read must return EOF immediately.

**II.** The child's still-open write descriptor prevents EOF at the parent.

**III.** Closing the child's read descriptor alone is sufficient to cause EOF at the parent.

**IV.** If the child closes its write descriptor and no other write descriptors exist, the parent can observe EOF.

A. I and III  
B. I and IV  
C. II and IV  
D. II and III  

### Q32. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A TLB entry is keyed by(ASID, virtual page). A process with ASID5 terminates, leaving cached translations. A new process is assigned ASID5 with a different page table; the old translations are not invalidated. Which statements are correct?

**Candidates**

**I.** A stale entry can translate the new process's address to an old physical frame.

**II.** The ASID field by itself makes reuse safe forever.

**III.** Invalidating entries for the reused ASID before execution prevents this stale-entry problem.

**IV.** Merely changing the page-table base necessarily makes all old ASID-tagged entries miss.

A. II and III  
B. II and IV  
C. III and IV  
D. I and III  

### Q33. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Relations R(A,B)={(1,x),(1,y),(2,x)} and S(A,B)={(1,x)} use set semantics. Compare E1=projection_A(R−S) and E2=projection_A(R)−projection_A(S). Which statements are correct?

A. E1={1,2}.  
B. E2={2}.  
C. Projection always distributes over set difference.  
D. The surviving tuple(1,y) explains why1 belongs to E1 but not E2.  

### Q34. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Given two arbitrary Turing machines M1,M2 and an input w, a simulator alternates one step of each machine on w. It accepts as soon as either simulation accepts. Which statements are correct?

**Candidates**

**I.** It recognizes the union of the two recognized languages.

**II.** It always halts if neither machine accepts w.

**III.** It avoids being trapped forever in M1 before giving M2 any steps.

**IV.** It decides the intersection of the languages.

A. III and IV  
B. I and III  
C. I and II  
D. I and IV  

### Q35. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A stable sorting algorithm sorts records by a numeric key. Which statements are correct?

**Candidates**

**I.** Equal-key records retain their relative input order.

**II.** Stability alone guarantees O(n log n) running time.

**III.** Stability matters when a previous ordering among equal keys must be preserved.

**IV.** A stable sort necessarily leaves all unequal-key records in their original relative order.

A. I and II  
B. I and IV  
C. I and III  
D. II and III  

### Q36. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In a compiler's constant lattice, a join keeps a constant only if all reachable incoming values agree. A block has incoming x=5 from one reachable predecessor and x=7 from an unreachable predecessor. Which statements are correct if reachability information is used?

A. The unreachable predecessor need not force x to be nonconstant.  
B. x may be propagated as5 at the block's entry.  
C. Treating every syntactic predecessor as reachable can lose this optimization.  
D. Reachability information never affects constant propagation.  

### Q37. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Which expression is guaranteed to stay within the same C array object when a is an array of four integers and p=a+4? Forming a one-past pointer is permitted, but dereferencing it is not.

A. *p  
B. *(p−1)  
C. *(p+1)  
D. a[4]  

### Q38. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A TCP peer performs an orderly shutdown of its sending direction after transmitting some bytes. The receiver drains all those bytes. Assume no errors. Which statements are correct?

**Candidates**

**I.** A subsequent receive can return zero to indicate end-of-stream in that direction.

**II.** The receiver must treat zero as one received byte whose value is0.

**III.** A half-close does not by itself prevent the other direction from carrying data.

**IV.** TCP requires both applications to terminate immediately when one direction closes.

A. II and IV  
B. I and III  
C. III and IV  
D. I and II  

### Q39. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A lexer uses maximal munch, breaking equal-length ties by rule priority. Its tokens include INTEGER=[0-9]+, REAL=[0-9]+\.[0-9]*, and RANGE=\.\., where an escaped dot denotes a literal dot. A single dot is not a token. For input1..2, which statements are correct?

A. The first token under these rules is REAL with lexeme `1.`.  
B. Giving RANGE highest priority makes the first token INTEGER with lexeme1.  
C. After the first token, scanning encounters a dot at which no token can start.  
D. Requiring at least one digit after the dot in REAL would allow the tokenization INTEGER,RANGE,INTEGER.  

### Q40. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An application must receive exactly five bytes from a TCP stream into buf[0..4]. There are no errors or end-of-stream events. Consider this pseudocode, where recv returns a positive number of bytes actually written:

```text
n = 0
while n < 5:
    k = recv(socket, buf, 5-n)
    n = n + k
```

The sender's five bytes are A,B,C,D,E in that order. The two recv calls return2 and3 respectively. Which statements are correct?

**Candidates**

**I.** The second call overwrites the buffer's first three positions.

**II.** The loop necessarily leaves A,B,C,D,E in consecutive buffer positions.

**III.** Passing buf+n as the destination before each call repairs the placement error.

**IV.** TCP's ordered delivery guarantees that the application cannot overwrite previously received bytes.

A. I and II  
B. I and IV  
C. II and III  
D. I and III  

### Q41. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A network-layer packet is carried through two links with different link-layer protocols. No tunnelling or address translation is used. Which statements are correct?

**Candidates**

**I.** The outgoing link can use a different frame format from the incoming link.

**II.** A router must preserve the incoming link-layer checksum unchanged in the outgoing frame.

**III.** Link-specific headers may be removed and replaced while forwarding the packet.

**IV.** Changing link-layer protocol necessarily changes the application's message content.

A. I and III  
B. I and IV  
C. II and III  
D. II and IV  

### Q42. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Order the set{1,2,3,4,12} by divisibility. Which statements are correct?

A. This poset is a lattice.  
B. This lattice is distributive.  
C. The join of2 and3 is12.  
D. The meet of4 and3 is1.  

### Q43. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A report states: “The mean travel time was unchanged after the timetable revision, although individual passengers experienced both increases and decreases.” Which conclusion is supported?

A. Every passenger's travel time stayed unchanged.  
B. Equal means imply identical travel-time distributions.  
C. An unchanged aggregate measure can coexist with changes in individual outcomes.  
D. The timetable revision necessarily improved every passenger's journey.  

### Q44. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Two sorted singly linked lists have distinct prefix nodes but share the same suffix nodes. A standard in-place merge is written assuming disjoint lists: it links the smaller current node to the result, advances that list pointer, and repeats, without testing pointer equality. Which statements are correct?

**Candidates**

**I.** Shared nodes can make the merge create a cycle or fail to terminate.

**II.** If both current pointers are equal, appending that shared suffix once and terminating avoids duplicate processing of that suffix.

**III.** Equality of node values alone proves that two pointers refer to the same node.

**IV.** Sortedness alone guarantees safety of this disjoint-list merge on shared-suffix inputs.

A. III and IV  
B. I and III  
C. I and IV  
D. I and II  

### Q45. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A compiler uses a non-relational constant-propagation analysis: it tracks each variable separately and joins different constants to “not constant.” Both branches below are feasible.

```text
if p then { x=2; y=7; }
else      { x=7; y=2; }
z=x+y;
```

At the assignment to z, which description is correct?

A. The analysis proves x=2 and z=9.  
B. The analysis proves y=7 and z=9.  
C. The stated analysis cannot prove z constant, although z is always 9.  
D. z can equal 4 or 14 during execution.  

### Q46. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Over a nonempty domain, which formula is the negation of “For every x, if P(x), there exists y such that R(x,y)”?

A. For every x, P(x) and for every y, not R(x,y).  
B. There exists x such that not P(x) and there exists y with R(x,y).  
C. There exists x such that P(x) and for every y, not R(x,y).  
D. There exists x such that P(x) and there exists y with not R(x,y).  

### Q47. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Two datasets each contain three real observations. Their medians are2 and9, respectively. Combine all six observations and define the new median as the average of the third and fourth ordered observations. Which assertion is necessarily true?

A. The combined median equals5.5.  
B. The combined median lies in[2,9].  
C. The combined mean lies in[2,9].  
D. The combined median equals one of the original six observations.  

### Q48. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For a finite list of integers, operation R reverses the list, and operation N negates every entry without changing the order. A student claims that applying R then N always gives the same list as applying N then R. Which statements hold?

**Candidates**

**I.** Checking the claim on one list of length three proves it for lists of every length.

**II.** The claim holds because each final position contains the negative of the same original entry under either order.

**III.** Applying the combined operation twice restores every original list.

**IV.** The claim implies that reversing a list always leaves it unchanged.

A. II and IV  
B. III and IV  
C. I and II  
D. II and III  

### Q49. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A circular track has two concentric lane centre-lines of radii r and r+1 metres. Two runners move at equal constant speeds toward a finish on a fixed radial line. The inner runner starts on that line and runs one complete lap. The outer runner starts ahead of that line and runs the remainder of the circuit. Both start simultaneously. By how many metres along the outer lane must its start be advanced from the finish line so that the runners finish simultaneously?

A. π  
B. 2π  
C. πr  
D. 2πr  

### Q50. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An initially empty hash table has slots 0 through 6. All inserted keys have primary hash 0. For each insertion, quadratic probing visits slots i² mod 7 for i=0,1,…,6, in that order, and reports failure if all these visits find occupied slots. There are no deletions. Which statements hold?

**Candidates**

**I.** The first four keys can all be inserted.

**II.** The fifth insertion succeeds because three slots are still empty.

**III.** No insertion ever examines slot 3.

**IV.** Replacing this probe rule by i mod 7 would have the same failure point.

A. I and II  
B. I and III  
C. I and IV  
D. II and III  

---

## ANSWER KEY — SET 005

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MSQ | 2 | B, C, D |
| 2 | MSQ | 2 | B, C, D |
| 3 | MSQ | 2 | A, C, D |
| 4 | MSQ | 2 | A, C, D |
| 5 | MSQ | 1 | A, C, D |
| 6 | MCQ | 1 | D |
| 7 | MCQ | 1 | C |
| 8 | MCQ | 2 | D |
| 9 | MSQ | 2 | A, C, D |
| 10 | MSQ | 2 | A, B, D |
| 11 | MSQ | 1 | A, C, D |
| 12 | MCQ | 1 | D |
| 13 | MSQ | 2 | B, C, D |
| 14 | MSQ | 1 | A, B, C |
| 15 | MSQ | 2 | B, C, D |
| 16 | MSQ | 2 | A, C, D |
| 17 | MSQ | 2 | A, C, D |
| 18 | MCQ | 1 | B |
| 19 | MSQ | 1 | B, C, D |
| 20 | MCQ | 2 | D |
| 21 | MCQ | 2 | C |
| 22 | MSQ | 1 | B, C, D |
| 23 | MSQ | 2 | B, C, D |
| 24 | MSQ | 2 | B, C, D |
| 25 | MSQ | 1 | B, C, D |
| 26 | MSQ | 1 | A, B, D |
| 27 | MCQ | 2 | C |
| 28 | MCQ | 2 | D |
| 29 | MCQ | 2 | A |
| 30 | MSQ | 1 | A, C, D |
| 31 | MCQ | 2 | C |
| 32 | MCQ | 2 | D |
| 33 | MCQ | 2 | C |
| 34 | MCQ | 1 | B |
| 35 | MCQ | 1 | C |
| 36 | MCQ | 2 | D |
| 37 | MSQ | 2 | A, C, D |
| 38 | MCQ | 2 | B |
| 39 | MCQ | 2 | B |
| 40 | MCQ | 2 | D |
| 41 | MCQ | 1 | A |
| 42 | MCQ | 1 | B |
| 43 | MSQ | 2 | A, B, D |
| 44 | MCQ | 2 | D |
| 45 | MSQ | 1 | A, B, D |
| 46 | MSQ | 1 | A, B, D |
| 47 | MSQ | 1 | A, C, D |
| 48 | MCQ | 2 | D |
| 49 | MSQ | 1 | A, C, D |
| 50 | MCQ | 2 | B |
