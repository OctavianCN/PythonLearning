### Lambda Expressions ###

def sq(x):
    return x**2

print(type(sq))
print(sq)

# is a function in the memory
print(lambda x: x**2) # cannot put annotation or comments inside

f = sq
print(f is sq) # true
print(f(3)) # is a callable

f = lambda x: x**2
print(f)
print(f(3)) # f is callable

g = lambda x, y=10: x+y

print(g(1))

f = lambda x, *args, y, **kwargs: (x,args,y,kwargs)
print(f(1,'a','b',y=100,a=10,b=20))

def apply_func(x, fn):
    return fn(x)

print(apply_func(3, sq))
print(apply_func(3, lambda x: x**2))
print(apply_func(3, lambda x: x**3))

def apply_func(fn, *args, **kwargs):
    return fn(*args, **kwargs)

print(apply_func(sq, 3))
print(apply_func(lambda x: x**2, 3))
print(apply_func(lambda x,y: x+y, 1, 2))
print(apply_func(lambda x,*,y: x+y, 1, y= 20))
print(apply_func(lambda *args:sum(args), 1, 2,3,4,5))

print(apply_func(sum,(1,2,3,4,5)))



