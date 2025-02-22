# Day 15:Wap to replace all negative numbers in a given array with zero.

def replace_negatives_with_zero(arr):
    return [0 if num < 0 else num for num in arr]

array = [-8, 10, -3, 4, -156, 65]
print("Original Array:", array)
modified_array = replace_negatives_with_zero(array)
print("New Array:", modified_array)

