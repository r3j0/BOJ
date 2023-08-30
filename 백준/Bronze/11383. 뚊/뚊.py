import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
first = [list(input().rstrip()) for _ in range(n)]
second = [list(input().rstrip()) for _ in range(n)]

done = 0
for i in range(n):
    if len(first[i]) * 2 != len(second[i]):
        done = 1
        break
    now = ""
    for j in range(0, m*2, 2): now += second[i][j]
    if ''.join(first[i]) != now:
        done = 1
        break
    now = ""
    for j in range(1, m*2, 2): now += second[i][j]
    if ''.join(first[i]) != now:
        done = 1
        break

if done == 1: print('Not Eyfa')
else: print('Eyfa')