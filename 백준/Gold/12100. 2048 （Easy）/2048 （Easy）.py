import sys
input = sys.stdin.readline

n = int(input().rstrip())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]

def moving(n, m, d):
    # 동 남 서 북
    row = [0, 1, 0, -1]
    col = [1, 0, -1, 0]
    merged = [[0 for _ in range(n)] for _ in range(n)]

    # 특정 방향에 가까운 블럭부터 먼저 실행
    if d == 0: # 동
        for i in range(n):
            for j in range(n - 2, -1, -1):
                if m[i][j] != 0:
                    nx = j
                    while nx < n - 1 and m[i][nx + 1] == 0:
                        m[i][nx + 1] = m[i][nx]
                        m[i][nx] = 0
                        nx += 1
                    
                    if nx != n - 1 and m[i][nx + 1] == m[i][nx] and merged[i][nx + 1] == 0:
                        m[i][nx] = 0
                        m[i][nx + 1] *= 2
                        merged[i][nx + 1] = 1
    elif d == 1: # 남
        for j in range(n):
            for i in range(n - 2, -1, -1):
                if m[i][j] != 0:
                    ny = i
                    while ny < n - 1 and m[ny + 1][j] == 0:
                        m[ny + 1][j] = m[ny][j]
                        m[ny][j] = 0
                        ny += 1
                    
                    if ny != n - 1 and m[ny + 1][j] == m[ny][j] and merged[ny + 1][j] == 0:
                        m[ny][j] = 0
                        m[ny + 1][j] *= 2
                        merged[ny + 1][j] = 1

    elif d == 2: # 서
        for i in range(n):
            for j in range(1, n):
                if m[i][j] != 0:
                    nx = j
                    while nx > 0 and m[i][nx - 1] == 0:
                        m[i][nx - 1] = m[i][nx]
                        m[i][nx] = 0
                        nx -= 1
                    
                    if nx != 0 and m[i][nx - 1] == m[i][nx] and merged[i][nx - 1] == 0:
                        m[i][nx] = 0
                        m[i][nx - 1] *= 2
                        merged[i][nx - 1] = 1

    elif d == 3: # 북
        for j in range(n):
            for i in range(1, n):
                if m[i][j] != 0:
                    ny = i
                    while ny > 0 and m[ny - 1][j] == 0:
                        m[ny - 1][j] = m[ny][j]
                        m[ny][j] = 0
                        ny -= 1
                    
                    if ny != 0 and m[ny - 1][j] == m[ny][j] and merged[ny - 1][j] == 0:
                        m[ny][j] = 0
                        m[ny - 1][j] *= 2
                        merged[ny - 1][j] = 1

    return list(m)

def backtracking(n, m, cnt):
    if cnt == 5:
        max_value = 0
        for i in range(n): max_value = max(max_value, max(m[i]))
        return max_value
    
    max_dir = 0
    for i in range(4): 
        new_arr = []
        for ni in range(n):
            new_arr_row = []
            for nj in range(n): new_arr_row.append(m[ni][nj])
            new_arr.append(new_arr_row)

        max_dir = max(max_dir, backtracking(n, moving(n, new_arr, i), cnt + 1))
    return max_dir

print(backtracking(n, maps, 0))