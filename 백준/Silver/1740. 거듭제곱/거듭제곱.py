import sys
input = sys.stdin.readline

n = int(input().rstrip())
res = 0
cnt = 0
while n > 0:
    res += (3 ** cnt) * (n % 2)
    n //= 2
    cnt += 1
print(res)