"""
Common Operations
"""

d = dict(zip('abc',range(1, 4)))

print(d)
print(len(d))
print(d['a'])
print(d.get('a'))
print(d.get('k')) # None

print(d.get('k', 'N/A')) # N/A
print(d.get('a', 'N/A')) # a

text = "sdasd dajisdoj  asdioasjdos  asjdioasjdi as8jdasjd oi jdwio dwjowjeBSDA AIDISDAjdsajidaj ASAAo"

counts = dict()
for c in text:
    counts[c] = counts.get(c, 0) + 1

print(counts)


counts = dict()
for c in text:
    key = c.lower().strip()
    if key:
        counts[key] = counts.get(key, 0) + 1

print(counts)

d = dict(a=1, b=2, c = 3)

print('a' in d) # True

d = dict.fromkeys('abcd', 0)

print(d)

del d['a']

print(d)

#del d['z']  # KEY Error

result = d.pop('b')
print(result) # 0 - is the value that b had
print(d)  # b is removed

#d.pop('z') - error

d = {'a': 1, 'b': 2}

print(d.pop('a', 100)) # 1
print(d.pop('z', 100)) # 100
print(d)

d = dict({i: i**2 for i in range(1, 5)})

print(d)
print(d.popitem()) # (4, 16) - remove last item and retuurns tuple key value
print(d)


d = {'a': 1, 'b': 2, 'c': 3}

def insert_if_not_present(d, key, value):
    if key not in d:
        d[key] = value
        return value
    else:
        return d[key]

print(d)

insert_if_not_present(d, 'z', 100)
insert_if_not_present(d, 'z', 10)
print(d)

d = dict(zip('abc', range(1, 4)))

print(d)

d.setdefault('a', 100)

print(d) # no changes because a is already present

d.setdefault('d', -10)
print(d) #d is added

text = "sdasd dajisdoj  asdioas-0213-jdosfs f... sse==--=w-;;;f'sg- wesasjdioasjdi as8jdasjd oi jdwio dwjowjeBSDA AIDISDAjdsajidaj ASAAo"

counts = dict()
for c in text:
    key = c.lower().strip()
    if key:
        counts[key] = counts.get(key, 0) + 1

import string

categories = {}

for c in text:
    if c != ' ':
        if c in string.ascii_lowercase:
            key = 'lower'
        elif c in string.ascii_uppercase:
            key = 'upper'
        else:
            key = 'other'

        if key not in categories:
            categories[key] = set()

        categories[key].add(c)

for cat in categories:
    print(f'{cat}: ', ''.join(categories[cat]))


for c in text:
    if c != ' ':
        if c in string.ascii_lowercase:
            key = 'lower'
        elif c in string.ascii_uppercase:
            key = 'upper'
        else:
            key = 'other'

        categories.setdefault(key, set()).add(c)


for cat in categories:
    print(f'{cat}: ', ''.join(categories[cat]))


def cat_key(c):
    categories = {' ': None,
                  string.ascii_lowercase: 'lower',
                  string.ascii_uppercase: 'upper'}
    for key in categories:
        if c in key:
            return categories[key]
    else:
        return 'other'

print(cat_key('a'))
print(cat_key('A'))
print(cat_key('-'))


from itertools import chain

def cat_key(c):
    cat_1 = {' ': None}
    cat_2 = dict.fromkeys(string.ascii_lowercase, 'lower')
    cat_3 = dict.fromkeys(string.ascii_uppercase, 'upper')
    categories = dict(chain(cat_1.items(),cat_2.items(), cat_3.items()))
    return categories.get(c, 'other')

print(cat_key('a'), cat_key('A'), cat_key(':'),cat_key(' '))


print(id(d)) # different id 4366706880

d= {} # the items of the dict are not cleared

print(id(d)) # different id 4367394112

d= dict(zip('abc', 'def'))

print(id(d)) #same id 4367393984
d.clear()
print(id(d)) #same id 4367393984