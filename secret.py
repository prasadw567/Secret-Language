import random
import string
print("Welcome to secret code language")
message=input("enter your message: ")
print("You have two choices:")
print("1:convert to secret language","    " ,"2:Decode the language")
choice=int(input("Enter your choice:"))
if(choice==1):
    word=message.split()
    for i in range(len(word)):
     if(len(word[i])<3):
        str1=word[i][1:]+word[i][0]
        print(str1,end=" ")
     else:
        random1=random.choices(string.ascii_lowercase,k=3)
        a=''.join(random1)
        random2=random.choices(string.ascii_lowercase,k=3)
        b=''.join(random2)
        str2=b+word[i][1:]+word[i][0]+a
        print(str2,end=" ")
else:
   word2=message.split()
   for i in range(len(word2)):
     if(len(word2[i])<3):
        str3=word2[i][1:]+word2[i][0]
        print(str3,end=" ")
     else:
        str4=word2[i][-4]+word2[i][3:-4]
        print(str4,end=" ")
