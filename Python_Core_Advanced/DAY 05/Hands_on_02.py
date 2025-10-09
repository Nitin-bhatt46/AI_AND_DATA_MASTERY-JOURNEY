def play_ground(a):
    if a == "left":
        b = input("...").lower()
        if b == "swim":
            c = input("...").lower()
            if c == "blue":
                return "lose"
            elif c == "red":
                return "lose"
            elif c == "green":
                return "win"
            else:
                return "lose"
        else:
            return "lose"
    else:
        return "lose"

def main():
    choice = input('Type "left" or "right": ').lower()
    result = play_ground(choice)
    print("You win!" if result == "win" else "Game Over.")


