# GATE CS 2027 — Full-Length Mock Test 057

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

Choose the grammatically correct completion: “Had the survey included night-shift workers, its conclusion ____ different.”

A. will have been
B. would have been
C. would be being
D. had been being

### Q2. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

In a company, 60% of employees work remotely. Of the remote employees, 25% work part-time. Of the remaining employees, 10% work part-time. What percentage of all employees work part-time?

**Required precision:** Integer percentage, without the percent sign.

A. 38  
B. 10  
C. 20  
D. 19

### Q3. [1 Mark] [MCQ]

Exactly one of statements P and Q is true. P says “The key is in drawer 1.” Q says “The key is not in drawer 2.” The key is in exactly one of drawers 1,2,3. Where is it?

A. Drawer 1
B. Drawer 2
C. Drawer 3
D. The premises permit all three drawers.

### Q4. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A point is rotated180 degrees about(1,0), then180 degrees about(0,2). Starting at(3,4), what is the squared distance between its initial and final positions?

**Required precision:** Integer.

A. 20  
B. 40  
C. 10  
D. 21

### Q5. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A report states: “The survey's volunteers reported shorter commutes than the city average. Because participation was voluntary, the survey alone cannot establish that the same pattern holds among all residents.” Which conclusion best respects this qualification?

A. Every resident has a shorter-than-average commute.  
B. Voluntary participation guarantees a representative sample.  
C. The volunteers' result is an observation whose generalization requires further evidence.  
D. Every volunteer's response must be false.

### Q6. [2 Marks] [NAT]

How many distinct arrangements of the multiset of letters A,A,B,B,C contain no adjacent A's?

**Answer format:** Integer.

### Q7. [2 Marks] [NAT]

Last year, centre A passed 90 of 100 candidates and centre B passed 1 of 10. This year, A passed 19 of 20 and B passed 16 of 80. By how many percentage points did the combined pass percentage fall, despite both centres improving individually? Round to two decimal places.

**Answer format:** Number to 2 decimal places.

### Q8. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A square sheet occupies0≤x≤4,0≤y≤4. Fold its left half onto its right half along x=2. Cut out, through both layers, the triangle with vertices(2,0),(3,0),(2,1). After unfolding, what is the perimeter of the remaining sheet? The cut boundaries are included in the perimeter.

**Required precision:** Decimal rounded to four places.

A. 33.6568  
B. 8.4142  
C. 17.8284  
D. 16.8284

### Q9. [2 Marks] [MCQ]

Four events Q,R,S,P occurred at distinct times. Four log entries assert Q before R, R before S, S before P, and P before Q, respectively. Exactly one of these four entries is wrong. An independent reliable record establishes R before P. Which ordering must be true?

A. Q before R.
B. Q before P.
C. S before P.
D. P before R.

### Q10. [2 Marks] [NAT]

A fair six-sided die is rolled twice independently. Given that the larger of the two results is4, what is the probability that their sum is even? Round to four decimal places.

**Answer format:** Decimal rounded to four places.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [NAT]

Let A={1,2} and B={1,2,3,4,5}. Consider the set of all X satisfying A⊆X⊆B, ordered by inclusion. How many ordered pairs (X,Y) satisfy X∩Y=A and X∪Y=B?

**Answer format:** Integer.

### Q12. [1 Mark] [MCQ]

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

### Q13. [1 Mark] [MCQ]

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

### Q14. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A recursive DNS resolver caches a record with TTL 120 seconds at time 0. A cache hit does not reset its expiry. A client requests it at times 50,119,121 and 200 seconds. Refreshes are instantaneous and reset the cached TTL to 120. How many upstream fetches occur because of these four requests, excluding the initial fetch at time 0?

**Required precision:** Integer.

A. 2  
B. 0  
C. 1  
D. 3

### Q15. [1 Mark] [MCQ]

For Boolean variables x,y,z, let F=(x AND y) OR ((NOT x) AND z). When y=z, which expression always equals F?

A. x
B. NOT y
C. x XOR y
D. y

