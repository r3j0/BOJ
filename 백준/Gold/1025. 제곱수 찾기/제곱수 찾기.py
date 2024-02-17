import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]

row = [-1, 1, 0, 0, -1, -1, 1, 1]
col = [0, 0, -1, 1, -1, 1, -1, 1]

result = -1
def backtracking(now, y, x, rowd, cold, dir):
    global result
    global row
    global col

    if int(''.join(map(str, now))) == int(int(''.join(map(str, now)))**0.5)**2:
        result = max(result, int(''.join(map(str, now))))

    if dir == -1: # 방향 정하기
        for d in range(8):
            for i in range(1, 9):
                for j in range(1, 9):
                    backtracking(now, y, x, i, j, d)
    else:
        if 0 <= y + row[dir]*rowd < n and 0 <= x + col[dir]*cold < m:
            now.append(arr[y + row[dir]*rowd][x + col[dir]*cold])
            backtracking(now, y + row[dir]*rowd, x + col[dir]*cold, rowd, cold, dir)
            now.pop()


for i in range(n):
    for j in range(m):
        backtracking([arr[i][j]], i, j, 0, 0, -1)

print(result)