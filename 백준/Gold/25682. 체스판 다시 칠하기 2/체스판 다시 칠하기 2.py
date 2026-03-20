# 체스판 다시 칠하기 2
import sys
input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())
arr = [list(input().rstrip()) for _ in range(n)]

char = ['B', 'W']
sums = [[[0 for _ in range(2)] for _ in range(m+1)] for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        # 1. LeftUp Black
        if char[(i + j) % 2] != arr[i][j]:
            sums[i+1][j+1][0] += 1
        
        # 2. LeftUp White
        if char[((i + j) % 2) ^ 1] != arr[i][j]:
            sums[i+1][j+1][1] += 1

ans = n * m
for i in range(1, n+1):
    for j in range(1, m+1):
        for p in range(2):
            sums[i][j][p] += sums[i-1][j][p] + sums[i][j-1][p] - sums[i-1][j-1][p]

            if i - k >= 0 and j - k >= 0:
                now = sums[i][j][p] - sums[i-k][j][p] - sums[i][j-k][p] + sums[i-k][j-k][p]
                ans = min(ans, now)

print(ans)