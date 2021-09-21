#Generate a List 'P' containing all prime numbers between 1 to 100. Find the summation of all elements of 'P' using lambda + reduce.
from functools import reduce
P=[]
for Number in range (1, 100):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        P.append(Number)
print(P)        
d=reduce(lambda x, y: x+y, P)
print(d)