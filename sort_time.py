import timeit
import random
r = []
for x in range(1000):
    r.append(random.random())

def sort():
    for y in range(len(r)):
        for z in range(len(r)-1):
            if(r[z]>r[z+1]):
               temp =r[z]
               r[z] = r[z+1]
               r[z+1] = temp


sort()
t = timeit.timeit(sort,number=1)
print(t)
            
