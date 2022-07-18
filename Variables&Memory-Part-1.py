#############################
import ctypes
import sys

b = 4
a = b
b = b + 1
print(a)
print(b)
# in python variables are refferences ( variables = memory addresses)
# in order to check the refference of a variable use id() - base 10 number hex - heaxdecimal value
print("Decimal value of a {0}".format(id(a)))
print("Decimal value of b {0}".format(id(b)))
print("Hexa value of a {0}".format(hex(id(a))))
print("Hexa value of b {0}".format(hex(id(b))))
############Refference Counting#################

# Reference Counting -> Python memory management clear the for a variables if there is no variable that is reference
#                       for that specific variable ( for example if a and b are reference for a memory address and then
#                       a and b are out of scope or whatever the reference counting for that memory is down to 0 and that
#                       space can be used again)
c = a
print("Reference value of a {0}".format(ctypes.c_long.from_address(id(a)).value)) # don't affect the refference count
print("Reference value of b {0}".format(ctypes.c_long.from_address(id(a)).value))
print("Reference value of c {0}".format(ctypes.c_long.from_address(id(a)).value))
print("Reference counting of a {0}".format(sys.getrefcount(a))) # creates an extra reffrence
print("Reference counting of b {0}".format(sys.getrefcount(b)))
print("Reference counting of c {0}".format(sys.getrefcount(c)))
# the reason that the first approch don't affect the refference count is that the id(a) finish to run first and after that
# the refference is counted

############Garbage Collector#################
# Garbage Collector role to remove circular refferences ( if obj A points to B and B points to A The memory management
# can't clean it so here the Garbage Collector comes in order to avoid memory leak)
# Garbage collector - can be controlled programatically using gc module
#                   - by default it is turned on
#                   - you can turn it off
#                   - run periodically on its own
#                   - you can call it manualy to do your own cleanup
import gc
def ref_count(address):
    return ctypes.c_long.from_address(address).value
def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object exists"
    return "Not found"
class A:
    def __init__(self):
        self.b = B(self)
        print('A: self: {0}, b: {1}'.format(hex(id(self)),hex(id(self.b))))
class B:
    def __init__(self, a):
        self.a = a
        print('B: self: {0}, a: {1}'.format(hex(id(self)), hex(id(self.a))))
gc.disable()
my_var = A()
print(hex(id(my_var))) # This is A
print(hex(id(my_var.b))) # This is B
print(hex(id(my_var.b.a))) # This is A again :D

a_id = id(my_var)
b_id = id(my_var.b)

print(hex(a_id))
print(hex(b_id))

print(ref_count(a_id)) # -> 2
print(ref_count(b_id)) # -> 1

print(object_by_id(a_id)) # Object exists
print(object_by_id(b_id)) # Object exists

my_var = None

print(ref_count(a_id)) # -> 1
print(ref_count(b_id)) # -> 1

print(object_by_id(a_id)) # Object exists
print(object_by_id(b_id)) # Object exists

gc.collect()

print(object_by_id(a_id)) # Not found
print(object_by_id(b_id)) # Not Found
print(ref_count(a_id)) # -> 0 but the memory address can be used by something else
print(ref_count(b_id)) # -> 0