# Day 21: WAP to find the second largest number in an array.

def find_second_largest(arr):
    if len(arr) < 2:
        return "Array must have at least two elements."
    largest = second_largest = float('-inf')

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        return "No second largest element (all elements might be equal)."
    return second_largest

# Input: List of numbers
array = list(map(int, input("Enter the elements of the array separated by space: ").split()))

# Find the second largest number
result = find_second_largest(array)

print(f"The second largest number is: {result}" if isinstance(result, int) else result)

