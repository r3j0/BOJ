import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

maps = {node:[] for node in range(n+1)}
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    maps[a].append(b)
    maps[b].append(a)
    

visited = [0 for _ in range(n+1)]
queue = deque()
visited[1] = 1
queue.append(1)
cnt = 0

while queue:
    size = len(queue)

    for s in range(size):
        now = queue.popleft()

        for a in maps[now]:
            if visited[a] == 0:
                visited[a] = 1
                queue.append(a)
                cnt += 1

print(cnt)