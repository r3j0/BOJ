import sys
input = sys.stdin.readline

n = int(input().rstrip())
maps = [list(input().rstrip()) for _ in range(n)]

maps_reverse = []
for j in range(n):
    now = ""
    for i in range(n):
        now += maps[i][j]
    maps_reverse.append(list(now))

done = 1
for i in range(n):
    if maps[i] != maps_reverse[i]:
        done = 0
        break

print('YES' if done == 1 else 'NO')