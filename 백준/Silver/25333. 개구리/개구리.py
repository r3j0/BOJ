import sys
import math
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    a, b, x = map(int, input().rstrip().split())
    print(x//(math.gcd(a, b)))