import sys
from collections import deque
input = sys.stdin.readline

# 한 정육각형이 있을 때...
# 왼쪽 위 : (짝수) (y - 1, x - 1) 이 건물이 아닐 때 (홀수) (y, x - 1) 이 건물이 아닐 때
# 왼쪽 : (y - 1, x) 이 건물이 아닐 때
# 왼쪽 아래 : (짝수) (y - 1, x + 1) 이 건물이 아닐 때 (홀수) (y, x + 1) 이 건물이 아닐 때
# 오른쪽 위 : (짝수) (y, x - 1) (홀수) (y + 1, x - 1)
# 오른쪽 : (y + 1, x)
# 오른쪽 아래 : (짝수) (y, x + 1) (홀수) (y + 1, x + 1)

w, h = map(int, input().rstrip().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(h)]

row_odd = [-1, -1, -1, 0, 1, 0]
col_odd = [-1, 0, 1, -1, 0, 1]
row_even = [0, -1, 0, 1, 1, 1]
col_even = [-1, 0, 1, -1, 0, 1]
result = 0
for i in range(h):
    for j in range(w):
        if maps[i][j] == 0: 
            continue
        for d in range(6):
            if i % 2 == 0:
                if not (0 <= i + col_even[d] < h and 0 <= j + row_even[d] < w and maps[i + col_even[d]][j + row_even[d]] == 1): 
                    result += 1
            else:
                if not (0 <= i + col_odd[d] < h and 0 <= j + row_odd[d] < w and maps[i + col_odd[d]][j + row_odd[d]] == 1): 
                    result += 1

# 외부에서 연결된 0 들을 전부 없애기
def BFS(y, x):
    global maps
    queue = deque()
    queue.append([y, x])
    maps[y][x] = 1

    while queue:
        now = queue.popleft()
        for d in range(6):
            if now[0] % 2 == 0:
                if 0 <= now[0] + col_even[d] < h and 0 <= now[1] + row_even[d] < w and maps[now[0] + col_even[d]][now[1] + row_even[d]] == 0:
                    maps[now[0] + col_even[d]][now[1] + row_even[d]] = 1
                    queue.append([now[0] + col_even[d], now[1] + row_even[d]])
            else:
                if 0 <= now[0] + col_odd[d] < h and 0 <= now[1] + row_odd[d] < w and maps[now[0] + col_odd[d]][now[1] + row_odd[d]] == 0:
                    maps[now[0] + col_odd[d]][now[1] + row_odd[d]] = 1
                    queue.append([now[0] + col_odd[d], now[1] + row_odd[d]])
# Left
for i in range(h):
    if maps[i][0] == 0: BFS(i, 0)
# Right
for i in range(h):
    if maps[i][w-1] == 0: BFS(i, w-1)
# Up
for j in range(w):
    if maps[0][j] == 0: BFS(0, j)
# Down
for j in range(w):
    if maps[h-1][j] == 0: BFS(h-1, j)

# 남은 0 들은 갇힌 공간. 옆면 지우기
for i in range(h):
    for j in range(w):
        if maps[i][j] == 0:
            for d in range(6):
                if i % 2 == 0:
                    if 0 <= i + col_even[d] < h and 0 <= j + row_even[d] < w and maps[i + col_even[d]][j + row_even[d]] == 1: 
                        result -= 1
                else:
                    if 0 <= i + col_odd[d] < h and 0 <= j + row_odd[d] < w and maps[i + col_odd[d]][j + row_odd[d]] == 1: 
                        result -= 1
print(result)