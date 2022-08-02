####### Closures Applications #########

class Averager:
    def __init__(self):
        self.numbers = []

    def add(self,number):
        self.numbers.append(number)
        total = sum(self.numbers)
        count = len(self.numbers)
        return total/count

a = Averager()
print(a.add(10))
print(a.add(20))
print(a.add(30))

b = Averager()
print(b.add(10))

def averager():
    numbers = []
    def add(number):
        numbers.append(number) # numbers is a non local variable
        total = sum(numbers)
        count = len(numbers)
        return total/count
    return add

a = averager()
print(a(10))
print(a(20))
print(a(30))
b = averager()
print(b(10))

print(a.__closure__) # different cell
print(b.__closure__)

def averager():
    total = 0
    count = 0
    def add(number):
        nonlocal total
        nonlocal count
        total += number
        count += 1
        return total/count
    return add

a = averager() # now we don't need to store the numbers we use closures to store previous total and count
print(a(10))
print(a(20))
print(a(30))
b = averager()
print(b(10))

print(a.__closure__) # different cells (two cells)
print(b.__closure__)


# same thing using a class
class Averager:
    def __init__(self):
        self.total = 0
        self.count = 0

    def add(self,number):
        self.total += number
        self.count += 1
        return self.total/self.count

a = Averager()
print(a.add(10))
print(a.add(20))
print(a.add(30))

b = Averager()
print(b.add(10))

############################################

from time import  perf_counter

print(perf_counter())
print(perf_counter())

class Timer:

    def __init__(self):
        self.start = perf_counter()

    # def poll(self):
    #     return perf_counter() - self.start
    def __call__(self): # made poll callable
        return perf_counter() - self.start

t1 = Timer()
# print(t1.poll())
# print(t1.poll())
print(t1())
print(t1())

# same thing but with closures (most of the times simpler code)
def timer():
    start = perf_counter()
    def poll():
        return perf_counter() - start
    return poll

t2 = timer()
print(t2())
print(t2())
