#str1="Elvis Tony\n"

from string import *

def dispword(str1):
    for i in str1:
        if i!=" "and i not in ascii_uppercase:
            print("-",end="")
        elif i==" ":
            print(" ",end="")
        else:
            print(i,end="")

#dispword(str1)
