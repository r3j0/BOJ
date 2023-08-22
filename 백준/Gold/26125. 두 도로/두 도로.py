import sys
import copy
input = sys.stdin.readline

n, m, s, t = map(int, input().rstrip().split())
graph = [[float('inf')] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a][b] = min(graph[a][b], c)

now_graph = [[float('inf')] * (n+1) for _ in range(n+1)]

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

q = int(input().rstrip())

for _ in range(q):
    a1, b1, c1, a2, b2, c2 = map(int, input().rstrip().split())
    result = min(min(graph[s][t], graph[s][a1] + min(c1, graph[a1][b1]) + graph[b1][t], graph[s][a2] + min(c2, graph[a2][b2]) + graph[b2][t]), min(graph[s][a1] + min(c1, graph[a1][b1]) + graph[b1][a2] + min(c2, graph[a2][b2]) + graph[b2][t], graph[s][a2] + min(c2, graph[a2][b2]) + graph[b2][a1] + min(c1, graph[a1][b1]) + graph[b1][t]))
    print(result if result != float('inf') else -1)