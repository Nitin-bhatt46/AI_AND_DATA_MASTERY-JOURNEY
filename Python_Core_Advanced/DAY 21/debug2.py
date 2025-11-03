prices = {"laptop":50000, "mouse":800, "keyboard":1500, "monitor":9000}
expensive = list(filter(lambda x:(x[1])>=5000, prices.items()))
print(expensive)
