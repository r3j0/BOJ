import sys
input = sys.stdin.readline

n, m, q = map(int, input().rstrip().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]

for _ in range(q):
    order = list(map(int, input().rstrip().split()))
    if order[0] == 0:
        maps[order[1]][order[2]] = order[3]
    else:
        tmp = maps[order[2]]
        maps[order[2]] = maps[order[1]]
        maps[order[1]] = tmp

for i in range(n):
    print(' '.join(map(str, maps[i])))