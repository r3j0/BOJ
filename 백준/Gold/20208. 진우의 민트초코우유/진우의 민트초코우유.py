import sys
input = sys.stdin.readline

n, m, h = map(int, input().rstrip().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]
mincho = []
home = []
start = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 2:
            mincho.append([i, j])
        elif maps[i][j] == 1:
            home = [i, j]
            start = [i, j]

visited = [0 for _ in range(len(mincho))]
res = 0
def backtracking(now_pos, now_cnt, now_hp):
    global res
    if now_cnt != 0 and now_pos[0] == home[0] and now_pos[1] == home[1]:
        res = max(res, now_cnt)
        return

    for i in range(len(mincho)):
        if visited[i] == 0 and now_hp - (abs(mincho[i][0] - now_pos[0]) + abs(mincho[i][1] - now_pos[1])) >= 0:
            visited[i] = 1
            backtracking([mincho[i][0], mincho[i][1]], now_cnt + 1, now_hp - (abs(mincho[i][0] - now_pos[0]) + abs(mincho[i][1] - now_pos[1])) + h)
            visited[i] = 0
    if now_cnt != 0 and now_hp - (abs(home[0] - now_pos[0]) + abs(home[1] - now_pos[1])) >= 0:
        backtracking([home[0], home[1]], now_cnt, now_hp - (abs(home[0] - now_pos[0]) + abs(home[1] - now_pos[1])))

backtracking(start, 0, m)
print(res)