import sys
import math

while True:
    a, b = map(int, input().rstrip().split())
    if a == b == 0: break

    print(math.comb(a, b))