import sys
input = sys.stdin.readline

n, s, m = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

dp = [[0 for _ in range(m+1)] for _ in range(n)]
for i in range(n):
    if i == 0:
        if 0 <= s-arr[0]: dp[i][s-arr[0]] = 1
        if s+arr[0] <= m: dp[i][s+arr[0]] = 1
    else: 
        for j in range(m+1):
            if dp[i-1][j] != 0:
                if 0 <= j-arr[i]: dp[i][j-arr[i]] = 1
                if j+arr[i] <= m: dp[i][j+arr[i]] = 1

done = 0
for i in range(m, -1, -1):
    if dp[n-1][i] == 1:
        print(i)
        done = 1
        break

if done == 0: print(-1)