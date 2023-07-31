import sys
from collections import deque
input = sys.stdin.readline

while True:
    n = list(map(int, input().rstrip().split()))[0]
    if n == 0: break

    graph = [[] for _ in range(n+1)]

    # Contact
    for idx in range(n):
        arr = list(map(int, input().rstrip().split()))
        if len(arr) == 1: continue
        graph[idx + 1] = arr[:-1]

    # Spam
    prop = [[] for _ in range(n+1)]
    while True:
        arr = list(input().rstrip().split())
        if len(arr) == 1: break
        start, t1, t2, p1, p2, p3 = arr
        start = int(start)
        t1 = int(t1)
        t2 = int(t2)

        visited = [0 for _ in range(n+1)]
        visited[start] = 1
        count = [0 for _ in range(n+1)]
        queue = deque()
        queue.append(start)

        while queue:
            now = queue.popleft()
            count[now] += len(graph[now])

            for next in graph[now]:
                if visited[next] == 0:
                    queue.append(next)
                    visited[next] = 1
        
        for v in range(len(visited)):
            if v == 0: continue

            if count[v] < t1: prop[v].append(p1)
            elif count[v] < t2: prop[v].append(p2)
            else: prop[v].append(p3)

    names = []
    for idx in range(n):
        names.append(input().rstrip())
    
    for i in range(n):
        print('%s:'%names[i], ' '.join(prop[i+1]))
