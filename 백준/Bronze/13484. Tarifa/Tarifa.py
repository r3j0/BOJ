import sys
input = sys.stdin.readline

x = int(input().rstrip())
n = int(input().rstrip())
now = x
for _ in range(n):
    tmp = int(input().rstrip())
    now += x - tmp

print(max(0, now))