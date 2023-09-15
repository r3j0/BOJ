import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
narr = []
# 물건을 분할하기
for i in range(n):
    now = 1
    done = 0
    while now <= arr[i][2]:
        go = min(now, arr[i][2] - done)
        done += go
        narr.append([go*arr[i][0], go*arr[i][1]])
        now <<= 1

dp = [[0 for _ in range(m+1)] for _ in range(len(narr)+1)]
for weight in range(1, m+1):
    for thing in range(1, len(narr)+1):
        now_weight = narr[thing - 1][0]
        now_value = narr[thing - 1][1]

        if weight >= now_weight:
            dp[thing][weight] = max(dp[thing-1][weight], dp[thing-1][weight - now_weight] + now_value)
        else:
            dp[thing][weight] = dp[thing - 1][weight]

print(dp[-1][m])
