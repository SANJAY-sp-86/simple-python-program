# Creating a file and writing 'Hello123Hai' into it
with open("file1.txt", "w") as file:
    file.write("Hello123Hai")

# Reading contents of 'file1.txt' and counting digits
with open("file1.txt", "r") as file:
    content = file.read()
    digit_count = sum(1 for char in content if char.isdigit())
    print("Number of digits:", digit_count)
