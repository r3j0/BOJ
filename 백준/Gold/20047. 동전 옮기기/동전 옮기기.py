import sys
input = sys.stdin.readline

n = int(input().rstrip())
s = list(input().rstrip())
t = list(input().rstrip())
i, j = map(int, input().rstrip().split())

need_two = [s[i], s[j]]
del s[j]
del s[i]

""" print(need_two)
print(''.join(s))
print(''.join(t)) """

dp = [[0 for _ in range(n)] for _ in range(3)]
# dp[i][j] : 문자 i 개 추가했을 때 j 번째 인덱스까지 같은 문자 개수

for j in range(n):
    for i in range(3):
        if i == 0:
            if len(s) > j and s[j] == t[j]:
                if j > 0: dp[i][j] = dp[i][j-1] + 1
                else: dp[i][j] = 1
        elif i == 1:
            if j > 0 and need_two[0] == t[j] and dp[i-1][j-1] > 0:
                dp[i][j] = dp[i-1][j-1] + 1
            elif need_two[0] == t[j]: dp[i][j] = 1
            if j - 1 >= 0 and len(s) > j - 1 and s[j-1] == t[j] and dp[i][j-1] > 0:
                dp[i][j] = max(dp[i][j], dp[i][j-1] + 1)
        else:
            if j > 0 and need_two[1] == t[j] and dp[i-1][j-1] > 0:
                dp[i][j] = dp[i-1][j-1] + 1
            if j - 2 >= 0 and len(s) > j - 2 and s[j-2] == t[j] and dp[i][j-1] > 0:
                dp[i][j] = max(dp[i][j], dp[i][j-1] + 1)

""" for i in range(3):
    for j in range(n):
        print(dp[i][j], end=' ')
    print() """
if dp[2][n-1] == n: print('YES')
else: print('NO')