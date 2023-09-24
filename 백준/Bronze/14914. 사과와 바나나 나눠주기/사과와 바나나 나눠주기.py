import sys
import math
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
for i in range(1, math.gcd(a, b) + 1):
    if a % i == 0 and b % i == 0:
        print(i, a//i, b//i)