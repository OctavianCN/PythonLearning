#########Dynamic vs Static Typing####################

# Statically typed programming Languages example: C++, Java, Swift
# Example Java: String     myVar        =   "hello" -> reference bound to a data type
#               data type  variable name    value
# Dynamically typed: Python
# my_var = "hello" -> my_var is a refference to a string object with value hello
# type not attached to my_var
# type() function to determine the type of object currently reffrenced by a variable
# variables in Python do not have an inherent static type
#type(my_var) -> Python looks up the obj my_var is referencing and returns the type of the object
#                at that memory location

my_var = "test"
print(type(my_var))
my_var = 10
print(type(my_var))
my_var = lambda x: x**2
print(my_var(2))
print(type(my_var))
my_var = 3 + 4j
print(type(my_var))

#########Variable Reassignment####################
new_var = 10 # new_var is refferencing an integer with the value of 10
print(hex(id(my_var))) # first_address
new_var = 15 # new_var is refferencing another address of an integer with the value of 15
print(hex(id(my_var))) # second_address (first_address != second_address)
new_var = new_var + 5 # new_var is refferencing another address by adding the value of second_address with 5
print(hex(id(new_var))) # third_address (first_address != second_address != third_address)
new_varA = 10
new_varB = 10
print(hex(id(new_varA))) # fourth address
print(hex(id(new_varB))) # fourth address (same address as new_varA)

#########Object Mutability####################
# Changing the data inside the object is called modifying the internal
# state of the object ( memory address not changed but internal state (data) has changed) -> Object was mutated
# An object whose internal state can be changed -> Mutable
# An object whose internal state cannot be changed -> Immutable
# Immutable objects: Numbers (int, folat, booleans etc), Strings, Tuples, Frozen Sets, User-Defined Classes
# Mutable objects: Lists, Sets, Dictionaries, User-Defined Classes
a = [1, 2] # mutable
b = [3, 4] # mutable
t = (a, b) # immutable
print(t)
a.append(3) # in this case althrough the tuple is immutable, its elements are not
b.append(5) # the object references in the tuple did not change but the reference objects did mutate
print(t)

my_list = [1, 2, 3]
print(my_list)
print(id(my_list)) # first id
my_list.append(4) # this modify the internal state of my_list
print(my_list)
print(id(my_list)) # same id as first id
my_list_1 = [1, 2, 3]
print(my_list_1)
print(id(my_list_1)) # second id different from before
my_list_1 = my_list_1 + [4] # first evaluates the right hand side and combine the two lists and returns a new object
# this does not modify the internal state of my_list_1
print(my_list_1)
print(id(my_list_1)) # third id diffrent from before
