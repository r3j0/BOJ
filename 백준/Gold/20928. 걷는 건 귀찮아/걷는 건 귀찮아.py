import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arrP = list(map(int, input().rstrip().split()))
arrX = list(map(int, input().rstrip().split()))

vis = [0 for _ in range(n)]
vis[0] = 1
queue = deque()
queue.append(0)

time = 0
res = 0
max_go = 0
while queue:
    size = len(queue)
    for s in range(size):
        now = queue.popleft()
        if arrP[now] <= m <= arrP[now] + arrX[now]:
            res = 1
            break
        if max_go >= arrP[now] + arrX[now]:
            continue
        max_go = arrP[now] + arrX[now]

        for i in range(now + 1, n):
            if vis[i] == 0 and arrP[now] <= arrP[i] <= arrP[now] + arrX[now]:
                queue.append(i)
                vis[i] = 1
            if arrP[now] + arrX[now] < arrP[i]:
                break
    
    if res == 1: break
    time += 1
if res == 1: print(time)
else: print(-1)