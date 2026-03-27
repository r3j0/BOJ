# 2839 : 설탕 배달
import sys
input = sys.stdin.readline

n = int(input().rstrip())
v5 = n // 5
n %= 5
while v5 > 0 and n % 3 != 0:
    v5 -= 1
    n += 5

if n % 3 == 0:
    print(v5 + n // 3)
else:
    print(-1)