"""
Pattern

create some object - do some work with that object
clean up the object after we're done using it

We want to make this easy
    -> automatic cleanup after we are done using the object

Context Managers - PEP 343

    with context as obj_name:
        with block( can use obj_name)
    after the with block, context is cleaned up automatically

The context management protocol

    Classes implement the context management protocol by implementing two methods:
        - __enter__ - setup and optionally return some object
        - __exit__ - tear down / cleanup

How Context Protocol Works:

    works in conjunction with a with statement
    my_obj = MyClass() - works as a regular class __enter__, __exit__ - were not called

    with My_Class() as obj:
        -> creates an instance of MyClass -> no associated symbol, but an instance exists
        -> calls my_instance.__enter__()
        -> return value from __enter__ is assigned to obj (not the instance of MyClass that was created)

    after the with block, or if an exception occurs inside the with blocj:
        -> my_instance.__exit__ is called

    class MyClass:
        def __init__(self):
         ...
        def __enter__(self):
            reutrn obj
        def __exit__(self, + ...):
            # clean up obj

    Scope of with block
        The with block is not like a function or a comprehension
        The scope of anything in the with block( including the object returned from __enter___)
        is the same scope as the with statement itself

    with open(fname) as f: -> f is a symbol in global scope
        row = next(f)    -> row is also in the global scope

    print(f) -> f is closed but the symbol exists
    print(row) -> row is available and has a value

    The __enter__ Method

        def __enter__(self):

        This method should perform whatever setup it needs to
        It can optionallu return an object -> as returned_obj

    The __exit__ Mehtod

    __exit__ is similar to the finally in a try statement -> runs even if an exception occurs in with block

    But should it handle things differently if an exception occurred?
    -> maybe -> so it needs to know about any exceptions that occurred
             -> it also needs to tell Python whether to silence the exception, or let it propagate


    with MyContext() as obj:
        raise ValueError
    print('done')

    Scenario 1

        __exit__ recives error, performs some clean up and silences error - print statement runs no exception is seen

    Scenario 2
        __exit__ recives error, performs some clean up and let's error propagate - print statement does not run the Value Exception is seen

    Needs three arguments: -> the exception type that occured (if any, None otherwise)
                           -> the exception value that occurred (if any, None otherwise)
                           -> the traceback object if an exception occurred (if any, None otherwise)
    Returns True or False: -> True = silence any raised exception
                           -> False = do not silence a raised exception

    def __exit__(self, exc_type, exc_value, exc_trace):
        # do clean up work here
        return True # or False
"""

try:
    10 / 2
except ZeroDivisionError:
    print('Zero Division exception occured')
finally:
    print('finally ran!')

try:
    10 / 0
except ZeroDivisionError:
    print('Zero Division exception occured')
finally:
    print('finally ran!')

def my_func():
    try:
        10 / 0
    except ZeroDivisionError:
        return
    finally:
        print('finally ran!')

my_func() # finally still ran

try:
    print('Opening file')
    f = open('text.txt', 'w')
    a = 1/0
except:
    print("an exception occured") # finally will still run even if we don't use except
finally:
    print("Closing file")
    f.close()

with open('text.txt', 'w') as file:
    print("inside with is the file closed?", file.closed) # False
    file.write("This is a test")

print("After with: is file closed", file.closed) # True

def test():
    with open('text.txt', 'w') as file:
        print('inside with: file closed?', file.closed) # False
        return file
        print('here will never run')

file = test()
print(file.closed)#True

with open('text.txt', 'w') as f:
    f.writelines('this is a test')

with open('text.txt') as f:
    row = next(f)

print(f.closed) # True
print(row) # this is a test


class MyContext:
    def __init__(self):
        self.obj = None

    def __enter__(self):
        print('entering context...')
        self.obj = 'The Return object'
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exiting context...')
        if exc_type:
            print(f'Error occured: {exc_type}, {exc_val}')
        return True

ctx = MyContext()
print('created context ...')
with ctx as obj: # with does not have it's own scope
    print('inside with block', obj)
    raise ValueError('custom message')

print(obj) # The Return object


class Resource:
    def __init__(self, name):
        self.name = name
        self.state = None

class ResourceManager:
    def __init__(self, name):
        self.name = name
        self.resource = None

    def __enter__(self):
        print('entering context')
        self.resource = Resource(self.name)
        self.resource.state = 'created'
        return self.resource

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exitting context')
        self.resource.state = 'destroyed'
        if exc_type:
            print('error occured')
        return False

with ResourceManager('spam') as res:
    print(f'{res.name} = {res.state}') # spam = created

print(f'{res.name} = {res.state}') # spam = destroyed

print('res' in globals()) # True


class File:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def __enter__(self):
        print('opening file ...')
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('closing file...')
        self.file.close()
        return False

with File('text.txt', 'w') as f:
    f.write('This is a late parrot!')

with File('text.txt', 'r') as f:
    print(f.readlines())

def test():
    with File('text.txt', 'w') as f:
        f.write('This is a late parrot!')
        return f

f = test() # closing file still run


class File:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def __enter__(self):
        print('opening file ...')
        self.file = open(self.name, self.mode)
        return self # return the instance of file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('closing file...')
        self.file.close()
        return False

with File('text.txt', 'r') as file_ctx: # after as is the instance of whatever is returned by enter method
    print(next(file_ctx.file))
    print(file_ctx.name)
    print(file_ctx.mode)