import sys
input = sys.stdin.readline

n = int(input().rstrip())
cnt = 0
for i in range(1, n - 1):
    for j in range(i + 1, n):
        for k in range(j + 2, n + 1):
            cnt += 1
print(cnt)