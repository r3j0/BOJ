import sys
import math
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n, a, b = map(int, input().rstrip().split())
    abg = math.gcd(a, b)
    start = n
    while abg % 2**start:
        start -= 1
    
    print(n - start)