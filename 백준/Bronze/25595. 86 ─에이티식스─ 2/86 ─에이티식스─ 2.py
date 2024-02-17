import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

odd = 0
even = 0
now = 0

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            if (i+j) % 2 == 1: odd += 1
            else: even += 1
        elif arr[i][j] == 2:
            now = (i+j) % 2

if (even == 0 and now == 0) or (odd == 0 and now == 1): print('Lena')
else: print('Kiriya')