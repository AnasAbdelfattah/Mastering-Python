# Write a program to remove all the duplicate elements from a list.
GivenList=[2 , 5 , 22 , 33 , 10 , 20 , 12 , 22 , 33 , 86 ]
testlist=[]
for num in range (0,len(GivenList), 1):
    if GivenList[num]  not in testlist:
        testlist.append(GivenList[num])
        
print(testlist)    