### Q16. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A lexer returns the longest available operator token from {>,>=,>> ,>>=}, ignoring the displayed spacing in this set. With input >>>= and no whitespace, how many operator tokens does it return?

**Required precision:** Integer.

A. 4  
B. 2  
C. 1  
D. 3

### Q17. [1 Mark] [MSQ]

A connected, undirected graph has a unique minimum spanning tree T. Every edge weight is replaced by w'(e)=3w(e)+7. Which statements necessarily hold?

A. T remains the unique minimum spanning tree.
B. Every shortest path remains a shortest path.
C. The relative weights of any two spanning trees remain ordered in the same way.
D. The weight of T increases by exactly 7.

### Q18. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Independent Poisson variables X,Y have means 2 and 3. Find E[X | X+Y=3].

**Required precision:** Exact finite decimal.

A. 2.4  
B. 0.6  
C. 2.2  
D. 1.2

### Q19. [1 Mark] [NAT]

A process has four virtual pages mapped to physical frames [7,2,7,9], respectively. Each physical frame occupies 4 KiB. How many KiB of distinct physical-frame storage do these mappings reference?

**Answer format:** Integer.

### Q20. [1 Mark] [MCQ]

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

### Q21. [1 Mark] [MCQ]

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

### Q22. [1 Mark] [MCQ]

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

### Q23. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A B+ tree root has separators [30,50] and leaves [10,20],[30,40],[50,60], in order. Leaves may contain two or three keys, except that a leaf root may contain fewer. Delete 40. Neither sibling can lend without violating its minimum; merge with the left sibling. Separators are the smallest keys of their right subtrees. What is the sole separator in the resulting root?

**Required precision:** Integer.

A. 100  
B. 25  
C. 50  
D. 51

### Q24. [1 Mark] [NAT]

An instruction's unsigned immediate field has six bits. How many different nonnegative integers can it encode directly?

**Answer format:** Integer.

### Q25. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A condition variable is associated with a mutex and predicate ready. Waiting atomically releases the mutex and later reacquires it before returning. Spurious wakeups are permitted. Which pattern correctly waits for ready?

A. Lock; if not ready, wait once; use protected data; unlock.  
B. Lock; while not ready, wait; use protected data; unlock.  
C. Test ready without the mutex, then lock only if true.  
D. Lock; repeatedly test ready without releasing the mutex until it becomes true.

### Q26. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

A binary min-heap stored from index 1 is [2,5,3,9,7,8]. Insert 1 by placing it at the next free index and repeatedly exchanging it with its parent while smaller. How many exchanges occur?

**Required precision:** Integer.

A. 4  
B. 1  
C. 3  
D. 2

### Q27. [1 Mark] [NAT]

Evaluate ∫₀¹ x/(1+x²) dx, rounded to four decimal places.

**Answer format:** Number to 4 decimal places.

### Q28. [1 Mark] [MCQ]

A segmented address has segment number 2 and offset 120. Segment 2 has base 4000 and limit 100, where valid offsets are 0 through limit−1. What is the correct outcome of translation?

A. Physical address 4120.
B. Physical address 4100.
C. An address-bound violation.
D. Physical address 120.

### Q29. [1 Mark] [MCQ]

Two processes use the same virtual page number but map it to different physical frames. A processor's TLB has no address-space tags. Which action can prevent stale translations from the first process being used by the second on a context switch?

A. Retain all translations merely because the virtual page numbers match.
B. Flush the relevant TLB translations when changing address spaces.
C. Change every physical memory byte to zero.
D. Assume every TLB hit automatically consults the new page table again.

### Q30. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A language L is accepted by a DFA. Which operations always produce another regular language?

A. Reverse every word of L.  
B. Take the complement of L over the same alphabet.  
C. Intersect L with an arbitrary context-free language.  
D. Concatenate L with itself.

### Q31. [1 Mark] [NAT]

What integer is printed? The static variable is initialized once.

