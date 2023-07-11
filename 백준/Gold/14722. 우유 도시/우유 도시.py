import sys
input = sys.stdin.readline

n = int(input().rstrip())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]
dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
if maps[0][0] == 0: dp[0][0][0] = 1

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0: continue

        if i - 1 >= 0:
            if maps[i][j] == 0:
                if dp[i-1][j][2] != 0: # 이전에 2번을 먹은 적이 있음
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][2] + 1)
                else: # 이전에 2번을 먹은 적이 없음
                    dp[i][j][0] = max(dp[i-1][j][0], 1)
                
                dp[i][j][1] = dp[i-1][j][1]
                dp[i][j][2] = dp[i-1][j][2]
            elif maps[i][j] == 1:
                dp[i][j][0] = dp[i-1][j][0]

                if dp[i-1][j][0] != 0: # 이전에 0번을 먹은 적이 있음
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j][0] + 1)
                else: # 이전에 0번을 먹은 적이 없음
                    dp[i][j][1] = dp[i-1][j][1]

                dp[i][j][2] = dp[i-1][j][2]
            else: # 2
                dp[i][j][0] = dp[i-1][j][0]
                dp[i][j][1] = dp[i-1][j][1]

                if dp[i-1][j][1] != 0: # 이전에 1번을 먹은 적이 있음
                    dp[i][j][2] = max(dp[i-1][j][2], dp[i-1][j][1] + 1)
                else: # 이전에 1번을 먹은 적이 없음
                    dp[i][j][2] = dp[i-1][j][2]
        if j - 1 >= 0:
            if maps[i][j] == 0:
                if dp[i][j-1][2] != 0: # 이전에 2번을 먹은 적이 있음
                    dp[i][j][0] = max(dp[i][j-1][0], dp[i][j-1][2] + 1, dp[i][j][0])
                else: # 이전에 2번을 먹은 적이 없음
                    dp[i][j][0] = max(dp[i][j-1][0], dp[i][j][0], 1)
                
                dp[i][j][1] = max(dp[i][j][1], dp[i][j-1][1])
                dp[i][j][2] = max(dp[i][j][2], dp[i][j-1][2])
            elif maps[i][j] == 1:
                dp[i][j][0] = max(dp[i][j][0], dp[i][j-1][0])

                if dp[i][j-1][0] != 0: # 이전에 0번을 먹은 적이 있음
                    dp[i][j][1] = max(dp[i][j-1][0] + 1, dp[i][j-1][1], dp[i][j][1])
                else: # 없음
                    dp[i][j][1] = max(dp[i][j-1][1], dp[i][j][1])

                dp[i][j][2] = max(dp[i][j][2], dp[i][j-1][2])
            else: # 2
                dp[i][j][0] = max(dp[i][j][0], dp[i][j-1][0])
                dp[i][j][1] = max(dp[i][j][1], dp[i][j-1][1])
                if dp[i][j-1][1] != 0: # 이전에 1번을 먹은 적이 있음
                    dp[i][j][2] = max(dp[i][j-1][1] + 1, dp[i][j-1][2], dp[i][j][2])
                else: # 없음
                    dp[i][j][2] = max(dp[i][j-1][2], dp[i][j][2])

print(max(dp[n-1][n-1]))