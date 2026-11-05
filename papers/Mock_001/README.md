# GATE CS 2027 — Full-Length Mock Test 001

**Paper Code:** CS  
**Duration:** 180 Minutes  
**Maximum Marks:** 100  
**Total Questions:** 65  
**Difficulty:** Medium to Hard

## General Instructions

- Attempt all 65 questions within 180 minutes.
- MCQ: select exactly one of four options. Incorrect 1-mark MCQ: −1/3; incorrect 2-mark MCQ: −2/3.
- MSQ: select every correct option. There is no partial credit and no negative marking.
- NAT: enter a numerical answer, using the stated precision. There is no negative marking.
- Unattempted questions receive zero marks.

---

## Section A — General Aptitude

### Q1. [1 Mark] [MCQ]

Choose the pair that completes the sentence grammatically.

Each of the instruments that ___ damaged during transport ___ now been recalibrated.

A. were; has  
B. was; have  
C. were; have  
D. was; has  

### Q2. [1 Mark] [NAT]

A service receives orders of two kinds, X and Y. Initially, 40% of the orders are X. Exactly 25% of X orders and 10% of Y orders are cancelled; all remaining orders are completed. What percentage of completed orders are X? Round to two decimal places.

**Answer format:** Numeric value; 2 decimal places.

### Q3. [1 Mark] [NAT]

Exactly two of A, B, C and D must be on duty. If A is on duty, B must be on duty. In addition, C is on duty if and only if D is not on duty. How many different pairs can be on duty?

**Answer format:** Numeric value; integer.

### Q4. [1 Mark] [MCQ]

A triangular tile has labelled vertices P=(1,1), Q=(3,1), R=(1,2) in a Cartesian plane. First reflect the tile in the x-axis. Then rotate the result clockwise by 90 degrees about the origin. Which ordered triple gives the final positions of P, Q and R?

A. ((-1,-1),(-1,-3),(-2,-1))  
B. ((1,1),(1,3),(2,1))  
C. ((1,-1),(1,-3),(2,-1))  
D. ((-1,1),(-1,3),(-2,1))  

### Q5. [1 Mark] [MCQ]

Read the passage.

“A library extended its evening opening hours in June. Evening visits increased, while total daily visits remained unchanged. The library did not record whether evening visitors had previously visited at other times.”

Which conclusion is best supported by the passage?

A. The extended hours attracted no new visitors.  
B. Some visits may have shifted from earlier hours to the evening.  
C. Every evening visitor formerly visited in the morning.  
D. The extension reduced the total number of visits.  

### Q6. [2 Marks] [MCQ]

Seven distinct people A, B, C, D, E, F and G sit around a circular table. A and B must sit next to each other. Neither C and D nor E and F may sit next to each other. Rotations of an arrangement are identical; reflections are different. How many arrangements are possible?

A. 96  
B. 120  
C. 144  
D. 240  

### Q7. [2 Marks] [MCQ]

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

A square sheet occupies 0 <= x <= 8 and 0 <= y <= 8. Fold its left half onto its right half along x=4. Next fold its bottom half onto its top half along y=4. Punch small point-like holes through all layers at (5,6) and (6,5) in the folded sheet. After fully unfolding, how many distinct holes lie on the line y=x+1? Ignore hole diameter and sheet thickness.

**Answer format:** Numeric value; integer.

### Q9. [2 Marks] [MCQ]

Arrange the following sentences into a coherent chronological account. Treat the explicitly stated causal and time relations as binding.

P. Based on the successful repeat trial, the final report recommended a full rollout.
Q. Both gauges were calibrated before the first trial began.
R. During that first trial, the two readings diverged as temperature rose.
S. Replacing one gauge eliminated this divergence in a repeat trial.
T. After receiving the final report, the committee accepted its recommendation.

Which sequence is correct?

A. Q-R-P-S-T  
B. R-Q-S-P-T  
C. Q-R-S-P-T  
D. Q-S-R-T-P  

### Q10. [2 Marks] [MCQ]

A fair coin selects one of two bags. Bag I contains 4 red and 2 blue balls; Bag II contains 2 red and 3 blue balls. Two balls are then drawn uniformly without replacement from the selected bag. Given that the two balls have the same colour, what is the probability that both are red?

