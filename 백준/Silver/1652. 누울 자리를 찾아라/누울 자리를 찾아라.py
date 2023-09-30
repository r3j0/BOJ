import sys
input = sys.stdin.readline

n = int(input().rstrip())
maps = [list(input().rstrip()) for _ in range(n)]
garo = 0
sero = 0

for i in range(n):
    cnt = 0
    for j in range(n):
        if maps[i][j] == '.': cnt += 1
        else:
            if cnt >= 2: garo += 1
            cnt = 0
    
    if cnt >= 2: garo += 1

for j in range(n):
    cnt = 0
    for i in range(n):
        if maps[i][j] == '.': cnt += 1
        else:
            if cnt >= 2: sero += 1
            cnt = 0
    
    if cnt >= 2: sero += 1

print(garo, sero)