import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image = [rock, paper, scissors]

computer_score = 0
user_score = 0
round_number = 0
max_rounds = 5
needed_to_win = 3  # best of 5 → first to 3

while round_number < max_rounds and user_score < needed_to_win and computer_score < needed_to_win:
    round_number += 1
    print(f"\nRound {round_number}")
    print(f"Score -> You: {user_score} | Computer: {computer_score}")

    try:
        user_input = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors: ").strip())
    except ValueError:
        # non-integer input
        print("Invalid choice, you lose this round.")
        computer_score += 1
        continue

    if user_input < 0 or user_input > 2:
        print("INVALID CHOICE, you lose this round.")
        computer_score += 1
        continue

    computer_input = random.randint(0, 2)

    print("\nYou chose:")
    print(game_image[user_input])
    print("Computer chose:")
    print(game_image[computer_input])

    # decide result using modular arithmetic
    if user_input == computer_input:
        print("It's a draw this round!")
        # no score change
    else:
        result = (user_input - computer_input) % 3
        if result == 1:
            user_score += 1
            print("You WIN this round!")
        else:  # result == 2
            computer_score += 1
            print("Computer WINS this round!")

# final result
print("\nFinal Result:")
print(f"You: {user_score} | Computer: {computer_score}")
if user_score > computer_score:
    print("🏆 You are the Champion!")
elif computer_score > user_score:
    print("💻 Computer Wins the Series!")
else:
    print("It's a DRAW series!")

