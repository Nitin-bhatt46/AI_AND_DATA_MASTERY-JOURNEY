import random
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def lost(i):
    print(f"your cards: {your_card[0:i+3]}, current score: {your_card[i] + your_card[i + 1] + your_card[i + 2]}")
    print(f"Computer Cards : {computer_card[0]}, final score {computer_card[0]}")
    print(f"You Lost")
    exit()


your_card =[]
computer_card =[]
for i in range(0,4) :
    your_card.append(random.choice(cards))
for i in range(0,4) :
    computer_card.append(random.choice(cards))
            # if your_card

print(logo)

for a in range(0,4):

    user_input = input("Do you want to play a game of BLACKJACK ? Type 'y' or 'n': ")

    if user_input == 'y':


        print(f"Your cards:{your_card[0:a+2]}, current score :{sum(your_card[0:a+2])}")
        print(f"Computer's first card: {computer_card[0]}")

        for i in range(0,2) :
            second_input=input(f"Type 'y' to get another card, type 'n' to pass : ")
            if second_input == 'y':
                if sum(your_card[0:i+3]) >21:
                    lost(i)
                else:
                    print(f"Your cards:{your_card[0:i+3]}, current score :{sum(your_card[0:i+3])}")
                    print(f"Computer's first card: {computer_card[0]}")

                    if (sum(computer_card[0:i+3])>21) and sum(your_card[0:i+3]) < 21 :
                        print(" You WIN")
                        exit()
                    elif (sum(computer_card[0:i+3])<21) and sum(your_card[0:i+3]) > 21 :
                        print("You lost")
                        exit()
                    elif (sum(computer_card[0:i+3]))== (sum(your_card[0:i+3])) :
                        print("Draw")
                        exit()
            else:
                print(f"Your final hand:{your_card[0:a+2]}, final score: {sum(your_card[0:a+2])}")
                print(f"Computer's final hand:{computer_card[0:a+2]}, final score {sum(computer_card[0:a+2])}")

                if (sum(computer_card[0:a+2])> 21) and sum(your_card[0 :a+3]) < 21 or sum(your_card[0 :a+3])  < sum(computer_card[0 :a+3]):
                    print("WIN")
                    exit()

                elif sum(computer_card[0:a+2]) > 21 and sum(your_card[0 :a+3]) < 21 or  sum(your_card[0 :a+3])  > sum(computer_card[0 :a+3]):
                    print("You lost")
                    exit()
                elif (sum(computer_card[0:a + 3])) == (sum(your_card[0:a + 3])):
                    print("Draw")
                    exit()







