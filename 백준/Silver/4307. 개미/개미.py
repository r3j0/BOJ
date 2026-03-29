# 4307 : 개미
import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    l, n = map(int, input().rstrip().split())
    arr = [int(input().rstrip()) for _ in range(n)]
    ans = [0, 0]
    res = []
    for i in range(n):
        res.append(min(arr[i], l - arr[i]))
    ans[0] = max(res)
    res = []
    for i in range(n):
        res.append(max(arr[i], l - arr[i]))
    ans[1] = max(res)
    print(' '.join(map(str, ans)))