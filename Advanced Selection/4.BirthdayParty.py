print("------------ Birthday Party ------------\n")
Friends={
  
}
#take the number of the friends 
HowManyFriends=input("give me how many friends attend the party : ")

#checking input is correct or not?
while(HowManyFriends.isnumeric() == False):
    print('Error, can you enter only numbers :',end='')
    HowManyFriends=input()
#end

#entering data in dictionary
for Friend in range(int(HowManyFriends)): 
    
    #input friend name 
    print(f"friend number {Friend+1} : " ,end='')
    FriendName=input().lower().strip()
    #checking input is correct or not?
    while(FriendName.isalpha() == False):
        print('Error, can you enter characters :',end='')
        FriendName=input()
    #end
    
    #input gift name 
    print("the gift is : ", end='')
    GiftName=input().lower()
    #checking input is correct or not?
    while(GiftName.isalpha() == False):
        print('Error, can you enter only characters :',end='')
        GiftName=input()
    #end
    
    #input data in dictionary
    Friends.update({GiftName : FriendName})
#end


#git the gift that joy want to search for
GiftInJoyMind=input("enter the git in your mind:")

#checking input is correct or not?
while(GiftInJoyMind.isalpha() == False):
        print('Error, can you enter only characters :',end='')
        GiftInJoyMind=input()
        
#whether gift in dictionary
if GiftInJoyMind.lower() in Friends.keys():
    print(f"thank you {Friends[GiftInJoyMind]}")
else:
    print("oops, sorry none!")



#end the program
    
    









# Friends=["amjad" , "anas" , "ahmed" , "john" , "sandy"]
# print("give me what his friends brought: ", end='')
# presents=input().split()


