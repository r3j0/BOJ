import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
res = arr[0]
for i in range(1, m):
    # Front
    res = max(res, (arr[i] - arr[i-1])//2 + (1 if (arr[i] - arr[i-1]) % 2 == 1 else 0))

res = max(res, n - arr[-1])
print(res)