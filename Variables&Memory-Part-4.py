###########Shared Refferences and Mutability################
# Python memory management decides to automatically re-use the memory refferences
# For immutable objects Examples:
a = 10 # same refference
b = 10 # same refference ( sometimes it keeps same refference sometimes it doesn't)
c = a # same refference
b = b + 5 # different refference from a and c (python evalutates righ hand side first)

a = 'hello' # same refference
b = 'hello' # same refference
c = a # same refference
b = b + 'world' # different refference from a and c (python evaluates right hand side first)

# For mutable objects Examples:

a = [1,2,3] # same refference
b = a # same refference
b.append(4) # b change the value of the refference to [1,2,3,4]
print(a) # same value [1,2,3,4]
print(b) # same value [1,2,3,4]
c = a.copy() # different refference
c.append(10)
print(a) # a = [1,2,3,4]
print(c) # c = [1,2,3,4,10]

####################Variables Equality############################
# Compare:
#       - Memory address: is ( is not )- identity operator (var1 is var2) (var1 is not var2) (not(var1 is var2))
#       - Object state (data): == ( != )- equality operator (var1 == var2) (var1 != var2) (not(var1 == var2))
a = 10
b = a
print(a is b) # True
print(a == b) # True
a = 'Hello'
b = 'Hello'
print(a is b) # True but should not count on it
print(a == b) # True

a = [1,2,3]
b = [1,2,3]

print(a is b) # False
print(a == b) # True

a = 10
b = 10.0

print(a is b) # False
print(a == b) # True

# The None object
# The None object can be assigned to variables to indicate that they are not set
# i.e an empty value (or null pointer)
# None is a real object that is managed by Python memory manager
# The memory manager will always use a shared reffrence assigning a variable to None

a = None
b = None
c = None
print(id(a))#same refference
print(id(b)) # same refference
print(id(c)) # same refference
print(id(None)) # same refference
print(type(None)) # None Type
print(a is None) # True
x = 10
print(x is None) # False
print(x is not None) # True
################################################