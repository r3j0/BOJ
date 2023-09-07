import sys
input = sys.stdin.readline

n = int(input().rstrip())
idx = 1
while 10**idx < n:
    if int(str(n)[-idx]) >= 5:
        n = ((n // (10**idx)) + 1) * (10**idx)
    else:
        n = (n // (10**idx)) * (10**idx)
    idx += 1

print(n)