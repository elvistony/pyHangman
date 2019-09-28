#Compiled all of them

from bank import *
from hangman import *
from verify import *
from string import *
from disp import *
from letin import *
#from check import *
#level 1
import os # This is the only outside resource


lvl=0


def trial(lvl):
    abt=ascii_lowercase
    k=0  #lives lost
    n='n'
    word=wordbank(lvl,n)
    #print(len(word))
    ls=len(word)-1
    word=word[:ls]
    name=word
    hang(k)
    #print(len(word))
    while True:
        #hang(k)
        dispword(word)
        #print("\n",word)
        print("\nLetter Bank :[",abt,"]")
        let=input(":")
        try:
            let=str(let[0])
        except:
            print("You Entered a NON String...")
        os.system('clear')
        lett=let[0]
        abt=getlet(lett,abt)
        new=verify(lett,word)
        if word==new:
            k=k+1
            word=new
            hang(k)
            #dispword(word)
        else:
            word=new
            hang(k)
            #dispword(word)
        if k==4:
            hang(k)
            print("YOU LOST...")
            break
        elif name.upper()==word:
            print(name.upper())
            print("\nLEVEL PASSED!!\n\n\nNEXT LEVEL...")
            break

    wait=input(" Press ENTER to continue . . . ")

#trial(1)
#trial(2)