A. 1/2  
B. 15/26  
C. 7/13  
D. 3/5  

---

## Section B — Computer Science and Engineering Mathematics

### Q11. [1 Mark] [MCQ]

For Boolean variables x, y and z, let F=(x OR y) AND ((NOT x) OR z). Which expression is equivalent to F for every input?

A. (x AND z) OR ((NOT x) AND y)  
B. (x AND y) OR ((NOT x) AND z)  
C. y OR z  
D. x XOR y XOR z  

### Q12. [1 Mark] [NAT]

A process opens a regular file for reading, obtaining descriptor p with file offset 0, and then executes q=dup(p). It performs the following successful operations in order: read 2 bytes through p; read 3 bytes through q; seek through p to absolute byte offset 1; read 1 byte through q. The file is long enough for every read. What is the resulting shared file offset? Offsets are zero-based.

**Answer format:** Numeric value; integer.

### Q13. [1 Mark] [MCQ]

A four-variable Boolean function F(A,B,C,D), with A as the most significant bit of the minterm index, is 1 at minterms 1,3,9,11. Minterms 0,2,8,10 are don't-cares, and all remaining minterms are 0. Which is a minimum-literal sum-of-products implementation?

A. NOT B  
B. NOT D  
C. A OR C  
D. (NOT B) AND D  

### Q14. [1 Mark] [MCQ]

Let R be a binary relation on a nonempty domain. Which formula is the logical negation of

`forall x exists y [R(x,y) AND forall z (R(x,z) -> z=y)]`?

All variables in the options are bound as displayed.

A. exists x forall y [NOT R(x,y) OR exists z (R(x,z) AND z!=y)]  
B. exists x exists y [NOT R(x,y) OR exists z (R(x,z) AND z!=y)]  
C. forall x forall y [NOT R(x,y) AND exists z (R(x,z) AND z!=y)]  
D. exists x forall y [NOT R(x,y) OR forall z (R(x,z) AND z!=y)]  

### Q15. [1 Mark] [NAT]

A byte-addressed machine executes a 4-byte load instruction beginning at address 100. Its indirect PC-relative mode first sign-extends an 8-bit displacement, multiplies that signed displacement by 4, and adds it to the address immediately after the instruction. The 32-bit word at this intermediate address is the effective address of the operand. The displacement bits are 11111010. Memory words M[80]=120 and M[120]=7 are given. What is the effective address of the operand? All addresses are decimal; the machine uses two's-complement displacements.

**Answer format:** Numeric value; integer.

### Q16. [1 Mark] [MCQ]

A 4-bit adder-subtractor computes A+(B XOR ssss)+s and keeps the low four result bits. Its carry-out is C and its two's-complement signed overflow flag is V. For A=0111, B=1010 and s=1, which triple (result,C,V) is correct?

A. (1101,1,0)  
B. (1101,0,0)  
C. (0011,1,1)  
D. (1101,0,1)  

### Q17. [1 Mark] [NAT]

In an ER model, Department is a strong entity with key dept_id. Project is weak and identified by its owning Department and partial key project_code. Task is weak and identified by its owning Project and partial key task_no. Project codes may repeat across departments; task numbers may repeat across projects. No surrogate keys or additional uniqueness constraints are introduced. How many attributes are needed in the minimal primary key of the mapped Task relation?

**Answer format:** Numeric value; integer.

### Q18. [1 Mark] [MCQ]

A lexer recognizes identifiers by `[a-z][a-z0-9]*`, the keyword `if`, and operators `==`, `=`, `++`, `+`. It uses maximal munch; an identifier lexeme exactly equal to `if` is classified as a keyword. Whitespace is ignored. What token-lexeme sequence is produced for `ifx==if+++x`?

A. if, x, ==, if, ++, +, x  
B. ifx, ==, if, ++, +, x  
C. ifx, =, =, if, +, ++, x  
D. ifx, ==, if, +++, x  

### Q19. [1 Mark] [MSQ]

