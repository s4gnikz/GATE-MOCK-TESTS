# GATE CS — Additional Practice Set 016

**Questions:** 50  
**Maximum marks:** 76

Read the task above each embedded question carefully. For an invalid-answer task, select options that do not correctly answer the embedded question. For a pair task, select the pair containing all valid candidates. MCQ has one correct choice; MSQ requires all correct choices. The answer key follows Q50.

### Q1. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An open-addressed hash table has seven slots and uses h1(k)=k mod 7 and h2(k)=1+(k mod 5), probing (h1(k)+j*h2(k)) mod 7 for j=0,1,... . Keys 10,17,24 are inserted in that order into an empty table. Key 10 is then deleted and its slot marked with a tombstone. Which statements are correct?

**Candidates**

**I.** Searching for 24 must continue past the tombstone.

**II.** Replacing that tombstone with a never-used marker preserves all successful searches.

**III.** A subsequent insertion of absent key 31 may reuse the tombstone slot.

**IV.** The deletion permanently reduces the maximum number of keys the table can hold to six.

A. I and IV  
B. II and III  
C. I and III  
D. II and IV  

### Q2. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A system has two resource types A and B. It uses the Banker's safety test. Current allocation and maximum claims are:

| Process | Allocation (A,B) | Maximum (A,B) |
|---|---|---|
| P0 | (1,0) | (2,2) |
| P1 | (0,1) | (1,2) |
| P2 | (1,1) | (3,1) |

The available vector is (1,1). P0 requests (0,1). The request is within its remaining claim and the available resources. Which conclusion is correct?

A. Grant it: P0,P1,P2 is a safe sequence afterward.  
B. Grant it: P2,P1,P0 is a safe sequence afterward.  
C. Defer it: the present state is safe, but the tentative grant is unsafe.  
D. Defer it: the present state is already unsafe.  

### Q3. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For real t let

```text
A(t) = [1  2  1]
       [2  t  3]
       [1  3  1].
```

Use Doolittle elimination, with unit diagonal in L and no row exchanges unless an option explicitly permits one. Which statements are correct?

**Candidates**

**I.** det(A(t))=-1 for every real t.

**II.** An unpivoted factorization A=LU with unit lower-triangular L exists for every real t.

**III.** At t=4, exchanging rows 2 and 3 after eliminating column 1 allows elimination to finish without a zero pivot.

**IV.** At t=5, the final diagonal entry U33 is 1.

A. I and III  
B. II and IV  
C. III and IV  
D. I and II  

### Q4. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Two transactions each increment the same data item x by reading it and later writing the incremented value. Both initially hold compatible shared locks on x and then request an upgrade to an exclusive lock without releasing their shared locks. A transaction retains every lock until commit. Which statement is correct?

A. The upgrades can deadlock even though retaining locks until commit prevents another transaction from reading an uncommitted write.  
B. The second upgrade must succeed because shared locks are compatible.  
C. Releasing each shared lock before requesting its exclusive lock always preserves two-phase locking.  
D. If both transactions instead request an exclusive lock before reading x and hold it until commit, a lost update remains possible in a completed execution.  

### Q5. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A hash table has indices 0–6, hash h(k)=k mod 7, and linear probing. Insert 10,17,24 into an empty table, then delete 17 by leaving a tombstone. A successful search for 24 must continue past tombstones. Afterwards insert 31, known absent, reusing the first available tombstone. What are the number of slots inspected in the search for 24 and the index occupied by 31?

A. (2,4)  
B. (3,4)  
C. (3,6)  
D. (2,5)  

### Q6. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A binary floating-point system has four significant bits including the leading 1, unbounded exponents, and round-to-nearest with ties to even after each addition. Starting at x=8, perform x=x+0.5 sixteen times. Which statements are correct?

A. The final stored x is 8.  
B. The exact real-arithmetic result would be 16.  
C. Every one of the sixteen additions is exact in this format.  
D. Instead adding 2 to the initial x four times gives stored result 16.  

### Q7. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An optimizer considers reusing a+b across a function call. Arithmetic is exact. Which conditions are sufficient for this reuse to preserve the expression value?

