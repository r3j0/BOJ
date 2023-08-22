import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
graph = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == float('inf'): print(0, end=' ')
        else: print(graph[a][b], end=' ')
    print()