import sys
input = sys.stdin.readline

_ = input().rstrip()

cnt = 0
while True:
    now = input().rstrip()
    if now == '고무오리 디버깅 끝': break
    if now == '문제': cnt += 1
    else:
        if cnt == 0: cnt = 2
        else: cnt -= 1

if cnt == 0: print('고무오리야 사랑해') 
else: print('힝구')