guess = input("Guess a letter: ").lower()

# Input validation for Debug 3
if not guess.isalpha() or len(guess) != 1:
    print(" Invalid input! Please enter a single alphabet letter.")
    continue
