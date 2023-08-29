import sys
input = sys.stdin.readline

c, n = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

dp = [0 for _ in range(1000001)]

# 지금까지의 비용으로 얻을 수 있는 고객 수가 c 를 넘을 때
result = 0
for weight in range(1, 1000001):
    for cost, value in arr:
        dp[weight] = max(dp[weight], 0 if weight < cost else dp[weight-cost]+value)

    if dp[weight] >= c:
        result = weight
        break

print(result)