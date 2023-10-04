import sys
import heapq
input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())
s, d = map(int, input().rstrip().split())
graph = [{} for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().rstrip().split())
    if graph[a].get(b): graph[a][b] = min(graph[a][b], w)
    else: graph[a][b] = w
    if graph[b].get(a): graph[b][a] = min(graph[b][a], w)
    else: graph[b][a] = w

# 도시별로, 1000개 배열을 생성 ( 1000번 도로를 건너서 도착했음을 의미, [지금까지의 거리, 도로 개수] )
# d 에서 세금 올릴때마다 1000개 배열 탐색하면서 보면

dp = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
# dp[i][j] = i 번째 도시까지 j 개 도로를 건넜을 때의 최소 거리

def dijkstra():
    dp[s][0] = 0
    queue = []
    visited = [0 for _ in range(n+1)]
    heapq.heappush(queue, (0, s, 0))

    while queue:
        current_distance, current_destination, current_road = heapq.heappop(queue)
        done = 0
        for i in range(current_road):
            if dp[current_destination][i] < current_distance:
                done = 1
                break
        
        if done == 1 or current_destination == d: continue

        for next_destination, next_distance in graph[current_destination].items():
            if current_distance + next_distance < dp[next_destination][current_road+1]:
                dp[next_destination][current_road+1] = current_distance + next_distance
                heapq.heappush(queue, (current_distance + next_distance, next_destination, current_road + 1))
        
    return

dijkstra()
#for di in dp: print(di)
print(min(dp[d]))

for _ in range(k): 
    p = int(input().rstrip())
    for i in range(n+1):
        if dp[d][i] == float('inf'): continue
        dp[d][i] += p * i
    print(min(dp[d]))