# Create an empty dictionary
programme_dict = {}

# Assume you have some code here to populate the dictionary, similar to what was provided earlier.

# Now you can use the code to find the number of students in a program
programme_to_find = input("Enter the name of the programme: ")
student_count = len(programme_dict.get(programme_to_find, []))
print("Number of students in", programme_to_find, ":", student_count)
