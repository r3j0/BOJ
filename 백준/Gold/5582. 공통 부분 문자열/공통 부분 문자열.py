import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

dp = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]

for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1

max_value = 0
for d in dp: 
    max_value = max(max_value, max(d))
print(max_value)