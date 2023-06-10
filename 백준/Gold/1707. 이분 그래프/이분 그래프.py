from collections import deque
import sys
input = sys.stdin.readline
test = int(input().rstrip())

for _ in range(test):
    v, e = map(int, input().rstrip().split())
    graph = [[] for _ in range(v)]
    for _ in range(e):
        a, b = map(int, input().rstrip().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    
    visited = [0 for _ in range(v)]
    count = 0
    q = deque()
    
    done = 0
    for i in range(v):
        if visited[i] == 0:
            visited[i] = 1

            q.append(i)

            while q:
                size = len(q)

                for s in range(size):
                    now = q.popleft()

                    for n in graph[now]:
                        if visited[n] == 0:
                            visited[n] = 1 if visited[now] == 2 else 2
                            q.append(n)
                        elif visited[n] == visited[now]:
                            done = 1
                            break
                if done == 1: break
        if done == 1: break
    
    print('YES' if done == 0 else 'NO')
    
            
