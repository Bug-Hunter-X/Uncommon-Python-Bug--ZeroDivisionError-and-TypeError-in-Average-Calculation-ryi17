def calculate_average(numbers):
    if not numbers:
        return 0
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    return sum(numeric_numbers) / len(numeric_numbers)

# Example usage with improved error handling:
data = [1, 2, 3, 0, 5]
average = calculate_average(data)
print(f"The average is: {average}")

data2 = []
average2 = calculate_average(data2)
print(f"The average is: {average2}")

data3 = [1,2,'a']
average3 = calculate_average(data3)
print(f"The average is: {average3}")

data4 = [1,2,3,4,5,6,7,8,9,10]
average4 = calculate_average(data4)
print(f"The average is: {average4}")
