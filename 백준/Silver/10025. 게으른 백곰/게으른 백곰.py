import sys 
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
size = k*2+1
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
maps = [0 for _ in range(1000001)]
for a in arr:
    maps[a[1]] = a[0]

for i in range(1, 1000001):
    maps[i] += maps[i-1]

if len(maps) <= k:
    print(maps[-1])
else:
    res = maps[size]
    for i in range(size+1, 1000001):
        res = max(res, maps[i] - maps[i - size - 1])
    print(res)

