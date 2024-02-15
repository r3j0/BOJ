import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().rstrip().split())
    if i == k - 1: continue
    graph[a].append(b)
    graph[b].append(a)

vis = [0 for _ in range(n+1)]
res = 1
for i in range(1, n+1):
    if vis[i] == 0:
        vis[i] = 1
        cnt = 1
        queue = deque()
        queue.append(i)
        while queue:
            now = queue.popleft()
            for next in graph[now]:
                if vis[next] == 0:
                    vis[next] = 1
                    cnt += 1
                    queue.append(next)
        
        if cnt == n: res = 0
        else: res *= cnt

print(res)