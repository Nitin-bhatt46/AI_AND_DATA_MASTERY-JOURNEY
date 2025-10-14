


**bids = \[('alice', 120, 1), ('bob', 150, 2), ('carol', 150, 3), ('dave', 90, 4)]**



**winner = bids\[0]  # initialize with first bid (name, amount, time)**



**for bid in bids\[1:]:**

    **# Compare amounts first**

    **if bid\[1] > winner\[1]:**

        **winner = bid**

    **# If same amount, pick earliest (smaller time)**

    **elif bid\[1] == winner\[1] and bid\[2] < winner\[2]:**

        **winner = bid**



**print(f"Winner is {winner\[0]} with {winner\[1]}")**

