# Write a program to find the largest element in a list using a for loop.
GivenList=[2 , 5 , 17 , 86 , 33 , 10 , 20 , 12 , 22 , 43  ]
MaxNum=GivenList[0]
for num in range(0 , len(GivenList), 1):
    if MaxNum< GivenList[num]:
        MaxNum=GivenList[num]
        
print(f"the max number equal: {MaxNum}")