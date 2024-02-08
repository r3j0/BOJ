import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]

# 1. BFS 로 영역 탐색 및 노드 번호 부여
# 2. A -> B 영역 거리 탐색 및 기록 ( 2 이상 거리, 가로 세로 여야 함 )
# 3. kruskal MST 로 모든 노드가 유파로 연결 되었는지 체크

visited_mapnum = [[0 for _ in range(m)] for _ in range(n)]
row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]

node_num = 1
node_map = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1 and visited_mapnum[i][j] == 0:
            visited_mapnum[i][j] = 1
            node_map[i][j] = node_num
            queue = deque()
            queue.append([i, j])

            while queue:
                now = queue.popleft()

                for d in range(4):
                    ny = now[0] + row[d]
                    nx = now[1] + col[d]

                    if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1 and visited_mapnum[ny][nx] == 0:
                        visited_mapnum[ny][nx] = 1
                        node_map[ny][nx] = node_num
                        queue.append([ny, nx])

            node_num += 1
node_num -= 1

graph = [{} for _ in range(node_num + 1)]
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            for d in range(4):
                ny = i + row[d]
                nx = j + col[d]

                if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 0:
                    cnt = 1
                    while 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 0:
                        ny += row[d]
                        nx += col[d]
                        cnt += 1
                    
                    if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1 and node_map[i][j] != node_map[ny][nx] and cnt - 1 >= 2:
                        if graph[node_map[i][j]].get(node_map[ny][nx], -1) == -1:    
                            graph[node_map[i][j]][node_map[ny][nx]] = cnt - 1
                        else:
                            graph[node_map[i][j]][node_map[ny][nx]] = min(graph[node_map[i][j]][node_map[ny][nx]], cnt - 1)
                        
                        if graph[node_map[ny][nx]].get(node_map[i][j], -1) == -1:
                            graph[node_map[ny][nx]][node_map[i][j]] = cnt - 1
                        else:
                            graph[node_map[ny][nx]][node_map[i][j]] = min(graph[node_map[ny][nx]][node_map[i][j]], cnt - 1)

arr = [i for i in range(node_num + 1)]
def parent(now):
    if now != arr[now]:
        arr[now] = parent(arr[now])
    return arr[now]

def union(a, b):
    a = parent(a)
    b = parent(b)

    if a < b: arr[b] = a
    else: arr[a] = b

edges = []
for a in range(1, node_num + 1):
    for b, cost in list(graph[a].items()):
        edges.append([cost, a, b])

edges.sort()
result = 0

for i in range(len(edges)):
    nc, na, nb = edges[i]
    if parent(na) != parent(nb):
        union(na, nb)
        result += nc

for i in range(1, node_num + 1): arr[i] = parent(i)
if arr.count(arr[1]) == node_num: print(result)
else: print(-1)