import sys
import heapq
input = sys.stdin.readline

def dijkstra(city_num, start):
    distances = [float('inf') for _ in range(city_num)]
    distances[start] = 0
    distances_path = [set() for _ in range(city_num)]
    
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance: continue

        for next_destination, next_distance in graph[current_destination].items():
            if current_distance + next_distance <= distances[next_destination]:
                if current_distance + next_distance < distances[next_destination]:
                    distances[next_destination] = current_distance + next_distance
                    distances_path[next_destination] = set()
                    heapq.heappush(queue, (current_distance + next_distance, next_destination))
                now_path = "%d_%d"%(current_destination, next_destination)
                if len(distances_path[current_destination]) > 0:
                    for i in distances_path[current_destination]:
                        distances_path[next_destination].add(i)
                distances_path[next_destination].add(now_path)
    
    return distances, distances_path

def dijkstra_dist(city_num, start):
    distances = [float('inf') for _ in range(city_num)]
    distances[start] = 0
    
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance: continue

        for next_destination, next_distance in graph[current_destination].items():
            if current_distance + next_distance < distances[next_destination]:
                distances[next_destination] = current_distance + next_distance
                heapq.heappush(queue, (current_distance + next_distance, next_destination))
    
    return distances

while True:
    n, m = map(int, input().rstrip().split())
    if n == m == 0: break

    s, d = map(int, input().rstrip().split())
    graph = [{} for _ in range(n)]

    for _ in range(m):
        u, v, p = map(int, input().rstrip().split())
        graph[u][v] = p
    
    # 1. 최단 경로 구하기
    result, result_path = dijkstra(n, s)

    # 2. 최단 경로에 포함된 도로 지우기
    for now_path in result_path[d]:
        left, right = map(int, now_path.split('_'))
        if graph[left].get(right):
            del graph[left][right]

    # 3. 다시 최단 경로 구하기
    result = dijkstra_dist(n, s)
    print(result[d] if result[d] != float('inf') else -1)