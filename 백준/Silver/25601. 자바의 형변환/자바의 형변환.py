import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
graph = {}
for _ in range(n-1):
    a, b = input().rstrip().split()
    if graph.get(b, -1) == -1:
        graph[b] = {a:1}
    else:
        graph[b][a] = 1
    if graph.get(a, -1) == -1:
        graph[a] = {}

a, b = input().rstrip().split()
res = 0
def DFS(start, end):
    global res
    queue = deque()
    queue.append(start)
    while queue:
        now = queue.popleft()
        if end == now: 
            res = 1
            break
        for next in list(graph[now].keys()):
            queue.append(next)

DFS(a, b)
DFS(b, a)
print(res)