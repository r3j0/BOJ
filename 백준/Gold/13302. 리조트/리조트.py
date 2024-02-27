import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
arr.sort()
# dp[i][j] : i 번째 날, 쿠폰 j 개를 가지고 있을 때
dp = [[-1 for _ in range(50)] for _ in range(n+1)]
dp[0][0] = 0
for i in range(1, n+1):
    if (len(arr) > 0 and arr[0] != i) or (len(arr) == 0):
        for j in range(0, 50):
            if dp[i-1][j] != -1:
                dp[i][j] = dp[i-1][j] + 10000
            else:
                dp[i][j] = dp[i-1][j]
        for j in range(3, 50): # 쿠폰 사용
            if dp[i-1][j] != -1:
                dp[i][j-3] = min(dp[i][j-3], dp[i-1][j]) 
    else:
        del arr[0]
        for j in range(0, 50):
            dp[i][j] = dp[i-1][j]
    
    if i >= 3:
        for j in range(1, 50):
            if dp[i-3][j-1] != -1:
                if dp[i][j] == -1:
                    dp[i][j] = dp[i-3][j-1] + 25000
                else:
                    dp[i][j] = min(dp[i][j], dp[i-3][j-1] + 25000)

    if i >= 5:
        for j in range(2, 50):
            if dp[i-5][j-2] != -1:
                if dp[i][j] == -1:
                    dp[i][j] = dp[i-5][j-2] + 37000
                else:
                    dp[i][j] = min(dp[i][j], dp[i-5][j-2] + 37000)

res = dp[n][0]
for j in range(1, 50):
    if dp[n][j] != -1:
        res = min(res, dp[n][j])
print(res)