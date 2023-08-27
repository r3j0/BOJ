import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

arr = [[0 for _ in range(m)] for _ in range(n)]
arr[0][0] = 1

row = [0, 1, 0, -1]
col = [1, 0, -1, 0]
dir = 0

cnt = 1
y = 0
x = 0
res = 0
while cnt < n * m:
    ny = y + row[dir]
    nx = x + col[dir]

    if 0 <= ny < n and 0 <= nx < m and arr[ny][nx] == 0:
        y = ny
        x = nx

        arr[ny][nx] = 1
        cnt += 1
    else:
        dir = (dir + 1) % 4
        res += 1

print(res)