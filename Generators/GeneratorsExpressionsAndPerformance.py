"""
Generators expressions use the same comprehension syntax - including nesting, if

but instead of [] we use ()

[i ** 2 for i in range(5)]              (i ** 2 for i in range(5)])
 - a list is returned                       - a generator is returned
 - evaluation is eager(everything           - evaluation is lazy ( return one element at a time)
            computed and in memory)
 - has local scope                          - has local scope

 - can access nonlocal and                   - can access nonlocal and
   global scope                                    global scope

 - iterable                                  - iterator (gets exhausted)


List comprehensions
    - everything is precalculated right away
    - takes longer to create/return the list
    - interation is faster ( objects already created)
    - entiere collections is loaded into memory
Generators
    - object creation is delayed until requested by next
    - generator is created/returned immedialty
    - iteration is slower ( objects need to be created)
    - only a single item is loaded at a time

if iterate through all elements -> time performance is about the same
if you do not iterate through all the elements -> generator more efficient

In general, generators tend to have less memory overhead
"""

l = [i**2 for i in range(5)]

print(l)

g = (i**2 for i in range(5))

print(type(g)) # generator
for item in g:
    print(item)

print(list(g)) # empty exhausted

import dis

exp = compile('[i**2 for i in range(5)]', filename='<string>', mode='eval')

dis.dis(exp)

exp = compile('(i**2 for i in range(5))', filename='<string>', mode='eval')

dis.dis(exp)



l = [i**2 for i in range(5)]
g = (i**2 for i in range(5))

print(list(l))
print(list(l))
print(list(g))
print(list(g)) # empty

start = 1
stop = 10

mult_list = [[i*j
              for j in range(start,stop+1)]
             for i in range(start,stop+1)]
print(mult_list)

mult_list = ((i*j
              for j in range(start,stop+1))
             for i in range(start,stop+1))
#print(list(mult_list)) # each item is a generator

print([list(row) for row in mult_list])


mult_list = ((i*j
              for j in range(start,stop+1))
             for i in range(start,stop+1))

for row in mult_list:
    print(', '.join([str(item) for item in row]))

mult_list = ([i*j
              for j in range(start,stop+1)]
             for i in range(start,stop+1))
print(list(mult_list))