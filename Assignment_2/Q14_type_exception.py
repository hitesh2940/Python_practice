#Write a program to take integer input from user. Handle Type exception (Value Error) for invalid input
try:
    a = int(input("please enter number "))
    
    print("you enter :",a)
        
except ValueError:
    print("enter valid number")
    