import sys
input = sys.stdin.readline

n = int(input().rstrip())
cnt = 0
for _ in range(n): cnt += len(input().rstrip())
print(cnt)