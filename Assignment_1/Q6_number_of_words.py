#Write a program that accepts a sentence and calculate the number of letters and digits
a=input()
character=0
number=0
for c in a:
    if(c.isalpha()):
        character+=1
    elif(c.isdigit()):
        number+=1
print("number count =",number,"and digit count =",character)        