import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]

visited = [[0 for _ in range(n)] for _ in range(n)]

visited[0][0] = 1
queue = deque()
queue.append((0, 0))

done = 0
while queue:
    y, x = queue.popleft()

    if y == n - 1 and x == n - 1:
        done = 1
        break
    if maps[y][x] == 0:
        continue

    if y + maps[y][x] < n:
        queue.append((y+maps[y][x], x))
        visited[y+maps[y][x]][x] = 1
    if x + maps[y][x] < n:
        queue.append((y, x+maps[y][x]))
        visited[y][x+maps[y][x]] = 1
    

if done == 1: print("HaruHaru")
else: print("Hing")