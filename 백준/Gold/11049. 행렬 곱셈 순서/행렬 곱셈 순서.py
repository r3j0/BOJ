import sys
input = sys.stdin.readline

n = int(input().rstrip())
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
arr = []
for _ in range(n): arr.append(list(map(int, input().rstrip().split())))

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

# 길이 2
for start in range(1, n):
    dp[start][start+1] = arr[start-1][0] * arr[start-1][1] * arr[start][1]

# dp[i][j] : i번째부터 j번째까지 곱했을 떄의 연산 횟수
for length in range(3, n+1):
    for start in range(1, n+2-length):
        # start ~ start + k / start + k + 1 ~ start + length - 1
        dp[start][start+length-1] += min([(dp[start][start + k] + dp[start+k + 1][start + length - 1] + (arr[start-1][0] * arr[start+k-1][1] * arr[start + length - 2][1])) for k in range(length - 1)])

print(dp[1][n])