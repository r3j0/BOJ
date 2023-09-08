import sys
input = sys.stdin.readline

n, k, l = map(int, input().rstrip().split())

res = []
for _ in range(n):
    arr = list(map(int, input().rstrip().split()))
    if sum(arr) >= k and min(arr) >= l: res.append(arr)

print(len(res))
for r in res:
    print(' '.join(map(str, r)), end=' ')