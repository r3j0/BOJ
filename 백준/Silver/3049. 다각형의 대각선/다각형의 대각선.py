import sys
import math
input = sys.stdin.readline

n = int(input().rstrip())
if n == 3: print(0)
else: print(math.comb(n, n-4))