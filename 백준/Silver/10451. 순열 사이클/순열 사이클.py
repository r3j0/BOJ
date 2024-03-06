import sys
from collections import deque
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))
    vis = [0 for _ in range(n)]

    cnt = 0
    for i in range(n):
        if vis[i] == 0:
            vis[i] = 1
            queue = deque()
            queue.append(i)
            
            while queue:
                now = queue.popleft()
                if vis[arr[now]-1] == 0:
                    queue.append(arr[now]-1)
                    vis[arr[now]-1] = 1
            cnt += 1
    print(cnt)