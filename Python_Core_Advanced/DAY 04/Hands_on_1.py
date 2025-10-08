
import random

# THIS ARE THE LIST WHICH WE HAVE CREATED FOR THE PASSWORD GENERATION.

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# CODE START FROM HERE
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
predict =0


# CREATING A LIST
password = []

if nr_numbers >= 1 and 1 <= nr_symbols:
    predict +=2
elif nr_numbers >= 1 or 1 <= nr_symbols:
    predict +=1
else:
    predict +=0

# THIS LOOP WILL RUN FOR THE NUMBER OF LETTER WHICH USER HAS INPUT
for i in range(nr_letters):
    # THIS FUNCTION RANDOM.CHOICE() CHOOSE N NUMBER FROM THE letters LIST AND APPEND TO THE LIST CALLED PASSWORD.
    password.append(random.choice(letters))

for j in range(nr_symbols):
    # THIS FUNCTION RANDOM.CHOICE() CHOOSE N NUMBER FROM THE symbols LIST AND APPEND TO THE LIST CALLED PASSWORD.
    password.append(random.choice(symbols))

for k in range(nr_numbers):
    # THIS FUNCTION RANDOM.CHOICE() CHOOSE N NUMBER FROM THE numbers LIST AND APPEND TO THE LIST CALLED PASSWORD.
    password.append(random.choice(numbers))


if len(password) >= 12:
    predict+=1


# SO, TO GET SHUFFLED ANSWER WE NEED TO USE SHUFFLE FROM THE RANDOM LIBRARY.
random.shuffle(password)

print(predict)

final_password = ""

# PASSWORD IS A LIST SO, TO NEED TO MAKE IT A STRING, TO GET BETTER OUTPUT.
for n in password:
    final_password += n


print("Your password is: ", final_password)
if predict == 3:
    print("Very Strong password")
elif predict == 2:
    print("Strong password")
elif predict == 1:
    print("Weak password")
else :
    print("Very Weak password")




