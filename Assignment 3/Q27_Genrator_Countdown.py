#Write a script to accept a input from user and to generate a list in countdown order till 0 using Generator function.
def countdown(n):    
    for i in range(n,0,-1):
        yield i
        
        
n=int(input("enter number you want to Countdown from"))

for i in countdown(n): 
    print(i)