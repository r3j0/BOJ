# 34011 : 꽁꽁 얼어붙은 트리
import sys
from collections import deque
input = sys.stdin.readline

# Height 를 먼저 구해야 한다.
# Height 를 구하고 "모든 약수의 합" 구하는 원리와 같이 간다
n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
edges = [[] for _ in range(n+1)]
for i in range(n-1):
    edges[arr[i]].append(i+2)

# BFS
height = [0 for _ in range(n+1)]
queue = deque()
queue.append(1)
time = 0
while queue:
    size = len(queue)
    for _ in range(size):
        now = queue.popleft()
        for e in edges[now]:
            queue.append(e)
        height[time] += 1
    time += 1

ans = list(height)
for i in range(2, n+1):
    j = 2
    while i * j <= n and height[i * j] > 0:
        ans[i] += height[i * j]
        j += 1
    ans[i] += 1

print(max(ans[2:]))