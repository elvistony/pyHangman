#life=1

def hang(life):
    print("\n~~~~~~~~~~~~~","\t\tLives Left:",4-life)
    hang={1:"|     |     |",2:"\n|     O     |",3:"\n|   / | \\   |",4:"\n|     /\\    |"}
    for i in range(1,life+1):
        print(hang.get(i),end="")
    for i in range(life+1,5):
        print("\n|           |",end="")
    print("\n~~~~~~~~~~~~~")
#hang(0)
