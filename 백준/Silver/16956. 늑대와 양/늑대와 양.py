import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
maps = [list(input().rstrip()) for _ in range(n)]
row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]
done = 1
for i in range(n):
    for j in range(m):
        if maps[i][j] == 'W':
            for d in range(4):
                ny = i + row[d]
                nx = j + col[d]

                if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == '.':
                    maps[ny][nx] = 'D'
                elif 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 'S':
                    done = 0
                    break
    
    if done == 0: break

print(done)
if done == 1:
    for i in range(n): print(''.join(maps[i])) 