import sys
import math
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
sums = [0]
for i in range(n):
    sums.append((sums[-1] + arr[i]) % m)

arr = [0 for _ in range(m)]
for i in range(1, n+1):
    arr[sums[i]] += 1

res = arr[0]
for i in range(m):
    if arr[i] > 1:
        res += math.comb(arr[i], 2)

print(res)