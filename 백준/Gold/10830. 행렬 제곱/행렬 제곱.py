import sys
input = sys.stdin.readline

n, b = map(int, input().rstrip().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(n)]

def matrix_pow(mat, orig):
    new_mat = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                new_mat[i][j] += mat[i][k] * orig[k][j]
            new_mat[i][j] %= 1000
    return new_mat

def solve(mat, now):
    if now == 1:
        return mat

    now_matrix = solve(mat, now // 2)
    if now % 2 == 1:
        return matrix_pow(matrix_pow(now_matrix, now_matrix), matrix)
    else:
        return matrix_pow(now_matrix, now_matrix)
    
matrix = solve(matrix, b)
for i in range(n):
    for j in range(n):
        matrix[i][j] %= 1000
for i in range(n): print(' '.join(map(str, matrix[i])))