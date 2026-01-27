# 1612 : 가지고 노는 1
import sys
input = sys.stdin.readline

n = int(input().rstrip())

if n == 1: print(1)
elif (n % 10) in [1, 3, 7, 9]:
    now_j = 1
    sums = 11 % n

    while sums != 0:
        now_j += 1
        sums = (sums * 10 + 1) % n

    print(now_j + 1)
else: print(-1)