import sys
input = sys.stdin.readline

r, c = map(int, input().rstrip().split())
rg, cg, rp, cp = map(int, input().rstrip().split())
maps = [list(input().rstrip()) for _ in range(r)]
pc = 0
for i in range(r):
    for j in range(c):
        if maps[i][j] == 'P': pc+=1

if pc == rp * cp: print(0)
else: print(1) 