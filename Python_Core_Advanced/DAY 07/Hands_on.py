# TODO-1: Import and print the logo from art.py when the program starts.
import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ALPHABET=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# TODO-2: What happens if the user enters a number/symbol/space?


def bruteforce(original_text):

    shift_amount = 0
    for shifted in range(len(alphabet)-1):
        output_text = ""
        shift_amount +=1
        for letter in original_text:

            if letter not in alphabet and letter not in ALPHABET:
                output_text += letter
            else:
                if  letter.isupper()==True:
                    shifted_position = ALPHABET.index(letter) + shift_amount
                    shifted_position %= len(ALPHABET)
                    output_text += ALPHABET[shifted_position]
                else:
                    shifted_position = alphabet.index(letter) + shift_amount
                    shifted_position %= len(alphabet)
                    output_text += alphabet[shifted_position]

        print(f"Shift by {shift_amount}: {output_text}")

def code(original_text,shift_amount):
    output_text = ""

    for letter in original_text:

        if letter not in alphabet and letter not in ALPHABET:
            output_text += letter

        elif letter.isupper() == True:
            shifted_position = ALPHABET.index(letter) + shift_amount
            shifted_position %= len(ALPHABET)
            output_text += ALPHABET[shifted_position]
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the result: {output_text}")


def caesar(original_text, shift_amount, encode_or_decode_or_bruteforce):

    if encode_or_decode_or_bruteforce == "bruteforce":
        bruteforce(original_text)

    elif encode_or_decode_or_bruteforce == "decode":
         code(original_text,-shift_amount)
    else :
        code(original_text,shift_amount)




# TODO-3: Can you figure out a way to restart the cipher program?

def main():
    should_continue = True
    while should_continue:

        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt or bruteforce to get all possible answer:\n").lower()
        text = input("Type your message:\n")
        shift = int(input("Type the shift number ignore if going with bruteforce:\n"))

        caesar(original_text=text, shift_amount=shift, encode_or_decode_or_bruteforce=direction)

        restart = input("Type 'yes' to restart and 'no' to exit: ").lower()
        if restart == "no":
            should_continue = False
            print("Goodbye!")




if __name__=="__main__":
    main()
