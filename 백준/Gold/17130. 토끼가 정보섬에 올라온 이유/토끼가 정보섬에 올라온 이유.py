import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
maps = [list(input().rstrip()) for _ in range(n)]
dp = [[[0, 0] for _ in range(m)] for _ in range(n)]
# dp[i][j][k] : (i, j) 를 지나면서 거치는 k[0] 경로 개수 k[1] 최대 당근 개수

col = [-1, 0, 1]
result = -1
for j in range(m):
    for i in range(n):
        if maps[i][j] == 'R': dp[i][j] = [1, 0]
        elif maps[i][j] != '#':
            for d in range(3):
                if j > 0 and 0 <= i + col[d] < n and maps[i][j] != '#' and dp[i + col[d]][j - 1][0] > 0:
                    dp[i][j][0] += dp[i + col[d]][j - 1][0]
                    dp[i][j][1] = max(dp[i][j][1], dp[i + col[d]][j - 1][1])
            
            if maps[i][j] == 'O' and dp[i][j][0] > 0: result = max(result, dp[i][j][1])
            elif maps[i][j] == 'C': dp[i][j][1] += 1

print(result)