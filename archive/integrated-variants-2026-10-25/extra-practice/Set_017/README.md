# GATE CS — Additional Practice Set 017

**Questions:** 50  
**Maximum marks:** 75

Read the task above each embedded question carefully. For an invalid-answer task, select options that do not correctly answer the embedded question. For a pair task, select the pair containing all valid candidates. MCQ has one correct choice; MSQ requires all correct choices. The answer key follows Q50.

### Q1. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A process executes the following pseudocode. Every fork succeeds, fork returns 0 only in the child, and all processes eventually execute print once. There is no buffered output before a fork.

```text
i = 0
while i < 3:
    if fork() == 0:
        break
    i = i + 1
print(i)
```

Ignoring output order, which multiset of values is printed?

A. {0,1,2,3}  
B. {0,1,1,2,2,2,3,3}  
C. {3,3,3,3}  
D. {0,0,0,3}  

### Q2. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A processor first checks L1. Every L1 access takes 1 ns. On an L1 miss it next checks L2, taking an additional 6 ns; on an L2 miss it additionally accesses memory, taking 60 ns. There is no overlap. Initially the L1 miss probability is 0.10 and the L2 local miss probability conditional on an L1 miss is 0.20. An L1 redesign reduces its miss probability to 0.05 but changes its access time to t ns. L2 timing and its conditional miss probability remain unchanged. For strictly lower average access time, which condition on t is necessary and sufficient?

A. t < 1.9 ns  
B. t < 2.8 ns  
C. t < 1.3 ns  
D. t < 3.6 ns  

### Q3. [1 Mark] [MSQ]

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

### Q4. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

What does the following conforming C program print? All arithmetic fits in int.

```c
#include <stdio.h>
static void change(int **p, int *q) {
    int *t = *p;
    *p = q;
    *t += **p;
    **p += 1;
}
int main(void) {
    int a[3] = {2,5,9};
    int *p = a;
    change(&p, a+1);
    change(&p, a);
    printf("%d %d %d\n", a[0], a[1], (int)(p-a));
    return 0;
}
```

A. 7 13 0  
B. 8 13 0  
C. 8 6 1  
D. The program has undefined behaviour due to pointer aliasing.  

### Q5. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Two threads each execute the following two-iteration loop on shared x, initially 0. Each read and write is atomic, the computation uses a private register r, and execution is a sequentially consistent interleaving preserving each thread's order.

```text
repeat twice:
    r = x
    x = r + 1
```

Which values of x are possible after both threads finish?

A. 1  
B. 2  
C. 3  
D. 4  

### Q6. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A producer performs V(s) twice and terminates. A consumer performs P(s), prints X, performs P(s), and prints X again. Initially s=0. Operations are atomic; scheduling is fair. For a counting semaphore, V increments its count. For the binary version in this question, V sets its value to 1 even if already 1; a successful P changes 1 to 0, otherwise blocks. Which statements are correct?

A. With the counting semaphore, the consumer eventually prints twice.  
B. With the binary semaphore, the consumer can print once and then remain blocked forever.  
C. With the binary semaphore, the consumer can print twice.  
D. With the counting semaphore, the consumer can remain blocked forever without printing, after the producer has terminated.  

### Q7. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

L is a Turing-recognizable language, and the halting problem has a computable many-one reduction to L. Which statements must hold?

**Candidates**

**I.** L is undecidable.

**II.** L is not Turing-recognizable.

**III.** The complement of L is not Turing-recognizable.

**IV.** The reduction gives a total decision procedure for L.

A. II and III  
B. II and IV  
C. I and III  
D. III and IV  

### Q8. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Use the standard SLR(1) construction for the augmented grammar below. How many LR(0) item-set states have a shift/reduce conflict in the resulting SLR table?

```text
S' -> S
S  -> A a | b A c | d c | b d a
A  -> d
```

A. 0  
B. 2  
C. 1  
D. 3  

### Q9. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Let U be an undecidable but recognizable language. Which statements are correct?

**Candidates**

**I.** U's complement cannot also be recognizable.

**II.** U must be infinite.

**III.** Every subset of U is recognizable.

