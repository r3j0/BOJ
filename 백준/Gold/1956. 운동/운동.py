import sys
input = sys.stdin.readline

v, e = map(int, input().rstrip().split())
graph = [[float('inf') for _ in range(v+1)] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().rstrip().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, v+1):
    for a in range(1, v+1):
        for b in range(1, v+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

min_dist = float('inf')
for a in range(1, v+1):
    for b in range(1, v+1):
        if graph[a][b] != float('inf') and graph[b][a] != float('inf'):
            min_dist = min(min_dist, graph[a][b] + graph[b][a])

print(min_dist if min_dist != float('inf') else -1)