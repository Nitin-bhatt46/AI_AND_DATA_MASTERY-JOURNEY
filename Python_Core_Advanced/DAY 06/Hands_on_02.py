import random

from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

list_chosen_word=[]
for i in chosen_word:
    list_chosen_word.append(i)



while not game_over:
    hint_list = [letter for letter in list(chosen_word) if letter not in correct_letters]
    # this above code is comprehension in which are making hints more powerful.It will not repeat the gussed word
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    print(f"need hint type 'hint'")
    guess = input("Guess a letter: ").lower()

    if guess == "hint" and lives >= 1:
        lives -= 1
        print(random.choice(hint_list))
        continue



    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            if letter not in correct_letters:
                correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True

            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])

