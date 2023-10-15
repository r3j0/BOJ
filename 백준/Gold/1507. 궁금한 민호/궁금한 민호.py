import sys
input = sys.stdin.readline

n = int(input().rstrip())
graph = [[float('inf')] + list(map(int, input().rstrip().split())) for _ in range(n)]
graph.insert(0, [float('inf')]*(n+1))
cur_graph = []
for g in graph: cur_graph.append(list(g))

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b or a == k or b == k or graph[a][b] == float('inf') or graph[a][k] == float('inf') or graph[k][b] == float('inf'): continue
            if graph[a][b] == graph[a][k] + graph[k][b]:
                graph[a][b] = float('inf')

sums = 0
for i in range(1, n+1):
    for j in range(1, i):
        if graph[i][j] == float('inf'): continue
        sums += graph[i][j]

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][k] == float('inf') or graph[k][b] == float('inf'): continue
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

if cur_graph == graph: print(sums)
else: print(-1)