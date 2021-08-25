#Write a program to check whether JohnDeere_file.txt exists if not then create a new file and Copy the content of file Delta_file.txt to JohnDeere_file.txt
import os
f=input("file name")
if os.path.isfile(f):
    print("yes file name exit")
else:
    f1=open("Delta_file.txt","r")
    f2=open("JohnDeere_file.txt","+a")
    b=f1.read()
    f2.write(b)
    
    f1.close()
    f2.close()
    
    f3=open("JohnDeere_file.txt","r")
    b=f3.read()
    print(b)
    f3.close()