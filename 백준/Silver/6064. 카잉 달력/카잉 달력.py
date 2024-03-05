import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    m, n, x, y = map(int, input().rstrip().split())
    now = x - 1
    while now % n != y - 1 and now < m * n: now += m
    if now >= m * n: print(-1)
    else: print(now+1)

""" 10 12
1 1
2 2
3 3
4 4
5 5
6 6
7 7
8 8
9 9
10 10
1 11
2 12
3 1 """