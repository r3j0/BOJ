import sys
input = sys.stdin.readline

n = int(input().rstrip())
cost = [list(map(int, input().rstrip().split())) for _ in range(n)]

dp = [float('inf') for _ in range(2**n)]
dp[0] = 0

def bitCount(now):
    cnt = 0
    while now > 0:
        if now % 2 == 1: cnt += 1
        now >>= 1
    return cnt

for i in range(2**n):
    k = bitCount(i)

    for j in range(n):
        if i & (1 << j) == 0:
            dp[i|(1 << j)] = min(dp[i|(1 << j)], dp[i] + cost[k][j])
print(dp[-1])