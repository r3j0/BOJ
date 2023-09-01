import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
pos = [[] for _ in range(10001)]

for x, y in arr:
    pos[x].append(1)
    pos[y].append(2)

posing = 0
cnt = 0
for i in range(1, 10001):
    posing += pos[i].count(1)
    posing -= pos[i].count(2)

    if posing > 0: cnt += 1

print(cnt)