import sys
from math import *
input = sys.stdin.readline

n = int(input().rstrip())
cnt = 0
for i in range(1, n+1):
    j = i
    while i*j <= n:
        cnt += 1
        j += 1
print(cnt)