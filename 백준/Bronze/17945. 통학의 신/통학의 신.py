import sys
import math
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
if a**2 - b == 0: print(-a)
else: 
    res = [-a+int(math.sqrt(a**2-b)), -a-int(math.sqrt(a**2-b))]
    print(min(res), max(res))