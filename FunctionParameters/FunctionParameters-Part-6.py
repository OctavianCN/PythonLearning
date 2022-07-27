# A Simple Function Timer


import time

def time_it(fn, *args, rep = 1, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args,**kwargs) # here we unpack the tuple and the dictionary
    end = time.perf_counter()
    return (end-start)/rep

print(time_it(print, 1,2,3,sep=' - ',end=' *** \n',rep=5))

def compute_powers_1(n, *, start=1,end):
    # using a for loop
    results = []
    for i in range(start,end):
        results.append(n**i)
    return results

def compute_powers_2(n, *, start=1,end):
    # using list comprehesion
    return [n**i for i in range(start,end)]

def compute_powers_3(n, *, start=1,end):
    # using generators expresion
    return (n**i for i in range(start,end))

print(compute_powers_1(2,end=5))
print(compute_powers_2(2,end=5))
print(list(compute_powers_3(2,end=5)))

print(time_it(compute_powers_1,2,start=0,end=20000,rep=5))
print(time_it(compute_powers_2,n=2,start=0,end=20000,rep=5))
print(time_it(compute_powers_3,2,start=0,end=20000,rep=5))