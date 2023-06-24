import sys
from collections import deque
input = sys.stdin.readline

maps = [list(input().rstrip()) for _ in range(10)]

sp = []
ep = []
for i in range(10):
    for j in range(10):
        if maps[i][j] == 'B': sp = [i, j]
        if maps[i][j] == 'L': ep = [i, j]

visit = [[0 for _ in range(10)] for _ in range(10)]

queue = deque()
queue.append(sp)
visit[sp[0]][sp[1]] = 1

col = [-1, 1, 0, 0]
row = [0, 0, -1, 1]
cnt = 0
while queue:
    size = len(queue)
    done = 0
    for _ in range(size):
        y, x = queue.popleft()

        if y == ep[0] and x == ep[1]:
            done = 1
            break

        for d in range(4):
            ny = y + row[d]
            nx = x + col[d]
            if 0 <= ny < 10 and 0 <= nx < 10 and visit[ny][nx] == 0 and maps[ny][nx] != 'R':
                queue.append([ny, nx])
                visit[ny][nx] = 1
    if done == 1: break

    cnt += 1

print(cnt-1)