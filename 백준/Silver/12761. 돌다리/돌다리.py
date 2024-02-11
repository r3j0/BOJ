import sys
from collections import deque
input = sys.stdin.readline

a, b, n, m = map(int, input().rstrip().split())
visited = [0 for _ in range(100001)]
queue = deque()
queue.append(n)
dir = [+1, -1, +a, -a, +b, -b]
time = 0
res = -1
while queue:
    size = len(queue)
    for s in range(size):
        now = queue.popleft()
        if now == m: 
            res = time
            break

        for d in range(6):
            go = now + dir[d]
            if 0 <= go <= 100000 and visited[go] == 0:
                visited[go] = 1
                queue.append(go)
        
        go1 = now * a
        if 0 <= go1 <= 100000 and visited[go1] == 0:
            visited[go1] = 1
            queue.append(go1)
        go2 = now * b
        if 0 <= go2 <= 100000 and visited[go2] == 0:
            visited[go2] = 1
            queue.append(go2)
    if res != -1: break
    time += 1
print(res)