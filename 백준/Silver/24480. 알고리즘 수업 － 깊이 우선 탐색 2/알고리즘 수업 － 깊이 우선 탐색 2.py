import sys
sys.setrecursionlimit(10**5+(10**4*5))
input = sys.stdin.readline

n, m, r = map(int, input().rstrip().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

visited = [0 for _ in range(n)]

visited[r-1] = 1
now = 2
def dfs(n):
    global now
    for g in sorted(graph[n], reverse=True):
        if visited[g] == 0:
            visited[g] = now
            now += 1
            dfs(g)

dfs(r-1)
for v in visited: print(v)