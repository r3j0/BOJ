import sys
from math import *
input = sys.stdin.readline

x1, y1, r1 = map(int, input().rstrip().split())
x2, y2, r2 = map(int, input().rstrip().split())

if r1 + r2 <= sqrt(abs(x1-x2)**2+abs(y1-y2)**2):
    print('NO')
else:
    print('YES')