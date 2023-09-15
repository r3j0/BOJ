import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
maps = [list(input().rstrip()) for _ in range(n)]
new_maps = [['.' for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if maps[i][j] == '.': continue
        if j < m//2:
            new_maps[i][j] = maps[i][j]
            new_maps[i][m-1-j] = maps[i][j]
        else:
            new_maps[i][j] = maps[i][j]
            new_maps[i][m-1-j] = maps[i][j]

for nm in new_maps:
    print(''.join(nm))