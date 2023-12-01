import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]

start = [0, 0]
for i in range(n):
    for j in range(n):
        if maps[i][j] == 9:
            start = [i, j]
            maps[i][j] = 0
            break

row = [-1, 0, 1, 0]
col = [0, -1, 0, 1]

def bfs(s, szc):
    global maps
    global row
    global col
    queue = deque()
    queue.append(s)
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[s[0]][s[1]] = 1

    t = 0
    resarr = []
    while queue:
        size = len(queue)
        done = 0
        for i in range(size):
            now = queue.popleft()

            if maps[now[0]][now[1]] != 0:
                if maps[now[0]][now[1]] < szc:
                    done = 1
                    resarr.append(now)
                elif maps[now[0]][now[1]] > szc:
                    continue
            for d in range(4):
                ny = now[0] + row[d]
                nx = now[1] + col[d]

                if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == 0:
                    queue.append([ny, nx])
                    visited[ny][nx] = 1
        if done: break        
        t += 1
    
    res = []
    if len(resarr) > 0:
        resarr.sort(key=lambda x:(x[0], x[1]))
        res = resarr[0]

    if len(res) == 0: return res, -1
    else: return res, t

sz = 2
szct = 0
sumtime = 0
while True:
    result, time = bfs(start, sz)
    if time == -1: break
    sumtime += time
    start = result
    maps[start[0]][start[1]] = 0
    szct += 1

    if sz == szct:
        sz += 1
        szct = 0

print(sumtime)