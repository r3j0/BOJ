import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [list(map(int, input().rstrip().split())) for _ in range(2)]

    dp = [[0 for _ in range(n)] for _ in range(2)]

    pre_max_now0 = 0
    pre_max_now1 = 0
    max_now0 = 0
    max_now1 = 0

    for i in range(n):
        now0 = arr[0][i]
        now1 = arr[1][i]

        if i > 1: now0 = max(now0, arr[0][i] + pre_max_now0)
        now0 = max(now0, arr[0][i] + max_now1)

        if i > 1: now1 = max(now1, arr[1][i] + pre_max_now1)
        now1 = max(now1, arr[1][i] + max_now0)

        dp[0][i] = now0
        dp[1][i] = now1

        pre_max_now0 = max(pre_max_now0, max_now0)
        pre_max_now1 = max(pre_max_now1, max_now1)

        max_now0 = max(now0, max_now0)
        max_now1 = max(now1, max_now1) 

    print(max(max_now0, max_now1))