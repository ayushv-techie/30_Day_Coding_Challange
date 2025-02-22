# Day 16: WAP to reverse the elements in a given array.

def reverse_array(arr):
    return arr[::-1]
array = list(map(int, input("Enter elements of Array: ").split()))
reversed_array = reverse_array(array)
print("Reversed array:", reversed_array)