A. a and b are unchanged local scalars whose addresses have never escaped, and the called function has no access to them.  
B. a and b are mutable globals, and the function's effects are unknown.  
C. The function is proven not to modify either operand, directly or indirectly.  
D. The expression text is identical before and after the call, regardless of side effects.  

### Q8. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A ternary relation R(S,P,J) contains (s1,p1,j1),(s1,p2,j2),(s2,p1,j2). Form the natural join of its three binary projections on SP, SJ and PJ, using set semantics. Which statements are correct?

A. The join has four tuples.  
B. The join contains the spurious tuple (s1,p1,j2).  
C. Joining all binary projections of any ternary relation always recovers exactly that relation.  
D. The original R satisfies SP→J.  

### Q9. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An undirected connected graph has distinct edge weights except that two edges share a weight. Which assertion is necessarily true?

A. It has at least two minimum spanning trees.  
B. Every maximum-weight edge is absent from every minimum spanning tree.  
C. Any edge that is uniquely lightest across some cut belongs to every minimum spanning tree.  
D. Kruskal's algorithm fails unless all weights are distinct.  

### Q10. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Choose the word that best completes the sentence: “The committee accepted the proposal, ___ its concern about the short implementation period.”

A. because  
B. notwithstanding  
C. therefore  
D. consequently  

### Q11. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A proposed undecidability proof transforms a machine M and input w into a recognizer N that, on every input x, simulates M on w and accepts x if that simulation halts. It then claims that testing whether L(N) is regular decides whether M halts on w. What is the flaw?

A. The construction requires knowing in advance whether M halts.  
B. Both possible languages of N are regular, so the test does not distinguish halting from nonhalting.  
C. N always recognizes a nonregular language.  
D. A recognizer cannot simulate another machine on a fixed input.  

### Q12. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A SQL column x has constraint `CHECK (x>0)` but no NOT NULL constraint. Under standard CHECK semantics, which values satisfy the constraint?

A. Positive integers only.  
B. Positive integers and NULL.  
C. Zero, positive integers, and NULL.  
D. Every integer and NULL.  

### Q13. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A square's side is increased by 10%. A circle's radius is increased by 10%. Which pair gives the percentage increases in their areas?

A. 10%,10%  
B. 20%,20%  
C. 21%,21%  
D. 21%,10%  

### Q14. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A basic block ends with `x=a+b; y=x*c; x=0; return y;`, using exact scalar arithmetic and no externally observable intermediate assignments. Which first assignment is dead solely because x is overwritten later?

A. x=a+b is dead.  
B. y=x*c is dead.  
C. Neither of these assignments is dead: y uses the first x value and return uses y.  
D. Both are dead.  

### Q15. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Two established TCP connections terminate at the same server IPv4 address and local port. Which statements are correct?

**Candidates**

**I.** They may be distinguished by different remote IPv4 addresses or remote ports.

**II.** The shared local port alone forces the two connections to be the same connection.

**III.** The connection-identifying four-tuple includes both endpoint addresses and both endpoint ports.

**IV.** Every established server-side connection must use a different local port.

A. I and III  
B. I and II  
C. I and IV  
D. II and III  

### Q16. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An open-addressed hash table of size 10 uses probes h(k,i)=(h₁(k)+4i) mod 10. A key has h₁(k)=1. Which statement is correct?

A. Its probe sequence visits all ten slots before repeating.  
B. It visits exactly five slots, so insertion can fail while some slots remain empty.  
C. It visits only slot 1.  
D. Its sequence depends on the values stored in occupied slots.  

### Q17. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A square paper is folded once along its vertical midline. A small circular hole is punched through both layers away from the fold and away from the edges. After unfolding, which statement must hold about the two holes?

A. They are images of each other under reflection in the fold line.  
B. They necessarily lie on the fold line.  
C. Their distance apart equals the side of the original square.  
D. Their positions are related by a 90-degree rotation about the centre for every punch location.  

### Q18. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Two processes P,Q use single-instance resources A,B. P acquires A then requests B; Q acquires B then requests A. Resources cannot be preempted. Which modifications prevent deadlock in every execution of these two processes?

**Candidates**

**I.** Require both to acquire A before acquiring B.

