###########Unpacking Iterables##################

#### What defines a tuple in Python is , not (). The , creates a tuple

#(1) is not a tuple is an int
1, #creates a tuple
() # the only exception is when creating an empty tuple

#Packed values refers to values that are bundled toghether in some way
#Tuples, Lists, Strings, Sets, Dictionaries - are packed values

# An iterable can be considered a packed value

#Unpacking - act of splitting packed values into individual variables

# Unpacking works with any iterable type

a = (1,2,3)
print(type(a)) #tuple
a = 1, 2, 3
print(type(a)) # tuple
a = (1)
print(type(a))# int
a = (1,)
print(type(a)) # tuple
a = ()
print(type(a)) # tuple

a, b, c = [1,'a',3.14] # positional unpacking a=1 b='a' c = 3.14 a b c is a tuple
a, b = 1, 2 # unpacking a tuple a=1 b=2
# python first evaluate right hand side
a, b =b, a # swap two variables
print(a)
print(b)
s = {1,2,3} # sets are like dictionaries but only with keys (is unordered)
#s[0] WRONG it does not support indexes
s = {1,4,6,2}
print(s) # not the same order
for e in s:
    print(e) #different order than it is declared

d = {'a':1, 'b':2, 'c':3}
for e in d:
    print(e) # returns just the keys
d,a,b = d # first python take the refference of the dictionary and then assign it
          # to variables
print(d) # will have the value a

d = {'a':1, 'b':2, 'c':3}
for e in d.values():
    print(e) # print values

a,b,c = d.values()

for e in d.items():
    print(e) # is a tuple
    a,b = e # now unpacked the tuple

for a,b in d.items():
    print(a,b)