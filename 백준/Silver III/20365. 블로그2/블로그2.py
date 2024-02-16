import sys
input = sys.stdin.readline

n = int(input().rstrip())
string = input().rstrip()

red = 0
red_cnt = 0
blue = 0
blue_cnt = 0
for i in range(n):
    if string[i] == 'B':
        if red_cnt != 0:
            red_cnt = 0
            red += 1
        blue_cnt += 1
    else:
        if blue_cnt != 0:
            blue_cnt = 0
            blue += 1
        red_cnt += 1

if red_cnt != 0: red += 1
if blue_cnt != 0: blue += 1

print(min(red, blue) + 1)