**IV.** U cannot contain any decidable infinite subset.

A. I and II  
B. III and IV  
C. I and III  
D. I and IV  

### Q10. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A survey includes 120 people. Seventy read newspaper A, sixty read newspaper B, and twenty read neither. Among those who read at least one, what fraction read exactly one?

A. 3/10  
B. 7/10  
C. 3/4  
D. 5/6  

### Q11. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A file contains 100 fixed-size records in ten disk blocks, ten records per block. An in-memory index gives the exact block containing any requested record. Ten requested record numbers are independently and uniformly selected with replacement from the 100 records. A data block is read from disk only on its first request and then remains cached. Which expression is the expected number of disk reads?

A. 10  
B. 10(1−(9/10)¹⁰)  
C. 100(1−(99/100)¹⁰)  
D. (9/10)¹⁰  

### Q12. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

For grammar A→Aa | Ab | c, which regular expression describes its language?

A. (a|b)*c  
B. c(a|b)*  
C. a*b*c  
D. c(ab)*  

### Q13. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Three tasks A,B,C take 4,3,2 hours. A and B may run simultaneously on separate workers, but C requires both to have finished and uses one worker. Exactly two workers are available and tasks cannot be split. What is the minimum completion time for all tasks?

A. 5 hours  
B. 6 hours  
C. 7 hours  
D. 9 hours  

### Q14. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Two processes use a shared counting semaphore initialized to 0. P executes `signal(s); signal(s);`, while Q executes `wait(s); wait(s); print();`. There are no other accesses. Which statements are correct?

**Candidates**

**I.** If both processes are eventually scheduled and semaphore operations are correct, Q can eventually print.

**II.** The two signals collapse into a single remembered event.

**III.** Q may block on its first wait depending on scheduling.

**IV.** Q must print before P executes its second signal.

A. III and IV  
B. I and III  
C. I and II  
D. I and IV  

### Q15. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

The three-input majority function is F=xy+xz+yz. A two-to-one multiplexer selects D0 when x=0 and D1 when x=1. Which pair (D0,D1) realizes F?

A. (y OR z, y AND z)  
B. (y AND z, y OR z)  
C. (y XOR z, y AND z)  
D. (NOT y, z)  

### Q16. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Let f(n)=n log₂n and g(n)=n^(3/2), for integers n≥2. Which statements are true?

**Candidates**

**I.** f is O(g).

**II.** g is O(f).

**III.** f is o(g).

**IV.** f and g are Θ-equivalent.

A. I and IV  
B. II and III  
C. II and IV  
D. I and III  

### Q17. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Choose the order that gives the clearest causal sequence.

P. The alarm then sounded as designed.
Q. The technician first disconnected the sensor's power supply.
R. This demonstrated that the system detected the simulated failure.
S. The disconnection removed the sensor's normal signal.

A. Q–S–P–R  
B. P–Q–R–S  
C. S–R–Q–P  
D. Q–R–S–P  

### Q18. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Relation Child(cid,pid) has primary key cid and a foreign key pid referencing Parent(pid), whose primary key is pid. Child.pid is nullable and referential integrity uses ordinary SQL semantics without additional restrictions. Which statements are correct?

**Candidates**

**I.** Two Child rows with different cid values may reference the same parent.

**II.** A non-NULL Child.pid must match a Parent.pid.

**III.** Every parent must be referenced by at least one child.

**IV.** Child.pid must be unique because it is a foreign key.

A. II and IV  
B. I and II  
C. III and IV  
D. I and III  

### Q19. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Languages A and B satisfy A≤mB: a total computable function f obeys x∈A iff f(x)∈B. Which implications necessarily hold?

**Candidates**

**I.** If B is decidable, A is decidable.

**II.** If A is decidable, B is decidable.

**III.** If A is not recognizable, B is not recognizable.

**IV.** If B is not recognizable, A is not recognizable.

A. III and IV  
B. I and II  
C. I and III  
D. I and IV  

### Q20. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A PDA's stack alphabet has only one ordinary symbol X plus a protected bottom marker. Which capabilities can it still support?

