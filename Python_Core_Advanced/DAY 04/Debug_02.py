while True :
    try:
        nr_letters = int(input("Letters: "))
        break
    except ValueError:
        print("Invalid input! Please Enter the number")

while True:

    try:
       nr_symbols = int(input("Symbols: "))
       break
    except ValueError:
        print("Invalid input! Please Enter the number")

while True :
    try:
        nr_numbers = int(input("Numbers: "))
        break
    except ValueError:
        print("Invalid input! Please Enter the number")


password = []

if nr_letters + nr_symbols + nr_numbers == 0 :
    print(" Password cannot be generated, no VALID INPUT ")
    exit()

for i in range(nr_letters):
    password.append(random.choice(letters))
for i in range(nr_symbols):
    password.append(random.choice(symbols))
for i in range(nr_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)
final = ""
for c in password:
    final += c

print(final)
