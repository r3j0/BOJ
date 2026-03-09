# 10026 : 적록색약
import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
maps = [list(input().rstrip()) for _ in range(n)]

ans = []
def solve(mode):
    vis = [[False for _ in range(n)] for _ in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(n):
            if not vis[i][j]:
                vis[i][j] = True
                bfs(mode, vis, [i, j], maps[i][j])
                cnt += 1
    
    return cnt

def bfs(mode, vis, pos, ch):
    same_ch = {'R':0, 'G':1, 'B':2}
    if mode: same_ch['G'] = 0

    queue = deque()
    queue.append(pos)

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while queue:
        now = queue.popleft()

        for d in range(4):
            ny = now[0] + dy[d]
            nx = now[1] + dx[d]

            if 0 <= ny < n and 0 <= nx < n and (not vis[ny][nx]) and (same_ch[maps[ny][nx]] == same_ch[ch]):
                vis[ny][nx] = True
                queue.append([ny, nx])

# 적록색약이 아닌 사람
ans.append(solve(False))

# 적록색약인 사람
ans.append(solve(True))

print(' '.join(map(str, ans)))