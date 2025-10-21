from  art import *
from game_data import data
import random


def choices():
    choice = random.choice(data)
    return choice



def main():
    choice_1 = choices()
    run = True
    score = 0
    while run:
        print(logo)
        choice_2 = choices()

        if score>0:
            print(f"Your Current Score: {score}")

        print(f"Compare A:{choice_1['name']}, {choice_1['description']}, {choice_1['country']} ")

        print(vs)

        print(f"Compare B:{choice_2['name']}, {choice_2['description']}, {choice_2['country']}")

        user_choice = input(f"Who has more followers? Type 'A' or 'B': ").upper()

        if choice_1['follower_count'] > choice_2['follower_count']:
            winner = 'A'
        elif choice_1['follower_count'] < choice_2['follower_count']:
            winner = 'B'
        else:
            winner = 'Draw'

        if winner == user_choice:
            choice_1 = choice_2
            score += 1
        else:
            print(f"Sorry, that wrong, final score is {score} ")
            run = False



if __name__ == '__main__':
    main()
