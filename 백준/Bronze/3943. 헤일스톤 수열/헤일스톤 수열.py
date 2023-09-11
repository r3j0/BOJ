import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())

    max_n = n
    while n != 1:
        if n % 2 == 0: n //= 2
        else: n = n * 3 + 1
        max_n = max(max_n, n)

    print(max_n)