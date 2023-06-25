import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
maps = [list(input().rstrip()) for _ in range(n)]

result = 0
for i in range(n):
    for j in range(m):
        if maps[i][j] == '#':
            lines = maps[i].count('#')
            if lines % 2 == 0:
                result = 3
                break
            if maps[i+(lines//2)][j] == '.': 
                result = 1
            elif maps[i+(lines//2)][j+lines-1] == '.':
                result = 2
            elif maps[i+lines-1][j+(lines//2)] == '.':
                result = 4
            
            break
    if result != 0: break
            

if result == 1: print('LEFT')
elif result == 2: print('RIGHT')
elif result == 3: print('UP')
elif result == 4: print('DOWN')