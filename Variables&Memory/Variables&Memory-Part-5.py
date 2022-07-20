############Everything is an object##################

#Everything is an object
# Functions are an instance of class function
# Classes are an instances of class class
# etc..
#They all have a memory address

def my_func(): # --> memory address with a value of function state
    pass
# my_func -> is the name of the function
# my_func() -> invokes the function
print(id(my_func))

# As a consequence:
#        - Any object can be assigned to a variable (including functions)
#        - Any object can be passed to a function ( including functions)
#        - Any object can be returned from a function ( including functions)

help(int) # documentation for class int
c = int()
print(c)
c = int('101', base=2)
print(c)

def square(a):
    return a**2

print(type(square))
f = square
print(id(square)) # same refference
print(id(f)) # same refference
print(f is square) # True
print(f(2)) # 4
print(square(2)) # 4

def cube(a):
    return  a**3

def select_function(fn_id):
    if fn_id == 1:
        return square
    else:
        return cube

f = select_function(2)
print(f is cube) # True
print(f(2)) # 8
print(select_function(2)(3)) # 27

def exec_function(fn, n):
    return fn(n)
print(exec_function(cube, 3)) # 27

########################################################################