# Creating a file and writing 'Hello' into it
with open("file1.txt", "w") as file:
    file.write("Hello")

# Reading contents of 'file1.txt' and counting vowels
with open("file1.txt", "r") as file:
    content = file.read()
    vowel_count = sum(1 for char in content if char.lower() in "aeiou")
    print("Number of vowels:", vowel_count)
