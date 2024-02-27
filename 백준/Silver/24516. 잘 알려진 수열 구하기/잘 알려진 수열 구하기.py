import sys
input = sys.stdin.readline

n = int(input().rstrip())
if n % 2 == 1:
    for i in range(n):
        print(i*2+1, end=' ')
else:
    for i in range(n):
        print((i+1)*2, end=' ')