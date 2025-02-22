# Day19: WAP to apply Binary search in an array.

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

array= list(map(int,input("Enter the Elements of array: ").split()))
arr= sorted(array)
print("Sorted array",arr)
x = int(input("Enter the target element: "))
result = binary_search(arr, x)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

