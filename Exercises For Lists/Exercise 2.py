# Write a program to count the number of elements in a list that are greater than a given value.
GivenList=[2 , 5 , 17 , 33 , 10 , 20 , 12 , 22 ]
GivenValue=int(input("enter the number : "))
count=0
for num in range(0,len(GivenList),1):
    if GivenValue < GivenList[num]:
        count+=1
        
if count==0 : 
    print("none")
else: 
    print(f"the elements are: {count}")
    