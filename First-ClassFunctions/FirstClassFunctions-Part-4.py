######## Lambda and Sorting #########

help(sorted) # can pass any iterable and returns a LIST in ascending order

l = [1,5,4,10,9,6]
print(sorted(l)) # l will be unaffected
l = ['c', 'B', 'D', 'a']
print(sorted(l))
print(ord('a')) # ascii of a
print(ord('A')) # ascii of A

print(sorted(l, key=lambda s: s.upper())) # case insensitive sort

d = {'def': 300, 'abc': 200, 'ghi': 100}
print(d)
print(sorted(d)) # list of keys sorted
print(sorted(d, key= lambda e: d[e])) # sort by value

def dist_sq(x):
    return (x.real)**2 + (x.imag)**2

print(dist_sq(1+1j))

l = [3+3j,1-1j,0,3 + 0j]
# sorted(l) not working on complex numbers no order
print(sorted(l,key=dist_sq)) # works order by distance
print(sorted(l, key = lambda x: (x.real)**2 + (x.imag)**2))

l = ['Cleese', 'Idle', 'Palin', 'Chapamn', 'Gilliam', 'Jones']
print(sorted(l))

print(sorted(l, key= lambda s: s[-1])) # sort by last element of each string
# sorting is stable sort if equal mentain the order originally when you specified the sort


# Randomizing an Iterable using Sorted
import random

help(random.random)
l = [1,2,3,4,5,6,7,8,9,10]
print(sorted(l,key= lambda x: random.random()))