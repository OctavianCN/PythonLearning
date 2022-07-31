######## Operator module #######
# -almost every arithmetic operation is in operator module (add,eq,pow,is,lt...)
import operator
print(dir(operator))

# Item getter

l = [1,2,3,4,5,6]
s = 'python'

f = operator.itemgetter(1,3,4) # returns a callable and get poz 1,3,4
print(f(l))