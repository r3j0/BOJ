import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    r, c, content = input().rstrip().split()
    r = int(r); c = int(c)
    maps = []
    for i in range(r):
        maps.append(content[i*c:(i+1)*c])
    
    visited = [[0 for _ in range(c)] for _ in range(r)]
    result = ""

    now = [0, 0]

    row = [0, 1, 0, -1]
    col = [1, 0, -1, 0]
    dir = 0
    dircnt = 0

    while True:
        result += maps[now[0]][now[1]]
        visited[now[0]][now[1]] = 1

        done = 0
        dircnt = 0
        while not (0 <= now[0] + row[dir] < r and 0 <= now[1] + col[dir] < c and visited[now[0] + row[dir]][now[1] + col[dir]] == 0):
            dir = (dir + 1) % 4
            dircnt += 1

            if dircnt == 5:
                done = 1
                break
        
        if done == 1: break

        now[0] += row[dir]
        now[1] += col[dir]
    
    answer = ""
    idx = 0
    while idx*5 + 4 <= len(result):
        go = int(result[idx*5:idx*5+5], 2)
        if go == 0: answer += " "
        else: answer += chr(ord('A') + go - 1)
        idx += 1
    
    print(answer.rstrip())