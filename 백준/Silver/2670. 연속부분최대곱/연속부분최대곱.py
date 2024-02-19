import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [float(input().rstrip()) for _ in range(n)]
dp = [arr[i] for i in range(n)]

for i in range(1, n):
    now = arr[i]
    for j in range(i-1, -1, -1):
        dp[i] = max(dp[i], now * arr[j])
        now *= arr[j]

print('%.3f'%max(dp))