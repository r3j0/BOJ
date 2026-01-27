# 2583 : 영역 구하기
import sys
from collections import deque
input = sys.stdin.readline

m, n, k = map(int, input().rstrip().split())
maps = [[False for _ in range(m)] for _ in range(n)]
for _ in range(k):
    lx, ly, rx, ry = map(int, input().rstrip().split())
    for i in range(lx, rx, 1):
        for j in range(ly, ry, 1):
            maps[i][j] = True
    
vis = [[False for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
ans = []

for i in range(n):
    for j in range(m):
        if maps[i][j] == False and vis[i][j] == False:
            vis[i][j] = True
            cnt += 1

            s = 1
            queue = deque()
            queue.append([i, j])
            while queue:
                now = queue.popleft()
                for d in range(4):
                    nx = now[0] + dx[d]
                    ny = now[1] + dy[d]

                    if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == False and vis[nx][ny] == False:
                        s += 1
                        vis[nx][ny] = True
                        queue.append([nx, ny])
            
            ans.append(s)

ans.sort()
print(cnt)
print(' '.join(map(str, ans)))