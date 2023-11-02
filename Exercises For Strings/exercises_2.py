MyString='Hello World!'
MyReversedString=''
for char in range((len(MyString)-1),-1,-1):  
    MyReversedString+= MyString[char]

print(MyReversedString)