**II.** Require a process to acquire both resources atomically or acquire neither.

**III.** Merely increase each process's CPU priority after it blocks.

**IV.** Allow each process to hold its first resource indefinitely while repeatedly requesting the second.

A. II and IV  
B. III and IV  
C. I and III  
D. I and II  

### Q19. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

To use the pumping lemma for context-free languages to prove non-context-freeness, a proof must handle which choice of decomposition w=uvxyz?

A. Only the lexicographically first decomposition.  
B. Every decomposition satisfying |vxy|≤p and |vy|>0, after choosing a suitable w with |w|≥p.  
C. Only decompositions with v=y=ε.  
D. No decomposition, because choosing a long word is sufficient.  

### Q20. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In C, `int a[3]={5,6,7}; int *p=a+3;` is executed. Which subsequent operation is valid by the one-past-the-end pointer rule?

A. Evaluate *p.  
B. Evaluate *(p-1).  
C. Form p+1 and dereference it.  
D. Write p[0]=8.  

### Q21. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

In tabular Boolean minimization, a dash represents an eliminated variable. A direct combination is allowed when two patterns have identical dash positions and differ in exactly one nondash bit. Which pairs can be directly combined in a single step?

**Candidates**

**I.** 01-10 and 01-11

**II.** 01-10 and 011-0

**III.** 0--10 and 1--11

**IV.** 0--10 and 1--10

A. I and III  
B. II and III  
C. I and IV  
D. II and IV  

### Q22. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Boolean function F=(x+y)(x+z). Which expressions are equivalent to F?

**Candidates**

**I.** x+yz

**II.** x(y+z)

**III.** (x+y)(x+z)(x+y+z)

**IV.** xy+xz

A. II and III  
B. II and IV  
C. III and IV  
D. I and III  

### Q23. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A mutex is held while a thread updates two fields that jointly maintain an invariant. Why can protecting only the first field's assignment be insufficient?

A. Another thread may observe the intermediate inconsistent pair before the second assignment.  
B. A mutex can protect only constant variables.  
C. Two fields always update atomically without synchronization.  
D. Locking necessarily prevents either assignment from executing.  

### Q24. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For A with rows (0,1),(1,0), which statements are true?

**Candidates**

**I.** A is nonsingular.

**II.** A has an LU factorization with unit-diagonal lower-triangular L and upper-triangular U without any row permutation.

**III.** Swapping the rows permits such an LU factorization.

**IV.** Every nonsingular matrix must permit elimination without pivoting.

A. III and IV  
B. I and III  
C. I and II  
D. I and IV  

### Q25. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A bounded-buffer implementation starts empty with semaphores empty=N, full=0, mutex=1, where N>0. The producer executes wait(empty),wait(mutex),insert,signal(mutex),signal(full). The consumer incorrectly executes wait(mutex),wait(full),remove,signal(empty),signal(mutex). Which statements are correct?

**Candidates**

**I.** If the consumer acquires mutex first, it can block on full while preventing the producer from acquiring mutex.

**II.** The given order is guaranteed deadlock-free because every semaphore is eventually signalled in the source code.

**III.** Moving the consumer's wait(full) before wait(mutex), leaving its remaining operations in order, removes this particular deadlocking acquisition order.

**IV.** Initializing full to N correctly represents the stated initially empty buffer.

A. I and II  
B. I and IV  
C. I and III  
D. II and III  

### Q26. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

What is the tight asymptotic running time of the following code? Each work() and each loop-control operation costs constant time. Arithmetic is exact and n is a positive integer.

```text
k = 1
for i = 1 to n:
    if i == k:
        for j = 1 to i:
            work()
        k = 2*k
```

A. Θ(log n)  
B. Θ(n log n)  
C. Θ(n)  
D. Θ(n²)  

### Q27. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Which statements about socket receive results are correct? Calls request a positive number of bytes and encounter no errors unless explicitly stated.

**Candidates**

**I.** On a connected TCP stream, returning zero after buffered input is exhausted indicates an orderly end of incoming data.

**II.** Each successful TCP receive must return exactly one complete application message.

**III.** Receiving a zero-length UDP datagram can return zero without implying that the sender has closed a connection.

