import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
sight = list(map(int, input().rstrip().split()))

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, t = map(int, input().rstrip().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

def dijkstra():
    distances = {node:int(1e10) for node in range(n)}
    distances[0] = 0
    queue = []
    
    heapq.heappush(queue, (0, 0))

    while queue:
        cdi, cde = heapq.heappop(queue)

        if cdi > distances[cde]: continue
        
        for nde, ndi in graph[cde]:
            di = cdi + ndi
            if (sight[nde] == 0 or nde == n - 1) and distances[nde] > di:
                distances[nde] = di
                heapq.heappush(queue, (di, nde))
    
    return distances

result = dijkstra()[n-1]
print(result if result != int(1e10) else -1)