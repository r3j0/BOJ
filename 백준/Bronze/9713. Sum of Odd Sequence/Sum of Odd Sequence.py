import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    now = 0
    if n % 2 == 1: now = (n + 1) // 2
    else: now = n // 2
    print(now*(now+1) - now)