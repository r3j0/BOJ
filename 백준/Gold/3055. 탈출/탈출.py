import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
maps = [list(input().rstrip()) for _ in range(n)]

startPos = [0, 0]
endPos = [0, 0]
waterPos = []

for i in range(n):
    for j in range(m):
        if maps[i][j] == 'S': startPos = [i, j]
        elif maps[i][j] == 'D': endPos = [i, j]
        elif maps[i][j] == '*': waterPos.append([i, j])

visited = [[0 for j in range(m)] for i in range(n)]

queue = deque()
queue.append(startPos)
visited[startPos[0]][startPos[1]] = 1

wqueue = deque()
for w in waterPos: wqueue.append(w)

row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]

done = 0
time = 0
while queue:
    size = len(queue)

    for s in range(size):
        y, x = queue.popleft()

        if y == endPos[0] and x == endPos[1]: 
            done = 1
            break

        for d in range(4):
            ny = y + row[d]
            nx = x + col[d]

            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0 and maps[ny][nx] != 'X' and maps[ny][nx] != '*':
                existWater = 0
                if maps[ny][nx] != 'D':
                    for e in range(4):
                        wny = ny + row[e]
                        wnx = nx + col[e]

                        if 0 <= wny < n and 0 <= wnx < m and maps[wny][wnx] == '*':
                            existWater = 1
                            break
                
                if existWater == 0:
                    queue.append([ny, nx])
                    visited[ny][nx] = 1
    
    if done == 1: break
    time += 1

    wsize = len(wqueue)
    for ws in range(wsize):
        wy, wx = wqueue.popleft()

        for d in range(4):
            wwy = wy + row[d]
            wwx = wx + col[d]

            if 0 <= wwy < n and 0 <= wwx < m and maps[wwy][wwx] == '.':
                maps[wwy][wwx] = '*'
                wqueue.append([wwy, wwx])


if done == 0: print('KAKTUS')
else: print(time)