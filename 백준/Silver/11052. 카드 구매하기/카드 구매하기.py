import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rstrip().split()))

dp = [0 for _ in range(n+1)]
for i in range(n): dp[i+1] = arr[i]

for i in range(2, n+1):
    for j in range(1, i//2+1):
        dp[i] = max(dp[i], dp[i-j] + arr[j-1])

print(dp[n])