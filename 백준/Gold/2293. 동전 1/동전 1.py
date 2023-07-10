import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

arr = []
for _ in range(n): arr.append(int(input().rstrip()))
arr.sort()

dp = [0 for _ in range(k+1)]
dp[0] = 1

for i in range(n):
    for j in range(arr[i], k+1):
        if j - arr[i] >= 0:
            dp[j] += dp[j-arr[i]]

print(dp[k]) 