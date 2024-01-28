import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]
order = [list(map(int, input().rstrip().split())) for _ in range(m)]
vis = [[0 for _ in range(n)] for _ in range(n)]

now = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]

row = [0, -1, -1, -1, 0, 1, 1, 1]
col = [-1, -1, 0, 1, 1, 1, 0, -1]

drow = [-1, -1, 1, 1]
dcol = [-1, 1, -1, 1]

for o in order:
    now_size = len(now)
    for ki in range(o[1]):
        for ni in range(now_size):
            now[ni][0] += row[o[0]-1]
            if now[ni][0] < 0: now[ni][0] = n - 1
            elif now[ni][0] > n - 1: now[ni][0] = 0
            now[ni][1] += col[o[0]-1]
            if now[ni][1] < 0: now[ni][1] = n - 1
            elif now[ni][1] > n - 1: now[ni][1] = 0
    
    for ni in range(now_size):
        maps[now[ni][0]][now[ni][1]] += 1
        vis[now[ni][0]][now[ni][1]] = 1
    
    arr = []
    for ni in range(now_size):
        cnt = 0
        for d in range(4):
            if 0 <= now[ni][0] + drow[d] < n and 0 <= now[ni][1] + dcol[d] < n and maps[now[ni][0] + drow[d]][now[ni][1] + dcol[d]] > 0: cnt += 1
        if cnt > 0: arr.append([ni, cnt])
    
    for a in arr:
        maps[now[a[0]][0]][now[a[0]][1]] += a[1]
    
    now = []
    for i in range(n):
        for j in range(n):
            if maps[i][j] >= 2 and vis[i][j] == 0:
                maps[i][j] -= 2
                now.append([i, j])
            else:
                vis[i][j] = 0

sums = 0
for i in range(n):
    for j in range(n):
        sums += maps[i][j]

print(sums)