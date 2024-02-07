import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(float, input().rstrip().split())) for _ in range(n)]
graph = [{} for _ in range(n+1)]

def Distances(ax, ay, bx, by):
    return ((ax - bx)**2 + (ay - by)**2)**(0.5)

for i in range(1, n+1):
    for j in range(i+1, n+1):
        graph[i][j] = Distances(arr[i-1][0], arr[i-1][1], arr[j-1][0], arr[j-1][1])
        graph[j][i] = Distances(arr[i-1][0], arr[i-1][1], arr[j-1][0], arr[j-1][1])
    
def prim():
    queue = []
    visit = [False] * (n + 1)
    sumw = 0
    heapq.heappush(queue, (0, 1))
    
    while queue:
        w, v = heapq.heappop(queue)
        if not visit[v]:
            visit[v] = True
            sumw += w
            for i in range(1, n+1):
                if graph[v].get(i) and not visit[i]:
                    heapq.heappush(queue, (graph[v][i], i))
    return sumw
               
print('%.2f'%prim())