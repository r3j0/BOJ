import sys
import heapq
input = sys.stdin.readline

n, e = map(int, input().rstrip().split())
graph = [[] for _ in range(n)]
for _ in range(e):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    distances = {node:int(1e10) for node in range(n)}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (distances[start], start))

    while queue:
        cdi, cde = heapq.heappop(queue)

        if distances[cde] < cdi: continue

        for nde, ndi in graph[cde]:
            di = cdi + ndi
            if di < distances[nde]:
                distances[nde] = di
                heapq.heappush(queue, (di, nde))

    return distances

v1, v2 = map(int, input().rstrip().split())
v1 -= 1
v2 -= 1

goCost = 0
for i in graph[v1]:
    if i[0] == v2:
        goCost = i[1]
        break
result1 = dijkstra(0)
result2 = dijkstra(v2)
result3 = dijkstra(v1)
if result1[v1] == int(1e10) or result3[v2] == int(1e10) or result2[n-1] == int(1e10):
    if result1[v2] == int(1e10) or result2[v1] == int(1e10) or result3[n-1] == int(1e10):
        print(-1)
    else:
        print(result1[v2] + result2[v1] + result3[n-1])
else:
    if result1[v2] == int(1e10) or result2[v1] == int(1e10) or result3[n-1] == int(1e10):
        print(result1[v1] + result3[v2] + result2[n-1])
    else:
        print(min(result1[v1] + result3[v2] + result2[n-1], result1[v2] + result2[v1] + result3[n-1]))
        