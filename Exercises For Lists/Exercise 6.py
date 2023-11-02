#Write a program to reverse a list using a while loop.
GivenList=["mahmoud" , 5 , 22 , "anas" , True , 20 , 12 , 33 , 86 ]
ReversedList=[]
i=len(GivenList)-1
while(i != -1):
    ReversedList.append(GivenList[i])
    
print(ReversedList)    
