import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
dp = [0 for _ in range(n+1)]
# dp[i] : i 번째 건물이 지어지기까지 걸리는 최소 시간

graph = [[] for _ in range(n+1)]
prefix = [0 for _ in range(n+1)]
inDegree = [0 for _ in range(n+1)]
for i in range(n):
    order = list(map(int, input().rstrip().split()))
    dp[i+1] = order[0]
    for k in range(1, len(order)-1):
        inDegree[i+1] += 1
        graph[order[k]].append(i+1)

queue = deque()
for i in range(1, n+1):
    if inDegree[i] == 0: queue.append(i)
for _ in range(n):
    now = queue.popleft()
    dp[now] += prefix[now]
    for next in graph[now]:
        inDegree[next] -= 1
        if inDegree[next] == 0:
            queue.append(next)
        prefix[next] = max(prefix[next], dp[now])

for i in range(1, n+1): print(dp[i])