n = int(input("Enter the number of elements in the list: "))
my_list = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    my_list.append(element)

sum_of_values = sum(my_list)
print("Sum =", sum_of_values)
