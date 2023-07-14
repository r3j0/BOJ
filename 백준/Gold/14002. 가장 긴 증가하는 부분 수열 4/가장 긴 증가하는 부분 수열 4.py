import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
dp = [[i] for i in range(n)]

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and len(dp[j]) + 1 > len(dp[i]):
            dp[i] = dp[j] + [i]

dp.sort(key=lambda x: -len(x))
print(len(dp[0]))
for i in dp[0]: print(arr[i], end=' ')