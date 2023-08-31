import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]

nine = 0
for i in range(n):
    for j in range(m):
        nine += str(maps[i][j]).count('9')

max_nine = 0

for i in range(n):
    now = 0
    for j in range(m):
        now += str(maps[i][j]).count('9')
    max_nine = max(max_nine, now)

for j in range(m):
    now = 0
    for i in range(n):
        now += str(maps[i][j]).count('9')
    max_nine = max(max_nine, now)

print(nine - max_nine)