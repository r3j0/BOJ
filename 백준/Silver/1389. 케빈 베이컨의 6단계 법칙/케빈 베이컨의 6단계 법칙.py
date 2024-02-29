import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

res_num = -1
res_value = -1
for i in range(1, n+1):
    queue = deque()
    queue.append(i)
    res = 0
    vis = [0 for _ in range(n+1)]
    vis[i] = 1
    time = 0
    while queue:
        size = len(queue)
        for s in range(size):
            now = queue.popleft()
            if time > 0: res += time
            for next in graph[now]:
                if vis[next] == 0:
                    vis[next] = 1
                    queue.append(next)
        time += 1
    if res_num == -1:
        res_num = i
        res_value = res
    else:
        if res_value > res:
            res_num = i
            res_value = res

print(res_num)