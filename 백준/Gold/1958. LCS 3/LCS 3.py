import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()
s3 = input().rstrip()

dp = [[[0 for _ in range(len(s3)+1)] for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    
for k in range(1, len(s3)+1):
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1] == s3[k-1]: dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else: dp[i][j][k] = max(dp[i-1][j-1][k-1], dp[i-1][j-1][k], dp[i-1][j][k-1], dp[i][j-1][k-1], dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

print(dp[len(s1)][len(s2)][len(s3)])