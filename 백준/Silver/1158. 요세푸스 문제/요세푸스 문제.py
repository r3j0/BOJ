from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
queue = deque()
for i in range(1, n+1): queue.append(i)

def skip():
    queue.append(queue.popleft())

result = []
while queue:
    skip_count = k % len(queue) + (len(queue) if k % len(queue) == 0 else 0)
    for _ in range(skip_count - 1): skip()
    result.append(queue.popleft())

print('<' + ', '.join(map(str, result)) + '>')