# Day 25: WAP to find the intersection of two arrays.

def find_intersection(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    intersection = set1.intersection(set2)
    return list(intersection)

array1 = [1, 2, 2, 3, 4]
array2 = [2, 3, 5]

result = find_intersection(array1, array2)
print("Intersection of arrays:", result)
