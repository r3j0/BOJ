import sys
input = sys.stdin.readline

n = int(input().rstrip())
cnt = 0

for a in range(1, 501):
    for b in range(1, 501):
        if a**2 == b**2 + n: cnt += 1

print(cnt)