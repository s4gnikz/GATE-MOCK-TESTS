# GATE CS 2027 — Full-Length Mock Test 041

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

Choose the grammatically correct completion in formal English: “Neither the two applicants nor their supervisor ___ available when the committee ___ its decision yesterday.”

A. were; announce
B. was; announced
C. were; announcing
D. was; announce

### Q2. [1 Mark] [NAT]

An article costs a seller ₹80 and is marked at ₹100. It is sold at a 10% discount on the marked price. What percentage of the actual selling price is profit?

**Answer format:** Percentage rounded to two decimal places.

### Q3. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A notice reads: “Only registered participants may enter the laboratory. Registration does not reserve a laboratory seat.” Which statement follows from the notice?

A. Every registered participant is guaranteed a seat.  
B. A person allowed to enter must be registered.  
C. Every person denied a seat is unregistered.  
D. Registration is unnecessary for laboratory entry.

### Q4. [1 Mark] [MCQ]

A triangular tile has labelled vertices P=(1,1), Q=(3,1), R=(1,2) in a Cartesian plane. First reflect the tile in the x-axis. Then rotate the result clockwise by 90 degrees about the origin. Which ordered triple gives the final positions of P, Q and R?

A. ((-1,-1),(-1,-3),(-2,-1))  
B. ((1,1),(1,3),(2,1))  
C. ((1,-1),(1,-3),(2,-1))  
D. ((-1,1),(-1,3),(-2,1))

### Q5. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A notice says: “Applications received after Friday will be considered only if places remain.” Which conclusion is justified?

A. Every late application will be accepted if a place remains.  
B. Applications submitted before Friday are considered only if places remain.  
C. Every application received by Friday will be accepted.  
D. No late application can be considered when all places have been filled.

### Q6. [2 Marks] [MCQ]

Seven distinct people A, B, C, D, E, F and G sit around a circular table. A and B must sit next to each other. Neither C and D nor E and F may sit next to each other. Rotations of an arrangement are identical; reflections are different. How many arrangements are possible?

A. 96  
B. 120  
C. 144  
D. 240

### Q7. [2 Marks] [MSQ]

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

### Q8. [2 Marks] [NAT]

A square sheet occupies[0,8]×[0,8]. Fold the right half left along x=4, then the top half down along y=4. Through all layers cut out the rectangle[1,3]×[0,1] of the folded sheet. Unfold the sheet. What is the total area removed from the original sheet?

**Answer format:** Integer square units.

### Q9. [2 Marks] [MCQ]

Four events occurred once each: calibration C, inspection I, trial T, and release R. Calibration preceded trial; inspection immediately followed calibration; release occurred after inspection but before trial. Which order is consistent?

A. C,I,R,T
B. C,R,I,T
C. I,C,R,T
D. C,I,T,R

### Q10. [2 Marks] [MCQ]

A school introduced optional tutoring. Participants subsequently scored higher than nonparticipants. The report concludes that tutoring caused the entire observed score difference. Which additional finding most directly weakens this conclusion?

A. Participants already had higher scores before tutoring began.
B. The tutoring sessions occurred in classrooms.
C. Both groups took the same final examination.
D. The report stated each group's size.

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

Relation R(A,B,C) has exactly the functional dependencies implied by A→B and B→A. Which is its highest normal form among the choices below? Assume atomic attribute values.

A. 1NF but not 2NF  
B. 2NF but not 3NF  
C. 3NF but not BCNF  
D. BCNF

### Q12. [1 Mark] [NAT]

An IPv4 fragment has a 20-byte header, total length 420 bytes, and fragment-offset field 100. At what payload byte offset, measured from the start of the original datagram's payload, does this fragment end? Give the exclusive end offset.

**Answer format:** Integer.

### Q13. [1 Mark] [NAT]

Two IPv4 ranges are10.0.0.0/25 and10.0.0.64/26. How many distinct addresses belong to their union?

**Answer format:** Integer.

### Q14. [1 Mark] [NAT]

An L1 miss is served by L2 with conditional hit probability0.8. An L2 miss causes a main-memory access. If L1's miss probability is0.1, what fraction of all accesses reach main memory?

**Answer format:** Exact decimal.

### Q15. [1 Mark] [MCQ]

