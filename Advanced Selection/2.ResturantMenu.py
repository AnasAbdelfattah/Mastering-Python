print("---------- Resturant Menu ----------")
#intialize the menue
menu={
"Soup" : ["vegetables", "seafood", "mushroom"],
"Meal":  ["burger", "grilled chicken", "mashed potatoes"]
    
}
print(f"what did she order ?  \n1.Soup: ",end='')
OrderSoup=input() #take the name of soup order 
print("2.Meal: ",end='')
OrderMeal=input() #take the name of meal order 

#conditions
if (OrderSoup != menu["Soup"][1] and OrderMeal==menu["Meal"][2]):
    print("she loves vegetables")
elif (OrderSoup == menu["Soup"][1] and OrderMeal  !=  menu["Meal"][2]):
    print("she doesn't love vegetables")
else:
    print("she would neither hate nor love vegetables")
    

#end 













