
# sum of primary diaginal



def matrix(A):
    n = len(A)
    primary_diaginal = 0
    secondary_diagonal = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            if i == j:
                print(A[i][j])
                primary_diaginal += A[i][j]
                #secondary_diagonal += A[i][n - i - 1]
    return primary_diaginal





A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix(A))
print()
# sum of secondary diagonal

def sum_secondary_diaginal(B):
    n = len(B)
    sum = 0
    for i in range(len(B)):
        for j in range(len(B[i])):
            if i + j == (n-1):
                print(B[i][j])
                sum += B[i][j]
    return sum

B = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(sum_secondary_diaginal(B))
print()
# sum of diagonals

def diagonal_sum(matrix):
    res = 0
    n = len(matrix)
    for i in range(len(matrix)):
        res += matrix[i][i]  # primary diagonal
        res += matrix[i][len(matrix) - 1 - i] # secondary diagonal

    return res - (matrix[n // 2][n // 2] if n % 2 else 0)

matrix1 = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

matrix2 = [
    [11, 22, 33, 44],
    [55, 66, 77, 88],
    [99, 111, 222, 333]
]

print(diagonal_sum(matrix1))
print(diagonal_sum(matrix2))