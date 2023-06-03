import sys
import heapq
input = sys.stdin.readline
n = int(input().rstrip())
m = int(input().rstrip())

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a-1].append((b-1, c))

start, end = map(int, input().split())
start -= 1
end -= 1

def dijkstra():
    distances = {node:int(1e10) for node in range(n)}
    visited = {node:[] for node in range(n)}
    distances[start] = 0
    visited[start].append(start)
    queue = []
    heapq.heappush(queue, (distances[start], start))

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance: continue

        for next_destination, next_distance in graph[current_node]:
            distance = current_distance + next_distance
            if distance < distances[next_destination]:
                distances[next_destination] = distance
                visited[next_destination] = visited[current_node] + [next_destination]
                heapq.heappush(queue, (distance, next_destination))
    
    return distances, visited

result1, result2 = dijkstra()
print(result1[end])
print(len(result2[end]))
for i in result2[end]:
    print(i+1, end=' ')