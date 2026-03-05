# 16202 : MST 게임
import sys
input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())
edges = []
for i in range(m):
    a, b = map(int, input().rstrip().split())
    edges.append([i+1, a, b])

edges.sort(key=lambda x:x[0])

def mst(e):
    parent = [i for i in range(n+1)]
    def find(k):
        s = []
        now = k
        while now != parent[now]:
            s.append(now)
            now = parent[now]
        
        parent[k] = now
        while s:
            parent[s.pop()] = now

        return now
    
    def union(a, b):
        a = find(a)
        b = find(b)

        if a == b: return False
        if a > b: a, b = b, a
        parent[b] = a
        return True
    
    min_edges = [float('inf'), -1, -1]
    cnt = 0
    score = 0
    done = True
    for e in edges:
        if (union(e[1], e[2])):
            cnt += 1
            score += e[0]

            if (min_edges[0] > e[0]):
                min_edges = e
        
        if cnt == n - 1: 
            done = False
            break
    if done: score = 0

    
    return score, min_edges

ans = []
for _ in range(k):
    sc, ed = mst(edges)
    for i in range(len(edges)):
        if edges[i] == ed:
            del edges[i]
            break
    ans.append(sc)

print(' '.join(map(str, ans)))