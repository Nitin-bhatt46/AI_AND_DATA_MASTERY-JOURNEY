name = input("Please Enter Your Name ")
print(f"Welcome {name} to Treasure Island v2.")
print("Your mission is to find the treasure.")
points=0
a=input('Type "left" or "right" \n')

if a == "left":
    points+=10
    b = input('You\'ve come to a lake. There is an island in the middle of the lake.\nType Swim to "swim" across or "wait" to wait for a boat\n').lower()
    if b == "wait":
        points +=20
        c= input('You\'ve reached the door.\n choose the color "Blue","Red",or "Green"\n').lower()
        if c == "blue":
            print("Eaten by beasts GAME OVER")
        elif c == "red":
            print("Burned bye the fire GAME OVER")
        elif c == "green":
            points +=30
            print("YOU WIN!")
        else:
            points -=10
            print("GAME OVER")
    else:
        points-=10
        print("Game Over")
else:
    points-=10
    print("Fall into a hole Game Over")

if points >= 50:
    print("Lengendary treasure hunter!")
elif points <=50 and points >=20:
    print("Nice job Keep Practicing")
else:
    print("Better luck next time")
