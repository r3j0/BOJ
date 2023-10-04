import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
size = len(arr)
sum_value = 0
for i in range(size):
    sum_value += arr[i][0]
    arr.append([arr[i][0] * 2, arr[i][1] + 1])

dp = [[0 for _ in range(m+1)] for _ in range(len(arr)+1)]

for weight in range(1, m+1):
    for thing in range(1, len(arr)+1):
        now_weight = arr[thing-1][1]
        now_value = arr[thing-1][0]

        if weight >= now_weight:
            dp[thing][weight] = max(dp[thing-1][weight], dp[thing-1][weight-now_weight] + now_value)
        else:
            dp[thing][weight] = dp[thing-1][weight]

if dp[len(arr)][m] > sum_value: print('W')
elif dp[len(arr)][m] == sum_value: print('D')
else: print('L')