# Mutable Sequence Types


l = [1, 2, 3, 4, 5]

print(id(l))

print(l[0])

l[0] = 'a' # l is mutated

print(l[0])

print(id(l))

l.clear() # l will be empty and mutated l

print(id(l))

l = [1, 2, 3, 4, 5]
print(id(l),l)

l = []  # we didn't mutate l here

print(id(l)) # different

suits = ['Spated', 'Hearts', 'Diamonds', 'Clubs']

alias = suits

print(id(suits), id(alias))

alias.clear()

print(alias, suits) # both empty

suits = ['Spated', 'Hearts', 'Diamonds', 'Clubs']

def something(l):
    l.append('None') # now l is mutated

something(suits)
print(suits) # l is changed

l = [1,2,3,4,5]
print(id(l))
print(l[0:2])
l[0:2] = ('a', 'b', 'c', 'd')
print(l) # a b c d 3 4 5
print(id(l)) # same id

l = [1,2,3]
print(id(l))
l = l + [4] # l not mutated
print(l, id(l)) # different id

l = [1, 2, 3]
print(id(l))
result = l.append(4) # l is mutated
print(type(result)) # None
print(l) # 1 2 3 4
print(id(l)) # same id

l.append([1,2,3])
print(l) # 1 2 3 4 [1,2,3]

l = [1,2,3]
print(id(l))
l.extend([1,2,3]) # extend expects an iterable else it gives exception

print(l) # 1 2 3 1 2 3
print(id(l)) # same id

l = [1, 2, 3]
l.extend({'X','a','A', 100_000})

print(l) # extended with different order(because of set)

l = [1, 2, 3, 4]
print(id(l))
print(id(l[3]))
a = l.pop() # pop - mutate the sequence by removing last elem and return the element that was poped off
print(id(a)) # same id as id(l[3])
print(a)

l = [1, 2, 3]
l.pop(1) # removes the second elem
print(l)

l = [1, 2, 3]
print(id(l))
del l[1] # removes the second elem
print(l)
print(id(l)) # same id


l = [1, 2, 3, 4]
print(id(l))
l.insert(1,'a') # a will be placed on index 1 and everything else will be shifted on the right
print(l)
print(id(l)) # same id

l = [1, 2, 3]
l2 = l[::-1]
print(id(l), id(l2)) # different objects

l.reverse() # l is mutated and is in reverse order
print(id(l))


l = [1, 2, 3, 4]
print(id(l))

l2 = l[:] # it is a copy of l with different id

print(id(l), id(l2))

l3 = l.copy() # different object same elems

print(id(l3), id(l)) # different

l = [['a', 'b'], 'c', 'd']
print(id(l), id(l[0]), id(l[1]))
l2 = l.copy()
print(id(l2), id(l2[0]), id(l2[1])) # l2 is changed but the elements are the same
print(l2[0] is l[0]) # True
print(l2[1] is l[1]) # True (for immutable dosen't matter but mutable can be changed
# To avoid it needs deep copy - This is called shallow copy