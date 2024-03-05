import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    a, b, c, p = map(int, input().rstrip().split())
    if a % p == b % p == 0 or b % p == c % p == 0 or c % p == a % p == 0: print(1)
    else: print(0)