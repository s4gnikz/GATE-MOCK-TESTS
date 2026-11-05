### Q38. [2 Marks] [MSQ]

A simple undirected graph has vertices A,B,C,D,E,F. Each edge of triangle ABC and each edge of triangle DEF has weight 1. Edges AD, BE and CF have weight 2, and edge AE has weight 3. There are no other edges. Two spanning trees are distinct when their edge sets differ. Which statements are correct?

A. The minimum spanning-tree weight is 6.  
B. There are exactly 27 minimum spanning trees.  
C. There are exactly 45 spanning trees of weight 7.  
D. Every spanning tree of weight 7 uses exactly two weight-2 edges.

### Q43. [2 Marks] [MCQ]

A contiguous memory region occupies addresses [0,240), where [u,v) has size v−u. Initially its free regions are [0,60), [100,180), and [200,240). Process X occupies [60,100), and process Y occupies [180,200). Compare first-fit and best-fit, each starting from this initial state.

First allocate A of size 50, then B of size 35. Next free X and A, leaving B and Y allocated. Every allocation takes space from the lowest-address end of its selected hole. First-fit searches from address 0 on each request; best-fit selects the smallest sufficient hole. Adjacent free regions are immediately coalesced, with no metadata overhead or compaction.

What are the largest single requests that can now be satisfied under (first-fit, best-fit), respectively?

A. (100,180)  
B. (100,100)  
C. (180,180)  
D. (180,100)

### Q45. [2 Marks] [MCQ]

An 8-bit ALU subtracts B from A using A+(NOT B)+1. The result is reduced modulo 256. N is its most significant bit, V indicates signed two's-complement overflow, and C is carry-out, with C=1 meaning no unsigned borrow. Both operands range independently over all 256 bit patterns.

How many ordered pairs (A,B) produce N=0, V=1 and C=1 simultaneously?

A. 8192  
B. 8128  
C. 8256  
D. 16384

### Q48. [2 Marks] [MSQ]

Consider the following complete read/write schedule; commits occur afterwards and are omitted. Subscripts identify transactions. Repeated writes by one transaction are distinct operations. The read returns the value written by the latest preceding write.

```text
w1(x); w2(x); w3(y); w2(y); r4(x); w4(y); w1(x)
```

A view-equivalent serial schedule must preserve the transaction from which every read obtains its value, any reads of initial values, and the final writer of each item. A serial order includes all four transactions, preserving each transaction's internal operation order. Which statements are correct?

A. The displayed schedule is conflict-serializable.  
B. The displayed schedule is view-serializable.  
C. Exactly two transaction orders give view-equivalent serial schedules.  
D. If only the first operation w1(x) is deleted, the resulting schedule has exactly one conflict-equivalent serial transaction order.

### Q51. [2 Marks] [MSQ]

Over alphabet {a,b,c}, define

```text
L = { a^i b^j c^k : i,j,k >= 0 and (i=j or j=k) }
R = { a^i b^j c^k : i,j,k >= 0 and j<=2 }
S = { a^n b^m c^n : n,m >= 0 }.
```

All exponents are integers, and L minus R denotes set difference. Which statements are correct?

A. L intersect R is regular.  
B. L minus R is regular.  
C. L minus R is context-free.  
D. L intersect S is context-free.

### Q53. [2 Marks] [MCQ]

A directed multigraph has vertices 1,2,3 and the following adjacency matrix, where entry Mij is the number of distinct edges from i to j:

```text
M = [0 2 1]
    [1 0 1]
    [0 1 1].
```

Count the closed walks of length four that never traverse the same directed edge twice. Vertices may repeat, and opposite-direction edges are distinct. The two parallel edges from 1 to 2 are distinguishable. Count ordered edge sequences together with their starting vertex; cyclic rotations are counted separately whenever the resulting ordered sequences differ.

How many such walks exist?

A. 7  
B. 12  
C. 16  
D. 24

### Q61. [2 Marks] [NAT]

A TCP sender's next new data byte has sequence number 5001. Its latest cumulative acknowledgement is ACK=1001, meaning that byte 1001 is next expected. The advertised receive window is 6000 bytes and the congestion window is 8000 bytes.

The sender transmits the maximum permitted amount of new data. It then receives ACK=3001 with an advertised receive window of 3500 bytes and an updated congestion window of 10000 bytes, and again transmits the maximum permitted new data. Finally, it receives ACK=5501 with an advertised receive window of 5000 bytes and an updated congestion window of 4500 bytes, and again sends as much new data as permitted.

There are no other transmissions, acknowledgements or window changes. Each advertised receive window starts at its ACK number. Ignore sequence-number wraparound and segment-size restrictions. Data already sent may lie beyond the right edge of a newly reduced receive window; it remains outstanding. How many new data bytes are transmitted in total across these three sending opportunities?

**Answer format:** Numeric value; integer.
