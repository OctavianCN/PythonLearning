
print('Running module2.py')
import module1 # it will not run if you execute main because python will grab it from sys modules

def hello():
    print('Module2 says Hello! \n and ...')
    module1.hello()
