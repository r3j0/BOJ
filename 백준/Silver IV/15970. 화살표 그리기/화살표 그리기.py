import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
arr.sort(key=lambda x:(x[0]))

colors = [[] for _ in range(n+1)]
for a in arr: colors[a[1]].append(a[0])

res = 0
for a in arr:
    idx = colors[a[1]].index(a[0])

    now = -1
    if idx > 0:
        now = abs(a[0] - colors[a[1]][idx-1])
    if idx < len(colors[a[1]]) - 1:
        if now == -1: now = abs(a[0] - colors[a[1]][idx+1])
        else: now = min(now, abs(a[0] - colors[a[1]][idx+1]))
    
    res += now

print(res)