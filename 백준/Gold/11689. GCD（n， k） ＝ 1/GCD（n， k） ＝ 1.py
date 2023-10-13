import sys
input = sys.stdin.readline
n = int(input())
result = now = n
i = 2
while i**2 <= n:
    if now % i == 0:
        result //= i
        result *= i - 1

        while now % i == 0: now //= i

    i += 1

if now != 1:
    result //= now
    result *= now - 1

print(result)   