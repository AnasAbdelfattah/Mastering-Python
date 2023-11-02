#Write a program to check if a given element is present in a list or not.
GivenList=["mahmoud" , 5 , 22 , 20 , "anas" , 33 , 86 ]
element=input("enter the element : ")
checked=False
for i in range(0, len(GivenList),1):
    if element==GivenList[i]:
        checked=True
    
    
if checked==True:
    print("the element exist")
else: 
    print("the element not exist")
