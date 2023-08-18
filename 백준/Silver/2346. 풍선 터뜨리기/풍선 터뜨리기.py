import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
queue = deque()
for i in range(n):
    queue.append((i+1, arr[i]))

while True:
    now = queue.popleft()
    print(now[0], end=' ')
    if not queue: break

    if now[1] > 0:
        for i in range(1, now[1]):
            go = queue.popleft()
            queue.append(go)
    else:
        for i in range(0, -now[1]):
            go = queue.pop()
            queue.appendleft(go)