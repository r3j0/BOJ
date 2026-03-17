# 15897 : 잘못 구현한 에라토스테네스의 체
import sys
input = sys.stdin.readline

n = int(input().rstrip())

ans = 0
i = 1
j = 0

while i <= n:
    j = n // (n // i)
    ans += n // i * (j - i + 1) + (j - i + (1 if n % j else 0))

    i = j + 1

print(ans)