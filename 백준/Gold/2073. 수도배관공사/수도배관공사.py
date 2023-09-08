import sys
input = sys.stdin.readline

d, p = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(p)]

dp = [[0 for _ in range(d+1)] for _ in range(p+1)]

for length in range(1, d+1):
    for thing in range(1, p+1):
        now_length = arr[thing - 1][0]
        now_value = arr[thing - 1][1]

        if length >= now_length:
            if length - now_length == 0:
                dp[thing][length] = max(dp[thing - 1][length], now_value)
            else:
                dp[thing][length] = max(dp[thing - 1][length], min(dp[thing - 1][length - now_length], now_value))
        else:
            dp[thing][length] = dp[thing - 1][length]

print(dp[p][d])