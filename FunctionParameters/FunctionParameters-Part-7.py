######Parameter Defaults Notes########


#When a module is loaded: all code is executed immediately

#Module code:

a = 10 # the integer object 10 is created and a references it

def func(a): # the function object is created, and func references it
    print(a)

func(a) # the function is executed

#Module code:

def func(a=10): # the function object is created and func refferences it
    print(a)    # the integer object 10 is evaluated/created and is assigned as the
                # default of a

func() # the fuction is executed
       # by the time this happens, the default value for a has already been
       # evaluated and assigned - it is not re-evaluated when the function is called


# let's say we want to create a function with current date/time
# and set the default value datetime.utcnow()

from datetime import datetime
import time
def log(msg,*,dt = datetime.utcnow()):
    print('{0}: {1}'.format(dt,msg))
log('message 1')
#time.sleep(60)
log('message 2') # will show the same time as message 1 because
                 # dt was loaded when the function was defined

# Solution

def log(msg, *, dt = None):
    dt = dt or datetime.utcnow() # if the user ( a or b) if a is true return a else return b
    print('{0}: {1}'.format(dt, msg))

log('message 1')
#time.sleep(60)
log('message 2')

#beware of using a mutable object (or a callable) for an argument default
my_list = [1,2,3]
def func(a=my_list):
    print(a)

func()
func(['a','b'])
my_list.append(4)
func() # func print 1,2,3,4

my_tuple = (1,2,3) # use a tuple instead
def func(a=my_tuple):
    print(a)

func()
func(['a','b'])
