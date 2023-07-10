import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = []
for _ in range(n): arr.append(int(input().rstrip()))
arr.sort()

dp = [0 for _ in range(k+1)]

for a in arr:
    for i in range(a, k+1):
        if dp[i-a] == 0: 
            if i == a: dp[i] = 1
            continue
        if dp[i] == 0:
            dp[i] = dp[i-a] + 1
        else:
            dp[i] = min(dp[i], dp[i-a] + 1)

    #print(dp)
if dp[k] == 0: print(-1)
else: print(dp[k])