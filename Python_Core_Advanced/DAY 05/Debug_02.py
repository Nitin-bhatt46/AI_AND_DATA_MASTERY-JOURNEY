def calculate_total(bill, tip):
    total = bill + bill * tip / 100
    return total

t = calculate_total(100, 10)
print(t)
