import sys
input = sys.stdin.readline

for _ in range(3):
    n = int(input().rstrip())
    now = 0
    for _ in range(n):
        now += int(input().rstrip())
    if now > 0: print('+')
    elif now < 0: print('-')
    else: print(0)
        