import sys
input = sys.stdin.readline

arr = [[] for _ in range(3)]
player = []

n = int(input().rstrip())
for _ in range(n):
    a, b, c = map(int, input().rstrip().split())
    arr[0].append(a)
    arr[1].append(b)
    arr[2].append(c)
    player.append([a, b, c])

for i in range(n):
    now = 0
    if arr[0].count(player[i][0]) == 1: now += player[i][0]
    if arr[1].count(player[i][1]) == 1: now += player[i][1]
    if arr[2].count(player[i][2]) == 1: now += player[i][2]
    print(now)