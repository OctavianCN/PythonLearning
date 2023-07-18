
from collections import namedtuple

file_name = "nyc_parking_tickets_extract.csv"

with open(file_name) as f:
    column_headers = next(f).strip('\n').split(',')
    sample_data = next(f).strip('\n').split(',')
    column_names = [header.replace(' ','_').lower()
                    for header in column_headers]
    print(list(zip(column_names,sample_data)))

Ticket = namedtuple('Tickets', column_names)

with open(file_name) as f:
    next(f)
    raw_data_row = next(f)

def read_data():
    with open(file_name) as f:
        next(f)
        yield from f

def parse_int(value, *, default=None):
    try:
        return int(value)
    except ValueError:
        return default

from datetime import datetime

def parse_date(value, *, default=None):
    date_format = '%m/%d/%Y'
    try:
        return datetime.strptime(value,date_format).date()
    except ValueError:
        return default

def parse_string(value, *, default=None):
    try:
        cleaned = value.strip()
        if not cleaned:
            return default
        else:
            return cleaned
    except ValueError:
        return default

from functools import partial

column_parsers = (parse_int,
                  parse_string,
                  lambda x: parse_string(x, default=''),
                  partial(parse_string, default=''),
                  parse_date,
                  parse_int,
                  partial(parse_string, default=''),
                  parse_string,
                  lambda x: parse_string(x, default=''))


def parse_row(row, *, default=None):
    fields = row.strip('\n').split(',')
    parsed_data = \
        [func(field) for func, field in zip(column_parsers, fields)]
    if all(item is not None for item in parsed_data):
        return Ticket(*parsed_data)
    else:
        return default



rows = read_data()

for _ in range(5):
    row = next(rows)
    parsed_data = parse_row(row)
    print(parsed_data)

print(all([10, 'hello'])) # if all True return true
print(all([10, 'hello', None])) # if one Flase return None

for row in read_data():
    parsed_row = parse_row(row)
    if parsed_row is None:
        print(list(zip(column_names,row.strip('\n').split(','))),
              end='\n\n')


def parsed_data():
    for row in read_data():
        parsed = parse_row(row)
        if parsed:
            yield parsed

parsed_row = parsed_data()
for _ in range(5):
    print(next(parsed_row))

makes_counts = {}

for data in parsed_data():
    if data.vehicle_make in makes_counts:
        makes_counts[data.vehicle_make] += 1
    else:
        makes_counts[data.vehicle_make] = 1

for make, cnt in sorted(makes_counts.items(),
                        key=lambda  t: t[1],
                        reverse=True):
    print(make,cnt)


from collections import defaultdict

d  = defaultdict(str) # if the key does not exists it will automatically make the value empty string

d['a'] = 1
print(d['a'])
print(d['b']) # return empty string

makes_counts = defaultdict(int) # now the default value is 0

for data in parsed_data():
    makes_counts[data.vehicle_make] += 1

for make, cnt in sorted(makes_counts.items(),
                        key=lambda  t: t[1],
                        reverse=True):
    print(make,cnt)

def violation_count_by_make():
    makes_counts = defaultdict(int)  # now the default value is 0

    for data in parsed_data():
        makes_counts[data.vehicle_make] += 1

    return { make: cnt
             for make, cnt in sorted(makes_counts.items(),
                                            key=lambda t: t[1],
                                            reverse=True) } # we transofrm the tuple in a dictionary

print(violation_count_by_make())

