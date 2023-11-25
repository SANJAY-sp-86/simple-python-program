def sum_of_numbers(n):
    # Using the formula for the sum of an arithmetic series
    sum_result = n * (n + 1) // 2
    return sum_result

# Example usage:
n = int(input("Enter a number 'n': "))
result = sum_of_numbers(n)
print(f"Sum of 'n' numbers: {result}")
12