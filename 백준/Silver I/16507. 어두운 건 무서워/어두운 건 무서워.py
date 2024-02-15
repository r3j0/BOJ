import sys
input = sys.stdin.readline

r, c, q = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(r)]

sums = [[0 for _ in range(c+1)]]
for i in range(r):
    now = [0]
    for j in range(c): now.append(now[-1] + sums[i][j+1] - sums[i][j] + arr[i][j])
    sums.append(now)

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().rstrip().split())
    print((sums[r2][c2] - sums[r2][c1-1] - sums[r1-1][c2] + sums[r1-1][c1-1])//((r2-r1+1)*(c2-c1+1)))