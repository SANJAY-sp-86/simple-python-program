# Read marks for 4 subjects
M1 = int(input("Enter marks for M1: "))
M2 = int(input("Enter marks for M2: "))
M3 = int(input("Enter marks for M3: "))
M4 = int(input("Enter marks for M4: "))

# Calculate percentage
total_marks = M1 + M2 + M3 + M4
percentage = total_marks / 4

# Assign grades based on percentage
if 80 <= percentage <= 100:
    grade = "Good"
elif 60 <= percentage <= 79:
    grade = "Average"
elif 40 <= percentage <= 59:
    grade = "Fair"
else:
    grade = "Fail"

print("Percentage =", percentage)
print("Grade =", grade)
