import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
graph_first = [[i for i in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a][b] = min(graph[a][b], c)
    graph[b][a] = min(graph[b][a], c)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                graph_first[a][b] = graph_first[a][k]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            print('-', end=' ')
        else:
            print(graph_first[i][j], end=' ')
    print()