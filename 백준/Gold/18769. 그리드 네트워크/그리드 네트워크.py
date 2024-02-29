import sys
import heapq
input = sys.stdin.readline

par = [0 for _ in range(500*500)]
def parent(now):
    while now != par[now]:
        now = par[now]
    return par[now]

def union(a, b):
    a = parent(a)
    b = parent(b)

    if a < b: par[b] = a
    else: par[a] = b

t = int(input().rstrip())
for _ in range(t):
    r, c = map(int, input().rstrip().split())
    edges = [[] for _ in range(4)]
    for i in range(r):
        arr = list(map(int, input().rstrip().split()))
        for j in range(c-1):
            edges[arr[j]-1].append([i*c+j, i*c+j+1])
    for i in range(r-1):
        arr = list(map(int, input().rstrip().split()))
        for j in range(c):
            edges[arr[j]-1].append([i*c+j, (i+1)*c+j])
    
    for k in range(r*c): par[k] = k
    res = 0
    for k in range(4):
        for l in range(len(edges[k])):
            if parent(edges[k][l][0]) != parent(edges[k][l][1]):
                union(edges[k][l][0], edges[k][l][1])
                res += k+1
    
    print(res)