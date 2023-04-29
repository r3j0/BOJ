import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]
row = [-1,1,0,0]
col = [0,0,-1,1]

cnt = 0
for i in range(n):
    for j in range(m):
        if maps[i][j] == '*' and visit[i][j] == 0:
            cnt += 1
            
            queue = deque()
            queue.append([i, j])
            while queue:
                size = len(queue)
                for s in range(size):
                    y, x = queue.popleft()
                    for d in range(4):
                        ny = y + row[d]
                        nx = x + col[d]

                        if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == '*' and visit[ny][nx] == 0:
                            visit[ny][nx] = 1
                            queue.append([ny, nx])

print(cnt)
