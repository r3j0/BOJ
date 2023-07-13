import sys
input = sys.stdin.readline

s = int(input().rstrip())
now = 1
while now < s:
    s -= now
    now += 1

print(now + (0 if s == now else -1))