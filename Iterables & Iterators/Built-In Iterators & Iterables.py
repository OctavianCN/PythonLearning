"""
Built-In Iterators and Iterables
"""

r = range(10)
print(r)
print(type(r))
print('__iter__' in dir(r)) # True
print('__next__' in dir(r)) # False

print(iter(r))

for num in r:
    print(num)

print([num for num in r]) # r is an iterable

z = zip([1,2,3], 'abc') #
print(z) # zip and range are lazy you don't know what is inside until you iterate them
print('__iter__' in dir(z)) # True
print('__next__' in dir(z)) # True zip si an iterator
print(list(z))
print(list(z)) # now z is exhausted

#with open('cars.csv') as f: - with close file after done
f = open('cars.csv')
print(next(f))
print(f.__next__()) # f is an iterator
print(f.readline()) # does the same thing as next
f.close()
print("=============")
with open('cars.csv') as f:
    for row in f:
        print(row, end='')

print("==============")

with open('cars.csv') as f:
    print(type(f))
    print('__iter__' in dir(f)) # True
    print('__next__' in dir(f)) # True

with open('cars.csv') as f:
    print(iter(f) is f) # True

with open('cars.csv') as f:
    l = f.readlines() # this loads the entire file into memory in the list

print(l)

print("==============")
origins = set()
with open('cars.csv') as f:
    rows = f.readlines()
for row in rows[2:]:
    origin = row.strip('\n').split(';')[-1]
    origins.add(origin)

print(origins)

print("================")
origins = set()
with open('cars.csv') as f:
    next(f), next(f) # skip the first two lines so we do not load the entire file into memory
    for row in f:
        origin = row.strip('\n').split(';')[-1]
        origins.add(origin)
print(origins)

e = enumerate('Python Rocks!')
print(iter(e) is e) # True is an iterator
print(list(e))
print(list(e)) # now we get an empty list

d = {'a': 1, 'b': 2}
keys = d.keys()
print(iter(keys) is keys) # False keys is an iterable not an iterator
