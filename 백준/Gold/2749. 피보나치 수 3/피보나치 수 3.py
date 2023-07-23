import sys
input = sys.stdin.readline

n = int(input().rstrip())
matrix = [[1, 1], [1, 0]]

def matrix_pow(mat, orig):
    new_mat = [[0 for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                new_mat[i][j] += mat[i][k] * orig[k][j]
            new_mat[i][j] %= 1000000
    return new_mat

def solve(mat, now):
    if now <= 1:
        return mat

    now_matrix = solve(mat, now // 2)
    if now % 2 == 1:
        return matrix_pow(matrix_pow(now_matrix, now_matrix), matrix)
    else:
        return matrix_pow(now_matrix, now_matrix)
    
matrix = solve(matrix, n-1)
for i in range(2):
    for j in range(2):
        matrix[i][j] %= 1000000

print(matrix[0][0])