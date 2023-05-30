import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

graph = [[] for _ in range(n+1)]

for _ in range(m):
	s, e, c = map(int, input().rstrip().split())
	graph[s].append((e, c))

start, end = map(int, input().split())

def dijkstra(graph, start):
	global n
	distances = [int(1e10)] * (n+1)
	distances[start] = 0
	queue = []
	heapq.heappush(queue, [distances[start], start])

	while queue:
		current_distance, current_destination = heapq.heappop(queue)

		if distances[current_destination] < current_distance:
			continue

		for next_destination, next_distance in graph[current_destination]:
			distance = current_distance + next_distance
			if distance < distances[next_destination]:
				distances[next_destination] = distance
				heapq.heappush(queue, [distance, next_destination])

	return distances

result = dijkstra(graph, start)
print(result[end])