import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

cnt = 0
for a in arr:
    cnt += (a + 1) // 2

print('YES' if cnt >= n else 'NO')