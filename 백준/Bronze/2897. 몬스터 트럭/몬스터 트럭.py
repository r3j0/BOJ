import sys
input = sys.stdin.readline

r, c = map(int, input().rstrip().split())
maps = [list(input().rstrip()) for _ in range(r)]

def countSpace(a, b, c, d):
    cntBlank = 0
    cntCar = 0
    if a == '.': cntBlank += 1
    elif a == 'X': cntCar += 1

    if b == '.': cntBlank += 1
    elif b == 'X': cntCar += 1

    if c == '.': cntBlank += 1
    elif c == 'X': cntCar += 1

    if d == '.': cntBlank += 1
    elif d == 'X': cntCar += 1

    return cntBlank, cntCar

cnt = 0
for i in range(r-1):
    for j in range(c-1):
        blank, car = countSpace(maps[i][j], maps[i+1][j], maps[i][j+1], maps[i+1][j+1])
        if blank == 4: cnt += 1
print(cnt)

cnt = 0
for i in range(r-1):
    for j in range(c-1):
        blank, car = countSpace(maps[i][j], maps[i+1][j], maps[i][j+1], maps[i+1][j+1])
        if blank == 3 and car == 1: cnt += 1
print(cnt)

cnt = 0
for i in range(r-1):
    for j in range(c-1):
        blank, car = countSpace(maps[i][j], maps[i+1][j], maps[i][j+1], maps[i+1][j+1])
        if blank == 2 and car == 2: cnt += 1
print(cnt)

cnt = 0
for i in range(r-1):
    for j in range(c-1):
        blank, car = countSpace(maps[i][j], maps[i+1][j], maps[i][j+1], maps[i+1][j+1])
        if blank == 1 and car == 3: cnt += 1
print(cnt)

cnt = 0
for i in range(r-1):
    for j in range(c-1):
        blank, car = countSpace(maps[i][j], maps[i+1][j], maps[i][j+1], maps[i+1][j+1])
        if car == 4: cnt += 1
print(cnt)