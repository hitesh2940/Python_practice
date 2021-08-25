#Write a python code to create a text file Delta_file.txt and to write the input string from the user. Read the stored string from the file and print it in the reverse order
f=open("Delta_file.txt",'w+')
s=input("enter string")
f.write(s)
f.close()

f=open("Delta_file.txt",'r')
a=f.read()
print(a[::-1])
f.close()

