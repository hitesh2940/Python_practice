#Write a program to read content of the Delta_file.txt and print no. of sentences, lines and characters present in file Delta_file.txt
f=input()
fa=open(f,'r')
c1=cw=cc=0
for line in fa:
    words=line.split()
    c1+=1
    cw+=len(words)
    cc+=len(line)
    
print("no of lines",c1)
print("no of words",cw)
print("no of characters",cc)   
fa.close() 
