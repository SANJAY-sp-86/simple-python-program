def sum_of_digits(number):
    # Converting the number to a string to iterate over digits
    digit_sum = sum(int(digit) for digit in str(number))
    return digit_sum

# Example usage:
number = int(input("Enter a number: "))
result = sum_of_digits(number)
print(f"Sum of digits: {result}")
