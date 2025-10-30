words = ["apple", "banana", "cherry", "kiwi"]
long_words = list(filter(lambda w: len(w) > 5, words))
print(long_words)  # Output: ['banana', 'cherry']
