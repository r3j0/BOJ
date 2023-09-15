import sys
input = sys.stdin.readline

start = int(input().rstrip())
maps = [[0 for _ in range(3)] for _ in range(3)]

def whoWin():
    for i in range(3):
        if maps[i].count(1) == 3: return 1
        if maps[i].count(2) == 3: return 2

    for j in range(3):
        cnt = 0
        for i in range(3):
            if maps[i][j] == 1: cnt += 1
            elif maps[i][j] == 2: cnt -= 1
        
        if cnt == 3: return 1
        elif cnt == -3: return 2
    
    cnt = 0
    for i in range(3):
        if maps[i][i] == 1: cnt += 1
        elif maps[i][i] == 2: cnt -= 1
    
    if cnt == 3: return 1
    elif cnt == -3: return 2

    cnt = 0
    for i in range(3):
        if maps[2-i][i] == 1: cnt += 1
        elif maps[2-i][i] == 2: cnt -= 1
    
    if cnt == 3: return 1
    elif cnt == -3: return 2

    return 0

done = 0
for _ in range(9):
    x, y = map(int, input().rstrip().split())
    maps[x-1][y-1] = start
    res = whoWin()
    if res == 1 or res == 2: 
        print(res)
        done = 1
        break
    start = 2 if start == 1 else 1

if done == 0: print(0)