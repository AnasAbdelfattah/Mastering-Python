import random as rd 
States_Capitals = {
  'Alabama': 'Montgomery',
  'Alaska': 'Juneau',
  'Arizona': 'Phoenix', 
  'Arkansas': 'Little Rock',
  'California': 'Sacramento',
  'Colorado': 'Denver',
  'Connecticut': 'Hartford',
  'Delaware': 'Dover',
  'Florida': 'Tallahassee',
  'Georgia': 'Atlanta',
  'Hawaii': 'Honolulu',
  'Idaho': 'Boise',
  'Illinois': 'Springfield',
  'Indiana': 'Indianapolis',
  'Iowa': 'Des Moines',
  'Kansas': 'Topeka',
  'Kentucky': 'Frankfort',
  'Louisiana': 'Baton Rouge',
  'Maine': 'Augusta',
  'Maryland': 'Annapolis',
  'Massachusetts': 'Boston',
  'Michigan': 'Lansing',
  'Minnesota': 'Saint Paul',
  'Mississippi': 'Jackson',
  'Missouri': 'Jefferson City',
  'Montana': 'Helena',
  'Nebraska': 'Lincoln',
  'Nevada': 'Carson City',
  'New Hampshire': 'Concord',
  'New Jersey': 'Trenton',
  'New Mexico': 'Santa Fe',
  'New York': 'Albany',
  'North Carolina': 'Raleigh',
  'North Dakota': 'Bismarck',
  'Ohio': 'Columbus',
  'Oklahoma': 'Oklahoma City',
  'Oregon': 'Salem',
  'Pennsylvania': 'Harrisburg',
  'Rhode Island': 'Providence',
  'South Carolina': 'Columbia',
  'South Dakota': 'Pierre',
  'Tennessee': 'Nashville',
  'Texas': 'Austin',
  'Utah': 'Salt Lake City',
  'Vermont': 'Montpelier',
  'Virginia': 'Richmond',
  'Washington': 'Olympia',
  'West Virginia': 'Charleston',
  'Wisconsin': 'Madison',
  'Wyoming': 'Cheyenne'  
}

print("-"*6+" State Capitals Game "+"-"*6)
RunAgain="y"
CorrectCounter=0
while(RunAgain=="y"):
   
    RandomState=rd.choice(list(States_Capitals.keys()))
    CapitalOfRandomState=States_Capitals[RandomState]
    print(f"What Is The Capital of {RandomState}:" , end=" "); AnswerOfUser=input().lower()
    if AnswerOfUser==CapitalOfRandomState.lower():
      CorrectCounter+=1
      print("Correct")
      print("Do You Want To Continue ! Y/N : "); Continue=input().lower()
      while(Continue!= 'y' and Continue != 'n'):
        print("Please Enter Only Y or N ")
        Continue=input().lower()     
      if Continue=="n":
        RunAgain="n"
    else:
      print("Worng , Game Over! ")
      RunAgain="n"
      
    if RunAgain=="n":
      print(f"You Got {CorrectCounter} Right") 
    
       
      
    
    
    