```c
#include <stdio.h>
int f(int n) {
    static int k = 0;
    int a = ++k;
    if (n == 0) return a;
    return a + f(n-1);
}
int main(void) {
    int x = f(2);
    int y = f(1);
    printf("%d\n", x+y);
    return 0;
}
```

**Answer format:** Integer.

### Q32. [1 Mark] [MCQ]

Select the numerical value that correctly answers the following problem.

Five real observations have mean10 and population variance8, where the variance is the sum of squared deviations divided by the number of observations. One observation equal to14 is removed. What is the population variance of the remaining four observations?

**Required precision:** Exact number.

A. 10  
B. 3  
C. 5  
D. 6

### Q33. [1 Mark] [MSQ]

M is a finite monoid with identity e. Every element a has a right inverse b satisfying ab=e. Which statements necessarily hold?

A. Every element has a two-sided inverse.
B. M is a group.
C. M must be commutative.
D. The right inverse of an element can be chosen arbitrarily from M.

### Q34. [1 Mark] [NAT]

A B+ tree internal node contains six separator keys. Under the usual k-keys/k+1-children rule, how many child pointers does it contain?

**Answer format:** Integer.

### Q35. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In C, `int a[3]={5,6,7}; int *p=a+3;` is executed. Which subsequent operation is valid by the one-past-the-end pointer rule?

A. Evaluate *p.  
B. Evaluate *(p-1).  
C. Form p+1 and dereference it.  
D. Write p[0]=8.

### Q36. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Grammar S→aSa | bSb | a | b is over{a,b}. Which statements are correct?

**Candidates**

**I.** Every generated string is an odd-length palindrome.

**II.** The grammar generates ε.

**III.** Reversing a generated string always gives a generated string.

**IV.** The language is closed under concatenation.

A. III and IV  
B. I and II  
C. I and IV  
D. I and III

### Q37. [2 Marks] [MCQ]

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

### Q38. [2 Marks] [MCQ]

A file contains 100 fixed-size records in ten disk blocks, ten records per block. An in-memory index gives the exact block containing any requested record. Ten requested record numbers are independently and uniformly selected with replacement from the 100 records. A data block is read from disk only on its first request and then remains cached. Which expression is the expected number of disk reads?

A. 10
B. 10(1−(9/10)¹⁰)
C. 100(1−(99/100)¹⁰)
D. (9/10)¹⁰

### Q39. [2 Marks] [MCQ]

A file contains bytes abcdef. fd1 opens it read-only; fd2=dup(fd1); fd3 opens the same pathname independently. All operations succeed. Read two bytes from fd1, one from fd2, and one from fd3. Then seek fd2 to absolute offset 1 and read two bytes from fd1. Which bytes does this final read return?

A. de  
B. ab  
C. bc  
D. cd

### Q40. [2 Marks] [MCQ]

Relations Employee(e,d), Required(d,p) and Done(e,p) contain the following tuples (set semantics):
```text
Employee = {(u,A), (v,A), (w,B), (z,C)}
Required = {(A,p), (A,q), (B,q)}
Done     = {(u,p), (u,q), (u,r), (v,p), (v,q), (w,q), (z,r)}
```
Let E be the set of employee identifiers e for which there exists an Employee tuple (e,d) satisfying
`for every project identifier t: Done(e,t) if and only if Required(d,t)`.
Quantification is over all project identifiers, and no tuples other than those listed exist. Which set is E?

A. {u,v,w}  
B. {v,w}  
C. {v,w,z}  
D. {u,v,w,z}

### Q41. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Routers have converged exact shortest distances d(v) to destination t. Each router v≠t selects a next hop u satisfying d(v)=w(v,u)+d(u). All relevant distances are finite. Which statements are correct?

A. If all link costs are strictly positive, the selected next-hop graph cannot contain a directed cycle.  
B. If zero-cost links are allowed, independent tie choices can create a forwarding cycle despite correct distances.  
C. Correct distances alone prevent forwarding cycles for every set of nonnegative link costs.  
D. With positive costs, distance strictly decreases at every selected hop.

### Q42. [2 Marks] [NAT]

