#Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
s=input()
u=0
l=0
for a in s:
    if a.isupper():
        u =u+1
    elif a.islower():
        l =l+1
print("Number of uppercase =",u,"Number of lower case",l)         
