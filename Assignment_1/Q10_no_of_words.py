#Please write a program which count and print the numbers of each character in a string input by console.

s = input()
  

d = {} 
    
for i in s: 
    if i in d: 
        d[i] += 1
    else: 
        d[i] = 1
    

print (str(d))