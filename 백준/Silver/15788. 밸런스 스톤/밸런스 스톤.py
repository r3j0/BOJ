import sys
input = sys.stdin.readline

n = int(input().rstrip())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]

S = set()
for i in range(n):
    sums = 0
    on = 0
    for j in range(n):
        sums += maps[i][j]
        if maps[i][j] == 0: on = 1
    
    S.add((sums, on))

for i in range(n):
    sums = 0
    on = 0
    for j in range(n):
        sums += maps[j][i]
        if maps[j][i] == 0: on = 1
    
    S.add((sums, on))

sums = 0
on = 0
for i in range(n):
    sums += maps[i][i]
    if maps[i][i] == 0: on = 1

S.add((sums, on))

sums = 0
on = 0
for i in range(n):
    sums += maps[n-1-i][i]
    if maps[n-1-i][i] == 0: on = 1

S.add((sums, on))

if len(S) == 2:
    a = S.pop()
    b = S.pop()
    print(abs(a[0]-b[0]))
else: print(-1)