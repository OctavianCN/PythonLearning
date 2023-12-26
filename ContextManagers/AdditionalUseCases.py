import decimal

print(decimal.getcontext())  # we can see the setting of this context

decimal.getcontext().prec = 14

print(decimal.getcontext())

decimal.getcontext().prec = 28  # set back the to old value

old_prec = decimal.getcontext().prec

decimal.getcontext().prec = 4

print(decimal.Decimal(1) / decimal.Decimal(3))

decimal.getcontext().prec = old_prec

print(decimal.Decimal(1) / decimal.Decimal(3))


class Precision:  # this is a change reset context manager (this was just for the precision)
    def __init__(self, prec):
        self.prec = prec
        self.current_prec = decimal.getcontext().prec

    def __enter__(self):
        decimal.getcontext().prec = self.prec

    def __exit__(self, exc_type, exc_val, exc_tb):
        decimal.getcontext().prec = self.current_prec
        return False


with Precision(3):
    print(decimal.Decimal(1) / decimal.Decimal(3))

print(decimal.Decimal(1) / decimal.Decimal(3))

with decimal.localcontext() as ctx:  # decimal already have a context manager (change reset context manager)
    ctx.prec = 3
    print(decimal.Decimal(1) / decimal.Decimal(3))

print(decimal.Decimal(1) / decimal.Decimal(3))

from time import perf_counter, sleep


# Another way to use context managers
class Timer:
    def __init__(self):
        self.elapsed = 0

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = perf_counter()
        self.elapsed = self.stop - self.start
        return False


with Timer() as timer:
    sleep(1)

print(timer.elapsed)

print('hello')

import sys


class OutToFile:
    def __init__(self, fname):
        self._fname = fname
        self._current_stdout = sys.stdout

    def __enter__(self):
        self._file = open(self._fname, 'w')
        sys.stdout = self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self._current_stdout
        self._file.close()
        return False


with OutToFile(
        'test.text'):  # we are not using as because we do not return anything (if we would use it, it would just be None because None is returned by default)
    print(sys.stdout)
    print('Line 1')  # it does not print anything in the console it just print it to the file
    print('Line 2')

print(sys.stdout)


class Tag:
    def __init__(self, tag):
        self._tag = tag

    def __enter__(self):
        print(f'<{self._tag}>', end='')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'</{self._tag}>', end='')


with Tag('p'):
    print('some', end='')
    with Tag('b'):
        print('bold', end='')
    print(' text', end='')

"""
Title
-Items 1
   - sub item 1a
   - sub item 1b
-Items 2
   - sub item 2a
   - sub item 2b
"""
print("")

class ListMaker:
    def __init__(self, title, prefix="- ", indent=3):
        self._title = title
        self._prefix = prefix
        self._indent = indent
        self._current_indent = 0
        print(title)

    def __enter__(self):
        self._current_indent += self._indent
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._current_indent -= self._indent
        return False

    def print(self, arg):
        s = ' ' * self._current_indent + self._prefix + str(arg)
        print(s)  # it is not infinite recursive because if i don't say self.print it looks in global scope first


with ListMaker('Items') as lm:
    lm.print('Item 1')
    with lm:
        lm.print('Item 1.a')
        lm.print('Item 1.b')
    lm.print('Item 2')
    with lm:
        lm.print('Item 2.a')
