import sys
input = sys.stdin.readline

n = int(input().rstrip())
mine = [list(input().rstrip()) for _ in range(n)]
board = [list(input().rstrip()) for _ in range(n)]

row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, -1, 1, -1, 0, 1]

flag = False
for i in range(n):
    for j in range(n):
        if board[i][j] == 'x':
            if mine[i][j] == '*': 
                flag = True
            cnt = 0
            for d in range(8):
                ny = i + row[d]
                nx = j + col[d]
                if 0 <= ny < n and 0 <= nx < n and mine[ny][nx] == '*': cnt += 1
            
            board[i][j] = str(cnt)

if flag == True:
    for i in range(n):
        for j in range(n):
            if mine[i][j] == '*': 
                board[i][j] = '*'

for i in range(n): print(''.join(board[i]))