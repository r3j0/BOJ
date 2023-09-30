import sys
input = sys.stdin.readline

a, b, n, w = map(int, input().rstrip().split())
res = []
error = 0
sheep = 1
while sheep * a < w and sheep < n:
    if (w - sheep * a) % b == 0 and sheep + ((w - sheep * a) // b) == n:
        if res != []: error = 1
        else: res = [sheep, (w - sheep * a) // b]
    
    sheep += 1

if res == [] or error == 1: print(-1)
else: print(' '.join(map(str, res)))