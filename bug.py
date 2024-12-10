def calculate_average(numbers):
    if not numbers:  # Check for empty list
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

# Example usage with potential error:
data = [1, 2, 3, 0, 5]
average = calculate_average(data)
print(f"The average is: {average}")

data2 = []
average2 = calculate_average(data2)
print(f"The average is: {average2}")

data3 = [1,2,'a']
average3 = calculate_average(data3)
print(f"The average is: {average3}")