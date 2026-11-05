# GATE CS 2027 — Full-Length Mock Test 091

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

### Q1. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“A library extended its opening hours. Evening attendance increased, but total daily attendance remained unchanged.” Which interpretation is consistent with both observations?

A. Some visits shifted from earlier hours to the evening.  
B. Total daily attendance necessarily increased.  
C. Earlier attendance necessarily increased too.  
D. The library must have measured attendance incorrectly.

### Q2. [1 Mark] [NAT]

Four people each leave an identical-looking umbrella in a stand. The umbrellas have different owners. At departure, each person takes one umbrella. How many assignments give exactly two people their own umbrellas?

**Answer format:** Integer.

### Q3. [1 Mark] [NAT]

A school has two classes. In the first,18 of30 students passed an examination. Across both classes,42 of60 students passed. What percentage of the second class passed?

**Answer format:** Exact percentage without the percent sign.

### Q4. [1 Mark] [NAT]

A thin square sheet occupies 0≤x≤4, 0≤y≤4. Fold the right half onto the left along x=2, then the top half onto the bottom along y=2. From the resulting folded square, remove the entire horizontal strip 0≤x≤2, 0.5<y<1 through every layer. After unfolding, how many connected pieces of paper remain? The cuts extend fully to both side edges of the folded square.

**Answer format:** Exact integer.

### Q5. [1 Mark] [MCQ]

Choose the sentence in which the opening phrase clearly modifies the intended subject and the list has parallel grammatical form.

A. After examining the records, several errors were found by Mira in dates, to calculate totals, and filing.
B. After examining the records, the totals were checked by Mira and correcting dates.
C. After examining the records, Mira corrected the dates, recalculated the totals, and reorganized the files.
D. After examining the records, correcting the dates, the totals were recalculated by Mira.

### Q6. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A fair coin selects one of two boxes. Box I contains two red balls and one blue ball; Box II contains one red ball and two blue balls. Two balls are drawn uniformly without replacement from the selected box. Given that at least one drawn ball is red, what is the probability that both are red?

A. 1/6  
B. 1/3  
C. 1/5  
D. 2/5

### Q7. [2 Marks] [MCQ]

“The disinterested adjudicator sanctioned the revised procedure, while remaining critical of its cost.” In this sentence, disinterested means impartial and sanctioned means approved. Which paraphrase preserves both meanings and the final qualification?

A. The bored adjudicator punished the revision because of its cost.
B. The impartial adjudicator rejected the procedure and praised its cost.
C. The adjudicator approved the procedure only after losing interest in all its consequences.
D. The impartial adjudicator approved the procedure but still criticized its cost.

### Q8. [2 Marks] [NAT]

Two positive numbers have product 64 and satisfy log₂x−log₂y=2. Find x+y.

**Answer format:** Integer.

### Q9. [2 Marks] [MCQ]

A conjecture states: “For every positive integer n, n²+n+41 is prime.” Which single calculation is sufficient to refute the conjecture?

A. It equals43 at n=1.
B. It equals47 at n=2.
C. It equals41² at n=40.
D. It is odd at n=3.

### Q10. [2 Marks] [NAT]

Unit cubes are stacked in four columns on a2×2 base. Heights are nonnegative integers. Maximum heights in the first and second rows are3 and1; maximum heights in the first and second columns are2 and3. What is the minimum total number of cubes consistent with these four maxima?

**Answer format:** Integer.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

An eight-slot hash table probes i² modulo8 for i=0,1,2,... when inserting a particular key. All slots reached by this sequence are occupied. What is the largest possible number of empty slots elsewhere in the table despite this insertion being unable to reach them?

**Answer format:** Integer.

### Q12. [1 Mark] [NAT]

Evaluate ∫₀¹ x/(1+x²) dx, rounded to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q13. [1 Mark] [NAT]

A signed fixed-point format stores a six-bit two's-complement integer divided by8. What real value results if the stored code011111 is incremented by1 with six-bit wraparound?

**Answer format:** Exact number.

### Q14. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let L={aⁿbⁿ:n≥0}. Which of the following is regular?

A. L  
B. L∩a*b*  
C. L∩a*b³  
D. {a,b}* minus L

### Q15. [1 Mark] [NAT]

