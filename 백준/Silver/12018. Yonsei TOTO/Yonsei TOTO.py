import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

avail = []
for _ in range(n):
    p, l = map(int, input().rstrip().split())
    arr = list(map(int, input().rstrip().split()))
    arr.sort(reverse=True)
    if p >= l: avail.append(arr[l-1])
    else: avail.append(1)

avail.sort()
idx = 0
while idx < len(avail) and avail[idx] <= m:
    m -= avail[idx]
    idx += 1

print(idx)