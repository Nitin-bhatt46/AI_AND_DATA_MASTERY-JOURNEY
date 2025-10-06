choice = input("Left or Right? ")
if choice = "left" or "Left":
    action = input("Swim or Wait? ")
    if action.lower == "wait":
        door = input("Pick color: Red/Green/Blue ")
        if door == "green":
            print("You win")
        elif door == "red":
            print("Burned by fire")
        else:
            print("Eaten")
    else:
        print("Game Over")
else:
    print("Game Over")


What to fix: assignment/comparison error, case handling, wrong method usage, and ensure only "green" wins while other colors give proper messages. Also make or condition correct.


Solution 1 :-

choice = input("Left or Right? ").lower()
if choice == "left":                                                # assignment operator
    action = input("Swim or Wait? ")
    if action.lower() == "wait":				    # Lower is function ()
        door = input("Pick color: Red/Green/Blue ")
        if door.lower() == "green":				    # lower()
            print("You win")
        elif door.lower() == "red":
            print("Burned by fire")
        else:
            print("Eaten")
    else:
        print("Game Over")
else:
    print("Game Over")
