from collections import deque

def solution(n, edge):
    answer = 0
    queue = deque()
    queue.append(1)
    visited = [0 for _ in range(n+1)]
    visited[1] = 1
    
    graph = {i:[] for i in range(n+1)}
    for a, b in edge: 
        graph[a].append(b)
        graph[b].append(a)
    
    times = [0 for _ in range(n+1)]
    now_time = 1
    while queue:
        size = len(queue)
        for s in range(size):
            now = queue.popleft()
            for go in graph[now]:
                if visited[go] == 0:
                    visited[go] = 1
                    times[go] = now_time
                    queue.append(go)
        now_time += 1
    
    max_time = max(times)
    for i in range(1, n+1):
        if max_time == times[i]: answer += 1
    
    return answer