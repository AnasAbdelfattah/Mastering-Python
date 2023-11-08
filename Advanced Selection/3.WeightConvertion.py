print("---------- Weight Conversion ----------\n")
RunAgain="y"
#start while loop to check continue or not 
while(RunAgain=="y"):
    Unit = int(input("choose Unit  ( 1.mg   2.kg   3.ton ) : "))
    #checking of the uint is incorrct 
    while Unit not in [1, 2, 3]:
        print(f"Error, Enter only 1 or 2 or 3 :",end='')
        Unit = int(input())
    #enter the weight 
    weight = int(input("Enter The Weight:"))
    #check if weight is negative
    while weight < 0:
        print(f"Error, enter only positive number:", end='')
        weight = int(input())

    if Unit == 3: #ton
        print(f"Grams : {weight * 1000 * 1000:,d}")
        
    elif Unit == 2:#kg
        print(f"Grams : {weight * 1000:,d}")
        
    else:          #mg
        print(f"Grams : {(weight/1000):,.2f}")
     
    #check of you want to continue ?   
    print(f"Do you want continue (Y/N): ",end='')
    RunAgain=input().lower()
    
    while(RunAgain != "y" and RunAgain != "n"):
        print("enter only y or n :", end='')
        RunAgain=input().lower()

    
    #break
    if (RunAgain=="n"):
        break    
    
#end while loop    