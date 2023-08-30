import sys
import math
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    a, b = map(int, input().rstrip().split())
    print(math.gcd(a, b))