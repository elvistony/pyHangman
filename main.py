#welcome Screen
from Hangman_main import *
from bank import *
from sys import *
from logos import *
import os
wait=input("Loading complete \n\tPress Enter to continue. . . ")
os.system('clear')

while True:
    print("""
                            MAIN MENU

                        1.Play Game
                        2.View Stash
                        3.Instructions
                        4.What's New!!
                        5.Exit""")
    ch=input("\t\tEnter your choice: ")
    try:
        ch=int(ch[0])
    except :
        print("You Entered a Non Number")

    if ch==1:
        lvvl=input("\t\tEnter level (1~6): ")
        try:
            lvvl=int(lvvl[0])
        except :
            print("You entered a Non Number")
        os.system('clear')
        try:
            trial(lvvl)
            os.system('clear')
            trial(lvvl+1)
            os.system('clear')
            trial(lvvl+2)
            os.system('clear')
            trial(lvvl+3)
            os.system('clear')
            trial(lvvl+4)
        except IndexError:
            print("You Pressed the wrong button(Entered not String)!!\n\tBack to Main Menu\n")
            wait=input("press Enter to continue. . . ")
        except :
            print("""
                    *************************
                        Game Complete !!
                    *************************
""")
            wait=input("press Enter to return to Main Menu. . . ")
    elif ch==2:
          c=input("Enter password character:")
          print(wordbank(0,c))
          wait=input("press Enter to continue. . . ")
    elif ch==3:
          os.system('clear')
          print("""
    ~~~~~~~~~~~~~~~INSTRUCTIONS~~~~~~~~~~~~~~~~~~~

                  HANGMAN VER:3.2.0

    This is a game that is based on the popular
    word search called Hangman. The Game is run
    by starting the main.py file present in the
    directory. The game is to guess the name/word
    using the given clues .
    ______________________________________________
    ~~~~~~~~~~~~~ 		Lives Left: 4
    |     |     |
    |           |
    |           |
    |           |
    ~~~~~~~~~~~~
    O--V-- T-I-T AUTHOR NAM
    Letter Bank :[ *bcdefghijklmnopqrstuvwxyz ]
    :
    ______________________________________________

    Here in the sample we may guess that the
    answer is
                 OLIVER  TWIST
    You have 4 lives- i.e. 4 chances to go wrong.
    You can refer the Letter bank to make sure you
    didn't enter that letter before and therefore
    dont lose points.
    Remember , only the first letter input(ed) will
    be accepted.
    """)
          wait=input("Press any Key to return to Menu. . .")
          os.system('clear')
    elif ch==4:
          os.system('clear')
          print("""
    *************WHAT'S  NEW VER.3.2**************

    Fixed Unexpected Crashes
    New Menu Items
    New Updated Word Bank
    Newer Splash Screen
    On Board Instruction Page
    Refined Coding
    Faster Processing

    **********************************************
    """)
          wait=input("Press Enter to return to Menu. . .")
    else:
          wait=input("Exiting. . .")
          exit()
    os.system('clear')
