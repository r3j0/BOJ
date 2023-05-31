import sys
import heapq
input = sys.stdin.readline

test = int(input().rstrip())

def dijkstra(graph, start, n):
    distances = [1e10] * (n+1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (distances[start], start))

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if current_distance > distances[current_destination]:
            continue
            
        for next_destination, next_distance in graph[current_destination]:
            distance = current_distance + next_distance
            if distance < distances[next_destination]:
                distances[next_destination] = distance
                heapq.heappush(queue, (distance, next_destination))

    return distances

for _ in range(test):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
    result = dijkstra(graph, c, n)
    cnt = 0
    max_time = 0
    for r in result:
        if r != 1e10:
            cnt += 1
            max_time = max(max_time, r)
    print(cnt, max_time)