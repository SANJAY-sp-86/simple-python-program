# Reading contents of 'file1.txt' and displaying the content
with open("file1.txt", "r") as file:
    content = file.read()
    print("Content of the file:", content)
