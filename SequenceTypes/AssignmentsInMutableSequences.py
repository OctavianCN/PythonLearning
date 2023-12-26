#### Assignments In Mutable Sequences #####

l = [1, 2, 3, 4, 5]
print(id(l), l)
print(l[0:3])
l[0:3] = 'python' # assign an iterable of any length
print(id(l), l) # same id

l = [1, 2, 3, 4, 5]
print(id(l), l)
print(l[2:5]) # 3 4 5
l[2:5] = []
print(id(l), l) # 1 2 (3, 4, 5 -deleted)

l = [1, 2, 3, 4, 5]
print(id(l), l)
print(l[2:5]) # 3 4 5
l[2:5] = '' # python is looking for an iterable in the right hand side
print(id(l), l) # 1 2 (3, 4, 5 -deleted)

l = [1, 2, 3, 4, 5]
print(id(l), l)
print(l[2:2]) # []
l[2:2] = 'abc'
print(id(l), l) # [1, 2, 'a', 'b', 'c', 3, 4, 5]

l = [1, 2, 3, 4, 5]
print(id(l), l)
l[0:3] = {100, 'X', 'a'}
print(id(l), l)

# Extended Slices
# Length of the extended slice and the length of the replacement should be the same ( Insertion and Deletion - NOT WORKING with extended slices)

l = [1, 2, 3, 4, 5]
print(id(l),l)
print(l[0:5:2])
l[0:5:2] = 'abc'
print(id(l), l)

# l = [1, 2, 3, 4, 5]
# print(id(l),l)
# print(l[0:5:2])
# l[0:5:2] = 'ab' # Exception
# print(id(l), l)