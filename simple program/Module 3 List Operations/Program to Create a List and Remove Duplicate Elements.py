n = int(input("Enter the number of elements in the list: "))
my_list = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    my_list.append(element)

unique_list = list(set(my_list))
print("List without duplicates:", unique_list)
