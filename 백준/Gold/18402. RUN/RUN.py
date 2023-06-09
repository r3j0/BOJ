import heapq
import sys
input = sys.stdin.readline

n = int(input().rstrip())
e = int(input().rstrip())
t = int(input().rstrip())

m = int(input().rstrip())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, t = map(int, input().rstrip().split())
    graph[a-1].append((b-1, t))

def dijkstra(start):
    distances = {node:int(1e10) for node in range(n)}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        cdi, cde = heapq.heappop(queue)
        if distances[cde] < cdi: continue

        for nde, ndi in graph[cde]:
            di = cdi + ndi
            if di < distances[nde]:
                distances[nde] = di
                heapq.heappush(queue, (di, nde))
    
    return distances

result = 0
for i in range(n):
    res = dijkstra(i)
    if res[e-1] <= t: result += 1

print(result)