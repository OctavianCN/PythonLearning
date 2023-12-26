###### Map, Filter, Zip, List Comprehensions #####

def fact(n):
    return 1 if n < 2 else n * fact(n-1)

print(fact(3))
print(fact(4))

results = map(fact,range(6))
print(results)  # get a map object - generator
for x in results:
    print(x) # now python starts calculate the results

for x in results:
    print(x) # it will return nothing

#solves the issue
results = list(map(fact,range(6)))
print(results)
for x in results:
    print(x)

for x in results:
    print(x)


l1 = range(5)
l2 = [10,20,30]
l3 = 100,200,300,400
results = list(map(lambda x,y,z: x+y+z, l1,l2,l3))
print(results)

#results = map(lambda x,y: x+y, l1,l2,l3) -lambda args needs to be the same as list

x = range(25)
print(x) # gets range (not a list) it is still not calculated

for i in x: # now x is calculated
    print(i)
for i in x: # range can be reused unlike map and filter
    print(i)

print(list(filter(lambda x: x%3 == 0, range(25)))) # filter the range with elements that are True to the function (only elements divisible by 3)

print(list(filter(None, [1,0,4,'a','',None,True,False]))) #  True will remain in the list

li = [1,2,3,4]
l2 =[10,20,30,40]
l3 = 'python'
results = zip(l1,l2,l3)
for x in results:
    print(x) # 1,10,p etc.. pair all iterables until it reaches h in python because len(python) > rest of them
for x in results:
    print(x) # Print nothing back (convert zip to list if you want to use as long as you want)

result = list(zip(range(10000),'python'))
print(results) # 0,p ... 5,n

l = range(10)
list(map(fact,l)) # map does not do the calculation until requested

results = [fact(n) for n in range(10)] # does calculation immediately
print(results)

results = (fact(n) for n in range(10)) # generator object -does not calculate
print(results)

for x in results:
    print(x) # print the results

for x in results:
    print(x) # here results is exhausted does not print anything

l1 = [1,2,3,4,5,6]
l2 = [10,20,30,40]

print(list(map(lambda x,y: x*y,l1,l2))) # same thing
print([x*y for x,y in zip(l1,l2)]) # same thing

print(list(filter(lambda  x: x%2 == 0, (x+y for x,y in zip(l1,l2)))))  #can also use map # keep only even numbers

print([x+y for x,y in zip(l1,l2) if (x+y)%2 == 0])