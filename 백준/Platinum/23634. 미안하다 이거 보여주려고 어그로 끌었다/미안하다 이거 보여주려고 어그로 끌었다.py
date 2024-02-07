import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
maps = [list(input().rstrip()) for _ in range(n)]

# 1. 불 영역을 세서 그룹화
# 2. 돌로 나눠진 영역 세기 ( 불이 존재하는 돌 영역 개수가 최종 불 합쳐져야 하는 목표 )
# 3. 불 BFS 를 하되 다른 불과 붙을 때 union을 하면서 영역 줄이기

row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]

group = [[-1 for _ in range(m)] for _ in range(n)]

group_cnt = 1
last_size = 0
for i in range(n):
    for j in range(m):
        if maps[i][j] == '0' and group[i][j] == -1:
            queue = deque()
            queue.append([i, j])
            group[i][j] = group_cnt
            size = 0

            while queue:
                now = queue.popleft()
                size += 1
                for d in range(4):
                    ny = now[0] + row[d]
                    nx = now[1] + col[d]

                    if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == '0' and group[ny][nx] == -1:
                        queue.append([ny, nx])
                        group[ny][nx] = group_cnt

            group_cnt += 1
            last_size = size

if group_cnt == 1: print(0, 0)
elif group_cnt == 2: print(0, last_size)
else:
    goal = 0
    visited_stone = [[0 for _ in range(m)] for _ in range(n)]

    queue_fire = deque()

    for i in range(n):
        for j in range(m):
            if maps[i][j] == '0': queue_fire.append([i, j])
            if maps[i][j] != '2' and visited_stone[i][j] == 0:
                queue = deque()
                queue.append([i, j])
                visited_stone[i][j] = 1
                available = 0

                while queue:
                    now = queue.popleft()
                    if maps[now[0]][now[1]] == '0': available = 1
                    for d in range(4):
                        ny = now[0] + row[d]
                        nx = now[1] + col[d]

                        if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != '2' and visited_stone[ny][nx] == 0:
                            queue.append([ny, nx])
                            visited_stone[ny][nx] = 1
                
                if available == 1:
                    goal += 1
    
    # 목표 불 그룹 개수 / 현재 불 그룹 개수
    # print(goal, group_cnt - 1)

    arr = [i for i in range(group_cnt)]
    def parent(a):
        if a == arr[a]: return a
        arr[a] = parent(arr[a])
        return arr[a]

    def union(ay, ax, by, bx):
        global group_cnt
        group[ay][ax] = parent(group[ay][ax])
        group[by][bx] = parent(group[by][bx])
        a = group[ay][ax] 
        b = group[by][bx]
        
        if a != b:
            group_cnt -= 1
            if a < b:
                arr[group[by][bx]] = a
                return a
            else:
                arr[group[ay][ax]] = b
                return b
        return -1

    time = 0
    while queue_fire:
        if goal >= group_cnt - 1:
            break
        queue_size = len(queue_fire)
        for s in range(queue_size):
            now = queue_fire.popleft()

            for d in range(4):
                ny = now[0] + row[d]
                nx = now[1] + col[d]

                if 0 <= ny < n and 0 <= nx < m:
                    if maps[ny][nx] == '1':
                        queue_fire.append([ny, nx])
                        group[ny][nx] = group[now[0]][now[1]]
                        maps[ny][nx] = '0'
                        for dd in range(4):
                            nny = ny + row[dd]
                            nnx = nx + col[dd]

                            if 0 <= nny < n and 0 <= nnx < m and maps[nny][nnx] == '0' and group[nny][nnx] != group[ny][nx]:
                                res = union(nny, nnx, ny, nx)
                                if res == -1: continue
                                group[nny][nnx] = res
                                group[ny][nx] = res
        time += 1

    sums = 0
    for i in range(n): sums += maps[i].count('0')
    print(time, sums)   