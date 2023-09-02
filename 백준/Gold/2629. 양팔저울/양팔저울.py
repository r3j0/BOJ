import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
k = int(input().rstrip())
order = list(map(int, input().rstrip().split()))
sa = sum(arr)
dp = [0 for _ in range(sa+1)]
dp[0] = 1
for a in arr:
    for i in range(sa, -1, -1):
        if dp[i] == 1 and i + a <= sa:
            dp[i + a] = 1
    for i in range(sa + 1):
        if dp[i] == 1:
            dp[abs(i-a)] = 1

for o in order:
    print('Y' if o <= sa and dp[o] == 1 else 'N', end=' ')