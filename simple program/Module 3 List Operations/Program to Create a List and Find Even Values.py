n = int(input("Enter the number of elements in the list: "))
my_list = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    my_list.append(element)

even_values = [x for x in my_list if x % 2 == 0]
print("Even Values:", even_values)
