import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = [i for i in range(n)]
result = -1

def parent(now):
    while now != arr[now]:
        now = arr[now]
    return now

def union(p1, p2):
    if p1 != p2:
        arr[p2] = p1

for turn in range(m):
    a, b = map(int, input().rstrip().split())
    a = parent(a)
    b = parent(b)

    if result != -1: continue
    if arr[a] == arr[b]:
        result = turn + 1
        continue
    else:
        union(a, b)

if result == -1: print(0)
else: print(result)