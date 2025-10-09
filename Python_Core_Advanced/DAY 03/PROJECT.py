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

user_input= int(input("What do you choose?\n Type \n 0 for Rock,\n 1 for Paper,\n 2 for Scissors\n"))

computer_input= random.randint(0,2)

game_image =[rock,paper,scissors]



print("Computer chose",game_image[computer_input])

print("You chose")


if user_input > 2 or user_input < 0:
    print("INVALID CHOICE , you loose")

# Handling special case where Rock beats Scissors

elif user_input == 0 and computer_input == 2:
    print(game_image[user_input])
    print("You WIN!")

elif user_input == 2 and computer_input == 0:
    print(game_image[user_input])
    print("You lose!")

elif user_input == computer_input:
    print(game_image[user_input])
    print("You draw!")


elif computer_input < user_input:
    print(game_image[user_input])
    print("You WIN")

elif computer_input > user_input:
    print(game_image[user_input])
    print("You LOST")
