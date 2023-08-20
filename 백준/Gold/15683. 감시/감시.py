import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]

cctv = []
sagak = 0
for i in range(n):
    for j in range(m):
        if 1 <= maps[i][j] <= 5:
            cctv.append((i, j, maps[i][j]))
        elif maps[i][j] == 0:
            sagak += 1

row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]


def backtracking(map, now_cctv, now_sagak):
    if len(now_cctv) == 0:
        return now_sagak

    go_cctv = now_cctv[-1]
    del now_cctv[-1]

    result = now_sagak

    # gamsi
    if go_cctv[2] == 1:
        for d in range(4):
            ny = go_cctv[0] + row[d]
            nx = go_cctv[1] + col[d]

            while 0 <= ny < n and 0 <= nx < m and map[ny][nx] != 6:
                if map[ny][nx] == 0: now_sagak -= 1
                if map[ny][nx] <= 0: map[ny][nx] -= 1
                ny += row[d]
                nx += col[d]
            
            result = min(result, backtracking(map, now_cctv, now_sagak))

            ny = go_cctv[0] + row[d]
            nx = go_cctv[1] + col[d]
            while 0 <= ny < n and 0 <= nx < m and map[ny][nx] != 6:
                if map[ny][nx] <= 0: map[ny][nx] += 1
                if map[ny][nx] == 0: now_sagak += 1
                ny += row[d]
                nx += col[d]

    elif go_cctv[2] == 2:
        for d in range(2):
            ny = go_cctv[0] + row[d]
            nx = go_cctv[1] + col[d]

            while 0 <= ny < n and 0 <= nx < m and map[ny][nx] != 6:
                if map[ny][nx] == 0: now_sagak -= 1
                if map[ny][nx] <= 0: map[ny][nx] -= 1
                ny += row[d]
                nx += col[d]

            ny = go_cctv[0] + row[d+2]
            nx = go_cctv[1] + col[d+2]

            while 0 <= ny < n and 0 <= nx < m and map[ny][nx] != 6:
                if map[ny][nx] == 0: now_sagak -= 1
                if map[ny][nx] <= 0: map[ny][nx] -= 1
                ny += row[d+2]
                nx += col[d+2]
            
            result = min(result, backtracking(map, now_cctv, now_sagak))

            ny = go_cctv[0] + row[d]
            nx = go_cctv[1] + col[d]
            while 0 <= ny < n and 0 <= nx < m and map[ny][nx] != 6:
                if map[ny][nx] <= 0: map[ny][nx] += 1
                if map[ny][nx] == 0: now_sagak += 1
                ny += row[d]
                nx += col[d]

            ny = go_cctv[0] + row[d+2]
            nx = go_cctv[1] + col[d+2]
            while 0 <= ny < n and 0 <= nx < m and map[ny][nx] != 6:
                if map[ny][nx] <= 0: map[ny][nx] += 1
                if map[ny][nx] == 0: now_sagak += 1
                ny += row[d+2]
                nx += col[d+2]

    elif go_cctv[2] == 3:
        for d in range(4):
            ny = go_cctv[0] + row[d]
            nx = go_cctv[1] + col[d]

            while 0 <= ny < n and 0 <= nx < m and map[ny][nx] != 6:
                if map[ny][nx] == 0: now_sagak -= 1
                if map[ny][nx] <= 0: map[ny][nx] -= 1
                ny += row[d]
                nx += col[d]

            ny = go_cctv[0] + row[(d+1) % 4]
            nx = go_cctv[1] + col[(d+1) % 4]

            while 0 <= ny < n and 0 <= nx < m and map[ny][nx] != 6:
                if map[ny][nx] == 0: now_sagak -= 1
                if map[ny][nx] <= 0: map[ny][nx] -= 1
                ny += row[(d+1) % 4]
                nx += col[(d+1) % 4]
            
            result = min(result, backtracking(map, now_cctv, now_sagak))

            ny = go_cctv[0] + row[d]
            nx = go_cctv[1] + col[d]
            while 0 <= ny < n and 0 <= nx < m and map[ny][nx] != 6:
                if map[ny][nx] <= 0: map[ny][nx] += 1
                if map[ny][nx] == 0: now_sagak += 1
                ny += row[d]
                nx += col[d]

            ny = go_cctv[0] + row[(d+1) % 4]
            nx = go_cctv[1] + col[(d+1) % 4]
            while 0 <= ny < n and 0 <= nx < m and map[ny][nx] != 6:
                if map[ny][nx] <= 0: map[ny][nx] += 1
                if map[ny][nx] == 0: now_sagak += 1
                ny += row[(d+1) % 4]
                nx += col[(d+1) % 4]

    elif go_cctv[2] == 4:
        for d in range(4):
            ny = go_cctv[0] + row[d]
            nx = go_cctv[1] + col[d]

            while 0 <= ny < n and 0 <= nx < m and map[ny][nx] != 6:
                if map[ny][nx] == 0: now_sagak -= 1
                if map[ny][nx] <= 0: map[ny][nx] -= 1
                ny += row[d]
                nx += col[d]

            ny = go_cctv[0] + row[(d+1) % 4]
            nx = go_cctv[1] + col[(d+1) % 4]

            while 0 <= ny < n and 0 <= nx < m and map[ny][nx] != 6:
                if map[ny][nx] == 0: now_sagak -= 1
                if map[ny][nx] <= 0: map[ny][nx] -= 1
                ny += row[(d+1) % 4]
                nx += col[(d+1) % 4]

            ny = go_cctv[0] + row[(d+2) % 4]
            nx = go_cctv[1] + col[(d+2) % 4]

            while 0 <= ny < n and 0 <= nx < m and map[ny][nx] != 6:
                if map[ny][nx] == 0: now_sagak -= 1
                if map[ny][nx] <= 0: map[ny][nx] -= 1
                ny += row[(d+2) % 4]
                nx += col[(d+2) % 4]
            
            result = min(result, backtracking(map, now_cctv, now_sagak))

            ny = go_cctv[0] + row[d]
            nx = go_cctv[1] + col[d]
            while 0 <= ny < n and 0 <= nx < m and map[ny][nx] != 6:
                if map[ny][nx] <= 0: map[ny][nx] += 1
                if map[ny][nx] == 0: now_sagak += 1
                ny += row[d]
                nx += col[d]

            ny = go_cctv[0] + row[(d+1) % 4]
            nx = go_cctv[1] + col[(d+1) % 4]
            while 0 <= ny < n and 0 <= nx < m and map[ny][nx] != 6:
                if map[ny][nx] <= 0: map[ny][nx] += 1
                if map[ny][nx] == 0: now_sagak += 1
                ny += row[(d+1) % 4]
                nx += col[(d+1) % 4]

            ny = go_cctv[0] + row[(d+2) % 4]
            nx = go_cctv[1] + col[(d+2) % 4]
            while 0 <= ny < n and 0 <= nx < m and map[ny][nx] != 6:
                if map[ny][nx] <= 0: map[ny][nx] += 1
                if map[ny][nx] == 0: now_sagak += 1
                ny += row[(d+2) % 4]
                nx += col[(d+2) % 4]

    elif go_cctv[2] == 5:
        for d in range(4):
            ny = go_cctv[0] + row[d]
            nx = go_cctv[1] + col[d]

            while 0 <= ny < n and 0 <= nx < m and map[ny][nx] != 6:
                if map[ny][nx] == 0: now_sagak -= 1
                if map[ny][nx] <= 0: map[ny][nx] -= 1
                ny += row[d]
                nx += col[d]
            
        result = min(result, backtracking(map, now_cctv, now_sagak))

        for d in range(4):
            ny = go_cctv[0] + row[d]
            nx = go_cctv[1] + col[d]
            while 0 <= ny < n and 0 <= nx < m and map[ny][nx] != 6:
                if map[ny][nx] <= 0: map[ny][nx] += 1
                if map[ny][nx] == 0: now_sagak += 1
                ny += row[d]
                nx += col[d]

    now_cctv.append(go_cctv)
    return result

print(backtracking(maps, cctv, sagak))