The following pseudocode uses a reference to one shared integer x. Arithmetic is exact.

```text
f(n, reference x):
    if n = 0: return x
    x = x + 1
    a = f(n - 1, x)
    x = x + a
    return x
```

Initially x=1. After evaluating f(3,x), what is the final value of x?

**Answer format:** Exact integer.

### Q43. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

An array of length 12 is cyclically rotated left by 8 positions using a cycle-following algorithm. Each disjoint permutation cycle uses one temporary variable to save its first value and performs one write to each array location in that cycle. How many separate cycles does the algorithm process?

**Required precision:** Integer.

A. 8  
B. 2  
C. 5  
D. 4

### Q44. [2 Marks] [NAT]

A lock manager uses shared and exclusive locks. Initially T1 holds S(A), T2 holds S(A) and S(B), and T3 holds S(B). T1 then requests X(B); T3 requests X(A); T2 requests an upgrade to X(A). All three requests wait, all existing locks are retained, and a request waits only for incompatible locks held by other transactions. How many directed edges are in the wait-for graph, counting each ordered pair once?

**Answer format:** Integer.

### Q45. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A multithreaded process has threads T1,T2. T2 holds a user-space mutex when T1 duplicates the process using a model in which the child contains only the calling thread but inherits a copy of the mutex's locked state. In the child, no automatic repair occurs and no surviving thread can release T2's lock. Which statements are correct?

**Candidates**

**I.** The child's copied mutex may remain permanently locked.

**II.** The child's copy of T2 necessarily continues and releases it.

**III.** Waiting on that mutex in the child can block indefinitely under this model.

**IV.** The parent's later unlock necessarily changes the child's private copied mutex state.

A. II and IV  
B. I and III  
C. III and IV  
D. I and II

### Q46. [2 Marks] [NAT]

Insertion sort on an array of distinct values shifts an earlier element right whenever it is greater than the current key. Count only these shifts, not key placements or failed comparisons. An initial array is formed by concatenating ascending blocks [4,5,6], [1,2,3], and [7,8]. How many shifts does insertion sort perform?

**Answer format:** Exact integer.

### Q47. [2 Marks] [MSQ]

A CRC uses generator G(x)=x³+x+1 over GF(2). An error is undetected exactly when its nonzero error polynomial is divisible by G. Which statements are correct?

A. Error x⁷+1 is undetected.  
B. Error x⁶+1 is undetected.  
C. Every single-bit error is detected.  
D. Every nonzero burst error of length at most three bits is detected.

### Q48. [2 Marks] [MSQ]

A PDA recognizes L and a DFA recognizes R over the same alphabet. To recognize L∩R, one uses a product control state with the PDA's original stack. Which statements are correct?

A. Consuming one input symbol updates both components according to that symbol.
B. Every epsilon transition of the PDA must consume a symbol in the DFA.
C. One stack suffices for this construction.
D. A second unbounded stack is necessary to remember the DFA's state.

### Q49. [2 Marks] [MSQ]

A weak entity Room is identified by the pair(BuildingID,RoomNumber). RoomNumber is unique only within a building. Which statements are correct?

A. Rooms in different buildings may share a RoomNumber.
B. RoomNumber alone necessarily identifies a room globally.
C. The owner's identifier contributes to the weak entity's identification.
D. Moving a room record to another building can cause an identifier collision if that building already has the same RoomNumber.

### Q50. [2 Marks] [NAT]

A syntax-directed definition assigns each bit string X two attributes: length X.len and fraction X.val. For a single bit b, len=1 and val=b/2. For concatenation X=YZ, the rules are X.len=Y.len+Z.len and X.val=Y.val+Z.val/2^(Y.len). A parse tree concatenates Y=10 and Z=11. What is X.val?

**Answer format:** Exact decimal.

### Q51. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A Karnaugh-map group fixes variable a=1 and c=0 while leaving b and d free. Which statements are correct?

