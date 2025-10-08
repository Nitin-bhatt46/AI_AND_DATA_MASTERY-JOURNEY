nr_letters = int(input("How many letters?\n"))
nr_symbols = int(input("How many symbols?\n"))
nr_numbers = int(input("How many numbers?\n"))

password = []

for i in range(nr_letters):
    password.append(random.choice(letters))

final_password =""

for i in password:
    final_password +=i

random.shuffle(final_password)

print("Your password is: " + final_password)




