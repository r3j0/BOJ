import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
res = -1
for i in range(n):
    now = 0
    pre = arr[i] - (i * k)
    if pre < 1: continue
    for j in range(n):
        if pre != arr[j]: now += 1
        pre += k
    if res == -1: res = now
    else: res = min(res, now)
print(res)