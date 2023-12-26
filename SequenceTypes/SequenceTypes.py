"""
What is a sequence?

In Math: S = x1, x2, x3, ...

Python lists have a concept of positional order but sets do not
- A list is a sequence type
- A set is not

In Python we start index numbers at 0

Built-in Sequence Types

mutable: lists, bytearrays
immutable: strings, tuples (in reality a tuple is more than just a sequence type), range (more limited than lists, strings and tuples) and bytes

Additional Standard Types:
        - collections package: namedtuple, deque
        - array module: array

Homogeneous vs Heterogeneous Sequences

Strings are homogeneous sequences
            - each element is of the same type (a character) 'python'
Lists are heterogeneous sequences
            - each element may be a different type [1, 10.5, 'python']

Homogeneous sequence types are usually more efficient (storage wise at least)
ex. prefer using a string of characters, rather than a list or tuple of characters

Iterable Type vs Sequence Type

What does it mean for an object to be iterable?
    It is a container type of object and we can list out the elements in that object one by one
So any sequence type is iterable
    Ex. l = [1, 2, 3] for e in l - works l[0] - works
But an iterable is not necessarly a sequence type -> iterables are more general
    Ex. s = {1, 2, 3} for e in s - works s[0] - not working

Standard Sequence Methods:
    - Built-in sequences types, both mutable and immutable support following methods:
        x in s    s1 + s2 - concatenation
        x not in s   s * n (or n * s) - n an integer (repetition)
    len(s)
    min(s), max(s) - if an ordering between elements of s is defined
    s.index(x) - index of first occurrance of x in s
    s.index(x, i) - index of first occurrance of x in s at or after index i
    s.index(x, i, j) - index of first occurrance of x at or after index i and before index j
    s[i]
    s[i:j] - slice from index i to but not including j
    s[i:j:k] - slice from index i to but not including j, in steps of k
Note that slices will return in the same container type
    range objects - more restrictive: no concatenation/repetition
                  - min, max, in, not in not as efficient
    Immutable sequence types may support hashing - hash(s) but not if they contain mutable types

Beware of concatenation

x = [[0,0]] a = x + x  a = [[0,0], [0,0] ]
a[0] is x[0] - True
a[1] is x[0] - True
a[0][0] = 100 =>   a = [[100,0], [100,0]]

Same happens here, but because strings are immutable it's quite safe
a = ['python'] * 2 => a = ['python', 'python' ]

"""

l = [1, 2, 3]
t = (1, 2, 3)
s = 'python'

# Sequence types are indexable
print(l[0], l[1])
print(s[2])

# Sequence types are iterables

for c in s:
    print(c)

s = {10, 20, 'x', 30} # s is iterable but it is not a sequence type and cannot refference an index number
for e in s:
    print(e)

l = [1, 2, 3]
t = (1, 2, 3)
l[0] = 100 # mutable
#t[0] = 100 - not working immutable

t = ([1,2], 3, 4)
t[0][0] = 100 # working tuple not mutated but the object in the first poz was mutated

print('a' in ['a','b',100]) # True

print(100 in range(200)) # ranges are sequence types

print(len('python'), len([1,2,3]), len({10,20,30}), len({'a':1,'b':2}))

l = [100, 90, 20]

print(l)
max(l)

l = [2+2j, 10+10j, 100+100j]
#print(min(l)) # not working cannot compair pairwise for complex

# if l is heterogenious min max don't work
l = ['a', 10, 100]
#print(min(l)) - not working

from decimal import Decimal

l = [10, 10.5, Decimal('20.3')]
print(min(l)) # works

print([1,2,3] + [3,4,2])
#print([1,2,3] + (1,2,3)) - not working
#print('abc' + ['d', 'e', 'f']) - not working

print('***'.join(['1', '2', '3']))
print(''.join(list('abc') + ['d', 'e', 'f']))

print([1, 2, 3] * 3)

s = "gnu's not unix"

print(list(enumerate(s))) # returns an object - iterables that contains a tuple with index and char

print(s.index('n')) # first occurence
print(s.index('n', 2)) # first occurence after 2
print(s.index('n', 1))
print(s.index('n', 7))
#print(s.index('z')) # exception
#print(s.index('n', 12))# exception

s = 'python'
l = [1,2,3,4,5,6,7,8,9,10]
print(s[1:4]) # not including index 4
print(s[4:1000]) # returns from index 4 to final
print(s[:]) # get all sequence
l = [1, 2, 3]
l2 = l[:]
print(l is l2) # false
print(s[::-1]) # reverse
