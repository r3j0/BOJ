import sys
input = sys.stdin.readline

b_y, b_x = map(int, input().rstrip().split())
d_y, d_x = map(int, input().rstrip().split())
j_y, j_x = map(int, input().rstrip().split())

while (not (b_y == j_y and b_x == j_x)) and (not (d_y == j_y and d_x == j_x)):
    # daisy
    if d_y > j_y: d_y -= 1
    elif d_y < j_y: d_y += 1
    else:
        if d_x > j_x: d_x -= 1
        else: d_x += 1

    # bessie
    if b_y > j_y: b_y -= 1
    elif b_y < j_y: b_y += 1
    
    if b_x > j_x: b_x -= 1
    elif b_x < j_x: b_x += 1

if b_y == j_y and b_x == j_x and d_y == j_y and d_x == j_x: print('tie')
elif b_y == j_y and b_x == j_x: print('bessie')
else: print('daisy')