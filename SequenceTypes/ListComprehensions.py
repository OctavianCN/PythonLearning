"""
List Comprehensions

"""

squares = []

for i in range(1, 101):
    squares.append(i**2)

print(squares[0:10])
squares = [i**2 for i in range(1, 101)]

print(squares[0:10])

squares = []
for i in range(1, 101):
    if i % 2 == 0:
        squares.append(i**2)

print(squares[0:10])

squares = [i**2 for i in range(1, 101) if i % 2 == 0]

print(squares[0:10])

squares = [i** 2
            for i in range(1, 101)
            if i % 2 == 0]

print(squares[0:10])

compiled_code = compile('[i**2 for i in (1,2,3)]', filename='string', mode='eval')

print(type(compiled_code))

import dis

dis.dis(compiled_code) # it makes a function - comprehantions are functions

table = []

for i in range(1, 11):
    row = []
    for j in range(1, 11):
        row.append(i*j)
    table.append(row)

table2 = [ # nested comprehentions
    [ i * j for j in range(1, 11)] # -> this is refferencing i from outerscope ( i is a free variable ) this is a closure
    for i in range(1, 11)
]
"""
C(n,k) = n! / (k! (n-k)!)

C(0,0)
C(1,0) C(1,1)
C(2,0) C(2,1) C(2,2)
C(3,0) C(3,1) C(3,2) C(3,3)
"""
from math import factorial

def combo(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

size = 10

pascal = [[combo(n,k) for k in range(n+1)] for n in range(size + 1)]

print(pascal)

# Nested Loops

l1 = ['a', 'b', 'c']
l2 = ['x', 'y', 'z']

result = []

for s1 in l1:
    for s2 in l2:
        result.append(s1 + s2)

result = [  s1 + s2
          for s1 in l1
          for s2 in l2 ] # nested loops

print(result)

result = [  s1 + s2
          for s2 in l2
          for s1 in l1 ] # different result

print(result)

l1 = ['a', 'b', 'c']
l2 = ['b', 'c', 'd']

result = []
for s1 in l1:
    for s2 in l2:
        if s1 != s2:
            result.append(s1 + s2)

result = [ # this is similar as above
    s1 + s2
    for s1 in l1
    for s2 in l2 if s1 != s2
]
print(result)

result = [
    s1 + s2
    for s1 in l1 if s1 != 'a' # this also works
    for s2 in l2 if s1 != s2
]

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = ['a', 'b', 'c', 'd']

print(list(zip(l1,l2)))

print(list(enumerate(l1))) # tuple with index and value
print(list(enumerate(l2)))

result = []
for index_1, item_1 in enumerate(l1):
    for index_2, item_2 in enumerate(l2):
        if index_1 == index_2:
            result.append((item_1, item_2))

print(result)

result = [ (item_1, item_2)
           for index_1, item_1 in enumerate(l1)
           for index_2, itme_2 in enumerate(l2)
           if index_1 == index_2]

l = [1, 2, 3]
print(sum(l))

'''
v1 = (c1, c2, c3, ..., cn)
v2 = (d1, d2, d3, ..., dn)
'''

# Doing vector multiplication

dot = 0
v1 = 1, 2, 3, 4, 5, 6
v2 = 10, 20, 30, 40, 50, 60
for i in range(len(v1)):
    dot += (v1[i] * v2[i])
print(dot)

print(list(zip(v1, v2)))

print(sum(i*j for i,j in zip(v1, v2)))

# Watch out!!
l = []
for number in range(5):
    l.append(number ** 2)
print(number)

if 'number' in globals():
    del number

l = [number ** 2 for number in range(5)]

print(l)

print('number' in globals()) # False number lives in that comprehension

number = 100
l = []
for number in range(5):
    l.append(number ** 2)

print(number) # number will be 4 because it is in global

number = 100
l = [number ** 2 for number in range(5)] # here number will be a local number because
                                         # we are doing an assignment ( because in for firstly we assign a value to number)

print(number) # number = 100 -> this is the global number

l = [number * i for i in range(5)] # here number will be global

fn_0 = lambda x: x**0
fn_1 = lambda x: x**1
fn_2 = lambda x: x**2
fn_3 = lambda x: x**3

funcs = [lambda x: x**0, lambda x: x**1, lambda x: x**2, lambda x: x**3]

for i in range(4):
    print(funcs[i](10))

if 'i' in globals():
    del i

funcs = []

for i in range(6):
    funcs.append(lambda x: x**i) # this lambda is a closure and i varibale it is refferencing the global i
# here i will always be 5

print(funcs[0](10))
print(funcs[2](10)) # same value


from datetime import datetime

datetime.now()

def log(msg, current_dt = datetime.now()):
    print(msg, current_dt)

print(log('abc'))

print(log('cde')) # same datetime as before - default values of parameters are already evaluated when compiled

funcs = [lambda x, p = i # this will be caluculated every time when the function is compiled
                        : x**p for i in range(5)]

print(funcs[1](10))
print(funcs[2](10))