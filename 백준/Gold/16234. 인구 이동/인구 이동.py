import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().rstrip().split())
A = [list(map(int, input().rstrip().split())) for _ in range(N)]
Aable = [[[[0, 0, 0, 0], 0] for _ in range(N)] for _ in range(N)]

row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]

time = 0

while True:
    done = 1
    for i in range(N):
        for j in range(N):
            Aable[i][j][1] = 0
            
            for d in range(4):
                Aable[i][j][0][d] = 0
                ny = i + row[d]
                nx = j + col[d]

                if 0 <= ny < N and 0 <= nx < N and L <= abs(A[ny][nx] - A[i][j]) <= R:
                    done = 0
                    Aable[i][j][0][d] = 1
                    Aable[ny][nx][0][(d+2)%4] = 1
    
    if done: break
    time += 1

    for i in range(N):
        for j in range(N):
            for k in range(4):
                if Aable[i][j][0][k] == 1 and Aable[i][j][1] == 0:
                    queue = deque()
                    queue.append([i, j])
                    Aable[i][j][1] = 1
                    sums = A[i][j]
                    cnt = 1
                    
                    while queue:
                        now = queue.popleft()

                        for d in range(4):
                            ny = now[0] + row[d]
                            nx = now[1] + col[d]

                            if 0 <= ny < N and 0 <= nx < N and Aable[now[0]][now[1]][0][d] == 1 and Aable[ny][nx][1] == 0:
                                Aable[ny][nx][1] = 1
                                sums += A[ny][nx]
                                cnt += 1
                                queue.append([ny, nx])
                    
                    queue = deque()
                    queue.append([i, j])
                    Aable[i][j][1] = 2
                    persons = sums // cnt
                    A[i][j] = persons

                    while queue:
                        now = queue.popleft()

                        for d in range(4):
                            ny = now[0] + row[d]
                            nx = now[1] + col[d]

                            if 0 <= ny < N and 0 <= nx < N and Aable[now[0]][now[1]][0][d] == 1 and Aable[ny][nx][1] == 1:
                                Aable[ny][nx][1] = 2
                                A[ny][nx] = persons
                                queue.append([ny, nx])

print(time)