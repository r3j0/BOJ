import sys
input = sys.stdin.readline

s = input().rstrip()
m = int(input().rstrip())
arr = []
for _ in range(m):
    a, x = input().rstrip().split()
    arr.append([a, int(x)])

dp = [1 for _ in range(len(s))]
for i in range(len(s)):
    if i != 0:
        dp[i] = dp[i-1] + 1
    for j in range(m):
        if len(arr[j][0]) > i+1: continue
        if s[i-(len(arr[j][0])-1):i+1] == arr[j][0]:
            if (i-(len(arr[j][0])-1)-1 >= 0):
                dp[i] = max(dp[i], dp[i-(len(arr[j][0])-1)-1] + arr[j][1])
            else:
                dp[i] = max(dp[i], arr[j][1])
print(dp[-1])