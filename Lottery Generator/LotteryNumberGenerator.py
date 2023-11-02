while(Regenrate == "y"): 
    import random as rd
    ListSize=7
    StartRange=0
    EndRange=9
    LotteryList=[]
    print("Lottery Number Generator" , end="\n\n")
    for i in range(ListSize):  
        LotteryList.append(rd.randint(StartRange, EndRange))   # generation random numbers


    print("The Lottery Numbers:", end=" ")

    for i in range(ListSize):  # showing the list of lottery numbers
        if i == (ListSize -1) :
            print(LotteryList[i])
        else:
            print(LotteryList[i], end='-')

    Regenrate=input("would like to generate another set of lottery numbers (Y/N)").lower() 
    while(Regenrate != 'y' and Regenrate != 'n'): #checking the input of the user
        print("please enter only Y or N ")
        Regenrate=input("would like to generate another set of lottery numbers (Y/N)").lower()
        
#end the while loop 
  
    
