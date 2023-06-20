import sys 
input = sys.stdin.readline

a = list(input().rstrip())
b = list(input().rstrip())

dp = [[0 for _ in range(len(a)+1)]]
for i in range(len(b)):
    new_dp = [0]
    for j in range(0, len(a)):
        if b[i] == a[j]:
            new_dp.append(dp[i][j] + 1)
        else:
            new_dp.append(max(dp[i][j+1], new_dp[-1]))
    dp.append(new_dp)

print(dp[len(b)][len(a)])