import sys
input = sys.stdin.readline

# 첫날에는 X, O
# 어제 O -> 다음 날 O X
# 어제 X -> 다음 날 O
# 어제 간 식당과 이웃한 식당은 가지 않는다. 

n = int(input().rstrip())
dp = [[0 for _ in range(n)] for _ in range(5)]
# dp[i][j] : i번째 식당을 j번째 날에 가는 경우의 수 (0번은 굶는 경우의 수)

for j in range(n):
    if j == 0:
        for i in range(5):
            dp[i][j] = 1
    else:
        for i in range(1, 5):
            dp[0][j] = (dp[0][j] + dp[i][j-1]) % 1000000007

            for k in range(5):
                if k != 0 and abs(k-i) <= 1: continue
                dp[i][j] = (dp[i][j] + dp[k][j-1]) % 1000000007

result = 0
for i in range(5): result += dp[i][-1]
print(result % 1000000007)
