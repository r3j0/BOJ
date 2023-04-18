import sys
import math
input = sys.stdin.readline

n, m, k = map(int, input().split())

sums = 0
for i in range(k):
    sums += (math.comb(n, m) * (math.comb(n - m, m - i) * math.comb(m, i)))
print(1 - (sums / (math.comb(n, m) ** 2)))