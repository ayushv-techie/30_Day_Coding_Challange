# Day 30: WAP to get n elements in an array each m x n and print multiplication of both the matrix.

def multiply_matrices(matrix1, matrix2):
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])

    if cols1 != rows2:
        raise ValueError("Matrix multiplication not possible: columns of Matrix 1 must equal rows of Matrix 2.")
    
    # Resultant matrix of size rows1 x cols2
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    
    # Matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

def print_matrix(matrix, name="Matrix"):
    print(f"\n{name}:")
    for row in matrix:
        print(" ".join(map(str, row)))

# Predefined matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix2 = [
    [7, 8],
    [9, 10],
    [11, 12]
]

# Printing matrices
print_matrix(matrix1, "Matrix 1")
print_matrix(matrix2, "Matrix 2")

# Multiply matrices and print the result
try:
    result = multiply_matrices(matrix1, matrix2)
    print_matrix(result, "Resultant Matrix")
except ValueError as e:
    print(e)