A. Counting an unbounded run of a symbols by pushing one X per a.  
B. Matching a later run of b symbols to that count by popping one X per b.  
C. Storing every arbitrary binary prefix exactly using only one X per input symbol and no other encoding or memory.  
D. Having infinitely many possible stack heights despite a finite stack alphabet.  

### Q21. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A weighted undirected connected graph has some negative edge weights. Which statements about Kruskal's MST algorithm are true?

**Candidates**

**I.** Sorting edges by nondecreasing weight and rejecting cycle-forming edges remains correct.

**II.** Every negative edge must be included, even if the negative edges form a cycle.

**III.** The cut/exchange justification does not require all weights to be nonnegative.

**IV.** Replacing all weights w by w+c for one constant c can change which spanning trees minimize total weight.

A. I and III  
B. I and IV  
C. II and III  
D. II and IV  

### Q22. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

After a successful fork, both processes execute `counter++`, where counter was an ordinary private global integer equal to 5 before fork. There is no shared-memory mapping. After both increments, what are their counter values?

A. Each process has value 6 in its own address space.  
B. Both necessarily observe a shared value 7.  
C. The child must have value 1.  
D. The parent must retain value 5.  

### Q23. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

In an S-attributed syntax-directed definition, which attribute kind is used?

A. Synthesized attributes only.  
B. Inherited attributes only.  
C. No attributes at all.  
D. Attributes that can depend only on future input characters, never on children.  

### Q24. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An HTTP cache has two stored representations of the same URL, selected by different values of a request header named in Vary. Why must that header be considered during lookup?

A. The same URL can require different cached representations depending on that header.  
B. Vary means every cached representation has an infinite lifetime.  
C. HTTP never uses request headers.  
D. The header changes the TCP sequence-number arithmetic.  

### Q25. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A four-port Ethernet switch initially has dynamic entries A→1, B→2, C→3 and no entry for D. It learns or updates the source port before forwarding each frame, floods an unknown destination to every port except ingress, and has no entry expiry during this sequence. Four frames arrive in order: (ingress 3, source A, destination B), (ingress 2, source B, destination A), (ingress 3, source C, destination D), (ingress 4, source D, destination C). Which lists their respective egress-port sets?

A. {2}; {3}; {1,2,4}; {3}  
B. {2}; {1}; {1,2,4}; {3}  
C. {2}; {3}; {1,2,3,4}; {3}  
D. {2}; {3}; {4}; {1,2,3}  

### Q26. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Consider S→aSbS | bSaS | ε. Which statements are true?

A. Every generated word has equally many a and b symbols.  
B. The word abab has more than one parse tree.  
C. Every prefix of every generated word has at least as many a as b symbols.  
D. The generated language is regular.  

### Q27. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Two transactions execute r1(X),w1(X),r2(X),w2(Y),r1(Y), then both commit, with operations listed in execution order. Which statement about conflict serializability is correct?

A. Equivalent to T1 followed by T2 because T1 first accesses X.  
B. Equivalent to T2 followed by T1 because T2 writes Y.  
C. Serializable because reads never participate in conflicts.  
D. Not conflict-serializable because the precedence graph contains both T1→T2 and T2→T1.  

### Q28. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Two blocking message queues A and B each have capacity one and are initially empty. Process P sends two messages to A before receiving from B. Process Q sends two messages to B before receiving from A. Both processes are eventually scheduled, and neither removes messages in any other way. What happens?

A. Both processes necessarily complete because the queues start empty.  
B. Only P can block; Q cannot.  
C. Both eventually block on their second send, with neither able to reach its receive.  
D. Sending to a full queue automatically deletes the older message.  

### Q29. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Six simultaneous UDP flows use six distinct internal source IP/port pairs; three connect to remote endpoint X and three to a different endpoint Y. Each public IPv4 address provides four usable external ports. Under policy I, each internal source pair needs its own external port independent of remote endpoint. Under policy II, an external port may be reused for X and Y, and reverse lookup includes that remote endpoint. What are the minimum public-address counts under policies I and II respectively?

A. (1,1)  
B. (2,1)  
C. (2,2)  
D. (3,2)  

