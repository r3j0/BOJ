import sys
input = sys.stdin.readline

n = int(input().rstrip())
blocks = list(input().rstrip())
dp = [0 for _ in range(n)]
for i in range(1, n):
    for j in range(i):
        if (blocks[j] == 'B' and blocks[i] == 'O') or (blocks[j] == 'O' and blocks[i] == 'J') or (blocks[j] == 'J' and blocks[i] == 'B'):
            if (dp[i] == 0 and dp[j] != 0) or (dp[i] == 0 and blocks[j] == 'B'):
                dp[i] = dp[j] + (i-j)**2
            else:
                if dp[j] != 0:
                    dp[i] = min(dp[i], dp[j] + (i-j)**2)
#print(dp)
if dp[n-1] == 0: print(-1)
else: print(dp[n-1])