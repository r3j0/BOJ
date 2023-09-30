import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

up_dp = [1 for _ in range(n)]
for i in range(1, n):
    if arr[i-1] <= arr[i]:
        up_dp[i] = up_dp[i-1] + 1
down_dp = [1 for _ in range(n)]
for i in range(1, n):
    if arr[i-1] >= arr[i]:
        down_dp[i] = down_dp[i-1] + 1

print(max(max(up_dp), max(down_dp)))