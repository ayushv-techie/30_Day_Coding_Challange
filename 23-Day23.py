# Day23: WAP to apply bubble sort on an array.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

n = int(input("Enter the number of elements in the array: "))
arr = []
print("Enter the elements:")
for _ in range(n):
    arr.append(int(input()))

sorted_arr = bubble_sort(arr)

print("Sorted Array:", sorted_arr)

