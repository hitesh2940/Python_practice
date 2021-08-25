#Write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
n=int(input())
f1=0
f2=1
end=","
c=2
a="0,1"
g=""
count=0
l=[0,1]
if(n==1):
    print(f1)
elif(n==2):
    print(f1," ,",f2)
elif(n>2):
    
    while c<n:
        f=f1+f2
        
        f=int(f)
        
        f1=f2
        f2=f
        c+=1
        
        l+=[f]
        b=f
        b=str(b)
        a+=","+b
    print(l)
    print(a)
    