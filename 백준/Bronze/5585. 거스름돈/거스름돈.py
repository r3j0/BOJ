# 5585 : 거스름돈
import sys
input = sys.stdin.readline

n = 1000 - int(input().rstrip())
arr = [500, 100, 50, 10, 5, 1]
cnt = 0
for a in arr:
    cnt += n // a
    n %= a
print(cnt)