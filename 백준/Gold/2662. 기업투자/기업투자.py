import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = [[0 for _ in range(m)]]
for _ in range(n):
    tmp = list(map(int, input().rstrip().split()))
    arr.append(tmp[1:])

dp = [[[0, [0 for _ in range(m+1)]] for _ in range(n+1)] for _ in range(m+1)]
# dp[m][n] : m 번까지 투자했을 때 n 금액까지 투자했을 때 최대 이익

debug = 0

for weight in range(1, n+1):
    for thing in range(1, m+1):
        if debug: print('>>', thing, weight)
        for now_weight in range(weight+1):
            if debug: print('( nw', now_weight, ')', dp[thing-1][now_weight][0], '( w-nw', weight - now_weight, ')', arr[weight - now_weight][thing-1])
            if dp[thing][weight][0] < dp[thing-1][now_weight][0] + arr[weight - now_weight][thing-1]:
                dp[thing][weight][0] = dp[thing-1][now_weight][0] + arr[weight - now_weight][thing-1]

                if debug: print(dp[thing-1][now_weight][1])
                dp[thing][weight][1] = list(dp[thing-1][now_weight][1])
                dp[thing][weight][1][thing] = weight - now_weight
                if debug: print(dp[thing][weight][1])
                if debug: print()

max_value = 0
max_pos = []
for i in range(m+1):
    for j in range(n+1):
        if debug: print(dp[i][j][0], end=' ')
        if max_value < dp[i][j][0]:
            max_value = dp[i][j][0]
            max_pos = [i, j]
    if debug: print()

print(dp[max_pos[0]][max_pos[1]][0])
print(' '.join(map(str, dp[max_pos[0]][max_pos[1]][1][1:])))