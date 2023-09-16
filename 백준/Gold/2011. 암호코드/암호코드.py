import sys
input = sys.stdin.readline

string = input().rstrip()
dp = [float('inf') for _ in range(len(string)+1)]
dp[0] = 1

for i in range(1, len(string)+1):
    tmp = float('inf')
    if '1' <= string[i-1] <= '9': 
        if tmp == float('inf'): tmp = 0
        tmp += dp[i-1]
    if i > 1 and 10 <= int(string[i-2:i]) <= 26: 
        if tmp == float('inf'): tmp = 0
        tmp += dp[i-2]

    mins = min(dp[i], tmp)
    if mins == float('inf'):
        continue
    dp[i] = mins % 1000000

print(dp[len(string)] if dp[len(string)] != float('inf') else 0)