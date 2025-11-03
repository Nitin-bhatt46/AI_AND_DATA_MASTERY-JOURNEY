nums = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x%2==0, nums))

even_squares = map(lambda x: x**2, even)
print(list(even_squares))
