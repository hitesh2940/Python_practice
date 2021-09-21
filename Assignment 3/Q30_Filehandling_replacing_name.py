f=open("Readme.txt",'a+')
    
f.seek(0)
f.write(" Python coding is a fun and Hitesh is Doing Excellent joB wiTH it""\n")
    

f.close()
p=open("Readme.txt")
p1=open("Writeme.txt", "w+")
for line in p:
    
    a=(line.replace("Hitesh", "Shardha"))
    p1.write(a.swapcase())
    
    
    
p.close()
p1.close()
c = open("writeme.txt", "r")
print(c.read())    
c.close()