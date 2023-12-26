"""
Slicing


Slicig relies on indexing -> only works with sequence types

Mutable Sequence Types              Immutable Sequence Types

extract data                         extract data
assign data

Example
l = [1,2,3,4,5]
l[0:2] -> [1, 2]
l[0:2] = ('a', 'b', 'c')
l -> ['a', 'b', 'c', 3, 4, 5]

The Slice Type

Although we usually slice sequences using the more conventional notation:
my_list[i:j]

slice definitions are actually objects -> of type slice

s = slice(0, 2)   type(s) -> slice   s.start = 0 s.end = 2
l = [1,2,3,4,5]  l[s] = [1,2]

This can be useful because we can name slices and use symbols instead of a literal subsequently

Slice Start and Stop Bounds

[i:j]   start at i (including i) stop at j ( excluding j)
        all integers k where i <= k < j

Step Value

Slices also support a third argument - the step value
[i:j:k]   slice(i,j,k) default k = 1

Any slice essentially defines a sequence of indices that is used to select elements
for another sequence.
In fact, any indices defined by a slice can also be defined using a range

The difference is that slices are defined independently of sequence being sliced
The equivalent range is only calculated once the length of the sequence being sliced is known

Example:
    [0:100]   l sequence of length 10 -> range(0,10)


Transformation

                [i:j] or [i:j:k] where k > 0          |    [i:j:k] where k < 0

i > len(seq)     len(seq)                                   len(seq) - 1
j > len(seq)     len(seq)                                   len(seq) - 1

i < 0            max(0, len(seq) + i)                        max(-1, len(seq) + i)
j < 0            max(0, len(seq) + j)                        max(-1, len(seq) + j)

i omitted/None      0                                        len(seq) - 1
j omitted/None      len(seq)                                 -1

Examples

    l = ['a', 'b', 'c', 'd', 'e', 'f']  length = 6

[-10:10:1]  -10 -> 0
            10 -> 6 -> range(0,6)

[10:-10:-1]   10 -> 5
              -10 -> max(-1, 6-10) -> max(-1, -4) -> -1
              -> range(5, -1, -1)

We can of course easly define empty slices!

[3:-1:-1]  3 -> 3
           -1 -> max(-1, 6-1) -> 5
           -> range(3, 5, -1) - empty slice we cannot go from index 3 to index 5 backwards

seq = 'python'
seq[::-1] -> 'nohtyp'

The slice object has a method, indices, that returns the equivlent range start/stop/step
for any slice given the length of the sequence being sliced:

slice(start, stop, step).indices(length) - > (start, stop, step)

the value in this tuple can be used to generate a list of indices using the range function


slice(10, -5, -1) -> with a sequence of length 6

slice(10, -5, -1).indices(6) -> (5, 1, -1)

list(range(*slice(10,-5,-1).indices(6))) -> [5,4,3,2]
"""

s = slice(0, 2)
print(type(s))
print(s.start)
print(s.stop)

l = [1,2,3,4,5]
print(l[0:2])
print(l[s])

data = []
for row in data:
    first_name = row[0:51]
    last_name = row[51:101]
    ssn = row[101:111]

range_first_name = slice(0, 51)
range_last_name = slice(51, 101)
range_ssn = slice(101, 111)

data = []
for row in data:
    first_name = row[range_first_name]
    last_name = row[range_last_name]
    ssn = row[range_ssn]

l = 'python'
print(l[0:1])
print(l[1:1])
print(l[0:600])
print(l[0:6:2])
print(l[:4])
print(l[3:])
print(l[3:0:-1]) # hty
print(l[3::-1]) # htyp
print(l[3:-1:-1]) # empty because -1 is actually n
print(l[3:-100:-1]) # htyp

s = slice(1,5)
print(s.start, s.stop)
print(s.indices(10)) # (1,5,1)
print(s.indices((4))) # (1,4,1)

print(list(range(*slice(0, 100, 2).indices(10)))) # gives the actual elements [0, 2, 4, 6, 8]