Dataset A contains 3 observations with mean 2 and population variance 2. Dataset B contains 2 observations with mean 7 and population variance 1. What is the population variance of their combined five observations? Use division by the population size, not by one less than that size.

**Answer format:** Numeric value; 1 decimal place.

### Q16. [1 Mark] [MCQ]

A condition variable is associated with a mutex and predicate ready. Waiting atomically releases the mutex and later reacquires it before returning. Spurious wakeups are permitted. Which pattern correctly waits for ready?

A. Lock; if not ready, wait once; use protected data; unlock.
B. Lock; while not ready, wait; use protected data; unlock.
C. Test ready without the mutex, then lock only if true.
D. Lock; repeatedly test ready without releasing the mutex until it becomes true.

### Q17. [1 Mark] [MCQ]

Consider this recursive function on a positive integer n. Arithmetic is exact.

```text
f(n):
    if n == 1: return 1
    r = f(floor(n/2))
    if n is even: return 2*r
    else: return 2*r + 1
```

Which pair gives f(45) and the number of simultaneous active calls at maximum recursion depth, including the initial and base calls?

A. (45,6)  
B. (45,5)  
C. (32,6)  
D. (63,6)

### Q18. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Every memory access first spends 1 ns at L1. An L1 miss spends an additional 9 ns at L2; an L2 miss spends another 90 ns at memory. The L1 hit probability is 0.8, and the L2 hit probability conditional on an L1 miss is 0.5. Which statements are correct?

A. The probability of an L1 miss followed by an L2 hit is 0.1.  
B. The probability of accessing main memory is 0.1.  
C. The average access time is 11.8 ns.  
D. Half of all original accesses are L2 hits.

### Q19. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A binary floating-point format rounds to nearest, ties to even, with three significant bits including the leading 1. Exponents can represent all values in this question. What is the rounded representation of 1.101₂?

A. 1.10₂  
B. 1.11₂  
C. 1.00₂  
D. 10.0₂

### Q20. [1 Mark] [NAT]

An in-place transpose of a row-major 3×4 array permutes old linear index i into new linear index (i mod4)×3+floor(i/4), for 0≤i<12. Starting at index1 and repeatedly applying this permutation, how many distinct indices occur before returning to1?

**Answer format:** Exact integer.

### Q21. [1 Mark] [NAT]

Let G be the additive group of integers modulo12. Define a group homomorphism f:G→G by f(x)=8x modulo12. How many cosets of the kernel of f are there in G?

**Answer format:** Integer.

### Q22. [1 Mark] [MSQ]

Given two arbitrary Turing machines M1,M2 and an input w, a simulator alternates one step of each machine on w. It accepts as soon as either simulation accepts. Which statements are correct?

A. It recognizes the union of the two recognized languages.
B. It always halts if neither machine accepts w.
C. It avoids being trapped forever in M1 before giving M2 any steps.
D. It decides the intersection of the languages.

### Q23. [1 Mark] [MCQ]

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

### Q24. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A foreign key has two columns(x,y) and uses the stated rule: if either referencing component is NULL, no referenced-row match is required; otherwise the pair must match. Which inserted pairs can pass the foreign-key check when the referenced table is empty?

A. (NULL,5)  
B. (7,NULL)  
C. (NULL,NULL)  
D. (7,5)

### Q25. [1 Mark] [MCQ]

For n a positive power of two, count executions of `work()`:

```text
i = 1
while i <= n:
    j = 0
    while j < n:
        work()
        j = j + i
    i = 2*i
```

What is the tight asymptotic count?

A. Θ(log n)
B. Θ(n)
C. Θ(n log n)
D. Θ(n²)

### Q26. [1 Mark] [NAT]

A direct-mapped cache has four lines and starts empty. Block b maps to line b modulo4. For references0,4,0,4, how many are conflict misses after excluding the first access to each distinct block as compulsory?

**Answer format:** Integer.

### Q27. [1 Mark] [MSQ]

A simple undirected graph has six vertices, every vertex has degree3, and the graph is bipartite. Which statements must hold?

A. Each bipartition class has three vertices.
B. The graph is connected.
C. The graph is isomorphic to K3,3.
D. The graph has a triangle.

### Q28. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For grammar S→aA | aB, A→b, B→c, which statements are true?

**Candidates**

**I.** The two S alternatives conflict in an LL(1) predictive table.

**II.** The generated language is inherently ambiguous.

