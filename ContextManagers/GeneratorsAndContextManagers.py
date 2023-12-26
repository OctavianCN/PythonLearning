"""
Use generators with context managers
"""

# def my_gen():
#     try:
#         print("creating context and yielding object")
#         yield [1,2,3,4]
#     finally:
#         print("exiting context and cleaning up")
#
# gen = my_gen()
# lst = next(gen)
# next(lst) # also get stop iteration exception but it executes finally

def my_gen():
    try:
        print("creating context and yielding object")
        yield [1,2,3,4]
    finally:
        print("exiting context and cleaning up")

gen = my_gen()
lst = next(gen)
print(lst)
try:
    next(gen)
except StopIteration:
    pass

print("---------------------------------")
class GenCtxManager:
    def __init__(self, gen_func):
        self._gen = gen_func()

    def __enter__(self):
        return next(self._gen)

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            next(self._gen)
        except StopIteration:
            pass
        return False

with GenCtxManager(my_gen) as obj:
    print(obj)



print("---------------------------------")
class GenCtxManager:
    def __init__(self, gen_func, *args, **kwargs):
        self._gen = gen_func(*args, **kwargs)

    def __enter__(self):
        return next(self._gen)

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            next(self._gen)
        except StopIteration:
            pass
        return False

def open_file(fname,mode):
    f = open(fname,mode)
    try:
        print("Opening file")
        yield f
    finally:
        print("Closing file")
        f.close()

with GenCtxManager(open_file, 'test.text', 'w') as f:
    f.writelines('testing...')
