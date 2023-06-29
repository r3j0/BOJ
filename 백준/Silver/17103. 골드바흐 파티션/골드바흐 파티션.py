from math import *

num = [0 for _ in range(1000001)]
for i in range(2, int(sqrt(1000001))+1):
    j = 2
    while i * j <= 1000000:
        num[i * j] = 1
        j += 1
num[0] = 1
num[1] = 1
import sys
input = sys.stdin.readline

test = int(input().rstrip())
for _ in range(test):
    n = int(input().rstrip())

    cnt = 0
    i = 2
    while i <= (n - i):
        if num[i] == 0 and num[n - i] == 0:
            cnt += 1
        i += 1
    
    print(cnt)