An IPv4 packet carrying a TCP segment crosses one router between two Ethernet LANs. The router performs ordinary forwarding, with no NAT, fragmentation or tunnelling. Its incoming TTL is greater than 1. Which statements are correct about the outgoing packet/frame?

A. The destination IPv4 address is unchanged.  
B. The destination Ethernet address must be unchanged.  
C. The IPv4 TTL is one less than on arrival.  
D. The TCP destination port is replaced by the router's port number.  

### Q20. [1 Mark] [NAT]

Insertion sort is run on keys `[3a, 1, 3b, 2, 3c]`, where 3a, 3b and 3c have equal numeric key 3 and the suffixes only identify records. The usual inner loop shifts a preceding record while its key is strictly greater than the key being inserted. A modified version shifts while it is greater than or equal. Count only shifts of preceding records one position to the right, not final placements of the inserted record. How many additional shifts does the modified version perform?

**Answer format:** Numeric value; integer.

### Q21. [1 Mark] [MSQ]

Use set semantics. R(A,B)={(1,x),(1,y),(2,x)} and S(B)={(x),(y)}. Define

`E = projection_A(R) - projection_A((projection_A(R) x S) - R)`

where x is Cartesian product and - is set difference. Which statements are correct? Each proposed change is applied independently to the original relations.

A. For the original relations, E={(1)}.  
B. If S is empty, E={(1),(2)}.  
C. If (2,y) is added to R, E remains {(1)}.  
D. If (z) is added to S, E is empty.  

### Q22. [1 Mark] [NAT]

For the grammar below, construct the standard LL(1) predictive parsing table using FIRST and FOLLOW sets. A conflicting entry means a single table cell containing two or more distinct productions. Count conflicting cells, not pairs of productions. The start symbol is S and the end marker is $.

```text
S -> A a | b
A -> a A | B
B -> b B | epsilon
```

How many table cells conflict?

**Answer format:** Numeric value; integer.

### Q23. [1 Mark] [NAT]

For real t, consider the homogeneous system M(t)v=0, where

```text
M(t) = [1  1  1]
       [1  t  2]
       [1  2  t]
```

What is the sum of all distinct real values of t for which the system has infinitely many solutions?

**Answer format:** Numeric value; integer.

### Q24. [1 Mark] [MCQ]

For every real x, define f(x)=|x-1|+|x+1| and g(x)=f(f(x)-3). At exactly which points is g not differentiable?

A. x=-1 and x=1 only  
B. x=-2,-1,1,2  
C. x=-2 and x=2 only  
D. At no real point  

### Q25. [1 Mark] [NAT]

X has a Poisson distribution with parameter lambda>0. It is known that P(X=0)=P(X=1). What is E[X^2]?

**Answer format:** Numeric value; integer.

### Q26. [1 Mark] [NAT]

A three-variable Boolean function F(A,B,C), with A as the most significant index bit, is 1 exactly at minterms 0,1,2,5,6,7 and has no don't-cares. How many distinct minimum-product-term sum-of-products covers can be formed using only prime implicants? Ignore the order of terms.

**Answer format:** Numeric value; integer.

### Q27. [1 Mark] [MCQ]

What does this C program print? Assume a conforming C implementation.

```c
#include <stdio.h>
int main(void) {
    int a[2][3] = {{2,4,6},{1,3,5}};
    int (*p)[3] = a;
    int *q = p[1];
    p[0][2] += q[1];
    int *r = p[0] + 1;
    *r++ = q[0];
    q[2] = *r;
    printf("%d\n", a[0][1] + a[1][2]);
    return 0;
}
```

A. 7  
B. 10  
C. 13  
D. The program has undefined behaviour.  

### Q28. [1 Mark] [MSQ]

An open-addressed hash table has seven slots and uses h1(k)=k mod 7 and h2(k)=1+(k mod 5), probing (h1(k)+j*h2(k)) mod 7 for j=0,1,... . Keys 10,17,24 are inserted in that order into an empty table. Key 10 is then deleted and its slot marked with a tombstone. Which statements are correct?

A. Searching for 24 must continue past the tombstone.  
B. Replacing that tombstone with a never-used marker preserves all successful searches.  
C. A subsequent insertion of absent key 31 may reuse the tombstone slot.  
D. The deletion permanently reduces the maximum number of keys the table can hold to six.  