A quicksort variant partitions a subarray into keys less than, equal to, and greater than its pivot, in time Θ(m) for a subarray of length m. It recurses only on the less-than and greater-than parts. What is its running time on n equal keys?

A. Θ(1)
B. Θ(log n)
C. Θ(n)
D. Θ(n²)

### Q16. [1 Mark] [NAT]

A three-variable Boolean function has ON minterms 1,3,5, with variable order abc and a most significant. All other minterms are OFF except minterm 7, which may first be treated as a don't-care. What is the increase in minimum SOP literal count when minterm 7 is instead required to be OFF? Count repeated literal occurrences separately.

**Answer format:** Integer.

### Q17. [1 Mark] [NAT]

A scheduler uses shortest remaining processing time, with zero switching cost. Job A arrives at 0 with burst7, B at 2 with burst2, and C at 3 with burst1. A tie retains the currently running job. At what time does A complete?

**Answer format:** Exact integer.

### Q18. [1 Mark] [NAT]

A port-address translator has one public IPv4 address and may allocate any source port from 40000 through 40099 inclusive. It must assign distinct translated source ports to simultaneous TCP connections that all contact the same external address and port. What is the maximum number of such connections it can distinguish using this pool?

**Answer format:** Integer.

### Q19. [1 Mark] [MSQ]

A TLB tags each translation by an address-space identifier (ASID) and a virtual page number. Processes P and Q have different ASIDs but may use the same virtual addresses. Which statements are correct?

A. A translation for P need not be discarded merely because the CPU switches to Q.
B. The ASID alone identifies a physical page without the virtual page number.
C. Reusing P's ASID for an unrelated address space may require invalidating stale translations carrying that ASID.
D. ASIDs eliminate the need to update a translation after its page-table mapping changes.

### Q20. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

For the grammar S→aSb | SS | ε, which statements are correct?

**Candidates**

**I.** Every generated string contains equally many a's and b's.

**II.** Every generated string has all a's before all b's.

**III.** The string abab is generated.

**IV.** The string ba is generated.

A. III and IV  
B. I and II  
C. I and III  
D. I and IV

### Q21. [1 Mark] [NAT]

A binary search tree contains distinct keys1,3,4,5,7,8 and has postorder traversal1,4,3,8,7,5. Starting from an empty BST and using ordinary leaf insertion without rotations, how many different insertion orders generate this exact tree?

**Answer format:** Exact integer.

### Q22. [1 Mark] [NAT]

A sorted file has 64 data blocks. A sparse primary index has one entry per data block and fits in a single memory-resident index block. A key search uses that index to identify the correct data block; keys are distinct. How many disk block reads are needed to retrieve a present record, assuming the data block is not cached?

**Answer format:** Integer.

### Q23. [1 Mark] [NAT]

A min-heap stores distinct keys in a one-based array of length15. A particular key's array index is known to be6. Ignoring its own position, how many other array positions are guaranteed to contain larger keys solely because of the heap-order property?

**Answer format:** Integer.

### Q24. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In the subset lattice of {a,b,c}, ordered by inclusion, which statements are correct?

A. The meet of{a,b} and{b,c} is{b}.  
B. Their join is{a,b,c}.  
C. They are comparable.  
D. The empty set is a lower bound of every pair of elements.

### Q25. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Let h map both a and b to the single symbol 0 and extend by concatenation. For L={aⁿbⁿ:n≥0}, which statements are correct?

**Candidates**

**I.** h(L)={0²ⁿ:n≥0}.

**II.** h(L) is regular.

**III.** Since h(L) is regular, L must be regular.

**IV.** h erases every input symbol.

A. II and III  
B. I and II  
C. II and IV  
D. III and IV

### Q26. [1 Mark] [MSQ]

For A with rows (0,1),(1,0), which statements are true?

A. A is nonsingular.
B. A has an LU factorization with unit-diagonal lower-triangular L and upper-triangular U without any row permutation.
C. Swapping the rows permits such an LU factorization.
D. Every nonsingular matrix must permit elimination without pivoting.

### Q27. [1 Mark] [NAT]

A tabular minimization pattern `1-0--` has five bit positions. How many minterms does it represent?

**Answer format:** Integer.

### Q28. [1 Mark] [MCQ]

A directed graph has a negative-weight cycle that is unreachable from source s. Which statement about source-reachable shortest paths follows?

