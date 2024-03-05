import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
xPos = [0 for _ in range(100001)]
yPos = [0 for _ in range(100001)]
for a in arr:
    xPos[a[0]] += 1
    yPos[a[1]] += 1

res = 0
for a in arr:
    res += (yPos[a[1]] - 1) * (xPos[a[0]] - 1)
print(res)