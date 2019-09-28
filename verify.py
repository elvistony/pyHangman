#Validation
from hangman import *
def verify(letter,str2):
    #letter=input(":")
    while letter in str2:
        if letter in str2:
            for i in range(len(str2)):
                if str2[i]==letter:
                    a=str2[:i]
                    b=str2[i+1:]
                    str2=a+letter.upper()+b
            #print("placed  ",str2)
            #print(str2)
            return str2
    else:
        #print(str2)
        return str2
#e="f"
#str2="elvis teena"
#str2=verify(e,str2)
#print("2")
#str2=verify(str2)
