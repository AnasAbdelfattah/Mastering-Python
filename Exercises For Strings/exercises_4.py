MyString='Hello World!'
Splittedwords=MyString.split()
checker=0
longest=''
for word in range(0,len(Splittedwords)):
    if len(Splittedwords[word])>checker:
        checker=len(Splittedwords[word])
        longest=Splittedwords[word]
print(f"the longest word is: {longest} and its length is : {checker}")
