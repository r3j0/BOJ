import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
cnt = [0 for _ in range(n)]
for i in range(m):
    a, b = map(int, input().rstrip().split())
    cnt[a-1] += 1
    cnt[b-1] += 1

for c in cnt:
    print(c)