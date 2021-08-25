#Write a program that calculates and prints the value according to the given formula:
import math
c=50
h=30
d1,d2,d3=[int(x)for x in input().split(',')]
q=math.sqrt((2*c*d1)/h)
print(q)
q=math.sqrt((2*c*d2)/h)
print(q)
q=math.sqrt((2*c*d3)/h)
print(q)