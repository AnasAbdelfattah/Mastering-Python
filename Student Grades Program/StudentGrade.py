print("---------- Student Grades Program ----------\n\n")
#create lists 
ListOfGrades=[]
CheckerList=[]

#take the grades from the user
EnterdGrades=(input("enter the grades:"))
ListOfGrades=EnterdGrades.split()

InvalidCounter=0
ValidCounter=0
Summation=0 
MaxGrade=ListOfGrades[0]#used in determining the max grade
MinGrade=ListOfGrades[0]#used in determining the min grade

#check if valid or invalid grade
for i in range(len(ListOfGrades)): 
    if (int(ListOfGrades[i]) >100 or int(ListOfGrades[i]) <0 )  :
        print(f"the grade in index {i} is invalid")
        InvalidCounter+=1
        CheckerList.append(0)
    else:
        CheckerList.append(1)
        SumForAverage=ListOfGrades[i]
        ValidCounter+=1
        if int(MaxGrade) <= int(ListOfGrades[i]):
            MaxGrade=ListOfGrades[i]
        if int(MinGrade )> int(ListOfGrades[i]):
            MinGrade=ListOfGrades[i]  
              
        Summation+=int(ListOfGrades[i])
#end for loop

       
print(f"the in number of invalid grades : {InvalidCounter}", end='\n')
print(CheckerList, end='\n')        
print(f"summation of grades equal : {Summation}", end='\n')
print(f"the min grade equal : {MinGrade} and index equal : {ListOfGrades.index(str(MinGrade))} ",end='\n')
print(f"the max grade equal : {MaxGrade} and index equal : {ListOfGrades.index(str(MaxGrade))} ", end='\n')
print(f"the average equal: {int(Summation)/int(ValidCounter)}")