A. Every source-reachable distance is necessarily undefined.
B. The unreachable cycle alone does not destroy shortest-path distances from s.
C. The cycle must be removed before even identifying vertices reachable from s.
D. All edge weights reachable from s must therefore be nonnegative.

### Q29. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A variable is live if its current value may be read along a subsequent control-flow path before being overwritten. In the code below, x, y, z and flag are ordinary variables, and there are no implicit uses after return. Which set contains exactly the variables live at P, immediately before y = z?

```text
L: x = y
   if flag goto K
P: y = z
   goto L
K: return x
```

A. {z, flag}  
B. {x, z, flag}  
C. {y, z, flag}  
D. {x, y, z, flag}

### Q30. [1 Mark] [NAT]

Define F(x)=the integral of (2t+1) from t=0 to t=x. What is the integral of xF'(x)−F(x) over x from 0 to 1?

**Answer format:** Decimal rounded to four places.

### Q31. [1 Mark] [MCQ]

For one program, processor P executes N instructions at CPI=1.5 and 3 GHz. Processor Q executes 0.8N instructions at CPI=2 and 4 GHz. Ignore all other delays. What is Q's speedup over P?

A. 0.8
B. 1.0
C. 1.25
D. 1.5

### Q32. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A data set has five real observations with median 10 and mean 12. A sixth observation equal to 100 is appended. Which quantity is determined uniquely from this information?

A. The new median.  
B. The new mean.  
C. The new range.  
D. The new population variance.

### Q33. [1 Mark] [MSQ]

Let L1={aⁿbⁿ:n≥0} and L2={aⁿb^(2n):n≥0}. Which statements are true?

A. L1∪L2 is context-free.
B. L1∩L2={ε}.
C. Every intersection of two context-free languages is context-free.
D. L1L2 is context-free.

### Q34. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In a basic block, t=a+b is computed, then a store through pointer p occurs, then u=a+b is computed. The scalar values a,b reside in memory and p may alias them. Arithmetic is exact and has no side effects. Which statements are correct?

A. Reusing t for u without alias information can be unsound.  
B. Proving the store cannot change a or b permits reuse in this block.  
C. Identical expression text alone guarantees equal values across the store.  
D. Recomputing a+b after the store preserves the required new operand values.

### Q35. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In the additive group Z12, let H be the subgroup generated by 8. What is the order of the coset 5+H in the quotient group Z12/H?

A. 3  
B. 4  
C. 6  
D. 12

### Q36. [2 Marks] [MCQ]

For the unary language L={a^(n²):n≥0}, a pumping proof chooses a^(p²) and a pumped segment of length d with 1≤d≤p. Why does pumping once extra give a contradiction?

A. p²+d lies strictly between p² and (p+1)², so it is not a square.
B. p²+d is always less than p².
C. Every unary language is finite.
D. Pumping is prohibited for unary alphabets.

### Q37. [2 Marks] [NAT]

An undirected graph has vertices1 through5 and edges12,23,31,34,45. A signed vertex-edge incidence matrix assigns an arbitrary orientation to every edge, placing−1 at its tail and+1 at its head. What is the dimension of the null space of this matrix over the real numbers?

**Answer format:** Integer.

### Q38. [2 Marks] [NAT]

A four-to-one multiplexer selects data input D(2s1+s0), where s1,s0 are the select bits. To implement F(a,b,c)=1 exactly when precisely one of a,b,c is1, choose s1=a,s0=b. Each data input may be0,1,c,or NOT c. How many of the four required data inputs equal NOT c?

**Answer format:** Integer.

### Q39. [2 Marks] [MCQ]

A programming language permits arbitrarily nested comments, with tokens OPEN and CLOSE marking comment boundaries. Why is a fixed finite-state lexer, with no extra stack or counter, insufficient to recognize exactly the balanced comment sequences of unbounded depth?

A. It would need to distinguish arbitrarily many outstanding OPEN counts.
B. Every finite input requires infinitely many processing steps.
C. The two-token alphabet is infinite.
D. All non-nested comments are also nonregular by definition.

### Q40. [2 Marks] [NAT]

