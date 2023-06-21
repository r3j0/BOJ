import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]

onepos = []
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            onepos.append((i, j))

print(abs(onepos[0][0]-onepos[1][0])+abs(onepos[0][1]-onepos[1][1]))