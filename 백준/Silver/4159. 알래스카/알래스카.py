import sys
input = sys.stdin.readline

while True:
    n = int(input().rstrip())
    if n == 0: break
    arr = [int(input().rstrip()) for _ in range(n)]
    maps = [0 for _ in range(1423)]
    for a in arr: maps[a] = 1
    energy = 0
    done = True
    for i in range(1423):
        if maps[i] == 1: energy = 200
        else: 
            energy -= 1
            if energy == 0: done = False
    for i in range(1422, -1, -1):
        if maps[i] == 1: energy = 200
        else: 
            energy -= 1
            if energy == 0: done = False
    
    print('POSSIBLE' if done else 'IMPOSSIBLE')