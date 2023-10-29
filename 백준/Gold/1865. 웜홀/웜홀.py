import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n, m, w = map(int, input().rstrip().split())
    edge = [{} for _ in range(n+1)] 
    for _ in range(m):
        s, e, t = map(int, input().rstrip().split())
        if edge[s].get(e): edge[s][e] = min(edge[s][e], t)
        else: edge[s][e] = t
        if edge[e].get(s): edge[e][s] = min(edge[e][s], t)
        else: edge[e][s] = t
    
    for _ in range(w):
        s, e, t = map(int, input().rstrip().split())
        if edge[s].get(e): edge[s][e] = min(edge[s][e], -t)
        else: edge[s][e] = -t
    
    allflag = False
    dist = [0 for _ in range(n+1)]
    for i in range(n):
        for key in range(1, n+1):
            for end_node, weight in edge[key].items():
                if dist[end_node] > dist[key] + weight:
                    dist[end_node] = dist[key] + weight
                    if i == n - 1:
                        allflag = True
                        break
            if allflag: break
        if allflag: break
    
    print('YES' if allflag else 'NO')
