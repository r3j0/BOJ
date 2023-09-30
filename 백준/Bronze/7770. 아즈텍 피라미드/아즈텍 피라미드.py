import sys
input = sys.stdin.readline

n = int(input().rstrip())
now = 0
pre = 1
cnt = 0
while now < n:
    now = now + pre
    pre += 4 + (cnt * 4)
    cnt += 1

if now == n: print(cnt)
else: print(cnt - 1)