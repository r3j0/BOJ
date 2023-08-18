import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
queue = deque()
for i in range(1, n + 1):
    queue.append(i)

while queue:
    now = queue.popleft()
    print(now, end=' ')

    if queue:
        go = queue.popleft()
        queue.append(go)