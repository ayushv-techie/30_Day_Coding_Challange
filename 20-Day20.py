# Day 20: WAP to check if the array is sorted in ascending order or not.
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

array = list(map(int, input("Enter the elements of the array separated by space: ").split()))
if is_sorted(array):
    print("The array is sorted in ascending order.")
else:
    print("The array is not sorted in ascending order.")
