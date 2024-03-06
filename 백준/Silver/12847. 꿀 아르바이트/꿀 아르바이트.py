import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
for i in range(1, n):
    arr[i] += arr[i-1]

res = arr[m-1]
for idx in range(m, n):
    now = arr[idx] - arr[idx-m]
    res = max(res, now)
print(res)
