"""
basic structure of dict: key: value

value -> any Python object

key -> any hashable object ( strings are hashable, lists are never hashable)

-> hash tables require hash of an object to be constant ( for the life of the program)
immutable objects are hashable
mutable objects are not hashable

hash(obj) -> some integer sys.hash_ifo.width
          -> Exception TypeError: unhasable type

-> int, float, complex, binary, Decimal, Fracion, ... -> hashable
-> strings -> hashable
-> frozen set -> hashable (all elements required to be hashable)
-> tuples -> hashable (all elements required to be hashable)
-> set, dict-> not hashable
-> list-> ot hashable
-> functions-> hashable
-> custom classes and objects -> maybe

If an object is hashable:
  -> the hash must be an integer
  -> if two object compare equal, the hash must also be equal

Important: two objects that do ot compare equal may still have same hash ( hash collision) -> more hash collisios -> slower dict

"""

a = {'k1': 100, 'k2': 200}

print(type(a))

print(hash((1,2,3)))

d = {(1,2,3): 'this is a tuple'}

print(d[(1,2,3)])

t1 = (1,2,3)
t2 = (1,2,3)
print(hash(t1) == hash(t2)) #True
print(t1 is t2) # False or true but it can be false

print(d[t1])
print(d[t2])

def my_funct(a,b,c):
    print(a,b,c)

print(hash(my_funct))

d = {my_funct: [10, 20, 30]}

print(d)

def fn_add(a, b):
    return a + b

def fn_inv(a):
    return 1/a

def fn_mult(a,b):
    return a*b

funcs = {fn_add: (10, 20), fn_inv: (2, ), fn_mult: (2, 8)}

for f in funcs:
    result = f(*funcs[f])
    print(result)

for f, args in funcs.items():
    print(f(*args))


d = dict(x=100, a=200)

print(d)

d = dict([('a', 100), ['x', 200]])

print(d)

d = {'a': 100, 'b': 200}

print(id(d))
d1 = dict(d) # this is a shallow copy

print(d is d1) # False



d = {'a': 100, 'b': {'x': 1, 'y': 2}, 'c': [1,2,3]}

d1 = dict(d)

print(d is d1) # False

print(d['b'] is d1['b']) # True

d1['b']['z'] = 100

print(d1['b'])
print(d['b'])



keys = ['a', 'b', 'c']
values = (1, 2, 3)

d = {}

for k, v in zip(keys, values):
    d[k] = v

print(d)

d = {k: v for k, v in zip(keys, values)}

print(d)

keys = 'abcd'
values = range(1, 5)

d = {k: v for k, v in zip(keys,values) if v % 2 ==0}

print(d)

x_coords = (-2, -1, 0, 1, 2)
y_coords = (-2, -1, 0, 1, 2)

grid = [(x, y)
        for x in x_coords
        for y in y_coords]
print(grid)

import math

grid_extended = [(x,y, math.hypot(x,y)) for x, y in grid]
print(grid_extended)

grid_extended = {(x,y): math.hypot(x,y) for x, y in grid}
print(grid_extended)


counters = dict.fromkeys(['a', 'b', 'c'], 0)
print(counters)
counters = dict.fromkeys('abc', 0)
print(counters)

d = dict.fromkeys('python')
print(d)