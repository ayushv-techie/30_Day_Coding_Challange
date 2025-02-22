# Day 26: WAP to rotate an array to the left by one position.

def rotate_left_by_one(arr):
    if not arr:
        return []

    first_element = arr.pop(0)
    arr.append(first_element)
    return arr

array = [10, 20, 30, 40, 50]
print("Array before left rotation:", array)

rotated_array = rotate_left_by_one(array)
print("Array after left rotation by 1 position:", rotated_array)