**III.** Replacing the grammar by S→aX, X→b | c gives an LL(1) grammar for the same language.

**IV.** No deterministic parser can recognize the generated language.

A. I and IV  
B. II and III  
C. II and IV  
D. I and III

### Q29. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Under set relational algebra, R(A,B) contains (1,x),(1,y),(2,x), and S(B) contains x,y. Let D=R÷S and P=π_A(R). Which statements hold?

**Candidates**

**I.** D contains exactly the tuple A=1.

**II.** D=P.

**III.** Adding (2,y) to R makes D=P.

**IV.** Removing y from S makes D empty.

A. I and III  
B. III and IV  
C. I and II  
D. I and IV

### Q30. [1 Mark] [NAT]

What integer is printed by this conforming C program?

```c
#include <stdio.h>
struct S { int a[2]; int *p; };
int main(void) {
    struct S s = {{1,2}, 0};
    s.p = s.a;
    struct S t = s;
    t.a[0] = 7;
    *t.p = 9;
    printf("%d\n", s.a[0] + t.a[0]);
    return 0;
}
```

**Answer format:** Integer.

### Q31. [1 Mark] [NAT]

Six labelled positions lie on a circle. How many assignments of exactly two1 bits and four0 bits have no adjacent1 bits, including across the last-to-first boundary? Rotations remain distinct assignments.

**Answer format:** Integer.

### Q32. [1 Mark] [MCQ]

A resolver caches an authoritative negative DNS response for a name with an unexpired negative-cache TTL. The name is then created at the authoritative server. Assuming no forced refresh or invalidation, why may the resolver temporarily continue reporting that the name does not exist?

A. DNS names can never be created after the first query.
B. TCP forbids any change to DNS records.
C. The cached negative result may be reused until its TTL expires.
D. Every negative DNS response has an infinite lifetime.

### Q33. [1 Mark] [MCQ]

Two threads in the same ordinary process have different stack pointers but access the same heap object without synchronization. Which statement is correct?

A. Distinct stacks imply their heap writes cannot race.
B. Shared address-space access permits a data race despite separate stacks.
C. Sharing the heap requires the threads to share the same stack pointer.
D. Each thread automatically receives a private copy of every heap allocation.

### Q34. [1 Mark] [NAT]

A postfix translation emits each operand when visited and emits an operator after both children. How many operator symbols appear in the postfix form of(a+b)*(c−d/e)?

**Answer format:** Integer.

### Q35. [1 Mark] [NAT]

For n=1024, a loop starts with i=n and repeatedly replaces i by floor(√i), stopping when i≤1. How many replacements are made? The square root is exact before taking the floor.

**Answer format:** Integer.

### Q36. [2 Marks] [MSQ]

Two sorted singly linked lists have distinct prefix nodes but share the same suffix nodes. A standard in-place merge is written assuming disjoint lists: it links the smaller current node to the result, advances that list pointer, and repeats, without testing pointer equality. Which statements are correct?

A. Shared nodes can make the merge create a cycle or fail to terminate.
B. If both current pointers are equal, appending that shared suffix once and terminating avoids duplicate processing of that suffix.
C. Equality of node values alone proves that two pointers refer to the same node.
D. Sortedness alone guarantees safety of this disjoint-list merge on shared-suffix inputs.

### Q37. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A recursive function has a local scalar variable x whose address is never returned or retained beyond its activation. Different recursive calls require separate x values until they return. Which allocation strategy directly supports this requirement?

A. A single global x shared by every activation with no saving.  
B. One x slot in each activation record on the runtime stack.  
C. No storage because recursion forbids locals.  
D. One immutable constant substituted for x in every call regardless of assignments.

### Q38. [2 Marks] [MSQ]

A compiler translates `x != 0 && 10/x > 1` using left-to-right short-circuit evaluation over exact integers, with division by zero raising an observable exception. Which transformations preserve behaviour for every x?

A. Test x!=0 first and branch around the division when false.
B. Evaluate 10/x before testing x!=0 for all x.
C. Replace the conjunction by an evaluation that performs the division only on the x!=0 branch.
D. Replace the whole expression by true because 10 is positive.

### Q39. [2 Marks] [MSQ]

For variables a,b,c,d, f=1 exactly when a XOR b=1, independently of c,d. A conventional sum-of-products Karnaugh-map minimization uses cubes that do not cover a zero. Which statements are correct?

