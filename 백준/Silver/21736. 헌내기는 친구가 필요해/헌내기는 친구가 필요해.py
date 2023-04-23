import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(input().rstrip()) for _ in range(n)]

doyeonPos = []
for i in range(n):
    for j in range(m):
        if maps[i][j] == 'I':
            doyeonPos = [i, j]
            break
    
    if len(doyeonPos) != 0: break

queue = deque()
queue.append(doyeonPos)

visit = [[0 for j in range(m)] for i in range(n)]
visit[doyeonPos[0]][doyeonPos[1]] = 1

result = 0

row = [-1,1,0,0]
col = [0,0,-1,1]

while queue:
    size = len(queue)

    for s in range(size):
        y, x = queue.popleft()

        if maps[y][x] == 'P': result += 1

        for d in range(4):
            ny = y + row[d]
            nx = x + col[d]

            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != 'X' and visit[ny][nx] == 0:
                visit[ny][nx] = 1

                queue.append([ny, nx])

if result == 0: print('TT')
else: print(result)