#Write a python code to take two inputs from user and performing division operation. 
try:
    a = int(input("please enter a first number "))
    b= int(input("please enter a second number"))
    print("answer is",a/b)
        
except ValueError:
    print("enter valid number")
except ZeroDivisionError:
    print("Division by 0 is not possible")
 