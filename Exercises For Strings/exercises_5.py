MyString='Hello World!'
character=input('enter the substring that you search for: ')
counter=0
for char in range (0,len(MyString)):
    if MyString[char]== character:
        counter+=1
print(f"the substring appears: {counter} times")
    
