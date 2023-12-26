########### Decorator Application - Decorator Class ##################

def my_dec(a,b):
    def dec(fn):
        def inner(*args, **kwargs):
            print("decorated function called a = {0}, b = {1}".format(a,b))
            return fn(*args,**kwargs)
        return inner
    return dec

@my_dec(10,20)
def my_func(s):
    print("Hello {0}".format(s))

my_func("World")


class MyClass:
    def __init__(self,a, b):
        self.a = a
        self.b = b
    def __call__(self, c):
        print("Called a= {0}, b={1}, c= {2}".format(self.a, self.b, c))

obj = MyClass(10,20)
print(type(obj)) # obj an instance of MyClass

obj(100) # object is callable because it have __call__


class MyClass:
    def __init__(self,a, b):
        self.a = a
        self.b = b
    def __call__(self, fn): # this is the decorator of the class My_Calass
        def inner(*args, **kwargs):
            print("decorated function called a = {0}, b = {1}".format(self.a,self.b))
            return fn(*args,**kwargs)
        return inner

@MyClass(10,20) # we decorated my func using MyClass
def my_func(s):
    print("Hello {0}".format(s))

my_func("World")

obj = MyClass(10,20)
def my_func(s):
    print("Hello {0}".format(s))

my_func = obj(my_func) #we can use the fact that a class is callable in order to decorate functions
my_func("World")