A buddy allocator manages one aligned1024-byte region and rounds each request up to a power of two, with no headers. It allocates A=200 bytes at address0, B=200 bytes at address256, and C=400 bytes at address512. After freeing A and B, what is the largest new single request, in bytes, that can be satisfied without freeing C?

**Answer format:** Exact integer.

### Q41. [2 Marks] [NAT]

A TCP sender has 3000 bytes outstanding. Its congestion window is 5000 bytes, and its receiver-advertised window is 4000 bytes. An ACK newly acknowledges 1000 bytes and advertises a new receiver window of 2500 bytes. The congestion window remains 5000. No other data is sent or acknowledged during this event. How many additional bytes may the sender transmit immediately?

**Answer format:** Exact integer.

### Q42. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For grammar S→L=R | R, L→*R | id, R→L, consider an LR(0) item set containing S→L·=R and R→L·. In SLR parsing, FOLLOW(R) contains '='. What conflict occurs in the SLR table for lookahead '='?

A. No conflict, because completed items are ignored on '='.  
B. Shift–reduce conflict between shifting '=' and reducing R→L.  
C. Reduce–reduce conflict between two completed productions shown here.  
D. Accept–reduce conflict because every completed item accepts the input.

### Q43. [2 Marks] [NAT]

Processes P and Q each reference two private pages. The interleaved reference sequence is P1,Q1,P2,Q2,P1,Q1,P2,Q2. Compare three initially empty frames managed by global FIFO with local FIFO allocating two frames exclusively to P and one exclusively to Q. How many more page faults occur under the global allocation?

**Answer format:** Integer.

### Q44. [2 Marks] [NAT]

A file-system inode contains four direct block pointers and one single-indirect pointer. Each disk block is 1024 bytes and each pointer is four bytes. No other addressing scheme exists. What is the largest file size in bytes that this inode can address? Indirect-block storage is not part of the file's data.

**Answer format:** Integer.

### Q45. [2 Marks] [NAT]

A DMA device delivers one word every 2 microseconds. The processor is interrupted after each batch of k words. Processing a batch takes 8+k microseconds, including all overhead, and starts as soon as that batch completes if the processor is free. DMA continues into other buffers while processing occurs. There is no other work. Require a steady state without growing backlog and a latency of at most 40 microseconds from arrival of the first word of each batch to completion of processing that batch. How many positive integers k satisfy both requirements?

**Answer format:** Integer.

### Q46. [2 Marks] [NAT]

How many permutations of six labelled elements have only even-length cycles in their disjoint-cycle decomposition?

**Answer format:** Integer.

### Q47. [2 Marks] [NAT]

A B+ tree has a root with two internal children. Each of those children has exactly three leaf children. Every leaf contains exactly four data entries. Internal separator copies are not data entries. How many data entries does the tree contain?

**Answer format:** Integer.

### Q48. [2 Marks] [NAT]

How many permutations of {1,2,3,4,5} place1 before2 before3, with no restriction on the relative positions of4 and5?

**Answer format:** Integer.

### Q49. [2 Marks] [MCQ]

A datagram socket has queued datagrams of lengths 12 and 5 bytes, in that order. Each receive uses an 8-byte buffer. The specified API returns at most one datagram per receive and discards excess bytes of a truncated datagram. What byte counts do the next two receives return?

A. 8 and 8
B. 8 and 5
C. 12 and 5
D. 8 and 4

### Q50. [2 Marks] [MCQ]

A comparison sorting algorithm sorts n distinct keys. Its decision tree has binary comparison outcomes. Which is a valid worst-case lower-bound argument?

A. There are n possible outputs, so height is at least log₂n.
B. There are n! possible input orders requiring different sorting permutations, so height is at least ceil(log₂(n!)).
C. Every sorting algorithm must use exactly n² comparisons.
D. Each comparison places one key permanently, so n comparisons always suffice.

### Q51. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A proposed undecidability proof transforms a machine M and input w into a recognizer N that, on every input x, simulates M on w and accepts x if that simulation halts. It then claims that testing whether L(N) is regular decides whether M halts on w. What is the flaw?

A. The construction requires knowing in advance whether M halts.  
B. Both possible languages of N are regular, so the test does not distinguish halting from nonhalting.  
C. N always recognizes a nonregular language.  
D. A recognizer cannot simulate another machine on a fixed input.

### Q52. [2 Marks] [MCQ]

