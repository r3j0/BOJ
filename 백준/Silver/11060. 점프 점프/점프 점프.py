import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

queue = deque()
queue.append(0)
visited = [0 for _ in range(n)]
visited[0] = 1
time = 0
done = 0
while queue:
    size = len(queue)

    for s in range(size):
        now = queue.popleft()
        if now == n - 1: 
            done = 1
            break

        for k in range(1, arr[now] + 1):
            if now + k < n and visited[now + k] == 0:
                visited[now + k] = 1
                queue.append(now + k)
    if done == 1: break

    time += 1

if done == 1: print(time)
else: print(-1)
