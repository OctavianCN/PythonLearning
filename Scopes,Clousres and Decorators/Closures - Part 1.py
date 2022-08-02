######## Closures ###########


def outer():
    x = 'python'
    def inner():
        print(x) # x is going to form a closure
    return inner # return the closure from the function

fn = outer() # fn is a closure

print(fn.__code__.co_freevars) # x is a free variable
print(fn.__closure__) # return a tuple that contains the address of the cell
                      # so x from outer function and x from inner function
                      # refference a cell (an object in memory) that refferences
                      # the string object python so both x refference same cell (so when outer function finish to run and x from outer dissapair the string python is still refferenced by the cell(so garbage collector don't clear it)
def outer():
    x = list(range(500,1000))
    print(hex(id(x))) # different memory addreses (
    def inner():
        x = list(range(500,1000))
        print(hex(id(x))) # different memory addresses
    return inner

fn = outer()
fn()

def outer():
    x = list(range(500,1000))
    print(hex(id(x))) # same memory address(memory address of the list not the cell (the real address of x))
    def inner():
        y = x
        print(hex(id(x))) # same memory address (memory address of the list not the cell)
    return inner

fn = outer()
fn()
print(fn.__closure__)

def outer():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

fn = outer()
print(fn.__code__.co_freevars) # count
print(fn.__closure__) # points to the cell that points to the int (count 0)
print(hex(id(0))) # same address as the cell points
print(fn()) # the cell changed where is pointing to
print(fn.__closure__) #cell  points to the memory address of 1
print(hex(id(1))) # same address as the cell points

def outer():
    count = 0  # point to the same cell
    def inc1():
        nonlocal count # point to the same cell
        count += 1
        return count

    def inc2():
        nonlocal count # point to the same cell
        count += 1
        return count
    return inc1,inc2

fn1, fn2 = outer()

print(fn1.__code__.co_freevars)
print(fn2.__code__.co_freevars)

print(fn1.__closure__) # same cell
print(fn2.__closure__) # same cell

print(fn1()) # 1
print(fn2()) # 2

def pow(n):
    def inner(x):
        return x ** n # n points to a cell that points to no value
    return inner

square = pow(2)
print(square.__closure__) # now n points to a cell that ponts to integer 2
print(square(5)) # 25

cube = pow(3)
print(cube.__closure__) # diffrent cell addreess from square
print(cube(5)) # 125

# cube and square were created from the same outer function (pow) but they have different
# scopes  - every call gets a new scope

def adder(n):
    def inner(x):
        return x + n
    return inner

add_1 = adder(1)
add_2 = adder(2)
add_3 = adder(3)
# three different scopes created (the n's are different on adder1 adder2 adder3)

print(add_1.__closure__) # three differenc cells
print(add_2.__closure__)
print(add_3.__closure__)

print(add_1(10)) # 11
print(add_2(10)) # 12
print(add_3(10)) # 13

adders = []
for n in range(1,4):
    adders.append(lambda x: x + n) # this n is refferencing the global n not local n
                                   # the adders are not closures here because it is not refferencing local n
print(adders[0].__closure__) # nothing no closure
print(adders[1].__closure__) # nothing
print(adders[2].__closure__) # nothing

print(adders[0](10)) # 13
print(adders[1](10)) # 13
print(adders[2](10)) # 13

def create_adders():
    adders = []
    for n in range(1,4): # n is a local variable inside create adders
        adders.append(lambda x: x + n) # when you create this function it is not evaluating n ( it is evaluating n when you call the lambda)
    return adders


adders = create_adders()

print(adders[0].__closure__) # now we have a closure pointing to the same cell each
print(adders[1].__closure__)
print(adders[2].__closure__)

print(adders[0](10)) # 13
print(adders[1](10)) # 13
print(adders[2](10)) # 13



def create_adders():
    adders = []
    for n in range(1,4):
        adders.append(lambda x, y=n: x + y) # here y will be different for all function because y is a default value and it is evaluated at creation time
    return adders


adders = create_adders()

print(adders[0].__closure__) # no closures we just create functions
print(adders[1].__closure__)
print(adders[2].__closure__)

print(adders[0].__code__.co_freevars) # no free variables
print(adders[1].__code__.co_freevars)
print(adders[2].__code__.co_freevars)

print(adders[0](10)) # 11
print(adders[1](10)) # 12
print(adders[2](10)) # 13