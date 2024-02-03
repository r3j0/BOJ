import sys
input = sys.stdin.readline

n = int(input().rstrip())

now = 1
for i in range(1, n+1):
    now *= i
    now %= 100000000
    while now > 10 and now % 10 == 0: now //= 10

print(now % 10)
