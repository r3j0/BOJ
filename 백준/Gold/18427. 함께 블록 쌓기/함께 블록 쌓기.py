import sys
input = sys.stdin.readline

n, m, h = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

dp = [[0 for _ in range(h+1)] for _ in range(n+1)]

# dp[n][h] : n 번째 사람이 블록을 사용했을 때 h 높이에 다다르는 경우의 수
for height_limit in range(1, h+1):
    for person in range(1, n+1):
        for now_block in arr[person-1]:
            if height_limit >= now_block and (height_limit - now_block == 0 or dp[person - 1][height_limit - now_block] > 0):
                if height_limit - now_block == 0:
                    dp[person][height_limit] += 1
                else:
                    dp[person][height_limit] += dp[person - 1][height_limit - now_block]
        dp[person][height_limit] = dp[person][height_limit] + dp[person - 1][height_limit]
        dp[person][height_limit] %= 10007

print(dp[n][h])