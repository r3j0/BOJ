import sys
import math
input = sys.stdin.readline

string = input().rstrip()

max_idx = 0
for i in range(1, int(math.sqrt(len(string)))+1):
    if len(string) % i == 0 and i <= math.sqrt(len(string)):
        max_idx = max(max_idx, i)

matrix = [['' for _ in range(len(string) // max_idx)] for _ in range(max_idx)]

cnt = 0
for j in range(len(string) // max_idx):
    for i in range(max_idx):
        matrix[i][j] = string[cnt]
        cnt += 1

for i in range(max_idx):
    print(''.join(matrix[i]), end='')