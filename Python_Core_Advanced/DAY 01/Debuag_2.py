bill = int (input("Enter your bill amount: ")) 
tip = int(input("Enter tip percentage: "))  # input convert input into string format we need in  integer format so, we convert it into integer.
total = bill + (bill * tip / 100) print("Total bill with tip:", total)
