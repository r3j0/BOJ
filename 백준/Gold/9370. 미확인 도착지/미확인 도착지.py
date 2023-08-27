import sys
import heapq
input = sys.stdin.readline

def dijkstra(g, start):
    distances = {node:20000000 for node in list(g.keys())}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in g[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])
    return distances

testcase = int(input().rstrip())
for _ in range(testcase):
    # 교차로의 개수, 도로의 개수, 목적지 후보의 개수
    n, m, t = map(int, input().rstrip().split())
    # 예술가들의 출발지, g와 h를 지나감
    s, g, h = map(int, input().rstrip().split())

    graph = {node:{} for node in range(1, n+1)}
    for _ in range(m):
        # a와 b 사이에 길이 d의 양방향 도로가 있다
        a, b, d = map(int, input().rstrip().split())
        if graph[a].get(b): graph[a][b] = min(graph[a][b], d)
        else: graph[a][b] = d
        if graph[b].get(a): graph[b][a] = min(graph[b][a], d)
        else: graph[b][a] = d
    
    # 목적지 후보
    destination = []
    for _ in range(t):
        destination.append(int(input().rstrip()))
    destination.sort()
    
    # 출발지 -> g / h -> 목적지 후보들
    # 출발지 -> h / g -> 목적지 후보들
    # 만약 목적지 후보들보다 큰 거리면 출력 X
    start_dist = dijkstra(graph, s)
    g_dist = dijkstra(graph, g)
    h_dist = dijkstra(graph, h)
    result = []
    for d in destination:
        if start_dist[g] + graph[g][h] + h_dist[d] <= start_dist[d]:
            result.append(d)
        elif start_dist[h] + graph[h][g] + g_dist[d] <= start_dist[d]:
            result.append(d)
    
    print(' '.join(map(str, result)))