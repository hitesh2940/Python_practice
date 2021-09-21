#Write a python script to implement a generator to generate square up to 'n' numbersspecified by user.
def sq(n):    
    a=0
    while a <= n:
        yield a*a
        a=a+1
n=int(input("enter number you want to sqaure upto"))

for i in sq(n): 
    print(i)