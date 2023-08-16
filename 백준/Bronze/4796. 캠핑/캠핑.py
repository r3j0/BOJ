import sys
input = sys.stdin.readline

t = 1
while True:
    a, b, c = map(int, input().rstrip().split())
    if a == b == c == 0: break

    print('Case %d: %d'%(t, (c//b)*a + min(a, (c%b))))
    t += 1