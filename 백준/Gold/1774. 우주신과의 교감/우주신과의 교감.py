import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
line = [list(map(int, input().rstrip().split())) for _ in range(n)]

arr = [i for i in range(n+1)]
dic = {i:{} for i in range(n+1)}
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    mi = min(a, b)
    ma = max(a, b)
    dic[mi][ma] = 1

def parent(now):
    if now != arr[now]:
        arr[now] = parent(arr[now])
    return arr[now]

def union(a, b):
    a = parent(a)
    b = parent(b)

    if a < b: arr[b] = a
    else: arr[a] = b

edges = []
result = 0

def Distances(ax, ay, bx, by):
    return float((ax - bx)**2 + (ay - by)**2)**(0.5)

for i in range(1, n+1):
    for j in range(i+1, n+1):
        if dic.get(i) and dic[i].get(j):
            edges.append([0, i, j])
        else:
            edges.append([Distances(line[i-1][0], line[i-1][1], line[j-1][0], line[j-1][1]), i, j])

edges.sort()

for i in range(len(edges)):
    cost, a, b = edges[i]
    if parent(a) != parent(b):
        union(a, b)
        result += cost

print('%.2f'%result)