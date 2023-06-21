import math
import sys
input = sys.stdin.readline

a1, p1 = map(int, input().rstrip().split())
r1, p2 = map(int, input().rstrip().split())

if (a1/p1 <= math.pi*(r1**2)/p2):
    print('Whole pizza')
else:
    print('Slice of pizza')