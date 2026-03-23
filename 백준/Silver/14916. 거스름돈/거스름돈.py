# 14916 : 거스름돈
import sys
input = sys.stdin.readline

n = int(input().rstrip())
coins5 = n // 5
n %= 5
while n % 2 != 0 and coins5 > 0:
    n += 5
    coins5 -= 1

if n % 2 == 0:
    print(coins5 + n // 2)
else:
    print(-1)
