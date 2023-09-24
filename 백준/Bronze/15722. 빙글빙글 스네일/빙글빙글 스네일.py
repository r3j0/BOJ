import sys
input = sys.stdin.readline

row = [1, 0, -1, 0]
col = [0, 1, 0, -1]

n = int(input().rstrip())
now_y = 0
now_x = 0
now_cnt = 0
now_numcnt = 0
now_num = 1
now_dir = 0
for _ in range(n):
    now_y += row[now_dir]
    now_x += col[now_dir]

    now_cnt += 1
    if now_num == now_cnt:
        now_cnt = 0
        now_numcnt += 1
        if now_numcnt == 2:
            now_num += 1
            now_numcnt = 0
        
        now_dir = (now_dir + 1) % 4

print(now_x, now_y)