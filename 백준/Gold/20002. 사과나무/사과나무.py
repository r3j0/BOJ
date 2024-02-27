import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

res = arr[0][0]

sums = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        sums[i+1][j+1] = sums[i][j+1] + sums[i+1][j] + arr[i][j] - sums[i][j]

for k in range(1, n+1):
    for i in range(n-k+1):
        for j in range(n-k+1):
            res = max(res, sums[i+k][j+k] - sums[i+k][j] - sums[i][j+k] + sums[i][j])

print(res)