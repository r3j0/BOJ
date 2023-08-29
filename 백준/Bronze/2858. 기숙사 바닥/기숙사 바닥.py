# 빨간색 : l * w - ((l-1) * (w-1))
# 갈색 : (l-1) * (w-1)

import sys
from math import *
input = sys.stdin.readline

r, b = map(int, input().rstrip().split())

for i in range(1, int(sqrt(r+b))+1):
    if (r+b) % i != 0: continue
    w = i
    l = (r+b) // i

    if (l*w)-((l-2)*(w-2)) == r and (l-2)*(w-2) == b:
        print(l, w)
        break