from collections import deque
n, m, r = map(int, input().split())

maps = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    maps[u].append(v)
    maps[v].append(u)

q = deque()
q.append(r)

v = [0 for _ in range(n+1)]
v[r] = 1

while q:
    now = q.popleft()
    for next in maps[now]:
        if (v[next] == 0):
            v[next] = v[now] + 1
            q.append(next)

for i in range(1, n+1):
    print(v[i]-1)