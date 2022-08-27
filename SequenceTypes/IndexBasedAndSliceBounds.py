# Index Based And Slice Bounds


# Why does sequence indexing start at 0, and not 1?
# Why does a sequence slice s[i:j] include s[i], but exclude s[j]
"""
Consider the following sequence of integers: 1, 2, 3, ..., 15
How can we describe this range of numbers without using an ellipsis (...) ?
a) 1 <= n <= 15
b) 0 < n <= 15
c) 1 <= n < 16
d) 0 < n < 16

b and d can become odd at times
Suppose we want to describe unsigned integers 0, 1, 2, ..., 10
a and c remains valid
a) 0 <= n <= 10
c) 0 <= n < 11
Now considere this sequence 2, 3, ..., 16
a) 2 <= n <= 16
c) 2 <= n < 16
How many elements are in this sequence? 15
Calculating number of elements from bound in a and c
a) =  # upper - lower + 1
c) =  # upper - lower
c - seems simpler for that calculation

Why Start indexing at 0 instead of 1?
Consider the following sequence:
                    2, 3, 4, ..., 16 - length 15
index n (1 based)   1  2  3       15     1 <= n < 16 - upper bound = length + 1
index n (0 based)   0  1  2       14     1 <= n < 15 - upper bound = length

For any sequence s, the index range is given by:
    0 based: 0 <= n < len(s)
    1 based: 1 <= n < len(s) + 1
So, 0 based appears simpler

Consider this sequence:
        a, b, c, d, ... z
1 based:1  2  3  4      26
0 based:0  1  2  3      25
How many elements come before d? 3 elements
1 based: index(d) -> 4    4-1 elements
0 based: index(d) -> 3    3  elements

Choosing 0 based indexing for sequence

describing ranges of indices using range(l, u) -> l <= n < u

we have the following results:
        the indices of any sequence s are given by: range(0, len(s)) [ 0 <= n < len(s) ]
                first index:  0   last index: len(s) - 1
                the length of a range(l, u) us given by: l - u

    s = [a, b, c, ..., z] len(s) -> 26
    indices -> range(0, 26)
    n elements precede s[n]

Slices

Because of the convention of starting indexing at 0 and defining ranges using [lower, upper)
we can think of slicing in these terms:
Each item in a sequence is like a box, with the indices between the boxes:

"""


