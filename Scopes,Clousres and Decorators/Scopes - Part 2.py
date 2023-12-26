###### Nonlocal Scopes ########

def outer_func():
    x = 'hello'
    def inner_func():
        print(x) # hello (will be x from outer_func)
    inner_func()

outer_func()

def outer_func():
    x = 'hello'
    def inner1():
        def inner2():
            print(x) # will be hello
        inner2()
    inner1()
outer_func()

def outer_func():
    x = 'hello'
    def inner():
        x = 'python'
        print('inner:', x) # python
    inner()
    print('outer:', x) # hello

outer_func()

def outer_func():
    x = 'hello'
    def inner():
        nonlocal x
        x = 'python'
        print('inner:', x) # python
    inner()
    print('outer:', x) # python

outer_func()


def outer_func():
    x = 'hello'
    def inner1():
        x = 'python'
        def inner2():
            nonlocal x
            x = 'eul'
            print('inner2:',x) # eul
        inner2()
        print('inner1:', x)  # eul


    inner1()
    print('outer:', x)  # hello


outer_func()

def outer_func():
    x = 'hello'
    def inner1():
        def inner2():
            nonlocal x # searches the x in inner1 not found and then search in outer_func (outer_func and inner1 = non locals)
            x = 'eul'
            print('inner2:',x) # eul
        inner2()
    inner1()
    print('outer:', x)  # eul

outer_func()
# x = 10
# def outer_func():
#     def inner1():
#         def inner2():
#             nonlocal x # error python does not find an x nonlocal (the x is global) so error
#             x = 'eul'
#             print('inner2:',x) # eul
#         inner2()
#
# outer_func()


# x = 10
# def outer_func():
#     global x
#     x = 100
#     def inner1():
#         def inner2():
#             nonlocal x # still error x in outer is global not nonlocal
#             x = 'eul'
#             print('inner2:',x) # eul
#         inner2()
#
# outer_func()

x = 10
def outer_func():
    x = 'hello'
    def inner1():
        nonlocal x
        x = 'python'
        def inner2():
            global x
            x = 'eul'
            print('inner2:',x) # eul
        inner2()
        print('inner1:', x)  # python


    inner1()
    print('outer:', x)  # python
outer_func()
print('global:', x) # eul