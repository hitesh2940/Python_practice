#Write a python script to generate list of no. 0 to 100. Filter out even and odd numbers using lambda + filter function.
list1=[]
for i in range(100):
    list1.append(i)
even = list(filter(lambda x: x%2 == 0, list1))
print(even)
print("\nOdd numbers from the said list:")
odd = list(filter(lambda x: x%2 != 0, list1))
print(odd)    
