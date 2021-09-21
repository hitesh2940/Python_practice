#Write a script to perform smart division to handle division by o error using Decorator function.
def Zero_division(func):
    def Inner_Function(a, b):
        try:
            func(a,b)
        except ZeroDivisionError:
            print("Cannot divide by zero")
    return Inner_Function
  
@Zero_division
def Divide(l,b):
        print(b/l)
      


Divide(0,5)
