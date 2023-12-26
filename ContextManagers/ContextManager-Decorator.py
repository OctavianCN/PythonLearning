"""
Using Decorators to Create Cotext Maagers using Generator Functions
"""

def open_file(fname, mode='r'):
    print('Opening file...')
    f = open(fname,mode)
    try:
        yield f
    finally:
        print('Closing file...')
        f.close()

class GenContextManager:
    def __init__(self, gen):
        self._gen = gen

    def __enter__(self):
        print('Calling ext to get the yielded value from generator')
        return next(self._gen)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Calling next to perform cleanup into generator')
        try:
            next(self._gen)
        except StopIteration:
            pass
        return False

file_gen = open_file('txta.txt', 'w')

with GenContextManager(file_gen) as f:
    f.writelines('Test')


def context_manager_decorator(gen_fn):
    def helper(*args, **kwargs):
        gen = gen_fn(*args,**kwargs)
        ctx = GenContextManager(gen)
        return ctx
    return helper

@context_manager_decorator
def open_file(fname, mode='r'):
    print('Opening file...')
    f = open(fname,mode)
    try:
        yield f
    finally:
        print('Closing file...')
        f.close()

# open_file = context_manager_decorator(open_file)

with open_file('txta.txt') as f:
    print(f.readlines())

from contextlib import contextmanager

@contextmanager
def open_file(fname, mode='r'):
    print('Opening file...')
    f = open(fname,mode)
    try:
        yield f
    finally:
        print('Closing file...')
        f.close()

with open_file('txta.txt') as f:
    print(f.readlines())


from time import perf_counter, sleep

@contextmanager
def timer():
    stats = dict()
    start = perf_counter()
    stats['start'] = start
    try:
        yield stats
    finally:
        end = perf_counter()
        stats['end'] = end
        stats['elapsed'] = end - start

with timer() as stats:
    sleep(2)

print(stats)

"""
We can use the decorator to decorate any generator  that has that format and turn it into a context manager
"""