# tiny functions tip + username

def get_username(first, year):
    return first.strip() + "_" + str(year)

def calculate_total(bill, tip_percent):
    return bill + (bill * tip_percent / 100)

def split_amount(total, people):
    return total / people

def main():
    first = input("First name: ")
    year = int(input("Birth year: "))
    bill = float(input("Bill amount: "))
    tip = float(input("Tip %: "))
    people = int(input("Number of people: "))

    username = get_username(first, year)
    total = calculate_total(bill, tip)
    per = split_amount(total, people)

    print(f"Username: {username}")
    print(f"Total: {total:.2f}")
    print(f"Each pays: {per:.2f}")

if __name__ == "__main__":
    main()
