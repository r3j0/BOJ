import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

graph = [{} for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a][b] = 1
    graph[b][a] = 1

queue = deque()
queue.append(1)
visited = [0 for _ in range(n+1)]
visited[1] = 1

time = 0
while queue:
    size = len(queue)
    
    for s in range(size):
        now = queue.popleft()
        for next in list(graph[now].keys()):
            if visited[next] == 0:
                visited[next] = 1
                queue.append(next)
            
    if time == 1: break
    time += 1
print(sum(visited) - 1)