A. f has a two-product implementation (NOT a)b+a(NOT b).
B. One product term is sufficient because eight of the sixteen inputs produce1.
C. Each of the two displayed products covers four minterms.
D. A valid product covering both(a,b)=(0,1) and(1,0) can omit both a and b without covering zeros.

### Q40. [2 Marks] [MSQ]

Unary relations R and S are finite. Compare query F={x : R(x) AND NOT S(x)} with query G={x : NOT S(x)} over an unrestricted infinite domain. Which statements are correct?

A. F is contained in the active domain of R.
B. G can return infinitely many values.
C. The occurrence of NOT makes F necessarily unsafe.
D. Positive range restriction by R is relevant to F's domain independence.

### Q41. [2 Marks] [NAT]

A relation R(A,B,C) uses domains of sizes 3,4,5, respectively, and satisfies AB→C and AC→B. Tuples are distinct. What is the maximum possible number of tuples in R?

**Answer format:** Integer.

### Q42. [2 Marks] [NAT]

Initially its completion counter is zero and its timer is stopped. A device completes DMA requests at times 0,3,6,9,12,… microseconds. On the first completion after an interrupt, it starts a 10-microsecond timer and sets a completion counter to 1. Further completions increment the counter. It interrupts when either the counter reaches 8 or the timer expires, then clears the counter and stops the timer. Completions are instantaneous; none coincide with the first two timer expirations. How many interrupts occur at or before time 30 microseconds?

**Answer format:** Exact integer.

### Q43. [2 Marks] [NAT]

An application sends600 bytes over UDP. UDP adds8 bytes, IPv4 adds20 bytes with no options, and a link protocol adds18 bytes per frame. The link permits at most 400 bytes of IP packet per frame. The sender creates IPv4 fragments with the largest legal payloads, including the UDP header in the original IP payload. How many bytes in total are transmitted in the link frames? Ignore preambles and interframe gaps.

**Answer format:** Exact integer.

### Q44. [2 Marks] [MSQ]

Consider S→aSbS | bSaS | ε. Which statements are true?

A. Every generated word has equally many a and b symbols.
B. The word abab has more than one parse tree.
C. Every prefix of every generated word has at least as many a as b symbols.
D. The generated language is regular.

### Q45. [2 Marks] [NAT]

Let an count length-n strings over {0,1,2} in which every run of consecutive2s has even length; runs of0s and1s are unrestricted. The empty string is allowed. What is a4?

**Answer format:** Exact integer.

### Q46. [2 Marks] [NAT]

On a finite nonempty domain, R is symmetric and irreflexive. Every element is related to exactly two distinct elements. Also, for every x,y,z, R(x,y) AND R(y,z) implies NOT R(x,z). What is the smallest possible domain size?

**Answer format:** Integer.

### Q47. [2 Marks] [MCQ]

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

### Q48. [2 Marks] [NAT]

A 10,000-bit payload is split into k equal packets, each with a 100-bit header, and sent through two equal-rate links via a store-and-forward router. Both links have rate R, propagation is negligible, links can work concurrently, and packets are transmitted back-to-back. k is a positive integer dividing 10,000. What k minimizes completion time of the final packet?

**Answer format:** Integer.

### Q49. [2 Marks] [MSQ]

A bounded buffer has capacity2 and is initially empty. A semaphore empty starts at2, full at0, and mutex at1. A consumer mistakenly executes wait(mutex), then wait(full), and retains mutex while blocked. A producer executes wait(empty), then wait(mutex) before inserting. Which statements are correct if the consumer runs first?

A. The consumer can block while holding mutex.
B. The producer can then block on mutex while unable to insert the item that would release the consumer.
C. Increasing the buffer capacity alone fixes this ordering bug for an initially empty buffer.
D. Having the consumer wait(full) before wait(mutex) avoids this particular hold-and-wait cycle.

### Q50. [2 Marks] [MSQ]

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

### Q51. [2 Marks] [NAT]

Two processes arrive at time 0. A has CPU burst 2, then I/O lasting 3, then CPU burst 2. B has one CPU burst of 4. The CPU uses nonpreemptive FCFS, choosing A first; I/O overlaps CPU work and has no contention. Switching costs are zero. What is their average total ready-queue waiting time?

