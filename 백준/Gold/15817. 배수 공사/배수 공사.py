import sys
input = sys.stdin.readline 

n, x = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

dp = [[0 for _ in range(x+1)] for _ in range(n+1)]
# dp[n][x] : n번 물건이 x 길이 파이프를 만들 수 있다.

for length_limit in range(1, x+1):
    for thing in range(1, n+1):
        now_length = arr[thing - 1][0]
        now_nums = arr[thing - 1][1]

        cnt = 0
        for k in range(1, now_nums + 1):
            if length_limit >= now_length * k and (length_limit - (now_length * k) == 0 or dp[thing - 1][length_limit - (now_length * k)] > 0):
                cnt += dp[thing - 1][length_limit - (now_length * k)] + (1 if length_limit - (now_length * k) == 0 else 0)
        dp[thing][length_limit] = dp[thing - 1][length_limit] + cnt

#for d in dp: print(d)
print(dp[n][x])