import sys
input = sys.stdin.readline

n = int(input().rstrip())
maps = []
for _ in range(n):
    now = [list(input().rstrip()) for _ in range(5)]
    maps.append(now)

result_maps = []
result = 0
result_avail = 0
for m1 in range(n-1):
    for m2 in range(m1+1, n):
        cnt = 0
        for i in range(5):
            for j in range(7):
                if maps[m1][i][j] != maps[m2][i][j]: cnt += 1
        if result_avail == 0 or result > cnt:
            result_avail = 1
            result = cnt
            result_maps = [m1+1, m2+1]

print(' '.join(map(str, result_maps)))