**Answer format:** Exact finite decimal time units.

### Q52. [2 Marks] [NAT]

A protocol numbers bytes modulo 2ⁿ and sends continuously at 1 MiB/s (1 MiB=2²⁰ bytes). It requires strictly more than 12 seconds before any sequence number is reused. Its sender window must hold at least one second of traffic and must be strictly smaller than half the sequence space. What is the smallest integer n satisfying both requirements?

**Answer format:** Integer.

### Q53. [2 Marks] [NAT]

Let A be the 3×3 upper-triangular matrix with rows (1,1,0),(0,1,1),(0,0,1). Find the entry in row 1, column 3 of A⁵+A⁻².

**Answer format:** Integer.

### Q54. [2 Marks] [NAT]

A data-only L1 cache holds two blocks; a unified L2 holds three. Both are fully associative with LRU replacement and initially empty. L2 is inclusive: evicting a block invalidates any L1 copy. A data L1 miss accesses L2 and updates its LRU order; an L1 hit does not access L2. Instruction accesses bypass L1 and access/update only L2. Every L2 miss fetches one block from memory. Accesses are data A, data B, data A, instruction C, instruction D, data A. All block labels are distinct. How many memory block fetches occur?

**Answer format:** Integer memory block fetches.

### Q55. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Use set semantics. R(A,B) contains (1,x),(2,x), and S(B,C) contains (x,p),(x,q). The natural join J=R⋈S is formed. Which statements are correct?

**Candidates**

**I.** J has four tuples.

**II.** A→C holds in J.

**III.** Projecting J onto (A,B) recovers R exactly.

**IV.** B is a candidate key of J.

A. I and II  
B. I and IV  
C. II and III  
D. I and III

### Q56. [2 Marks] [MSQ]

A rooted ordered full binary tree has exactly four leaves. Every internal node has a left and a right child, and the root has depth 0. Which lists can be the depths of its leaves in left-to-right order?

A. (1,2,3,3)
B. (2,1,3,3)
C. (2,2,2,2)
D. (3,3,1,2)

### Q57. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Let f(0)=0 and f(x)=x² sin(1/x) for x≠0. Which statements are correct?

A. f is continuous at0.  
B. f is differentiable at0 with derivative0.  
C. f' is continuous at0.  
D. The limit of f(x)/x as x approaches0 is0.

### Q58. [2 Marks] [MCQ]

Activities have half-open intervals A=[0,4), B=[1,2), C=[2,3), D=[3,5), E=[4,6). Which statement correctly compares greedy rules for maximizing the number of nonoverlapping activities?

A. Earliest starting time always yields an optimum and selects three here.
B. Earliest finishing time can select B,C,D, while choosing A first limits the total to two.
C. Shortest duration is the only rule that can produce three here.
D. Every maximal compatible set must have the same cardinality.

### Q59. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

In a tabular Boolean-minimization procedure, two product cubes may be combined only if their don't-care positions are identical and they differ in exactly one remaining bit. Here '-' denotes a don't-care position. Which pairs can be combined under that rule?

**Candidates**

**I.** 0-01 and0-11.

**II.** 00-1 and0-01.

**III.** -100 and-101.

**IV.** 0101 and1010.

A. III and IV  
B. I and III  
C. I and II  
D. I and IV

### Q60. [2 Marks] [MCQ]

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

### Q61. [2 Marks] [NAT]

A 0/1 knapsack has capacity6. Items A,B,C have (weight,value) pairs (3,5),(4,7),(2,4). Each item can be selected at most once. A faulty implementation updates its one-dimensional DP array in increasing capacity order for each item, allowing an item to be reused. By how much can its final dp[6] exceed the true optimum, starting with all entries zero and processing items A,B,C in that order?

**Answer format:** Exact integer.

### Q62. [2 Marks] [NAT]

A processor uses 16-bit instructions and has 16 registers. Each register operand occupies four bits. In a two-register instruction, the first eight bits form the opcode. In a one-register instruction, the first twelve bits form the opcode. A zero-register instruction uses all sixteen bits as its opcode. Decoding must be unambiguous: no complete opcode may be a prefix of another complete opcode. Exactly 200 two-register opcodes and 800 one-register opcodes are allocated. What is the maximum number of distinct zero-register instructions that can also be allocated?

