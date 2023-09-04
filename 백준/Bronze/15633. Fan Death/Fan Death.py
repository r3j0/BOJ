import sys
import math
input = sys.stdin.readline

n = int(input().rstrip())
sums = 0
for i in range(1, n+1):
    if n % i == 0:
        sums += i

print(sums*5-24)