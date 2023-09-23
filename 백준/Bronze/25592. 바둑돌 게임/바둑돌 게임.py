import sys
input = sys.stdin.readline

n = int(input())
turn = 1

cnt = 1
now = 2

while cnt <= n:
    cnt += now
    now += 1
    turn = 1 if turn == 2 else 2

if turn == 1: print(cnt - n)
else: print(0)