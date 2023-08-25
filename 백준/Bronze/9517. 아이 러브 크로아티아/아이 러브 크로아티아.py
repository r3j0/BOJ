# 210초 / 8명

import sys
input = sys.stdin.readline

k = int(input().rstrip()) - 1
n = int(input().rstrip())
now_time = 0
result = -1
for _ in range(n):
    time, status = input().rstrip().split()
    now_time += int(time)
    if now_time >= 210 and result == -1:
        result = k

    if status == 'T':
        k = (k + 1) % 8

print(result + 1)