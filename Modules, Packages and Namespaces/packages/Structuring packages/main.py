import common.validators.boolean
import common.validators.dates
import common.validators.json
import common.validators.numeric
from common.validators.numeric import  is_numeric, is_integer # to import just the functions


common.validators.json.is_json('{}')
common.validators.dates.is_date('2018-01-01')

print('\n\n********** self *********')
# for k in globals().keys():
#     print(k) Error the dictionary change size during iteration (because k is changing)

for k in dict(globals()).keys():
    print(k) # here we  have common

print('\n\n********* common ***********')

for k in common.__dict__.keys():
    print(k) # here we have validators

print('\n\n********* validators ***********')

for k in common.validators.__dict__.keys():
    print(k) # here we have boolean dates json and numeric

print('\n\n********* numeric ***********')

for k in common.validators.numeric.__dict__.keys():
    print(k) # here we have the functions from numeric


import common.validators # if the rest of the modules are imported on the validators package

common.validators.json.is_json('da')


