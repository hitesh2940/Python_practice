#Write a Python script to receive three inputs from user and to find largest no. using lambda function
from functools import reduce
lst=[]
a=int(input("Enter First Number"))
b=int(input("Enter Second Number"))
c=int(input("Enter Third Number"))
lst.append(a)
lst.append(b)
lst.append(c)

d=reduce(lambda x, y: x if (x > y) else y, lst)
print(d)