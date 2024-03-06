import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
maps = [list(input().rstrip()) for _ in range(n)]

res = 1
for k in range(2, min(n, m)+1):
    for i in range(n-k+1):
        for j in range(m-k+1):
            if maps[i][j] == maps[i+k-1][j] == maps[i][j+k-1] == maps[i+k-1][j+k-1]: res = k
print(res**2)