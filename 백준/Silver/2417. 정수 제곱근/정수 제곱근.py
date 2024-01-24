import sys
import math
input = sys.stdin.readline

n = int(input().rstrip())
s = math.isqrt(n)
if s**2 < n: s += 1
print(s)
