# 17244 : 아맞다우산
import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
board = [list(input().rstrip()) for _ in range(n)]

start = [-1, -1, -1]
end = [-1, -1]
cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'S':
            start = [i, j, 0]
        elif board[i][j] == 'E':
            end = [i, j]
        elif board[i][j] == 'X':
            board[i][j] = str(cnt)
            cnt += 1

endb = (1 << cnt) - 1

vis = [[[False for _ in range(32)] for _ in range(m)] for _ in range(n)]
vis[start[0]][start[1]][0] = True

queue = deque()
queue.append(start)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

time = 0
done = False
while queue:
    size = len(queue)
    for _ in range(size):
        now = queue.popleft()

        if now[0] == end[0] and now[1] == end[1] and now[2] == endb:
            done = True
            break

        for d in range(4):
            ny = now[0] + dy[d]
            nx = now[1] + dx[d]

            if 0 <= ny < n and 0 <= nx < m and board[ny][nx] != '#':
                # 물건 소지
                if '0' <= board[ny][nx] <= '4':
                    nb = now[2] | (1 << int(board[ny][nx]))
                    if not vis[ny][nx][nb]:
                        vis[ny][nx][nb] = True
                        queue.append([ny, nx, nb])

                # 물건 미소지
                if not vis[ny][nx][now[2]]:
                    vis[ny][nx][now[2]] = True
                    queue.append([ny, nx, now[2]])
    if done: break
    time += 1

print(time)