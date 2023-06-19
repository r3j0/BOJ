import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

dp_a = [0 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and dp_a[i] < dp_a[j]:
            dp_a[i] = dp_a[j]
    dp_a[i] += 1

dp_d = [0 for _ in range(n)]
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if arr[j] < arr[i] and dp_d[i] < dp_d[j]:
            dp_d[i] = dp_d[j]
    dp_d[i] += 1

maxv = 0
for i in range(n):
    maxv = max(maxv, dp_a[i] + dp_d[i])
print(maxv - 1)
