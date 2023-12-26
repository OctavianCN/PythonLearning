######### Global and Local Scopes ##########
# python first verify current scope (and then the other scopes) last scope is built in scope
a = 10 # here is in module scope (global scope)
# print -> is in built in scope
print(a)

def my_func(n):
    c = n**2 # c is local scope to my func
    return c

def my_func(n):
    print('global a:', a) # if a not found in this scope it searches in the scope above it(in global scope and then in the built in scope and then return error)
    c = a**n
    return c

print(my_func(2))

def my_func(n):
    a = 20 # here creates another label named a in local scope with value 20 (not the same a as in global scope)
    c = a**n
    return c
print(a) # here is global a
print(my_func(2))
print(a) # is still a = 10

def my_func(n):
    global a # here you tell python that you will refer to the global label a
    a = 20 # here it change the refference of global a
    c = a**n
    return c
print(a) # a = 10
my_func(2)
print(a) # a = 20

def my_func():
    global var
    var = 'hello world'
    return

#print(var)-> error
my_func()
print(var) # now var exists after my_func is called

a = 10

def my_func():
    global a
    a = 'hello'
    print('global a:', a)

my_func()
print(a) # hello

# a = 10
# def my_func():
#     print('global a:', a) # error python see a local a (at compile time python see a and think it is local) in the function so it detects that a was refferenced before the assignment
#     a = 'hello world'
#     print(a)
#
# my_func()
# print(a)

print(True) # python looks for print and true in the module scope first and then in the built in scope else error

def print(x):
    return 'hello {0}'.format(x)

print('world') # here we lost the print function because we defined above so it takes the print from this scope

del print # we got print back by deleting our prin function
print('Hello World')

for i in range(10):
    x = 2*i
print(x)  # x exists because we created in for statement