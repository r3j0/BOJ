import sys
input = sys.stdin.readline

a = int(input().rstrip())
b = int(input().rstrip())
now = 0
for _ in range(b+1):
    now += a
    a *= 10
print(now)