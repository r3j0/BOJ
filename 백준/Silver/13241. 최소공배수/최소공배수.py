import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
ma, mb = max(a, b), min(a, b)

while True:
    divs = ma // mb
    mods = ma % mb
    ma = mb
    mb = mods
    if mods == 0: 
        break

print(ma*(a//ma)*(b//ma))