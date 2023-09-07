import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n, m = map(int, input().rstrip().split())
    maps = [list(map(int, input().rstrip().split())) for _ in range(n)]
    column = []
    for j in range(m):
        cnt = 0
        for i in range(n):
            if maps[i][j] == 1: cnt += 1
        column.append(cnt)
    
    result = 0
    for j in range(m):
        now = column[j]
        for i in range(n):
            if maps[i][j] == 1:
                result += (n - i) - now
                now -= 1
    
    print(result)