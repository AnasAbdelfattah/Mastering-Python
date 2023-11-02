# Write a program to find the sum of all the even elements in a list and find the average.
GivenList=[2 , 5 , 17 , 33 , 10 , 20 , 12 , 22 , 43 , 86 ]
sum=0
count=0
for num in range (0, len(GivenList), 1):
    if GivenList[num] %2 ==0 : 
        sum+=GivenList[num]
        count+=1 
        
print(f"the sum equal: {sum}")
print(f"the average equal: {float(sum/count):.2f}") 

