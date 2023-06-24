import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))
    m = int(input().rstrip())
    dp = [0 for _ in range(m+1)]
    dp[0] = 1

    for i in range(1, n+1):
        for j in range(arr[i-1], m+1):
            dp[j] += dp[j - arr[i-1]]
        
    print(dp[m])