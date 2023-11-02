import random as rd 
print("-------------- PasswordGenerator --------------\n")
# all possible characters , numbers and special characters
characters = "ab01234cdefghijklm!@#$%nopuvwxyzAB^&*CDEFGHIJKLMNOPQRSTqrstUVWXYZ56789"

PasswordLength=(input("Password Length: "))  
while(PasswordLength.isdigit() == False  or int(PasswordLength) <=0):  #restrictions
    print("password length must be 1 character or more!!\n")
    PasswordLength=(input("Password Length: "))  
#end the while loop 
                                           
NumberOfPasswords=(input("Number Of Passwords: ")) 
while(NumberOfPasswords.isdigit()== False or int(NumberOfPasswords) <=0):  #restrictions
        print("Number of Passwords must be one or more!!\n")
        NumberOfPasswords=(input("Number Of Passwords: "))
#end the while loop        
NumberOfPasswords=int(NumberOfPasswords)
PasswordLength=int(PasswordLength)
# start generation    
Password=''
for i in range (NumberOfPasswords):
    for j in range (PasswordLength):
        Password+=rd.choice(characters)
       
    print(Password); Password=''     
#end generation
