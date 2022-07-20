######Function Arguments and Mutability#############

def process(s): # s reference the same object as my_var
    # process scope
    print("s before concat is {0}".format(hex(id(s))))
    s = s + 'world' # since strings are immutable s reference another object with value hello world
    print("s after concat is {0}".format(hex(id(s))))
    return s

# module scope
my_var = 'hello' # my_var reference an object with value hello
print("my_var before calling process is {0}".format(hex(id(my_var))))
process(my_var)
print("my_var after calling process is {0}".format(hex(id(my_var))))
# immutable are safe for side effects in functions

def process(lst): # reference same object as my_list
    print("lst before append is {0}".format(hex(id(lst))))
    lst.append(100) # still reference same object as my_list
    print("my_list after append is {0}".format(hex(id(lst))))

my_list = [1,2,3] # reference object of type list
print("my_list  before calling process is {0}".format(hex(id(my_list))))
print(my_list)
process(my_list)
print(my_list) # my_list object value changed and my_list reference same memory address
print("my_list before calling process is {0}".format(hex(id(my_list))))
# mutable objects are not safe for side effects in functions

def process(t):
    print("t before append is {0}".format(hex(id(t)))) # same address
    print("t[0] before append is {0}".format(hex(id(t[0])))) # same address
    t[0].append(3)
    print("t after append is {0}".format(hex(id(t)))) # same address
    print("t[0] after append is {0}".format(hex(id(t[0])))) # same address different value

my_tuple = ([1,2], 'a')
print("my_tuple before calling process is {0}".format(hex(id(my_tuple)))) #  same address
print("t[0] before process is {0}".format(hex(id(my_tuple[0])))) # same address
process(my_tuple)
print("my_tuple before calling process is {0}".format(hex(id(my_tuple)))) #  same address
print("t[0] after process is {0}".format(hex(id(my_tuple[0])))) # same address different value
########################