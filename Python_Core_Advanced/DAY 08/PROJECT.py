

bidding = 1

data = {'name':\[],'bid':\[]}



while not bidding == 0:

    # TODO-1: Ask the user for input

    name= input("Enter your name : ")

    bid = int (input("Enter bid : "))

    # TODO-2: Save data into dictionary {name: price}





    data\['name'].append(name)

    data\['bid'].append(bid)





    print(data.items())



    # TODO-3: Whether if new bids need to be added





    # TODO-4: Compare bids in dictionary

    again = input("Would you like to try again? (y/n) : ").lower()

    if again =='n':

        bidding = 0



max\_bid = max(data\['bid'])  # Find the highest bid

winner\_index = data\['bid'].index(max\_bid)  # Get the index of that bid

winner\_name = data\['name']\[winner\_index]   # Get the corresponding name



print(f"The winner is {winner\_name} with a bid of {max\_bid}")
