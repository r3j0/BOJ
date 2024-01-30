import sys
input = sys.stdin.readline

n, m, x = map(int, input().rstrip().split())
maps = [['.' for _ in range(m)] for _ in range(n)]
arr = list(map(int, input().rstrip().split()))

for i in range(m):
    for j in range(arr[i]):
        if n - 1 - j < 0: break
        maps[n-1-j][i] = '#'

for j in range(m):
    if maps[n-x][j] == '#': maps[n-x][j] = '*'
    else: maps[n-x][j] = '-'
    if (j+1)%3 == 0:
        now_y = n-x+1
        while now_y < n and maps[now_y][j] == '.':
            maps[now_y][j] = '|'
            now_y += 1

for i in range(n): print(''.join(maps[i]))