Let e_n be the number of binary strings of length n that have no consecutive 1s and contain an even number of 1s. The empty string is counted, so e_0=1. Which formal ordinary generating function E(x)=sum over n>=0 of e_n*x^n is correct?

A. (1+x)/(1-x-x^2)  
B. (1-x+x^3)/(1-2x+x^2-x^4)  
C. 1/(1-x-x^2)  
D. (1-x)/(1-2x+x^2-x^4)

### Q53. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A machine has a 1 ns clock, ideal CPI=1, and no overlapping stalls. Conditional branches are 20% of instructions. A static predictor predicts not taken; 60% of branches are taken, and each misprediction costs three additional cycles. A new predictor mispredicts 10% of all branches but requires a 1.1 ns clock; all other CPI contributions stay unchanged. Approximately what is the new processor's speedup over the old one on the same instruction stream?

A. 0.857  
B. 1.166  
C. 1.283  
D. 1.360

### Q54. [2 Marks] [MSQ]

A DNS record is cached with a positive TTL. The authoritative server changes the record before that TTL expires. Assume ordinary caching without an explicit invalidation mechanism. Which statements are correct?

A. A resolver can continue returning the cached old record until expiry.
B. Every cache is immediately informed of the authoritative change by the TTL field itself.
C. Reducing the authoritative record's TTL afterward does not retroactively shorten a previously cached expiry under this model.
D. TTL is a guarantee that the authoritative value cannot change during that interval.

### Q55. [2 Marks] [NAT]

An instruction computes an address by first adding a signed displacement to a base register, then reading a32-bit pointer from that address, then using the pointer as the final operand address. Base=1000, displacement=12, and memory word at1012 contains2040. The operand is a four-byte integer. How many data-memory reads are needed to obtain the operand, excluding instruction fetch and assuming no cache hits?

**Answer format:** Integer.

### Q56. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Two transactions both hold shared locks on x and each requests an upgrade to an exclusive lock before releasing its shared lock. No other transaction holds a lock. Which statements are correct?

**Candidates**

**I.** Both upgrade requests can block, creating a deadlock.

**II.** The two-phase-locking rule by itself prevents this deadlock.

**III.** Each exclusive upgrade conflicts with the other transaction's shared lock.

**IV.** The original pair of shared locks already conflicted with each other.

A. III and IV  
B. I and II  
C. I and IV  
D. I and III

### Q57. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

What pair is printed by this C program? The && operator short-circuits and sequences evaluation of its left operand before its right operand.

```c
#include <stdio.h>
int main(void) {
    int a[5] = {1,2,0,4,5};
    int i = 0, sum = 0;
    while (i < 5 && a[i++] > 0)
        sum += a[i];
    printf("%d %d\n", i, sum);
    return 0;
}
```

A. 2 3  
B. 3 2  
C. 2 2  
D. 3 3

### Q58. [2 Marks] [NAT]

Over alphabet {0,1}, accept a word exactly when it contains exactly one position at which two adjacent symbols are equal. Overlapping adjacent pairs count separately: 000 has two such positions. What is the number of states in the minimal complete DFA, including a rejecting sink?

**Answer format:** Integer.

### Q59. [2 Marks] [NAT]

A synchronous circuit has two D flip-flops with state(a,b), initialized to(0,1). Its next state is(a XOR b,a), using old values simultaneously. An output pulse occurs on an edge exactly when the old state is(1,0). How many output pulses occur during the first eight clock edges?

**Answer format:** Integer.

### Q60. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Six distinct keys are in two already sorted runs of three keys each. Only comparisons between keys reveal their relative order. What is the smallest achievable worst-case number of additional comparisons needed to merge the runs into one sorted run?

A. 3  
B. 4  
C. 5  
D. 6

### Q61. [2 Marks] [NAT]

How many truth assignments to propositions p,q,r,s satisfy all three conditions: p implies q, r implies q, and s is true exactly when p and r have different truth values?

**Answer format:** Integer.

### Q62. [2 Marks] [MCQ]

A linear-probing table has occupied slots 2,3,4 holding keys whose home slots are respectively 2,2,4. Slot 5 has never been occupied. The key in slot 2 is deleted. Which repair preserves searches for the two remaining keys if no tombstones are allowed?