A. The group represents product a(NOT c).  
B. It covers four minterms.  
C. Its product must include b and d because they vary.  
D. It can legally include specified zero cells in an exact SOP implementation without don't-cares.

### Q52. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

An8-bit ALU adds unsigned inputs200 and100 and retains only eight result bits. Let C be its carry-out bit. Interpret the retained result as a signed two's-complement integer R. What is R+256C?

**Required precision:** Exact integer.

A. 300  
B. 600  
C. 150  
D. 301

### Q53. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A singly linked structure has nodes0,1,2,3,4,5 and next pointers 0→1→2→3→4→5→2. Floyd's cycle-detection algorithm starts slow=fast=node0. In each iteration, slow advances once and fast twice, then equality is tested. What is the node label at the first equality after an iteration?

**Required precision:** Exact integer.

A. 4  
B. 8  
C. 2  
D. 5

### Q54. [2 Marks] [NAT]

A simple graph contains a five-cycle a–b–c–d–e–a and two additional vertices p,q. Each of p,q is adjacent to all five cycle vertices, but p and q are not adjacent to each other. There are no other edges. What is the graph's chromatic number?

**Answer format:** Integer.

### Q55. [2 Marks] [NAT]

A hash table has11 slots and uses double hashing h1(k)=k mod11 and h2(k)=1+(k mod10). To insert a key, probe(h1+i·h2) mod11 for i=0,1,... . Initially slots0,1,3,5 are occupied and all others empty. How many probes are made to insert key22, counting the successful probe?

**Answer format:** Integer.

### Q56. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

How many distinct permutations of the multiset {A,A,B,B,C,C} have neither the two A's adjacent nor the two B's adjacent? Adjacency of the C's is allowed.

**Required precision:** Exact integer.

A. 42  
B. 84  
C. 21  
D. 43

### Q57. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A binary floating-point format has four significant bits including the leading 1, unbounded exponents, and round-to-nearest, ties-to-even after each operation. Let a=16, b=1, c=−16, all exactly representable. Which statements are correct?

A. The computed value of (a+b)+c is 0.  
B. The computed value of a+(b+c) is 1.  
C. Both parenthesizations must agree because no overflow occurs.  
D. The exact real-arithmetic value of a+b+c is 1.

### Q58. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A strip of length6 is tiled with unit tiles and length-two tiles. Two length-two tiles may not be adjacent. Tiles of the same length are indistinguishable. How many different left-to-right tilings exist?

**Required precision:** Integer.

A. 18  
B. 9  
C. 5  
D. 10

### Q59. [2 Marks] [NAT]

A microsequencer stores a subroutine return address in one link register, with no stack or other saved copy. Main calls micro-subroutine U, which calls V before returning. V returns via the link register, then U also returns through it. How many distinct return addresses must be simultaneously preserved at the moment V is entered for both returns to work correctly?

**Answer format:** Integer.

### Q60. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A16-to-1 multiplexer is built entirely from2-to-1 multiplexers arranged as a binary selection tree, without sharing data inputs between tree branches. How many2-to-1 multiplexers are required?

**Required precision:** Integer.

A. 15  
B. 30  
C. 8  
D. 16

### Q61. [2 Marks] [NAT]

Two Ethernet stations independently choose backoff counters uniformly from{0,1,2,3} after the same collision. Under the simplified model that only equal counters cause another collision, what is the probability that one station selects a counter exactly one larger than the other?

**Answer format:** Exact decimal.

### Q62. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A procedure make() creates a fresh variable x=0 and returns a closure inc that increments that captured variable by1 and returns its new value. Set f=make(), g=f, and h=make(). Each closure retains its environment after make returns. Calls f(),g(),h(),f() are made in that order. What is the sum of the returned values?

**Required precision:** Integer.

A. 7  
B. 14  
C. 4  
D. 8

### Q63. [2 Marks] [MCQ]

Select the numerical value that correctly answers the following problem.

A quadratic f(x)=ax²+bx+1 satisfies f(1)=0 and ∫₀¹f(x)dx=0. Find its minimum value on [0,1], rounded to four decimal places.

