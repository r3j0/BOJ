import sys
input = sys.stdin.readline

n, b = map(int, input().rstrip().split())
arr = [int(input().rstrip()) for _ in range(n)]
dp = [[0 for _ in range(b+1)] for _ in range(n)]
# dp[i][j] : i번째 구간에서 낮잠을 잤을 때, j만큼 낮잠 잘 구간이 남았을 때의 최대

for i in range(1, n):
    # 연속 자기
    for j in range(b-2, max(b-i-2, -1), -1):
        dp[i][j] = max(dp[i][j], dp[i-1][j+1] + arr[i])

    # 띄엄띄엄 자기
    if i > 1:
        if i > 2:
            for j in range(b+1):
                dp[i-2][j] = max(dp[i-2][j], dp[i-3][j])
        for j in range(b-2, max(b-i-2, -1), -1):
            dp[i][j] = max(dp[i][j], dp[i-2][j+2] + arr[i])

    """ for j in range(b+1):
        for i in range(n): print(dp[i][j], end=' ')
        print()
    print() """

for i in range(n-2, n):
    for j in range(b+1):
        dp[i][j] = max(dp[i][j], dp[i-1][j])

print(dp[n-1][0])