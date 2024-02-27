import sys
import heapq
input = sys.stdin.readline

n, m, a, b, c = map(int, input().rstrip().split())
graph = [{} for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int, input().rstrip().split())
    graph[x][y] = z
    graph[y][x] = z

def dijkstra(start):
    global b
    global c
    arr = [float('inf') for _ in range(n+1)]
    arr[start] = 0
    backtrack = [[-1, -1] for _ in range(n+1)]
    # 어디서 왔는가, 최대는 몇인가
    backtrack[start] = [-1, 0]
    queue = []
    heapq.heappush(queue, [0, start])

    while queue:
        now_weight, now_location = heapq.heappop(queue)

        for next_location, next_weight in list(graph[now_location].items()):
            if arr[next_location] > arr[now_location] + next_weight and arr[now_location] + next_weight <= c:
                arr[next_location] = arr[now_location] + next_weight
                heapq.heappush(queue, [arr[next_location], next_location])

            if backtrack[next_location] == [-1, -1]:
                backtrack[next_location] = [now_location, max(backtrack[now_location][1], next_weight)]
            else:
                if backtrack[next_location][1] > max(backtrack[now_location][1], next_weight):
                    backtrack[next_location] = [now_location, max(backtrack[now_location][1], next_weight)]
    #print(arr)
    #print(backtrack)
    if arr[b] <= c:
        print(backtrack[b][1])
    else:
        print(-1)

dijkstra(a)

        