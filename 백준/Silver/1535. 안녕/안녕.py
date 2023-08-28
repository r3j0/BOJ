import sys
input = sys.stdin.readline

n = int(input().rstrip())
weightList = list(map(int, input().rstrip().split()))
valueList = list(map(int, input().rstrip().split()))

dp = [[0 for _ in range(100)] for _ in range(n+1)]

for weight in range(0, 100):
    for person in range(1, n+1):
        now_weight = weightList[person-1]
        now_value = valueList[person-1]

        if now_weight <= weight:
            dp[person][weight] = max(dp[person-1][weight], dp[person-1][weight-now_weight] + now_value)
        else:
            dp[person][weight] = dp[person-1][weight]

print(dp[n][99])