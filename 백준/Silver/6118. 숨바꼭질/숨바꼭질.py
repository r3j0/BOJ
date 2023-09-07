import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [{} for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dijkstra():
    global graph
    distances = {node:float('inf') for node in range(n+1)}
    distances[1] = 0

    queue = []
    heapq.heappush(queue, (0, 1))

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance: continue

        for next_destination, _ in graph[current_destination].items():
            if distances[current_destination] + 1 < distances[next_destination]:
                distances[next_destination] = distances[current_destination] + 1
                heapq.heappush(queue, (distances[next_destination], next_destination))

    return distances

result = dijkstra()
min_hut = -1
min_value = 0
min_another = 0
for i in range(1, n+1):
    if min_value < result[i] and result[i] != float('inf'):
        min_hut = i
        min_value = result[i]
        min_another = 1
    elif min_value == result[i]:
        min_another += 1

print(min_hut, min_value, min_another)