import sys
input = sys.stdin.readline

row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]

t = int(input().rstrip())
for _ in range(t):
    string = input().rstrip()
    now_dir = 0
    now_pos = [0, 0]

    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    for s in string:
        if s == 'F': 
            now_pos[0] += row[now_dir]
            now_pos[1] += col[now_dir]
        elif s == 'B':
            now_pos[0] -= row[now_dir]
            now_pos[1] -= col[now_dir]
        elif s == 'L':
            if now_dir == 0: now_dir = 3
            else: now_dir -= 1
        elif s == 'R':
            now_dir = (now_dir + 1) % 4

        min_x = min(min_x, now_pos[0])
        max_x = max(max_x, now_pos[0])
        min_y = min(min_y, now_pos[1])
        max_y = max(max_y, now_pos[1])
    
    print((max_x - min_x) * (max_y - min_y))