### Q30. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A schedule consists of w1(x),w2(x),w1(x), followed by commits after all writes. There are no reads. The first and last writes belong to T1 and the middle write to T2. All writes assign fixed constants independently of prior values. Which statements are correct?

**Candidates**

**I.** Its conflict graph is acyclic.

**II.** It is view-equivalent to the serial order T2,T1.

**III.** It is conflict-serializable.

**IV.** Its final writer of x is T1.

A. I and II  
B. II and IV  
C. I and III  
D. I and IV  

### Q31. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An even-parity bit is appended to each fixed-length data word. Which statements are correct?

A. Every single-bit error in the transmitted word is detected.  
B. Every two-bit error is detected.  
C. Some errors affecting the parity bit and one data bit are undetected.  
D. Every odd number of flipped bits is detected.  

### Q32. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A database permits uncommitted updates to reach disk and uses an undo log. Before overwriting an on-disk data item, its old value is forced into the log. Which statements are correct?

**Candidates**

**I.** The log-before-data rule supplies information needed to undo an uncommitted on-disk update.

**II.** Writing the old value to the log only after overwriting the disk item is equally safe against a crash between those writes.

**III.** A transaction's abort may require restoring disk data, not merely clearing a memory buffer.

**IV.** The stated rule by itself proves that every committed update is already on disk.

A. II and III  
B. II and IV  
C. III and IV  
D. I and III  

### Q33. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A bounded buffer has capacity2 and is initially empty. A semaphore empty starts at2, full at0, and mutex at1. A consumer mistakenly executes wait(mutex), then wait(full), and retains mutex while blocked. A producer executes wait(empty), then wait(mutex) before inserting. Which statements are correct if the consumer runs first?

A. The consumer can block while holding mutex.  
B. The producer can then block on mutex while unable to insert the item that would release the consumer.  
C. Increasing the buffer capacity alone fixes this ordering bug for an initially empty buffer.  
D. Having the consumer wait(full) before wait(mutex) avoids this particular hold-and-wait cycle.  

### Q34. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A routing table contains prefix203.0.113.0/24 via X and more-specific prefix203.0.113.128/25 via Y. No other route matches. Which statements are correct under longest-prefix matching?

A. Address203.0.113.200 uses Y.  
B. Address203.0.113.100 uses X.  
C. Installing the /24 after the /25 necessarily makes it override the /25.  
D. Removing the /25 makes203.0.113.200 use X.  

### Q35. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

An application sends two messages over one TCP connection, adding no lengths, delimiters or other framing. The receiver knows neither message length. Which statements are correct?

**Candidates**

**I.** TCP's ordered delivery alone identifies the boundary between the messages.

**II.** The same received byte string may correspond to more than one split into two messages.

**III.** A protocol-level length field can make boundaries recoverable.

**IV.** One send call necessarily corresponds to one recv call.

A. I and II  
B. I and III  
C. II and III  
D. I and IV  

### Q36. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A foreign key has two columns(x,y) and uses the stated rule: if either referencing component is NULL, no referenced-row match is required; otherwise the pair must match. Which inserted pairs can pass the foreign-key check when the referenced table is empty?

A. (NULL,5)  
B. (7,NULL)  
C. (NULL,NULL)  
D. (7,5)  

### Q37. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Initially x=y=1 and a database invariant requires x+y≥1. Two concurrent transactions read the same initial snapshot. T1, seeing y=1, writes x=0; T2, seeing x=1, writes y=0. A scheme rejects only concurrent writes to the same item, so both commit. Which statements are correct?

A. Their writes target different items.  
B. The final state violates the invariant.  
C. The execution is equivalent to a serial execution of these conditional transactions.  
D. Avoiding direct write-write conflicts alone is insufficient for this invariant.  

### Q38. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Assume mathematical integer arithmetic and no aliasing. In the code below, which statements are correct?

```text
p = a + b
b = b + 1
q = a + b
r = a + b
```

**Candidates**

**I.** q may always be replaced by p.

**II.** r may be replaced by q.

**III.** The assignment to b kills availability of the original a+b value for q.

