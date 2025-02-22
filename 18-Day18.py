# Day 18: Wap to get an array from user and remove all duplicate elements from the array

def remove_duplicates(arr):
    return list(set(arr))
array = list(map(int, input("Enter the elements of array: ").split()))
new_arr = remove_duplicates(array)
print("Array without duplicates:", new_arr)
