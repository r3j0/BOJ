import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]

visit = [[0 for j in range(m)] for i in range(n)]
group_map = [[0 for j in range(m)] for i in range(n)]
group_tiles = {}
walls = []

row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]

groups = 1
for i in range(n):
    for j in range(m):
        if arr[i][j] == '1': walls.append([i, j])
        elif visit[i][j] == 0:
            tiles = 0

            stack1 = []
            stack2 = []
            stack_mode = 1
            
            stack1.append([i, j])
            visit[i][j] = 1

            while True:
                size = 0
                if stack_mode == 1: size = len(stack1)
                else: size = len(stack2)

                if size == 0: break

                for s in range(size):
                    y = 0; x = 0
                    if stack_mode == 1:
                        y = stack1[s][0]
                        x = stack1[s][1]
                    else:
                        y = stack2[s][0]
                        x = stack2[s][1]

                    group_map[y][x] = groups
                    tiles += 1

                    for d in range(4):
                        ny = y + row[d]
                        nx = x + col[d]

                        if 0 <= ny < n and 0 <= nx < m and arr[ny][nx] == '0' and visit[ny][nx] == 0:
                            visit[ny][nx] = 1
                            if stack_mode == 1:
                                stack2.append([ny, nx])
                            else:
                                stack1.append([ny, nx])
                if stack_mode == 1:
                    stack_mode = 2
                    stack1 = []
                else:
                    stack_mode = 1
                    stack2 = []
            
            group_tiles[groups] = tiles
            groups += 1

new_map = [['0' for j in range(m)] for i in range(n)]

for w in range(len(walls)):
    already = {}
    go_tiles = 1

    # Left
    if walls[w][1] > 0 and arr[walls[w][0]][walls[w][1] - 1] == '0':
        gval = group_map[walls[w][0]][walls[w][1] - 1]
        already[gval] = 1
        go_tiles += group_tiles[gval]
    
    # Right
    if walls[w][1] < m - 1 and arr[walls[w][0]][walls[w][1] + 1] == '0':
        gval = group_map[walls[w][0]][walls[w][1] + 1]
        if already.get(gval, -1) == -1:
            already[gval] = 1
            go_tiles += group_tiles[gval]

    # Up
    if walls[w][0] > 0 and arr[walls[w][0] - 1][walls[w][1]] == '0':
        gval = group_map[walls[w][0] - 1][walls[w][1]]
        if already.get(gval, -1) == -1:
            already[gval] = 1
            go_tiles += group_tiles[gval]

    # Down
    if walls[w][0] < n - 1 and arr[walls[w][0] + 1][walls[w][1]] == '0':
        gval = group_map[walls[w][0] + 1][walls[w][1]]
        if already.get(gval, -1) == -1:
            already[gval] = 1
            go_tiles += group_tiles[gval]

    new_map[walls[w][0]][walls[w][1]] = str(go_tiles%10)

for i in range(n):
    print(''.join(new_map[i]))