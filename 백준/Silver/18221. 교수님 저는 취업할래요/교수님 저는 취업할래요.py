import sys
import math
input = sys.stdin.readline

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

profPos = []
sungPos = []

for i in range(n):
    for j in range(n):
        if maps[i][j] == 2: sungPos = [i, j]
        if maps[i][j] == 5: profPos = [i, j]

if ((sungPos[0] - profPos[0])**2) + ((sungPos[1] - profPos[1])**2) >= 25:
    cnt = 0
    for i in range(min(profPos[0], sungPos[0]), max(profPos[0], sungPos[0]) + 1):
        for j in range(min(profPos[1], sungPos[1]), max(profPos[1], sungPos[1]) + 1):
            if maps[i][j] == 1: cnt += 1
    if cnt >= 3: print(1)
    else: print(0)
else: print(0)