import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
res = 0
for a in range(m-2):
    for b in range(a+1, m-1):
        for c in range(b+1, m):
            sums = 0
            for i in range(n):
                sums += max(arr[i][a], arr[i][b], arr[i][c])
            res = max(res, sums)
print(res)