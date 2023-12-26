##############Named Tuples - Application - Alternative to Dictionaries############

data_dict = dict(key1= 100, key2= 200, key3= 300)
print(data_dict['key1'])

from collections import namedtuple

Data = namedtuple('Data', data_dict.keys()) # from python 3.7 the order of keys is guaranteed

print(Data._fields)

d1 = Data(*data_dict.values()) # Data not taking an iterable it takes values
print(d1)

d2 = Data(key1=10, key3=30, key2=20)
print(d2)

Data = namedtuple('Data', 'key3 key2 key1')
print(Data._fields)
d2 = Data(*data_dict.values()) # here unpack as positional arguments
print(d2)
d2 = Data(**data_dict) # here unpack as keyword arguments
print(d2)

key_name = 'key2'
print(data_dict[key_name])
print(getattr(d2, key_name))

print(data_dict.get('key10',None))
print(getattr(d2,'key10',None))

# Convert a list of dictionaries to a list of named_tuples

data_list = [
    {'key2': 1, 'key1': 2},
    {'key1': 3, 'key2': 4},
    {'key1': 5, 'key2': 6, 'key3': 7},
    {'key2': 100}
]

keys  = set() # sets have unique values and we will use it to have all possible keys

for d in data_list:
    for key in d.keys():
        keys.add(key)

print(keys) #  sets have different order

keys = {key for dict_ in data_list for key in dict_.keys()} # set comprehension
print(keys)

Struct = namedtuple('Struct', sorted(keys))
print(Struct._fields)
Struct.__new__.__defaults__ = (None, )* len(Struct._fields)

tuple_list = []
for dict_ in data_list:
    tuple_list.append(Struct(**dict_))
print(tuple_list)

def tuplify_dicts(dicts):
    keys = keys = {key for dict_ in dicts for key in dict_.keys()}
    Struct = namedtuple('Struct', sorted(keys), rename=True)
    Struct.__new__.__defaults__ = (None,) * len(Struct._fields)
    return [Struct(**dict_) for dict_ in dicts]

tuple_list = tuplify_dicts(data_list)
print(tuple_list)