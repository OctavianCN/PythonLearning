# run.py

# print(f'loading run.py: __name__ = {__name__}') # the name is __main__ not run .py
#
# import module1 # now the name of module1 will apper as module1
#
# # when you execute your code python change the name to main
#
# if __name__ == '__main__':
#     print('Module was executed...')
import timing


code = '[x**2 for x in range(1_000)]'

result = timing.timeit(code, 100)
print(result)

# If you specify on terminal python ThisIsADir and inside the
# directory it is a file named __main__.py then python will call that file