###########Extended Unpacking#################


# * - unpacking operator
print("Unpacking with * operator")
l = [1,2,3,4,5,6]

#Var 1
a = l[0]
b = l[1:]

#Var 2
a, b = l[0], l[1:] # parralel asignment

#Var 3
a, *b = l # this works with any iterable

a,b,*c,d = 1,2,3,4,5 # * can only be used once
print(a) # 1
print(b) # [2]
print(c) # [3,4]
print(d) # 5


l1 = [1,2,3]
l2 = [4,5,6]
l = [*l1,*l2] # combined list

# For unordered types

s = {10,-99,3,'d'}
print(s)
a, *b,c = s # still works but don't know who is the first elem because it is an unordered list
print(a)

d1 = {'p': 1, 'y': 2}
d2 = {'t': 3, 'h': 4}
d3 = {'h': 5, 'o': 6, 'n': 7}
l = [*d1,*d2,*d3] # unpacking all the keys(order not guaranteed) of dict
                  # with repetitions ( h will appear two times
l2 = {*d1,*d2,*d3} # unpacked in a set and set have unique elements
print(l)
print(l2)

# ** unpacking operator ( cannot be used in left hand side of an assigment)
print("Unpacking with ** operator")

d1 = {'p': 1, 'y': 2}
d2 = {'t': 3, 'h': 4}
d3 = {'h': 5, 'o': 6, 'n': 7}
d = {**d1,**d2,**d3} # get key value pairs dicts are merged (last added overwrote prev value)
                     #  ex h will be 5
print(d)

d1 = {'a': 1, 'b': 2}
d2 = {'a': 10, 'b': 3, **d1} # a=1 b= 10
d3 = {**d1, 'a': 10, 'b': 3} # a= 10 b = 3
print("d2 = {0} \nd3 = {1}".format(d2,d3))

# Nested Unpacking
print("Nested Unpacking")

l = [1,2,[3,4]]

a,b,(c,d) = l
print(a,b,c,d)

a,*b,(c, *d) = [1,2,3,'python'] # works because second * is nested inside a tuple
print(a,b,c,d)

l = [1,2,3,'python']
a,b,c,d = l[0],l[1:-1],l[-1:][0][0],[char for char in l[-1:][0][1:]] # var 1
print(a,b,c,d)
a,b,c,d = l[0],l[1:-1],l[-1:][0][0],list(l[-1:][0][1:]) # var 2
print(a,b,c,d)
