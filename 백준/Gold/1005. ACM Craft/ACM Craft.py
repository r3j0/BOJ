import sys
from collections import deque
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n, k = map(int, input().rstrip().split())
    arr = list(map(int, input().rstrip().split()))
    graph = [[] for _ in range(n+1)]
    indegree = [0 for _ in range(n+1)]
    result = [0 for _ in range(n+1)]
    for _ in range(k):
        x, y = map(int, input().rstrip().split())
        graph[x].append(y)
        indegree[y] += 1
    
    w = int(input().rstrip())
    
    queue = deque()
    for i in range(1, n+1):
        if indegree[i] == 0: queue.append(i)
    
    while queue:
        now = queue.popleft()
        result[now] += arr[now - 1]
        for next in graph[now]:
            indegree[next] -= 1
            result[next] = max(result[next], result[now])
            if indegree[next] == 0:
                queue.append(next)
    
    print(result[w])