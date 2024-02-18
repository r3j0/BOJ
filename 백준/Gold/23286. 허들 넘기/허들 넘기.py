import sys
input = sys.stdin.readline

n, m, t = map(int, input().rstrip().split())
graph = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    u, v, h = map(int, input().rstrip().split())
    graph[u][v] = h

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], max(graph[a][k], graph[k][b]))

for _ in range(t):
    s, e = map(int, input().rstrip().split())
    print(graph[s][e] if graph[s][e] != float('inf') else -1)