###########Arguments vs Parameters#################

def my_func(a,b): # a and b are parameters of my_func and are local to my_func
    print(id(a)) # same as x
    print(id(b)) # same as y
    pass

x = 10
y = 'a'
print(id(x))
print(id(y))
my_func(x,y) # x and y are called arguments of my_func
             # also x and y are passed by reference
             # i.e the memory addresses of x and y are passed

#####################Positional and Keyword Arguments####################

#Most common way of assigning argumets to parameters via order in which are passwd

my_func(10,20) # a=10 b=20
my_func(20,10) # a=20 b=10

#Default values
def my_func(a,b=100):
    pass

my_func(10,20)
my_func(5)

#def my_func(a,b=100,c): WRONG cannot be like that
#    pass

# If a positional parameter is defined with a default value
# every positional parameter after it must also be given a default value

def my_func(a,b=10,c=5):
    pass

my_func(a=1,c=2) # keyword arguments (named arguments)
my_func(1,c=2) # position argument + keyword arguments
my_func(c=3,a=1,b=2)

#my_func(c=1,2,3) WRONG after you use a named argument everything after should be named

