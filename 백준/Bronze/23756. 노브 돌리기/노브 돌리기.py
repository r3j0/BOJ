import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = int(input().rstrip())
result = 0
for _ in range(n):
    tmp = int(input().rstrip())

    if a < tmp: result += min(tmp - a, 360 - tmp + a)
    else: result += min(a - tmp, 360 - a + tmp)
    a = tmp

print(result)