import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
arr = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    for x in range(x1-1, x2):
        for y in range(y1-1, y2):
            arr[x][y] += 1

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] > m: cnt += 1
print(cnt)