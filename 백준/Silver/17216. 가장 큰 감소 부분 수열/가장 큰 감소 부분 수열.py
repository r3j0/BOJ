import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
dp = [0 for _ in range(n)]
dp[0] = arr[0]

for i in range(1, n):
    dp[i] = arr[i]
    for j in range(0, i):
        if arr[j] > arr[i] and dp[i] < dp[j] + arr[i]:
            dp[i] = dp[j] + arr[i]
print(max(dp))