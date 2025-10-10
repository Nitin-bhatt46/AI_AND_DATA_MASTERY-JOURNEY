guess = input("Guess a letter: ").lower()

if guess in correct_letters:
    print(f"You've already guessed {guess}")
    continue 

