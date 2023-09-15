import sys
input = sys.stdin.readline

h, m, s = map(int, input().rstrip().split())
t = h * 3600 + m * 60 + s
q = int(input().rstrip())
for _ in range(q):
    order = list(map(int, input().rstrip().split()))
    if order[0] == 2:
        t -= order[1]
        while t < 0: t += 86400
    elif order[0] == 1:
        t = (t + order[1]) % 86400
    else:
        print(t//3600, t%3600//60, t%60)