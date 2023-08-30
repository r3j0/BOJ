import sys
input = sys.stdin.readline

def two(n):
    while n > 1:
        if n % 2 != 0: return 0
        n /= 2
    return 1

n = int(input().rstrip())
if n == 0: print(0)
elif n == 1: print(1)
else: print(len(str(bin(n))[2:]) + (0 if two(n) else 1))