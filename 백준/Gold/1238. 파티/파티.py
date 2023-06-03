import sys
import heapq
input = sys.stdin.readline

n, m, x = map(int, input().rstrip().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    a -= 1
    b -= 1
    graph[a].append((b, c))

def dijkstra(start):
    distances = {node:int(1e8) for node in range(n)}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (distances[start], start))

    while queue:
        cdi, cde = heapq.heappop(queue)

        if cdi > distances[cde]: continue

        for nde, ndi in graph[cde]:
            di = cdi + ndi
            if di < distances[nde]:
                distances[nde] = di
                heapq.heappush(queue, (di, nde))

    return distances

result_back = dijkstra(x-1)
student_max = 0
for i in range(n):
    result_go = dijkstra(i)
    student_max = max(student_max, result_go[x-1] + result_back[i])

print(student_max)