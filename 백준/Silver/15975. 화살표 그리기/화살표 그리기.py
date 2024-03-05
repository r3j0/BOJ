import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
colors = [[] for _ in range(100001)]
for a in arr:
    colors[a[1]].append(a[0])

res = 0
for i in range(100001):
    if len(colors[i]) > 1:
        colors[i].sort()
        for j in range(len(colors[i])):
            if j == 0:
                res += colors[i][j+1] - colors[i][j]
            elif j == len(colors[i]) - 1:
                res += colors[i][j] - colors[i][j-1]
            else:
                res += min(colors[i][j+1] - colors[i][j], colors[i][j] - colors[i][j-1])

print(res)