**Answer format:** Numeric value; integer.

### Q63. [2 Marks] [MCQ]

For positive integer n, an algorithm splits into subproblems of sizes floor(n/3) and n−floor(n/3), then does Θ(n) additional work, with constant-time base cases for n≤2. What is its asymptotic running time?

A. Θ(log n)
B. Θ(n)
C. Θ(n log n)
D. Θ(n²)

### Q64. [2 Marks] [MSQ]

Let L1={a^n b^n c^m:n,m≥0} and L2={a^m b^n c^n:n,m≥0}. Which statements hold?

A. L1 union L2 is context-free.
B. L1 intersect L2 is regular.
C. L1 intersect L2 equals {a^n b^n c^n:n≥0}.
D. L1 union L2 is regular.

### Q65. [2 Marks] [NAT]

For Boolean inputs a,b,c, a circuit computes p=NAND(a,b), q=NAND(a,c), r=NAND(b,c), u=NAND(p,q), v=NAND(u,u), and F=NAND(v,r). Consider two otherwise identical faulty copies: in one, p is permanently0; in the other, p is permanently1. All other gates work normally. For how many of the eight input assignments do the two faulty copies produce different F outputs?

**Answer format:** Integer.

---

## ANSWER KEY — MOCK TEST 091

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MSQ | 1 | B, C, D |
| 2 | NAT | 1 | 6 |
| 3 | NAT | 1 | 80 |
| 4 | NAT | 1 | 3 |
| 5 | MCQ | 1 | C |
| 6 | MSQ | 2 | A, B, D |
| 7 | MCQ | 2 | D |
| 8 | NAT | 2 | 20 |
| 9 | MCQ | 2 | C |
| 10 | NAT | 2 | 6 |
| 11 | NAT | 1 | 5 |
| 12 | NAT | 1 | 0.3466 (range 0.34655–0.34665) |
| 13 | NAT | 1 | -4 |
| 14 | MSQ | 1 | A, B, D |
| 15 | NAT | 1 | 7.6 (exact) |
| 16 | MCQ | 1 | B |
| 17 | MCQ | 1 | A |
| 18 | MCQ | 1 | D |
| 19 | MSQ | 1 | B, C, D |
| 20 | NAT | 1 | 5 |
| 21 | NAT | 1 | 3 |
| 22 | MSQ | 1 | A, C |
| 23 | MCQ | 1 | A |
| 24 | MCQ | 1 | D |
| 25 | MCQ | 1 | B |
| 26 | NAT | 1 | 2 |
| 27 | MSQ | 1 | A, B, C |
| 28 | MCQ | 1 | D |
| 29 | MCQ | 1 | A |
| 30 | NAT | 1 | 16 |
| 31 | NAT | 1 | 9 |
| 32 | MCQ | 1 | C |
| 33 | MCQ | 1 | B |
| 34 | NAT | 1 | 4 |
| 35 | NAT | 1 | 4 |
| 36 | MSQ | 2 | A, B |
| 37 | MSQ | 2 | A, C, D |
| 38 | MSQ | 2 | A, C |
| 39 | MSQ | 2 | A, C |
| 40 | MSQ | 2 | A, B, D |
| 41 | NAT | 2 | 12 |
| 42 | NAT | 2 | 2 |
| 43 | NAT | 2 | 684 |
| 44 | MSQ | 2 | A, B |
| 45 | NAT | 2 | 29 |
| 46 | NAT | 2 | 4 (exact) |
| 47 | MCQ | 2 | D |
| 48 | NAT | 2 | 10 |
| 49 | MSQ | 2 | A, B, D |
| 50 | MSQ | 2 | A, B, D |
| 51 | NAT | 2 | 1.5 |
| 52 | NAT | 2 | 24 |
| 53 | NAT | 2 | 13 |
| 54 | NAT | 2 | 5 |
| 55 | MCQ | 2 | D |
| 56 | MSQ | 2 | A, C |
| 57 | MCQ | 2 | C |
| 58 | MCQ | 2 | B |
| 59 | MCQ | 2 | B |
| 60 | MCQ | 2 | B |
| 61 | NAT | 2 | 1 |
| 62 | NAT | 2 | 1536 (exact) |
| 63 | MCQ | 2 | C |
| 64 | MSQ | 2 | A, C |
| 65 | NAT | 2 | 5 |
