import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
maps = [list(input().rstrip()) for _ in range(n)]

# Garo
gcnt = 0
for i in range(n):
    if maps[i].count('.') == m: gcnt += 1

# Sero
scnt = 0
for j in range(m):
    jcnt = 0
    for i in range(n):
        if maps[i][j] == '.': jcnt += 1
    
    if jcnt == n: scnt += 1

print(max(gcnt, scnt))