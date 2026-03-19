# 10942 : 팰린드롬?

import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

dp = [[False for _ in range(n+1)] for _ in range(n+1)]

# 1. 초기 홀/짝 세팅
for i in range(1, n+1):
    dp[i][i] = True

for i in range(1, n):
    if arr[i-1] == arr[i]:
        dp[i][i+1] = True

# 2. size 3부터 팰린드롬 찾기
for size in range(3, n+1):
    for i in range(n-size+1):
        if arr[i] == arr[i+size-1] and dp[i+2][i+size-1]:
            dp[i+1][i+size] = True

m = int(input().rstrip())
for _ in range(m):
    s, e = map(int, input().rstrip().split())
    print(1 if dp[s][e] else 0)