#Create a list 'L' of all elements divisible by 5 between 1 to 1000 using lambda function. Generate another list 'doubling' having all elements doubled (multiplied by 2) from 'L' using lambda + map function
list1=[]

for i in range(1,1000):
    list1.append(i)
nums = list(filter(lambda x: x%5 == 0, list1))
print(nums)
list2=list(map(lambda x:x*2 ,nums))
print(list2)
