# Day22: WAP to check the frequency of elements in an array.

def count_frequency(arr):
    frequency = {}
    
    for element in arr:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    print("Element Frequency:")
    for key, value in frequency.items():
        print(f"{key}: {value}")
n = int(input("Enter the number of elements in the array: "))
arr = []
print("Enter the elements:")
for _ in range(n):
    arr.append(int(input()))
count_frequency(arr)
