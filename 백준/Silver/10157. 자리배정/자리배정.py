import sys
input = sys.stdin.readline
c, r = map(int, input().rstrip().split())
k = int(input().rstrip())
arr = [[0 for _ in range(c)] for _ in range(r)]
arr[0][0] = 1
row = [1, 0, -1, 0]
col = [0, 1, 0, -1]
dir = 0
now = [0, 0]
now_num = 1
while True:
    arr[now[0]][now[1]] = now_num
    ny = now[0] + row[dir]
    nx = now[1] + col[dir]
    if 0 <= ny < r and 0 <= nx < c and arr[ny][nx] == 0:
        now[0] = ny
        now[1] = nx
    else:
        dir = (dir + 1) % 4
        ny = now[0] + row[dir]
        nx = now[1] + col[dir]
        if arr[ny][nx] != 0:
            break
        else:
            now[0] = ny
            now[1] = nx
    now_num += 1

done = False
for i in range(r): 
    if arr[i].count(k) > 0:
        print(arr[i].index(k)+1, i+1)
        done = True
        break

if done == False: print(0)
        