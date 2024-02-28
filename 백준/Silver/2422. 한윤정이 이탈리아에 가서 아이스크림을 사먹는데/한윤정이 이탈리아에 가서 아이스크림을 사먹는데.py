import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
dic = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().rstrip().split())
    mi = min(x, y)
    ma = max(x, y)
    dic[mi][ma] = 1

res = 0
for a in range(1, n-1):
    for b in range(a+1, n):
        if dic[a][b] == 0:
            for c in range(b+1, n+1):
                if dic[a][c] == 0 and dic[b][c] == 0:
                    res += 1
print(res)