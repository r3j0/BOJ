# 14846 : 직사각형과 쿼리
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

sums = [[[0 for _ in range(11)] for _ in range(n+1)] for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        sums[i+1][j+1][arr[i][j]] += 1
        for k in range(1, 11):
            sums[i+1][j+1][k] += sums[i][j+1][k] + sums[i+1][j][k] - sums[i][j][k]

q = int(input().rstrip())
for _ in range(q):
    x1, y1, x2, y2 = map(int, input().rstrip().split())

    cnt = 0
    for k in range(1, 11):
        now = sums[x2][y2][k] - sums[x1-1][y2][k] - sums[x2][y1-1][k] + sums[x1-1][y1-1][k]
        if now > 0: cnt += 1
    
    print(cnt)