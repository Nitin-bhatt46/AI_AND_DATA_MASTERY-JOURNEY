transactions = [(200, 2), (100, 5), (450, 3), (150, 1), (600, 2)]


total_amount = list(map(lambda x:x[0]*x[1],transactions))
output=list(filter(lambda x:x>=1000, total_amount))
print(output)
