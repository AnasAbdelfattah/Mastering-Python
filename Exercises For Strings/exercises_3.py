MyString='Hello World!'
vowels=0
for char in range(0,len(MyString)):
    if MyString[char] in "aeiou":
        print(MyString[char])
        vowels+=1
print(f"vowels : {vowels:d}")
