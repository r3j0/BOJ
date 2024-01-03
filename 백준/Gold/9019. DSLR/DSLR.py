import sys
from collections import deque
input = sys.stdin.readline
visited = [0 for _ in range(10001)]
t = int(input().rstrip())
for k in range(t):
    a, b = map(int, input().rstrip().split())
    path = ['' for _ in range(10001)]
    visited[a] = k+1
    queue = deque()
    queue.append(a)
    while queue:
        now = queue.popleft()
        if now == b:
            print(path[now])
            break
        if visited[(now*2)%10000] != k+1:
            visited[(now*2)%10000] = k+1
            path[(now*2)%10000] = path[now] + 'D'
            queue.append((now*2)%10000)
        if now == 0:
            if visited[9999] != k+1:
                visited[9999] = k+1
                path[9999] = path[now] + 'S'
                queue.append(9999)
        else:
            if visited[now-1] != k+1:
                visited[now-1] = k+1
                path[now-1] = path[now] + 'S'
                queue.append(now-1)
        
        ll = ((((now//100)%10)*1000) + (((now//10)%10)*100) + ((now%10)*10)) + ((now//1000)%10)
        if visited[ll] != k+1:
            visited[ll] = k+1
            path[ll] = path[now] + 'L'
            queue.append(ll)
        
        rr = ((now%10)*1000) + (((now//1000)%10)*100) + (((now//100)%10)*10) + ((now//10)%10)
        if visited[rr] != k+1:
            visited[rr] = k+1
            path[rr] = path[now] + 'R'
            queue.append(rr)