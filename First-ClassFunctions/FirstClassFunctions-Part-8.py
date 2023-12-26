##### Reducing Function Arguments #######

def my_func(a,b,c):
    print(a,b,c)

def fn(b,c):
    return my_func(10,b,c)

fn(20,30)

# Instead of this use this

from functools import partial

f = partial(my_func, 10)
f(20,30)

def my_func(a,b,*args, k1, k2, **kwargs):
    print(a,b,args,k1,k2,kwargs)

f = partial(my_func, 10, k1 = 'a')
f(2,3,k2 = 10, f1= 15, f2 = 16)

def pow(base, exponent):
    return base ** exponent

square = partial(pow, exponent = 2)
print(square(5))
print(square(base = 10))
print(square(5, exponent = 3)) # Overwrite exponent

def my_func(a,b,c):
    print(a,b,c)
a = 10
f = partial(my_func, a)
f(20,30) # 10 20 30
a = 100
f(20,30)# still 10 20 30 partial still points to the memory address of 10

# if a is mutable than everything is changing
a = [1,2,3]
f = partial(my_func, a)
f(20,30) # [1,2,3] 20 30
a[0] = 10
f(20,30)# [10,2,3] 20 30
a.append(100)
f(20,30)# [10,2,3,100] 20 30