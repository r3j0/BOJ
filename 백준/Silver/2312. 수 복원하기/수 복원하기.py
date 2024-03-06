arr = [0 for _ in range(100001)]
arr[0] = 1
arr[1] = 1
for i in range(2, 50001):
    j = 2
    while i * j <= 100000:
        arr[i * j] = 1
        j += 1

import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    sus = {}
    now = 2
    while n > 1:
        while arr[now] == 1 or n % now != 0: now += 1
        if sus.get(now): sus[now] += 1
        else: sus[now] = 1
        n //= now
    res = list(sus.items())
    res.sort(key=lambda x:x[0])
    for k, v in res: print(k, v)