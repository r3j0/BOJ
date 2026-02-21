from collections import deque
n = int(input())
maps = [list(input()) for _ in range(n)]

vis = [[0 for _ in range(n)] for _ in range(n)]
vis[0][0] = 1

queue = deque()
queue.append([0, 0])

dy = [1, 0]
dx = [0, 1]
done = False
while queue:
    now = queue.popleft()
    if now == [n-1, n-1]:
        done = True
        break

    for d in range(2):
        ny = now[0] + dy[d]
        nx = now[1] + dx[d]

        if 0 <= ny < n and 0 <= nx < n and vis[ny][nx] == 0 and maps[ny][nx] == '.':
            queue.append([ny, nx])
            vis[ny][nx] = 1

print('Yes' if done else 'No')