**Required precision:** Number to 4 decimal places.

A. -0.6666  
B. -0.1667  
C. -0.3333  
D. 0.6667

### Q64. [2 Marks] [MCQ]

A dynamic array doubles its capacity when full. Initially it is empty with capacity one. Appending a value costs one unit, and a resizing append additionally copies every existing value at one unit per copy. For n=2^k appends, k≥1, what is the exact total cost?

A. n+k
B. 2n−1
C. n log₂n
D. 3n

### Q65. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For a language L, define its prefix set Pref(L)={u: there exists v such that uv belongs to L}. Which statements hold?

**Candidates**

**I.** If L is regular, Pref(L) is regular.

**II.** For a DFA of L, marking all states from which an accepting state is reachable as accepting recognizes Pref(L).

**III.** Pref(L) always equals L.

**IV.** If L is empty, Pref(L) contains epsilon.

A. I and II  
B. III and IV  
C. I and III  
D. I and IV

## ANSWER KEY — MOCK TEST 057

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | B |
| 2 | MCQ | 1 | D |
| 3 | MCQ | 1 | C |
| 4 | MCQ | 1 | A |
| 5 | MSQ | 1 | A, B, D |
| 6 | NAT | 2 | 18 |
| 7 | NAT | 2 | 47.73 (range 47.725–47.735) |
| 8 | MCQ | 2 | D |
| 9 | MCQ | 2 | C |
| 10 | NAT | 2 | 0.4286 (accepted range 0.42855–0.42865) |
| 11 | NAT | 1 | 8 |
| 12 | MCQ | 1 | D |
| 13 | MCQ | 1 | A |
| 14 | MCQ | 1 | C |
| 15 | MCQ | 1 | D |
| 16 | MCQ | 1 | B |
| 17 | MSQ | 1 | A, C |
| 18 | MCQ | 1 | D |
| 19 | NAT | 1 | 12 |
| 20 | MCQ | 1 | A |
| 21 | MCQ | 1 | D |
| 22 | MCQ | 1 | B |
| 23 | MCQ | 1 | C |
| 24 | NAT | 1 | 64 |
| 25 | MSQ | 1 | A, C, D |
| 26 | MCQ | 1 | D |
| 27 | NAT | 1 | 0.3466 (range 0.34655–0.34665) |
| 28 | MCQ | 1 | C |
| 29 | MCQ | 1 | B |
| 30 | MCQ | 1 | C |
| 31 | NAT | 1 | 15 |
| 32 | MCQ | 1 | C |
| 33 | MSQ | 1 | A, B |
| 34 | NAT | 1 | 7 |
| 35 | MSQ | 1 | A, C, D |
| 36 | MCQ | 2 | D |
| 37 | MCQ | 2 | B |
| 38 | MCQ | 2 | B |
| 39 | MCQ | 2 | C |
| 40 | MCQ | 2 | B |
| 41 | MCQ | 2 | C |
| 42 | NAT | 2 | 32 |
| 43 | MCQ | 2 | D |
| 44 | NAT | 2 | 5 |
| 45 | MCQ | 2 | B |
| 46 | NAT | 2 | 9 |
| 47 | MSQ | 2 | A, C, D |
| 48 | MSQ | 2 | A, C |
| 49 | MSQ | 2 | A, C, D |
| 50 | NAT | 2 | 0.6875 |
| 51 | MSQ | 2 | C, D |
| 52 | MCQ | 2 | A |
| 53 | MCQ | 2 | A |
| 54 | NAT | 2 | 4 |
| 55 | NAT | 2 | 3 |
| 56 | MCQ | 2 | A |
| 57 | MCQ | 2 | C |
| 58 | MCQ | 2 | B |
| 59 | NAT | 2 | 2 |
| 60 | MCQ | 2 | A |
| 61 | NAT | 2 | 0.375 |
| 62 | MCQ | 2 | A |
| 63 | MCQ | 2 | C |
| 64 | MCQ | 2 | B |
| 65 | MCQ | 2 | A |
