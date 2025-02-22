# Day 27: WAP to rotate an array to the right by one position.

def rotate_right_by_one(arr):
    if not arr:
        return []
    last_element = arr.pop()
    arr.insert(0, last_element)
    return arr

array = [10, 20, 30, 40, 50]
print("Array before right rotation:", array)

rotated_array = rotate_right_by_one(array)
print("Array after right rotation by 1 position:", rotated_array)