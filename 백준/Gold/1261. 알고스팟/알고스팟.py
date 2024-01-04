import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
maps = [list(input().rstrip()) for _ in range(n)]
wall_cnt = 0
for i in range(n):
    for j in range(m):
        wall_cnt += (1 if maps[i][j] == '1' else 0)

visited = [[n*m+1 for _ in range(m)] for _ in range(n)]
visited[0][0] = 0

queue = deque()
queue.append([0, 0, 0])

row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]
while queue:
    y, x, c = queue.popleft()
    for d in range(4):
        ny = y + row[d]
        nx = x + col[d]

        if 0 <= ny < n and 0 <= nx < m:
            if maps[ny][nx] == '1' and c+1 <= wall_cnt and visited[ny][nx] > c+1:
                visited[ny][nx] = c+1
                queue.append([ny, nx, c+1])
            elif maps[ny][nx] == '0' and visited[ny][nx] > c:
                visited[ny][nx] = c
                queue.append([ny, nx, c])

print(visited[n-1][m-1])