**IV.** TCP preserves the sender's write-call boundaries as receive-call boundaries.

A. I and III  
B. II and III  
C. II and IV  
D. III and IV  

### Q28. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“The disinterested adjudicator sanctioned the revised procedure, while remaining critical of its cost.” In this sentence, disinterested means impartial and sanctioned means approved. Which paraphrase preserves both meanings and the final qualification?

A. The bored adjudicator punished the revision because of its cost.  
B. The impartial adjudicator rejected the procedure and praised its cost.  
C. The adjudicator approved the procedure only after losing interest in all its consequences.  
D. The impartial adjudicator approved the procedure but still criticized its cost.  

### Q29. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An eight-bit binary floating-point encoding has one sign bit, a three-bit biased exponent and four fraction bits, with the usual sign-and-magnitude ordering of finite magnitudes. Consider only finite, nonzero represented values. Let raw be the unsigned eight-bit encoding. Define T(raw) as the eight-bit bitwise complement of raw for negative values, and raw XOR 0x80 for positive values. Which statements are true?

**Candidates**

**I.** Sorting raw as unsigned integers gives increasing numerical order across both signs.

**II.** Within positive values, unsigned raw order agrees with numerical order.

**III.** Within negative values, larger unsigned raw always represents a numerically larger value.

**IV.** Sorting T(raw) as unsigned integers gives increasing numerical order across both signs.

A. III and IV  
B. I and II  
C. II and IV  
D. I and III  

### Q30. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Records carry keys(city,year) and a distinct arrival number. The required order is ascending city, then ascending year, with original arrival order retained when both keys tie. Only single-key sorts are available. Which procedures always meet the requirement?

**Candidates**

**I.** Stable sort by year, then stable sort by city.

**II.** Stable sort by city, then stable sort by year.

**III.** Stable sort by arrival number, then stable sort by year, then stable sort by city.

**IV.** Arbitrary unstable sort by year, then stable sort by city.

A. I and II  
B. I and IV  
C. II and III  
D. I and III  

### Q31. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A condition variable is associated with a mutex and predicate ready. Waiting atomically releases the mutex and later reacquires it before returning. Spurious wakeups are permitted. Which pattern correctly waits for ready?

A. Lock; if not ready, wait once; use protected data; unlock.  
B. Lock; while not ready, wait; use protected data; unlock.  
C. Test ready without the mutex, then lock only if true.  
D. Lock; repeatedly test ready without releasing the mutex until it becomes true.  

### Q32. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A directed weighted graph has edges s→a(1), a→a(−1), s→t(5), and no others. Distances refer to walks, which may repeat vertices. Which statements are correct?

**Candidates**

**I.** There is a finite shortest-walk distance from s to t, equal to5.

**II.** Every vertex reachable from s has a finite shortest-walk distance.

**III.** A negative cycle reachable from s need not make the s-to-t distance unbounded below.

**IV.** The negative self-loop can be inserted into a walk from s to t.

A. II and III  
B. I and III  
C. II and IV  
D. III and IV  

### Q33. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A process has two threads sharing ordinary process resources. One thread changes a global variable and opens a file. Which statements are correct under the conventional process/thread model?

A. The other thread can access the same global variable, subject to synchronization requirements.  
B. The threads necessarily have separate virtual address spaces.  
C. The open descriptor belongs to a process-wide descriptor table shared by the threads.  
D. Each thread normally has its own execution stack and register context.  

### Q34. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An IPv4 receiver reassembles fragments using the tuple(source address,destination address,protocol,identification). Two fragments have the same identification value but different source addresses. Which statements are correct under this rule?

**Candidates**

**I.** They belong to different reassembly contexts.

**II.** Equal identification values alone are sufficient to combine them.

**III.** The fragment offset determines placement within a context rather than replacing the context key.

**IV.** Arrival order alone uniquely identifies which datagram each fragment belongs to.

A. III and IV  
B. I and II  
C. I and IV  
D. I and III  

### Q35. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Grammar S→aS | aSbS | ε uses terminals a,b. Which statements are correct?

A. Every generated string has at least as many a's as b's.  
B. Every prefix of every generated string has at least as many a's as b's.  
C. The grammar generates ba.  
D. The grammar generates aab.  

