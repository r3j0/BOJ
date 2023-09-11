import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())
big_graph = [{} for _ in range(n+1)]
small_graph = [{} for _ in range(n+1)]
m = int(input().rstrip())
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    big_graph[a][b] = 1
    small_graph[b][a] = 1

def big_dijkstra(start):
    distances = {node:float('inf') for node in range(n+1)}
    distances[start] = 0

    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance: continue

        for next_destination, next_distance in big_graph[current_destination].items():
            distance = current_distance + next_distance
            if distance < distances[next_destination]:
                distances[next_destination] = distance
                heapq.heappush(queue, (distance, next_destination))
    
    return distances
def small_dijkstra(start):
    distances = {node:float('inf') for node in range(n+1)}
    distances[start] = 0

    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance: continue

        for next_destination, next_distance in small_graph[current_destination].items():
            distance = current_distance + next_distance
            if distance < distances[next_destination]:
                distances[next_destination] = distance
                heapq.heappush(queue, (distance, next_destination))
    
    return distances

for i in range(1, n+1):
    result1 = list(big_dijkstra(i).values())
    result2 = list(small_dijkstra(i).values())

    cnt = 0
    for i in range(1, n+1):
        if result1[i] == result2[i] == float('inf'):
            cnt += 1
    
    print(cnt)