### Q29. [1 Mark] [MCQ]

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

### Q30. [1 Mark] [NAT]

Over the alphabet {a,b}, let L contain exactly the strings that end in a and contain an even number of b symbols. The empty string is not in L. What is the number of states in a smallest complete DFA for L?

**Answer format:** Numeric value; integer.

### Q31. [1 Mark] [NAT]

Two packets of 1000 bits each are ready at time 0 and travel through three store-and-forward links in order. Their rates are 2 Mbit/s, 1 Mbit/s and 2 Mbit/s, respectively; 1 Mbit=10^6 bits. Each link transmits only one packet at a time, buffers are sufficient, and propagation and processing delays are zero. Packets retain their order. Each link begins transmitting as soon as both the packet and that link are available. At what time, in milliseconds, does the last bit of the second packet reach the destination?

**Answer format:** Numeric value; integer.

### Q32. [1 Mark] [MCQ]

Consider the grammar S -> SS | aSb | epsilon. Count finite ordered parse trees, distinguishing different tree shapes even when they yield the same string. How many parse trees yield the string ab?

A. Exactly one  
B. Exactly two  
C. A finite number greater than two  
D. Infinitely many  

### Q33. [1 Mark] [MCQ]

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

### Q34. [1 Mark] [MSQ]

Let L={w#reverse(w) : w is a string over {0,1}}, where # is a separator not in {0,1}. A pushdown recognizer reads input left to right and may reject immediately on a mismatch. Which statements are correct?

A. A deterministic pushdown recognizer can push before # and compare/pop after #.  
B. The recognizer can accept after input exhaustion even if unmatched symbols remain on its stack.  
C. The same push-then-pop equality test recognizes {w#w : w over {0,1}}.  
D. The one-symbol input # belongs to L.  

### Q35. [1 Mark] [NAT]

How many functions f:{1,2,3}->{1,2,3} satisfy f(f(x))=f(x) for every x and have exactly two fixed points? A fixed point is an x for which f(x)=x.

**Answer format:** Numeric value; integer.

### Q36. [2 Marks] [NAT]

For n = 128, consider the following pseudocode, where all bounds are integers. The operation `touch` takes one unit of time. How many times is `touch` executed?
```text
width = 1
while width < n:
    base = 0
    while base < n:
        for offset = 0 to width-1 inclusive:
            touch(base + offset)
        base = base + 2*width
    width = 2*width
```


**Answer format:** Numeric value; integer.

### Q37. [2 Marks] [MCQ]

A stack log uses symbol a for a push and b for a pop. A valid log starts with an empty stack, never pops an empty stack, and ends with an empty stack. Let L contain exactly the valid logs in which neither aaa nor bbb occurs as a substring; the empty log belongs to L. Which statement about L is correct?

A. L is regular because no run has more than two identical operations.  
B. L is not regular, but a deterministic pushdown automaton can recognize it.  
C. L is context-free, but no deterministic pushdown automaton can recognize it.  
D. L is not context-free because the run restriction and the stack restriction must both be checked.  

### Q38. [2 Marks] [NAT]

A syntax-directed translator emits postfix code for fully parenthesized binary expressions. It recursively emits the entire left operand, then the entire right operand, and finally the binary operator. The generated code is evaluated on an initially empty stack: an operand pushes one value, and an operator pops two values and pushes their result. No temporary storage other than this stack is used. What is the maximum stack depth reached when evaluating the translation of `(a+b)*(c+(d*e))`?

**Answer format:** Numeric value; integer.

### Q39. [2 Marks] [MSQ]

A is a real 3x3 matrix with distinct eigenvalues 1, 2 and 4. Let u be a nonzero column vector satisfying Au=2u, and let v be a real column vector satisfying v^T u=-2. Define B=A+u v^T. Which statements hold for every such A,u,v?

A. Zero is an eigenvalue of B.  
B. B is diagonalizable over the real numbers.  
C. A and B necessarily commute.  
D. rank(B)=2.  

### Q40. [2 Marks] [NAT]

For real a, define f_a(x)=x^4-2a*x^2+4x on the whole real line. What is the smallest integer a for which f_a has two distinct strict local minima?

**Answer format:** Numeric value; integer.

### Q41. [2 Marks] [MCQ]

A 5×5 matrix is stored in row-major order in a one-dimensional C array: row r, column c is a[5*r+c], for 0≤r,c<5. Consider this complete program. All arithmetic fits in int.
```c
#include <stdio.h>
static void swap(int *p, int *q) {
    int t = *p; *p = *q; *q = t;
}
int main(void) {
    int a[25];
    for (int i = 0; i < 25; ++i) a[i] = i;
    for (int k = 0; k < 2027; ++k) {
        for (int r = 0; r < 5; ++r)
            for (int c = r + 1; c < 5; ++c)
                swap(&a[5*r+c], &a[5*c+r]);
        for (int r = 0; r < 5; ++r)
            for (int c = 0; c < 2; ++c)
                swap(&a[5*r+c], &a[5*r+4-c]);
    }
    printf("%d %d", a[7], a[17]);
    return 0;
}
```
What is printed?

A. 13 11  
B. 11 13  
C. 7 17  
D. 17 7  

### Q42. [2 Marks] [MCQ]

A four-input Boolean function F(a,b,c,d) equals 1 exactly when at least three inputs are 1. It is implemented using a 4-to-1 multiplexer whose select bits are b (more significant) and c (less significant). Data inputs I0, I1, I2, I3 correspond respectively to bc = 00, 01, 10, 11. Which tuple of data-input functions implements F? Here juxtaposition means AND and + means OR.

A. (0, ad, ad, a+d)  
B. (0, a+d, a+d, ad)  
C. (ad, ad, ad, 1)  
D. (0, 0, 0, a+d)  

### Q43. [2 Marks] [MCQ]

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

### Q44. [2 Marks] [MCQ]

Two positive-edge-triggered D flip-flops store bits (q1,q0). At every active clock edge both are updated simultaneously according to q1(next) = q0 XOR q1 and q0(next) = NOT q1. The initial state is (0,0). What is the state after 2027 active clock edges?

A. (0,0)  
B. (0,1)  
C. (1,1)  
D. (1,0)  

### Q45. [2 Marks] [MCQ]

Three processes P, Q and R use two initially empty pipes X and Y. Initially P owns X's write end and Y's read end; Q owns X's read end and Y's write end; R owns an additional copy of X's write end. No other descriptors for these pipes exist. A read-until-EOF operation returns only after all data has been consumed and every write descriptor for that pipe is closed. Pipe capacities exceed all data written here. All processes are eventually scheduled; there are no errors or signals.

- P writes one byte to X, closes its X writer, then reads Y until EOF, then terminates.
- Q reads X until EOF, then writes one byte to Y, closes its Y writer and terminates.
- R waits for P to terminate, then closes its X writer and terminates.

Which single change, with all other operations unchanged, is sufficient to ensure that all three processes terminate?

A. Increase the capacity of X.  
B. Have P wait for R to terminate immediately before P reads Y.  
C. Move R's close of the X writer to immediately before R waits for P.  
D. Have Q close its Y writer only after P terminates.  

### Q46. [2 Marks] [NAT]

The shared integer x is initially 0. Three threads execute exactly once:
```text
A: rA = x;  x = 2*rA + 1;
B: rB = x;  x = rB + 3;
C: rC = x;  x = rC + 5;
```
Each displayed read and each displayed write is separately atomic. Local registers are private. Execution is sequentially consistent, and a thread's read precedes its write. After all six operations have completed, how many distinct final values of x are possible?

**Answer format:** Numeric value; integer.

### Q47. [2 Marks] [MSQ]

A CRC uses generator g(x) = x³ + x + 1 over GF(2). An error polynomial e(x) is undetected exactly when g(x) divides e(x). The transmitted block is long enough to contain each error pattern mentioned below. Which statements are correct? A burst of length L has nonzero first and last bits separated by L−1 positions.

A. Every single-bit error is detected.  
B. Every burst of length at most 3 is detected.  
C. A two-bit error whose nonzero bits are seven positions apart can be undetected.  
D. Every error affecting an odd number of bits is detected.  

### Q48. [2 Marks] [MCQ]

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

### Q49. [2 Marks] [MSQ]

A language evaluates Boolean operands left to right with short-circuit evaluation. Integer division truncates toward zero. In the expression
```text
(x != 0 AND y/x > 2) OR (z++ > 0)
```
`z++` yields the old value of z and then increments z. Integers are unbounded, and x, y, z refer to distinct locations. Which statements about correct intermediate-code generation are true?

A. The increment of z is executed exactly when x = 0 or (x ≠ 0 and y/x ≤ 2).  
B. When x > 0, replacing y/x > 2 by y > 2*x preserves the expression's result and side effects for all y and z.  
C. The division may always be moved before the test x != 0 because it has no side effect.  
D. When x = 0, the result is whether the old z is positive, and z is incremented exactly once.  

### Q50. [2 Marks] [MSQ]

Consider a context-free pumping-lemma proof attempt for L = {a^n b^n c^n : n ≥ 0}. For an arbitrary pumping length p ≥ 1, choose s = a^p b^p c^p. A legal decomposition is s = uvxyz, with |vxy| ≤ p and |vy| > 0, and pumping produces uv^i xy^i z. Which claims are correct?

A. The substring vxy cannot contain both an a and a c.  
B. For every legal decomposition, pumping with i=0 produces a string outside L.  
C. It is sufficient to exhibit one legal decomposition for which pumping with i=0 produces a string outside L.  
D. A proof may assume, without treating other cases, that v and y each contain only a symbols.  

### Q51. [2 Marks] [MCQ]

A singly linked list initially consists of six distinct nodes with values 1,2,3,4,5,6 in that order, followed by NULL. The following pointer operations are executed. Node fields are modified in place; no nodes are allocated or freed.
```text
p = head
q = NULL
while p != NULL and p.next != NULL:
    r = p.next
    p.next = r.next
    r.next = q
    q = r
    p = p.next
```
Which pair gives the lists reached from (head, q) after termination?

A. (1→3→5, 2→4→6)  
B. (1→3→5, 6→4→2)  
C. (1→5, 6→4→3→2)  
D. (1→2→3, 6→5→4)  

### Q52. [2 Marks] [NAT]

Two signed fixed-point numbers are stored in 8-bit two's-complement form with four fractional bits. Their raw hexadecimal encodings are E7 and 39. Multiply their exact represented values, then round the result to the nearest representable value in the same format (ties to even). The result is in range. What is the unsigned decimal interpretation, from 0 to 255, of the resulting 8-bit encoding?

**Answer format:** Numeric value; integer.

### Q53. [2 Marks] [NAT]

The values 1,2,3,4,5,6 arrive in that order. A single initially empty stack has capacity three. At each step the next unread input may be pushed if space is available, or the top may be popped to an output sequence. Each value must be pushed and popped exactly once. The output is required to begin with 3,2. How many distinct complete output sequences satisfy these conditions?

**Answer format:** Numeric value; integer.

### Q54. [2 Marks] [MCQ]

A microprogrammed control unit uses a fixed-width microinstruction. One field jointly encodes the following bus-transfer commands:

- An idle command, in which no source drives the bus and no destination is loaded.
- A non-idle command chooses exactly one of eight sources and a nonempty subset of five destination registers. Every such source/subset pair is allowed.

There are no other bus-transfer commands. Each allowed command needs a distinct binary code, and unused codes are permitted. The other independently encoded fields select one of six ALU operations (including no-operation), one of 128 next addresses, and one of four sequencing conditions (including unconditional sequencing). Codes cannot be shared across these four fields. What is the minimum microinstruction width?

A. 19 bits  
B. 20 bits  
C. 21 bits  
D. 25 bits  

### Q55. [2 Marks] [MSQ]

A component is faulty with probability 1/4. Each test is positive with probability 4/5 for a faulty component and 1/10 for a sound component. Repeated results are conditionally independent given the component's status. Testing stops at the first negative result or after three tests, whichever occurs first. N is the number of tests performed. Which statements are correct?

A. E[N]=577/400.  
B. P(faulty | N=3)=512/515.  
C. Given that exactly two positive results were observed before a negative result, the probability of a faulty component is 128/155.  
D. Given that the first result was positive and the stopping result was negative, the probability of a faulty component is 32/65.  

### Q56. [2 Marks] [NAT]

For a Turing machine M over binary input strings, consider these four sets of valid machine encodings:

1. M accepts the string 01.
2. Every string accepted by M is equal to 01.
3. M halts on every binary input string.
4. There exists a binary input string on which M eventually enters a designated state q (the state q is part of the machine description and is distinct from its initial state).

A set is recognizable if some Turing machine accepts exactly its members and may fail to halt on nonmembers. How many of the four sets are recognizable?

**Answer format:** Numeric value; integer.

### Q57. [2 Marks] [MSQ]

A byte-addressed processor has address lines A15 through A0. A memory board uses four 4K×8 RAM chips to provide one contiguous 16 KiB region starting at address 0x8000. Each selected chip supplies one byte. Chip address pins use A11 through A0; a decoder chooses one chip. Assume the decoder is enabled exactly for addresses in the intended region. Which statements are correct?

A. A13 and A12 can select the chip, while A15=1 and A14=0 enable the board.  
B. Address 0xB123 selects chip index 3 (indices 0–3 in increasing address order) at local offset 0x123.  
C. If the board enable checks only A15=1 and ignores A14, each physical byte is mapped at two processor addresses.  
D. Connecting chip address pins to A12 through A1, while otherwise retaining the stated decoder, still gives one-to-one addressing of the 16 KiB region.  

### Q58. [2 Marks] [MCQ]

Table T(k,v) contains exactly these rows; NULL denotes the SQL null value, and duplicates are retained:
```text
(1,10), (1,NULL), (1,10), (2,NULL), (2,NULL), (3,5)
```
What rows, in any order, does the following standard SQL query return?
```sql
SELECT k, COUNT(*) AS n, COUNT(v) AS c
FROM T
GROUP BY k
HAVING COUNT(v) < COUNT(*) AND SUM(v) >= 10;
```

A. (1,3,2) only  
B. (1,3,2) and (2,2,0)  
C. (1,2,1) only  
D. No rows  

### Q59. [2 Marks] [MCQ]

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

### Q60. [2 Marks] [MCQ]

A processor first checks L1. Every L1 access takes 1 ns. On an L1 miss it next checks L2, taking an additional 6 ns; on an L2 miss it additionally accesses memory, taking 60 ns. There is no overlap. Initially the L1 miss probability is 0.10 and the L2 local miss probability conditional on an L1 miss is 0.20. An L1 redesign reduces its miss probability to 0.05 but changes its access time to t ns. L2 timing and its conditional miss probability remain unchanged. For strictly lower average access time, which condition on t is necessary and sufficient?

A. t < 1.9 ns  
B. t < 2.8 ns  
C. t < 1.3 ns  
D. t < 3.6 ns  

### Q61. [2 Marks] [MCQ]

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

### Q62. [2 Marks] [MSQ]

For a 0/1 knapsack with nonnegative integer capacity W and items of positive integer weights wi and positive values vi, let D[j] initially be zero for every 0 ≤ j ≤ W. Each item may be used at most once. Consider the update `D[j] = max(D[j], D[j-wi] + vi)` for j ≥ wi. Which statements are correct?

A. Processing each item once and scanning j downward from W to wi computes the maximum value for capacity W.  
B. Processing each item once and scanning j upward from wi to W always computes the same 0/1 optimum.  
C. With one item of weight 2 and value 3 and capacity 4, an upward scan produces D[4]=6.  
D. For a downward scan, immediately before updating D[j] for an item, D[j-wi] still excludes that item.  

### Q63. [2 Marks] [MSQ]

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

### Q64. [2 Marks] [MSQ]

Let L={empty set, {a}, {b}, {c}, {a,c}, {b,c}, {a,b,c}}, ordered by inclusion. Notice that {a,b} is absent. Meets and joins are taken within L. A complement of x is a y with meet(x,y)=empty set and join(x,y)={a,b,c}. An order automorphism is a bijection L->L preserving the order in both directions. Which statements are correct?

A. L is a distributive lattice.  
B. Exactly six elements of L have at least one complement.  
C. L has exactly two order automorphisms.  
D. The join of {a} and {b} is {a,b,c}.  

### Q65. [2 Marks] [NAT]

An idealized half-duplex CSMA/CD link connects two stations 2400 m apart. Propagation speed is 2×10^8 m/s and the bit rate is 100 Mb/s, where 1 Mb/s = 10^6 bits/s. Detection circuitry adds 2 microseconds after the collision disturbance reaches a transmitting station. Ignore all other delays and framing overhead. A sender must still be transmitting when a worst-case collision is detected. Under the model, what is the minimum integer frame length in bytes? Treat the worst-case round-trip propagation bound as inclusive.

**Answer format:** Numeric value; integer.

---

## ANSWER KEY — MOCK TEST 001

| Question | Type | Marks | Correct Answer |
|---|---|---|---|
| 1 | MCQ | 1 | A |
| 2 | NAT | 1 | 35.71 (exact) |
| 3 | NAT | 1 | 2 (exact) |
| 4 | MCQ | 1 | A |
| 5 | MCQ | 1 | B |
| 6 | MCQ | 2 | A |
| 7 | MCQ | 2 | A |
| 8 | NAT | 2 | 2 (exact) |
| 9 | MCQ | 2 | C |
| 10 | MCQ | 2 | B |
| 11 | MCQ | 1 | A |
| 12 | NAT | 1 | 2 (exact) |
| 13 | MCQ | 1 | A |
| 14 | MCQ | 1 | A |
| 15 | NAT | 1 | 120 (exact) |
| 16 | MCQ | 1 | D |
| 17 | NAT | 1 | 3 (exact) |
| 18 | MCQ | 1 | B |
| 19 | MSQ | 1 | A, C |
| 20 | NAT | 1 | 3 (exact) |
| 21 | MSQ | 1 | A, B, D |
| 22 | NAT | 1 | 2 (exact) |
| 23 | NAT | 1 | 2 (exact) |
| 24 | MCQ | 1 | C |
| 25 | NAT | 1 | 2 (exact) |
| 26 | NAT | 1 | 2 (exact) |
| 27 | MCQ | 1 | B |
| 28 | MSQ | 1 | A, C |
| 29 | MCQ | 1 | A |
| 30 | NAT | 1 | 3 (exact) |
| 31 | NAT | 1 | 3 (exact) |
| 32 | MCQ | 1 | D |
| 33 | MCQ | 1 | A |
| 34 | MSQ | 1 | A, D |
| 35 | NAT | 1 | 6 (exact) |
| 36 | NAT | 2 | 448 (exact) |
| 37 | MCQ | 2 | B |
| 38 | NAT | 2 | 4 (exact) |
| 39 | MSQ | 2 | A, B, D |
| 40 | NAT | 2 | 2 (exact) |
| 41 | MCQ | 2 | A |
| 42 | MCQ | 2 | A |
| 43 | MCQ | 2 | A |
| 44 | MCQ | 2 | C |
| 45 | MCQ | 2 | C |
| 46 | NAT | 2 | 12 (exact) |
| 47 | MSQ | 2 | A, B, C |
| 48 | MCQ | 2 | B |
| 49 | MSQ | 2 | A, D |
| 50 | MSQ | 2 | A, B |
| 51 | MCQ | 2 | B |
| 52 | NAT | 2 | 167 (exact) |
| 53 | NAT | 2 | 13 (exact) |
| 54 | MCQ | 2 | B |
| 55 | MSQ | 2 | A, C, D |
| 56 | NAT | 2 | 2 (exact) |
| 57 | MSQ | 2 | A, B, C |
| 58 | MCQ | 2 | A |
| 59 | MCQ | 2 | C |
| 60 | MCQ | 2 | A |
| 61 | MCQ | 2 | C |
| 62 | MSQ | 2 | A, C, D |
| 63 | MSQ | 2 | A, B, D |
| 64 | MSQ | 2 | B, C, D |
| 65 | NAT | 2 | 325 (exact) |
