import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    k = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))

    prefixSum = [0 for _ in range(k+1)]
    for i in range(1, k+1): prefixSum[i] = prefixSum[i-1] + arr[i-1]

    # dp[start][end] : start 부터 end 까지 합친 최소 비용
    # dp[start][end] = dp[start][k] + dp[k+1][end] + (prefixSum(end) - prefixSum(start - 1))
    dp = [[0 for _ in range(k+1)] for _ in range(k+1)]

    for length in range(2, k+1):
        for start in range(1, k+2-length):
            dp[start][start+length-1] = min([dp[start][start+k] + dp[start+k+1][start+length-1] for k in range(length - 1)]) + (prefixSum[start+length-1] - prefixSum[start - 1])
    
    print(dp[1][k])