import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
cluster = int(input().rstrip())
cnt = 0
for a in arr:
    cnt += a // cluster + (1 if a % cluster != 0 else 0)

print(cluster * cnt)