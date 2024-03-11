import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]

row = [-1, 1, 0, 0, -1, -1, 1, 1]
col = [0, 0, -1, 1, -1, 1, -1, 1]
res = 0
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1: continue
        visited = [[0 for _ in range(m)] for _ in range(n)]
        visited[i][j] = 1
        queue = deque()
        queue.append([i, j])

        time = 0
        done = 0
        while queue:
            size = len(queue)
            for s in range(size):
                now = queue.popleft()
                if maps[now[0]][now[1]] == 1: 
                    done = 1
                    break 
                for d in range(8):
                    ny = now[0] + row[d]
                    nx = now[1] + col[d]

                    if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0:
                        visited[ny][nx] = 1
                        queue.append([ny, nx])
            time += 1
            if done == 1: break
        
        res = max(res, time-1)

print(res)
                