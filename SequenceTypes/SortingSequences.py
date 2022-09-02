"""
Sorting Sequences
"""

t = 10, 3, 5, 8, 9, 6, 1

print(sorted(t)) # returns a sorted list

t = 1+1j, 10, 20

#print(sorted(t)) # Exception

s = {10, 3, 5, 8, 9, 6, 1}

print(sorted(s)) # returns a sorted list

d = {3:100, 2:200, 1:10}

print(sorted(d)) # returns a list with the sorted keys of the dict

d = {'a': 100, 'b': 50, 'c': 10}

print(sorted(d, key=lambda k: d[k])) # returns a list with keys sorted by the value

t = 'this', 'parrot', 'is', 'a', 'late', 'bird'

print(sorted(t)) # sort this in alphabetical order

def sort_key(s):
    return len(s)

print(sorted(t, key=sort_key)) # sort based on the length of the string
print(sorted(t, key=lambda s: len(s))) # if the strings have same length then it is sorted based on preserved order ( stable sort)

t = 'aaaa', 'bbbb', 'cccc', 'dddd', 'e'*4

print(sorted(t, key=lambda s: len(s))) # ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee']

t = 'aaaa', 'bbbb','e'*4, 'dddd', 'cccc'

print(sorted(t, key=lambda s: len(s))) # ['aaaa', 'bbbb', 'eeee', 'dddd', 'cccc']

t = 1+1j, 2+2j, 3+3j

print(sorted(t, key = abs)) # sort based on the absolute value

print(sorted(t, key = lambda c: c.imag))

print(sorted(t, key = lambda c: c.imag, reverse=True)) # in reverse order


t = 'aaaaa', 'bbvbb','e'*4, 'dddd', 'cccc'

print(sorted(t, key=lambda s: len(s), reverse=True))

l = 'this bird is a late parrot'.split(' ')
print(l)
print(sorted(l, key=lambda s: len(s))) # this does not mutate l
print(l)
l.sort(key=lambda s: len(s)) # this is an implace sort ( now l was mutated)
print(l) # sort is more efficient than sorted

from timeit import timeit
import random

# random.seed(0)
# n = 10_000_000
# l = [random.randint(0, 100) for n in range(n)]
#
# print(l[0:10])
#
# print(timeit(stmt='sorted(l)', globals=globals(), number= 1)) # 0.76
# print(timeit(stmt='l.sort()', globals= globals(), number=1)) # 0.72


class MyClass:

    def __init__(self, name, val):
        self.name = name
        self.val = val

    def __repr__(self):
        return f'MyClass({self.name}, {self.val})'

    def __lt__(self, other):
        print('calling __lt__')
        return self.val < other.val

c1 = MyClass('c1', 20)
c2 = MyClass('c2', 10)
c3 = MyClass('c3', 20)
c4 = MyClass('c4', 10)

print(sorted([c1, c2, c3, c4])) # sorted by the value ( if it didn't had the __lt__ or __gt__ than it couldn't sort)

l = [c4, c2, c3, c1]

print(l)
print(sorted(l, key=lambda c: c.name))