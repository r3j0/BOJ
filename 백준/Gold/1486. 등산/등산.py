import sys
import heapq
input = sys.stdin.readline

n, m, t, d = map(int, input().rstrip().split())
maps = [list(input().rstrip()) for _ in range(n)]

row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]

height = {chr(ord('A')+i):i for i in range(26)}
for i in range(26):
    height[chr(ord('a')+i)] = 26+i

graph = [[{} for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        for dir in range(4):
            ny = i + row[dir]
            nx = j + col[dir]

            if 0 <= ny < n and 0 <= nx < m:
                now_height = height[maps[i][j]]
                go_height = height[maps[ny][nx]]
                if (abs(now_height - go_height) > t): continue
                if now_height >= go_height:
                    graph[i][j][str(ny)+"_"+str(nx)] = 1 
                else:
                    graph[i][j][str(ny)+"_"+str(nx)] = (now_height - go_height) ** 2
def dijkstra(sy, sx):
    distances = [[float('inf') for _ in range(m)] for _ in range(n)]
    distances[sy][sx] = 0
    queue = []
    heapq.heappush(queue, (0, sy, sx))

    while queue:
        current_distance, current_y, current_x = heapq.heappop(queue)

        if current_distance > distances[current_y][current_x]: continue

        for next_destination, next_distance in graph[current_y][current_x].items():
            ny, nx = map(int, next_destination.split('_'))
            if current_distance + next_distance < distances[ny][nx]:
                distances[ny][nx] = current_distance + next_distance
                heapq.heappush(queue, (current_distance + next_distance, ny, nx))
    
    return distances

result = dijkstra(0, 0)

max_height = height[maps[0][0]]
for i in range(n):
    for j in range(m):
        if i == j == 0: continue
        now_result = dijkstra(i, j)
        if result[i][j] + now_result[0][0] > d: continue
        max_height = max(max_height, height[maps[i][j]])
print(max_height)