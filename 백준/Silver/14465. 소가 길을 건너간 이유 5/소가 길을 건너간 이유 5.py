import sys
input = sys.stdin.readline

n, k, b = map(int, input().rstrip().split())
arr = [0 for _ in range(n)]
for _ in range(b): 
    a = int(input().rstrip())
    arr[a-1] = 1

sums = [0]
for i in range(n):
    sums.append(sums[-1] + arr[i])
del sums[0]

res = sums[k-1]
for i in range(k, n):
    res = min(res, sums[i] - sums[i-k])
print(res)