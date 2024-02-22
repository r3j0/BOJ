import sys
input = sys.stdin.readline

n = int(input().rstrip())
red = list(map(int, input().rstrip().split()))
blue = list(map(int, input().rstrip().split()))
yellow = list(map(int, input().rstrip().split()))

if red[0] != red[1]:
    red_line = (red[0] + red[1]) / 2
    n = max(n - red_line, red_line)
    blue[0] -= red_line
    if blue[0] < 0: blue[0] *= -1
    blue[1] -= red_line
    if blue[1] < 0: blue[1] *= -1
    yellow[0] -= red_line
    if yellow[0] < 0: yellow[0] *= -1
    yellow[1] -= red_line
    if yellow[1] < 0: yellow[1] *= -1

if blue[0] != blue[1]:
    blue_line = (blue[0] + blue[1]) / 2
    n = max(n - blue_line, blue_line)
    yellow[0] -= blue_line
    if yellow[0] < 0: yellow[0] *= -1
    yellow[1] -= blue_line
    if yellow[1] < 0: yellow[1] *= -1

if yellow[0] != yellow[1]:
    yellow_line = (yellow[0] + yellow[1]) / 2
    n = max(n - yellow_line, yellow_line)

print('%.1f'%(n))