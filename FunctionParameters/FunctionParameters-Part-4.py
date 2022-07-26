###### *args #####

#function parameters similar to unpacking
def func(a,b,*c): # accept two or more param when we call func 1 (minimum 2 param)
    print(a) # 1
    print(b) # 2
    print(c) # tuple(3,4,5,6) (instead of list on unpacking with *)
    pass
# convention *args instead of *c
func(1,2,3,4,5,6)
func(1,2)
# You cannot add more positional arguments after *args

def func1(a,b,*args,d): # it is OK defined because after positional args we get
    pass                #keyword arguments

#func1(10,20,'a','b',100) # won't work a call like this

def func2(a,b,c):
    pass

l = [10,20,30]
#func2(l) not working
func2(*l) # works

def avg(*args):
    count = len(args)
    total = sum(args)
    return count and total/count # if count is 0 then it is false false and anything is false then it returns 0

print(avg(1,4,5,2))

### Keyword Arguments ##########

# positional parameters can optionally be passwd as named keyword arguments

def func(a,b,c):
    pass

func(1,2,3) # positional param
func(a = 1, c = 3, b = 2) #keyword arguments (optional here)

def func(a,b,*args, d): # a,b mandatory pos args , *args exhaust positional args
    pass                 # d is a mandatory keyword argument

func(1,2,'a','b',d=100) # works
# func(1,2) fails
# func(1,2,3) fails

def func(*args,d):
    pass
func(1,2,3,d=100)
func(d=100)

def func(*,d): # no positional arguments at all
    pass
func(d = 100)
#func(1,2,3,d=100)# won't work it will give exception

def func(a,b=1,*,d,e=True): # a mandatory pos argument(can be named if wanted)
    pass                    # b optional pos argumet
                            # * no additional pos arguments
                            # d mandatory keyword argument
                            # e optional keyword argument





