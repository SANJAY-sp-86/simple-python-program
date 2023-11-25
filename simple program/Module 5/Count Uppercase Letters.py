word = input("Enter a word: ")
count = sum(1 for char in word if char.isupper())
print("Number of uppercase letters:", count)
