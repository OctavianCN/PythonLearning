########### Parametrized Decorators ####################


def timed(fn):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(10): # here 10 is hardcoded and we don't want to hardcode the values
            start = perf_counter()
            result = fn(*args,**kwargs)
            end = perf_counter()
            total_elapsed += (end - start)
        avg_run_time = total_elapsed / 10
        print('Avg run time: {0:.6f}s'.format(avg_run_time))
        return result
    return inner

def calc_fib_recurse(n):
    return 1 if n < 3 else calc_fib_recurse(n-2) + calc_fib_recurse(n-1)

#@timed
def fib(n):
    return calc_fib_recurse(n)

fib = timed(fib)

print(fib(30))
###########################################################################
def timed(fn, reps):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(reps):
            start = perf_counter()
            result = fn(*args,**kwargs)
            end = perf_counter()
            total_elapsed += (end - start)
        avg_run_time = total_elapsed / reps
        print('Avg run time: {0:.6f}s ({1} reps)'.format(avg_run_time,reps))
        return result
    return inner

#@timed(5) - not working because it actually call timed(5,fib) and it is not working
def fib(n):
    return calc_fib_recurse(n)

fib = timed(fib, 5) # it works
print(fib(28))


################################################################
# We have to create a decoretor factory in order to parametrize the decorator

# decorator running order
def dec(fn):
    print("running dec")

    def inner(*args, **kwargs):
        print("running inner")
        return fn(args,kwargs)

    return inner

@dec # this will be called when run and prints only running dec
def my_func():
    print("running my_func")

def dec_factory():
    print("running dec factory")
    def dec(fn):
        print("running dec")

        def inner(*args, **kwargs):
            print("running inner")
            return fn(args, kwargs)

        return inner
    return dec

dec = dec_factory() # dec will be the decorator returned by dec_factory
                    # and it will print only running dec facotry

@dec_factory() # you need to call the dec_factory in order to get the decorator frum the factory
def my_func():
    print("Running my_func")

# my_func = dec_factory()(my_func) - get the decorator and call my func


def dec_factory(a, b): # added the parameters to the decorator function
    print("running dec factory")
    def dec(fn):
        print("running dec")

        def inner(*args, **kwargs):
            print("running inner")
            print("a = {0}, b= {1}".format(a,b))  #  a, b free variables
            return fn(*args, **kwargs)

        return inner
    return dec

dec = dec_factory

@dec_factory(10,20)
def my_func():
    print("running my_func")

my_func()

@dec(5,15) # works the same as before
def my_func():
    print("running my_func")

my_func()


def my_func():
    print("running my_func")

my_func = dec_factory(250,150)(my_func)  # also works the same as before

my_func()

def timed(reps):  # timed is the factory not the decorator it just returns a decorator
    def dec(fn):
        from time import perf_counter

        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(reps):
                start = perf_counter()
                result = fn(*args,**kwargs)
                end = perf_counter()
                total_elapsed += (end - start)
            avg_run_time = total_elapsed / reps
            print('Avg run time: {0:.6f}s ({1} reps)'.format(avg_run_time,reps))
            return result
        return inner
    return dec


@timed(15)  # now it works
def fib(n):
    return calc_fib_recurse(n)

print(fib(28))
