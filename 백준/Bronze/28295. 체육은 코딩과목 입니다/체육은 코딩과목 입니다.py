import sys
input = sys.stdin.readline

dir = ['N', 'E', 'S', 'W']
now = 0
for _ in range(10):
    n = int(input())
    if n == 1: now = (now + 1) % 4
    elif n == 2: now = (now + 2) % 4
    else: now = (now + 3) % 4

print(dir[now])