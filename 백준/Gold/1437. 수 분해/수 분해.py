import sys
input = sys.stdin.readline

n = int(input().rstrip())
if n == 0: print(0)
elif n == 1: print(1)
else:
    max_result = 3 ** (n // 3)
    n %= 3
    if n == 1: 
        max_result //= 3
        max_result *= 2
        max_result *= 2
    elif n == 2:
        max_result *= 2
    print(max_result % 10007)
