import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
maps = [list(input().rstrip()) for _ in range(2)]
visited = [[0 for _ in range(n)] for _ in range(2)]

done = 0
queue = deque()
queue.append([0, 0])
visited[0][0] = 1

time = 0
while queue:
    size = len(queue)
    for s in range(size):
        now = queue.popleft()

        if now[1] + 1 >= n or now[1] + k >= n: 
            done = 1
            break
        
        if maps[now[0]][now[1]+1] == '1' and visited[now[0]][now[1]+1] == 0 and now[1]+1 > time:
            queue.append([now[0], now[1]+1])
            visited[now[0]][now[1]+1] = 1
        if maps[now[0]][now[1]-1] == '1' and visited[now[0]][now[1]-1] == 0 and now[1]-1 > time:
            queue.append([now[0], now[1]-1])
            visited[now[0]][now[1]-1] = 1
        if maps[now[0] ^ 1][now[1]+k] == '1' and visited[now[0] ^ 1][now[1]+k] == 0 and now[1]+k > time:
            queue.append([now[0] ^ 1, now[1]+k])
            visited[now[0] ^ 1][now[1]+k] = 1

    if done == 1: break
    time += 1

print(done)