
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
a=input('Type "left" or "right" \n')

if a == "left":
    b = input('You\'ve come to a lake. There is an island in the middle of the lake.\nType Swim to "swim" across or "wait" to wait for a boat\n').lower()
    if b == "swim":
        c= input('You\'ve reached the door.\n choose the color "Blue","Red",or "Green"\n').lower()
        if c == "blue":
            print("Eaten by beasts GAME OVER")
        elif c == "red":
            print("Burned bye the fire GAME OVER")
        elif c == "green":
            print("YOU WIN!")
        else:
            print("GAME OVER")
    else:
        print("Game Over")
else:
    print("Fall into a hole Game Over")
