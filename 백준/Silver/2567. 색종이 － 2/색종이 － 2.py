import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [[0 for _ in range(110)] for _ in range(110)]
for _ in range(n):
    a, b = map(int, input().rstrip().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            arr[i][j] = 1

row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]

res = 0
for i in range(110):
    for j in range(110):
        if arr[i][j] == 1:
            for d in range(4):
                y = i + row[d]
                x = j + col[d]

                if 0 <= y < 110 and 0 <= x < 110 and arr[y][x] == 0:
                    res += 1
print(res)