####Putting It All Together###########

# Examples for *args and **kwargs
#           - print() - function uses it

print(1,2,3,sep='#',end='!')
print() # for \n
def func(a,b, *args):
    print(a,b,args)

func(1,2,'x','y','z')

# func(a=1,b=2,'x','y','z') - syntax error positional arguments follows keyword arguments

def func(a,b=2,c=3,*args): #
    print(a,b,c,args)

func(1,2,3,'x','y','z') # works as expected

#func(1,c=5,'x','y','z') Not working
#Rules: Positional arguments first and after that keyword arguments

func(1,c=5) # works but cannot pass more values

def func(a,b=2,*args,c=3,d):
    print(a,b,args,c,d)

func(10,20,'x','y','z',c=4,d=1)

#func(1,'x','y','z',b=4,d=10) - ERROR - multiple values for b

def func(a,b,*args,c=10,d=20,**kwargs):
    print(a,b,args,c,d,kwargs)

func(1,2,'x','y','z',c=100,d=200,x=0.1,y=0.2)

def calc_hi_lo_avg(*args, log_to_console=False):
    hi = int(bool(args)) and max(args) # if args is empty then bool(args) = False and I can convert it to int to 0
    lo = min(args) if len(args) > 0 else 0
    avg = (hi + lo) / 2
    if log_to_console:
        print("high = {0}, low = {1}, avg = {2}".format(hi,lo,avg))
    return avg

avg = calc_hi_lo_avg(1,2,3,4,5)
avg = calc_hi_lo_avg(1,2,3,4,5,log_to_console=True)