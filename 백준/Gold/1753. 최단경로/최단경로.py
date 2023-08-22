import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().rstrip().split())
graph = {node:{} for node in range(1,v+1)}
k = int(input().rstrip())
for _ in range(e):
    st, en, w = map(int, input().rstrip().split())
    if graph[st].get(en): graph[st][en] = min(graph[st][en], w)
    else: graph[st][en] = w

def dijkstra(graph, start):
    distances = {node: float(1e10) for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])
        
    return distances

result = dijkstra(graph, k)
for i in range(v):
    print(result[i+1] if result[i+1] != float(1e10) else 'INF')