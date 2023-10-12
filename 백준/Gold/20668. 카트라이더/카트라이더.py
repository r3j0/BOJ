import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = {i:{} for i in range(1, n+1)}
for _ in range(m):
    a, b, l, k = map(int, input().rstrip().split())
    
    if not graph[a].get(b): graph[a][b] = []
    graph[a][b].append([l * 3628800, k])
    
    if not graph[b].get(a): graph[b][a] = []
    graph[b][a].append([l * 3628800, k])

def dijkstra(start):
    distances = {node:[float('inf') for _ in range(10)] for node in range(1, n+1)}
    distances[start][0] = 1

    queue = []
    # distance / destination / speed
    heapq.heappush(queue, [0, start, 1])
    while queue:
        current_distance, current_destination, current_speed = heapq.heappop(queue)
        if distances[current_destination][current_speed - 1] < current_distance: continue

        for speed_d in [1, 0, -1]:
            now_speed = current_speed + speed_d
            if now_speed <= 0: continue

            for next_destination, next_item in graph[current_destination].items():
                for next_length, next_limit in next_item:
                    if now_speed > next_limit: continue
                    distance = current_distance + (next_length // now_speed)
                    if distance < distances[next_destination][now_speed - 1]:
                        distances[next_destination][now_speed - 1] = distance
                        heapq.heappush(queue, [distance, next_destination, now_speed])
    return distances

result = min(dijkstra(1)[n])
print(int(result) // 3628800 ,end='.')
result %= 3628800
print(('%.9f'%(result / 3628800))[2:])