import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = []
for _ in range(n):
    day, cost = map(int, input().rstrip().split())
    arr.append((day, cost))

dp = [0 for _ in range(n+1)]
for i in range(n+1):
    if i != 0: dp[i] = max(dp[i], max(dp[:i]))
    if i != n and i+arr[i][0] <= n:
        dp[i+arr[i][0]] = max(dp[i+arr[i][0]], dp[i] + arr[i][1])

#print(dp)
print(dp[n])