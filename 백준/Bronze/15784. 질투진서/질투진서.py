import sys
input = sys.stdin.readline

n, a, b = map(int, input().rstrip().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]

maxrow = max(maps[a-1])
maxcol = maps[0][b-1]
for i in range(1, n):
    maxcol = max(maxcol, maps[i][b-1])

if maxrow == maxcol == maps[a-1][b-1]: print('HAPPY')
else: print('ANGRY')