A. Leave slot 2 empty and do nothing else.
B. Move the key from slot 3 to slot 2 and leave slot 3 empty; keep the key whose home is 4 in slot 4.
C. Move the key from slot 4 to slot 2 and leave slot 3 unchanged.
D. Clear all three slots without reinserting either remaining key.

### Q63. [2 Marks] [NAT]

A memoized function F(n) has base F(0)=0,F(1)=1. For n≥2 it calls F(n−1), then F(n−2), sums the results, and stores the result. The cache is initially empty, and base cases are cached too. On a cache hit, the function returns immediately. During evaluation of F(6), how many function invocations occur, including cache hits and the initial call?

**Answer format:** Exact integer.

### Q64. [2 Marks] [NAT]

A system has three page frames and initially no resident pages. It uses optimal replacement with knowledge of the future. For references 1,2,3,4,1,2,5,1,2,3,4,5, how many page faults occur?

**Answer format:** Integer.

### Q65. [2 Marks] [NAT]

Integers a,b,c,d independently range over the full eight-bit two's-complement range. What is the minimum signed two's-complement width sufficient to represent every exact value of ab−cd, without overflow?

**Answer format:** Integer bits.

---

## ANSWER KEY — MOCK TEST 041

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | B |
| 2 | NAT | 1 | 11.11 (two decimals) |
| 3 | MSQ | 1 | A, C, D |
| 4 | MCQ | 1 | A |
| 5 | MSQ | 1 | A, B, C |
| 6 | MCQ | 2 | A |
| 7 | MSQ | 2 | B, C, D |
| 8 | NAT | 2 | 8 |
| 9 | MCQ | 2 | A |
| 10 | MCQ | 2 | A |
| 11 | MCQ | 1 | C |
| 12 | NAT | 1 | 1200 |
| 13 | NAT | 1 | 128 |
| 14 | NAT | 1 | 0.02 |
| 15 | MCQ | 1 | C |
| 16 | NAT | 1 | 3 |
| 17 | NAT | 1 | 10 |
| 18 | NAT | 1 | 100 |
| 19 | MSQ | 1 | A, C |
| 20 | MCQ | 1 | C |
| 21 | NAT | 1 | 20 |
| 22 | NAT | 1 | 1 |
| 23 | NAT | 1 | 2 |
| 24 | MCQ | 1 | C |
| 25 | MCQ | 1 | B |
| 26 | MSQ | 1 | A, C |
| 27 | NAT | 1 | 8 |
| 28 | MCQ | 1 | B |
| 29 | MSQ | 1 | B, C, D |
| 30 | NAT | 1 | 0.3333 (accepted range 0.33325–0.33335) |
| 31 | MCQ | 1 | C |
| 32 | MSQ | 1 | A, C, D |
| 33 | MSQ | 1 | A, B, D |
| 34 | MCQ | 1 | C |
| 35 | MSQ | 1 | A, C, D |
| 36 | MCQ | 2 | A |
| 37 | NAT | 2 | 1 |
| 38 | NAT | 2 | 2 |
| 39 | MCQ | 2 | A |
| 40 | NAT | 2 | 512 |
| 41 | NAT | 2 | 500 |
| 42 | MSQ | 2 | A, C, D |
| 43 | NAT | 2 | 2 |
| 44 | NAT | 2 | 266240 |
| 45 | NAT | 2 | 4 (exact) |
| 46 | NAT | 2 | 225 |
| 47 | NAT | 2 | 24 |
| 48 | NAT | 2 | 20 |
| 49 | MCQ | 2 | B |
| 50 | MCQ | 2 | B |
| 51 | MSQ | 2 | A, C, D |
| 52 | MCQ | 2 | B |
| 53 | MSQ | 2 | A, C, D |
| 54 | MSQ | 2 | A, C |
| 55 | NAT | 2 | 2 |
| 56 | MCQ | 2 | D |
| 57 | MSQ | 2 | A, C, D |
| 58 | NAT | 2 | 6 |
| 59 | NAT | 2 | 3 |
| 60 | MSQ | 2 | A, B, D |
| 61 | NAT | 2 | 5 |
| 62 | MCQ | 2 | B |
| 63 | NAT | 2 | 11 |
| 64 | NAT | 2 | 7 |
| 65 | NAT | 2 | 16 |
