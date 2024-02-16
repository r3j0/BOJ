import sys
input = sys.stdin.readline

string = list(input().rstrip())
dp = [0 for _ in range(len(string)+1)]
dp[0] = 1

for i in range(1, len(string)+1):
    # 2자리 사용
    if i >= 2:
        if 10 <= int(string[i-2] + string[i-1]) <= 34:
            dp[i] += dp[i-2]

    # 1자리 사용
    if string[i-1] != '0':
        dp[i] += dp[i-1]
        
print(dp[-1]) 