"""
In-place Concatenation and Repetition
"""

l1 = [1, 2, 3, 4]
l2 = [5, 6]
print(id(l1), l1)
print(id(l2), l2)

l1 = l1 + l2
print(id(l1), l1) # id of l1 changed

t1 = 1, 2, 3
#l1 = l1 + t1 not working

l1 = [1, 2, 3, 4]
l2 = [5, 6]
print(id(l1), l1)
print(id(l2), l2)

l1 += l2 # += (in-place concatenation) not the same as + ( for mutable types)
print(id(l1), l1) # id of l1 did NOT changed
# += - mutate l1


l1 = [1, 2, 3, 4]
t1 = (5, 6)
print(id(l1), l1)
print(id(t1), t1)

l1 += t1
print(id(l1), l1) # list is extended with what was in the tuple and memory address did not change

l1 += range(7, 11)
print(id(l1), l1)

l1 += {100, 'X', 'a'}
print(id(l1), l1)

t1 = 1, 2, 3
t2 = 4, 5, 6

print(id(t1), t1)
print(id(t2), t2)

t1 += t2
print(id(t1), t1) # memory address has changed because t1 is immutable

l1 = [1, 2, 3]

print(id(l1), l1)

l1 = l1 * 2

print(id(l1), l1) # memory of l1 changed

l1 *= 2
print(id(l1), l1) # memory of l1 did NOT changed

t1 = 1, 2, 3
print(id(t1), t1)
t1 *= 2
print(id(t1), t1) # t1 address has changed