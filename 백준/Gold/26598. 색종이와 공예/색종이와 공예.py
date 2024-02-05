import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
maps = [list(input().rstrip()) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]
def BFS(start_y, start_x):
    queue = deque()
    queue.append([start_y, start_x])
    focusing = maps[start_y][start_x]
    visited[start_y][start_x] = 1

    left = m
    right = -1
    up = n
    down = -1

    cnt = 1
    while queue:
        now = queue.popleft()
        left = min(left, now[1])
        right = max(right, now[1])
        up = min(up, now[0])
        down = max(down, now[0])

        for d in range(4):
            ny = now[0] + row[d]
            nx = now[1] + col[d]

            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0 and maps[ny][nx] == focusing:
                cnt += 1
                visited[ny][nx] = 1
                queue.append([ny, nx])
    
    return [cnt, left, right, up, down]

result = True
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            result_cnt, left, right, up, down = BFS(i, j)

            if (right - left + 1) * (down - up + 1) != result_cnt:
                result = False
                break
    
    if result == False: break

print('BaboBabo' if result == False else 'dd')