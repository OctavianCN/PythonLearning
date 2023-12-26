"""
### Project

For this project you are given a file that contains
 some parking ticket violations for NYC.

For this sample data set, the file is named:
```
nyc_parking_tickets_extract.csv
```

Goals:

##### Goal 1
Create a lazy iterator that will return a named tuple of
the data in each row. The data types should be appropriate
- i.e. if the column is a date, you should be storing dates
in the named tuple, if the field is an integer, then it
 should be stored as an integer, etc.

##### Goal 2

Calculate the number of violations by car make.

##### Note:
Try to use lazy evaluation as much as possible -
it may not always be possible though! That's OK, as long as it's kept to a minimum.

"""
from collections import namedtuple
from datetime import datetime


def creating_tuple(file_name,tuple_name):
    file = open(file_name, "r")
    line = next(file)
    line = line.strip('\n')
    attributes = ["_".join(word.split(" ")) for word in line.split(",")]
    file.close()
    return namedtuple(tuple_name, attributes)

def check_and_convert(data):
    try:
        # Try converting to a date
        date_obj = datetime.strptime(data, "%m/%d/%Y")
        return date_obj.date()  # Return the date object if successful
    except ValueError:
        try:
            # Try converting to an integer
            return int(data)
        except ValueError:
            # If all conversion attempts fail, treat it as a string
            return data

def function_gen(file_name):
    with open(file_name) as f:
        next(f) # skip firs_line
        for line in f:
            my_list = line.strip('\n').split(",")
            my_new_list = []
            for data in my_list:
                new_data = check_and_convert(data)
                my_new_list.append(new_data)
            print(my_new_list)
            my_tuple = Tickets(*my_new_list)
            yield my_tuple

file = "nyc_parking_tickets_extract.csv"
Tickets = creating_tuple(file, "Tickets")
print(Tickets._fields)

my_func = function_gen(file)
print(type(my_func))
print(next(my_func))
a = next(my_func)
print(type(a.Issue_Date))
print(type(a.Violation_Code))