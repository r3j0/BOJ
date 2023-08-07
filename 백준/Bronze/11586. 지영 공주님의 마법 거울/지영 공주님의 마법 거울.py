import sys
input = sys.stdin.readline

n = int(input().rstrip())
maps = [list(input().rstrip()) for _ in range(n)]
k = int(input().rstrip())

if k == 1:
    for m in maps: 
        print(''.join(m))
elif k == 2:
    for m in maps:
        print(''.join(reversed(m)))
else:
    for i in range(n-1, -1, -1):
        print(''.join(maps[i]))