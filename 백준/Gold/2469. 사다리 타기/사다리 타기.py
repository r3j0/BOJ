import sys
input = sys.stdin.readline

k = int(input().rstrip())
n = int(input().rstrip())
start = []
for i in range(k):
    start.append(chr(ord('A') + i))
end = list(input().rstrip())

lines = [list(input().rstrip()) for _ in range(n)]
mid = 0
for i in range(n):
    if lines[i].count('?') > 0:
        mid = i
        break

# 윗줄 추적
for i in range(mid):
    for garo in range(k - 1):
        if lines[i][garo] == '-':
            start[garo], start[garo + 1] = start[garo + 1], start[garo]

# 아랫줄 역추적
for i in range(n - 1, mid, - 1):
    for garo in range(k - 2, -1, -1):
        if lines[i][garo] == '-':
            end[garo], end[garo + 1] = end[garo + 1], end[garo]

result = []
nstart = [start[i] for i in range(len(start))]
for garo in range(k - 1):
    if start[garo] == end[garo + 1] and start[garo + 1] == end[garo]:
        result.append('-')
        nstart[garo], nstart[garo + 1] = nstart[garo + 1], nstart[garo]
    else:
        result.append('*')

if ((result.count('-') == 0 and start == end) or result.count('-') > 0) and nstart == end: print(''.join(result))
else: print('x'*(k-1))