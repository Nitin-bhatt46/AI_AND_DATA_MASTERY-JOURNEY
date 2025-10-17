import random
print(r"""
   _____                           _______ _                _   _                 _               
  / ____|                         |__   __| |              | \ | |               | |              
 | |  __ _   _  ___  ___ ___         | |  | |__   ___      |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __|        | |  | '_ \ / _ \     | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \        | |  | | | |  __/     | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/        |_|  |_| |_|\___|     |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
""")

Attempt = 0


def choice(number):
    global Attempt
    choice = input("Choose a difficulty. Type 'easy' or 'hard':").lower()

    if choice == 'easy':
        Attempt = 10
    elif choice == 'hard':
        Attempt = 5
    else:
        print("Invalid choice")

    for i in range(1, Attempt+1):
        user_predict =input("Make a guess: ")
        if user_predict == choice:
            print("Correct! You got it!")
            return
        elif user_predict < choice:
            print("Too low!")
        elif user_predict > choice:
            print("Too high!")

        print(f"Guess again! You have {Attempt-i} attempts remaining to guess the number.")

    print("You've run out of guesses. Refresh the page to run again.")
    exit()



def main():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)
    print(number)
    choice(number)
    exit()

if __name__=="__main__":
    main()
