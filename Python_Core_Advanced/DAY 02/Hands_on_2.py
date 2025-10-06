from datetime import datetime
First_name=input("Kindely Enter you First_Name ")
Year = int(input("Enter Your Birth year "))
bill = float(input("Enter the Bill Amount "))
People = int(input("Enter the number of person "))
if People <= 0:
    print("Invalid Input")
    exit()
if datetime.now().year -Year <=18:
    percent = 0;
    print("Tip Suggestion is disable")
else :
    percent = int(input("Tip %: "))
total = bill + (bill * percent / 100)
each = total / People
print(f"UserName {First_name}{Year}")
print(f"Total Bill with Tip {total}")
print(f"Amount Each Person has to pay: {each:.2f}")