### Q36. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Resource type A has two instances and B one. P holds one A and requests B; Q holds B and requests one A. The other A instance is free. A process releases its resources after receiving its requested resource and finishing. Which statement is correct?

A. The cycle in the resource graph necessarily implies deadlock.  
B. Q can receive the free A and finish, allowing P to proceed.  
C. No process can receive any resource.  
D. P must be aborted for any progress.  

### Q37. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Functions f:A→B and g:B→C have injective composition g∘f. Which statements necessarily follow?

**Candidates**

**I.** f is injective.

**II.** g is injective on all of B.

**III.** g is injective when restricted to f(A).

**IV.** f is surjective onto B.

A. II and III  
B. II and IV  
C. I and III  
D. III and IV  

### Q38. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For Boolean variables x,y,z, let F=(x AND y) OR ((NOT x) AND z). When y=z, which expression always equals F?

A. x  
B. NOT y  
C. x XOR y  
D. y  

### Q39. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A language has lexical nesting. Procedure Outer defines local x and nested procedure Inner, whose body references x. Inner is called by an unrelated procedure Caller while Outer remains active. Which link is needed to find the lexically enclosing activation containing x?

A. A dynamic link to Caller alone  
B. A static link to Outer's activation  
C. A link to whichever activation was created most recently  
D. A link to the global symbol table alone  

### Q40. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An undirected connected graph may have equal edge weights. For one edge e, there is a cut for which e is the unique lightest crossing edge. Which statements must hold?

**Candidates**

**I.** Every minimum spanning tree contains e.

**II.** e is the unique lightest edge in the entire graph.

**III.** If a spanning tree omits e, adding e creates a cycle containing another edge crossing that cut.

**IV.** The graph has a unique minimum spanning tree.

A. I and II  
B. I and III  
C. I and IV  
D. II and III  

### Q41. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

R(A,B,C) has exactly the functional dependencies implied by A→B and B→A. Which statements are correct?

**Candidates**

**I.** AC and BC are candidate keys.

**II.** A alone is a candidate key.

**III.** R is in3NF.

**IV.** R is in BCNF.

A. I and IV  
B. II and III  
C. I and III  
D. II and IV  

### Q42. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A PDA recognizes L and a DFA recognizes R over the same alphabet. To recognize L∩R, one uses a product control state with the PDA's original stack. Which statements are correct?

**Candidates**

**I.** Consuming one input symbol updates both components according to that symbol.

**II.** Every epsilon transition of the PDA must consume a symbol in the DFA.

**III.** One stack suffices for this construction.

**IV.** A second unbounded stack is necessary to remember the DFA's state.

A. II and III  
B. II and IV  
C. III and IV  
D. I and III  

### Q43. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An SQL integer column x has CHECK(x>0) but no NOT NULL constraint. A CHECK passes when its condition is TRUE or UNKNOWN. Which statements are correct?

**Candidates**

**I.** A row with x=NULL can satisfy this CHECK.

**II.** Every non-NULL value satisfying this CHECK is positive.

**III.** The CHECK alone excludes NULL values.

**IV.** Adding NOT NULL would impose no additional restriction.

A. I and II  
B. II and IV  
C. III and IV  
D. I and III  

### Q44. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For real numbers a,b, define a⋆b=2a+b. Which identities or implications hold for all real a,b,c?

**Candidates**

**I.** (a⋆b)⋆c=a⋆(b⋆c)

**II.** a⋆b=b⋆a

**III.** If a⋆b=a⋆c, then b=c.

**IV.** a⋆(b+c)=(a⋆b)+c

A. II and IV  
B. III and IV  
C. I and II  
D. I and III  

### Q45. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Relations R(x) and S(x) are finite subsets of an infinite domain D. In the following tuple-calculus formulas, x is the only free variable and quantifiers range over D. Which formulas necessarily define finite result sets for every finite R,S?

**Candidates**

**I.** R(x) AND NOT S(x)

**II.** NOT R(x) AND NOT S(x)

**III.** EXISTS y (R(y) AND x=y)

**IV.** FOR ALL y (S(y) IMPLIES x=y)

A. I and II  
B. I and IV  
C. I and III  
D. II and III  