**IV.** The repeated textual spelling alone proves all three sums equal.

A. II and IV  
B. II and III  
C. III and IV  
D. I and II  

### Q39. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Two virtual pages of one process intentionally map to the same physical frame. Both mappings are writable and there is no copy-on-write mechanism. Which statements are correct?

**Candidates**

**I.** A write through one mapping can be read through the other at the corresponding offset.

**II.** The virtual page numbers must be equal.

**III.** The mappings can have different virtual addresses while sharing storage.

**IV.** Each write necessarily allocates a fresh physical frame.

A. III and IV  
B. I and II  
C. I and III  
D. I and IV  

### Q40. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

“The grant was contingent on the laboratory obtaining approval.” Which phrase best replaces “contingent on” without changing the meaning?

A. unrelated to  
B. dependent on  
C. completed before  
D. guaranteed despite  

### Q41. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

Over GF(2), a CRC generator is g(x)=x³+x+1. The transmitted codeword suffers error polynomial e(x)=x^k g(x), for some k≥0 that fits within the transmitted frame. Which statements are correct?

**Candidates**

**I.** The CRC remainder of the error polynomial is zero.

**II.** This nonzero error can escape detection.

**III.** Multiplication by x^k guarantees detection of every nonzero polynomial.

**IV.** The error polynomial must be a single-bit error.

A. I and II  
B. I and IV  
C. II and III  
D. II and IV  

### Q42. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A lexer uses maximal munch with tokens HEX=0x[0-9A-F]+ and ID=[A-Z]+. No rule requires whitespace between tokens. On the input0x1G, which statements are correct?

**Candidates**

**I.** The lexer can return HEX with lexeme0x1 followed by ID with lexemeG.

**II.** The entire input must be one valid HEX token because it starts with0x.

**III.** Successful tokenization alone does not prove that the token sequence is a valid expression in the parser's grammar.

**IV.** G is a valid hexadecimal digit under the given HEX rule.

A. II and III  
B. I and III  
C. II and IV  
D. III and IV  

### Q43. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

An instance of R(A,B) contains exactly(1,2) and(2,2). Which proposed functional dependency is violated by this instance?

A. A→B  
B. AB→A  
C. B→A  
D. AB→B  

### Q44. [1 Mark] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Initially, on-call flags A and B are both 1. Transaction T1 reads B and, if B=1, writes A=0. Transaction T2 reads A and, if A=1, writes B=0. Both read the same initial snapshot. A system rejects concurrent transactions only when they write a common item. Which statements hold?

A. Both transactions can commit under this rule.  
B. Every serial execution leaves A=B=0.  
C. The committed outcome can violate the invariant A+B≥1.  
D. Testing only for overlapping write sets fails to prevent this anomaly.  

### Q45. [2 Marks] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A NAT maps internal TCP endpoint 192.168.1.8:5000 to public endpoint 203.0.113.2:42000 for a connection to 198.51.100.9:443. It translates an outgoing IPv4 packet with no options and no fragmentation. Which checksum fields must be updated because of these substitutions?

A. Only the IPv4 header checksum.  
B. Only the TCP checksum.  
C. Neither checksum, because payload bytes are unchanged.  
D. Both the IPv4 header checksum and the TCP checksum.  

### Q46. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A toy floating-point format has four significant binary bits and round-to-nearest, ties-to-even. It supports all exponents needed below. Which real values round to exactly1.5?

A. 1.4375  
B. 1.49  
C. 1.5625  
D. 1.625  

### Q47. [2 Marks] [MCQ]

Select the one option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

A linear-probing hash table uses EMPTY for never-used slots and DELETED for tombstones. Searches stop at EMPTY, but continue past DELETED. Which claims hold?

A. Replacing a deleted occupied slot by EMPTY can make another existing key unreachable by search.  
B. An insertion can remember the first DELETED slot, continue searching for an existing copy of its key, then reuse that slot if the key is absent.  
C. A search can always stop at DELETED because it no longer contains a key.  
D. Tombstones can increase the number of probes in an unsuccessful search.  

