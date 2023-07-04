import sys
input = sys.stdin.readline

n = int(input().rstrip())
maps = [list(input().rstrip()) for _ in range(n)]

row = [0 for _ in range(n)]
col = [0 for _ in range(n)]

for i in range(n):
    for j in range(n):
        if maps[i][j] == 'W':
            row[i] = 1
            col[j] = 1

for i in range(n):
    for j in range(n):
        if row[i] == 0 and col[j] == 0:
            maps[i][j] = 'W'
            row[i] = 1
            col[j] = 1
            break

for i in range(n):
    print(''.join(maps[i]))