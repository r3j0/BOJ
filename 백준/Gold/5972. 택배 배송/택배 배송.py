import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    a -= 1
    b -= 1
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra():
    distances = {node:int(1e10) for node in range(n)}
    distances[0] = 0
    queue = []
    heapq.heappush(queue, (distances[0], 0))

    while queue:
        cdi, cde = heapq.heappop(queue)

        if cdi > distances[cde]: continue

        for nde, ndi in graph[cde]:
            di = cdi + ndi
            if di < distances[nde]:
                distances[nde] = di
                heapq.heappush(queue, (di, nde))
    
    return distances

result = dijkstra()
print(result[n-1])