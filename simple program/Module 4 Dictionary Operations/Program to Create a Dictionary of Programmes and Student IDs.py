N = int(input("Enter the number of programmes: "))
programme_dict = {}

for i in range(N):
    programme_name = input(f"Enter the name of Programme {i + 1}: ")
    M = int(input(f"Enter the number of students for {programme_name}: "))
    student_ids = [int(input(f"Enter studentID {j + 1} for {programme_name}: ")) for j in range(M)]
    programme_dict[programme_name] = student_ids

print("Dictionary of Programmes and Student IDs:", programme_dict)
