import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
maps = [list(input().rstrip()) for _ in range(n)]
graph = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j: continue
        if maps[i][j] == 'Y': graph[i].append(j)

visited = [0 for _ in range(50)]
max_cnt = 0
for i in range(n):
    queue = deque()
    queue.append(i)
    visited[i] = i+1
    time = 0
    cnt = -1
    while queue and time <= 2:
        size = len(queue)
        for s in range(size):
            now = queue.popleft()
            cnt += 1
            for next in graph[now]:
                if visited[next] != i+1:
                    visited[next] = i+1
                    queue.append(next)
        time += 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)