#Write a python program to read current date and time, delete content of file JD_file.txt and save date time in it.
import datetime 
f = open("JD_file.txt", "r+") 
f.seek(0)  
f.truncate() 
f.close()
ct = datetime.datetime.now() 
f=open("JD_file.txt",'w+')
f.write(str(ct))
f.close()