data = [
    ("Nitin", [4, 5, 3, 4]),
    ("Ravi", [5, 5, 5, 4]),
    ("Simran", [2, 3, 2, 4]),
    ("Meena", [4, 4, 4, 4])
]


rating =list(map(lambda x:(x[0],sum(x[1])/len(x[1])),data))

output=list(filter(lambda x:x[1]>=4,rating))
print(output)
