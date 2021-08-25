#Write a python program to implement a simple calculator to perform operations : +, -, *, /.

a=int(input("enter first number"))
b=int(input("enter Second number"))
print("enter + to add")
print("enter - to subtract")
print("enter / to divide")
print("enter * to multiply")
c=input()
if(c=="+"):
    print(a+b)
elif(c=="-"):
    print(a-b)
elif(c=="/"):
    print(a/b)
elif(c=="*"):
    print(a+b)
else:
    print("Enter Correct expression")    