### Q46. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A compiler optimizes signed integer expressions. In this question, signed overflow traps, division by zero traps, and expressions have no side effects other than such traps. Which replacements preserve both value and whether a trap occurs for every integer x in the representable range?

**Candidates**

**I.** x−x → 0

**II.** x/x → 1

**III.** x*0 → 0

**IV.** (x+1)−1 → x

A. I and IV  
B. II and III  
C. II and IV  
D. I and III  

### Q47. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A directed graph permits parallel edges. Its adjacency-list representation stores one entry per edge, while its Boolean adjacency matrix stores only whether at least one edge exists for each ordered vertex pair. Which statements hold?

A. The Boolean matrix alone may not determine the number of edges.  
B. Summing entries in a Boolean matrix row always gives the outdegree when parallel edges count separately.  
C. Reachability is unchanged if parallel edges are collapsed to one edge.  
D. Two different edge multisets can have the same Boolean adjacency matrix.  

### Q48. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A processor issues instructions out of order but commits their architectural results in program order using a reorder buffer. Which mechanism chiefly prevents a younger completed instruction from exposing its architectural result before an older faulting instruction is resolved?

A. In-order commit from the reorder buffer.  
B. Issuing every ready instruction as soon as possible.  
C. Increasing the number of execution units.  
D. Predicting every branch as taken.  

### Q49. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

The input consists of a deterministic Turing machine M, a finite word w, and a nonnegative integer k. Which questions are decidable?

**Candidates**

**I.** Does M halt on w within k transitions?

**II.** Does M ever halt on w?

**III.** Does M enter an accepting state during its first k transitions, including its initial configuration?

**IV.** Is the language accepted by M empty?

A. III and IV  
B. I and II  
C. I and III  
D. I and IV  

### Q50. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

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

---

## ANSWER KEY — SET 016

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | C |
| 2 | MSQ | 2 | A, B, D |
| 3 | MCQ | 1 | A |
| 4 | MSQ | 2 | B, C, D |
| 5 | MSQ | 1 | A, C, D |
| 6 | MCQ | 2 | C |
| 7 | MSQ | 1 | B, D |
| 8 | MCQ | 2 | C |
| 9 | MSQ | 1 | A, B, D |
| 10 | MSQ | 1 | A, C, D |
| 11 | MSQ | 2 | A, C, D |
| 12 | MSQ | 1 | A, C, D |
| 13 | MSQ | 2 | A, B, D |
| 14 | MSQ | 2 | A, B, D |
| 15 | MCQ | 1 | A |
| 16 | MSQ | 1 | A, C, D |
| 17 | MSQ | 1 | B, C, D |
| 18 | MCQ | 2 | D |
| 19 | MSQ | 1 | A, C, D |
| 20 | MSQ | 1 | A, C, D |
| 21 | MCQ | 2 | C |
| 22 | MCQ | 2 | D |
| 23 | MSQ | 1 | B, C, D |
| 24 | MCQ | 1 | B |
| 25 | MCQ | 2 | C |
| 26 | MSQ | 2 | A, B, D |
| 27 | MCQ | 1 | A |
| 28 | MSQ | 2 | A, B, C |
| 29 | MCQ | 2 | C |
| 30 | MCQ | 2 | D |
| 31 | MSQ | 1 | A, C, D |
| 32 | MCQ | 1 | B |
| 33 | MCQ | 2 | B |
| 34 | MCQ | 2 | D |
| 35 | MCQ | 2 | C |
| 36 | MSQ | 1 | A, C, D |
| 37 | MCQ | 1 | C |
| 38 | MSQ | 1 | A, B, C |
| 39 | MSQ | 1 | A, C, D |
| 40 | MCQ | 2 | B |
| 41 | MCQ | 2 | C |
| 42 | MCQ | 2 | D |
| 43 | MCQ | 1 | A |
| 44 | MCQ | 2 | B |
| 45 | MCQ | 2 | C |
| 46 | MCQ | 2 | D |
| 47 | MCQ | 2 | B |
| 48 | MSQ | 1 | B, C, D |
| 49 | MCQ | 1 | C |
| 50 | MCQ | 2 | A |
