# input convert all the value given by the user in string format so, we have to handle it with data type conversion.

bill = float(input("Total bill: "))
percent = int(input("Tip %: "))
people = int(input("Split among: "))
each = 0

if people == 0:							    # this help to handle the condition of 0 people
    print("Input value is not valid")
else :
    total = bill + (bill * percent / 100)
    each = total / people
    print(f"Each pays:{ each:.2f}")                                  # :.2f help to show last two decimal.


