import sys
input = sys.stdin.readline

n = int(input().rstrip())
now = 1
cnt = 0
while n != 0:
    n -= now
    cnt += 1

    now += 1
    if n < now:
        now = 1

print(cnt)