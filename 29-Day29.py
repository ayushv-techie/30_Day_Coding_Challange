# Day 29: WAP to transpose a matrix.
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    
    return transposed

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
for row in matrix:
    print(row)

transposed = transpose_matrix(matrix)

print("\nTransposed Matrix:")
for row in transposed:
    print(row)
