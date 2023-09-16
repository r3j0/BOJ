import sys
input = sys.stdin.readline

n = int(input().rstrip())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]

white = {}
for i in range(n):
    for j in range(n):
        if maps[i][j] == 2: white[str(i)+"_"+str(j)] = 1

row = [-1, 1, 0, 0, -1, -1, 1, 1]
col = [0, 0, -1, 1, -1, 1, -1, 1]
result = 0

def backtracking(now_white):
    global result
    if len(now_white) == 1:
        result = 1
        return

    key_list = now_white.keys()
    for k in key_list:
        y, x = map(int, k.split('_'))
        for d in range(8):
            ny = y + row[d]
            nx = x + col[d]
            meet_white = 0
            meet_white_pos = ''
            while 0 <= ny < n and 0 <= nx < n:
                if meet_white == 0:
                    if now_white.get(str(ny)+"_"+str(nx)):
                        meet_white = 1
                        meet_white_pos = str(ny)+"_"+str(nx)
                else:
                    if maps[ny][nx] != 1:
                        del now_white[k]
                        del now_white[meet_white_pos]
                        now_white[str(ny)+"_"+str(nx)] = 1
                        backtracking(now_white)
                        if result == 1: return
                        del now_white[str(ny)+"_"+str(nx)]
                        now_white[meet_white_pos] = 1
                        now_white[k] = 1

                ny += row[d]
                nx += col[d]
            

backtracking(white)

print('Possible' if result == 1 else 'Impossible')