#Write a program to append a message DELTA IoT Solutions, Hyderabad !!!' on new line to Delta_file.txt. Handle file not Found exception in your implementation.
try:
    f=open("Delta_file.txt",'a+')
    
    f.seek(0)
    f.write("DELTA IoT Solutions, Hyderabad !!!""\n")
    

    f.close()
    f=open("Delta_file.txt",'r')
    a=f.read()
    print(a)
    f.close()
except FileNotFoundError:
    
    print("file not found please enter valid correct name again")
