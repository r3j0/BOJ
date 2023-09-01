import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
aArr = list(map(int, input().rstrip().split()))
bArr = list(map(int, input().rstrip().split()))

arr = []
for i in range(n): arr.append([bArr[i], aArr[i]])

dp = [[0 for _ in range(100*n+1)] for _ in range(n+1)]
result = 0

for ci in range(0, 100*n+1):
    for ni in range(1, n+1):
        now_weight = arr[ni-1][0]
        now_value = arr[ni-1][1]

        if ci >= now_weight:
            dp[ni][ci] = max(dp[ni-1][ci], dp[ni-1][ci-now_weight] + now_value)
        else:
            dp[ni][ci] = dp[ni-1][ci]
    
    max_value = 0
    for ni in range(1, n+1):
        max_value = max(max_value, dp[ni][ci])
    
    if max_value >= m: 
        result = ci
        break
print(result)