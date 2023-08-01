import sys
import math
input = sys.stdin.readline

n, w, h = map(int, input().rstrip().split())
threshold = math.sqrt(w**2+h**2)
for _ in range(n):
    if threshold >= int(input()):
        print('DA')
    else:
        print('NE')