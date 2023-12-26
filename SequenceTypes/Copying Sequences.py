# Copying Sequences

"""
Why copy sequences?

Mutable sequences can be modified.

s = [10, 20, 30]
new_list = reverse(s)
new_list -> 30 20 10
s -> 30 20 10

l1 = [1, 2, 3]
l2 = list(l1)     l2 is not l1

t1 = (1, 2, 3)
t2 = tuple(t1)    id(t1) = id(t2) same object

t1 = (1, 2, 3)
t2 = t1[:]     id(t1) = id(t2) same object

Same thing with strings, also an immutable sequence type

Since the sequence is immutable, it is actually ok to return the same sequence

Shallow Copies

When we use any of the copy methods, the copy essentially copies
all object references from one sequence to another

s = [a, b]   id(s) -> 1000    id(s[0]) -> 2000  id(s[1])-> 3000
cp = s.copy() id(cp) -> 5000    id(cp[0]) -> 2000  id(cp[1])-> 3000

When we made a copy of s, the sequence was copied, but it's elements point to the
same memory address as the original sequence elements

The sequence was copied, but it's elements were not

This is called a shallow copy

If the elements of the list are immutable, then it is not really important
But if the elements of the list are mutable, then it could be important

Deep Copies

So, if collections contain mutable elements, shallow copies are not sufficient to ensure
the copy can never be used to modify the original.
Instead, we have something called deep copy

s = [[0, 0], [0, 0] ]
cp = [e.copy() for e in s] - cp is a copy of s but every element of cp is a shallow copy of the corresponding element is s
For example
s = [[ [0, 1], [2, 3] ], [ [4, 5], [6, 7] ]]
We would need to make copies at least 3 levels deep to ensure a true deep copy

Deep copies, in general, tend to need a recursive approch

Deep copies are not easy to do. You might even have to deal with circular references
a = [10, 20]
b = [a, 30]
a.append(b)
If you wrote your own deep copy algorithm, you would need to handle this circular reference!

In general, objecs know how to make shallow copies of themselve,
built-in objects like lists, sets, and dictionaries do - they have a copy() method

The standard library copy module has generic copy and deepcopy operations

The copy function will create a shallow copy
The deepcopy function will create a deep copy, handling nested objects, and circular references properly

Custom classes can implement the __copy__ and __deepcopy__ methods to allow you to
override how shallow and deep copies are made for custom objects

"""

# Copying Sequences

# Shallow Copy

l1 = [1,2,3]

l1_copy = []

for item in l1:
    l1_copy.append(item)

print(l1_copy)
print(id(l1), id(l1_copy)) # different id

l1_copy = [item for item in l1]

print(l1_copy)
print(id(l1), id(l1_copy)) # different address

l1_copy = l1.copy()

print(l1_copy)
print(id(l1), id(l1_copy)) # different addresses

l1_copy = list(l1)

print(l1_copy)
print(id(l1), id(l1_copy)) # different addresses

t1 = 1,2,3
l1_copy = list(t1) # from tuple to list

print(l1_copy)

t1 = 1,2,3
t2 = tuple(t1)

print(id(t1), t1)
print(id(t2), t2) # same object

l1 = [1, 2, 3]
l2 = l1[:]
print(id(l1), id(l2)) # different addreses

t1 = 1, 2, 3
t2 = t1[:]
print(id(t1), t1)
print(id(t2), t2) # same object (no point making a copy for immutable container

s1 = 'python'
s2 = str(s1)
print(id(s1), s1)
print(id(s2), s2) # same object

s1 = 'python'
s2 = s1[:]
print(id(s1), s1)
print(id(s2), s2) # same object

import copy

l1 = [1,2,3]
l2 = copy.copy(l1)
print(id(l1), l1)
print(id(l2), l2) # different id

t1 = 1, 2, 3
t2 = copy.copy(t1)
print(id(t1), t1)
print(id(t2), t2) # same id

# Deep Copies

v1 = [0,0]
v2 = [0,0]

line1 = [v1, v2]

line2 = line1.copy()

print(id(line1), id(line2)) # different addresses

print(id(line1[0]), id(line2[0])) # same addresses

line2  = [v for v in line1]

print(id(line1[0]), id(line2[0])) # same addresses
print(id(line1[1]), id(line2[1])) # same addresses

print(line1)
print(line2)

line1[0][0] = 100

print(line1)
print(line2) # same change as line1

line2 = [v.copy() for v in line1]

print(line1)
print(line2)

print(id(line1), id(line2)) # different addresses

print(id(line1[0]), id(line2[0])) # different addresses

line1[0][0] = 100

print(line1)
print(line2) # different than line1

v1 = [1, 1]
v2 = [2, 2]
v3 = [3, 3]
v4 = [4, 4]

line1 = [v1, v2]
line2 = [v3, v4]

plane1 = [line1, line2]

print(plane1)

plane2 = [line.copy() for line in plane1]

print(plane1)
print(plane2)

print(id(plane1[0]), id(plane2[0])) # different memory addresses

print(plane1[0])
print(plane2[0])

print(id(plane1[0][0]), id(plane2[0][0])) # same memory addresses

# Solution:

v1 = [1, 1]
v2 = [2, 2]
v3 = [3, 3]
v4 = [4, 4]

line1 = [v1, v2]
line2 = [v3, v4]

plane1 = [line1, line2]

plane2 = copy.deepcopy(plane1)

print(id(plane1), id(plane2)) # different memory addresses
print(id(plane1[0]), id(plane2[0])) # different memory addresses
print(id(plane1[0][0]), id(plane2[0][0])) # different memory addresses

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return  f'Point {self.x}, {self.y}'

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f'Line({self.p1.__repr__()}, {self.p2.__repr__()})'

p1 = Point(0, 0)
p2 = Point(10, 10)

line1 = Line(p1, p2)
line2 = copy.deepcopy(line1)

print(line1.p1, id(line1.p1))
print(line2.p1, id(line2.p1)) # different memory addresses

p1 = Point(0, 0)
p2 = Point(10, 10)

line1 = Line(p1, p2)
line2 = copy.copy(line1)

print(line1.p1, id(line1.p1))
print(line2.p1, id(line2.p1)) # same memory addresses

# Copy and Deep copy are applicable to objects in general

