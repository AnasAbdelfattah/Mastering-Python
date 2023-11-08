print("---------- Project With Coleages ----------")
print(f"what did team members bring? ", end='')
#take the stuff that the members brought
Stuff=input().split()
#condition
if ("battery" in Stuff):
    print("I don’t need to bring the battery") 
else:
    print("I will need to bring the battery")
#end