### Q48. [2 Marks] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A client has a fresh cached DNS address for host h and an HTTP cache entry for a resource on h. The HTTP entry is stale but has an entity tag. Which statements hold?

**Candidates**

**I.** Revalidating the HTTP entry need not require a fresh DNS query.

**II.** A conditional request can allow the server to confirm reuse of the cached body without resending that body.

**III.** A valid DNS cache entry guarantees that every cached HTTP resource for h is fresh.

**IV.** Receiving an HTTP response automatically renews the DNS record's TTL.

A. II and IV  
B. III and IV  
C. I and III  
D. I and II  

### Q49. [1 Mark] [MCQ]

Select the pair containing **all and only the valid answers** to the following question.

**Question to evaluate**

A transmitted binary word contains data bits followed by one even-parity bit. The receiver checks only whether the parity of the whole received word is even. Which errors are always detected?

**Candidates**

**I.** Exactly one data bit flips.

**II.** Exactly two data bits flip.

**III.** Exactly one data bit and the parity bit flip.

**IV.** Exactly three distinct bits of the word flip.

A. I and IV  
B. III and IV  
C. I and II  
D. I and III  

### Q50. [1 Mark] [MSQ]

Select every option that is **not a valid answer** to the question below. Judge the options against the question exactly as written.

**Question to evaluate**

Arrange the sentences into the most coherent account. No other comparison, restoration or verification is implied.

P. The comparison showed that the missing entries were present in the backup.
Q. The librarian noticed gaps in the catalogue and compared it with a backup.
R. A final check then confirmed that the restored catalogue contained every entry.
S. Using that evidence, she restored the missing entries from the backup.

A. Q, P, S, R  
B. P, Q, S, R  
C. Q, S, P, R  
D. Q, P, R, S  

---

## ANSWER KEY — SET 017

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MSQ | 1 | B, C, D |
| 2 | MSQ | 2 | B, C, D |
| 3 | MSQ | 1 | B, C, D |
| 4 | MSQ | 2 | A, C, D |
| 5 | MCQ | 1 | A |
| 6 | MCQ | 2 | D |
| 7 | MCQ | 1 | C |
| 8 | MSQ | 2 | A, C, D |
| 9 | MCQ | 1 | A |
| 10 | MSQ | 2 | A, C, D |
| 11 | MSQ | 2 | A, C, D |
| 12 | MSQ | 1 | A, C, D |
| 13 | MSQ | 2 | A, C, D |
| 14 | MCQ | 2 | B |
| 15 | MSQ | 1 | A, C, D |
| 16 | MCQ | 1 | D |
| 17 | MSQ | 1 | B, C, D |
| 18 | MCQ | 2 | B |
| 19 | MCQ | 2 | C |
| 20 | MCQ | 1 | C |
| 21 | MCQ | 2 | A |
| 22 | MSQ | 2 | B, C, D |
| 23 | MSQ | 1 | B, C, D |
| 24 | MSQ | 1 | B, C, D |
| 25 | MSQ | 2 | B, C, D |
| 26 | MSQ | 2 | C, D |
| 27 | MSQ | 1 | A, B, C |
| 28 | MSQ | 1 | A, B, D |
| 29 | MSQ | 2 | A, C, D |
| 30 | MCQ | 2 | B |
| 31 | MCQ | 1 | B |
| 32 | MCQ | 1 | D |
| 33 | MCQ | 2 | C |
| 34 | MCQ | 2 | C |
| 35 | MCQ | 2 | C |
| 36 | MCQ | 1 | D |
| 37 | MCQ | 1 | C |
| 38 | MCQ | 1 | B |
| 39 | MCQ | 1 | C |
| 40 | MSQ | 1 | A, C, D |
| 41 | MCQ | 2 | A |
| 42 | MCQ | 2 | B |
| 43 | MSQ | 1 | A, B, D |
| 44 | MCQ | 1 | B |
| 45 | MSQ | 2 | A, B, C |
| 46 | MCQ | 2 | D |
| 47 | MCQ | 2 | C |
| 48 | MCQ | 2 | D |
| 49 | MCQ | 1 | A |
| 50 | MSQ | 1 | B, C, D |
