import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = [list(input().rstrip()) for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]
max_value = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == '1':
            if i == 0 and j == 0: 
                dp[i][j] = 1
                max_value = max(max_value, dp[i][j])
                continue
            available = []
            if i > 0 and j > 0: available.append(dp[i-1][j-1])
            else: available.append(0)
            if i > 0: available.append(dp[i-1][j])
            else: available.append(0)
            if j > 0: available.append(dp[i][j-1])
            else: available.append(0)

            dp[i][j] = min(available) + 1
            max_value = max(max_value, dp[i][j])

print(max_value**2)