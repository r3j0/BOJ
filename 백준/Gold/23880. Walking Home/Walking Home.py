import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n, k = map(int, input().rstrip().split())
    maps = [list(input().rstrip()) for _ in range(n)]

    dp = [[[[0 for _ in range(4)] for _ in range(2)] for _ in range(n)] for _ in range(n)]
    # dp[i][j][k][l] : (i, j) 좌표에서 k 방향을 바라본 채 l 번 방향을 변경했을 떄의 경우의 수
    dp[0][0][0][0] = 1
    dp[0][0][1][0] = 1

    for i in range(n):
        for j in range(n):
            if i == j == 0 or maps[i][j] == 'H': continue

            # 오른쪽 방향
            if j > 0:
                if not (i == 0 and j - 1 == 0):
                    # 방향 꺾기
                    for l in range(k): dp[i][j][0][l+1] += dp[i][j-1][1][l]
                # 그대로 가기
                for l in range(k+1): dp[i][j][0][l] += dp[i][j-1][0][l]
                    

            # 아래쪽 방향
            if i > 0:
                if not (i - 1 == 0 and j == 0):
                    # 방향 꺾기
                    for l in range(k): dp[i][j][1][l+1] += dp[i-1][j][0][l]
                # 그대로 가기
                for l in range(k+1): dp[i][j][1][l] += dp[i-1][j][1][l]
    
    result = 0
    for i in range(2): result += sum(dp[n-1][n-1][i])
    print(result)