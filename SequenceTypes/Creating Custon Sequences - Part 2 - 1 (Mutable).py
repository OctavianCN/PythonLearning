# Custom Sequences

class MyClass:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'MyClass (name = {self.name})'
    def __add__(self, other):
        print(f'You called + on {self} and {other}')
        return 'Hello from __add__'
    def __iadd__(self, other):
        print(f'You called += on {self} and {other}')
        return 'Hello from __iadd__'

c1 = MyClass('instance 1')
c2 = MyClass('instance 2')
print(c1 + c2)
print(id(c1))
c1 += c2
print(c1)
print(id(c1)) # id changed

class MyClass:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'MyClass (name = {self.name})'

    def __add__(self, other):
        return MyClass(self.name + other.name)

    def __iadd__(self, other):
        if isinstance(other, MyClass):
            self.name += other.name
        else:
            self.name += other
        return self

    def __mul__(self, n):
        return MyClass(self.name * n)

    def __imul__(self, n):
        self.name *= n
        return self

c1 = MyClass('Eric')
c2 = MyClass('Idle')
print(id(c1))
print(id(c2))
result = c1 + c2
print(id(result),result)
c1 += c2
print(id(c1),c1)

c3 = MyClass('Eric')
print(id(c3))
result = c3 * 3
print(id(result), result)
c3 *= 3
print(id(c3), result)

c1 = MyClass('Eric')
#print(3 * c1) -exception
# Python tries first to do:
print((3).__mul__(c1)) # Not Implemented
# and then
#print(c1.__rmul__(3)) - exception

class MyClass:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'MyClass (name = {self.name})'

    def __add__(self, other):
        return MyClass(self.name + other.name)

    def __iadd__(self, other):
        if isinstance(other, MyClass):
            self.name += other.name
        else:
            self.name += other
        return self
    def __mul__(self, n):
        return MyClass(self.name * n)

    def __rmul__(self, n):
        return self.__mul__(n)
    def __imul__(self, n):
        self.name *= n
        return self

    def __contains__(self, item): # implement in operator
        return item in self.name

c1 = MyClass('Eric')
print(3 * c1) # Now it works

c1 = MyClass('Eric Idle')

print('Eric' in c1)



